---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

At every 2<=a<=b, the three ball averages are exactly max{x_i,(x_i+b beta)/(b+1),mu} and max{y_j,(y_j+a alpha)/(a+1),mu}. Passing to |f| preserves its maximal function and decreases total edge variation. In the alpha>=beta case, the first half is the one-Lipschitz truncation T(t)=max(t,mu); the second has nonnegative excess <=ab[(alpha-beta)]/((a+1)(a+b)). Thus the summed cross-edge error is bounded by ab times that excess and Var(f)>=ab|alpha-beta| by Jensen. The opposite case swaps sides. A point mass on a vertex of the smaller part gives the exact lower expression 2-3/(a+1)-(a-1)/(a+b); the upper-lower difference is (2(a+b)-1)/((a+1)(a+b)). Squeezing proves C_ab=2-a/(a+b)+O(1/a) uniformly b>=a, sup 2 not attained. Explicit check K4,4 gives 41/40. All boundaries a=2 and unbalanced sequences are included; no claim that finite-size bounds coincide. Independently checked point-mass algebra and analytic inequalities; inspected the exact rational checker check.py (Git blob 53918310c0a9b2177fa57df1a2e6fe45a846dbae), but its finite tests are only corroboration.

## originality

PASS

The full joint large-biclique variation constant is not stated in the examined graph maximal-operator literature. González-Riquelme–Madrid obtain sharp variation on complete and star graphs; González-Riquelme–Kovač–Madrid construct generic unbounded graph examples, which neither dominate nor imply these bounds for K_a,b. The highly relevant Liu–Xue 2021 article concerns bounded p-variation norms on finite graphs and remains incompletely inspected, so it is an explicit priority risk rather than a false noncoverage conclusion. Best-of-knowledge PASS for the exact finite bracket and uniform joint asymptotic, not a universal graph theorem.

## value

PASS

Centered graph maximal variation is a natural stability invariant; a complete bipartite graph models a substantial two-community geometry not covered by complete graphs or stars. The limiting constant ranges rigorously from 3/2 to 2 as relative part sizes vary, and K4,4 already amplifies variation; the sharp uniform asymptotic is information a researcher could need. The unresolved finite-size exact optimum does not negate the meaningful joint limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
