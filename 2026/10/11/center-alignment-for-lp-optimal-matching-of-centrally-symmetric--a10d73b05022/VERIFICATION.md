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

For centered centrally symmetric bodies,
\[
g(u)=h_{QA}(u)-h_B(u)
\]
is even. A residual translation \(z\) changes the support-function difference to
\[
g(u)+z\cdot u.
\]
Antipodal pairing gives
\[
\frac12\left(
|g(u)+z\cdot u|^p+
|g(u)-z\cdot u|^p
\right).
\]
Strict convexity of
\[
x\mapsto|x|^p
\]
for \(p>1\) makes this at least
\[
|g(u)|^p,
\]
with equality exactly when
\[
z\cdot u=0.
\]
For nonzero \(z\), this fails only on a great subsphere of measure zero, so the integrated inequality is strict.

The checker supplies two independent regression layers. It verifies the paired inequality on deterministic grids for several real exponents greater than \(2\), including nonintegral exponents. It also numerically integrates an even trigonometric function plus several nonzero linear translation modes around the circle and verifies strict increase relative to zero translation.

For \(p=4\), the checker additionally verifies the exact polynomial identity
\[
(r+s)^4+(r-s)^4-2r^4
=
12r^2s^2+2s^4.
\]
These finite checks are not used as a proof of the continuum statement.
