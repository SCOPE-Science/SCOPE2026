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

# Reproducible checks

The proof in `RESULT.md` is the basis of the universal statement. As independent finite corroboration, run `python check_cube_sections.py` under Python 3. The program computes all vertices of relevant cube hyperplane sections from coordinate-edge intersections using exact `fractions.Fraction` arithmetic, then tests whether reflection in the arithmetic mean of the vertices preserves the vertex set.

The program reports 289 non-dominant sorted quadruples with positive integer entries 1 through 8, and six selected five-coordinate non-dominant cases; all exhibit a non-centrally-symmetric face. An additional 896 exact off-center sections corroborate the central-symmetry lemma including equality thresholds. Five dominant cases verify the coefficient inequality used to construct an affine-cube graph. Neither finite enumeration nor the successful program output substitutes for proving the quantified real-parameter statement. No external independent mathematical audit has been performed.
