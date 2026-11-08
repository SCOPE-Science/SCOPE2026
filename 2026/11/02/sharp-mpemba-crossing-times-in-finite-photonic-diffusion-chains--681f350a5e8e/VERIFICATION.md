---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

PASS. Path Neumann Laplacian has eigenvalues 4omega sin²(k pi/(2N)), orthonormal midpoint-cosine eigenvectors. Central start kills odd modes; the near-uniform missing-endpoint start has coefficients -phi_k(N)/(N-1). Consequently H_I=sum_{even k} e^(-2lambda_k t) and H_II=(N-1)^(-2)sum_{k>=1}cos²(k pi/(2N))e^(-2lambda_k t). After multiplying the difference by e^(2lambda_1t), pair each even k with k+1; the ratio (lambda_{k+1}-lambda_1)/(lambda_k-lambda_1)<=8/3 and epsilon<=1/16 enforce every paired contribution strictly decreasing. Opposite endpoint signs prove exactly one quadratic crossing. k=2 vs k=1 balancing gives T_N and an additive -1/(6pi²omega) with controlled higher-mode tails. Cubic Fourier overlap <cos² x cos 2x>=1/4 yields KL difference -N^(-5)(1+o(1)) at s_N, derivative -2(lambda2-lambda1)a² and local unique KL shift -N^(-1/3)/(6pi²omega). Finite eigenvalue and root tests corroborate only finite cases.

## originality

PASS

PASS (best of knowledge). Longhi already supplies the physical chain and initial comparison. Restricted to additional quantitative/rigorous odd-N statements not obtained from inspected older Markovian Mpemba papers. Unread Longhi supplement is explicitly a material residual risk, not claimed absent.

## value

PASS

PASS. This exact spectral crossing classification strengthens the earlier physical qualitative result with a universal odd-chain existence/uniqueness theorem, sharp macroscopic time and observable-dependent KL correction; resolving two different relaxation metrics is mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
