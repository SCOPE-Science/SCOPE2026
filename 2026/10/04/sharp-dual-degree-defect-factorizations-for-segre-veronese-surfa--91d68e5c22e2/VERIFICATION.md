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

The symbolic proof uses the jet exact sequence and the intersection ring of \(\mathbb P^1\times\mathbb P^1\). The critical computed class is
\[
c_2(J_1(\mathcal O(a,b)))=4-4a-4b+6ab.
\]
The lower defect is checked by the exact identity
\[
(6ab-4a-4b+4)-2ab=4(a-1)(b-1),
\]
and the upper defect by
\[
6ab-8\sqrt{ab}+4-(6ab-4a-4b+4)=4(\sqrt b-\sqrt a)^2.
\]
For fixed \(D\), the only analytic input is that \(u+D/u\) has derivative \(1-D/u^2<0\) for \(0<u<\sqrt D\).

The bundled checker uses integer arithmetic to enumerate all factor pairs for \(1\le D\le5000\), verifies unique minima and maxima, and checks the radical upper bound after squaring nonnegative quantities. It separately checks the jet-class polynomial for \(1\le a\le b\le100\). The output reports 21,723 factor pairs checked. Finite regression does not establish the universal theorem; it is only an independent implementation check of the formulas and equality logic.
