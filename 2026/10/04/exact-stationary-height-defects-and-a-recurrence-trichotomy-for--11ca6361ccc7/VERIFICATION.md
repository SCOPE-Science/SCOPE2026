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

The mathematical core is algebraic. The included `verify.py` uses only the Python standard library and exact `Fraction` arithmetic to represent polynomials in \(x,y,z,\alpha\). It verifies the following identities exactly:
\[
L V=-\frac25x^2-\frac25y^2+3\alpha z^2,
\]
\[
L F_1=2\alpha\left[\left(z+\frac1{20}ight)^2-\frac1{400}ight]-\frac25x^2,
\]
\[
L F_2=\alpha\left[\left(z-\frac1{10}ight)^2-\frac1{100}ight]-\frac25y^2,
\]
\[
L z=\alpha z-5xy.
\]
It also verifies the determinant polynomial that gives the two nonzero equilibrium heights. Running the script on the packaged source prints `VERIFY_OK`; the recorded output is included in `verification_output.txt`.

The invariant-measure steps after these identities are analytic: integrate Lie derivatives against an invariant probability measure; use arbitrary continuous tests of \(z\) for the conditional law; and use invariance of the compact support for the equality cases. No finite numerical trajectory is treated as an infinite-time certificate.

A bibliographic limitation remains: the 1981 primary paper was not available for full-text inspection without a human publisher-verification step. The canonical equations and historical description were instead checked against later detailed sources that reproduce and discuss the original system.
