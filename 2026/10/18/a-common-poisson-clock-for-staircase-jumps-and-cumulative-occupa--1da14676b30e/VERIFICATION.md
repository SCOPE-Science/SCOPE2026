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

Use the same iid uniform levels and independent exponential marks for every p. Then S_k=−log(a_k) is the arrival clock and the ceiling of E_k/[−log(1−p a_k)] has exactly the positive-integer geometric law, with the endpoint p a_k=1 handled separately by G_k=1. At the n-step cutoff completed holds contribute Σ λ_jG_j and the unfinished hold contributes λ_K(n−T_K), with n−T_K<G_K. The sum of |λ_jG_j−E_j| has expectation at most Σ 2p·2⁻ʲ≤4. For q=ceil(3t), the high-probability event in Step 3 controls S_q, the extrema of the first O(t) exponentials and their sum by gamma/exponential tails. For S_k≤t−10 log t the upper hold sum is at most 6t e^{S_k}/p+q<n. If S_k≥t+10 log t, S_{k−1}≥S_k−3 log t, its rate is at most 1/2, and its last hold alone is at least e^{S_k}/(2p t⁶)>n. This excludes q and larger indices and brackets K by the two Poisson counts. Unfinished reward is bounded by E_K+1; the mark sum over the clock band has expectation equal to the band length by independence. This proves both errors on the same coupling and uniformly for deterministic triangular p. The compound-Poisson jump (1,E) has second-moment matrix [[1,1],[1,2]], giving the joint CLT by characteristic functions since log(t)=o(√t). Independent finite checks: the chain is the running minimum of Bernoulli-p accepted uniforms, hence P(X_m>x)=(1−px)^m for 0≤x<1; integration and the jump compensator give the stated means and bound the geometric-harmonic remainder by e^{−np}/(np). At p=1, integrating the two joint-survival triangles gives E[M_iM_j]=1/[(j+1)(j+2)]+1/[(i+1)(j+2)] for i≤j. Rank independence gives zero covariance of I_j and M_i for j≤i; for i<j integrate the new record over 0<u<M_i with factor (1−u)^{j−i−1}, giving the claimed covariance. Their sums and the independent record indicators give the three calibration formulas.

## originality

PASS

The chain, marginal mean, state-vector law, count and occupation transforms, and separate fixed-p record/minimum limit laws are not the distinct claim. The supported advance is the explicit simultaneous marked approximation with a uniform quantitative error and no rate restriction beyond np_n→∞, yielding the joint covariance. None of the inspected statements gives that coupling or a stronger result that has been shown to imply it.

## value

PASS

This directly answers how jump count and integrated occupation fluctuate together for a studied stochastic model. The approximation explains the cross-covariance using shared randomness rather than combining scalar limits. Its uniformity also controls sparse triangular thinning, where a fixed-parameter CLT alone cannot be applied without additional analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
