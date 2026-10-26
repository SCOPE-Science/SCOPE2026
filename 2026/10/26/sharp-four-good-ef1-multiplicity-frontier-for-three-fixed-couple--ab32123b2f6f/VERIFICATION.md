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

The general guarantee concerns arbitrary nonnegative additive singleton values, including zeros and ties. The reduction to finite strict ordinal rankings is exact for the balanced \((2,1,1)\) allocation pattern: only an agent in a singleton group can fail EF1, and only by ranking both paired goods ahead of her singleton. Breaking ties arbitrarily preserves the implication from an ordinally EF1 allocation to one that satisfies the original cardinal inequalities.

Run `verify_four_goods.cpp` using a C++17 compiler. It builds 36 distinct allocations, precomputes the failure masks of 24 orders for each of the three group labels, and exhausts exactly 24 to the fifth power ordered five-tuples of remaining agent ranks with the first agent normalized. Integer population counts construct the exact histogram and check the positive minimum two, extremal witness frequency, and analytic expected-count identity. There are no randomized or numerical approximations in the certificate.

Run `check_examples.py` with Python 3. It applies the literal EF1 inequality to all 36 balanced allocations for the displayed four-good witness and to all 243 complete allocations for the previously published five-good example. The outputs, including the two surviving four-good group-assignment vectors and the zero survivors at five goods, appear in `verification_output.txt`.

The finite exhaustive program proves the four-good universal statement only because the proof reduces *all* admissible cardinal valuations to the finite ordinal universe with explicit symmetry. It is not a proof of any larger-instance classification, and none is claimed. The scientific literature review is not an independent audit.
