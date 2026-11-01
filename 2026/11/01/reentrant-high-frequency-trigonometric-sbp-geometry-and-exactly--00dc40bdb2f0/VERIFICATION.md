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

# Reproduction and independent-check limits

Use `python verify_fsbp.py` with SymPy and mpmath. The standalone script contains the analytic branch matrices and independently obtains the collocation derivatives by sampled-basis inversion, checks all entries of the SBP equation by exact symbolic simplification and high-precision evaluations, tests admissible and inadmissible parameter bands, validates the cardinal derivative obstruction against numerical inversion at arbitrary nonsingular interior nodes, and confirms the two unique-root approximations at 65-digit precision.

Observed execution: `VERIFY_OK 1319` and the root values:

```
CALIBRATED_MIDPOINT_FREQUENCY 4.02870132202535962396501666020650727836021013
CALIBRATED_OFFCENTER_FREQUENCY 5.06677716107025300202845072428169172203104922
CALIBRATED_OFFCENTER_POSITION 0.620037659782573913653161029170380786867476682
```

The theorem's existence, exhaustiveness, inequality ranges, and uniqueness of both calibration roots follow from the exact cardinal-function argument, explicit matrix identities, trigonometric signs, and strictly monotone residuals stated in `RESULT.md`. The verifier's finite samples are not exhaustive and are not a proof of those assertions. The scientific comparison included the general FSBP literature and the stated inspected sections; independent scientific audit is not performed.
