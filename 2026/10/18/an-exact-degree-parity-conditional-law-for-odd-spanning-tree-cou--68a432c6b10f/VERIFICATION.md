---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For n>=2 the handshaking map from the edge indicator bits onto even-sum degree parity vectors is surjective; fixing d sets the n-1 incident-to-last-vertex bits uniquely in terms of the C(n-1,2) independent internal bits. The F2 reduced Laplacian minor is therefore a uniform symmetric (n-1)x(n-1) matrix with exact diagonal d[1:n-1], so Kirchhoff makes tree-count odd iff full rank. Under binary congruence the diagonal transforms as P^T b, proving all nonzero b classes equiprobable. Zero diagonal gives the alternating-form product p0(2k)=prod_{j=1}^k(1-2^{1-2j}) and p0(2k+1)=0. For nonzero b, congruence to e1 and Schur complement C+vv^T yield p1(2k+1)=p0(2k) (singular even-dimensional alternating C has nullity>=2) and p1(2k)=(1-2^{-(2k-1)})p0(2k-2)=p0(2k) (odd-dimensional C requires 1-d radical and v.w=1). This derives the exact three-case formula and n=2 boundary. A fresh independent exact-rational enumeration of all graphs n=2..6 and of all symmetric matrices with every fixed diagonal m=1..5 agrees for every feasible d and b. Numeric infinite product independently evaluated to 0.4194224417951076; enumeration alone is not the all-n proof.

## originality

PASS

Qualified best-of-knowledge: the exact graph-level conditional law is not stated by the inspected source theorems. Its nontrivial extra ingredient is an exact fibre equivalence between entire degree parity vectors and fixed-diagonal binary symmetric reduced Laplacians, followed by congruence orbit separation and an alternating rank-one update. Classical counts explain the product; originality is the finite-n conditional graph-level classification, not the alternating-form count itself.

## value

PASS

This gives the complete finite-n conditional law for a canonical n-bit observable on the strongly dependent degree-conditioned Erdos–Renyi graph ensemble. The exact independence of the tree-parity event from every degree-parity vector at odd n and the single all-even exceptional fibre at even n are structural phenomena not determined by the known unconditioned p-Sylow limiting law. The result is naturally relevant to parity-restricted random graphs, binary Laplacian minors and 2-primary critical groups, even though its alternating-form ingredients are classical. It is an all-order exact law rather than a routine substitution or arbitrary numerical slice; it does not claim full integer tree counts or biased-edge models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
