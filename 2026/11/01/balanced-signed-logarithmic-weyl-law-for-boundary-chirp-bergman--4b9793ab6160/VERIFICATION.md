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

The analytic reduction uses the weighted monomial eigenbasis and the beta-moment identity. The critical asymptotic lemma is DLMF formula 13.8.11 for Tricomi's function at fixed nonreal argument; its principal-branch evaluation and the subsequent \(K\)-Bessel expansion are written explicitly in `RESULT.md`. The phase-density step uses Weyl's criterion and an \(O(\sqrt N)\) exponential-sum estimate. The signed counting law is obtained by two-sided spectral cutoffs. These infinite statements have been proved in the text, not inferred from numerical calculations.

The exact finite checks are in `CHECK.py`; `requirements.txt` pins the sole nonstandard dependency, `mpmath==1.3.0`. Run `python -m pip install -r requirements.txt` and `python CHECK.py` from this directory. The checker compares finite beta moments with a separate exponential-integral binomial representation, tests large-parameter complex amplitudes and phases for multiple weights and frequencies, verifies signs away from phase crossings, and tests several finite phase proportions. In the executed environment the program printed `PASS: 98 finite assertions (mpmath 1.3.0).` Numerical observations do not supply uniform error bounds, infinite density proofs, or independent validation.

There is no claimed external mathematical audit or publication-priority certification. The formula applies for fixed \(\alpha>-1\), \(c>0\), and real \(\vartheta\); no joint-uniformity assertion is made at parameter endpoints.
