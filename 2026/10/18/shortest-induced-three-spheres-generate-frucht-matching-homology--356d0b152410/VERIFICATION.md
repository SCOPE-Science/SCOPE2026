---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction of the exact finite checks

Execute `python3 verify_frucht.py` with Python 3 standard library. It reconstructs all 1,025 nonempty simplices of the matching complex of the explicitly embedded 18-edge Frucht graph, all signed boundary columns, and the integer chain identities. It obtains the boundary ranks \(17,100,233,144,8\) with exact unit pivots and uses integral quotient reduction, not modular inference, to certify primitivity and integral generation.

It enumerates all 36 incident-edge pairs and all disjoint four-pair selections; after deduplication these are exactly 87 distinct eight-edge octahedral carriers. Each of the 87 fundamental chains has sixteen signed facets and exact zero integer boundary. Each has nonzero primitive quotient coordinates. A fixed ordered subset of twenty carrier indices has an integral unit-pivot certificate, so it spans all of third homology.

Execute `python3 verify_modular.py` independently to check all boundary ranks and the augmented carrier rank modulo 2, 3, 5, and 101. This second program does not establish integral saturation; that depends exclusively on the integer certificates above.

The graph-edge list, orientation convention, carrier enumeration order, and chosen indices are stated in the result or generated explicitly by the verifier; no external files or libraries are required. No infinite family is tested or claimed. This is reproducible checking of finite mathematical work, not an independent scientific audit.
