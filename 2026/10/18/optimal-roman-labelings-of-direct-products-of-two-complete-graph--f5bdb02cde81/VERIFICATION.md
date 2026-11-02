---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The direct/tensor adjacency is exactly r≠r′ AND c≠c′. For D=2-labeled support, B(D) consists of cells having no defender neighbor, and Roman feasibility is exactly B(D)\D⊆O where O is the 1-support. Weight below six is impossible: |D|=0 forces mn≥16 ones, |D|=1 forces m+n−2 ones plus weight 2≥8, |D|=2 forces at least two labels 1, and |D|≥3 costs≥6. At weight six, |D|=2 and exactly two forced ones yields either diagonal/cross-corner pairs or a same-row/same-column configuration only at corresponding dimension four. For |D|=3, no ones are allowed; all distinct rows/columns give three matched defenders, or three corners of a 2×2 rectangle are valid, while a repeated row with a third column different from its two defender columns leaves an uncovered zero; analogous repeated-column and all-same configurations are excluded. The resulting five disjoint counts sum to 6C(m,3)C(n,3)+6C(m,2)C(n,2)+[n=4]mC(n,2)+[m=4]nC(m,2). An independently written adjacency-only enumerator exhaustively checked all size-2/size-3 defender placements on ten boards through 9×9, including 4×4=360, 5×5=1200, 8×9=34272 and 9×9=50112 and verified each geometric class. The finite tests corroborate the all-parameter case proof rather than establish it. Fixed m≥4 and n→∞ (or vice versa) yields cubic growth of the matching count vs quadratic growth of the rest.

## originality

PASS

Best-of-knowledge originality of the all-optimum named-function classification and 5-family enumerator. The closest 2021 same-graph result proves only the minimum weight six. Primary direct-product total Roman and set-domination literature and the unitary-Cayley alias do not imply this exact count. Closest indexed Resultary findings have different graph products or Roman variants. Search absence is not proof of novelty; an unindexed matching classification remains possible.

## value

PASS

This is a complete natural classification and exact multiplicity formula for all minimum Roman allocations on an infinite two-parameter family of canonical graph products, rather than a renamed known minimum. It exhibits three distinct bulk geometries, two sharp dimension-four boundary mechanisms, the distribution between two and three defenders and the asymptotic dominance of matching triples. A graph domination researcher may need exact named-optimum counts to study robustness, sampling, or refinement of Roman domination polynomials; these follow neither routinely from the scalar gamma_R=6 nor from the different total Roman/set-domination theories. It does not assert a full polynomial, orbit enumeration, or higher-factor generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
