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
# Reproducibility and scope

Run `python3 verify_token_dom.py` using Python 3 and only the standard library. The script independently constructs the graph vertices as unordered pairs of the original \(K_{2,n}\) vertex set, then constructs its closed neighbourhoods directly using symmetric differences. It enumerates all vertex subsets of those token graphs for \(n=2,3,4,5\) and counts dominating sets by cardinality and by the presence of the distinguished pair.

The same script independently evaluates the closed finite-sum formula using integer polynomials and the binomial inclusion-exclusion expansion. It compares all coefficients and both hub branches for each tested \(n\). It then checks the predicted minimum count and hub threshold through \(n=11\), computing the polynomial formula exactly. The fully executed output from the extracted standalone script was:

```
VERIFY_OK brute_parameters=2..5 examined_vertex_subsets=2131008 formula_parameters=2..11 min_hub_absent_after_4=True
```

The executable arithmetic certificate is finite. The unbounded theorem is the structural bijection, the exact inclusion-exclusion calculation and the all-case optimum classification written in `RESULT.md`; these are not delegated to an experiment. No independent audit or external certification has been performed. The references distinguish the previously known domination number and feasible-set lemma from the enumerative contribution. Public priority beyond the named inspected sources is not claimed.
