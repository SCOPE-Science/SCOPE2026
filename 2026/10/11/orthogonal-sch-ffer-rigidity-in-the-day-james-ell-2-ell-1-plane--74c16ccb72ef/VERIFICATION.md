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

For a same-sign Euclidean point,
\[
\|x+y\|^2=1+\frac{1+r^2}{(1+r)^2}\ge\frac32,
\]
with equality exactly at \(r=1\).

For an opposite-sign taxicab point,
\[
\|x+y\|^2=\frac32+2\sqrt2\,u+2u^2\ge\frac32,
\]
with equality exactly at \(u=0\).

At an axis junction, every unit Birkhoff direction satisfies
\[
\|x+y\|^2=2+\frac{2\tau}{\sqrt{1+\tau^2}}\ge2.
\]

Thus the global minimum is \(\sqrt{3/2}\), and equality occurs exactly for the balanced diagonal/taxicab pair under the stated norm symmetries and order reversal. No numerical sampling is used as proof.
