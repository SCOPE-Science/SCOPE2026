# Self-review

## Correctness — PASS

For \(0<\mu<1\), the arctangent denominator is strictly positive. The fixed-point formula gives \(q_\mu=(\arcsin\mu/\pi,0)\); differentiating the deformation and substituting this point cancels the entire perturbation to the cat derivative. At \(\mu=0\), the lifted primitive-two equations have Jacobian determinant \(5\), so the analytic implicit-function theorem gives two distinct analytically continued cycles. Their first displacements follow by solving the displayed linear system, and direct multiplication of the two branch Jacobians gives the exact trace formula. Inserting the uniform Taylor expansion yields the coefficients \((25-7\sqrt5)/2\) and \((25+7\sqrt5)/2\). Both are positive, hence their traces differ from the cat-map period-two trace \(7\) for all sufficiently small positive \(\mu\). The standard differentiable-conjugacy derivative identity supplies the final obstruction. The supporting numerical script ran successfully, but cannot certify the universal result by itself.

## Originality — PASS within inspected evidence

The foundational map and its fixed-point, trace, hyperbolicity and topological-conjugacy results are known from [1] and not claimed anew. The inspected source discusses generic fixed-point nonconjugacy but its own exact trace formula admits the exceptional curve \(\cos\alpha=-\mu\), where the fixed-point matrix is unaltered. The two explicit period-two quadratic coefficients and their difference were not found in the source. The related rational-Anosov resonance paper [2] treats operator and periodic multipliers from a different perspective; no matching real two-cycle perturbation formula was found in the relevant full text. The recent Blaschke-deformation paper [3] proves non-\(C^1\)-conjugacy for a different toral automorphism, with matrix \(\left(\begin{smallmatrix}5&2\\2&1\end{smallmatrix}\right)\), and does not supply the present coefficients. Searches of mathematical research summaries and the literature disclosed no covering formula. Potential equivalent unpublished or unindexed calculations remain the main risk.

## Value — PASS

On a natural curve where the fixed-point derivative is exactly indistinguishable from the undeformed cat map, the two primitive period-two cycles provide the first quantitative spectral obstruction to differentiable conjugacy. The nonzero and asymmetric golden-ratio coefficients identify how and at what order fixed-point spectral blindness is broken. This addresses a motivated rigidity question rather than an arbitrary parameter substitution or mere numerical difference.

## Scope, closest works and remaining risks

[1] Bandtlow, Just and Slipantschuk, arXiv:2402.14770v1, especially equations (2)–(5), defines the exact family and establishes fixed-point data and hyperbolicity. [2] Slipantschuk, Bandtlow and Just, arXiv:2211.05925v1, concerns rational Anosov resonances. [3] Shchetka, arXiv:2610.19019v1, Section 4, treats a distinct Blaschke-deformed map. The theorem gives a small-parameter analytic asymptotic, not an explicit full-parameter rigidity theorem. General invariance of periodic derivatives under differentiable conjugacy is standard. Numerical evaluations are not an independent audit.

Self-review: passed. Independent audit: not yet performed.
