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

The all-alphabet proof reduces the optimization to rotation orbits and classifies every optimizing binary context matrix by its tied pairs and transitive quotient tournament. An additional reconstruction lemma shows that only the initial singleton diagonal can be invisible to the resulting code; this is required to deduplicate matrix partitions into distinct codes.

To reproduce the independent finite checks, from the directory containing the accompanying source files run `g++ -std=c++17 -O3 check_optima.cpp -o check_optima` followed by `./check_optima`, and run `python3 check_structure.py`. The C++ program enumerates all \(2^{q^2}\) context matrices at \(q\le5\), computes their resulting codes and deduplicates them. The separate Python program generates the predicted structural class without enumerating all matrices and explicitly checks prefix/suffix disjointness. Both checks produce exactly \(1,6,42,408,4920\) distinct optimizers for \(q=1,2,3,4,5\), respectively. The finite tests are not an infinite certificate; the written arguments establish the general claim.

The novelty assessment compared the statement with the full HTML version of the closest primary article, an accessible abstract of an earlier restricted-overlap paper, and targeted semantic-record searches; these cannot exclude every earlier equivalent formulation. No independent audit has been performed.
