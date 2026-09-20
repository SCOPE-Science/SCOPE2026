# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The fixed-parameter refinement follows from a strict containment that is already implicit in Leonetti's proof. His sets satisfy
\(G_m+G_m\subseteq\Gamma_m\) and
\(F_m+G_m\subseteq\Gamma_m\cup\bigcup_j\Gamma_{m,j}\), while
\(\Gamma_m\subseteq\Gamma_{m,j}\) for every \(j\). Thus only the union of the \(r\) one-coordinate-deleted CRT constraints is needed. In one full CRT period this union is exactly the event that at least \(r-1\) of the \(r\) coordinate conditions hold, giving the exact density
\[
\prod_i\eta_i+\sum_j(1-\eta_j)\prod_{i\ne j}\eta_i.
\]
Since \(\eta_i\to2\delta\), the limiting bound is
\(r(2\delta)^{r-1}-(r-1)(2\delta)^r\). The endpoint-period error is controlled by the same \(Q_m/x_{m+1}\to0\) estimate used in the source proof.

The optimization corollary was rederived independently from the refined formula. With \(L=\log(1/\alpha)\) and \(a=\log2\), minimizing
\((r-1)a+L/r+\log r+o(1)\) gives
\(r\sim\sqrt{L/a}\) and the stated multiplicative envelope. Kneser's bound gives the matching logarithmic exponent from below. Exact finite CRT enumeration and numerical optimization in the artifact agree with the formulas.

Stress tests considered the cases \(r=2\), unequal finite coordinate densities \(\eta_i\), incomplete CRT periods, and the admissibility condition \(\alpha^{1/r}<1/4\). None changes the limit argument. The result does not claim equality for the extremal profile or a sharp multiplicative constant.

## Originality

**PASS, to the best of our knowledge.** The full proof of Leonetti's arXiv:2609.20206 was inspected. Theorem 1.2 states
\(d_*(A+A)\le(r+1)(2\delta)^{r-1}\), and the proof obtains this by separately summing the contribution of \(\Gamma_m\) and the \(r\) sets \(\Gamma_{m,j}\). The inspected version does not collapse the redundant \(\Gamma_m\) term into the union, count that union exactly, define the extremal profile \(\Lambda(\alpha)\), or optimize over \(r\) to obtain the small-density envelope.

Bienvenu's arXiv:2502.09438 / J. Number Theory 281 (2026) was inspected for its density-profile statements and three-dimensional projection context. It gives broad realizability regions for lower/upper densities of \(A\) and \(2A\), but no statement located there implies the fixed-parameter refinement or the asymptotic envelope recorded here. Hegyvári--Hennecart--Pach arXiv:1902.02512 was checked as the earlier source of the density question. Exact and synonymous searches for the refined coefficient, the CRT "at least r-1 coordinates" count, and the small-\(\alpha\) extremal profile found no matching theorem.

The principal inaccessible-source risk is an unpublished manuscript of I. Z. Ruzsa cited by Leonetti, with no public identifier located. Leonetti reports that it showed a necessary condition \(\nu\ge1/2\) if the earlier interpolation inequality were true. Its full contents were not inspected, so an undocumented overlap cannot be ruled out. The motivating preprint is also recent enough that unindexed contemporaneous work remains possible.

## Value

**PASS.** The first theorem strictly improves the quantitative conclusion of a recent construction for every allowed \((r,\delta)\), by replacing a union bound with the exact CRT union density. More importantly, parameter optimization turns that refinement into a global description of the small-source-density regime: if the upper density of \(A+A\) is forced to be one, the minimal possible lower density is \(\alpha^{1-o(1)}\), and the construction supplies an explicit subexponential envelope multiplying \(\alpha\). This isolates the remaining gap to Kneser's universal lower bound \(2\alpha\) and gives a concrete target for future sharpening.

No independent validation, formal verification, or expert review is asserted.
