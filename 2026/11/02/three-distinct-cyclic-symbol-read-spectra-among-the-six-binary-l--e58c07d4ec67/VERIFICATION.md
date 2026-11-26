---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Assessed the corrected RESULT.md under /workspace/repairs/5. The six masks are exactly the monic odd quintics with neither x+1 nor x²+x+1 as a factor; every reducible quintic has a factor of degree at most two, and 31 is prime, so the irreducible quintics are primitive. The parity-check columns are all distinct nonzero five-bit vectors, giving dimension 26 and distance 3 (any two distinct columns sum to a third). The bundled finite recurrences count internal windows at append and the remaining b−1 cyclic windows at closure; the second uses character orthogonality instead of retaining syndrome states. Independent enumeration used neither recurrence: evaluate all 2²⁶ binary polynomial multiples of each degree-five p with degree at most 30, exactly the words satisfying c(α)=0, and count nonzero windows by popcount of the OR of b consecutive cyclic rotations. All 576 coefficients, reciprocal pairs, and nine displayed coefficient pairs matched. Replay: /workspace/branches/05-direct-multiples.py; arrays: /workspace/branches/05-direct-multiples-output.json. Reversal sends a polynomial to x³⁰c(x⁻¹) and takes C_p to the code of the reciprocal polynomial without altering the cyclic window count. The frozen first-moment explanation used independence of the window columns, which is not sufficient to prove uniformity of the projection from the kernel. The repaired proof uses the complementary columns: at least 27 distinct nonzero columns cannot lie in a proper subspace, so every window pattern has 2^(26−b) completions. Summing over the 31 window positions proves the invariant for all eighteen arrays. The repair changes no coefficients, parameter ranges or classification.

## originality

PASS

The supported distinct claim is the explicit complete set of length-31 cyclic primal Hamming enumerators at b=2,3,4 and the exact three-way split for each b. Inspected adjacent work concerns simplex duals, smaller or differently ordered codes, subcode hierarchies, or generation dimensions, not the same coefficient multiplicities. No precise covering result was established. The corrected prior-work paragraph withdraws the categorical nonapplicability claim for Shi–Özbudak–Solé; full-text coverage of its specialized claims remains unresolved.

## value

PASS

Primitive cyclic order is intrinsic to how these codes are used in a cyclic read metric, while their ordinary weight enumerators are invariant under permutation. Length 31 is a natural first degree at which several reciprocal classes of primitive binary generators are available: degrees 3 and 4 have two primitive polynomials each forming one reciprocal pair, and degree 2 has only one. The complete spectra show that reversal accounts for all equalities at each tested read width and precisely quantify how distinct orderings with identical ordinary Hamming and dual b-symbol enumerators separate. Those coefficients are useful as exact benchmarks for order-sensitive cyclic metrics; no claim is made for arbitrary interleavers, longer lengths, or all b.

The dated certificate retains the supplied scientific assessment, sources and limitations.
