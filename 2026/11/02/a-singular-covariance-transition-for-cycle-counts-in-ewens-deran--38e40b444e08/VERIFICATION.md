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

# Verification and limits

Execute `python3 verify.py` with Python 3. It requires no third-party packages. The checked invocation returned `PASS: 2003 exact integer/rational assertions and asymptotic numerical comparisons`.

The verifier uses exact rational coefficients, an independently written recurrence for generating-function coefficients, exhaustive permutation enumeration only up to eight elements, and exact parity checks over finite ranges. It separately compares exact rational covariances to their analytic leading term at a large finite size. These do not prove asymptotic or universal statements; the full proof is in `RESULT.md`.

The exact mixed-moment expression is a specialization of previously published factorial moments. Verification of the additional strict finite sign and asymptotic scale is a mathematical proof exercise using alternating series and singularity asymptotics, not an independent external certification. The literature comparison is nonexhaustive and historical priority remains open to further assessment.
