---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Every permissible word of length L gives a directed trail of L-3 distinct nonpalindromic four-letter edges in the order-three de Bruijn digraph and uses at most one member of each reversal pair. The 64-vertex flow, binary pair constraints, and endpoint choices yield a 368-variable, 186-row integer-program relaxation even without connectivity; its optimum upper-bounds every word. Independently rebuilt the matrix from all 240 allowed four-grams and solved with SciPy HiGHS: status optimal, objective -110, certified MIP dual bound -110, zero relative gap; the displayed literal word has 113 letters and all 110 windows are distinct, nonpalindromic and pairwise non-reversals. This proves L_4(4)=113 conditional on correct MILP solver bound; no separate machine-checked rational optimality proof is claimed.

## originality

PASS

Noncyclic four-symbol exact finite optimum L_4(4)=113 is not logically supplied by Mitchell’s binary aperiodic classification or by Mitchell–Wild and Gabrić–Sawada periodic/cyclic k-ary construction bounds: unwrapping a cyclic example is a lower construction, not an upper bound for unrestricted finite trails. The exact quaternary integer optimum remains a best-of-knowledge new finite benchmark.

## value

PASS

The smallest nonbinary fixed-span exact length gives a meaningful benchmark separating finite path optimization and periodic cycles, with explicit witness and upper certificate. It is natural adjacent to published binary and cyclic orientable sequence problems and not just a substituted parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
