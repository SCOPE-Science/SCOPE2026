# Mathematical assessment: quartic sampling on type-\(D_d\) roots

## Correctness — PASS

The mathematical claim is restricted to all integer dimensions \(d\ge5\) and exact spherical-harmonic degree four. With probability surface measure and evaluation divided by \(\sqrt{h_{d,4}}\), the addition theorem gives the normalized Gegenbauer Gram \(P_{d,4}(x\cdot y)\), whose diagonal is one. The signed-pair geometry supports an orthogonal antisymmetric/symmetric decomposition. The symmetric block is a Johnson two-subset adjacency combination. The complete-graph incidence identity establishes its three eigenspaces, multiplicities and explicit eigenvalues without assuming an unproved representation-theoretic statement. All branches are positive except the seven-dimensional standard block in dimension eight. Direct derivatives and endpoint comparisons give the optimal uniform positive spectral gap \(11/640\), attained in dimension nine. All checks in `checker.py` reproduced the recorded exact-rational output. Finite checks support, but are not substituted for, the proof valid in every dimension.

## Originality — PASS with publication-priority uncertainty

The closest source texts provide classical harmonic-index design definitions and reproducing kernels (Bannai–Okuda–Tagami, 2013; Zhu and coauthors, 2015), and special \(D_4\) harmonic-design results (Hirao–Nozaki–Tasaka, 2023). The latter dimension is outside the new theorem and is not presented as original. The main comparison is mathematical implication: design vanishing of the sum of evaluation vectors in dimension four cannot establish full evaluation rank in all higher dimensions, the dimension-eight seven-dimensional standard-sector obstruction, or the optimal dimension-uniform spectral gap at nine. Classical Johnson graph eigenvalues and Gegenbauer addition formulas are ingredients, not independently claimed advances. Targeted searches did not yield a published theorem asserting the combined degree-four \(D_d\) spectrum and sharp global stability constant. An older general eigenmatrix of the signed-pair association scheme could make the factorization a specialization, and a prior optimization of those eigenvalues could subsume the sharp gap. This remains a meaningful priority risk; search failure is not proof of uniqueness.

## Value — PASS

The dimension family is a canonical root-system sampling configuration. Exact surjectivity versus a seven-dimensional loss at \(d=8\) determines which degree-four harmonic data can interpolate arbitrary measurements. The uniform bound has a precise analytic role: a dimension-independent optimal norm for minimum-energy interpolation and a sharp worst-case dimension, \(d=9\). These facts give structural sampling information not supplied merely by knowing that the roots are spherical designs. No claim of analogous behavior for other harmonic degrees or configurations is made.

## Literature and limitations

Sources: Bannai–Okuda–Tagami, arXiv:1308.5101v1; Zhu–Bannai–Bannai–Kim–Yu, arXiv:1507.05373v1; Hirao–Nozaki–Tasaka, arXiv:2303.09000v3. Classical Johnson-scheme formulas and spherical addition theorems are explicitly used. More comprehensive historical association-scheme spectral treatments might subsume aspects of the result. The numerical checks are finite, and independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
