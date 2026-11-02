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

# Verification record

The package contains a standalone `check_selection.py` and `requirements.txt`. Run `python -m pip install -r requirements.txt`, followed by `python check_selection.py` from the extracted package. The symbolic part verifies the exact numerator-denominator polynomial identity underlying the global rearrangement theorem and the one-step drift; it is not merely a set of numerical spot checks. The rational part tests strict monotonicity, pairwise order, all permutations of four selection strengths over multiple dominance coefficients and starting frequencies, and the sharp overdominance reversal. The saved package checker passed 673 assertions.

The quantified proof is in `RESULT.md`: the weighted-binomial variance identity implies monotonicity, the commutator factorization supplies its exact sign, and adjacent exchanges prove the finite-length extremum. For overdominance, strict concavity and the opposite endpoint signs of the quadratic imply one crossover. These arguments, not finite enumeration, establish the theorem.

Limitations: no finite-population stochastic validation, no independent scientific audit, no assertion of complete historical priority. Two closely relevant 1970s texts were only available in abstract/metadata form.
