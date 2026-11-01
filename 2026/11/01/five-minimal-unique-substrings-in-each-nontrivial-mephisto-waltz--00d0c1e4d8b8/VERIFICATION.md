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

# Reproducible verification

Run `python3 verify_mephisto.py` using a standard Python 3 interpreter and no external dependencies. The output from the replay is preserved in `verification_output.txt`.

The script uses a suffix-array-neighbor longest-common-prefix computation to find all minimal unique factor intervals for each of the first eight substitution iterates. It compares the result with the five-interval formula at every iterate from two through eight, checks the exceptional first iterate, and performs independent all-factor occurrence enumeration for the first five iterates. It also checks exactly \(3402\) length-at-least-four factor/covering-parent multiplicity identities in the first three applicable iterates.

The computed last case has length \(6561\), with five intervals beginning at indices \(1457,2186,3644,4373,5102\), each of length \(731\). Checks of finitely many words are not an infinite proof: the phase-disjointness argument and MUS-lift induction in `RESULT.md` supply that proof.

The program does not check whether the same scientific statement has already appeared in unpublished literature; such absolute novelty certification is not claimed. Independent mathematical audit has not been performed.
