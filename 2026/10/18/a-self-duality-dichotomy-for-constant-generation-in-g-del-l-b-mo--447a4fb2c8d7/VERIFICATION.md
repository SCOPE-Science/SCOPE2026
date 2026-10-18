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

The mathematical proof covers all positive-arity Boolean clones, all formulas in the two-modal fragment, arbitrary formula nesting, and all finite transitive irreflexive GL frames. The only background completeness theorem invoked is GL finite-frame completeness.

Reproduction: run `python3 gl_constant_checker.py`. The checker exhaustively enumerates 242 labelled transitive irreflexive frames with 1–4 worlds, compares both modal selectors with terminal/nonterminal status under all one-variable valuations, checks 254 nonselfdual Boolean truth tables of arity up to three against an explicit equal-complement witness, and constructs both truth values for six sample formulas with selfdual Boolean operations. A successful run prints `VERIFY_OK`.

Computation is not used as proof of arbitrarily many worlds, infinite Boolean clones, or syntactic formulas. No independent audit has been performed.
