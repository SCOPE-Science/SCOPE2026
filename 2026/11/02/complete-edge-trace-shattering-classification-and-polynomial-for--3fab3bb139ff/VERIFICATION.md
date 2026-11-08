---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

All-positive labeling forces support inside a spanning Hamiltonian cycle, hence a linear forest except full cycle; a forbidden endpoint labeling excludes spanning paths. For linear forests, contract every positive-edge path-run, retaining orientations. The remaining negative constraints form max-degree-two forbidden adjacencies; Dirac handles block counts >=6 and explicit 3..5-block cycles plus orientation handle the boundary. The precise two-component n-2 condition excludes orders 2 and 3. Labeled path-component exponential counting yields F_nk and M_n. An independent all-concept/all-compatible-support brute-force test at n=3..6 (8,37,218,1546 supports) matched every edge trace and formula; the unrestricted proof is separate.

## originality

PASS

PASS qualified: known numerical Hamiltonian VC dimensions, all-cycle hypergraphs and different graph queries do not establish this all-support iff rule or all-order counting polynomial; 1997 graph-set-system full text remains priority risk.

## value

PASS

Classifies every shattered fixed-edge support of labeled Hamilton cycles, including the sharp two-component boundary and an all-order polynomial; such a natural complete VC-set-system classification has independent mathematical value beyond a scalar VC dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
