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

# Reproduction and limits

Execute `python3 CHECK.py` with Python 3, standard library only. The script independently regenerates the first 50,000 binary symbols from the published integer-index recurrence and compares the first 5,000 against the direct base-\(3/2\) digit-parity algorithm. It checks the precise length-nine witness at indices \(12\)–\(20\), the maximum alternating-run length within that finite prefix, and every cube whose period is between \(1\) and \(120\) and coprime to \(3\) that lies entirely within that prefix. The finite checks are supportive only.

The infinite proof is entirely elementary: equal-adjacent starts are restricted modulo three, four consecutive even-sampled bits have an equal adjacent pair, alternating runs have maximum length nine, and a coprime-period cube with an equal pair would replicate that pair across forbidden residues. This yields the complete length-\(3p\) classification and the sharp restricted exponent.

No claims are made about powers with periods divisible by \(3\), nor is the unrestricted critical-exponent conjecture settled. No independent mathematical audit has been conducted.
