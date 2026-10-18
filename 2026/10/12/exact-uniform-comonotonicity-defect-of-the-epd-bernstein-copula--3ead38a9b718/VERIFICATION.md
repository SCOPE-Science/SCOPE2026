---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Set n=m+1. For the stated beta-sum C_m, binomial tails give C_m(u,v)=E[min(J_u,J_v)]/n, J_u~Bin(n,u), J_v independent Bin(n,v). For u<=v, M(u,v)-C_m=(1/n)E(J_u-J_v)_+, nonincreasing in v at fixed u, so global max lies on diagonal. Diagonal defect E|J-K|/(2n). Difference of independent paired Bernoullis is a lazy symmetric walk whose number of active steps N~Bin(n,2p(1-p)); conditional E|S_N| nondecreasing as number of steps grows, and 2p(1-p) max at p=1/2. At p=1/2, J-K~Bin(2n,1/2)-n, telescoping central-binomial sum gives E|J-K|=n*binom(2n,n)/4^n. Thus ||M-C_m||∞=binom(2m+2,m+1)/(2*4^(m+1)), global (1/2,1/2) maximizer and asymptotic 1/(2sqrt(pi(m+1))). Independently recomputed exact n=2..8 rational center identities and verified analytic monotonicity; finite grid not used to prove global bound.

## originality

PASS

The EPD beta representation of Blier-Wong et al. is precisely Baker’s bivariate order-statistic copula with n=m+1 (so the object is not novel). Baker 2014 full primary manuscript gives order-statistic formula, association indices and convergence to Fréchet upper copula but not the exact sup-norm approximation error or center-maximization proof within materially read text. Distinguish qualitative convergence and Spearman correlation from maximum vertical copula gap. Resultary search for central-binomial uniform comonotonicity defect found no stronger result; potential older Bernstein approximation identity risk remains.

## value

PASS

The EPD order-statistic Bernstein copula is a natural standard positive-dependence approximation to singular comonotonicity; the sharp Kolmogorov/uniform defect for every finite degree, exact extremizer, and sharp sqrt-degree constant are meaningful quantitative calibration facts beyond qualitative convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
