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
The proof was checked at three levels.

1. **Admissibility.** Exact symbolic multiplication verifies \(V^{\mathsf T}V=I\) and \(\det V=1\). Therefore the displayed \(U_\alpha\) is unitary whenever \(|\alpha|=1\), and its outgoing column is exactly \(\alpha|\mathrm{in}\rangle\).
2. **Repeated resonance.** Exact determinant expansion verifies \(\det(zI-U_\alpha)=z^2(z-r)^2-\alpha(1-rz)^2\) with \(r=-1/\sqrt6\). At \(\alpha=0\), the nullities of \(U_0-rI\) and \((U_0-rI)^2\) are respectively one and two, establishing a genuine size-two Jordan resonance.
3. **Impulse response.** The rational function \(S(z)=(1-rz)^2/[z^2(z-r)^2]\) is expanded after the substitution \(w=z^{-1}\). The checker matches the closed formula for the first thirteen coefficients. The infinite statement is proved independently by the identity \((1-rw)^{-2}=\sum_{k\ge0}(k+1)r^kw^k\) and by the order-two residue formula.

The general multiplicity claim uses the standard residue formula for a pole of order \(m\). It proves only a degree-at-most-\(m-1\) polynomial factor in the time index; it does not assert generic attainment of that degree or classify all realizable resonance multiplicities.
