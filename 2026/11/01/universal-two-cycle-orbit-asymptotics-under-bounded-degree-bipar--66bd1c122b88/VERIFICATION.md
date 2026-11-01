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

# Verification of the bounded-degree deletion theorem

The exact counting lemma and the universal asymptotic are proved in `RESULT.md`. The following finite calculations corroborate the lemma and selected parameter families; they do not certify an infinite asymptotic.

Run `python checks/verify_formula.py` to enumerate firing vectors on small bicliques and crowns, compare the full bipartite double sum with the independent cut sum, and evaluate the exact crown / full-biclique ratio at shore sizes 10, 20, 40 and 80. Results are in `checks/formula_output.txt`.

Compile `checks/verify_independent.cpp` with `g++ -O2 -std=c++17 checks/verify_independent.cpp -o verify_independent`, then execute `./verify_independent`. This checks every chip vector with coordinates between zero and twice its graph degree minus one for seven small cases, directly tests whether the state returns in two steps without being fixed, and independently compares the orbit count with a cut count. Cases include matching deletions and irregular missing-edge patterns. Results are in `checks/independent_output.txt`.

The computational evidence does not verify the Gaussian approximation or uniform variance inequalities for all sizes; these are justified by the mathematical arguments in `RESULT.md`. The ratio at size 80 is only approximately \(0.134992\), compared with its limit \(e^{-2}\approx0.135335\), as expected from a non-exact asymptotic. No independent audit has been performed.
