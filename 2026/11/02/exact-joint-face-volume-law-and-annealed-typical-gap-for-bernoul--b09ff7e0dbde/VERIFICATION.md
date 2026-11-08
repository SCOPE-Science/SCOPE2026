---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Each signed coordinate pair independently contributes two, one or zero retained vertices, so (K,L,d-K-L) is multinomial and the hull is a K-crosspolytope with L pyramids when K>=1, otherwise an (L-1)-simplex. The face polynomial follows by multiplying by (1+z) for each pyramid, and intrinsic volumes follow from orthogonal unit-height apexes. Full dimension requires no missing coordinates and K>=1; conditional K is Bin(d,rho) conditioned positive, rho=p/(2-p). Hence R=2^(K-d), Z=2^(d-K)(3^K+1), exact moments by the binomial pgf, full-dimensionality probability and unconditioned ambient-volume moment follow. Binomial LLN/CLT and a bounded log(1+3^(-K)) remainder yield the joint rank-one Gaussian limit; strict logarithmic concavity yields annealed > typical exponent gaps for 0<rho<1. Independently checked the conditional binomial and endpoint d=2,3 canonical face-polynomial identities algebraically; no asymptotic conclusion depends on finite experiments.

## originality

PASS

Best-of-knowledge original contribution after comparing actual claims and implications with primary literature: New explicit multinomial conditioning and limiting-rate comparison are additional propositions; no stronger inspected theorem directly states them.

## value

PASS

Independent vertex thinning of an archetypal centrally symmetric polytope is a natural sparse random-polytope benchmark. Its exact joint combinatorial/geometric spectrum and asymptotic distinction between mean and typical face complexity and volume are useful calibration quantities, not merely an arbitrary face-count table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
