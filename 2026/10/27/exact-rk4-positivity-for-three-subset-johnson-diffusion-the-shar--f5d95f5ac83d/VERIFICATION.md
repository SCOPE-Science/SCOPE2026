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

The attached `verify.py` uses the Johnson intersection-number recurrence to recompute all entries of the classical RK4 endpoint operator, then checks the printed transition-polynomial formulas symbolically with exact algebra. It verifies the cubic monotonicity discriminant, positivity certificate for the distance-two coefficient, and the integer sign change from 33 to 34 with exact identities. Separately it constructs graph adjacency matrices for every integer n from 6 through 12, calculates integer powers of the Laplacian generator, and compares the exact rational entries in a complete representative row at three rational timesteps for each n.

From the attached source, run `python verify.py` after installing the two packages listed in `requirements.txt`. A successful run reports:

`VERIFY_OK: 3 symbolic distance-transition identities, 6 sign/threshold certificates, 2100 independent exact rational matrix entries, sharp n=34 switch`

The finite matrix tests cannot certify the infinite range of sizes. That range is established by the coefficient and sign identities in `RESULT.md`. No independent human or external audit has occurred.
