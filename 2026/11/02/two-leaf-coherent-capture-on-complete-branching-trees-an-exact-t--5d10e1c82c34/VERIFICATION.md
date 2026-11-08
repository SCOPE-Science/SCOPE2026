---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Radial/child-antisymmetric decomposition diagonalizes the full tree adjacency into Jacobi blocks of lengths 1..L+1 and yields distinct eigenvalue count D(L)=sum_{r=2}^{L+2}phi(r). Leaf transitivity and backward leaf eigenvector induction show every eigenvalue has a nonzero single-leaf projection. For two leaves splitting h levels above, eigenvalues absent from their common child-subtree force equal leaf projections; eigenvalues of that subtree yield two independent projections by using a third branch, requiring b>=3. Hence bright rank D(L)+D(h-1). Orthogonal dark/bright splitting and strictly negative real parts of the dissipative generator on bright space establish eventual capture for positive losses; strict totient increments establish optimal far-apart placement. Independently obtained modular Krylov ranks for b=3,4 and a boundary contradiction for b=2.

## originality

PASS

General bright/dark invariant-subspace capture in coherent quantum walks is known (Novo et al, arXiv:1412.7209), and finite homogeneous q-ary tree adjacency spectra are known (Scarabotti, DOI:10.1137/S0895480104445344). The final contribution is the exact two-distinct-leaf additional bright rank D(h-1), b>=3 boundary, all-distance optimal placement, and resulting capture fraction. The known one-trap/root and spectral results do not mathematically imply that increment without a further two-leaf eigenspace analysis.

## value

PASS

For a canonical finite tree and two local loss channels, the two-leaf bright-space dimension is a natural physical invariant and the totient placement law directly identifies optimal absorber separation with an exact branching boundary. The result is more than a finite numerical census or a generic dark-state restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
