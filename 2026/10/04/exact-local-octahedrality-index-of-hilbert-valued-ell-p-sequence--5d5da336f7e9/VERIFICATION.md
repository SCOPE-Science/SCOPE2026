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

The theorem is checked analytically from the stated definitions; there is no numerical certificate.

For the lower bound when \(p\ge2\), the verification step is the coordinatewise identity
\[
\|x_\gamma\pm u_\gamma\|^2=2\|x_\gamma\|^2
\]
for \(u_\gamma\perp x_\gamma\) and \(\|u_\gamma\|=\|x_\gamma\|\). Summing \(p\)-th powers gives both global distances exactly \(\sqrt2\).

For \(1\le p\le2\), the relevant exact expression for a one-coordinate witness is
\[
1-a^p+(1+a^2)^{p/2},
\]
which tends to \(2\) as the selected coordinate norm \(a\) tends to \(0\). Infinite \(\Gamma\) guarantees such arbitrarily small coordinates for every fixed unit vector.

For the upper bound, the parallelogram law gives a coordinate minimum at most \(\sqrt{1+a^2}\), so the global minimum has \(p\)-th power at most
\[
1-a^p+(1+a^2)^{p/2}.
\]
Differentiating the nonconstant part gives
\[
pa\left((1+a^2)^{(p-2)/2}-a^{p-2}\right).
\]
Its sign is negative for \(p<2\), zero for \(p=2\), and positive for \(p>2\), giving the claimed maxima and hence the exact upper constants.

Limits: no finite-index result for \(p<2\), no one-dimensional-fibre extension, no arbitrary-fibre classification, and no \(p=\infty\) endpoint are asserted. Literature search is evidence for comparison only and is not used as a proof of novelty.
