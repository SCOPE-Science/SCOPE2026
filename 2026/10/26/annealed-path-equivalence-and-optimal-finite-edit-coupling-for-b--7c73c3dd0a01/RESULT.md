# Annealed path equivalence and optimal finite-edit coupling for Bernoulli bootstrap walks

## Finding
Let the independently resampled, inclusion-induced Bernoulli bootstrap walk be defined below with parameter \(0<p<1\). Although every fixed-environment (quenched) joint path law is singular to a pair of independent simple walks, the averaged (annealed) joint path law is **equivalent on the complete infinite path space** to a reference consisting of two independent fair walks after their obligatorily shared first step. There is a coupling that changes only finitely many increments almost surely, and its **smallest possible expected number of changes**, among couplings preserving the first walk exactly, is
\[
 B(p)=\frac{|1-2p|}{2}+\sum_{k=1}^{\infty}|1-2p|^{2^k}.
\]
For \(0<|1-2p|<1\), the minimum expected mismatch count after time \(N\) decays as \(2^{-N+o(N)}\). As \(p\) tends to either endpoint,
\[
 B(p)=\log_2\frac{1}{2\min\{p,1-p\}}+O(1).
\]
At \(p=1/2\) the annealed path law equals the reference exactly; at \(p=0,1\) it is singular to that reference.

## Assumptions and scope
Let \((\xi_j)_{j\ge1}\) be independent, equiprobable \(\{-1,1\}\) signs, and let \((\beta_{n,K})_{n\ge1,\ K\subseteq\{1,\ldots,n\}}\) be mutually independent Bernoulli\((p)\) variables, independent of \(\xi\). Define the negative-index set \(\kappa_n=\{i\le n:\xi_i=-1\}\), its size \(M_n=|\kappa_n|\), and
\[
 \zeta_0=1,\qquad \zeta_n=(-1)^{\sum_{K\subseteq\kappa_n}\beta_{n,K}},\qquad \eta_j=\xi_j\zeta_{j-1}.
\]
Write \(P_p\) for the joint law on \(\{-1,1\}^{\mathbb N}\times\{-1,1\}^{\mathbb N}\) of \((\xi,\eta)\) after averaging over all coefficients. Write \(Q\) for the joint law of \((\xi,\widetilde\eta)\), where the same fair sequence \(\xi\) is used, \(\widetilde\eta_1=\xi_1\), and \(\widetilde\eta_j\) for \(j\ge2\) are independent fair signs independent of the entire \(\xi\) sequence. Both laws are considered on the product sigma-field of the **entire infinite increment sequences**, equivalently of the corresponding two walk paths.

An admissible coupling of \(P_p\) and \(Q\) must have identical \(\xi\) sequences in both copies; it need not preserve the coefficient environment. The cost is the total Hamming discrepancy \(\sum_{j\ge2}{\boldsymbol1}\{\eta_j\ne\widetilde\eta_j\}\), which may initially take the value infinity. For a fixed deterministic coefficient array \(\beta\), \(P_p^\beta\) denotes the law of \((\xi,\eta)\) with that array held fixed. The extension to \(p=0,1\) uses the same definitions with degenerate coefficients.

## Proof
**1. Conditional product structure.** Set \(a=1-2p\) and \(r=|a|\). For each \(n\ge1\), exactly \(2^{M_n}\) distinct coefficients occur in the parity defining \(\zeta_n\). Different times \(n\) use disjoint coefficient rows. Consequently, conditional on the entire \(\xi\) sequence, the signs \((\zeta_n)_{n\ge1}\) are independent and
\[
 \mathbb E(\zeta_n\mid\xi)=b_n(\xi):=a^{2^{M_n}},\qquad |b_n|=r^{2^{M_n}}.
\]
This includes \(M_n=0\), where the exponent is one. Under \(Q\), the signs \(\widetilde\zeta_n:=\xi_{n+1}\widetilde\eta_{n+1}\) are iid fair and independent of \(\xi\), and \(\widetilde\eta_1=\xi_1\).

