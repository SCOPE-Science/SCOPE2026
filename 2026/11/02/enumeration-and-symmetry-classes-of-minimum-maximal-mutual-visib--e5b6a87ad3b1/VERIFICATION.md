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
# Reproducibility
Run `python3 verify.py` with Python 3.10 or newer. The script enumerates every \((m+n-1)\)-element subset of squares for boards \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)\), checks visibility using all length-two rook geodesics, and checks maximality by inserting every available square. It asserts the labeled formula, the existence of a universal root vertex, and symmetry-orbit formulas under independent factor permutations on all but the largest board, including the full factor-swap quotient in balanced cases. The actual source path and embedded source bytes are identical at generation time. Output ends in `VERIFY_OK`, after reporting 145180 candidate subsets.

# Proof versus computation
The all-parameter statement is derived mathematically in `RESULT.md` by converting to bipartite four-cycle saturation, characterizing the minimum edge layer as diameter-at-most-four trees, counting universal-center descriptions with double-star subtraction, and classifying pendent-neighbor profiles using integer partitions. Exhaustive small-board checks are not a claim of proof by computation. The symmetry check omits \((4,5)\) only for runtime reasons; the formal orbit argument covers it. Independent mathematical review remains unperformed.
