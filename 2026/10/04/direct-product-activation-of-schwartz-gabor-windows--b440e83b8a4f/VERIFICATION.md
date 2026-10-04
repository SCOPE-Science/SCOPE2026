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

The verification is exact and algebraic.

For two phase-space lattices,
\[
(\Lambda_1\oplus\Lambda_2)^\circ
=
\Lambda_1^\circ\oplus\Lambda_2^\circ
\]
because the direct-sum symplectic pairing splits factorwise. Hence
\[
(\Lambda_1\oplus\Lambda_2)_{\mathrm{int}}
=
\Lambda_{1,\mathrm{int}}
\oplus
\Lambda_{2,\mathrm{int}}.
\]
Finite subgroup indices multiply, and therefore the positive square-root indices satisfy
\[
\nu(\Lambda_1\oplus\Lambda_2)
=
\nu(\Lambda_1)\nu(\Lambda_2).
\]

Iteration gives
\[
\nu(\Lambda^{\oplus k})=\nu^k,
\qquad
\nu((\Lambda^{\oplus k})^\circ)=r^k.
\]
Substituting these exact identities and product dimension \(kd\) into the primary source's exact rational multiwindow formula gives
\[
q_{\min}^{\mathcal S}(\Lambda^{\oplus k})
=
\left\lceil
\frac{r^k+kd}{\nu^k}
\right\rceil.
\]

The one-window condition is therefore
\[
\nu^k-r^k\ge kd.
\]
When \(\nu>r\),
\[
\nu^k-r^k
\ge
(\nu-r)\nu^{k-1},
\]
so activation occurs at a finite power.

For the primary-source example
\[
(d,\nu,r)=(2,2,1),
\]
the exact window counts are
\[
\left\lceil\frac3{2}\right\rceil=2,\qquad
\left\lceil\frac5{4}\right\rceil=2,\qquad
\left\lceil\frac7{8}\right\rceil=1.
\]

No numerical approximation or finite search is used in the proof.
