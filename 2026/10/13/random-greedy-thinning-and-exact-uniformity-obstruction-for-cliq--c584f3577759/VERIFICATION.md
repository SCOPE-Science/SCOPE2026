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

The attached standalone `verify.py` is self-contained Python 3 and uses standard-library `fractions.Fraction`, `itertools.permutations`, and exact integer counting. Running `python3 verify.py` in the directory of the extracted artifacts outputs `verification_output.txt`. It independently constructs every corona edge and exhaustively simulates greedy acceptance for six finite tests; it separately implements the Bernoulli-thinned core law and checks exact per-output rational probabilities and private-choice equiprobability, as well as exact bias for complete cores.

Tests comprise \(2\cdot9!+4\cdot8!=887{,}040\) permutations, not a proof for unrestricted core graphs. The infinite theorem follows from the cluster-minimum coupling, the private-clique symmetry and exact counting given in RESULT.md. A public mathematical research search cannot exclude equivalent older formulations. Independent audit has not been performed.
