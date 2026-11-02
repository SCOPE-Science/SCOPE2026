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

Place `verify.py` beside this document and run `python verify.py` with Python 3, NumPy and SymPy available. On the recorded run, the script returned `PASS 4801 assertions` and printed the exact/approximate values for mixed Petersen and five-cycle examples. It checks the exact Petersen adjacency polynomial and rank-five Fiedler spectral projector, the \((2/3)I_3\) local Gram identity at all ten vertices, positivity and boundary identities for 1,140 pairs \((k,m)\), stochasticity and full numerical product spectra for six modest matrices, and seeded local edge-perturbation tests.

The exact analytical argument in RESULT.md—not finite enumeration or floating-point experiments—proves the universal minimax optimum and uniqueness. Tests of perturbed matrices are sanity checks only; they do not establish unrestricted optimization. Complete factors' edge transitivity and Fiedler projected-edge independence are checked separately in the proof. For the mixed family with one Petersen factor the computed holding is strictly positive; with two Petersen factors it is zero.

The bibliographic day 2007-09-06 refers to the first exact-day verified public preprint record. An earlier technical report is listed by the publisher only as May 2007. Independent audit: not yet performed.
