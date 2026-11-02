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

The mathematical proof is self-contained and has five independent steps: the coordinate Frobenius identity, Fitting preperiod partition, normal-basis fixed-point counting, exact multipartite binary adjacency power ranks and multipartite stable-orbit formula. All vector spaces, field extensions, ranks and period quantifiers are explicitly defined in `RESULT.md`.

Run `python3 check_dynamics.py` using Python 3 standard library only. The script independently generates full state transition functions over selected binary fields, enumerates actual cycles and first-entry preperiods, and compares every observed count to the claimed formulas. Its successful diagnostic is `EVOLUTION_SQUARE_ORBIT_CENSUS_OK 21`; the attached `verification_output.txt` contains the complete output of the 21 enumerations, including the finite-extension fixed-point discrepancy for \(K_{1,1}\).

Exhaustive checks over finitely many graphs and fields corroborate the argument but do not prove the universal formulas. The algebra's multiplication is nonassociative, so map iterates must not be confused with associative powers. Cycle-length/preperiod-depth totals do not determine root-by-root tree branching. No independent audit has been carried out.
