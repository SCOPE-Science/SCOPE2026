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

The analytic proof is primary. The only finite certificate needed is the root-of-unity bookkeeping after the equilateral-triple reduction.

`verify.py` uses exponents modulo \(15\). It enumerates all six permutations \((p,q,r)\) of \((0,1,2)\) and all fifth-root choices solving \(t^5=\omega^q\). It then forms the normalized coefficient triples dictated by the proof, deduplicates them, and checks equality with the two canonical families
\[
(1,t\omega,t^2\omega,t^3),\qquad (1,t\omega^2,t^2\omega^2,t^3),\qquad t^5=1.
\]
The result is exactly ten normalized vectors. For every canonical vector, each of the two independent cyclic autocorrelations is checked to be a rotated copy of the three cube roots, so it vanishes exactly through \(1+\omega+\omega^2=0\).

The checker also verifies that the third-root witness and the fifteenth-root witness recorded in arXiv:1910.00924v1 occur in the classified set.

Limits: the checker does not replace the geometric lemma that three unit complex numbers summing to zero form an equilateral triple; that lemma is proved directly in the mathematical argument. No claim is made for supports other than \(\{0,1,2,3\}\subset\mathbb Z_5\).
