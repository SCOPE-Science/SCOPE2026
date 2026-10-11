---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Writing the two-fiber operation as (i,x)*(j,y)=(i,A_ij x+B_ij y), with B=1-F, gives the exact self-distributivity equations B_ij(A_ik-A_jk)=0 and B_ik(1-A_ij)=B_ij B_jk. With A_00=A_11=2 and B_00=B_11=-1, the off-diagonal variables u=B_01 and v=B_10 have exactly two branches under the unit-coefficient hypotheses: u=v=0 with A_01=A_10=1, or A_01=A_10=2 and uv=1. Thus r=u ranges through nonzero r not equal to 1, giving F_01=1-r and F_10=1-r^{-1}; r=-1 is the printed all-2 case and the other p-3 choices are omitted. A fresh exhaustive finite-field replay for p=5,7,11 found exactly the predicted p-1 total solutions (the decoupled point plus p-2 coupled points), supporting the algebraic derivation without replacing it.

## originality

PASS

The primary source's Definition 5.1 permits the general tagged affine coefficients used here, while Proposition 5.1 explicitly claims that the admissible operations fall into three completely specified classes. Direct coefficient comparison shows the prime-field family above lies outside those three classes except at r=-1. Current Resultary searches for the proposition, the two-fiber prime-field slice, and the coefficient relation returned the assigned correction but no earlier source-specific correction. Originality is therefore passed for the explicit omission/counterfamily to the claimed exhaustive list, not for abstract existence of these quandles in broader quandle theory.

## value

PASS

An explicit p-3-parameter omission for every odd prime p at least 5 is a substantive correction to an asserted exhaustive classification, and the complete two-fiber unit-coefficient solution explains exactly where the source coefficient matching lost the branch. This is mathematically motivated classification repair rather than a one-off numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
