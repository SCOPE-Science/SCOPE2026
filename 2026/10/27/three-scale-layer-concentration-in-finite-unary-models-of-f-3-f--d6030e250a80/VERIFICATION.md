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

The identity fixes f²(x), so these are labelled rooted forests of height at most two, including shallower components. Choosing and connecting the three layers proves the profile count, with the identity map the only r=n, s=t=0 case. The nested labelled set construction proves the EGF including its empty-size term. Differentiating the entropy weight F gives b=ae^a, r=ae^b and n=r[1+b(1+a)]; all factors increase and the last expression ranges from zero to infinity. The displayed negative Hessian has the stated positive determinant. In relative coordinates on the ε-rectangle, its top diagonal entry is bounded below by a constant times s_*, its cross term is O(s_*), and its bottom diagonal is bounded below by a constant times t_*; t_*/s_*=a→∞, so its minimum eigenvalue is bounded below by a positive multiple of s_*. Integrating twice gives an Ω(ε²s_*) loss on the boundary, and concavity extends it to all exterior profiles, including the limit t=0. Along the ray to the identity profile the finite endpoint limit is F=−n log n, consistent with its weight one up to the same Stirling error. Rounding the two saddle coordinates costs O(s_*/r_*²+t_*/s_*²)=o(1) in F. Uniform O(log n) Stirling errors and O(n²) profiles are negligible compared with s_*~n/W(log n), since log n=b+O(log b). This proves the joint bound and then T/n→1. The inspected checker is finite corroboration for the count through n=6, not evidence for the concentration bound; it was not run.

## originality

PASS

The elementary labelled profile count and nested exponential construction are not the basis for an originality pass. The supported distinction is the joint relative concentration of root and depth-one layer sizes under uniform labelled sampling, with explicit saddle scales and an exponential rate at scale n/W(log n). The closest inspected records change either the measure, the observable, or the limit, and general counting constructions alone do not give the two-coordinate tail on this nonuniform scale.

## value

PASS

The axiom gives a natural test case in which almost all vertices lie at depth two, yet the two smaller layers are separated by another diverging scale. An explicit joint exponential estimate, rather than total model counts or a marginal limit, makes it possible to control simultaneous depth-profile exceptions. It is a structurally informative quantitative result for the uniform labelled model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
