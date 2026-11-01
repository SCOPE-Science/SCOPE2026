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

For m integer-frequency planar oscillators xdot_j=jJx_j+e1*u over exactly T=2pi, the terminal response columns b_k of any partition sum to the integral of all positive integer-frequency sines/cosines over the period, hence sum b_k=0. The rank is at most N-1, so N<=2m cannot reach arbitrary y∈R^{2m}, regardless of nonuniform positive segment lengths. On uniform N>=2m+1, each b_{j,k}=Δ sinc(jΔ/2)(cos(jc_k),-sin(jc_k)); discrete Fourier orthogonality for frequencies ±1,...,±m yields weighted Gramian W_N=π diag_j(sinc²(jπ/N)I2)>0. Least squares gives E_N(y)=π^{-1}sum||y_j||²/sinc²(jπ/N) versus continuous E_*=π^{-1}||y||². Sinc decreases on (0,π), so worst-target ratio exactly sinc^{-2}(mπ/N), <π²/4 at minimal N=2m+1, approaching π²/4 as m→∞. Independent numerical direct integral/Gramian comparisons verified 15 finite banks, including full-period zero column sum; analytic DFT covers all m,N.

## originality

PASS

The general sampled-control reachability and Riccati literature offers prior machinery but not an identified exact finite hold-count law for the resonant common-actuator family. Berlin–Galyaev–Lysenko studies bounded minimum-time switching for two nonsynchronous oscillators; it is not unrestricted fixed-2π all-target L2-energy control. Bourdin–Trélat 2020 proves eventual small-mesh reachability, not the sharp N=2m+1 obstruction/construction, and their 2016 and 2023 work addresses general LQ/Riccati and convergence. Fourier orthogonality and sinc response are classical ingredients; the combined sharp resource plus worst-energy theorem is the surviving claim. Historical harmonic sampling priority risk remains.

## value

PASS

For a bank of harmonic oscillators sharing one scalar actuator, the smallest number of piecewise-constant control holds needed to hit every terminal state is a natural hardware and control resource. The theorem proves impossibility under arbitrary timing, gives a matched uniform design and exact worst-target L2 overhead <π²/4 with sharp large-bank limit. The general sampled-control convergence literature gives no finite quantitative budget/loss guarantee; the conclusion is a motivated complete structural result despite elementary Fourier tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
