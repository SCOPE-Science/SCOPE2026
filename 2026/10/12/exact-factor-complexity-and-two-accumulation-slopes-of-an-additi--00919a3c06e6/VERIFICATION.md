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

# Verification

Execute `python3 verify.py` with Python 3 and no third-party dependencies. This exact source file was run and produced:

`VERIFY_OK blocks=7 contexts=7 base=0..7 factors=1..260 bispecial_lengths=8,13,18,43,68,93 prefix=78125`

The program generates the \(78125\)-symbol prefix \(\beta^7(0)\) and counts actual distinct factors for every \(1\le n\le260\), comparing them with the formula. Independently, it exhausts all seven source triples to check the finite bilateral-order base, tests marker recognition on all possible three-block contexts, and directly tallies bilateral orders at six selected larger lengths. These tests are bounded; they do not certify infinitely many values. The proof in `RESULT.md` establishes universal quantifiers using desubstitution and the bilateral-order identity. No external independent audit or validation has been performed.
