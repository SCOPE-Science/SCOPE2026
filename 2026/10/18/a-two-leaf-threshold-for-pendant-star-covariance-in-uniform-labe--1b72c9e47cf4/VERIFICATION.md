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

# Reproducibility and evidence

Run `python verify.py` using Python 3 standard library. The script independently reconstructs all \(n^{n-2}\) Cayley trees from Prüfer words for each integer \(4\le n\le8\), counts leaf and exact pendant-star-centre statistics, and uses exact integer/Fraction arithmetic to verify both mixed moments and each prescribed pendant-star conditional probability mass function. It also checks 30,743 exact finite instances including the sign formula through order 250.

The analytic proof in `RESULT.md` establishes the theorem for every admissible \(n,k\) by a bijection, a conditional occupancy law and strict logarithmic bounds. The finite checks cannot certify all parameter values or scientific priority. The sign derivation was also rechecked algebraically from the displayed inequalities.
