---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For every real norm-one strongly exposed point supported on a finite maximal antichain alpha, each branch intersects alpha exactly once and norm-one mass one at alpha kills all off-antichain coordinates. For y in the strict f_alpha slice, epsilon_s=1-sign(x_s)y_s >=0 and sum epsilon_s<N delta. Every chain extended to a branch through s contributes ||y-x|| at most |1-a|+1-|a| <=2 epsilon_s, uniformly <=2 max epsilon_s <2N delta; the diameter also bounds by 2. Moving epsilon<min(1,N delta) from one antichain s to a strict descendant gives a unit-ball vector with f_alpha=1-epsilon/N and ||y-x||=2 epsilon. Limit epsilon->min(1,N delta) proves the sharp supremum including the strict-slice transition delta=1/N. No finite experiment substitutes for the analytic proof.

## originality

PASS

Best-of-knowledge PASS for the sharp local radius law, distinct from the known qualitative strong-exposure characterization. The latter supplies the canonical antichain exposing functional but not the equality rho(delta)=min{2,2N delta}. Explicit branch-norm reduction plus a descendant perturbation is required to obtain the sharp slope and saturation. General density/residuality of exposing operators and unrelated tensor exposed-point statements have no implication to this antichain radius.

## value

PASS

Strong exposure of these points directly drives the source’s dentability result. An exact pointwise modulus with visible dependence on antichain size is a naturally needed quantitative refinement, not a mere reformulation of strong exposure: it gives a sharp linear rate and exact saturation threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