**2. Occupation identity.** For any nonnegative sequence \(f(k)\), the nondecreasing chain \(M_n\), starting at zero, visits each integer level \(k\ge0\) for a geometric number of successive times with success parameter \(1/2\), mean two. Tonelli's theorem gives
\[
 \mathbb E\sum_{n=0}^{\infty}f(M_n)=2\sum_{k=0}^{\infty}f(k).
\]
In particular, subtracting the \(n=0\) summand and taking \(f(k)=r^{2^k}\) or \(r^{2^{k+1}}\), for \(0\le r<1\), yields
\[
 \mathbb E\sum_{n=1}^{\infty}|b_n|=r+2\sum_{k\ge1}r^{2^k}<\infty,
 \qquad
 \mathbb E\sum_{n=1}^{\infty}b_n^2=r^2+2\sum_{k\ge1}r^{2^{k+1}}<\infty.
\]
Thus both series are finite for almost every \(\xi\); the squared-summability estimate alone also suffices for equivalence below.

**3. Complete path-space equivalence.** Fix any \(\xi\) in the full-measure set of Step 2. On the coordinate space of signs \(z_n\), let \(\nu\) be the iid fair product law. The first \(N\) coordinates of the biased conditional law have density
\[
 L_N(z)=\prod_{n=1}^{N}(1+b_nz_n)
\]
relative to \(\nu\). This is a nonnegative martingale with \(\mathbb E_\nu L_N=1\) and \(\sup_N\mathbb E_\nu L_N^2=\prod_n(1+b_n^2)<\infty\). Hence \(L_N\) converges in \(L^1(\nu)\) to a density \(L\). Moreover \(\log L_N=\sum_{n\le N}\log(1+b_nz_n)\) converges to a finite real value \(\nu\)-almost surely: the independent centered summands have summable variances, and their expectations have summable absolute values because \(\sum b_n^2<\infty\) and \(\sup_n|b_n|\le r<1\). Thus \(L>0\), \(\nu\)-almost surely, proving mutual absolute continuity of the conditional products. Integrating this assertion against the **same** marginal law of \(\xi\) proves \(P_p\sim Q\). This proves equivalence of complete infinite paths, not just fixed-dimensional distributions or a diffusion limit.

**4. Optimal coupling.** Given \(\xi\), a sign with mean \(b_n\) differs in total variation from a fair sign by exactly \(|b_n|/2\). Every coupling preserving \(\xi\) therefore obeys
\[
 \mathbb E\!\left[\sum_{j\ge2}{\boldsymbol1}\{\eta_j\ne\widetilde\eta_j\}\,\middle|\,\xi\right]
 \ge\frac12\sum_{n\ge1}|b_n|.
\]
For the reverse inequality, draw independent uniform variables \((U_n)\), independent of \(\xi\). For each \(n\), obtain \(\zeta_n\) and \(\widetilde\zeta_n\) by thresholding the same \(U_n\) at \((1+b_n)/2\) and \(1/2\). Conditional on \(\xi\), each of the two sign sequences has its required independent-coordinate law, and disagreement probability is \(|b_n|/2\) for every coordinate. Set \(\eta_{n+1}=\xi_{n+1}\zeta_n\) and \(\widetilde\eta_{n+1}=\xi_{n+1}\widetilde\zeta_n\), with the first increments equal to \(\xi_1\). This is an admissible coupling attaining the lower bound, and its total mismatch count is finite almost surely by Step 2. Taking expectations and applying the exact occupation identity yields precisely \(B(p)\).

