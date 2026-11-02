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

# Reproducibility

Run `python3 verify.py` in a directory containing the supplied standalone script. It uses only the Python standard library.

The script was executed successfully on the supplied code path. It checked constructed cyclic covering strings and transition histograms for alphabet sizes 2 through 50, independently computed shortest target-tour costs by exact subset dynamic programming for alphabet sizes 2, 3 and 4, and exhausted every binary cyclic word of lengths 4 through 11 to rule out a shorter binary cover. Exact computed minima were 12, 24 and 40.

The proof for arbitrary alphabet size is in `RESULT.md`; no finite test is treated as a proof for every alphabet. The checker enumerates Hamiltonian tours of target motifs, not every possible covering string for alphabet sizes greater than two. The theorem itself bridges that distinction via the cyclic occurrence-selection argument.

No independent scientific audit has been performed.
