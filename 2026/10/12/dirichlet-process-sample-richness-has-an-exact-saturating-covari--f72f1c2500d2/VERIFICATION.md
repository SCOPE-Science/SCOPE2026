---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For P~PD(0,theta), theta>0, iid draws and K_n distinct species, H(P)=-sum_i P_i log P_i, use discovery increment I_{n+1}. Given P, E I_{n+1}=sum_i P_i(1-P_i)^n. First two size-biased GEM variables V1,V2 iid Beta(1,theta) yield equal-species part E[-V1 log V1 (1−V1)^n] and distinct-species part E[(1−V1)^{n+1}(−log[(1−V1)V2])]. Direct beta differentiation gives formulas A_n=theta/((theta+n)(theta+n+1))[psi(theta+n+2)−psi(2)] and B_n=theta/(theta+n+1)^2+theta/(theta+n+1)[psi(theta+1)−psi(1)]. Subtract theta/(theta+n)EH and simplify to Cov(I_{n+1},H)=theta/((theta+n)(theta+n+1))sum_{j=1}^n 1/(theta+j), strictly positive. From K1=1, telescoping/summation-by-parts gives finite covariance theta[sum_{k=1}^{n−1}(theta+k)^{-2}−(theta+n)^{-1}sum_{k=1}^{n−1}(theta+k)^{-1}] and trigamma form, with limit theta psi1(theta+1). Independently evaluated the distinct special-function and finite-sum expressions for theta=0.3,1,2.5 and n=1,2,4,10,100 at 35 decimal-digit precision. Under DP Chinese-restaurant independent new-table Bernoulli indicators, Var(K_n)~theta log n; JMLR's exact prior entropy variance V_H=theta/(theta+1)^2+psi1(2)/(theta+1)−psi1(theta+2) yields the claimed scaled correlation limit. n1 zero. Finite calculations do not replace analytic proof.

## originality

PASS

Distinguishes joint prior-predictive Cov(K_n,H(P)) from posterior entropy estimates, fixed-P accumulation identities and joint richness with unbiased Gini–Simpson. Archer–Park–Pillow give prior H moments and posterior H conditional on frequency counts; Cerquetti's Bayesian diversity moments concern Tsallis indexes and diversity posterior. Neither examined scientific passage directly provides the finite-n unconditional K_n-H covariance or its exact saturation/correlation constant, despite potentially implying it after a new joint moment calculation. Best-of-knowledge PASS with a concrete terminology-equivalence risk.

## value

PASS

Quantifies a genuine distinction between unboundedly varying richness and a bounded absolute information-association with the random latent Shannon diversity under a benchmark Dirichlet-process prior. Exact monotone n law, saturation ceiling and correlation decay constant are jointly useful for assessing richness as an entropy proxy and prior predictive uncertainty, beyond the standard mean/variance of H alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
