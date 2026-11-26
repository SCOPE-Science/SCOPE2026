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

The bracket determines the W-block T_A=(A⊗1+1⊗A) on exterior wedges and leaves B:V→W free before imposing the composition equation. From D^2=0 one needs A^2=0, T_A^2=0 and T_AB+BA=0. For square-zero A, T_A^2(u∧v)=2Au∧Av, which proves the characteristic restriction. In a basis of r length-two chains and n-2r singleton chains, the wedge between the vectors of one two-chain contributes rank zero, between two distinct two-chains contributes rank two, and between a two-chain and a singleton contributes rank one. These are disjoint wedge subspaces and give s_r. To count B, choose B(e) arbitrarily on each length-two chain e→Ae; then B(Ae)=-T_AB(e) is forced and consistent since T_A^2=0. The n-2r singleton images lie in ker T_A. Thus the exponent is rm+(n-2r)(m-s_r)=h_r. Selecting the image, then the kernel containing it, then the induced isomorphism yields exactly the Gaussian factors and |GL_r|. The degree difference to the r=0 term is zero at (n,r)=(3,1) and negative for all n>=4 and r>0: m>=2(n-1), 2(n-r)<=2(n-1), and for n=4 either r>1 or the nonnegative product (n-2r)(n-r-1) is positive. The limit follows from the leading coefficient one in each allowed summand. A bounded independent matrix calculation confirmed all stated sample totals, with A-counts (1,21), (1,104), (1,105,210) and fiber dimensions (9,5), (9,5), (24,14,12) for (n,q)=(3,2),(3,3),(4,2) respectively.

## originality

PASS

The standard parametrization by generator values and the standard square-zero matrix count are ingredients. Neither counts the central fibers satisfying the Lie and square-zero equations jointly. The closest indexed same-day square-zero result treats a different Lie algebra and a different rank statistic. No equivalent earlier count was identified in the bounded searches and statement comparison.

## value

PASS

For a basic free nilpotent algebra the result gives a complete finite-field count stratified by a canonical observable, the action on the abelianization. The difference between characteristic two and odd characteristic, and the exceptional limiting central-image proportion in generator dimension three, are structural consequences not apparent from counting arbitrary maps on generators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
