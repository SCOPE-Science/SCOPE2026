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

The universal argument is symbolic and applies to every odd prime power \(q\). The accompanying `verify.py` is only a bounded consistency check.

The checker exhaustively enumerates every pair \((A,u)\) with \(A\in\operatorname{GL}_2(\mathbb F_q)\) and \(u\in(\mathbb F_q^2)^*\) for \(q=3,5,7\). It constructs the induced map on the radical basis \(x,y,x\wedge y\), computes \(\dim\ker(\phi-I)\) by modular Gaussian elimination, adds the fixed scalar line, and compares the resulting distribution with the theorem. It separately checks that the four fibers sum to \(q^2|\operatorname{GL}_2(q)|\) and that their weighted Burnside sum equals \(3q\).

For \(q=3\), the checker also constructs the action on all \(3^4\) algebra elements and computes the actual orbit partition; it has exactly \(9\) orbits, agreeing with \(3q\).

A fresh replay from the extracted package must end with `VERIFY_OK`.

The computation does not test non-prime extension fields and is not used to infer the all-prime-power theorem. Extension fields are covered by the proof, whose counting depends only on standard finite-field cardinalities and linear algebra.
