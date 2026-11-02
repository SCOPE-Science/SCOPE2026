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

# Reproducible finite checks

Run `python3 rook_rank_verifier.py` with Python 3 and no third-party packages. The source enumerates finite first-order extension types using first-appearance row/column orbits, plus a fully separate direct-vertex method for smaller cases. The output in `rook_rank_verifier_output.txt` is the actual execution record.

The orbit implementation compares all rectangular rook graphs with sorted side sizes between 2 and 7, at quantifier ranks 2 through 5. It checks the resulting equivalence relation against sorted truncated side sizes and the exact class count. A direct recursion on graph vertices, without orbit reduction, covers side sizes between 2 and 4 through rank 4. Further combinatorial enumeration verifies clique and independent-set maxima on that small range.

These checks do not exhaust arbitrarily large side sizes or quantifier ranks. The infinite mathematical proof rests on the coordinate-equality Ehrenfeucht–Fraïssé strategy in `RESULT.md`; neither finite outputs nor source-code execution constitute independent expert audit.
