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

# Reproducibility and limits

Run `python3 verify_independence.py` with a standard Python 3.10+ interpreter. The program exhausts all binary matrices of sizes \(2\times2\), \(3\times3\), and \(4\times4\), and all ternary teams over a two-element base. It cross-checks a combinatorial cardinality histogram against direct rectangle predicates, and three rational inclusion probabilities against a logically independent recombination predicate.

Expected terminal output: `VERIFY_OK rectangle_matrices 66064 ternary_teams 256 rational_probability_tests 3`.

The computational test does not certify any infinite asymptotic statement; the supplied proof establishes those separately through exact rectangularity, binomial tail bounds, and elementary Poisson convergence. No external formal certification or independent audit has been performed.
