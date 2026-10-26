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
# Reproduction and limitations

Run `python verify_skew_commuting.py` in a standard Python 3 environment; it uses only the standard library. Finite fields of orders 4, 9 and 16 are built from irreducible polynomials, and the Ore ring multiplication is implemented by the rule \(x c=c^s x\). The checker does **not** call the local-chain-ring exterior-minor criterion: instead, each commutator is formed directly in the truncated Ore quotient.

Full ordered-pair enumeration over \(\mathbb F_4[x;\sigma]/(x^3)\) gives 1,408 commuting pairs out of 4,096 and centralizer-size histogram \(\{16:56,64:8\}\). Over \(\mathbb F_4[x;\sigma]/(x^5)\) it gives 102,400 commuting ordered pairs out of 1,048,576 and histogram \(\{64:896,256:112,1024:16\}\). Over \(\mathbb F_9[x;\sigma]/(x^3)\) it gives 76,545 out of 531,441 and histogram \(\{81:702,729:27\}\). Twelve direct centralizer enumerations are also checked over \(\mathbb F_{16}\), where \(\sigma(c)=c^4\). The test ends with `ALL_SKEW_TRUNCATION_CHECKS_PASSED` when successful.

All finite enumerations terminate exhaustively for their stated configurations. They are not a proof of the formula at arbitrary prime-power \(s\) or truncation length; the general proof is in `RESULT.md`. A publication-priority search and a self-review have been completed, but no independent mathematical audit has been performed.
