---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: In G[Q_d], d>=2, m=2^d, projection onto uniform hypercube fiber s and s^perp diagonalizes Hamiltonian into mA_G+dI and the independent Q_d walk, respectively. For same-fiber antipodal transfer, non-target amplitudes at distances zero and one must be equal; with cos t nonzero this forces cos t=-i sin t, impossible for real t. Thus cos t=0 and t=(2r+1)pi/2; phase (-i sin t)^d. Uniform-sector consistency then requires e^{-imtA_G}e_g=e_g. This is equivalent to 2^(d-2)(2r+1)theta integer for every locally supported adjacency eigenvalue theta. The theta are algebraic integers, and this condition makes them rational, hence integers. Conversely all locally supported integral theta return at *every* odd half-period. Independently reconstructed seven-vertex double-star tree characteristic x^3(x²-2)(x²-4), middle-deleted characteristic x²(x²-2)²; resolvent support precisely {-2,0,2}, while global spectrum has ±sqrt(2). The full algebra proves all finite connected G, not finite checker extrapolation.

## originality

PASS

PASS, qualified: Ge et al. Lemma 5 supplies a sufficient global-spectrum period condition for G[H], notably G[Q_d] when all G eigenvalues are integers. Godsil develops local eigenvalue support, and later blow-up analyses use a distinct independent-set fiber. The submitted necessity argument from hypercube nonuniform amplitudes, vertex-local iff for every d>=2, exact all transfer times, and explicit nonintegral connected outer graph are not implied by a *global sufficient* condition. Resultary finds the same assigned record but no independent dominating local hypercube equivalence. Still relies on standard product decomposition/eigenvalue support, and an unindexed periodicity corollary remains risk.

## value

PASS

PASS: Turns an established sufficient global integrality construction into a sharp necessary-and-sufficient *local* criterion with complete transfer-time set; the connected nonintegral tree proves the condition strictly enlarges the family. This answers a natural graph-quantum-walk transfer classification rather than a renamed parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
