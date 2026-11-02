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

# Reproduction and boundaries

The theorem is analytic and applies to all integers \(a,b\ge1\), all \(p_U,p_V\in(0,1)\), and all fixed initial colorings. The proof derives exact transition kernels, sidewise renewal equations, the tie-restart contraction, product-class probabilities and the binomial central-limit transition.

Run `python biclique_biased_verifier.py` with Python 3 and the `sympy` package. The included verifier constructs the exact reduced Markov transition matrix directly, solves the finite absorbing chain for all initial count pairs on each of eighty choices of small graphs and rational biases, then compares the results to the theorem's formulas. Its recorded result is `PASS: 80 exact absorbing chains, 980 state/parameter comparisons; 500 tie-mass checks`. It also checks the \(K_{4,4}\) rational example.

Finite exact matrices do not verify the infinite families or prove that no previously published result covers the theorem; the proof and literature comparisons are essential. The upper bound for the expected hitting time is not asserted sharp. Independent audit and validation are not performed.
