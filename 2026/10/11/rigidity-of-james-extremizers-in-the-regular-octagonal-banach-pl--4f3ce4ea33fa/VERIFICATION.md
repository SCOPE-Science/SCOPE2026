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

After symmetry reduction,
\[
x=(1,t),\qquad0\le t\le\sqrt2-1.
\]
Four of the five upper-half boundary pieces for \(y\) force one of \(N(x+y)\) or \(N(x-y)\) below \(\sqrt2\), except for the shared endpoint.

On the top edge
\[
y=(a,1),\qquad-(\sqrt2-1)\le a\le\sqrt2-1,
\]
the two extremality conditions are
\[
N(x+y)\ge\sqrt2\Longleftrightarrow a+t\ge0,
\]
\[
N(x-y)\ge\sqrt2\Longleftrightarrow a+t\le0.
\]
Hence \(a=-t\), so \(y=Qx\), and direct substitution gives
\[
N(x+y)=N(x-y)=\sqrt2.
\]
Conjugation by a regular-octagon symmetry changes \(Q\) at most to \(-Q\), yielding the global condition \(y=\pm Qx\).

No numerical sampling or external certificate is used as proof.
