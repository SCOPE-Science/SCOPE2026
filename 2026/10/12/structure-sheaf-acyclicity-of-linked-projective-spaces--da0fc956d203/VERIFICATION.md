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

The proof is symbolic and theorem-driven; no finite computation is used.

The source-side chain checked in arXiv:2609.37634v1 is:

1. The Mayer--Vietoris simplicial resolution for a simple-normal-crossings scheme is exact.
2. A linked projective space \(X\) is simple normal crossings.
3. Every nonempty component intersection \(X_\Delta\) is the scheme-theoretic image of a rational map from a projective space. Since the same intersection is smooth by simple normal crossings, it is a smooth projective unirational variety.
4. Over \(\mathbb C\), smooth projective unirational varieties satisfy
   \[
   H^q(X_\Delta,\mathcal O_{X_\Delta})=0
   \quad(q>0),
   \]
   while integrality and projectivity give \(H^0(X_\Delta,\mathcal O)=\mathbb C\).
5. Therefore the hypercohomology spectral sequence of the simplicial resolution has only the row \(q=0\), so
   \[
   H^i(X,\mathcal O_X)\cong H^i(\mathcal D(X),\mathbb C).
   \]
6. In the proof of the Hilbert-polynomial theorem, the source defines simplicial complexes \(K_a\) and proves them contractible when \(|a|\le r\). For \(a=0\), every independence polytope contains \(0\), so \(K_0\) has exactly the nonempty component intersections as faces:
   \[
   K_0=\mathcal D(X).
   \]
7. Hence \(\mathcal D(X)\) is contractible and
   \[
   H^0(X,\mathcal O_X)\cong\mathbb C,
   \qquad
   H^i(X,\mathcal O_X)=0
   \quad(i>0).
   \]

A consistency check is that this implies
\[
\chi(X,\mathcal O_X)=1,
\]
which agrees with evaluating the source's diagonal Hilbert polynomial at the zero multidegree. That Euler-characteristic agreement is only a check; it is not used to infer the individual vanishing groups.

The result is limited to complex linked projective spaces. No positive-characteristic extension, line-bundle vanishing theorem, or flat degeneration is claimed.
