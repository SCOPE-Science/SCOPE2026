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

Encoding the two east-step heights by u<=v gives three columns with predicates y<=u, u<=y<=v, v<=y. At b=1 there are three distinct concepts and a nonconstant query. For b>=2 the two middle queries at heights 0 and 1 are shattered using three nonempty intervals meeting those queries and the point interval at height 2. If a triple cannot be visited in increasing coordinate order, all-positive already fails. For comparable triples, repeated outer columns give nested events, three middle points have interval convexity, and for two middle points a negative outer query plus the appropriate positive middle query forces the other middle point. A triple with one vertex per column cannot have three negatives: the middle height lies between u and v when both outer queries are negative. For the uniform online lower bound, restricting to u<=t<=v gives an independent rectangle; binary threshold trees on the two coordinates concatenate, yielding the sum of floored logarithms. The 2^d leaf count gives the upper bound. An independent bounded depth-feasibility recursion on paths enumerated by step positions, for both languages, matched every tabulated rank through b=10. It rejects a split unless both conditioned spaces can realize the remaining depth; cardinality pruning only removes branches with fewer hypotheses than leaves. It separately parsed the frozen tree as data, checked exactly six decisions per leaf against the actual visited-vertex sets, and verified 64 distinct witnesses. The hand upper bound for middle-only b=10 also holds: root heights 4–6 give positive endpoint rectangles with rank 4 (threshold rank is additive by the sum-of-floored-logs potential), 3 and 7 leave blocks of 3 and 7 points, and the sole split there with >=16 positives leaves three 3-point blocks, insufficient for depth 4. All other roots fail the initial 32-per-side test. Replay: python3 /workspace/branches/audit_finite_reproduction.py.

## originality

PASS

Two distinct indexed results cover the middle-only ranks and the full-language VC/asymptotic results, respectively, and those components are not credited with separate novelty. Neither establishes the finite full-language ranks or the first gain on adding outer-column queries. That exact query-language comparison, with first gain at b=10 and earlier failure of the full cardinality bound at b=7, is the supported distinct finding. Same-day index dates do not establish record priority.

## value

PASS

The cutoff is the first height at which a natural oracle enrichment increases the realizable online mistake bound without increasing VC dimension, not an arbitrary sampled height. The full class nearly saturates its counting bound there, whereas the interval restrictions cannot; the explicit binary-tree witness and the obstructions supply a usable small benchmark for query-language comparisons. The already-covered restricted table and asymptotic order are context, not the basis for the value judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
