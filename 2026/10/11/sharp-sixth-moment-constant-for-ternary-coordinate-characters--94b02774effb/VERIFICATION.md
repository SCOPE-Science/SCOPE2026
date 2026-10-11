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
The proof is analytic and valid for every integer \(n\ge2\). The critical identity is
\[
\|F_a\|_6^6=6S^3-9SQ+3R+|T|^2,
\]
with \(S=\sum|a_j|^2\), \(Q=\sum|a_j|^4\), \(R=\sum|a_j|^6\), and \(T=\sum a_j^3\). The additional \(|T|^2-R\) term is exactly the order-three resonance omitted by the ordinary Steinhaus sixth moment.

The sharp optimization uses only two inequalities and one strict smoothing identity:
\[
|T|^2\le\left(\sum x_j^{3/2}\right)^2\le\sum x_j^2,
\]
for \(x_j=|a_j|^2\) and \(\sum x_j=1\), followed by
\[
2h((u+v)/2)-h(u)-h(v)=\frac{(u-v)^2(16-9(u+v))}{4},\qquad h(t)=3t^3-8t^2.
\]
Because \(u+v\le1\), pairwise averaging is strictly improving unless the two masses agree. The unique maximizing mass vector is therefore uniform. Equality in the phase bound requires all \(a_j^3\) to have one argument.

`verify.py` checks the exact moment identity numerically by full enumeration for several dimensions, verifies explicit extremizers, and performs deterministic random stress tests. These computations are corroborative; they do not replace the all-dimensional proof. The script was replayed from the packaged path before serialization.
