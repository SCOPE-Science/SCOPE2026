---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

All maximal independent sets are A and B when t=0. For t>=1 every independent set meeting both sides lies in a unique missing pair {a_i,b_i}; these pairs are maximal; each entire side remains maximal iff its cardinality is at least 2. For t=1, equating the weights of surviving maximal sets yields the exact displayed positive free parameters, with singleton-side exceptions. For t>=2 both entire sides and P1,P2 are maximal; their weights must all equal W but P1 and P2 are disjoint, so w(P1∪P2)=2W=w(A∪B). Since P1∪P2 is a proper subset of A∪B if a+b>4, positivity is impossible. The remaining a=b=t=2 yields two disjoint edges with all solutions (p,q,q,p). Finite independent maximal-independent-set enumeration checked representative boundary cases, and source verify.py fully inspected; no small finite experiment is used in place of the unbounded proof.

## originality

PASS

Bhaskara et al. introduced levelability, complete multipartite positive weight examples and the generic four-maximal-set obstruction, which are explicitly prior; the exact matching-deletion threshold plus every integer level in the surviving family is not stated in inspected source. General well-covered vector-space algorithms for arbitrary fixed graphs do not symbolically give this family classification in their conclusions.

## value

PASS

Asks a natural sharp robustness question: when does deleting a matching of size t destroy positive weight equalization of maximal independent sets in complete bipartite graphs? The one-edge boundary, exceptional 2K2 and full positive-integer cone are a self-contained exact structural classification, more useful than a single small graph check despite short obstruction proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
