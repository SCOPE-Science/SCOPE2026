---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Reproduce from the package root using `python artifacts/verify.py`. No external dependencies are required. The program constructs each small complete multipartite graph by its vertex partition, computes each vertex's degree, tests the degree-qualified domination predicate for every candidate subset in ascending cardinality, and independently enumerates deletions until the first change. It compares both stability and the total count of optimum deletions with the theorem for all 183 integer-partition profiles of order 2 through 11 having at least two parts. The run checks 36,315 deletion subsets up to the optimum sizes and also checks the twelve-vertex profile (4,4,4). Actual stdout is preserved in `artifacts/verification_output.txt`.

The analytic proof alone establishes the result for arbitrarily large finite part sizes. The finite verifier cannot establish infinite validity or mathematical priority. Independent external audit has not been performed.
