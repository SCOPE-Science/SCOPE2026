# Self-review

**Correctness — PASS.** The Ehrhart count is exact, the sectional genus follows by general linear-section differences, and the singularity computation identifies precisely \(\binom n2\) Segre-cone vertices. The explicit rational splitting witness gives exactly \(m=n-2\) nearby simple solutions and the interpolation argument proves evaluation determinant order \(m-1\), so the trace discriminant has order \(2m-2\). Theorem 5.2 of [1] then gives the stated degree subtraction. The finite checker corroborates n=4..12 but is not substituted for this proof.

**Originality — PASS, with risk.** The closest work is Goertz--Sturmfels--Telen, arXiv:2610.29204v1 (Theorems 4.1, 5.2 and Example 8.3), which gives the general factorization and four suspected numerical cases but explicitly leaves singular toric degree formulas open. Sturmfels, arXiv:1410.6703v2, gives only the generic Hurwitz degree. The all-n formula and the local rank-one-cone correction do not follow from the earlier table alone. Equivalent older formulas under different descriptions remain a possibility.

**Value — PASS.** This is the natural second-hypersimplex family singled out in the motivating paper's explicit open computational question. The result determines a complete exact family rather than a single extrapolated example, and explains why the singularity degree correction grows with n.

**Limits.** The conclusion is characteristic zero and second-hypersimplex specific. The checker verifies finite arithmetic, while the indefinite assertion rests on the written Segre-cone and trace-pairing proof. Independent review has not been performed.

Self-review: passed. Independent audit: not yet performed.
