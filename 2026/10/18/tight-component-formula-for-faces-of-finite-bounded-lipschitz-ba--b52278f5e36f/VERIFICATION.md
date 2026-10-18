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

# Exact computational checks and limits

Execute `python3 verify_bl_graph.py` with Python 3, no external packages. The script constructs complete active constraint normals from the formula defining the finite bounded-Lipschitz unit ball, computes their ranks over the rational numbers, and compares the resulting minimal-face dimensions to the tight-component formula. It covers 46,000 normalized boundary configurations on sampled weighted shortest-path metrics and line metrics, plus the two contrasting four-point cases in the motivating 2023 paper. The output includes `PASS exact minimal-face dimension versus tight-component formula` when all checks succeed.

The algebraic proof in `RESULT.md` applies to every real-valued nonconstant boundary function on every finite genuine metric space. The rational checker does not exhaust all metrics, certify originality, prove the full theorem, or provide independent scientific review. The single-point and constant endpoints are established separately in the displayed proof.
