---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Reconstructed the exhaustive oriented-factor proof: zero-marker counts depend on unordered gaps, one-marker adjacent thresholds cannot separate reversal before x+y+3, two-marker factors need at least the two shortest gaps plus three symbols, and the first three-marker factor fixes oriented cyclic gaps. At K=floor(2n/3), no such factor forces the four enumerated repeated-gap profiles; the 10^d1 marginals then reconstruct the unique necklace. Explicit distinct-gap reversal pairs in each residue class prove sharpness; n=3,4,5, adjacent gaps and periodic cases handled. Independent complete rotation-class enumeration n=3..15 reproduced R(n), while universal theorem rests on the symbolic proof.

## originality

PASS

A general binary circular-string automaton decides each primitive instance, but no inspected source states the weight-three exact all-n 2n/3 threshold and exact n-max-gap orientation obstruction. This is a qualified closed-form structural specialization, not a claim to invent cyclic assembly.

## value

PASS

Full multiplicity oriented cyclic k-reads and exactly three sparse markers define a natural reconstruction inverse problem. The exact uniform minimal read budget, individual chirality obstruction, and explicit decoding mechanism could be directly used in sparse circular sequence assembly; not a numerical table or a renamed generic algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
