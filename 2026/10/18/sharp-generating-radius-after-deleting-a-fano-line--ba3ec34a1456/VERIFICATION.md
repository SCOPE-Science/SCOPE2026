---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

At cube vertices each positive convex row attains norm exactly on monochromatic triples, so the norming-face convex hull K is independent of weights. Dual support formula h_K(a)=1-2 min_e min(P_e,N_e) for ||a||1=1. Every six-line proper 2-colouring has 3 base vertices of one colour with zero or one same-colour leaf, checked by all 128 sign vectors independently for each of seven deleted lines (ten proper colourings each). In the zero-leaf case min masses force 3d base+2d leaf ≤1; one-leaf case 6d≤1. Explicit normalized a=(1/5,1/5,1/5,-1/10,-1/10,-1/10,-1/10) saturates d=1/5 and yields radius 1-2/5=3/5. Restore seventh line => all 128 sign vertices norm attaining => radius 1. This is exact finite exhaustive hypergraph argument plus continuous LP support bound, not sampling of arbitrary coefficients.

## originality

PASS

Compared exact hypotheses, invariants, reductions, implicit prior implications, and relevant primary theorem/proof sections. None of the inspected cited primary results implies this final precise statement under its hypotheses; originality is best-of-knowledge only, with named residual risks.

## value

PASS

Quantifies the exact stability loss from deleting one hyperedge in a canonical minimally non-two-colourable incidence structure, yielding a genuinely sharp positive-contraction generating invariant independent of all strictly positive stochastic row weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
