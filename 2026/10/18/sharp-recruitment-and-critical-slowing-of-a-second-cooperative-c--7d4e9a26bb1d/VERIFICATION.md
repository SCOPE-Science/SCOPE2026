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

Reconstructed the local argument for the five-dimensional deterministic ODE in RESULT.md, lines 27–77. Pair differences decay exactly. For the upper endemic root, the symmetric first-group block has trace -(1+u)/(1-u) and determinant Delta > 0; its antisymmetric eigenvalue is negative. The absent pair has eigenvalues -1±beta*u. Solving the first two symmetric stationary equations gives c,a=u+O(b²); dividing the last equation by b gives beta*c*(1-b)=1, hence a unique positive local branch with b=u*(beta-1/u)+O((beta-1/u)²). At that branch the last diagonal entry is -beta*c*b and coupling in both directions is O(b), so the small eigenvalue is -b+O(b²). At criticality, writing b for the second-pair mean and eta for its half-difference, b'=beta*(c-u)*b-beta*c*(b²-eta²). To check the physical-side assertion without assuming the sign of a stable-fiber projection, use |eta|≤b and |(log b)'|≤delta in a sufficiently small neighborhood, with delta less than half a first-group exponential decay rate lambda. Stable variation of constants then bounds the first-group displacement by C*exp(-lambda*t)*initial displacement + C*b(t)². Also eta/b decays exponentially. After a fixed short transient the log derivative is bounded above by an integrable exponential minus a positive multiple of b; together with the initial log bound this closes the small-neighborhood bootstrap. The lower bound b(t)≥b(0)*exp(-delta*t) absorbs the exponential in the asymptotic ratios. Thus -b'/b²→1. Dividing the stable forcing convolution by b² gives -J_A^{-1}*((1-u)/u,0), i.e. (1/Delta,(1-u)/(u*Delta)), and therefore the stated coordinate limits. At alpha=9/2 Delta=4. In an isolated triangle stationarity forces all three coordinates equal, so beta<4 excludes a positive stationary state there. For a sunflower every active pair requires lambda*c>1, and an absent pair with that inequality is unstable. These are local deterministic results, not stochastic or global claims. VERIFICATION.md and check.py were inspected and not executed; the independent check is analytic.

## originality

PASS

The exact unequal-strength localized-boundary threshold with the local stability exchange and critical amplitudes is distinct on the material inspected. Group localization and general higher-order SIS dynamics are established; an indexed equal-strength sunflower result also overlaps the support-instability mechanism, not the full unequal-strength conclusion. The pass does not award priority for those ingredients.

## value

PASS

Two overlapping triples are a minimal nontrivial motif for support of one group by another. The exact boundary and measured-coordinate critical amplitudes distinguish a local coexistence mechanism from mere linear invasion and show how the relaxation of the two groups differs. These are informative benchmarks for the stated ODE even though no stochastic, applied or global conclusion follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
