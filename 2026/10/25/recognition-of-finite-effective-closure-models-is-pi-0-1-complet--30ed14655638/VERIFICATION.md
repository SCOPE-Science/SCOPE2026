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

The proof has two independent components. A co-recursive-enumerability certificate lists one modal formula outside a generated theory and finitely many formulas within the theory excluding every possible counterworld. The hardness construction transforms any Turing-machine description into a primitive-recursive syntactic procedure that computes theory membership by inspecting only the finite set of indices occurring in the input formula and performing bounded computations for those indices.

The normality conditions are verified as *frame* properties, with all valuations quantified for (G) and (E), rather than just the model's actual valuation. The construction has one world, an empty generator and a standard extensive, monotone, idempotent, finite-union-preserving closure operation.

Run `python checker.py` from this package to reproduce finite checks of bounded-time halting and looping examples, the uniform modal recursion, conjunction, modus ponens, finite-test instances of (G), and the two possible one-world Kripke relations. Observed output on this package: `ALL_CHECKS_OK (44624 finite diagnostic assertions)`. These checks are supporting diagnostics; their finite coverage proves neither \(\Pi^0_1\)-hardness nor novelty, which rest on the written mathematical reduction and literature comparison. No external certification or independent audit has occurred.
