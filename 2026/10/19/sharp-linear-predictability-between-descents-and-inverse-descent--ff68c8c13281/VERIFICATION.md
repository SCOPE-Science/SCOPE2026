---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

This pass is for the corrected claim in /workspace/repairs/1/RESULT.md and SLOGAN.txt. The frozen equality characterization is false: for n=2, w=(4) and a=b=(-4) yield correlation 1 but are not positive multiples of w. For each index pair, swapping the adjacent values j,j+1 flips E_j and leaves D_i unchanged unless both occupy i,i+1. In that exceptional event D_i=E_j, and its probability is 2/[n(n-1)]. This verifies the constant cross block. Disjoint adjacent-position comparisons are independent, whereas a triple has both descents with probability 1/6. Thus A_n is the stated strictly diagonally dominant symmetric positive-definite matrix. For a,b nonzero the numerator is c_n(1^T a)(1^T b); Cauchy–Schwarz in A_n gives simultaneous equality in magnitude exactly for a=sw,b=tw with s,t nonzero, w=A_n^(-1)1. The sign is sign(st), proving the corrected characterization st>0 for the signed maximum and any sign combination for the absolute one. The same normal equations give the common affine projection of each E_j. Substituting the explicit weights into 3w_i-w_(i-1)-w_(i+1)=12 with w_0=w_n=0 checks the inverse profile; summing by a geometric series gives the stated rho_n. Independently inverted the rational matrices for n=2,...,8: rho is 1,1,13/14,21/25,34/45,62/91,813/1316. For n>=7 the strict bound w_i<12 gives rho_n<6/n; the closed sum differs from 12(n-1) by a bounded term, giving n rho_n->6. The exponential terms in w_i give both boundary-layer limits. Replay by forming 12A_n with diagonal 3 and neighbor entries -1, solving the displayed Dirichlet equations, and checking correlation at (-w,-w). The supplied verifier was read, not executed; its square-based inequalities alone do not check the sign characterization. The repaired result retains the original theorem's numerical content and treats uniqueness as a coefficient direction, not as uniqueness of an oriented coefficient pair.

## originality

PASS

For the repaired claim, the credited result is the evaluated position-by-value structure together with the optimized linear correlation, common affine projection and exact Dirichlet profile. The published marginal covariance and total-count results, and the classical joint enumeration, are prior ingredients or constraints. Sign correction removes an error without adding a novelty claim.

## value

PASS

Position-adjacent and value-adjacent order each give a natural signature of a random ranking. The sharp optimized dependence measures what can be gained beyond unweighted counts: the common affine prediction is rank one, all zero-sum score contrasts are invisible to the other family at second order, and the exact extremizing pattern distinguishes boundary and bulk. This supplies a useful finite-size and asymptotic benchmark without claiming conditional independence or nonlinear optimality. The sign repair preserves this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
