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

The proof of the universal three-shift identity is mathematical; finite tests do not establish universality. The included standalone `verify.py` checks direct cubic Möbius products via roots and formal derivatives, avoiding the discriminant proof for prime fields. It exhausts every unordered triple in the fields of orders \(5\) and \(11\), and selected triples in fields of orders \(17\) and \(23\); in total there are \(216\) direct shift-triple cases. It separately checks \(496\) triples for the character-correlation lemma over four prime fields and \(12\) triples over an explicitly represented field of order \(125\). The output was `VERIFY_OK direct_mobius_triples=216 prime_character_triples=496 extension_triples=12 field_order=125`.

Run `python3 verify.py` with Python 3 and no third-party packages. The proof handles all remaining finite fields meeting the assumptions. No independent mathematical audit has been performed.
