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

The file `verify_cycle_convex.py` constructs each tested graph from its cycle lengths and optional bridge paths. It independently computes cycle hulls by repeatedly finding connected components in the currently selected induced graph, then detects vertices with two neighbors in one component. It enumerates all subsets and tests the original definitions of convex independence, Helly independence, and Radon independence (the latter against every nonempty bipartition).

The program compares those three predicates to the theorem's structural criterion, checks the associated polynomial coefficientwise, and checks the predicted maximum-cardinality count. The supplied `verify_output.txt` is the recorded output from execution. It includes mixed triangle/long-cycle cases, multiple long-cycle cases, and examples with attached bridges. Its terminal marker is `VERIFY_OK`.

Finite checks do not prove the all-size theorem. The proof in `RESULT.md` establishes the closure rules, complete support classification, equality of the three independence systems for nonempty sets, exact enumeration, and the unbounded gap. The original prior-work sources were compared via accessible texts and bibliographic records; publication priority remains subject to external verification.
