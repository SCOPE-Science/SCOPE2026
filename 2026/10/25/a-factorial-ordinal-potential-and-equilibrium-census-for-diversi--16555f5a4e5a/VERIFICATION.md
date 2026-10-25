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

Run `python3 verify.py` using only the Python standard library. The program enumerates every \(0,1,2\)-labeled occupancy of the two parts with at least one vacancy and at least two agents for \(2\le A,B\le5\). It directly recomputes each mover's fractional utility and the independently evaluated factorial potential, checks the strict ordinal inequality for each profitable cross-part vacancy jump, then compares a separately derived closed polynomial to observed red counts of equilibria. It repeats the potential test for four additional three-/four-type families. Actual completed output: `PASS 125760 two-color configurations; 80 exact equilibrium polynomials; 18965 three/four-color configurations; 508416 strict moves`.

This executable is a finite reproducibility check. It does not enumerate unbounded networks, all possible numbers of types, or external literature, and thus does not alone establish the theorem or originality. Universal proof details and occupancy boundary cases appear in `RESULT.md`.
