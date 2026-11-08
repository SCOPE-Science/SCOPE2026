# A logarithmic defect crossover between star and full fair coupon sampling

## Finding

Let \(m\) tend to infinity through positive integers, let \(c=c_m\) be integers with \(1\le c<m\), set \(k=m-c\), and write
\[
\delta_m=c-\log m+\tfrac12\log\log m.
\]
Assume \(\delta_m=o(\log m)\) and \(c/\log m\to1\). The coupon universe is the family \(\binom{[m]}{k}\) of all \(k\)-subsets. In the *star* mechanism each independent round chooses a uniform center \(i\in[m]\) and reveals all \(k\)-subsets containing \(i\); in the *full* mechanism each independent round reveals a uniformly selected collection of exactly \(\binom{m-1}{k-1}\) different coupons, sampled from the \(\binom mk\) coupon types. Both mechanisms are fair and reveal the same number of coupons per round.

Let \(T_\star\) and \(T_{\mathrm{full}}\) be their respective first full-coverage times. Define \(U_t\) as the number of as-yet-uncovered coupon types after \(t\) full-mechanism rounds. If \(\delta_m\to x\in\mathbb R\), put \(\Lambda_x=e^x/\sqrt{2\pi}\). Then
\[
U_{c+1}\ \Longrightarrow\ \mathrm{Poisson}(\Lambda_x),\qquad
T_{\mathrm{full}}-(c+1)\ \Longrightarrow\ \mathrm{Bernoulli}(1-e^{-\Lambda_x}),
\]
\[
T_\star-(c+1)\ \xrightarrow{\mathsf P}\ 0,\qquad
\mathbb ET_{\mathrm{full}}-\mathbb ET_\star\ \longrightarrow\ 1-e^{-\Lambda_x}.
\]
In fact the last two displays admit the sharp boundary limits \(\delta_m\to-\infty\) or \(\delta_m\to+\infty\), still with \(\delta_m=o(\log m)\): replace \(1-e^{-\Lambda_x}\) by \(0\) or \(1\), respectively. In these extreme cases the full-mechanism centered time converges in probability to the corresponding constant.

## Assumptions and scope

All logarithms are natural; all round choices are independent over time and uniform on the specified draw families. The integer sequence \(c\) is allowed to change with \(m\) and satisfies \(c\sim\log m\). The real-window hypothesis implies this automatically, while the stated two-sided extreme extensions assume it explicitly. In a finite critical window \(x\in\mathbb R\), \(\Lambda_x\) is positive and finite. The difference between expectations concerns two distinct probability laws and requires no coupling. The parameters \(m,c,k\) are deterministic. No conclusion is asserted for arbitrary defect scales outside the stated window.

The problem is combinatorial probability (primary MSC2020 60C05). Its motivation is that the fixed-defect case of the fair star-versus-full comparison has the opposite, small expectation ordering. The theorem detects the previously unresolved transition when the defect diverges logarithmically.

## Proof

**1. Missing-coupon representation.** Put
\[
N=\binom{m}{c},\qquad M=\binom{m-1}{c-1},\qquad q=M/N=c/m.
\]
In every full-mechanism round the set of *missed* coupon labels is a uniformly random \(M\)-subset of the \(N\)-element coupon universe, independently between rounds. For every fixed integer \(r\ge1\), the falling-factorial moments of the number \(U_t\) missed in all of the first \(t\) rounds satisfy the exact identity
\[
\mathbb E(U_t)_{\underline r}=(N)_{\underline r}\left(\frac{(M)_{\underline r}}{(N)_{\underline r}}\right)^t,
\]
with the usual interpretation that it is zero if \(r>M\) and \(t\ge1\). In particular \(\mu_t=\mathbb EU_t=Nq^t\). Because distinct labels are negatively correlated for being omitted in a single draw,
\[
\operatorname{Var}(U_t)\le \mathbb EU_t=\mu_t
\]
for every integer \(t\ge1\): specifically, \(\Pr(i,j\text{ both missed})=[M(M-1)/(N(N-1))]^t\le q^{2t}\).

**2. Critical Poisson parameter.** For \(c\sim\log m\), elementary product expansion and Stirling give
\[
\begin{aligned}
\log\mu_{c+1}
&=\log\binom mc+(c+1)\log(c/m)\\
&=c-\log m+\tfrac12\log c-\tfrac12\log(2\pi)+O(c^2/m+1/c)\\
&=\delta_m-\tfrac12\log(2\pi)+o(1).
\end{aligned}
\]
The last equality follows since \(c/\log m\to1\). Hence when \(\delta_m\to x\in\mathbb R\), the mean \(\mu_{c+1}\to\Lambda_x\). The quantities \(N,M\) tend to infinity much faster than \(c\). Thus for every fixed \(r\), with \(t=c+1\),
\[
\mathbb E(U_t)_{\underline r}
=\mu_t^r\left(1+O_r(t/M+t/N+1/N)\right)
\longrightarrow \Lambda_x^r.
\]
The standard factorial-moment criterion for nonnegative integer random variables establishes \(U_{c+1}\Rightarrow\mathrm{Poisson}(\Lambda_x)\).

