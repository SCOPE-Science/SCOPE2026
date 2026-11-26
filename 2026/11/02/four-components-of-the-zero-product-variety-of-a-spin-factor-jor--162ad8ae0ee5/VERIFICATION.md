---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The equations are ab+B(u,v)=0 and av+bu=0. When a=b=0 only orthogonality remains. With exactly one nonzero scalar the opposite factor vanishes; with both nonzero the vector equation gives (b,−v)=(b/a)(a,u) and the scalar equation then imposes F(a,u)=0. Conversely the entire rank-one isotropic cone, including zero rows, satisfies both equations. The orthogonality hypersurface is geometrically irreducible because a (1,1) polynomial factoring would have bilinear rank one, whereas B has rank n≥2; its dimension is 2n−1. The nonzero rank-one isotropic locus projectivizes to the Segre of the smooth geometrically irreducible F-quadric of dimension n−1 and a projective line. Its affine cone has dimension n+1, as do both axes. Nonisotropic unit-axis points, an isotropic point with both scalars nonzero, and an independent orthogonal vector pair (take the first vector nonisotropic) separate the four loci. The latter works also for n=2. This verifies all dimensions, equidimensionality at n=2 only, and ambient codimension 3. For finite fields, x=0 contributes q^(n+1), a=0 with u≠0 contributes (q^n−1)q^(n−1), and a≠0 contributes one solution per x plus q−1 extras on (q−1)N_B(1) norm-one-rescaled x. The parity signs in the norm count follow by additive orthogonality and G²=χ(−1)q: the nonzero t sum is −1 for n even or χ(−1)G for n odd. This uses finite-field characters, not primeness of q. Inspected the standalone direct-pair checker and its recorded prime/extension examples as corroboration, not proof of the general theorem. No scheme-radicality claim is needed or assessed.

## originality

PASS

Panyushev already defines exactly this zero-product variety, derives the two axis components, and obtains dimension lower bounds and non-equidimensionality in relevant cases. His inspected §6 explicitly leaves classification of all components and their dimensions open. The distinct contribution supported here is the full reduced classification, including the two non-axis loci and the n=2 boundary, and the resulting exact finite-field census. The Gauss-sum norm formula itself is classical and not credited as original.

## value

PASS

This solves the component-classification question for a natural full family of simple Jordan zero fibers, down to the smallest included vector dimension and with uniform odd-characteristic scope. The Segre cone and the orthogonality hypersurface explain why different dimensions appear and lead to an exact discriminant-sensitive census. This is not merely the classical norm count or the already known two axes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
