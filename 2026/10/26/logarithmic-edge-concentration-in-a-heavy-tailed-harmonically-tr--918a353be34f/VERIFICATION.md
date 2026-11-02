---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Reconstructed stationary sign process from a two-sided equilibrium alternating renewal law, the unique stationary harmonic convolution Y_t=integral_{-infinity}^t e^{-(t-u)}sigma_u du, and entrance gap D=2-(Z+1)e^{-U}>=2(1-e^{-U}). The near-zero run law bounds Pr(D<delta)=O(delta^eta), establishing exponentially thin log-gap tails. The positive-age measure at a stationary observation is ar F(a) da/(2m), leading to the exact H([log(D/eps)]_+) term. The negative sign contributes J([log(D/(2-eps))]_+) and is O(eps). Karamata/integration of regularly varying survival yields H(L)~c L^{1-beta}/(beta-1). Split D>=e^{-L/2} versus its exponentially rare complement, apply dominated convergence to the long-tail ratio, then reflection symmetry and tail integration yield both edge coefficients and divergent all positive reciprocal-gap moments. Checked that m=1/(beta-1),c=1 gives 1/2 for Lomax, and half-t density has m=1,c=1/2,beta=2 giving 1/4. The exact identity depends on the distribution of the stationary positive-run entrance gap and makes no finite-time claim.

## originality

PASS

Farago and Smith (2024) provide the established more general non-Markovian trapped RTP and stationary integral equations; those are credited. Their inspected half-t numerics use nonlinear sine force and do not give this sharp harmonic integrated edge coefficient. Guéneau-Majumdar-Schehr (2023) focuses on periodic/Poisson resetting, and other standard harmonic RTP works use exponential runs, which do not imply the regularly varying log-edge law. A hidden general consequence of earlier integral equations is a residual novelty risk.

## value

PASS

A natural stationary boundary observable of non-Markovian active particles has a qualitatively different inverse-logarithmic singularity from Poisson run-time algebraic edge scaling. The closed leading constant over the entire regularly varying family, exact renewal identity and resulting blow-up of all inverse-gap moments answer a motivated model-specific asymptotic question left implicit by the general numerical integral equations, rather than merely rename a renewal identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
