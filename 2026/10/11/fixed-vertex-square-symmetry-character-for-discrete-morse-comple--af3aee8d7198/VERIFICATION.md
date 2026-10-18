---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For the one-dimensional cone graph h+T, Morse matchings are acyclic functional digraphs with ≤n arrows; Kozlov complete-source shellability supplies pure wedge-homology concentration in dimension n−1, not the character. Under g, each selected orbit of arcs contributes −1 to the augmented alternating Lefschetz sum (the permutation-sign factor cancels with face parity). Equivariant selections correspond to rooted partial forests on vertex-orbit quotient, and row expansion of det(I−L_g) gives their signed sum; directed cycles cancel as vanishing determinants. If g fixes f>0 tree vertices, fixed subtree is connected; determinant of hub+fixed block is (−1)^f f² via adj(L_F)=11ᵀ for a tree; moving quotient components have unique parent arrows and their Dirichlet determinant is (−1)^b for b moving orbits. If f=0, automorphism inverts a central edge, hub has no fixed neighbor and the remaining moving quotient Laplacian has row sum zero, giving trace zero. Multiply (−1)^n from homology concentration to get sgn_V(g) f(g)², including identity trace n². Rational character equals epsilon⊗U⊗U; integral equivariant basis not claimed. The reviewed exact Prüfer/automorphism/forest checker was inspected and independent small n=2,3,4 symmetry traces also computed; finite checks are corroboration, infinite proof is orbit determinant plus tree geometry.

## originality

PASS

Jojić arXiv:1109.4475 §2 gives complete-source shellability and generating facets for directed-tree complexes, thus *covers* wedge-concentration premise but contains no calculation of the action of arbitrary tree automorphisms on top homology; extracting representation characters from shelling requires further equivariance, not automatic. Donovan–Scoville arXiv:2207.13780 studies Morse complexes of tree/star families with nonequivariant topology; Engström gives related directed-forest shellability. An earlier documented triangular-book result computes the page-permutation character for the special star base T=K_{1,k}; that special case is excluded as original. The assessed uniform formula for all finite tree automorphisms, including nonstar trees and central-edge inversions, is a substantive new statement relative to inspected primary material.

## value

PASS

Character of an entire finite group action on top rational homology is strictly richer than Betti number n² and determines multiplicity of every irreducible representation by character inner products. The explicit ε⊗(U⊗U) decomposition for all tree automorphism groups supplies a reusable equivariant Morse-complex invariant, detects edge-inverting/no-fixed-vertex symmetries, and is not an arbitrary small-graph computation. Finite checks are supporting, while the structural orbit-determinant proof supplies the all-tree classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
