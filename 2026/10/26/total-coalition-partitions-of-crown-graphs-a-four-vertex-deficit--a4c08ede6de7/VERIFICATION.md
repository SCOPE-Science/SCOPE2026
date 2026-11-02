---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For Cr_n=K_nn minus matching, a set is total dominating iff it contains >=2 vertices from EACH side. A total-coalition partition must have every block not dominating yet some distinct partner that takes both counts to >=2. Deficit epsilon=2n-number_of_blocks bounds non-singleton sizes. For n>=5, any optimum with deficit<=4 must contain U and V singletons; each needs a distinct (1,2) or (2,1) triple, exhausting deficit and fixing all remaining blocks singleton. Cases n=3,4 require separate combinatorial finite profiles. Count n>=5 as C(n,1)C(n,2)C(n-1,2)C(n-2,1)=[n(n-1)(n-2)/2]^2. Independent exhaustive graph-adjacency partition enumeration tested all 203, 4140, 115975 unlabeled-block partitions at n=3,4,5 and recovered (TC,M)=(3,48),(4,857),(6,900). No claim finite enumeration proves all n; general proof uses deficit argument.

## originality

PASS

General total coalitions, Cr_3=C_6 scalar answer and min-degree lower bounds are old; none of the inspected total-coalition primary theorems determines complete crown upper bound and optimal partition census for all n>=4. The general k=1 specialization of later k-coalitions could be relevant, but the abstract-level source was not taken as wholly noncovering.

## value

PASS

The crown graph is a canonical almost-complete bipartite graph; total-coalition extremal partition shape and exact count are natural open-type domination invariants. General degree bounds do not give the complete optimizer census; the 3,4 exceptions add substantive boundary cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
