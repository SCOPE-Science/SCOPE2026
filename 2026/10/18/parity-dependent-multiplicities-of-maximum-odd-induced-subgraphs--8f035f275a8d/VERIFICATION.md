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
# Reproducibility and verification

Run the embedded `verify.py` with Python 3.9 or later and no third-party dependencies. The program constructs rook-graph adjacency directly, enumerates all vertex masks on seventeen small rectangular boards (up to twenty vertices), computes the actual family of maximum-cardinality induced subgraphs whose vertices all have odd degree, and compares their **exact complement masks** with the asserted structural classification. It also compares the independently counted maximum size and number with the even-fibre recurrence.

The executed program reported `PASS: 17 exhaustive graph sizes; 122 maximizing vertex sets matched exactly, including their identity`. Its larger symbolic checks report \(M_{4,6}=96\), \(M_{5,5}=10\), \(M_{6,6}=4512\), \(M_{6,12}=21792\), and \(M_{8,8}=500992\). The latter are formula evaluations, not exhaustive graph searches.

The proof, not the finite census, establishes the infinite assertion. The June 2026 existing maximum-size theorem is credited, not independently claimed. No external independent audit or bibliographic certification is asserted.
