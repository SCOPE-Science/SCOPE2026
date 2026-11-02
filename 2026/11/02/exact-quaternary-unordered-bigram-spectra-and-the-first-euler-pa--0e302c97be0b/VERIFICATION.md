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
# Direct reproducibility checks

Extract `verify.py` from the same package and run `python3 verify.py` (Python standard library only).

Actual executable output:

`VERIFY_OK literal_lengths=2..9 literal_words=349520 graph_profiles_m=1..12 profile_vectors_tested=646645 rational_coefficients_m=1..12 exact_match=True`

The program uses three different objects: literal strings and their length-two composition multisets; nonnegative ten-edge multiplicity vectors with a direct connectedness/odd-degree feasibility test; and exact rational-series coefficients computed using integer binomial convolutions. It checks all four-letter words of length 2 through 9 and all ten-coordinate edge profiles of total 1 through 12. The twelve exact coefficients are `10,34,116,367,1060,2782,6704,14963,31276,61738,116020,208848`.

The all-length identity is established mathematically by classifying connected simple supports on at most four vertices and all eight parity subgraphs with four odd degrees. These finite experiments cannot prove an infinite claim. No independent mathematical audit is asserted.
