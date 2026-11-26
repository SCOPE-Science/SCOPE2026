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

For the connected unit-edge graph with four positive equal diagonal gains, the quadratic form is strictly positive; the kernel of the Laplacian consists only of constants and any nonzero constant incurs a positive gain penalty. The covariance is half the inverse, so trace comparisons are unchanged. Pair occupancy plus hub inclusion exhausts the graph orbits: five, four and two profiles for m>=4, m=3 and m=2, respectively. I derived all seven rational trace differences separately by differentiating log det(L+kD+zI) at z=0, using the scalar arrowhead determinant and the three types of shifted 2x2 block determinants. All stated numerator and denominator identities match, and denominators are positive. The three cluster penalties are strict, leaving the two unclustered profiles for m>=4. The Q-H numerator has negative coefficients at m=4,5; its two positive roots at m=6 and 7 are as stated, with product 9/4; at m=8 its discriminant is negative with positive leading coefficient, and each larger m adds a strictly positive polynomial. For m=2 the other profile loses strictly. At m=3 strict dominance leaves A_3 and C_3, and the comparison quartic is strictly increasing on positive gain, has opposite signs at 3/10 and 1/3, and changes the winner in the stated direction. Strict dominance excludes additional ties. An independent exact calculation also inverted the full grounded matrices for each of the five representative profiles at gains 1/100, 1 and 25 for both m=6 and 7, giving hub/no hub/hub with no ties at those gains. Replay: python3 /workspace/branches/exact_review_checks.py 1 (SymPy). The frozen checker was read, not run; its 1,984 small-network and 36 larger sample checks are recorded evidence, not the universal proof.

## originality

PASS

Compared with the available exact and general results, the distinct claim is the all-m four-leader finite-gain friendship phase classification, including the exact double switches specifically at m=6,7 and their common root product. The noisy-consensus objective and placement problem are known, and reentrance exists on other graph/budget models. No inspected statement or implication covers the assigned classification. The plausible Sun–Li–Liu same-graph paper remains an unresolved source, not negative evidence or a reason by itself to fail.

## value

PASS

The classification answers when a natural clustered graph's central hub should receive one of four noisy leaders, with the concentration-versus-spread tradeoff changing twice only at two graph sizes. It supplies usable exact thresholds and the root-product relation, and explains why low- or high-gain heuristics alone miss the intermediate optimum. The proof is a complete optimization over all placements and graph sizes, not merely a sampled nonmonotonicity example or a restatement of the general inverse-trace criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
