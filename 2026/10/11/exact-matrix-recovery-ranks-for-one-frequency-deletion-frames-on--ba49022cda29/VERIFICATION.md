---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Reconstructed the map X -> (v_{ell,x}^*Xv_{ell,x}) by Fourier inversion of the site x: difference bands delta decouple, with T_delta^ell the sum of X_{a,b} over a-b=delta surviving deletion ell. On delta=0, sum_ell T=(N-2)sum_diag, uniquely recovering all diagonal entries for N>=4. On delta!=0, each entry survives N-3 deletions, so S_delta=sum_ell T/(N-3). Defining x_j=X_{j,j-delta} for j not 0,delta and x_0=x_delta=0 gives measured x_ell+x_{ell+delta}, with b_0=0. The homogeneous recurrence alternates around cosets of <delta>: odd length gives no kernel; even length gives one free alternating scalar per coset except the forced-zero coset <delta>; those alternating cycles have zero sum. Summation over disjoint delta bands yields R=(N-1)^2-sum_even_order(N/ord(delta)-1). Because each projector is Hermitian, complex span rank equals real span dimension among Hermitian matrices. Odd N gives full Gram recovery and global phase; even N>=4 has an explicit order-two two-frequency pair (1,i)/(1,-i); N=2,3 handled separately. Independently constructed exact integer incidence band matrices and computed rational ranks for group types Z4,V4,Z5,Z6,Z7,Z8,Z4xZ2,Z2^3,Z9,Z3^2,Z10; all agreed, including 44/36/28. These finite checks only corroborate the all-order cycle proof; bundled verify.py was inspected, not executed in the container.

## originality

PASS

Qualified best-of-knowledge PASS for the complete finite-abelian matrix-tomography rank/nullity classification, not for prime matrix recovery or the known odd-cyclic phase-retrieval corollary. The all-abelian element-order sum and explicit nonidentity-coset nullspace basis give nonisomorphic order-eight groups different ranks (44,36,28). The published cyclic proof already yields linear full matrix recovery for odd cyclic groups by its recurrence and supplies the main method; thus novelty is limited to exact even-group deficiency and extension across noncyclic structures. The inspected fixed-family and larger Gabor/representation results do not assert or imply the complete formula without a new computation. Historical equivalence risk remains.

## value

PASS

The complex span of prescribed rank-one intensity operators is a natural matrix-tomography capacity invariant, stronger than the known yes/no pure-state phase retrieval property. The exact all-abelian formula supplies an explicit basis for every missing operator direction and reveals that isomorphic order alone does not determine measurement rank (order-eight ranks 44,36,28). A researcher studying informational completeness, deterministic masks, or noise sensitivity would need the exact defect and its coset mechanism. The result is limited to noiseless rank and does not assert stability or minimal mask subsystems; the covered odd-prime and cyclic phase-retrieval consequences are not used as novelty evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
