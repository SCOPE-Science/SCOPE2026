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

# Reproduction
Run `python3 verify.py` with Python 3's standard library. The program reconstructs the Petersen edge list from disjoint two-subsets, enumerates its ten coordinate and fifteen fundamental-set facets, checks the odd-cycle condition, then exhaustively enumerates the integer compositions in degrees five through ten. The dimension-ten regularity cutoff is proved in the accompanying result; the computation is not used as a surrogate for that upper bound.

Expected minimum-generator counts by degree: `(5,1), (6,0), (7,10), (8,0), (9,0), (10,0)`; the ten degree-seven vectors are the closed-neighborhood exponent offsets. The Hilbert function `1, 15, 120, 670, 2895, 10303` independently yields the *known* h-vector `1, 5, 15, 25, 5, 1`. The verifier checks exact integers, not approximate ranks or numerical heuristics.

This verifies the stated monomial formula conditional on standard cited theorems (normality, facets, canonical interior and local duality). Independent external validation and historical-priority certification have not been performed.
