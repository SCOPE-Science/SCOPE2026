---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The determinant of Omega^H(A-zI)[w,V] factors as det(D-zI)*[(rho-z)det(g,B)+sigma det(h,B)] because V is invariant and residual perpendicular V,w. Gaussian unitary invariance and conditioning on B makes the ratio a quotient of independent circular complex normals. Its radial tail 1/(1+t^2) gives infinite q>=2 moments. Independent symbolic differentiation of the exact real-marginal CDF .5(1+x/sqrt(1+x^2)) gives median-of-three density 3/[4(1+x^2)^(5/2)]; SymPy exact integral computes its coordinate second moment 1/2. Real+imag variances sum to sigma^2 and centering gives (rho-lambda)^2+sigma^2=||(A-lambda I)w||^2. Median tails of k=2h+1 have order t^-2(h+1), giving threshold q<k+1. Finite sketch simulation not used as infinite proof.

## originality

PASS

Shao (2026) introduces square complex-Gaussian randomized Rayleigh–Ritz and high-probability O(epsilon) Ritz convergence; its refinement is a different statistic. Nakatsukasa–Tropp (2024) use oversampled sketched pseudoinverse; Gu (2020) treats Gaussian quotient probability, which is acknowledged. The exact invariant-spectator ratio reduction plus three-median residual-scale identity was not identified in read source sections.

## value

PASS

A high-probability stable randomized eigenvalue extraction can have infinite mean-square loss; the exact dimension-free replacement risk and minimal odd repetition count are nontrivial risk-calibration facts for that specific unrefined estimator. Does not claim advantage over deterministic Hermitian Rayleigh quotient or robustness in arbitrary trial geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
