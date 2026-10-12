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
The proof is analytic.

For
\[
m=k+\delta,\qquad k=\lfloor m\rfloor,
\]
the pointwise integer inequality
\[
(n-k)(n-k-1)\ge0
\]
gives
\[
\mathbb E[\Theta(\Theta-1)]
\ge
k(k-1)+2k\delta.
\]
Equality holds on the adjacent support \(\{k,k+1\}\).

For
\[
0\le n\le K,
\]
the pointwise inequality
\[
n(K-n)\ge0
\]
gives
\[
\mathbb E[\Theta(\Theta-1)]
\le
m(K-1).
\]
Equality holds on the endpoint support \(\{0,K\}\).

Convex mixtures of the two extremizers preserve the mean and interpolate the factorial moment, proving that the entire interval is attainable.

The bundled checker evaluates these identities with exact rational arithmetic for many finite caps and replays the explicit threshold-separation certificate. The finite replay corroborates, but does not replace, the universal proof.
