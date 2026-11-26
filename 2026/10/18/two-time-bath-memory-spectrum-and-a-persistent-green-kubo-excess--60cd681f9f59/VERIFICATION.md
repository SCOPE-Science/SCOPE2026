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

For gamma,r>0 the synchronized difference has Lyapunov drift -2(u-v)^2-r u^2, bounded above by a negative multiple of u^2+gamma v^2; the same Lyapunov function on one process adds only the constant noise input 4. This gives bounded second moments and contraction, hence a unique invariant law (synchronous convergence extends to arbitrary finite-valued starting states by truncation). The generator on X^2,XQ,Q^2 yields exactly the equations in RESULT.md (56–58), including c=b+1. Conditional first moments propagate by M because only X jumps to zero; thus the lag covariance is the first coordinate of exp(tM)(a,b)^T. The two roots of the decay polynomial are positive and distinct. Writing rho=b/a in (1/2,1) and g=1/gamma, evaluation of that polynomial at d=1+r-rho gives (rho-1)(rho+g)-r rho<0, so both residues are positive. Direct inversion yields (a+gamma b)/r; the same-variance comparator has covariance a exp(-rt) (its diffusivity is chosen to give variance a), whereas the unit-diffusivity comparator has integral 2/r^2. Their distinction is respected. The derivative of 1+gamma b/a is strictly negative. At fixed gamma, k_f-(1+r)=g/(k_f-g)=O(1/r), k_s tends to g, and rho tends to 1/2; the slow amplitude is r^-2+O(r^-3), the fast amplitude 2/r+O(r^-2). This proves the fixed-positive-lag limit and the two separate area contributions gamma and 2 after r^2 scaling, without interchanging a nonuniform pointwise limit and integration. The finite matrix comparisons and Euler/Bernoulli reset simulation are recorded corroboration (not rerun); the simulation approximates continuous-time Poisson resets by fixed-step trials, and neither check is needed for the proof.

## originality

PASS

Credit is limited to the evaluated stationary autocovariance weights and the integrated/fixed-lag strong-reset laws for the retained bath. The model and one-time statistics are prior, and Goswami is an earlier overlapping source than the frozen attribution to Santra–Das suggests. The matrix-exponential method itself is standard. No covering prior result for the evaluated covariance and large-rate excess was established in the examined evidence.

## value

PASS

The time-integrated observable detects a persistent discrepancy even when the one-time variance and short-time scaling look like isolated resetting. Identifying both a slow tail with amplitude order r^-2 and a fast contribution of the same integrated order gives a concrete reason for the excess and determines the leading accumulated-observation variance. This is useful for the specified single-bath model without claiming universal behavior or novelty of the generator method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