**5. Temporal tail and endpoint behavior.** For \(n\ge1\), the count \(M_n\) is binomial with parameters \((n,1/2)\), whence
\[
 \mathbb E[r^{2^{M_n}}]=2^{-n}\sum_{k=0}^n\binom nk r^{2^k}.
\]
For every fixed \(0<r<1\), the sum is at least \(r\). It is at most \(\exp(O((\log n)^2))\): split at \(k=\lceil2\log_2 n\rceil\), use \(\binom nk\le n^k\) below the split, and bound the upper sum by \(2^n\exp(-c n^2)\), with \(c=-\log r>0\). Therefore the minimum expected number of mismatches with indices \(j\ge N+1\) is
\[
 B_N=\frac12\sum_{n\ge N}\mathbb E[r^{2^{M_n}}]=2^{-N+o(N)}.
\]
Finally let \(t=-\log r\downarrow0\). The lacunary series \(\sum_{k\ge1}e^{-t2^k}\) differs from \(\log_2(1/t)\) by a uniformly bounded amount: below \(k=\lfloor\log_2(1/t)\rfloor\), the total deficit from one is at most \(\sum t2^k=O(1)\); above that threshold, the remaining sum is bounded by a convergent superexponential series. Since \(t\sim1-r=2\min\{p,1-p\}\), the claimed endpoint law follows.

**6. Boundary and quenched singularity.** For any fixed \(\beta\), the sequence \(\eta\) is a deterministic measurable function of \(\xi\). The corresponding graph has \(Q\)-measure zero, since conditional on \(\xi\) the infinitely many reference signs \(\widetilde\eta_j\), \(j\ge2\), are independent fair. Hence \(P_p^\beta\perp Q\) for every coefficient array. For \(p=0\), all \(\zeta_n=1\), so the two walks agree forever. For \(p=1\), all \(\zeta_n=1\) once the first negative increment has occurred, almost surely at a finite time. In either endpoint case, the two increment sequences agree eventually \(P_p\)-almost surely but \(Q\)-almost never, proving singularity. At \(p=1/2\), \(b_n=0\) for all \(n\ge1\), so \(P_{1/2}=Q\) exactly.

## Verification
The standalone \(\texttt{CHECK.py}\) performs 64 exact-rational checks: binomial occupancy moments at twelve finite horizons for four rational biases, equivalent finite-horizon occupation decompositions, and parity enumeration of up to eight Bernoulli coefficients. These checks test the finite identities used in the proof; they do not substitute for the infinite-product, optimal-coupling or asymptotic arguments proved above. Running \(\texttt{python CHECK.py}\) prints a passing count of 64.

## Relationship to prior work
Hamza and Tournier (2026), Section 3 under assumption (G1), define exactly this inclusion-induced random coefficient model and prove quenched and annealed **functional central limit theorems** (their Theorem 2 and Corollary 3). Their Appendix B, Lemma 19, supplies a related subexponential binomial-sum bound; that estimate is not claimed as novel here. Neither those Brownian limits nor the prior deterministic-bootstrap limit and ergodicity theory identify annealed equivalence on infinite path space, the optimal expected number of mismatches in a coupling fixing the original walk, or the quenched/annealed path singularity distinction. The deterministic construction of Collevecchio, Hamza and Shi (2015) was also checked and concerns weak limits, not independent Bernoulli coefficient rows. Product-measure equivalence criteria and maximal coupling are standard tools; the model-specific sharp occupation formula and phase boundary are the content of this finding.

## Limitations
The assertion is specific to the independent-across-\(n\), independent-within-\(n\), constant-parameter (G1) coefficient model, **not** the paper's broader dependent-coefficient (G) model, and not the n-invariant (G2) model. The coupling preserves the original walk but generally does not preserve the sampled coefficient environment. Its exponential tail concerns the **expected number of optimal-coupling discrepancies**, not necessarily the total-variation distance between unrestricted path laws, nor a finite-time mixing time. Literature equivalence under alternative product-measure or finitary-coupling terminology remains a priority risk; no claim of independent external audit is made.

## References
- A. Collevecchio, K. Hamza and M. Shi, *Bootstrap Random Walks*, arXiv:1508.02840v2 (2015), Sections 1–5. https://arxiv.org/html/1508.02840v2
- K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1 (public 2026-10-01), Sections 2–3 and Appendix B. https://arxiv.org/html/2610.01658v1
- A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, arXiv:2010.16000 (2020; revised 2021), Sections 1–3 and 5. https://arxiv.org/html/2010.16000v2
