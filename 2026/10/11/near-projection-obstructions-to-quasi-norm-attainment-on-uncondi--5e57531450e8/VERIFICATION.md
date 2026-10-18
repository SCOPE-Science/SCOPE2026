---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For any infinite 1-unconditional Schauder decomposition, diagonal D_eps=diag(1-eps/n) has norm 1 by late nonzero blocks, norm distance eps from identity on first block and inverse norm (1-eps)^-1. A Hahn–Banach norm-one functional supporting nonzero D_eps y satisfies sum abs phi(y_n)<=||y|| by unconditional phase choices, hence strict ||D_eps y||<||y|| because all diagonal coefficients <1. Norm-one projection P maps B_X onto B_Y, while invertible D_eps carries B_Y to a closed subset missing norm sphere; S_eps=i D_eps P is not QNA. Includes complex scalars and arbitrary nonzero block dimensions; excludes ell-infinity products.

## originality

PASS

The classical Hilbert diagonal I-K example is already known, but Choi et al Proposition 4.3 is X to c0 and Proposition 4.4 is l1 to Y, not near-projection non-QNA endomorphisms for every 1-complemented arbitrary block sum. The exact eps and inverse estimates require arbitrary-block support-functional lemma. Ostrovskii norm-attainment/AP necessary condition has different hypotheses. Best-of-knowledge new structural quantified obstruction, folklore-risk remains.

## value

PASS

Motivated structural exclusion for possible universal QNA endomorphism spaces (Choi et al Problem 7.11), including nonreflexive L1 and arbitrary non-AP components. Exact norm-boundary points at norm-one projections and invertible near-identity examples matter; not a universal classification or mere renaming of Hilbert case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
