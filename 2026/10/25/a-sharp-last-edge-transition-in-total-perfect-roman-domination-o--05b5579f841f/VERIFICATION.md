---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS. Definition requires each 0-vertex to have exactly one adjacent 2 and no positive-support isolate. For G_{n,k}=K_{n,n} minus k matching edges (n>=3), weight 4 requires exactly adjacent 2s on unaffected vertices a_i,b_j with i,j>k, hence (n-k)^2 optima if k<n. For crown k=n, no weight <=5 is possible; weight-six configurations are precisely Type M (matched 2s plus one extra positive in each part) and Type X (unmatched 2s plus cross-part 1s) except n=3 admits all-ones and twelve one-2 patterns. Counts give n(n-1)^2+n(n-1)=n^2(n-1) plus 13 at n=3. Independently exhaustively enumerated every feasible labeling of weight <=6 for all n=3,4,5,6 and k=0..n: all minima and exact counts agreed; the proof treats arbitrarily large n by number of 2-labels.

## originality

PASS

PASS, best knowledge: Almulhim introduced total perfect Roman domination and gave general classes/bounds, but the actual full paper reviewed has no matching-deleted balanced-biclique optimizer census. Published SCOPE crown perfect Roman result is a different predicate: its weight-four matched 2s are isolated in the positive support and violate totality. The sharp final-deletion weight jump and full labeled-optimizer count survive the direct mathematical comparison.

## value

PASS

PASS. A natural one-parameter graph perturbation has an abrupt two-unit invariant change at exactly the last matching deletion, and the complete labeled optimum configurations exhibit a nontrivial exceptional n=3 term. A motivated exact extremal classification is independently useful for domination-variant comparisons, not just a tiny graph computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
