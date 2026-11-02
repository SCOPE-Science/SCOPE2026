---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS: Reconstructed product c_n=3^n/n! product_{h=0}^{n-1}(3h+1) and the 2-adic carry count from the -2/3 binary expansion 0101... . For n<4^L no carry survives past the 2L input bits; direct four-choice two-bit transition counting gives exact 2x2 matrix, including L=0. Its trace 2+z+2z^2 and determinant 4z^2 give the rational generating function. Differentiating the recurrence gives the exact stated mean and variance; the dominant analytic eigenvalue at z=1 is 4, with derivatives 4 and 16/3, the other eigenvalue 1, so quasi-power characteristic functions give the CLT. Independently enumerated valuations via the coefficient ratio for all 21845 samples in blocks L=0..7 and matched complete histogram and rational moments to the transfer, using /mnt/data/independent_math_checks_scope05.py. This finite sample is not the CLT proof.

## originality

PASS

PASS best-of-knowledge: Straub, Moll and Amdeberhan (2008, 2009) already obtain 2-adic coefficient integrality, the underlying carry representation and a criterion for odd coefficients. They do not state the complete dyadic-block histogram, bivariate rational distribution generating function, finite variance or Gaussian fluctuation theorem in the inspected full preprint. New contribution is transfer-operator enumerative synthesis and limit law, not the underlying carry identity; unindexed statistical presentations remain a risk.

## value

PASS

PASS: The known thin set of odd 3-central binomial coefficients makes the full valuation distribution a motivated natural arithmetic statistic. Exact full-block histograms, finite-size variance and Gaussian typical scale are substantive distributional information, not a pointwise rewriting of the carry formula. The scope is precise complete 4^L blocks, not arbitrary truncations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
