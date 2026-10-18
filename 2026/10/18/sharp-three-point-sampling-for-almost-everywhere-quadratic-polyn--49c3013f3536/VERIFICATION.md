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

# Verification notes

The analytic certificate is the explicit two-root polynomial for the squared leading-coefficient magnitude, followed by real-linear inversion and a single scalar energy test. The nonzero constant term of the false-branch energy polynomial proves measure-zero ambiguity without random sampling assumptions. The lower-bound argument uses real dimension five modulo global phase and maximal Jacobian rank of the polynomial observation map.

Run `python checker.py` from the same directory. The Python standard library is sufficient. The program checks the exact integer example without tolerance, checks the competing energy values using rational arithmetic, computes Fourier moments from three samples, and tests the reconstruction on 1,000 fixed-seed complex triples. Its observed output is embedded as `checker.out`.

The random tests are finite and are not offered as a proof of the almost-everywhere or minimality statements. The analytic proof, exact integer witness, and direct coefficient identities stand independently of them. Degenerate strata and quantitative numerical conditioning are outside the claim.
