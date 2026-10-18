---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

From the actual frozen RESULT.md derive c_F=||Omega b||²/[(Omega b)^T Omega Ab] and c_G=[(Omega Ab)^T Omega b]/||Omega Ab||². Orthogonally decompose Av=a v+d w. Independent standard normal sketches of v and w make (u^T z)/||u||²=Z/sqrt(chi²_ell)=T_ell/sqrt(ell), so c_F^{-1}=a+(d/sqrt ell)T_ell. Rotating to Av/sqrt(m) yields c_G=a/m+(d/(m sqrt ell))T'_ell. The reciprocal denominator density is positive at zero for every finite ell when d>0, giving the displayed 2 f_Y(0)/t tail and all |c_F|^q divergences q>=1; the exact A-orthogonal energy decomposition transfers this to expected squared error. For ell>2 Student variance d²/[m²(ell-2)] and residual expansion give ||b||²(d²/m)(ell-1)/(ell-2); all moment thresholds and eigenvector boundary d=0 were reconstructed. The inspected standard-library verifier samples exact coefficient identities, not rare-tail proofs.

## originality

PASS

The sketched projection equations and embedding-conditional stability results were already published. The independent one-dimensional Gaussian ratio computation identifies an unconditional reciprocal pole and a sharp FOM-versus-GMRES risk distinction not stated or implied by the inspected theorems on high-probability convergence or deterministic numerical stability; novelty is best-of-knowledge, not an assertion that Student distributions are new.

## value

PASS

An exact universal separation between the unconditional moments of two established one-step Krylov projections is mathematically motivated by rare projection singularities and high-probability safeguards. Infinite A-error at every finite oversampling size is a concrete all-parameter phenomenon, with exact tail constant and finite-risk comparator; it is not an arbitrary small example or a renamed normal-ratio identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
