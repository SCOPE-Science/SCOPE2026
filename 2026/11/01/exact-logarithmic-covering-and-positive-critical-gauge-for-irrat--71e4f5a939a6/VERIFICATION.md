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

# Reproducibility and proof boundaries

Run the package-local `CHECK.py` using Python 3 and its standard library. It prints:

`PASS: 230 exact-rational word-count/separation tests`

The checks use four reduced rational approximants to golden-mean rotation and 20 finite symbolic depths each; they also establish the separation inequality at 30 finite scales for each of five rational contraction factors. All arithmetic in these checks is rational, without a floating-point tolerance. These experiments do not certify the infinite irrational-rotation word-complexity assertion, the continued-fraction gap bound, or positivity of Hausdorff measure. Those statements are proved in the `RESULT.md` argument, using the primary papers' explicitly cited coding and invariant-set descriptions.

Critical proof dependencies: (1) the complete two-sided invariant set is the closure of the monotone irrational rotation coding; (2) Sturmian length-\(n\) factor complexity is \(n+1\); (3) the strict inequality \(1-2\lambda>\lambda\) for \(\lambda<1/3\) prevents one covering interval from meeting distinct depth-\(n\) prefix sets; (4) bounded continued-fraction coefficients control largest circle rotation partition gaps and permit the mass-distribution lower bound. The comparison with Janson--Öberg's published Problem 6.4 and upper bound is separate from these correctness dependencies. Publication priority is not independently established.
