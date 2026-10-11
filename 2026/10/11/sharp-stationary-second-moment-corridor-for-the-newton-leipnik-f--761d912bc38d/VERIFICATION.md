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

The algebraic certificate `verify.py` expands the Lie derivatives of \(F_1=x^2/2+z^2\) and \(F_2=(y^2+z^2)/2\), checks the reduced Cauchy–Schwarz polynomial, solves its roots exactly, and substitutes both nonzero equilibrium branches into the three vector-field equations.

Its recorded output in `verification_output.txt` is `VERIFY_OK` and prints the exact roots \(637/928-35\sqrt{257}/928\) and \(637/928+35\sqrt{257}/928\), together with their decimal values.

The certificate verifies algebraic identities only. The infinite-time statement rests on invariance of the probability measure and the analytic equality case of Cauchy–Schwarz; no finite numerical trajectory is used as a substitute for those arguments.

The theorem is limited to compactly supported invariant Borel probability measures of the nominal Newton–Leipnik flow. It does not verify existence, uniqueness, or physicality of a chaotic invariant measure.
