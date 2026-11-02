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

# Verification and scope

The analytic argument in `RESULT.md` is the source of the all-horizon classification. The program `checks/verify_fifth_resonance.py` uses Python 3 standard library and exact integer/rational arithmetic. From the package root, execute `python3 checks/verify_fifth_resonance.py`.

The program checks signed zero-frequency relations of total degrees one through five on 17 successive Fourier vectors. Degree five has exactly the expected two opposite sign patterns per consecutive time triple. Degree four has only pair cancellations, and no odd relation below degree five is found. All first-five cosine moments are checked as exact rational numbers for 10 horizon lengths, together with 58 recurrence identities. The finite search is **not** an exhaustive proof for all times: the independent analytic eigenvalue/Lucas argument in `RESULT.md` supplies the infinite proof.

Further numerical two-dimensional Haar-grid integration was used as an auxiliary check for several phase shifts and horizons. Grid integration is not a proof and is not required to run the standalone program. The result applies only to the unforced Möbius parameter \(\varepsilon=0\), and no independent audit is claimed.
