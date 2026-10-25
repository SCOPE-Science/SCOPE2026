---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For step of order L>=3, the three modulation characters 0,+a,-a are distinct; Parseval splits the 3N-dimensional band into diagonal cyclic (I+xT_a) and two off-diagonal scalar sectors. Direct expansion gives singulars sqrt(N)*|1+x exp(2pi i ka/N)|/(1+x) (N times) and sqrt(Nx)/(1+x) (2N times). The least diagonal numerator squared is D_L(x)=(x-1)^2+4x s_L^2, where s_L^2=0 for even L and sin^2(pi/(2L)) for odd. Minimizing (1+x)/min(sqrt(x),sqrt(D_L(x))) is a strict-decreasing then strict-increasing balance at x satisfying x+1/x=3−4s_L^2, unique up to inversion (balanced x=1 iff L=3). The best squared condition number is 5−4s_L^2; smallest odd prime divisor yields all-step best unless N power of two. At balanced even L the diagonal nullity is N/L. Independent construction of ORIGINAL projector rows and dense complex SVD for (N,a)=(4,1),(5,1),(6,2),(9,3) at x=2.3 matched all 3N singulars (<1e−11); submitted output claims 200 further numerical comparisons. Finite SVD is corroboration only.

## originality

PASS

Prior pointwise Gabor-projector Gram spectrum is explicitly credited. The potentially original theorem is the complete jointly optimal power and step-order arithmetic design for the full observable linear band; distinguish from local nonlinear spectrogram Jacobian and full-space tomography.

## value

PASS

The entire linearly observable band of a two-site cyclic Gabor window is a natural identifiability class, and its smallest singular value relative to largest governs worst-case isotropic measurement error. Exact balancing of diagonal and off-diagonal channels identifies when equal tap powers are singular, determines unique weighted optimizers, and yields a clean arithmetic least-odd-prime rule over all cyclic steps. It separates linear operator-band design from unrelated nonlinear phase retrieval conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
