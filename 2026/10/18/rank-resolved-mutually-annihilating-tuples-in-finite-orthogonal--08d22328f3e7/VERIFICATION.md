---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: For odd-characteristic nondegenerate B and ordered Xi with all XiXj=0, skew-adjointness implies B(X_i v,X_j w)=0, so joint image U is totally isotropic and each Xi annihilates U^perp. Fixing isotropic U, Xi factors through V/U^perp≅U* and is exactly an alternating map U*→U, with q^binom(r,2) choices per Xi, and all supported products vanish automatically. Möbius inversion on the subspace lattice gives the spanning-image factor A_{r,k}(q), then the classical isotropic extension-line/flag counts yield the three Witt-type I_V(r) formulas. The rank-zero tuple is counted once, rank one impossible, n=1 and k=1 included. Independently enumerated all actual 4x4 skew-adjoint squarezero matrices over F3 and all pairwise zero-product ordered pairs, obtaining rank profile {0:1,2:64}; the source explicit n6 hyperbolic two-generator rank-three witness follows from independent block multiplication. Proof, not prime-field finite test, covers odd prime powers and all n,k.

## originality

PASS

PASS best-of-knowledge: Unrestricted mutually annihilating matrix pairs, single symmetric nilpotents, and commuting Lie pairs do not determine joint-image-rank counts for skew-adjoint zero-product k-tuples in both Witt types. Boos–Cerulli work over C on degeneration orders of self-dual quiver representations and does not tabulate such finite-field point counts. The critical isotropic-map/alternating-form calculation is elementary but the combined exact type-resolved stratum distribution was not covered in the inspected primary texts. Residual possibility of equivalent results in Hall-polynomial/alternating-pencil or self-dual quiver count literature.

## value

PASS

PASS: Joint-image dimension is a canonical rank invariant for self-dual representations of the radical-square-zero loop algebra. The complete labeled distribution across every odd finite field, tuple size, dimension and orthogonal Witt type distinguishes split/nonsplit forms and reveals odd joint-image rank possible for k=2 even though individual alternating maps have even rank. This is a meaningful structural enumeration beyond a tiny parameter example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
