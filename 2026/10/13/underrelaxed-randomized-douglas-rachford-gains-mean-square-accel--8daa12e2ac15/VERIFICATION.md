---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For Algorithm 2 of Han–Su–Xie at A=I_2, b=0, two independent with-replacement uniform row reflections have product I or −I with probability 1/2. Thus the fixed-momentum scheme has scalar iid c_t∈{1,1−2alpha}, and exact recurrence x_(t+1)=(c_t+beta)x_t-beta*x_(t−1) for source x^1=x^0≠0. Fresh-sample independence gives the 3×3 second-moment matrix with first row (s+2mu beta+beta²,−2beta(mu+beta),beta²), second (mu+beta,−beta,0), third (1,0,0), s=1−2alpha+2alpha², mu=1−alpha. The simple leading eigenvalue s at beta=0 has derivative 2alpha(1−alpha)(2alpha−1)/s. This proves local strict acceleration 0<alpha<1/2 and worsening for alpha>1/2, with initial state exciting the dominant mode. At alpha=1/2, direct characteristic polynomial gives rho=1/2+beta²+O(beta³), hence no local speedup. At alpha=1/4,beta=1/10, independent exact symbolic determinant reproduces cubic 1000z³−685z²+56z−1; three rational disjoint sign-change intervals locate all roots and rho≈0.593480527629743<3/5<5/8. The original Theorem 4.1 sufficient stability coefficients are gamma1=87/100, gamma2=19/200. Theorem is about actual E||x||² rate, not ||E x||² or wall clock.

## originality

PASS

The original paper's Theorem 4.1 gives a valid but pessimistic expected-SQUARED-error upper bound which worsens with momentum; Theorem 4.2 instead accelerates a bound for the norm of expected error. Neither implies the actual second-moment spectral-radius improvement shown here inside the sufficient regime. Later adaptive/without-replacement sampling changes the Bernoulli reflection law. Related generalized stochastic-heavy-ball and pseudoinverse-free acceleration results lack this exact recurrence/phase boundary. Resultary hits on related accelerated splitting and stochastic momentum differ in algorithm, metric or sampling; no implication-equivalent published statement found.

## value

PASS

A mathematically motivated exact counterexample showing that an established mean-square upper bound can reverse the ranking of two actual schemes even inside its sufficient stability range. The explicitly derived second-moment matrix, local alpha=1/2 sign boundary, critical quadratic term, and rational stable numerical witness explain the mechanism. It is an instructive model-specific structural fact, not an unsupported universal algorithmic speedup claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
