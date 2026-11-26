---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

PASS applies only to repairs/2/RESULT.md. The frozen substitution at lines 83–104 combines valid-block flags and ends with an identity AND without specifying the required inversion. Read literally, it outputs Ind(z) instead of 1−Ind(z); Wang–Wu §3.3 checks p(τ_d)=0, so every promised input then lacks an accepting certificate. Since Definition 3.8 also outputs zero on unpromised inputs, that literal substitution is constant zero, refuting its rectangle bound. The repaired circuit explicitly inserts a free NOT before the final AND, after computing the conjunction, with all padding before that final output. Independently, ripple additions cost at most 2(j+1) ANDs each; their tree sum is 4m−2k−4. The prefix comparator invariant gives the two inclusive threshold flags in 4(k+1) ANDs, plus at most one for their OR. Together with conjunction and the terminal AND this is at most 4km+2k²+2k<5km. For the repaired polarity, sequential enforcement of the multiplication constraints fixes the outputs, and the identity p≡fg fixes the whole degree-(2d−2) certificate uniquely and accepts it precisely on the promise. For d=5km the field has enough points and (2d−2)/2^(4k)<1/6; four shared evaluations and independent address sampling give the existing O(k log k) protocol, including error control when no address is valid. The 0-rectangle proof uses projection density and existence of an accepted certificate at the selected valid address. The 1-rectangle proof uses uniqueness and 4k(2d−1)>m/(8k). The repaired N_k=km+4km(2d−1), 8√40<51 and k≤log₂N_k give the stated explicit bound, and Wang–Wu Fact 2.1 and their RP-to-NP query simulation give the two communication lower bounds. The frozen verifier checks components and sample parameters, not the final acceptance polarity; it was inspected, not executed.

## originality

PASS

For the repaired claim, the distinct result is the quantitative near-square-root exponent from shrinking the Wang–Wu certificate length while preserving its existence, uniqueness and linear verification interface. No novelty is credited for binary adders, constant comparators, the qualitative separation or the transfer laws for communication classes.

## value

PASS

For the repaired construction, the simple circuit substitution changes the effective growth of the input length from cubic to quadratic in the address-space size, while leaving the randomized communication and the rectangle bound in the underlying parameters unchanged. This improves the power of the actual input length from one third to one half up to logarithms, and thus strengthens the quantitative adaptive-query separation rather than just shaving a constant or renaming parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
