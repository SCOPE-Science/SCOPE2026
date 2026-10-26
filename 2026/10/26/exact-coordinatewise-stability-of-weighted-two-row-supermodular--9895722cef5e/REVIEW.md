# Scientific review — weighted two-row supermodular projection

## Correctness — PASS
The two-row anti-Monge differences are equivalent, with fixed column order, to monotonicity of the bottom-minus-top column differences. Completing the weighted squares separates the means from the differences, with difference weights \(c_j=a_jb_j/(a_j+b_j)\). Each isotonic pooling cell has explicitly reconstructed top/bottom Jacobian rows, whose exact absolute sums are \(1+2\alpha(1-c_j/C_B)\). Since \(C_B\le C\), this proves the uniform upper bound. Strictly decreasing input differences produce a stable, strictly complementary, full-pooling cell; a finite sign perturbation realizes the upper bound. The sharp lower bound, its unique equal-weight minimizer, the unattained upper bound three, and intermediate values follow by inequalities and continuity. Exact-fraction checker: 12,883 assertions passed. Finite tests do not substitute for the general proof.

## Originality — PASS within examined sources
Chatterjee–Guntuboyina–Sen, arXiv:1311.3765 (2013), establish the isotonic/shape-constrained regression setting and statistical risk results. Hütter–Mao–Rigollet–Robeva, arXiv:1904.03136 (2019), treat the anti-Monge cone and least-squares estimation, including algorithms. The inspected relevant full-text sections do not state the sharp input-to-fit coordinatewise norm for weighted **two-row** reconstruction or its complete weight range. Published full texts on \(\ell_p\) isotonic map stability concern perturbations of the scalar monotone output, not the two-row reconstruction, and therefore do not imply this sharp constant. Algebraic reuse of isotonic pooling is acknowledged and not claimed as new. Prior art might express equivalent formulas through different matrix parametrizations; historical priority is provisional.

## Value — PASS
The natural data-to-fit stability question differs from mean-square risk and from Hilbert-metric nonexpansivity: perturbations are independently bounded per observation. The exact heteroscedastic constant detects a factor approaching three while identifying the unique minimax weight design and its \(2-1/m\) amplification. The two-row reduction is a transparent structural bridge between Monge regression and one-dimensional pooling, providing a useful sharp boundary case for general Monge stability.

## Limitations
Only fixed-order, complete, two-row, real arrays with positive weights are proved. Larger matrices, incomplete arrays, correlated errors, and alternative coordinate norms are not covered. Scientific independence and exhaustive historical priority were not established.

Self-review: passed. Independent audit: not yet performed.
