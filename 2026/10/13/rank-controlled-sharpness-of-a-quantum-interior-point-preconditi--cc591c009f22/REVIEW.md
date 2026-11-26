# Independent mathematical audit

## correctness

PASS

The compared primary definitions give the same partition threshold, current-iterate ω and unnormalized reduced Y. Strict complementarity on the exact path yields x_N=O(μ), x_J bounded below, D_1=μ diag(x_J^−2) and D_2^−1=μ diag(s_N^−2), so the threshold identifies J. From Ax*=b≠0, r≥1. With B=A_J(I+D_1)^−1/2, let C=B diag(x_J²)Bᵀ. The push-through identity for S=B D_1^−1/2 gives G=SSᵀ(ĥ I+SSᵀ)^−1=C(C+μĥ I)^−1. In the fixed orthogonal decomposition ran A_J ⊕ ker A_Jᵀ, C is uniformly positive definite on the first summand and zero on the second. Thus G equals I+O(μ) and 0 respectively, and H=BBᵀ+μQ(μ) with Q(μ)→A_N diag((s_N*)^−2)A_Nᵀ. This gives Y blocks I+O(μ), O(μ²), O(μ), and μQ⊥/h₀+o(μ), respectively. Full row rank of A makes Q⊥ positive definite by its weighted Gram form. For r<m, two invertible elimination factors I+O(μ) reduce Y to its upper diagonal block and the Schur complement, changing the latter by O(μ³). Applying singular-value inequalities with those factors and their inverses gives relative factors 1+O(μ) for every singular value, so this argument does not confuse eigenvalues of a generally nonsymmetric Y with singular values. The r=m case directly gives Y→I and includes N empty. The source's additional norm normalization of its reduced equation leaves the condition number unchanged and tends to 1 here. For the integer witness, columns 1,2 give an admissible I₂ basis, both primal and dual are strictly feasible at the displayed positive μ points, and μ→0 gives a strictly complementary optimum. Inserting the diagonal blocks and ω=1 gives Y₁₁=(1+μ)/(1+γ₁μ(1+μ)), Y₂₂=2μ/γ₁, so μκ₂→γ₁/2; the original normal matrix is diag(1/μ,2μ). This independently verifies the example exactly, not by extrapolation. The frozen verification notes and rational checker were inspected read-only.

## originality

PASS

Credit the exact support-rank dichotomy and leading compressed-Gram singular-value law for the WYT scalar, and the verified attaining witness. The preconditioner, the two-scale partition and the reciprocal-gap upper bound are prior work; the result does not establish that the broad rank-loss mechanism is new. Coverage by Chai–Toh beyond the verified comparison remains a limitation, not evidence that the law was previously known.

## value

PASS

The theorem explains exactly which strictly complementary LP limits saturate the specified preconditioner's prior worst-case bound. A verifiable geometric diagnostic, rank of the positive support, predicts whether conditioning tends to one or diverges, and the weighted projected Gram matrix gives a usable coefficient in the divergent case. The witness shows this is not an artifact of a misidentified partition or of unbounded integer data. This is narrowly useful for the specified linear-system stage, not a lower bound for quantum algorithms or arbitrary preconditioners.

The dated certificate retains the supplied scientific assessment, sources and limitations.
