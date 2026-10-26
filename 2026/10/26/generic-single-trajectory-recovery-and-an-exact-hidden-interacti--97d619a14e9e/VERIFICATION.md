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

# Verification and limits

The proof rests on: (i) the exact equivalence of model ambiguity and a nonzero supported polynomial vanishing along the orbit; (ii) an explicitly nonzero all-dimension polynomial Lie-Wronskian, certified at uncoupled positive exponential growth with binary-separated rates; (iii) Taylor's determinant leading coefficient for \(p_n\) nearby exact time samples; and (iv) the conserved product \(x_1x_2\) in the positive nonstationary three-species counterexample.

Run `python verify.py` from the extracted package. The executed checker verified the exponent counts and rational Vandermonde determinants for \(n=3,4,5,6\), symbolically checked that an explicit \(n=3\) system with all hard triadic coefficients \(1/20\) has three nonzero row-Wronskians, and confirmed the exact invariant-surface and vector-field identities of the counterexample. The expected final output is `all checks PASS`.

These tests certify only the sampled algebraic identities. The unlimited-dimensional result is established by the binary-expansion and determinant proof in `RESULT.md`; no infinite inference is made from the test counts. The result does not quantify statistical estimation error, robustness to derivative noise, optimal experimental scheduling, state-only observation identifiability, or global solution existence for arbitrary coefficients. Independent audit has not been performed.