**3. Only two possible limiting rounds.** Since \(\mu_c=\mu_{c+1}/q\) and \(\mu_{c+2}=q\mu_{c+1}\), in the finite window \(\mu_c\to\infty\), \(\mu_{c+2}\to0\). The variance bound and Chebyshev give \(\Pr(U_c=0)\le1/\mu_c\to0\). Markov gives \(\Pr(U_{c+2}>0)\le\mu_{c+2}\to0\). As \(\{T_{\mathrm{full}}\le t\}=\{U_t=0\}\), the Poisson limit yields
\[
\Pr(T_{\mathrm{full}}=c+1)\to e^{-\Lambda_x},\qquad
\Pr(T_{\mathrm{full}}=c+2)\to1-e^{-\Lambda_x}.
\]

**4. Mean convergence, not merely weak convergence.** For any finite parameters, the tail sum formula and monotonicity give
\[
\begin{aligned}
\left|\mathbb ET_{\mathrm{full}}-(c+1)-\Pr(T_{\mathrm{full}}>c+1)\right|
&\le (c+1)\Pr(U_c=0)+\sum_{t=c+2}^\infty\Pr(U_t>0)\\
&\le (c+1)/\mu_c+\mu_{c+1}\,q/(1-q).
\end{aligned}
\]
Both terms tend to zero, giving \(\mathbb ET_{\mathrm{full}}-(c+1)\to1-e^{-\Lambda_x}\).

**5. Star limit.** The star mechanism completes exactly when \(c+1\) distinct centers have been selected. Thus \(T_\star\ge c+1\), while the probability that a repetition occurs among the first \(c+1\) uniform centers is at most \(c(c+1)/(2m)=o(1)\). Moreover independent geometric waiting times for successive new centers give
\[
\mathbb ET_\star=m\sum_{j=m-c}^{m}\frac1j=c+1+O(c^2/m).
\]
This proves both the star convergence and the expectation difference.

**6. One-sided boundary regimes.** If \(\delta_m\to-\infty\), still \(o(\log m)\), the logarithmic estimate in step 2 yields \(\mu_{c+1}\to0\) and \(\mu_c=\mu_{c+1}m/c\to\infty\). The same Chebyshev/Markov and mean-tail bounds imply \(T_{\mathrm{full}}-(c+1)\to0\) in probability and in mean. If \(\delta_m\to+\infty\), still \(o(\log m)\), then \(\mu_{c+1}\to\infty\) and \(\mu_{c+2}\to0\). Applying the variance bound at time \(c+1\) gives \(\Pr(U_{c+1}=0)\to0\), and the same bounds imply \(T_{\mathrm{full}}-(c+1)\to1\) in probability and in mean. Combining with step 5 proves the two boundary statements.

## Verification

The attached standard-library script `verify.py` exhaustively compares the exact falling-factorial moment formula with enumerations of independent missed sets in small universes. It also checks the star expectation identity as exact fractions and assesses the Stirling-scale parameter numerically on explicit large finite instances. The script prints `PASS 131 finite checks` when run with Python 3. These finite checks test the formulas but do not establish the infinite assertions; the proof is in steps 1–6 above.

## Relationship to prior work

Barak-Pelleg and Berend (2026) introduce the fair star mechanism, give its exact expectation, and compare it with uniform full sampling in the fixed-defect case \(k=m-c\) for each fixed \(c\ge2\). They show that the star mechanism is then asymptotically slower in expectation, while it is faster when \(k\) is a fixed proportion of \(m\). Their concluding remarks ask for finer structural comparisons. The new theorem isolates an intermediate regime \(c\sim\log m\), identifies its exact logarithmic centering and two-point distribution, and quantifies an expectation reversal of order one.

Berend and Sher (2026) obtain Poisson uncovered-coupon counts and two-point cover-time limits for full group draws when the critical number of rounds is a *fixed* integer. Their results supply the finite-round analogy but do not assert a uniform theorem when the critical time \(c+1\) grows. The growing-time factorial-moment bounds above, plus the star comparison, supply that missing link. Berend and Sher (2025/2026) also analyze group-draw expectation inequalities but not this intermediate logarithmic star/full comparison. Falgas-Ravry, Larsson and Markström (2020) establish general concentration criteria and relative-scale bounds for structured covering times. Their inspected results do not give the order-one two-round transition or this explicit star/full expectation comparison.

## Limitations

This is a result for the explicitly defined star and uniform full fair mechanisms with \(c\sim\log m\), not an extremality theorem across all fair mechanisms. The self-review is not independent validation; historical priority is provisional. Earlier general uniform-group-drawing Poisson approximation theorems might cover parts of the full-model calculation through reductions. A finite checker cannot certify the analytic limit, and no numerical convergence rate or claim outside the specified logarithmic window is established.

## References

1. D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216, first posted 26 June 2026. https://arxiv.org/html/2606.28216
2. D. Berend and T. Sher, *Asymptotic Results for Uniform Group Drawing in the Coupon Collector's Problem*, arXiv:2605.06953, first posted 7 May 2026. https://arxiv.org/html/2605.06953v1
3. D. Berend and T. Sher, *On a Conjecture on Uniform Group Drawings in the Coupon Collector Problem*, arXiv:2509.17201, first posted 21 September 2025. https://arxiv.org/html/2509.17201v2
4. O. Falgas-Ravry et al., *Speed and concentration of the covering time for structured coupon collectors*, *Advances in Applied Probability* 52 (2020), 433–462. https://doi.org/10.1017/apr.2020.5
