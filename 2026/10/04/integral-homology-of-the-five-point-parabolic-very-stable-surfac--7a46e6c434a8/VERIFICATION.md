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

The finite verifier models a degree-\(4\) del Pezzo surface as the blow-up of \(\mathbf P^2\) at five general points. In the basis \(H,E_1,\ldots,E_5\), it constructs the sixteen \((-1)\)-curve classes
\[
E_i,\qquad H-E_i-E_j,\qquad 2H-E_1-\cdots-E_5.
\]
Using the exact intersection form, it verifies that all sixteen classes have self-intersection \(-1\), every vertex of the incidence graph has degree \(5\), the graph has \(40\) edges, and it contains no triangles. Hence all pair intersections counted by the graph are distinct and there are no triple intersection points.

It then checks
\[
\chi(W)=16\cdot2-40=-8,
\]
\[
\chi(X)=3+5=8,
\]
and therefore
\[
\chi(Y)=16.
\]
With \(b_0=1\), \(b_1=10\), and no homology above degree \(2\), it checks \(b_2=25\).

The verifier does not replace the published identification of \(W\), the published computation \(H_1(Y,\mathbf Z)\cong\mathbf Z^{10}\), the finite-map description establishing affineness, or the Andreotti--Frankel--Hamm theorem. The Hopf-map conclusion additionally uses the published group homology \(H_2(\pi_1Y,\mathbf Z)\cong\mathbf Z^{25}\).

The saved replay output ends in `VERIFY_OK`.
