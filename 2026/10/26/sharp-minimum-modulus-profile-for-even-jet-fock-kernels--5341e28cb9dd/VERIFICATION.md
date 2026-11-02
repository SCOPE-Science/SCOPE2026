---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Monomial norms are n! except the mth norm m!(1+tau m!), so the kernel exactly equals e^t-qt^m. For r<=R, |e^t-qt^m|>=e^{-|t|}-q|t|^m>=e^{-r}-qr^m; t=-r attains equality only because m is even. For r>=R, t=-R is a contained zero; at the nearest-zero radius equality in Re(t)>=-|t| forces t negative real and uniqueness. Derivative at -R is e^{-R}+qmR^(m-1)>0. Stirling and W derivative yield stated correction. Independent calculations used 12 (m,tau) parameter pairs with 640 sampled complex tests each plus exact R relation.

## originality

PASS

Classical Fock kernels, rank-one Hilbert-space norm changes and Lambert inversion are antecedents. The inspected global Fock-Sobolev abstract covers spatially weighted norms, not the individual m-jet coefficient perturbation or its exact two-variable modulus. Distinctness does not prove priority; exact kernel-zero calculations may appear under Lu Qi-Keng terminology.

## value

PASS

The nearest-zero radius and exact lower envelope give a natural sharp nonvanishing threshold for reproducing kernel entries under a single-jet penalty, and the uniform-penalty asymptotic is a useful quantitative boundary; the claim does not infer stability of multipoint Gram matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
