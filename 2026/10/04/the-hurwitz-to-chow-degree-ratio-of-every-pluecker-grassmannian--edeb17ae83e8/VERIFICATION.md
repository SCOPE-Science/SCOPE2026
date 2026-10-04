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
The proof uses three exact identities:
\[
T_{\operatorname{Gr}(k,n)}\simeq S^\vee\otimes Q,
\qquad
K_{\operatorname{Gr}(k,n)}=-nH,
\]
\[
2g-2=(k(n-k)-n-1)D,
\]
and
\[
\operatorname{Hdeg}=2D+2g-2.
\]
Combining them gives
\[
\operatorname{Hdeg}
=
(k-1)(n-k-1)D.
\]

The coisotropic-polar correspondence identifies the Hurwitz degree with
\[
\delta_1,
\]
while
\[
\delta_0=D.
\]

The bundled checker evaluates the standard hook-length expression for the Pluecker degree through \(n=120\), checks duality, verifies that the sectional-genus numerator is even, and replays the final degree identity. These finite tests are regression evidence only.

Limits: ordinary complex Grassmannians, minimal Pluecker embedding, and only the first two polar degrees.
