---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Polynomial long division verified that g divides x^15+1 with quotient 1+x²+x³+x⁴+x⁶. Its six shifts have distinct leading degrees and rank six. Independent hyperplane/coset enumeration generated all 2,824 message spaces and computed support from the sum of all word weights on each divided by 2^(r−1), rather than the frozen script's basis-support union. Every bin, the hierarchy (6,9,11,13,14,15) and all six minimizer counts agree. The ordinary distribution also agrees by independently comparing all 64 words to arrays a_i+b_j with a and b even, in CRT order.

## originality

PASS

The cyclic construction and classical parameters are not claimed as new. The full support counts of its exact parity-cut presentation are not supplied by the inspected cyclic or graph-code comparisons. The pass concerns the verified distribution of this fixed code, not its presentation or all length-15 optimal codes.

## value

PASS

The fixed natural cyclic code also describes even cuts of a small complete bipartite graph. Its table counts all simultaneous cut supports, including 40 extremal two-spaces and 11 two-spaces meeting every coordinate. These incidence-sensitive counts distinguish it from alternatives with the same parameters and are useful beyond confirming its already-known minimum distance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
