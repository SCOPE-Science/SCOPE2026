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

The exact finite integer certificates are in `verify.py` and `kernel_basis.json`. Use `python3 verify.py` to reproduce `verification.log`: ranks for one through five markers, five independent rational-kernel witnesses checked by integer multiplication, and an explicit twelve-coordinate collision verified by directly enumerating each of its 36 graph neighbours. Use `python3 check_graph.py` to reproduce `graph_check.log` (3,131 separate marked graph instances). The modular-rank proof uses a nonzero minor modulo 1,000,003 to certify rational rank lower bounds and explicit independent integer null vectors for the upper bound.

This verifies the **finite matrix rank calculation**, not an exhaustive literature novelty claim. The theorem for all dimensions rests additionally on the abstract orbit classification, the distance-layer induction and the linear map identity given in `RESULT.md`. No failure of full iterative refinement at five markers is asserted. No independent audit has been performed.
