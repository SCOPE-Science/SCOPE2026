---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS. Directly reconstruct L(x)=sum_{j<m}x_j+b x_m and its exact drift delta-(x_{m-1}-c)^2. Below delta<0 forces L(F^n x)<=L(x)-n(a*-a), hence linear norm escape; for arbitrary invariant probability bounded increasing arctan(L) gives strict integral contradiction without moments. At delta=0 telescoping on bounded trajectories makes x_{n,m-1}->c, and shifts make all coordinates converge; invariant probability invariance with arctan(L) gives the sole atom. Above delta>0 solves two real fixed points. Critical centered Jacobian P is a primitive stochastic m-cycle/(m-1)-cycle companion with stationary vector (1,...,1,b)/S, yielding simple center eigenvalue 1 and all transverse eigenvalues <1. Normalized center Q solves (P-I)Q=e1-e/S with Q_{m-1}=((m-1)(m-2)/2-b)/S^2; cubic parabolic iterate z'=z-z²/S-2Hz³/S³+O(z^4) yields the log coefficient S+2H=(m-1)^2-b. Local strong-stable tracking extends to every bounded orbit except exponentially converging ones. Independent SymPy exact drift and Q residual for all 3<=m<=12 tested with multiple rational b, without pretending this finite test proves the asymptotic.

## originality

PASS

PASS with qualified priority. The fixed-point fold and cubic-dimensional local dynamics are known (Zheng et al., 2018) and planar stationary moment identity is previously published; neither is claimed independently new. Richter (2002) treats the very same higher-dimensional generalized Hénon family, but available abstract/preview does not establish an identical all-Borel-probability threshold and universal m-dimensional log relaxation; institutional full-text access was blocked. Closest published Resultary entries concern other flows or a planar stationary variance identity. The assessed novelty is the joint global no-moment recurrence threshold and dimension-uniform orbitwise subleading log law; direct older implicit coverage remains an explicit nontrivial risk.

## value

PASS

PASS. The extension from local fold discriminants to all invariant probabilities without moment assumptions and an exact, dimension-parametric logarithmic relaxation coefficient addresses a natural dynamical threshold and critical slowing-down question, with consequences not mechanically implied by numerical orbit sampling. The strong-stable exception is mathematically necessary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
