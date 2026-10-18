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

# Verification notes

The proof is symbolic. Critical reductions are (a) the generalized Vandermonde factorization with the complete homogeneous quadratic \(h_2\); (b) the degree-\(p-1\) minimal polynomial of a primitive \(p\)-th root over the third cyclotomic field, for primes \(p\ne3\); (c) the resulting integer constraint \(10=p|v|+3T\); and (d) the exhaustive fifteen-case elementary count of pair-sum residue histograms. No finite experiment is used to infer an infinite statement.

The standalone `CHECKER.py` checks each of the \(\binom{3p}{4}\) possible four-column sets at primes \(p=5,7,11,13\) in exact integer cyclotomic coordinates. It validates the same expected obstruction classification and reproduces the three possible ternary histograms. Run `python3 CHECKER.py`; expected output is preserved in `CHECKER_OUTPUT.txt`. The checker requires only the Python standard library.

The tests cover \(130521\) finite column sets, not every possible prime; analytic steps (a)–(d) cover every prime in the theorem. Prior-work priority is not externally certified. Independent audit remains not performed.
