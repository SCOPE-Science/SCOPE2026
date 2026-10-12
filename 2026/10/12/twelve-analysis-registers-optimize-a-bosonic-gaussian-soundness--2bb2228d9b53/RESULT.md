# Twelve analysis registers optimize a bosonic Gaussian soundness certificate
## Finding
Let \\(\\mathcal G_b\\) be the class of pure bosonic Gaussian states and let \\(q(\\psi)\\) be the rejection probability of the three-copy general bosonic Gaussian base test of Iyer, O'Gorman, Parekh, Thompson, and Zhao. Their Lemma 6.12 gives, for every integer \\(m\\ge 3\\), the spectral-gap lower bound
\\[
c_m=\\frac{2m}{3(m-1)(m-2)}
\\]
for the \\(m\\)-register symmetrized Reynolds operator associated with the three-copy projector. Combining this general bound with their Theorem 3.5 is feasible exactly for integers \\(m\\ge 7\\), and for every such \\(m\\) yields
\\[
q(\\psi)\\ge \\alpha_m\\operatorname{dist}(\\psi,\\mathcal G_b)^2,
\\qquad
\\alpha_m=\\frac{2(m-6)}{3(m^2-4)}.
\\]
The coefficient \\(\\alpha_m\\) has a unique integer maximum at \\(m=12\\), where
\\[
\\alpha_{12}=\\frac1{35}.
\\]
Thus the tolerant-testing theorem in the same paper can use
\\[
\\beta_{12}=\\sqrt{\\frac{3}{\\alpha_{12}}}=\\sqrt{105},
\\]
in place of the paper's displayed \\(m=7\\) certificate \\(\\alpha_7=2/135\\) and \\(\\beta_7=\\sqrt{405/2}\\). The lower-bound coefficient improves by a factor \\(27/14\\), while the admissible tolerance multiplier is reduced by the factor \\(\\sqrt{14/27}\\approx0.72008\\). The operational base test still acts on three copies; \\(m\\) is an auxiliary symmetrization size used in the soundness analysis.

## Assumptions and scope
The statement uses exactly the three-copy general bosonic Gaussian acceptance projector and the general symmetrized spectral-gap inequality proved in arXiv:2609.39113v1. It assumes the correspondence used in Section 6 of that paper between the symmetrized three-copy projector on \\(m\\) analysis registers and the average of the relevant \\(O(W_{m,I})\\) Reynolds projectors over three-element subsets \\(I\\). Theorem 3.5 is applied with \\(k=3\\) and with the guaranteed gap \\(\\Delta=c_m\\), not with an asserted exact gap.

The claim is only about the best coefficient guaranteed by this particular published lower bound. It does not assert that \\(c_m\\) is the exact spectral gap for \\(m\\ne7\\), that \\(m=12\\) is optimal for every possible proof, or that \\(\\sqrt{105}\\) is the information-theoretically optimal tolerant-separation constant.

## Proof
For \\(k=3\\), Theorem 3.5 requires
\\[
\\frac{6}{m(m-1)}<\\Delta.
\\]
Substituting the Lemma 6.12 guarantee \\(\\Delta=c_m\\) gives
\\[
\\frac{6}{m(m-1)}<\\frac{2m}{3(m-1)(m-2)}.
\\]
For integer \\(m>3\\), all denominators are positive, and this is equivalent to
\\[
m^2-9m+18=(m-3)(m-6)>0.
\\]
Hence the sufficient route becomes feasible exactly at \\(m=7\\).

The nontrivial branch of the coefficient in Theorem 3.5 is
\\[
\\frac{m(m-1)c_m-6}{(m-3)(m+2)}.
\\]
Using \\(c_m=2m/[3(m-1)(m-2)]\\), its numerator is
\\[
\\frac{2m^2}{3(m-2)}-6
=\\frac{2(m-3)(m-6)}{3(m-2)}.
\\]
After cancelling \\(m-3\\), this becomes
\\[
a_m=\\frac{2(m-6)}{3(m-2)(m+2)}
=\\frac{2(m-6)}{3(m^2-4)}.
\\]
The discrete difference is
\\[
a_{m+1}-a_m
=\\frac{2(-m^2+11m+2)}{3(m^2-4)(m^2+2m-3)}.
\\]
The denominator is positive for \\(m\\ge7\\). The positive root of \\(-m^2+11m+2\\) is \\((11+\\sqrt{129})/2\\), which lies strictly between \\(11\\) and \\(12\\). Therefore \\(a_m\\) is strictly increasing for \\(7\\le m\\le12\\) and strictly decreasing for \\(m\\ge12\\). Its unique maximum is
\\[
a_{12}=\\frac{12}{420}=\\frac1{35}<\\frac12.
\\]
Thus the \\(1/2\\) truncation in Theorem 3.5 is inactive for every feasible integer \\(m\\), and \\(\\alpha_m=a_m\\).

