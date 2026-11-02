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

# Verification and limits

Run `python3 verify.py` in a standard Python 3 environment, using no third-party libraries. It exhaustively enumerates square-zero block matrices \((X,y)\) and direct commuting-pair relations \(Xy'=X'y\), and checks the claimed degrees, total involution count and ordered-pair count. The ten tested sizes/fields comprise \((1,1,2)\), \((2,1,2)\), \((1,2,2)\), \((2,2,2)\), \((1,3,2)\), \((2,3,2)\), \((1,2,3)\), \((2,2,3)\), \((1,2,4)\), \((1,2,5)\). The fields of odd order are algebraic boundary tests, not involution cases; the finite field of order four uses a polynomial basis over \(\mathbb F_2\).

Observed marker: `THREE_BLOCK_INVOLUTION_DEGREE_CENSUS_OK 10 665`.

All infinite-parameter assertions depend on the proof in `RESULT.md`, not finite enumeration. The mathematical review is self-review only; no independent audit has been conducted.
