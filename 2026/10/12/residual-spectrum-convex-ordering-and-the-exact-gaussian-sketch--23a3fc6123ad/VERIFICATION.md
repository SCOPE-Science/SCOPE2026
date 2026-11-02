---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For real standard Gaussian Y independent of the fixed orthonormal Q, the blocks G=Y^TQ and H=Y^TU are independent Gaussian and G has rank r almost surely for ell>=r. Orthogonality of range(Q) and range(B) gives exactly R=1+sum_j lambda_j ||G^dag h_j||^2, with conditional iid and unconditional exchangeable nonnegative Z_j. For ell>=r+2, the common beta-prime mean is finite and Hardy-Littlewood-Polya plus Jensen yields lambda majorizes mu => R_mu <=cx R_lambda for every convex phi for which expectations exist. Integrating Gaussian N_r(0,(G^TG)^-1) against Wishart_r(ell,I) gives density Gamma((ell+1)/2)/(pi^(r/2) Gamma((ell-r+1)/2)) (1+||z||²)^(-(ell+1)/2), whence ||z||²~BetaPrime(r/2,(ell-r+1)/2)=(r/nu)F_(r,nu). The tail index nu/2 follows exactly. For every nonzero weight vector, a single positive component supplies lower moment-divergence and a finite sum supplies upper moment-finitemess, proving iff 0<q<nu/2 even for ell=r or r+1. When nu>4, conditioning on G and using the Gaussian quadratic-form variance gives Var R=Var tr(S^-1)+2 E tr(S^-2) sum lambda², strictly increasing under non-permutation strict majorization. Edge cases zero B (undefined), ell=r, ell=r+1, finite mean ell>=r+2, finite variance ell>=r+4, d=1, zeros padded, and random Q (only conditional) were checked. Fresh independent calculations passed 900 direct reconstruction identities, 17 exact rational r=1 variance cases, 60 F/beta-prime CDF cases, and conditional variance diagnostics, which corroborate rather than prove infinite statements.

## originality

PASS

The exact Gaussian decomposition/first mean are preexisting. Best-of-knowledge, the additional all-spectrum convex-risk majorization, strict spectral variance dependence and explicit exact-q cutoff as a unified Gaussian two-sided sketch robustness classification are not stated by the reviewed primary works, including a closely related 2024 extension. Classical inverse-Wishart and majorization ingredients and the risk of a routine-corollary priority objection are fully acknowledged.

## value

PASS

Residual squared singular-value proportions are a natural matrix-sketch quality invariant. The exact expected squared inflation is blind to spectral concentration, but nonlinear loss/convex risk and finite variance are crucial for reliability of randomized approximate factorizations. Explicit monotonicity across all residual profiles, a rank-one worst convex-risk calibration, and the sharp oversampling-dependent q-moment frontier distinguish genuinely consequential regimes. The theorem is incremental and based on standard Gaussian and majorization tools, but gives a directly interpretable algorithm-specific risk classification beyond a mere reformulation of its known mean formula; no faster algorithm or unconditional random-range result is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
