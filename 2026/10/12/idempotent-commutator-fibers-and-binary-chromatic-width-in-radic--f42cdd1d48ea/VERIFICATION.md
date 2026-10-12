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

# Reproducible checks and limits

Run the standalone `verify.py` script with Python 3 and no third-party packages. It builds multiplication directly from the defining algebra relations, checks all idempotents by multiplication, enumerates every ordered idempotent pair, and compares every radical target count with an independent four-label evaluation. The cases include \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\) (represented by a quadratic quotient), loopless parallel and opposite arrows, a triangle, a path, and isolated vertices. It also verifies a fully supported triangle target needs precisely two idempotent commutators over \(\mathbb F_2\). A passing invocation prints `VERIFY_OK`.

The finite checks cannot establish the theorem for every quiver and field; that conclusion is justified by the explicit coefficient proof and proper-coloring construction in `RESULT.md`. Graph chromatic number can be hard to compute for large inputs, but the theorem remains exact. The full text of one historical general idempotent-commutator characterization was not obtained, so bibliographic priority is unresolved. No independent mathematical audit has been performed.
