# Exact complete-null FDR of Knockoff+ at reciprocal levels
## Finding
Consider the Knockoff+ rule at nominal level \(q=1/r\), where \(r\ge 2\) is an integer. Assume all \(p\) hypotheses are null and, conditional on the nonzero distinct magnitudes \((|W_1|,\ldots,|W_p|)\), the signs are independent fair coin flips, as in the exact knockoff sign-flip property. Order the statistics by decreasing magnitude and let \(\tau\) be the first prefix at which Knockoff+ can reject.

Then the false discovery rate equals the probability of making any rejection, and it has the exact finite-\(p\) formula
\[
\operatorname{FDR}_{p,r}
=
\sum_{d=0}^{\left\lfloor (p-r)/(r+1)\right\rfloor}
\frac{r}{(r+1)d+r}
\binom{(r+1)d+r}{d}
2^{-((r+1)d+r)},
\]
with the sum interpreted as zero when \(p<r\). The sequence is nondecreasing in \(p\) and converges to
\[
\operatorname{FDR}_{\infty,r}=f_r^r,
\]
where \(f_r\in(1/2,1)\) is the smaller root of
\[
2f=1+f^{r+1}.
\]
Equivalently, if \(\lambda_r=1/f_r>1\), then \(\lambda_r+\lambda_r^{-r}=2\) and \(\operatorname{FDR}_{\infty,r}=\lambda_r^{-r}\).

For \(q=1/2\), this gives the closed form
\[
\operatorname{FDR}_{\infty,2}=\frac{3-\sqrt5}{2}=0.381966011250105\ldots.
\]
For the practically common level \(q=0.1\), corresponding to \(r=10\),
\[
f_{10}=0.500245462266794\ldots,
\qquad
\operatorname{FDR}_{\infty,10}=0.000981367289898861\ldots.
\]
Thus, under the complete null with exact fair knockoff signs, the usual Knockoff+ guarantee can be vastly conservative: at nominal level \(0.1\), even infinitely many distinct nonzero statistics have complete-null FDR below \(0.001\).

## Assumptions and scope
All hypotheses are null. Conditional on the magnitudes, all signs are iid Rademacher variables, and the nonzero magnitudes are distinct so that decreasing thresholds expose the statistics one at a time. These conditions hold for continuous valid knockoff statistics under the standard sign-flip lemma. The result concerns the probability of any Knockoff+ rejection under the complete null; it does not describe power, mixed null/non-null configurations, ties, approximate knockoffs, or settings in which the conditional sign-flip property fails.

## Proof
After sorting by decreasing \(|W_j|\), let \(P_k\) and \(N_k\) be the positive- and negative-sign counts in the first \(k\) positions. At level \(q=1/r\), the Knockoff+ inequality is
\[
\frac{1+N_k}{P_k}\le \frac1r,
\]
which is equivalent to
\[
P_k-rN_k\ge r.
\]
Define the random walk \(S_k=P_k-rN_k\). Each new sign gives increment \(+1\) or \(-r\), independently with probability \(1/2\). Since upward jumps are exactly one, the threshold is crossed if and only if the walk first hits the level \(r\). Under the complete null every nonempty rejection set has false discovery proportion one, so the FDR is precisely this hitting probability by time \(p\).

Let \(F(z)\) be the defective probability generating function for the time needed by this walk, starting from zero, to hit level one. A first-step decomposition gives
\[
F(z)=\frac z2\left(1+F(z)^{r+1}\right).
\]
Indeed, a first \(+1\) step succeeds immediately; after a first \(-r\) step, spatial homogeneity and the strong Markov property decompose the climb from \(-r\) to \(+1\) into \(r+1\) successive one-level passages. Hitting level \(r\) similarly has generating function \(F(z)^r\).

Lagrange inversion applied to \(F=z(1+F^{r+1})/2\) gives
\[
[z^n]F(z)^r
=
\frac rn 2^{-n}[u^{n-r}](1+u^{r+1})^n.
\]
The coefficient vanishes unless \(n=(r+1)d+r\); in that case it equals
\[
\frac{r}{(r+1)d+r}
\binom{(r+1)d+r}{d}
2^{-((r+1)d+r)}.
\]
Summing the first-passage probabilities up to \(p\) yields the finite formula.

At \(z=1\), the defective one-level hitting probability is the smaller solution \(f_r\in(1/2,1)\) of \(2f=1+f^{r+1}\). The strong Markov factorization then gives the eventual level-\(r\) hitting probability \(f_r^r\). Monotonicity in \(p\) follows because the finite-horizon hitting events are nested.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to compare the closed formula with a state-by-state random-walk dynamic program for every \(2\le r\le12\) and every horizon through \(150\). It also exhaustively checks, for short sign strings, that the Knockoff+ prefix inequality is exactly the level-hitting event. High-precision bisection verifies the displayed limiting constants. A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Candès, Fan, Janson, and Lv establish that, conditional on magnitudes, null knockoff signs are iid fair coin flips and that adding one to the negative count yields finite-sample Knockoff+ FDR control. Their theorem gives the bound \(\operatorname{FDR}\le q\), not the complete-null finite-horizon law above. Rajchert and Keich study whether the additive \(+1\) correction can be reduced in competition-based FDR control; their focus is necessity of the correction in broader configurations rather than the exact FDR attained by the original \(+1\) rule under the complete null. Ren and Barber reinterpret knockoffs through e-values and stopping times, but the inspected material does not state this Fuss-Catalan first-passage law or its reciprocal-level limit.

The derivation identifies a simple structural reason for strong complete-null conservatism: at \(q=1/r\), the signed prefix process must climb \(r\) levels against a negative-drift \(+1/-r\) walk before any rejection can occur.

## Limitations
The exact formula uses reciprocal integer levels and distinct nonzero magnitudes. General nominal levels lead to a staircase boundary rather than this single skip-free hitting level. Ties require a grouped-threshold analysis. The literature comparison cannot rule out an older equivalent result stated purely as a ballot, target-decoy, or random-walk identity; the mathematical first-passage coefficients themselves are classical consequences of Lagrange inversion, while the claim here is their exact identification with complete-null Knockoff+ FDR.

## References
1. Emmanuel Candès, Yingying Fan, Lucas Janson, Jinchi Lv, “Panning for Gold: Model-X Knockoffs for High-dimensional Controlled Variable Selection,” arXiv:1610.02351, first submitted 2016-10-07; Journal of the Royal Statistical Society Series B 80 (2018), 551–577.
2. Andrew Rajchert, Uri Keich, “Controlling the False Discovery Rate via Competition: is the +1 needed?”, arXiv:2204.13248, first submitted 2022-04-28; Statistics & Probability Letters 197 (2023), 109819.
3. Zhimei Ren, Rina Foygel Barber, “Derandomised knockoffs: leveraging e-values for false discovery rate control,” Journal of the Royal Statistical Society Series B 86 (2024), 122–154, DOI: 10.1093/jrsssb/qkad085.
