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

# Verification record

The self-contained `verify.py` was executed with Python 3, with only the standard library. It enumerates all subsets of each \(\binom n2\)-vertex ground set for \(n=5,6,7\), checks agreement between the local-degree and connected-component face tests, verifies all Hasse arrows acyclic, and independently obtains all integer Morse differentials by recursive gradient-path substitution and exact Schur-complement cancellation.

The output records 85, 405 and 1,911 nonempty faces; 180, 1,155 and 6,405 directed Hasse incidences; and 39, 185 and 747 matched pairs. Facet-count vectors are \( (0,0,30)\), \( (0,0,15,90)\), and \( (0,0,0,945)\). The critical cells are \((1,6)\), \((1,0,24,10)\) and \((1,0,8,408)\), in dimensions from zero. All Morse boundary entries vanish for the five- and six-point cases. The seven-point degree-three boundary has an eight-row, 408-column integral matrix with a determinant-\(-1\) minor selected by the procedure in `RESULT.md`.

The exact deterministic results are in `verified_output.txt` and end with `ALL_CHECKS_PASS`. This is a finite exhaustive verification of the specified three cases, not a computational proof of any untested larger-parameter statement. No independent audit is reported.
