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

The ambient ordered deleted product DConf(Δ^(n−1),2) is equivariantly homeomorphic via normalized x−y to the unit sphere in the sum-zero R^n hyperplane, dimension n−2. Vertex permutations act by sign and the swap by antipodal degree (−1)^(n−1). Truncating to the codimension-two skeleton removes exactly 2n open top-dimensional cells with first/second support of size n−1 and the other singleton; every lower cell survives. The relative cellular complex is therefore concentrated in dimension n−2 and, with ambient-induced coherent orientations, is Z_epsilon⊗P_n; the fundamental sphere class maps to the primitive all-ones vector in the relative group. The integral LES yields the quotient P_n/Z·1 (not the augmentation kernel) and vanishing of all other reduced groups. For t=0 permutation trace is 2fix(sigma)−1, and for t=1 it is −1, both multiplied by epsilon. The C2 invariant subspace ranks give n−1 for odd n and n for even n; S_n invariants vanish for n>=4. Independent full-cell Lefschetz sums checked 24 signed group actions at n=4..7. The universal statement uses the exact cellular proof and finite-group averaging over Q, not numerical extrapolation.

## originality

PASS

Qualified best-of-knowledge ORIGINALITY PASS for the specific final claim, NOT a declaration that known nonequivariant calculations or general frameworks are new. González–González, An algorithmic discrete gradient field for non-colliding cell-like objects and the topology of pairs of points on skeleta of simplexes (arxiv:2307.14454), Theorem 1.2(III) gives exact nonequivariant (2n−1)-sphere wedge for the same skeleton. Remark 1.7 explicitly says its optimal gradient field is not particle-swap equivariant. This covers all nonequivariant ranks but does not give the joint integral module. Abrams–Gay–Hower, Discretized configurations and partial partitions (arxiv:1009.2935), Theorem 1.1 covers deleted product of entire simplex, the ambient sphere underlying the argument. It does not calculate the truncated skeleton homology with the complete S_n×C2 action. Residual priority risks are stated; no stronger indexed result was identified which logically implies the assessed claim.

## value

PASS

The integral quotient lattice and joint vertex-permutation/particle-interchange action are new structures beyond the known 2n−1 sphere count. Unlike rational character alone, the canonical primitive diagonal quotient determines torsion-free integral representation data and explains the parity transition for unlabeled particles; it is a natural infinite family and the full action of its evident symmetry group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
