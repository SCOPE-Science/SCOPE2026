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

The exact theorem is proved with a ternary-carry gap lemma, a square-period exclusion argument using paired ones in morphism blocks, and an exact descent/inflation bijection for nonconstant maximal repetitions. The finite checker is separate corroboration rather than certification of the quantified infinite result.

Run `python3 checker.py` in a directory containing the embedded standalone file. This constructs independent maximal-run triples using period equality streaks and prefix-function minimal-period calculations, then compares all triples to those obtained from the stated two families for levels one through six. It additionally compares the period/length histograms and both aggregate identities. Expected last line: `PASS: independent enumeration equals all predicted run triples, period/length spectra, and totals at levels 1..6`.

The checker does not independently prove the period-reduction lemma for all levels, and it does not establish publication priority. No independent mathematical audit has been conducted.