The theorem's universal upper coefficient for a three-copy test is \\(\\alpha_1=3\\). Theorem 3.6 therefore gives the admissible tolerant ratio
\\[
\\beta_m=\\sqrt{\\frac{3}{\\alpha_m}}.
\\]
At \\(m=12\\), \\(\\beta_{12}=\\sqrt{105}\\). At \\(m=7\\), \\(\\alpha_7=2/135\\) and hence \\(\\beta_7=\\sqrt{405/2}\\), exactly the value displayed in Theorem 6.1 of the source.

## Verification
The algebra above was replayed with exact rational arithmetic in `artifacts/verify.py`. The script checks the feasibility threshold, the closed form for \\(\\alpha_m\\), the sign formula for the discrete difference, the values \\(\\alpha_7=2/135\\) and \\(\\alpha_{12}=1/35\\), and the improvement factors. Its finite range check is corroborative only; the infinite-domain uniqueness statement follows from the exact sign analysis of the quadratic numerator.

The source text was inspected at Theorem 3.5, Theorem 3.6, Theorem 6.1, Lemma 6.12, and the proof of Theorem 6.1. The paper explicitly says that the added \\(m-k\\) registers are introduced for analysis, while the bosonic base tester itself acts on three copies.

## Relationship to prior work
Iyer et al., arXiv:2609.39113v1, prove the general spectral-gap-to-soundness theorem, the tolerant-testing conversion, the general bound \\(c_m\\), and instantiate the general bosonic argument at \\(m=7\\), obtaining \\(\\alpha=2/135\\) and \\(\\beta=\\sqrt{405/2}\\). The present result keeps their general \\(m\\)-dependent Lemma 6.12 instead of fixing \\(m=7\\), and exactly optimizes the resulting sufficient certificate.

Girardi et al., arXiv:2510.07305v1, introduced closely related three-copy rotation-invariance tests and polynomial-copy tolerant Gaussianity testing, but does not contain the later symmetrized-gap certificate being optimized here. Chen et al., arXiv:2607.11847v1, concern tomography of bosonic and fermionic Gaussian states rather than this three-copy property-test soundness constant.

Published-result searches for the exact source identifier, twelve-register formulation, \\(1/35\\) coefficient, \\(\\sqrt{105}\\) tolerance multiplier, and the general \\(c_m\\) expression returned no implication-equivalent result. The closest retrieved records concerned unrelated classical Gaussianization or Gaussian extremal problems.

## Limitations
The result is a sharp optimization of a sufficient analytical certificate, not a computation of the exact \\(m\\)-register spectral gap. A stronger gap estimate could change the best certified \\(m\\) or lower the tolerant multiplier further. The result also does not improve the asymptotic \\(\\Theta(1/\\varepsilon^2)\\) copy complexity, which is already optimal in the source; it improves the explicit tolerant-separation constant supplied by this proof route.

A contemporaneous or differently phrased result not indexed by the searched literature systems could overlap with the same constant optimization. No such statement was found in the inspected primary papers.

## References
1. V. Iyer, B. O'Gorman, O. Parekh, K. Thompson, A. Zhao, *Optimal testing of fermionic and bosonic Gaussian states*, arXiv:2609.39113v1, 2026. Theorem 3.5, Theorem 3.6, Theorem 6.1, Lemma 6.12, Section 6.3.
2. F. Girardi, F. Witteveen, F. A. Mele, L. Bittel, S. F. E. Oliviero, D. Gross, M. Walter, *Is it Gaussian? Testing bosonic quantum states*, arXiv:2510.07305v1, 2025.
3. S. Chen, M. Fanizza, F. Girardi, L. Lami, F. A. Mele, M. Walter, F. Witteveen, *Optimal tomography of bosonic and fermionic Gaussian states*, arXiv:2607.11847v1, 2026.
