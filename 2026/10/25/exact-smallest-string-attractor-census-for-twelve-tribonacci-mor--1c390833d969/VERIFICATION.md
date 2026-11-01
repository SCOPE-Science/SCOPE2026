---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The factor f coverage set C_w(f) is the union of all positions in all occurrences. A position subset S is an attractor iff it intersects each C_w(f). Removing a superset mask from the antichain preserves the logical hitting constraints. Since every T_k for k≥2 has all three letters, every cardinality-3 attractor has one position per letter. Independently regenerated every T_k (k=0..11), enumerated coverage masks for each distinct substring, and searched all possible letter-class triples by bit-mask intersections, including 20,576,304 raw candidate triples at k=11 length 927; counts match 1,1,2,8,12,16,32,56,112,224,416,832. Source certificate actual entire stage arrays were read and structurally checked: all 12 lengths, unique sorted triple arrays and matching counts; source verify.py and an independently structured verify_independent.py through k=9 were inspected. Exact lower bound each letter occurs implies minimality given nonempty all-triple lists. No extrapolation beyond k=11.

## originality

PASS

The claimed all-solution finite census survives published size-three/existence and k-bonacci construction results: these give one or several optimal triples, not the full multiplicity and explicit lists of all optimal sets through k=11. The close 2026 all-attractor paper concerns other morphic families. Best-of-knowledge priority, with significant finite computation.

## value

PASS

The count of all minimum attractors, rather than just their minimum size, is a natural fine-scale repetitiveness invariant; Tribonacci is the canonical ternary episturmian morphic family. Twelve consecutive exact solution sets through length 927 give meaningful structural data, and the 416 at k=10 refutes a naive simple doubling continuation, constraining future all-order characterization. The exact set enumeration is independently useful as a benchmark even without a new infinite recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
