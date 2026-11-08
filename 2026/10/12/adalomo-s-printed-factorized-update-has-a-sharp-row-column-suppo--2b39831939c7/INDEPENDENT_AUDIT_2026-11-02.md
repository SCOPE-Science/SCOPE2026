# Independent mathematical audit

## correctness

PASS

The frozen RESULT.md has a precisely limited first-step theorem for finite real m×n matrices, m,n≥1, zero row/column accumulators, and 0≤β<1. The printed ACL 2024 Algorithm 1 has r_i=(1−β)Σ_j G_ij², c_j=(1−β)Σ_i G_ij² and v=rc/(1ᵀr); for G≠0, V_ij=(1−β)R_i C_j/||G||_F². Thus all quotient denominators are positive iff every row and column contains a nonzero gradient. If a whole row or column is zero, the corresponding 0 numerator and 0 denominator form 0/0. For G=0 the normalization has zero total mass. Grouped RMS normalization is applied after raw U, so it cannot repair an undefined U. The strongly convex F(W)=1/2||W−B||² with first gradient [[0,0],[1,−1]] has a nonstationary undefined printed update. Independently reconstructed the exact rational support theorem and exhaustively checked 1×1, 1×3, 2×2, 2×3 and 3×3 matrices with entries {-1,0,1} (20,523 matrices, three β values each), beyond the source 2×3 enumeration. The Git tree SHA was independently reassembled from all seven Git blob entries and matched the assigned tree.

## originality

PASS

Best-of-knowledge originality for the exact *printed AdaLomo first-step* support iff, not the factorization formula itself. Direct inspection of the accessible definitive ACL conference paper confirms its printed unregularized quotient but no separate zero-row/column domain classification in the relevant original method and normalization sections. Adafactor supplies the predecessor factorization with an epsilon-protected quotient, and the first-party AdaLomo code protects sparse rows via an epsilon floor. Three targeted Resultary searches and focused public searches did not expose an implication-equivalent prior classification. The theorem is a short immediate consequence of the published recurrence, and this makes novelty modest and potentially contestable; absence of indexed matches is not proof of priority.

## value

PASS

Although the proof is elementary, it is a complete necessary-and-sufficient well-posedness boundary for a specific factorized optimizer’s first mathematical step, motivated before the calculation by the defining paper’s explicit sparse-gradient use case. The 2×2 strongly convex nonstationary witness shows failure is not confined to a zero-gradient optimum; any complete inactive row/column causes an entire raw update strip to be undefined. This precise condition is needed to state valid assumptions in analyses or faithful reproductions of the printed algorithm, and the documented contrast to Adafactor and safeguarded maintained AdaLomo identifies the exact mathematical fix. It is an interpretive algorithm-specification result, not a new convergence guarantee or practical software vulnerability, and has limited depth; it nonetheless clears the motivated structural-boundary bar rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
