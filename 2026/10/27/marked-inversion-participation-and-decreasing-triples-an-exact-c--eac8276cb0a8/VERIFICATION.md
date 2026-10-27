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

# Reproduction and mathematical limits

Run `python3 verify_degree_triangles.py` with Python 3 (standard library only). It exhaustively enumerates the \(n!\) permutations for every \(n\in\{3,4,5,6,7,8\}\), testing every marked position's covariance, mean, and degree variance exactly, without floating-point arithmetic. It also reconstructs the exact local overlap summation for selected \(n\) up to \(1000\), tests positivity and reflection symmetry, and integrates the first-order projection polynomial with exact fractions to obtain \(13/7200\).

Expected final line: `VERIFY_OK`.

The finite checks do not certify the unrestricted formula or a limiting theorem. Those are established by the four-index covariance classification, algebraic summation, bounded-kernel first-order projection, and Riemann-sum argument in `RESULT.md`. The leading variance constant is corroborated by previously published asymptotics. No independent audit is asserted.
