---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Every uncentered shortest-path ball containing the hub is {c}, {c,v_j}, or V, and every ball containing leaf i is {v_i}, {c,v_i}, or V. Subtracting nonnegative hub baseline b, writing t_i=|f(v_i)|-b, q=max_i t_i, s=sum_i t_i/(k+1), gives maximal hub excess H=max(0,q/2,s) and leaf excess L_i=max(t_i,t_i/2,s). The cases L_i>=H and H>L_i yield |L_i-H|<=|t_i|/2+(k-1)/(2(k+1))*sum_{j!=i}|t_j|, including k=1,2. Summation proves C_k=(k^2-k+2)/(2(k+1)). Leaf singleton indicator yields equality for every k. Independent direct enumeration of graph balls and Fraction exact averages verified all 3905 sign patterns for k=1,...,5 with hub baseline 2 and offsets in {-2,-1,0,1,2}. The unrestricted bound rests on the analytic inequality, not finite tests.

## originality

PASS

Independent statement/implication comparisons found no decisive prior coverage of the exact assessed theorem, with explicit caveats. The operators must be compared by admissible balls: uncentered at a leaf includes hub-centered full ball and at hub includes all leaf-centered two-point balls. Centered maximal results cannot be relabeled into the new uncentered formula.

## value

PASS

This answers the sharp variation-operator norm on every unweighted star with no sign/symmetry restrictions, locates the precise first variation-amplification branch count k=4, and proves unbounded linear dependence on branching. It separates centered and uncentered graph-ball regularity in a useful simplest family, contrasting interval variation contraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
