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

# Reproducibility and limits

The closed-form scalar numerator and its first parameter derivative are derived in `RESULT.md` from radial monomial beta moments. To reproduce the exact finite checks, run `python3 check.py` with Python 3. No packages or network access are required. The checker reports: `PASS: 75 exact rational assertions; k=1..12 derivative and sign; four exact root brackets.`

The sign for every \(k\ge1\), existence of local analytic root branches and their exact disk count are established analytically in the proof. Finite exact-rational tests do not certify infinitely many parameters. The proposed law does not count the root at \(s=0\) as an attainable punctured-disk fibre, and applies only for sufficiently small negative \(\beta\) at each fixed \(k\). Historical priority is assessed against identified sources but not independently certified.
