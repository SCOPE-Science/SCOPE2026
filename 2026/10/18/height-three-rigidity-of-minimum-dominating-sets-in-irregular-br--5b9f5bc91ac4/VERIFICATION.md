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

For full-depth rooted trees with every nonleaf having at least two children, the three exact root states A (selected), B (omitted but dominated by a child), C (omitted and awaiting parent) yield a=1+Σmin(a_i,b_i,c_i), c=Σb_i, and B as an A/B child-selection minimum with at least one A. The induction checks the minimizing-state multiplicities, not just costs: remaining heights 1,2,0 modulo 3 give respectively unique A; unique B with a=b+1; and c<a=b=c+1, B with exactly d minimizers. Root C is infeasible. Thus h=3t+1 has unique D=∪L_3j, h=3t+2 unique D=∪L_{3j+1}, and h=3t≥3 has D=(∪L_{3j+2})∪{v}, v∈L_0∪L_1; h=0 is singleton. No uniform branching is assumed. Independent fresh all-subset enumeration matched exact minimizer families on 1 height-0, 2 height-1, 12 height-2 and 1 height-3 profiles of at most 15 vertices; source checker and its separate DP were read but not relied upon to prove all heights.

## originality

PASS

Best-of-knowledge original complete optimizer classification generalizing known period-three binary-tree counting to nonuniform full-depth branching, with a strict root choice dichotomy.

## value

PASS

The natural question is to classify all minimum dominating vertex sets, not just calculate γ(T). Universally forced every-third-level structure under arbitrarily irregular vertex degrees, with exact multiplicity depending solely on the root degree, is a meaningful structural rigidity fact and useful closed-form boundary for tree-domination enumeration; not a mere fixed-degree substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
