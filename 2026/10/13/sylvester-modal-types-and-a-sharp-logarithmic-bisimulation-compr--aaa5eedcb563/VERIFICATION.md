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

Under immediate-child accessibility, induction on remaining height identifies greatest ordinary bisimulation exactly with equality of (color, set of child descriptors); different remaining heights are separated by a sufficiently long iterated diamond. Any nonempty set of at most q available child types is realizable independently, with repeats filling any unused slots. This proves the exact type and level-count formulas. The recurrence gives t_(k+1)≥a t_k; after t_k is large, the q-element subsets give log t_(k+1)≥q log t_k−q log(2q). Subtracting the fixed affine threshold yields log t_k≥c q^k, while counting all colorings gives log t_k≤C q^k. Splitting levels at q^k comparable to h with a sufficiently small constant bounds the lower-height terms by O(log h·q^(h/4)) and the upper-height tail by O(q^h/h). At q^k comparable to h with a sufficiently large constant there are at least q^(h−k) types, realized on disjoint height-k subtrees to attain Ω(q^h/h). Thus the lower bound concerns the maximum, not every coloring. The one-color and unary cases have exactly h+1 classes; t_k+1 in the binary sequence means addition of one, not the successor index. Independent greatest-relation pruning over all 32,768 binary height-three colorings found maximum nine classes. The frozen Python verifier and its recorded five small cases were inspected, not run; the asymptotic estimate is analytic.

## originality

PASS

Credit prior ordered-DAG and graded upper bounds, the classical sequence, and material binary two-color coverage from the companion catalogue result. The distinct claim is the exact ordinary type census and sharp ordinary extremum in the genuinely set-valued regime q≥3 (with arbitrary fixed palette); neither the binary coincidence nor large graded quotients establishes that ordinary lower bound. The binary case and Sylvester recognition are a specialization and context, not independently cleared contributions.

## value

PASS

The invariant is the actual space remaining after ordinary modal minimization on a canonical family. The matching lower bound shows what unordered, multiplicity-free model reduction really cannot compress, rather than relying on the order-sensitive or graded counts that can overestimate it substantially. The finite type census explains why the transition occurs near remaining height log_q h.

The dated certificate retains the supplied scientific assessment, sources and limitations.
