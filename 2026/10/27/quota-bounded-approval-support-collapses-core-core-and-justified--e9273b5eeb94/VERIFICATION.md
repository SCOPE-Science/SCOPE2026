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

The cap gives an independent direct proof for fractional blocking, without LP duality. Write L=sum_i y_i, Z=sum_c z_c and u_i=u_i(W). In any blocker, qZ <= L <= sum_i (1+u_i)y_i = sum_(i,c) x_ic <= sum_c |S_c|z_c <= qZ. Equality throughout forces u_i y_i=0 and, for every z_c>0, |S_c|=q and x_ic=z_c for every supporter. Those supporters have y_i>0 by their row equalities and are therefore all unrepresented; c is unelected and violates JR. Conversely a JR violation gives an integral singleton block, which embeds into the fractional system (choose exactly 1+u_i approved alternatives for each participating voter). This proves both equivalences and vacuity for nonintegral q, including q<1. A maximal disjoint family of quota-size supports has size at most k and intersects each other quota-size support, as required. For the sharp example, only q-1 voters gain from singleton c, and neither two-candidate alternative can improve all 2q voters: each leaves one of the two represented c-supporters at utility one. The fractional witness has the stated row equalities and sum_i y_i=q with only z_c=1; this remains valid at q=1. The frozen script was inspected, not run. Its capped-profile regression tests JR and integral core, not all fractional obstructions; line 107 checks a weak inequality rather than explicitly testing equality, which the displayed witness satisfies exactly by direct substitution.

## originality

PASS

The imported core+ notion, its implication of integral core, and its dual characterization are not contributions. The supported distinct result is the exact cap-specific converse for every committee, its constructive characterization, and the sharp one-voter breach at every integral quota. Existing results inspected do not give that combination or mechanically yield the sharp family.

## value

PASS

The support cap turns two otherwise stronger blocking notions into an elementary incidence test and greedy construction for all committees in a natural sparse-approval regime. The uniform three-candidate obstruction identifies a sharp boundary, rather than merely showing that fractional and integral blocking sometimes differ.

The dated certificate retains the supplied scientific assessment, sources and limitations.
