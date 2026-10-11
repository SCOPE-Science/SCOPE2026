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

The proof is exact and finite after the convexity reduction. The unit ball has six vertices. Simultaneous application of the isometries \(R(s,t)=(t,t-s)\) and \(S(s,t)=(t,s)\), together with the invariance under \(y\mapsto-y\), partitions the 36 ordered vertex pairs into one 12-pair class with \(y=\pm x\) and one 24-pair class containing every other pair.

For \(m\in[0,1/2]\), the nontrivial representative \(x=(1,1)\), \(y=(1,0)\) has
\[
N(mx+(1-m)y)=1,
\]
\[
N(mx-(1-m)y)=1-m,
\]
\[
N(x-y)=1,\qquad N(x+y)=2.
\]
These are interval identities, not sample-based observations. They yield \(1+\frac32m-2m^2\). The same/opposite class yields \(1\).

`verify.py` checks the six vertices, the isometry action, the complete two-orbit partition, exact rational values at several parameters, and the maximizing value \(41/32\) at \(m=3/8\). Running it with the Python standard library prints `VERIFY_OK`.

No infinite computation, numerical optimization, or external certificate is used. The only literature-dependent premise is the published definition and lambda symmetry of the four-term constant; the remaining argument is self-contained.
