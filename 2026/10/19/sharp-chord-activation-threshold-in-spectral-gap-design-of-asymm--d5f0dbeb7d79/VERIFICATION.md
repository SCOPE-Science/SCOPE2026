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

The proposed tree weights sum to B and the centered four-level vector f has eigenvalue ell. Grounding the larger hub yields ell singleton blocks and an irreducible right grounded star with a strictly positive ell-eigenvector. Interlacing gives lambda_2>=ell and f gives equality. The quotient ell eigenvalue is simple: the left-leaf equation forces the larger hub coordinate to vanish and the right grounded eigenvector and centering then fix the other coordinates up to scale. The centered PSD certificate ff^T+nu P has trace D and edge costs 1 for spokes and bridge, 0 for right chords and 2nu for left chords. The condition 2nu<=1 is exactly Delta<=0. Equality forces f to be a gap eigenvector, whose equations fix every individual spoke and the bridge; they use the whole budget and force all chords to be zero, even at Delta=0. In particular p=50,q=18 is an exact equality instance, with alpha=5/7 and nu=1/2. With all left chords absent the same dual bound holds for either sign of Delta. For Delta>0 the displayed budget-neutral perturbation strictly raises the left transverse modes and the simple quotient mode, with every other nonzero mode separated initially. This proves improvement and necessity of at least one left chord for every unrestricted optimizer. Existence follows from continuity on the closed budget simplex.

## originality

PASS

The unit-budget fastest-mixing-process SDP and tree-support optimization are prior. The supported distinct theorem is the precise inequality deciding whether the unrestricted asymmetric barbell can improve on its chord-free tree, including unrestricted uniqueness and necessary larger-clique chord activation. The compared exact formulations and support transitions do not imply that threshold.

## value

PASS

The barbell is a natural bottleneck network in budgeted diffusion design. The sharp boundary determines when an exact sparse design is globally optimal over unrestricted edgewise weights and when the larger clique's internal chords are indispensable. This settles a support-design and rigidity question that is not answered by giving the SDP or optimizing a preselected tree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
