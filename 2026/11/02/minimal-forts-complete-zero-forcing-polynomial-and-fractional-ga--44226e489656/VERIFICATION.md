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

The crown adjacency rule makes the fort condition exactly b-1_{i in B} !=1 for each omitted left i and symmetrically a-1_{j in A} !=1. An exhaustive symbolic case distinction for a,b<=2 proves the only minimal mixed forts are matching-index four-sets; shore triples cover the >=3 cases. Fort hitting gives the zero-forcing polynomial; disjoint triple packing and an explicit size-four fort when n mod 3=2 give floor(2n/3). Uniform fractional weights 1/3 and dual weights on all shore triples prove Z*=2n/3 for all n>=3. Independent verification: Independently generated crown adjacency for n=3,4,5, enumerated minimal forts and forcing subsets. Minimal fort totals 5,14,30 and generating coefficients n=3 {2:6,3:18,4:15,5:6,6:1}; n=4 {4:30,5:48,6:28,7:8,8:1}; n=5 {6:90,7:100,8:45,9:10,10:1}. The all-order LP certificates were algebraically checked. Inspected verify.py; finite enumeration alone is not the proof.

## originality

PASS

Best-of-knowledge: inspected accessible closely related primary PDFs, searched published mathematical records for aliases/stronger results, and compared implications. The complete-bipartite minimal forts and its fractional optimum are different because the crown has no cross-adjacent matched pairs; the known Q3=Cr4 case cannot imply an all-n theorem without further argument. Residual priority limitations are explicit.

## value

PASS

The deletion of a perfect matching from K_{n,n} changes the fort hypergraph from twin pairs to shore triples and matched four-sets; the exact polynomial, fort packing and fractional integrality gap tending to 3 quantify the change over a natural infinite graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
