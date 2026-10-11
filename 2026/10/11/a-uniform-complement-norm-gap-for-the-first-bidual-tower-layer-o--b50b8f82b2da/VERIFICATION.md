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

# Analytic verification and scope

The proof requires no external software, infinite certificate, or numerical extrapolation. Its critical checks are:

1. If \(Q\) is a norm-one projection onto the pullback of \(C(K)\) under \(\pi:L\to K\), then \(J^{-1}Q\) is unital and contractive; evaluation at \(u\) has a representing probability measure supported on \(\pi^{-1}(u)\). The probability conclusion uses total mass \(1\) and total variation at most \(1\).
2. For a point \(y\) with \(\mu\{y\}\le1/3\), the signed measure has exact variation \(\|\delta_y-\mu\|=2(1-\mu\{y\})\ge4/3\). This is an operator-norm lower bound, not just a scalar heuristic.
3. For \(E=C(\beta\Gamma)\), separating the \(\ell_1(\Gamma)\) and remainder-measure bands gives \(E^{**}=\ell_\infty(\Gamma)\oplus_\infty C(U)^{**}\), and the canonical map has the graph form shown in the proof. The associated spectrum map includes both the identity copy of \(U\) and at least two additional lifts over one remainder point.
4. Disjoint infinite subsets of \(\Gamma\) supply infinitely many disjoint nonempty clopen sets of \(U\), so \(C(U)\) contains \(c_0\), is nonreflexive, and its canonical bidual embedding cannot be onto. The corresponding spectrum map cannot be injective.
5. Restricting any tower projection to its second positive level preserves the norm-one projection property and its complement norm is bounded above by that of the full operator. The canonical adjoints \((J_{X^{(2n-1)}})^*\) supply compatible norm-one retractions, so the class being bounded is nonempty.

A three-point finite model with equal averaging weights attains the local \(4/3\) fiber inequality; it is not asserted to establish the optimal coefficient on the completed infinite tower. The only claimed general bound is \(4/3\), and no statement about independent validation is made beyond the status recorded above.
