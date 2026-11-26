---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On at least three selected vertices, the presence of the hub is detected by distance one, and if present it is uniquely determined. Fixing the hub excludes nilpotence. On one or two selected vertices, the only remaining hub-involving nilpotents are the singleton arrows A_j and B_i and the length-two paths H_ij for i≠j. Against a leaf-only path forest, A_j needs its leaf to be a terminal, B_i needs its leaf to be a source, and H_ij needs both conditions: the possible nonempty products with the forest have incompatible hub domain/image patterns. Thus there are 2c+c²−a_1 choices per forest and both pair orders contribute. Two A maps or two B maps always commute. Mixed types have unequal products: one order has a leaf-to-leaf arrow not present in the other. Two H maps have matching leaf-to-leaf arrows in both orders only when they are identical. Hence the hub–hub contribution is 3m²−m. Labeling the ordered paths gives m!/prod_j a_j! for each partition. On exp(t s), two applications of t d/dt plus twice the first application mark c²+2c; subtracting z exp(s) marks off the isolated paths, giving the exact coefficient factor s²+3s−z. At m=0 the summand and correction vanish. A fresh metric-based enumeration confirmed (B_m,C_n)=(1,1),(1,7),(7,41),(61,229),(685,1753),(9361,17891) for n=1 through 6. Method and results: /workspace/branches/5963f948-4ec0-4479-87ab-316711d9b653/record5-independent-check.md. The supplied checks/verify.py is present despite omission from the top-level support list; it was not run. Finite corroboration is separate from the all-size argument.

## originality

PASS

Verified antecedents describe individual partial isometries or individual nilpotent path forests. The supported distinct claim is the ordered commuting-pair excess and the local source–terminal compatibility rule that yields it. A known count or profile of individual nilpotents would not by itself fix this compatibility statistic.

## value

PASS

The distinguished hub is canonical from n≥3 and the question isolates its exact contribution to commutation without requiring a solution for the entire leaf monoid. The source–terminal rule turns a global pair computation into moments of the one-forest decomposition, giving a usable all-size correction for a natural graph monoid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
