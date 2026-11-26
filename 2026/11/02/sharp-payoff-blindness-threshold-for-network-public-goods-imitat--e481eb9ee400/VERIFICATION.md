---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Verification report

Run `python3 verify.py`. The exact-rational checks directly accumulate payoffs over groups for every profile on \(C_4\) and \(K_5\) at selected synergy parameters. They check payoff blindness at \(\Theta=\varepsilon=0\) on \(C_4\) at \(r=9\), retained nonzero comparisons at positive equality, and neutrality above the maximum. The torus checks determine the stencil from group incidences and enumerate its free spins at side lengths 6, 7 and 10. The run printed `PASS: C4 and K5 boundary checks; exhaustive nonzero torus stencils for L=6,7,10`. The proof in `RESULT.md`, not these finite checks, establishes the general theorem.
