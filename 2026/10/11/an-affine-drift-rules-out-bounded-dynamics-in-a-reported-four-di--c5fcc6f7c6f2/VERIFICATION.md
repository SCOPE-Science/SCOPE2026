---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For the exact printed polynomial vector field, define F=w-(b/4)(x+z). Differentiation yields xdot+zdot=1-4y, so LF=wdot-(b/4)(xdot+zdot)=-by-(b/4)(1-4y)=-b/4 identically for all real a,b and states; independently verified by symbolic coefficient cancellation. Thus along EVERY classical solution on its existence interval F(t)=F(0)-bt/4. For b≠0 a forward-complete bounded state cannot exist because F is a continuous affine state function. Any compact positively invariant set would contain a bounded forward-complete solution; any periodic orbit/compact attractor is impossible. For compactly supported invariant probability measure the integral of F would equal its translate by -bt/4 for all t, contradiction. No proof of global existence, and b=0 is excluded: (-1,1/4,±1,0) are exact equilibria when b=0. The source vector field and all seven source blobs are checked against their pinned identities; a complete Git tree was independently reconstructed.

## originality

PASS

Best-of-knowledge originality for the EXACT published autonomous vector field: the 2021 primary article (equations (2), Secs. 2.1–3, conclusions) asserts bounded hidden attractors but does not give a constant Lie derivative or a no-compact-recurrence theorem. The 2023 full-text reuse repeats the equations and bounded-attractor assumption without the obstruction. The same-authors 2022 follow-up concerns a newly constructed system with a nontrivial equilibrium, whereas the 2021 b-nonzero system has none; its full text was not obtainable. Resultary searches yielded the assessed finding itself and neighboring theorems for DIFFERENT Sprott vector fields, no earlier exact-system implication. General no-equilibrium/negative-divergence statements do not imply the no-compact-set conclusion. An unindexed prior correction remains possible.

## value

PASS

Though a short affine cancellation, the result is a substantive structural correction for a specifically published and subsequently reused dynamical model: it rules out the original paper’s claimed compact hidden/coexisting attractors for ALL nonzero-b parameters, not just one numerical simulation. Negative divergence and absence of equilibria do not establish this obstruction. Future dynamical studies of this exact flow need to know it before relying on attractor or stationary-measure assumptions. The result is not a general theory of Sprott systems; its precise model-validation motivation makes the exact boundary meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
