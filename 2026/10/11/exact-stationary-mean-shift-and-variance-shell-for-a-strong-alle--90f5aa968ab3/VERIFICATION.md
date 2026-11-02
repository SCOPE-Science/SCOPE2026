---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For every compactly supported invariant Borel probability measure in the strict positive quadrant, log x and log y are smooth and bounded on support so their generator integrals vanish. The exact predator identity ωx/(1+ηx)-σ=ω(x-x*)/[(1+ηx)(1+ηx*)] gives E[(x-x*)/(1+ηx)]=0. Writing x=x*+(x-x*) in the decomposition of E[x-x*] proves E[x]-x*=ηE[(x-x*)²/(1+ηx)] ≥0. A vanishing square forces x=x* on invariant support; invariance then forces dot x=0 there and y=K(1-x*)(x*-α), hence only the coexistence Dirac. Averaging log x gives E[y]/K=E[(1-x)(x-α)]=(1-E[x])(E[x]-α)-Var(x), exactly the second formula. E[y]>0 yields α<E[x]<1. The parameter inequality is precisely α<x*<1 and makes equilibrium y*>0. Exact arithmetic independently verified both rational identities, numerical x*=110265/183841, and a nondegenerate two-point weighted-moment check. These finite checks corroborate, but do not replace, the all-measure analytic proof.

## originality

PASS

Best-of-knowledge originality of the PAIRED source-specific invariant-measure mean-shift and predator/prey-variance-shell constraint, not the generic Holling-II Jensen bias alone. The primary Ma–Zhao–Du article was materially read, including model, positive equilibrium, Hopf and numerical cycles; it does not state the paired stationary identities. The published Rosenzweig–MacArthur fiberwise theorem supplies the identical saturating-response mean-excess algebra after rescaling h=1/η and is PRIOR coverage of that first ingredient (and even strengthens it conditionally), but is for a different prey vector field and has no stated or implied Ma–Zhao–Du quadratic-prey mean-predator shell. Xie and Zu–Mimura involve different prey equations; published delayed, cooperation and food-chain results establish analogous moment laws for different systems without an exact implication for this paired statement. No examined general theorem dominates the complete two-identity claim. An inaccessible plausible 2010 source remains a disclosed historical-priority risk, not a reason to claim proven novelty or automatic failure.

## value

PASS

The natural objects are the compact positive stationary statistics and finite-amplitude periodic cycles of the established Ma–Zhao–Du strong-Allee Holling-II flow, where source research highlights Hopf-born coexistence oscillations. Beyond the familiar Jensen mean-elevation ingredient, the paired exact quadratic prey-variance/mean-predator shell controls the biological mean predator abundance in terms of mean prey density and prey fluctuation for every invariant measure, without near-Hopf or stability assumptions. The resulting strict prey-mean > x* ordering is an observable cycle diagnostic and the shell quantitatively constrains any numerical periodic-state estimates. It is a modest model-specific structural lemma, not a new global classification or a general averaging principle, yet it supplies a precise exact natural fact not found as an already stated implication of the inspected primary papers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
