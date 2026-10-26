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

Run `python3 verify.py` using Python 3.9 or later, with no third-party packages or input files. The program independently obtains every scattered subsequence of each source word up to a prescribed length by repeated set updates; it computes the greedy universality index without applying the theorem's transfer matrices. For each binary word of length 0 through 14, it compares the number of absent patterns with the theorem's explicit coefficient formula after grouping by length and index. For words through length 12, it additionally verifies the first-letter transfer identity against independently enumerated missing strings. Algebraic recurrence and selected initial coefficients are checked through length 60.

Observed exact output:

`VERIFY_OK complete_words=32767 max_length=14 one_arch_transfers=8166 bivariate_cells=64 scalar_recurrence_through=60`

The exhaustive finite enumeration is not a proof beyond its checked bounds. In particular, the asymptotic dominant-pole argument is mathematical rather than numerical; the verifier does not independently certify the uniqueness of the smallest-modulus pole. All accepted claims are conditional only on the explicit binary-alphabet definitions in the manuscript, and the program's finite checks are corroborating evidence.
