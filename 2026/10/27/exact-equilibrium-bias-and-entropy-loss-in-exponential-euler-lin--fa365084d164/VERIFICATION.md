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

# Verification

Run the included standard-library Python 3 script with `python verify.py`. It re-evaluates the diagonal Kraus jump integral and no-jump contribution against the claimed transition matrix on seeded connected weighted graphs, checks nonnegativity, column sums, detailed balance, stationary laws, unitality/degree regularity and all off-diagonal two-mode contraction factors. It also tests the two-vertex fixed-coherence exception and the exact three-vertex witness, including the fourth-order entropy coefficient and stiff-step stationary limit.

Verified local execution: `PASS 109276 assertion families, including off-diagonal coherence blocks, diagonal Kraus evaluation, exact stationary law and entropy coefficient`.

The script is a finite floating-point corroboration only. No finite random or deterministic test certifies universal graph statements, infinitesimal asymptotics, or publication priority. The universal mathematical conclusions follow from the analytic proof in `RESULT.md`. Some very stiff test cases approach roundoff/underflow; exact inequalities in the proof, not finite-precision strict comparisons, establish their boundaries.

Independent audit has not been performed.
