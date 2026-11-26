# Independent mathematical audit

## correctness

PASS

For a nonconstant unit rim Fourier vector (zero at the hub), the Laplacian quadratic form depends only on the mean spoke and rim weights. The first and highest-frequency tests give affine bounds with slopes -u and v; minimizing their maximum and using the hub budget gives μ(P) ≥ (1−p̄)r ≥ μ*. At the proposed invariant chain u+v>4, so the hold constraints are feasible. The hub–rim contrast eigenvalue is −1/m, bounded in modulus by μ* (including equality at m=4); the rim modes attain both ±μ*. The same two affine tests give p*−p̄≤ε/r and |q̄−q*|≤H. The first-mode Rayleigh quotient is at least μ*−(u/v)ε. For M=μ(P)I−(P−J) one has 0≤M≤2μ(P)I, so ||Mf||²≤2μ(P)⟨f,Mf⟩ and ||(P−P*)f||≤B. Dividing by f_j on the rim gives imaginary part sin(2π/m)(δq_j−δq_{j−1}); the cycle spectral gap is 4 sin²(π/m), yielding (1). The real part gives the spoke bound (2) by the triangle inequality, with coefficient 2(1−cos(2π/m))=u. Both bounds vanish at ε=0, and the row sums fix the holding weights. No symmetry of the competitors beyond matrix symmetry is used. Replay: RESULT.md lines 39–98. Read the supplied verify.py and VERIFICATION.md; the reported floating-point checks are finite and were not rerun or used to infer the theorem.

## originality

PASS

Passes only for unrestricted uniqueness and explicit global wheel-edge stability. The minimum and invariant optimizer are known and correctly excluded from the originality claim. Neither the closest wheel source nor the closest indexed analogue establishes the claimed wheel rigidity estimates.

## value

PASS

The established minimum alone would not tell whether noisy, asymmetric edge assignments can remain optimal. The theorem rules out that ambiguity and provides explicit bounds on individual edge families from observable spectral suboptimality. That is useful on a natural two-orbit graph beyond simply recomputing the symmetric chain; no claim of sharpness or uniform-in-m constants is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
