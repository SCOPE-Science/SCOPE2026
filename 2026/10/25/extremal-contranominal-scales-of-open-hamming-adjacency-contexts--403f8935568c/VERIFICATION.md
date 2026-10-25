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
# Verification of extremal open-Hamming contranominal scales

The accompanying standard-library Python program `verify.py` builds the exact open Hamming adjacency matrix, enumerates candidate object supports, and directly tests the contranominal witness conditions. It requires Python 3.8 or later. Run from this directory with `python3 verify.py`.

An actual complete execution checked \(4,321,392\) object supports of the proposed maximum cardinalities across fourteen parameter pairs. These are \((q,d)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(5,1),(5,2),(6,2)\). Exhaustive exclusion of the immediately larger cardinality was also performed when the enumeration threshold allowed it. All cases matched the theorem's maximum dimensions and exact counts where claimed.

Observed counts of maximum-dimensional object sets include: \(2\) at \((2,3)\), \(16\) at \((2,4)\), \(54\) at \((3,3)\), \(648\) at \((3,4)\), \(80\) at \((4,2)\), \(1344\) at \((4,3)\), \(10\) at \((5,2)\), and \(12\) at \((6,2)\). For \((4,3)\), these partition into \(48\) line, \(864\) two-parallel-pairs, and \(432\) parity-tetrahedron cases. The checker directly confirmed unique witnesses and every paired incidence for every enumerated scale of dimension at least four.

For \((q,d)=(5,3)\), an additional reproducible pseudorandom sample of \(25,000\) five-object supports was checked for scale existence and, when present, coordinate-line rigidity. Deterministic seed: `20261018`.

All asserted finite checks passed. Exhaustion of finite parameter sets is not an infinite-parameter proof; arbitrary dimensions and alphabet sizes are covered by the symbolic common-neighbor classification in the result. The checker does not establish publication priority or independent validation.
