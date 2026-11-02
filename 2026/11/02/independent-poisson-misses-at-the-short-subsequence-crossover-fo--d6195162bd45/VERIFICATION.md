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

# Reproducibility checks

Run `python3 verify_greedy.py` and `python3 verify_critical.py` from the directory containing those files. Both use Python's standard library only.

The first program evaluates exact greedy-automaton counts for every binary pattern of lengths one through four and every unordered pair for all source lengths up to twelve, with independently enumerated inputs through length eight. It checks the all-pattern single-avoidance identity and a polynomial majorant for joint avoidance. It also records larger-length pair-avoidance maxima.

The second program constructs the exact distribution of contained-pattern subsets under a different automaton, then computes the probability of a nonempty common length-\(r\) subsequence by finite inclusion–exclusion. Its recorded probabilities are finite-length comparisons, not exact matches to the limiting law. The proof of the asymptotic independent-Poisson law relies on the product-automaton loop-state lemma and the generating-function limit, not on finite computation. Outputs are included verbatim in `verify_greedy_output.txt` and `verify_critical_output.txt`.

The scope is uniform iid binary strings, fixed \(r\), and \(d_na_{n,r}\to\lambda\in(0,\infty)\). No external independent audit has been performed.
