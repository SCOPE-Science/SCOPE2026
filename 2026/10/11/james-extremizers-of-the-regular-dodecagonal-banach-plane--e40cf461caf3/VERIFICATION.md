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

Let \(P\) be the regular dodecagon with Euclidean circumradius \(1\), and put
\[
c=\cos\frac{\pi}{12}.
\]
Then
\[
cB_2\subseteq P\subseteq B_2,
\]
hence
\[
\|z\|_2\le N_{12}(z)\le\frac{\|z\|_2}{c}.
\]

For \(x,y\in S_{X_{12}}\),
\[
\|x+y\|_2^2+\|x-y\|_2^2
=
2\|x\|_2^2+2\|y\|_2^2
\le4,
\]
so one Euclidean chord has length at most \(\sqrt2\), proving
\[
J(X_{12})\le\frac{\sqrt2}{c}.
\]

The pair \(v_0,v_3\) is Euclidean orthogonal. Its sum and difference lie on dodecagon edge-normal rays, whose boundary radius is \(c\), so both normed chord lengths equal \(\sqrt2/c\).

If equality holds globally, then both Euclidean chord lengths must be at least \(\sqrt2\); the parallelogram identity forces both to equal \(\sqrt2\) and forces \(\|x\|_2=\|y\|_2=1\). The only dodecagon boundary points on the Euclidean unit circle are vertices. Equal Euclidean chord lengths force \(\langle x,y\rangle=0\), hence
\[
x=v_k,\qquad y=\pm v_{k+3}.
\]
This also verifies the converse.

No numerical sampling or external certificate is used as proof.
