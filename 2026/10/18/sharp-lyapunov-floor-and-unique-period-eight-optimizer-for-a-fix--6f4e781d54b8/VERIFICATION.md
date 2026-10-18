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

# Mathematical and computational checks

The exact proof is in `RESULT.md`. The standalone `verify_sharp_lyap.py` uses only standard Python 3 and exact fractions; execute it from the same directory. The script verifies exact images and branches of the claimed primitive period-eight cycle, the return multiplier \((64/25)^2\), and four additional rational parameter examples in the asserted region. It also checks more than one thousand starting points for the absence of four consecutive outer visits over at most 48 forward steps each. Expected terminal message: `EXACT_PERIOD8_AND_FINITE_ITINERARY_CHECKS_OK`.

The universal four-visit and uniqueness claims depend on the analytical inequalities and affine itinerary argument, not on the finite tests. At the original branch boundaries the classical derivative need not exist; the claim explicitly excludes those orbits or measures charging the switching set. No independent audit has been performed.
