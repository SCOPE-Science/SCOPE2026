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

Run `python3 checker.py` with a standard Python 3 installation. The program generates the finite words directly from the defining binary morphism, enumerates the positions of every substring of the tested lengths, and independently derives length-\((G+2)\) minimal absent candidates from the length-\((G+1)\) factor set. For each level \(2\le k\le7\) it checks both repeated length-\(G\) substrings and their exact start positions, uniqueness of all length-\((G+1)\) factors, and equality of the computed maximal MAWs with the formula in the result. For \(k=2,3,4\), it also enumerates all MAWs through the full possible word-length range, thereby checking maximality without using the proof's upper bound.

Observed successful sample host lengths: \(9,27,81,243,729,2187\); all assertions passed. These are finite consistency checks, not an exhaustive verification over all substitution levels. The unrestricted claim is justified by the full recursive border and extension argument in `RESULT.md`. Historical originality remains subject to priority uncertainty. No independent or machine-formal mathematical audit is claimed.
