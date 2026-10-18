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

The mathematical proof is in RESULT.md. This record describes bounded executable checks only; no independent audit has been performed.

Run `python3 verify.py` in a directory containing that file. It requires Python 3 and no external packages or network access. The checker evaluates the original box and diamond semantic clauses directly over upset truth sets, enumerates every local neighbourhood family for eleven finite posets, and compares the observed tables at every instance arity up to poset width against the two signatures. It tests **1,100 distinct local families for each of the two modalities**, covering all 256 on the three-point antichain and 512 on the disjoint union of two two-point chains. It also tests two-world box and diamond nonfaithfulness, and one-world zero-arity detection of an empty diamond neighbourhood through arity four.

All enumerated tests completed without assertion failure in this review. The final output line is `Two-world box and diamond equivalences, and one-world diamond emptiness detection: passed`. The cases checked do not exhaust all finite posets or all arities; universality and sharpness are justified by the explicit mathematical argument, not finite extrapolation.

The self-review checked the upset maximal-trace lemma, necessity of the box minimal-trace representative, diamond co-witness characterization using downset complements, the induction from one-step operators to full formula semantics, the persistent constant-family constructions and the chain count. An external independent audit is **not performed**.
