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
Run `python3 verify.py` (Python standard library only). The verifier constructs complete multipartite graphs from the part-size vectors; its direct adjacency implementation uses union–find to reject cyclic vertex-induced subgraphs. This directly recomputes every forest and maximal-forest coefficient on 183 profiles, testing 177556 subsets, independently of the closed formulas. It recursively lists every nondecreasing integer partition of all orders two through sixteen with at least two parts (898 total) and tests every coefficientwise extremal inequality and every log-concavity minor with exact integers. Its only negative log-concavity slack is -104 at profile (1,)*12+(4,) of order sixteen. It also tests the parameterized obstruction on 80 family members. `verification_output.txt` is the exact captured output of an execution of the included program.

The binomial-difference identity and its strictness prove the infinite extremal theorem, while the polynomial difference and its positivity prove infinite non-log-concavity for the stated family. Finite enumeration proves precisely the bounded lower-order cutoff, not any statement over all finite graphs or infinitely many other classes. External expert validation has not occurred.
