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

Run `python3 verify.py` in the directory containing the packaged witness data. It reads `data/base_witnesses.json`, independently forms every length-three codeword of each of the ten seeds, deletes each of its three positions, and verifies that the union of the resulting length-two subsequences equals the entire alphabet square. It also verifies the exact codeword counts, vertex-to-target arrows, triples, distinct codewords, and arithmetic of the three GDD families. The saved output in `verification_output.txt` ends with `VERIFY_OK`.

This exact finite check supplies all ten seed certificates. The all-parameter extension is a deduction using Lemma 1.1 of Chang–Chee–Zhou (reproducing the Colbourn–Hoffman–Rees design-existence theorem) and the elementary group-pair count. The program checks the parameter congruences over a finite range for regression only; the symbolic proof in `RESULT.md`, not finite enumeration, establishes them for all permitted integers.

Independent review of the proof and publication priority has not been performed. The numerical existence assertion is conditional only on the separately published group-divisible-design existence theorem, not on a computational conjecture or an unobserved optimization certificate.
