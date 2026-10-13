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

# Verification and reproducibility

The proof is in `RESULT.md`; the companion code `verify.py` is a finite diagnostic that checks its algebra and parameter matching. From a folder containing the two files, run `python3 verify.py` with Python 3 and no third-party dependencies.

The script independently evaluates \(\frac{d}{dx}[x^2f_{|C+m|}(x)]\) in partial fractions and in the factored polynomial representation with exact rational arithmetic for 1,584 input pairs, including shifts inside and outside the claimed boundary. It checks positive polynomial signs for rational shifts satisfying \(3m^2\le1\), tests the explicit negative-leading-coefficient obstruction at four shifts outside the boundary, and compares the complex characteristic functions of the Cauchy/positive-stable mixture and its claimed strictly stable law at several parameters. The actual run returned: `PASS: 2530 exact-rational and finite complex-analytic identity checks`.

None of these finite checks constitutes proof of monotonicity for every real \(x\) or every parameter. Those quantifiers are justified analytically by the quartic's coefficients, the integral representation of independent scaling, and identity of holomorphic Laplace transforms. The conditional mixture identity does not rely on simulated positive-stable variables. No independent scientific audit has been performed.
