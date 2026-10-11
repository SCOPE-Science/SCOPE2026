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
# Verification

The exact reproducing-kernel differentiation, the quadratic boundary numerator, the signs at \(z=\pm1\), the positive coefficient difference and the discriminant are displayed in RESULT.md. The standard-library script `verify.py` exactly expands the numerator as a polynomial in three variables and checks all needed algebraic identities over rational coefficients.

Run `python3 verify.py` next to this document. The expected first line is `Exact polynomial and discriminant identities: PASS`. The script was run successfully on the packaged source; it performs exact symbolic calculations, not finite experimental guesses.

The proof of the universal root-location assertion uses positivity of \(A-C\), \(P_t(1)\) and \(P_t(-1)\) in the specified parameter range, root-product arguments for real or conjugate roots, and a sign-change argument after the critical parameter. The passage from the limiting point \(w=-1\) to actual \(w\in\mathbb D\) uses standard continuity of polynomial roots, and does not require assuming a root at an inadmissible boundary point.

Not established: classifications for higher derivatives, weighted disks, other domains or position-dependent coefficients. Independent audit has not been performed.
