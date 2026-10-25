---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Take X~Bin(21,1/2), Y=floor(3X/5), and F(t)=2^21 E[t^Y] of degree 12 with the displayed exact binomial coefficients. F has four real simple roots and four conjugate pairs: rational centers with radius 10^-5 satisfy 8 disjoint exact Taylor/Rouché inequalities, plus conjugate disks. Interval polynomial arithmetic certifies a strictly positive degree-2 factor and two strictly positive degree-5 factors, hence normalized law is P5. For any nonnegative real factorization, irreducible factors are four real linears plus four real conjugate quadratics. Conservative interval tests retain 41 possibly nonnegative groups of degree at most 4. Exhaustive subset partition DP proves that even this optimistic family cannot cover all eight irreducible factors; hence not P4 or any smaller j. Independently recomputed coefficient list, rational disk inequalities, positive 2+5+5 grouping, all 41 optimistic candidate groups, and absence of a <=4 cover. This is an exact finite rational certification of the precise 21-trial law, not a numerical-root heuristic.

## originality

PASS

Liggett 2021 explicitly gives the SAME random variable, and proves it is not P4 but is P6; Section 3 leaves membership in the intermediate P5 undecided. The current exact factorization establishes P5, sharpening the known degree bound from [5,6] to exactly 5. The lower bound itself is prior, not claimed new. Resultary semantic searches under floor/truncated binomial, convolution and factorization degree found no matching P5 result. O PASS best of knowledge, with residual unpublished factorization/certificate risk.

## value

PASS

This closes the unique natural integer gap P5 in Liggett's concrete 21-trial extremal example: the minimal maximal summand support is exactly five. A rigorous positive decomposition and exhaustive lower-degree obstruction address a precise published quantization/convolution question, not an arbitrary factorization of a random polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
