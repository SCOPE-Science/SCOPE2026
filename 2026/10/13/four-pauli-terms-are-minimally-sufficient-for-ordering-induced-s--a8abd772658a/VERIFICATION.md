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

The proof is analytic. Its critical checks are:

1. \(R\) commutes with \(P\) and \(Q\), so both the Hamiltonian and the product preserve the \(R=\pm1\) sectors.
2. On \(R=+1\), the ordered four-factor product is exactly \(e^{-ihaP}e^{-i2hbQ}e^{-ihaP}\), the Strang product for \(2(aP+bQ)\).
3. On \(R=-1\), the middle two factors and outer two factors cancel pairwise, while the Hamiltonian vanishes.
4. Taylor expansion using \(P^2=Q^2=I\) and \(PQ=-QP\) gives cubic difference \(\frac{4iab}{3}(2bP-aQ)h^3+O(h^4)\), whose coefficient has norm \(\frac{4|ab|}{3}\sqrt{a^2+4b^2}\).
5. For at most three distinct Pauli directions, different unordered pairs have different Pauli products. Thus nonzero commutators are orthogonal and cannot cancel in the degree-two BCH term.

The embedded checker instantiates \(P=X\otimes I\), \(Q=Y\otimes I\), \(R=I\otimes Z\), verifies exact quadratic-commutator cancellation numerically to machine precision, checks both sector identities, checks the predicted cubic coefficient, and confirms the expected \(r^{-2}\) repeated-step trend. These finite calculations corroborate but do not replace the proof.

The result does not classify all four-term solutions and does not establish achievability under extra geometric-locality or hardware constraints.
