---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For an infinite iid uniform finite-field matrix, the leading-corner nullity D_n is a homogeneous Markov chain: up probability q^(−2d−1), down (1−q^(−d))² for d≥1, otherwise stay. Its zero-return generating function F=1−1/U with U=Σ a_{q,k}z^k and a=∏(1−q^(−j)), so joint probability of exactly b positive zero-visits ending at n is [z^n]F^b. Multiplying by q^(n²) gives exact integer count of GL_n with B_n=b. Drift to zero gives exponential first-return tails and aperiodicity. Renewal mean 1/c_q, variance (2A_q+c_q−1)/c_q², so analytic renewal-pole coefficient asymptotics yield conditioned CLT with asymptotic count variance 2c_q A_q−c_q(1−c_q)>0. Independently enumerated all matrices at q2 n≤3 and q3 n≤2 and matched exact renewal histograms. Fixed q, n→∞, all prime powers; finite samples alone not infinite proof.

## originality

PASS

Lvov arXiv:2610.00134, 15-page full text, Theorems 1–4, explicitly covers this exact leading-principal-corner **corank Markov chain** and recurrence; its introduction even calls the finite-field chain classical. The fundamental Markov property and transitions are therefore not original. That paper is about reversibility and recurrence over profinite local rings; it does not state the conditional finite-n count-by-number-of-zero-visits convolution or the explicit fixed-q Gaussian law and Euler-product variance. Independent renewal processing produces those exact natural count invariants. Best-of-knowledge PASS limited to enumerator and CLT, with strong prior premise and risk that a standard renewal-reward theorem implies the CLT generically.

## value

PASS

The exact joint count of nonsingular leading principal corners in a uniform invertible matrix is a natural elimination-pivot statistic, not given by the one-time rank distribution; the exact finite-size enumerator and explicit positive fixed-field fluctuation constant quantify its persistent dependence and give a useful distributional classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
