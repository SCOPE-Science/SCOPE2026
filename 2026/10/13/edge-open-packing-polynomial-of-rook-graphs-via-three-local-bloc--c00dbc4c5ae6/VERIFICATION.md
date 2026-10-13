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

# Verification summary

Run `python3 eop_rook_verify.py` with Python 3 and no third-party packages. The included `eop_rook_verification_output.txt` records the observed output.

The direct checker constructs every rook graph edge, tests every edge subset for the existence of a forbidden third edge joining endpoints of two distinct selected edges, and compares exact polynomials for nine boards. The nine exhaustive boards have a total of 328221 candidate edge subsets. The two larger boards (3-by-4 and 4-by-4) receive 217579 additional direct checks among sets of size no greater than the proved maximum; their remaining subsets are not individually tested. The separate triple-factorial enumeration and distinguished-row recurrence, together with symmetry, one-edge counts and extremal degree, agree on 225 side-length pairs with 0 through 14 rows and columns.

All arithmetic is exact integer arithmetic. Finite exhaustion on specific boards does not certify a statement at arbitrary size; the proof uses induced-star structure, disjoint label blocks, and the labeled exponential formula. Other graph products and asymptotic distributions remain outside the theorem.
