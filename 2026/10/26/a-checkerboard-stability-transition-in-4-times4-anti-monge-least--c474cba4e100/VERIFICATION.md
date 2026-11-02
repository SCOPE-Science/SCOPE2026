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

D_n has independent adjacent mixed-difference rows; every active subset is locally realizable by strict KKT complementarity, so the global infinity norm modulus equals max over P_A=I−D_A^T(D_AD_A^T)^−1D_A. Independently built D from four-corner coefficients and rationally enumerated all 2,16,512 active masks for n=2,3,4, obtaining sharp maxima 3/2,17/9,9/4; exactly mask 341 wins for n=4, while full-pooling mask 511 gives 17/8. The source supplies strictly feasible finite witness at eps 1/100 and proves embedding lower bound for n>4, not equality there.

## originality

PASS

The original least-squares anti-Monge projection and Dykstra algorithm are pre-existing. The complete rational 4x4 infinity-norm Lipschitz classification, unique checkerboard active face and explicit sharp finite input pair were not stated in the inspected main results, algorithm, proof or appendix of the directly matched primary paper.

## value

PASS

Provides a complete, natural, low-dimensional stability classification of the anti-Monge least-squares projection; the checkerboard face displaces full pooling at the first possible square size, with an exact sharp finite-pair witness. The precise constant informs deterministic maximum-error amplification of a widely used shape-constrained estimator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
