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

Actual sextic equations and exact generator matrices were inspected. Independent 4x4 projective-matrix closure checks reproduced 8 group elements (orders 1:1,2:5,4:2) for type I and 24 (1:1,2:9,3:8,4:6) for type II. The repository checker verifies each generator by exact symbolic polynomial substitution; the independent closure alone does not verify those substitutions. A projective stabilizer injects into Aut of the smooth minimal Enriques model; published orders 8 and 24 provide matching upper bounds. Thus full stabilizer and all-automorphism realization follow, assuming the displayed published Enriques models.

## originality

PASS

Published automorphism group orders and D8/S4 abstract groups are already known; the added mathematical statement is explicit projective realization by matrices on the named two sextic equations. The Shimada–Veniani primary group/order result and displayed equations do not visibly assert this projective surjectivity. No implication-equivalent statement was identified in focused Resultary comparison; earlier Kondō equation-level material was not fully read, so priority remains best-of-knowledge.

## value

PASS

The exact projective realization of all automorphisms on canonical Enriques sextics answers the geometrically natural question whether an abstract smooth-surface symmetry is visible linearly in its distinguished model; explicit finite generators are useful beyond abstract automorphism group orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
