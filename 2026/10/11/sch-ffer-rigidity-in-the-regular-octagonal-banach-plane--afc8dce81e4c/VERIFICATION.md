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

Let \(r=\sqrt2-1\). By regular-octagon symmetries and \(y\mapsto-y\), reduce to
\[
x=(1,t),\qquad0\le t\le r,
\]
with \(y\) on the upper half of the unit sphere.

The right and left vertical pieces give one chord of norm \(2\). The upper-right slanted piece gives \(N(x+y)>\sqrt2\). The upper-left slanted piece gives \(N(x-y)>\sqrt2\), except at the endpoint shared with the top edge.

On the top edge
\[
y=(a,1),\qquad-r\le a\le r,
\]
one has
\[
N(x+y)\le\sqrt2\Longleftrightarrow a+t\le0,
\]
and
\[
N(x-y)\le\sqrt2\Longleftrightarrow a+t\ge0.
\]
Hence the Schäffer objective can equal \(\sqrt2\) only when \(a=-t\), which is \(y=Qx\). In that case both chord norms are exactly \(\sqrt2\).

Conjugating back by a dihedral symmetry changes \(Q\) at most to \(-Q\), so the complete global equality condition is \(y=\pm Qx\).

No finite sampling or external certificate is used as proof.
