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

# Verification scope

The standalone `check_bicylinders.py` runs from an extracted copy of this package and checks the defining radical relation, both outer-contact equalities, both contact-orbit masses, all three normalized Löwner covariance entries, the ellipsoid-volume ratio, and 24,000 combined finite random-point tests over eight radius ratios. The checks were actually executed, with successful output; the scientific conclusion rests on the general proof and exact contact moments in `RESULT.md`, not on sampling.

The global all-parameters algebraic proof, its assumptions, and its contact identities are recorded in `RESULT.md`. No independent validation or expert audit has been carried out. The scripts do not test whether earlier publications contained equivalent results; that is addressed as a qualified literature comparison in `REVIEW.md` and `AUDIT.json`.
