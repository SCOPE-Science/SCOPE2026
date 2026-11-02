---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Orthogonal three-vector Lanczos coordinates give A[v1 v2]=[v1 v2] [[alpha,a],[a,beta]]+b v3 e2^T. Writing Gram metric G=S^T S on this span, sketched Ritz H=G11^-1 G1: A:,1:2 has offdiagonals a+bt1, a and second diagonal beta+bt2, where t=G11^-1 G12. The eigenvalue discriminant is (alpha-beta-bt2)²+4a(a+bt1). For (1-epsilon)I<=G<=(1+epsilon)I, every 2D compression yields ||t||<=epsilon/sqrt(1-epsilon²); hence maximum imaginary part is bounded by sqrt([a(b epsilon/sqrt(1-epsilon²)-a)]_+). The sharp SPD 3x3 tridiagonal and Gram G=[[1-e²,0,-e sqrt(1-e²)],[0,1,0],[-e sqrt(1-e²),0,1+e²]] attain equality with eigenvalues 1±e,1, and become defective at epsilon=a/sqrt(a²+b²). Independent symbolic checks confirmed H, Gram spectrum, characteristic polynomial and critical threshold; the universal bound rests on the compression inequality.

## originality

PASS

Previously studied sketched Rayleigh–Ritz already permits nonreal estimates on symmetric inputs, and standard randomized Arnoldi gives its oblique projection formula. These are acknowledged. The new asserted distinction is a SHARP deterministic embedding tolerance depending on two consecutive Lanczos couplings, with a best possible imaginary envelope and defective extremizer. The original foundational sRR full manuscript was located but inaccessible via authorized OA link; a related complete sketched Arnoldi primary text was inspected. Residual priority risk is explicit.

## value

PASS

The exact epsilon threshold gives a meaningful finite-iteration quality certificate for sketched symmetric eigensolvers, tying an observable sketch distortion to Lanczos couplings. Optimality and a defective transition make it more than a qualitative observation of nonreal computed eigenvalues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
