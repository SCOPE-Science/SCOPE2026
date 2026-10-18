---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: For N finite disjoint supported nonnegative wells W_Y, disjointness gives exact ||W_Y||_(3/2)=N^(2/3)||v||_(3/2). Radial v with L²(0,rho) profile is L^(3/2)(R³) by compact support/Hölder. For u∈H¹(R³), Hölder and 3D Sobolev yield integral W_Y|u|²<=C_S N^(2/3)||v||_(3/2)||grad u||². Therefore q_H[u]>=0 for all admissible geometries when 0<lambda<=1/(C_S N^(2/3)||v||_(3/2)); compactly supported L^(3/2) form perturbation has essential spectrum [0,infty), so inf sigma(H)=0 for all those Y. For sufficiently large fixed loop length relative to support radius, regular polygon and a noncongruent small smooth loop deformation retain disjoint wells, giving two tied geometries, contradicting a literal unrestricted unique maximizer. Proof analytic, not relying on experiments. A zero resonance at threshold is possible but does not change inf sigma=0.

## originality

PASS

PASS, narrowly qualified: Exner Conjecture 5.3 in materially inspected 2023 original explicitly states a unique regular-loop maximizer for two and three dimensions; its discussion independently notes that in 3D a single regular attractive well needs critical coupling for binding. The novel claim is the uniform all-admissible-geometries N-dependent explicit Sobolev nonbinding plateau and consequent missing binding hypothesis for that exact literal global uniqueness assertion, not the general textbook Sobolev inequality or existence of single-well thresholds. Older point-interaction optimization binds by a different mechanism, not a regular potential counterexample. The concession about a restricted interpretation of principal eigenvalue is essential; no false assertion that binding-regime conjecture is disproved.

## value

PASS

PASS, limited: Provides a rigorous necessary boundary condition for a named geometry-optimization conjecture: without binding one cannot have its literal uniqueness in three dimensions, and a quantified uniform coupling interval exhibits the obstruction. Although the estimate is a straightforward Sobolev/Hölder bound and not a sharp binding threshold, applying it uniformly to a natural conjectured optimization family produces a substantive scope correction rather than an arbitrary negative test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
