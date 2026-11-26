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

Choose the k distinct threshold sites first and give each A particles. The remaining mass on them has exactly the weak-composition count in (1), conditional on the independent bulk sum with law u_n/z. For fixed k the permitted mass divided by L converges to e>0, so the sector divided by z^(L−1)L/θ_L tends to b^(k−1)/(k!(k−1)!), with b=e/(Θz). The sector k=0 is exponentially small relative to that normalization by bounded-variable concentration. Uniformly for k≤L, bound the binomial numerator by ((R+1)L)^(k−1) for N_L≤RL and the choice of sites by L^k/k!. Together with θ_L≥cL² this yields the summable bound ((R+1)/(cz))^(k−1)/(k!(k−1)!) on the normalized sector weights; it remains summable against every fixed power of k. This justifies the count normalization and the Bessel formulae, including the mean since the k-weighted series is I_0(2√b). Given k, the extra polynomial weighting of the bulk sum is bounded after division by L^(k−1), with denominator tending to e^(k−1)/(k−1)!; its atypical mass tends to zero. Conditional on the remaining mass M_L, the site-label-ordered excesses are uniform lattice compositions. Riemann sums on their simplex give the uniform Dirichlet law at each fixed k (a point when k=1), and M_L/L→e and A/L→0 give the claimed scaling. Tightness of k gives the joint limit on the disjoint union of mass-vector strata; the prelimit strata allow variable total mass and the limit is on the sub-simplex of total e. The supplied checker was read, not run. It tests finite enumeration and convergence of counts for the three implemented weight choices, not the asymptotic theorem or the full mass law.

## originality

PASS

The frozen result gives the precise count and mass law on the quadratic fast-rate boundary left open in the directly relevant published papers. There is demonstrable limiting-law coverage by a later dated indexed theorem on exponential-tail bulks, not merely a similar formula: its fixed-parameter model and this bounded-bulk model are asymptotically equivalent after normalization, and the alternate cutoffs and ranking can be reconciled. This subsequent coverage is credited explicitly; it is not evidence of an antecedent solution or of independent chronological priority. The pass is for the critical fast-rate law relative to the inspected antecedent results, not for the general exponential-bulk extension or for the classical Bessel/Dirichlet identities themselves.

## value

PASS

The result answers the specific open critical-scale stationary question for the fast-rate model. It distinguishes a finite random number of condensates from both a growing mesoscopic cloud and a single macroscopic condensate, gives the exact parameter from the physical excess density and weight normalization, and describes the joint allocation of macroscopic mass. The significance is the normalization and joint limit at the model's transition, not the use of a named distribution or a finite numerical fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
