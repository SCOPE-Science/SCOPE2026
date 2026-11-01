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

Run `python3 verify.py` on Python 3.10 or newer. No third-party dependencies or external data are needed. The executable regenerates the 56-vertex Kneser graph, all eleven-element closed neighborhoods and all 111,482 nonempty faces. It validates each free simplex pair before removal and independently checks the 1,662-cell matching on all 4,190 Hasse incidences. It computes the complete attaching-word reduction, verifying the three exact elementary generator/relator cancellations and the final signed degree histogram `{-2: 60, 0: 299, 2: 47}`. Successful completion prints `ALL_VERIFY_OK`.

It additionally computes unsigned coefficient-field ranks of the original reduced 2-skeleton over characteristics two, three and five to cross-check the integral CW answer. These field computations are not a substitute for the attaching-word homotopy argument.

The calculation is finite and exact for the specified 56-vertex graph. It does not classify any larger Kneser graph, produce a symmetry action, or supply independent external validation.
