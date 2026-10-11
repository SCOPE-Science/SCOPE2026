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

# Verification of the two-sum spectrum

The exact proof computes every ordered collision for fixed nonzero sum from the factorization \((x^2-y^2)(x^2+y^2+s^2/2)=0\). The corresponding quadratic-circle count is \(q-\chi(-1)\), with intersection size \(2(1+\chi(-1))\). The unique odd-multiplicity fiber has size \(2+\chi(-2)\); the first two fiber moments determine the remaining two positive levels. The zero-sum case and characteristic-five Frobenius case are independent algebraic reductions.

The accompanying `verify_fifth_graph.py` constructs exact field arithmetic using irreducible monic quotient polynomials, exhausts all \(q^2\) ordered pairs in each chosen field, and compares per-slice multiplicities, total support, and energy to the formulas. Run `python verify_fifth_graph.py`. Tested orders: \(3,5,7,9,11,13,17,19,23,25,27,29,31,37,41,49,125\). All tests passed. Integer arithmetic avoids floating-point threshold issues. The finite field checks neither substitute for the unrestricted algebraic proof nor constitute an independent audit.
