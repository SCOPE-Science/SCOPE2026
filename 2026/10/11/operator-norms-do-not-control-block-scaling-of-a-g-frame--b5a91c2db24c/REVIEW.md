# Independent mathematical audit

## correctness

PASS

In H=ℓ²(N) let P_j be e_j-projection, ε_j=2^{−2j}, α_j=2^{−j}, Λ_j=P_j+ε_jI. Each Λ_j is a positive invertible diagonal operator with eigenvalues 1+ε_j and ε_j, so its norm tends to 1 but minimum modulus ε_j tends to 0. By Tonelli, Σ_j||Λ_j x||²=Σ_k[1+2ε_k+E]|x_k|² with E=Σ_j ε_j²=1/15; frame lower bound 16/15 and upper bound 47/30 are exact. Let D_j=α_j Λ_j^{-1}; D_jΛ_j=α_j I and Σ α_j²=1/3, so scaled analysis is a tight g-frame, yet ||D_j||=α_j/ε_j=2^j→infinity, making ambient ⊕D_j unbounded. Independently recomputed exact fractions, spectra and geometric sums without finite truncation. Primary Ahmadi–Rahimi Proposition 3.1 and Kumar–Malhotra–Khanna Theorem 24 both infer uniform lower singular bounds from only liminf operator norms, which the example explicitly refutes while preserving invertibility of every block.

## originality

PASS

The 2021 Ahmadi–Rahimi and 2024 Kumar–Malhotra–Khanna COMPLETE original article proofs were directly inspected: each falsely promotes liminf_j||Λ_j||>0 to an eventual uniform lower bound on min singular values, concluding global ambient block multiplier boundedness. The precise infinite positive invertible diagonal-block counterexample is not contained in those original propositions; they are target false claims, not covering resolutions. A different published Resultary K-frame record concerns unbounded scalar scaling for a rank-one K-frame with closed-range issues and lacks this all-invertible g-frame block construction with operator norms tending to one; related analysis-range criteria are acknowledged as PRIOR. Targeted Resultary searches revealed no distinct identical correction, with nonindexed errata a residual risk.

## value

PASS

Disproving two directly related published bounded-preconditioner theorems with a nondegenerate invertible block example is a motivated corrective finding. It isolates a substantive operator-theoretic error—maximal singular values do not control the required minimum moduli—and distinguishes boundedness of D on the ambient coefficient sum from boundedness of D◦T_Λ* on actual analysis vectors. Positive invertible analysis blocks and exact tightness rule out easy kernel or finite-dimensional corner cases; a future frame-theory reader needs this precise obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
