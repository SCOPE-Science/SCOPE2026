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
# Exact verification and scope

Run `python3 verify.py` using Python 3's standard library. The program independently produces 700 exact central trinomial coefficients via the integer recurrence, compares 80 terms with the integer binomial sum, and evaluates digit congruences using the five weights \((1,1,3,2,4)\). It regenerates all residue-state minimum/maximum tables at lengths two, three and four, and confirms each of the twelve transfer identities underlying the universal finite-state induction.

It additionally scans 15,625 digital residues, checks every prefix of four residue classes up to the sixth full base-five block against the exact claimed envelopes, checks the complete-block count identities and produces the upper-extremum digit-word witnesses through length twelve. Expected successful status is the literal text `VERIFY_OK` followed by counts.

The proof of arbitrary lengths uses the translation-equivariant Bellman recurrence, not extrapolation from finite scans. The verifier does not establish literary originality, external mathematical certification or an independent audit. No third-party packages, network access or data files are required.
