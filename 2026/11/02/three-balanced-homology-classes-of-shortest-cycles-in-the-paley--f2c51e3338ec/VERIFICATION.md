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

# Reproducibility and verification

Execute `python3 check_paley13.py` with Python 3 standard library. Expected final marker: `PALEY13_FLAG_TORUS_SYSTOLE_EXACT_OK`.

The program derives the full edge set from quadratic residues, the entire clique triangle set, boundary rank over the two-element field, all distinct simple four-edge cycles, two explicit independent degree-one cocycles and their evaluations, and the full \(78\)-element affine group action. It asserts each necessary cardinality and pair of independently discriminating cohomology values; failure causes a nonzero exit. The mod-two chain rank supplies the dimension needed to interpret cocycle pairings as complete classes.

The proof in `RESULT.md` derives total cycle count from common-neighbor cardinalities and identifies all essential cycles as an entire affine orbit; the checker reconstructs that orbit from the original group action. No numerical approximation or unverified extrapolation is used.

The established toroidal embedding and general length-spectrum background are attributed to the two referenced scholarly sources. No independent audit or external validation has been performed. Literature access cannot exclude every classical or unindexed equivalent computation.
