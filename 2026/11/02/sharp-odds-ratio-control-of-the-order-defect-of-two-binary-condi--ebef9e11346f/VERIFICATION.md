---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

On a positive 2x2 table, reconstruct P=E[.|X], Q=E[.|Y] 4x4 weighted averaging matrices. Direct PQ-QP multiplication gives four rows of signed terms using u=b/(a+b),v=d/(c+d),r=c/(a+c),s=d/(b+d). Both delta_X=s-r and delta_Y=v-u have sign ad-bc, so each absolute row sum is twice max of two positive terms, yielding exact formula in RESULT.md for L∞. For fixed theta=ad/(bc), logistic odds p=t/(1+t),q=theta*t/(1+theta*t) gives |q-p|=|theta-1|t/((1+t)(1+theta*t)), maximized at t=1/sqrt(theta), equal |sqrt(theta)-1|/(sqrt(theta)+1). All conditional probs strictly between zero and one imply strict <2Y for theta!=1. Family (sqrt(theta)*T,T,1/sqrt(theta),1) has fixed odds and achieves limiting 2Y as T->infty; theta=1 commutator zero. Independently multiplied 625 positive integer tables exactly and checked sharpness family. No extrapolation beyond positive tables or L∞.

## originality

PASS

Yule association coefficient of a 2x2 table is classical (Warrens), and commutation criteria for projections are classical. The full published Resultary binary-event projection-chain Lp theorem excludes p=∞ and treats centered products, not the commutator nor the supremum at fixed odds. Current exact 4x4 L∞ commutator and 2Y sharp unattained fixed-odds law do not follow from those quoted results alone. Uninspected Kallenberg primary full text is an explicit residual, not a fabricated NOT_COVERING verdict.

## value

PASS

The commutator of row and column conditional expectations measures order-sensitivity of two natural binary information projections. The exact positive-table L∞ norm and sharp maximum at fixed odds ratio connect operator-theoretic order defect to Yule association, including nonattainment under full support. This is a natural complete four-atom invariant rather than a textbook equality test; no claim beyond binary full-support tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
