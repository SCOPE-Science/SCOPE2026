---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Normalize v and resolve Av into its components μv and σw with w a unit perpendicular vector. Independent Gaussian rows make the sketches of v and w independent centered isotropic normals. Given the first sketch, its inner product with the second divided by its length is a standard normal with conditional law independent of that length. This gives σZ/χ_s (equivalently σt_s/√s) for the centered scalar, with the stated strict moment threshold and variance. For fixed interior μ, both escape tails increase strictly with σ; the positive semidefinite spectral polynomial (MI−A)(A−mI) shows precisely which directions maximize σ. Writing q=√(p/(1−p)) differentiates the sum of reciprocal-threshold tails to c_s(q^(s−1)−1)/(1+q²)^((s+1)/2), proving strict balance for s≥2 and constancy for s=1. The boundary limits equal 1/2 while at the exact eigenvector the escape probability is zero. At balance, χ_s²/(χ_s²+Z²) is Beta(s/2,1/2), and its CDF at 1/2 has the quoted endpoint asymptotic by the beta integral. These calculations establish the result for every fixed real symmetric A with m<M and every positive integer s; the uploaded numerical verifier was read but not run.

## originality

PASS

The assessed distinct result is the pointwise fixed-mean extremal law for arbitrary fixed symmetric spectra, including its equality set, orientation dependence and sharp unconditional half-probability supremum. The Gaussian Student law, its moment frontier, the absolute-tail beta expression, and the extremal interval-variance inequality are ingredients, not new distribution results. The closest two-eigenvalue source also gives the conditional escape thresholds and hence the pointwise endpoint-mixture formula before averaging. Neither that proof nor the earlier related sketched Ritz moment statement solves the stated extremal question over starts in a general fixed matrix.

## value

PASS

Establishes that no finite unconditioned Gaussian row count lowers the worst-direction spectral-interval escape probability below 1/2, even though balanced endpoint mixtures have exponentially small escape and the limiting eigenvectors never escape. It identifies the unique spectral form of extremizers at fixed mean and the approach to the obstruction; a tail estimate alone would not answer these questions. This is about exit probability, not an order-one error magnitude or a claim about a full restarted solver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
