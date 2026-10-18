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

PASS: Directly reconstructed the n-parameter contact perturbation: k_i=1+(i-1)/(n-1), pi_i=1/n, W_ij=2, Wtilde=W+(1/4)uu^T, u=(k_2,-k_1,0,..). Since u^T diag(pi) k=0, W diag(pi)k=Wtilde diag(pi)k=3*1. With gamma_i=3/k_i-1, both vector fields on z=k*x reduce identically to k_i*x*(1-3x), x(0)=1/5. Polynomial ODE uniqueness proves equality for every t>=0; x=e^t/(2+3e^t), nonconstant, and all z_i stay <1. Bounds: 1<=k_i<=2, 0.2<=z_i(0)<=0.4, 0.5<=gamma_i<=2, Wtilde entries in [1.5,3], hence both in original P_(m,M) for m=0.1,M=4 and pi positive. Distinct initial prevalence values preclude any block of size >=2 under Definition 3.2. The two-community classification follows because det G=0 iff the positive analytic trajectory lies on its initial proportional ray; normalized transverse velocity is proportional to affine P-Qx, identically zero for nonstationary motion iff P=Q=0. The integral Gram-wedge identity yields T^4 coefficient (k*x0^2*delta)^2/12 and, after zero first transverse jet, T^6 coefficient (k*x0^2*Q*v)^2/45. Independent exact rational two-community substitutions and second-jet boundary checks corroborate; finite tests alone do not prove the universal theorem.

## originality

PASS

PASS (best knowledge): The 2026 published primary article literally states in Definition 3.2 and Conjecture 3.3 that not-block-regular should imply reconstructible, explicitly claims the two-community implication as established but omits proof. Its Gram invertibility criterion proves low-rank trajectories are nonreconstructible, but does not construct this strictly positive symmetric, unequal-prevalence, nonstationary family or classify the two-community transverse Gram orders. A 2022 PNAS nonidentifiability surrogate treats a general low-subspace mechanism; that principle does not make the proposed later block-regularity counterexample an already published special case. Contrasts concern theorem implications, not just matching keywords.

## value

PASS

PASS: Disproving a named published identifiability conjecture inside its own model, including the authors' claimed two-community positive case, is substantively valuable. The explicit admissible all-size construction identifies heterogeneous recoveries and proportional prevalence as a second mechanism, and the two-community Gram asymptotics quantify exact observability transition orders. It does not purport to describe noise robustness or all higher-dimensional singular families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
