---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Reversing one-symbol duplication with transposition amounts to deleting a nonfirst occurrence of a symbol. Deleting two positions produces the same parent exactly when every symbol between them is constant, so each eligible constant run contributes exactly one distinct parent and precisely the singleton first run of each symbol is ineligible. Hence \(|P(y)|=r(y)-s(y)\). The maximum follows from run count versus distinct-symbol count, and summing run counts minus singleton-first-run counts over all received words gives the stated global edge formula. Fresh exhaustive generation for \(q=2,3\) and \(1\le n\le4\) reproduced the pointwise law, maxima and edge counts.

## originality

PASS

The complete Polyanskii--Vorobyev paper defines the same duplication-with-transposition graph, parent/child language, roots and distance, but its main results are asymptotic root-distance bounds for arbitrary duplicated blocks and approximate duplication. It does not give the one-step indegree law or the edge count for the length-one specialization. Resultary and targeted parent/preimage/indegree searches returned no equivalent formula.

## value

PASS

The theorem determines the exact local branching structure and total edge complexity of a canonical one-step specialization of the duplication graph for every alphabet and length. That is a natural graph/channel invariant with a complete extremal classification, not an arbitrary tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
