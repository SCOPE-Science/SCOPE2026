---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 check_mobius.py` with the Python 3 standard library. The checker constructs the graph from its defining formulas, verifies all ten table rows, exhausts all singleton and two-vertex seeds without a symmetry reduction, and compares the successful seeds with the edges of the bipartite complement. It tests every pair of minimum states for one-token exchanges, counts eligible slides, and checks distances from every jump state. The proof in `RESULT.md` also derives the line graph, slide obstruction, and all eccentricities from the pair characterization directly. No properties of any other cubic graph are asserted by this certificate.
