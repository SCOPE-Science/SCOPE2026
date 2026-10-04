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
Run `python3 verify.py` in the package directory.

The verifier regenerates both Pell families:
\[
a+b\sqrt2=\sqrt2(3+2\sqrt2)^t,\qquad t\ge1,
\]
and
\[
b+a\sqrt2=(2+\sqrt2)(3+2\sqrt2)^t,\qquad t\ge0.
\]

It checks every candidate with
\[
N<10^{38},
\]
verifies the Pell equations and parity conditions, and confirms that there are exactly \(25\) candidates from each family.

All coordinates in this finite range are below \(2^{64}\). The verifier uses the deterministic Miller--Rabin base set valid on that whole range, exact Pollard--Rho splitting, primality rechecks of every factor, and multiplication back to the original coordinate before evaluating divisor sums.

For family A it tests
\[
\sigma(a^2)+2=3\sigma(b^2),
\]
and for family B it tests
\[
3\sigma(a^2)+2=\sigma(b^2).
\]
Every residual is nonzero. The regenerated table must agree byte-for-byte with `pell_candidates.csv`.

The computation certifies only the finite cutoff. The global Pell reduction is proved symbolically in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
