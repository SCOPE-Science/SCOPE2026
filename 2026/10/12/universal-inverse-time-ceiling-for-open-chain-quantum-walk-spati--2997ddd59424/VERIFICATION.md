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

For each site, source Eq. (26) gives independent Bernoulli occupation bits, hence diagonal local purity equals product_i[pij^2+(1-pij)^2]. With xij=2pij(1-pij) in [0,1], 1-product_i(1-xij)<=sum_i xij; after summing over sites with sum_j pij=1 this is at most 2 sum_i(1-sum_j pij^2)<=2M. Substitution into the source Eq. (24) gives E_MW <=(2^M/(2^M-1))*2M/(2t+M+1). All M and all site profiles allowed, fixed-M decay O(t^-1). Independent exact rational enumerations M=1..4 cross-checked purity/finite inequalities; analytic factorization proves arbitrary M.

## originality

PASS

PASS, best of knowledge: the original Goyal-Chandrashekar paper prints the exact M-walker density-matrix product law and shows numerical late-time decline, but in its relevant full primary section does not quantify the coin-independent all-M inverse-time upper bound. An indexed query for equivalent bounds found no specific dominating theorem. The later exchange-symmetric two-walker problem uses different hypotheses and is not treated as a verified whole-document noncoverage claim.

## value

PASS

PASS: source explicitly interprets the observed open-chain entanglement decline physically without an all-coin rate. A uniform finite-time ceiling and one-particle inverse-participation refinement give an exact, reusable analytic constraint on this natural spatial-entanglement measure rather than simply reproducing its plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
