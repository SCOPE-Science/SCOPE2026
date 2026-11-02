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

This package includes `thue_second_verifier.py`, a standalone Python 3 exact-integer verifier without external packages. Execute `python3 thue_second_verifier.py` in the directory containing the file. The expected terminal marker is `TM_TWO_TORTOISE_VERIFY_OK`.

The checker constructs all length-18 factors, not a sampled initial prefix, from the four words \(\mu^5(ab)\) with \(ab\in\{00,01,10,11\}\). It explicitly compares the complete four nontrivial two-pass fibres against literal binary witnesses, verifies the two missing alternating length-five factors, and checks failure of the proposed identity at length 17. For each length \(18\le n\le512\), it independently constructs the complete factor set from substituted adjacent blocks and checks the one- and two-pass deficit formulas against the source first-pass digit law. The exact verified count of lengths with two-pass deficits \(4,6,8\) is respectively \(237,20,238\).

The **infinite** statement is not inferred from the finite verification range. It is proved in RESULT.md by the certified length-18 collision partition, inheritance of equal images under deletion of first-two ones, and a parity-synchronization/desubstitution lemma giving an exact bijection between new two-pass pairs and left-special factors of length \(n-4\). These are mathematical proof steps available for independent inspection. No external independent audit has been performed.
