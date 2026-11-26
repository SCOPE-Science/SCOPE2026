---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Detailed balance holds for a transfer from i to j because moving one particle multiplies the product occupancy weight by w_j/w_i, exactly compensating the departure rates; the symmetric destination factor cancels. Positive rates and complete routing give irreducibility. Counting ordinary-site compositions gives the finite slow marginal, including s=N_M. Factoring out a common constant represents it as exp(c·h/√M) times the probability that an iid geometric sum equals N_M−s; its site mean and variance are 1/(a−1) and a/(a−1)^2. The span-one local CLT, with floor error at most one, gives the asserted Gaussian on compact rescaled lattices. The log successive-mass ratio has derivative −(M−1)/[(k+M)(k+1)], bounded above by −constant/M over the relevant lower tail; summing from the mode at M/(a−1)+O(1) gives a discrete Gaussian envelope times O(M^−1/2). The maximum mass bound also covers points above the mode. At fixed total s there are binom(s+r−1,r−1) lattice points; hence the Gaussian envelope still dominates any polynomial test and the bias exp(||c||∞s/√M), after Riemann rescaling. This justifies normalization, weak convergence and every mixed polynomial moment. In simplex coordinates x=tp the Jacobian gives t^(r−1); at c=0 the direction is independent uniform Dirichlet for all δ, and it is only at δ=0 that the radius is σ chi_r (Rayleigh for r=2). With arbitrary c the simplex law conditional on t is weighted by exp(tc·p), with no angular effect when all biases are equal. Independent finite canonical evaluations agree with the predicted tied r=3 and biased r=2 limits; these are diagnostics, not the justification of the asymptotics.

## originality

PASS

The finite composition marginal, critical density and the conditional product framework follow from established zero-range theory and are not original components. The supported distinct contribution is the full deterministic fixed-r joint critical-window evaluation with weak rate splitting and moment convergence, including the exact critical chi/Dirichlet factorization for general r. There is demonstrable two-site overlap with another, later-dated catalogue result despite the different routing; this and the unresolved older thesis are explicit limitations, not priority findings. No inspected earlier claim supplies the general fixed-r window evaluation.

## value

PASS

Resolves how competing deterministic defects share the critical excess: the total and proportions have distinct, explicit laws, and a rate perturbation of precisely the stated scale changes the proportions by a nontrivial tilt rather than automatically selecting a single site. The joint law and all-moment convergence supply a quantitative reference for finite-defect competition, beyond the known stationary product weights or a critical-density threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
