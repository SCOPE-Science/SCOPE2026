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

The positive-coordinate upper and lower bounds follow from the convex combination minus the square, with 1-ε-x>0 and its counterpart. Direct expansion gives u'=u-u²-d², d'=(λ-2u)d. Here |d|<u, including d=0 after a finite hit; the strict lower inequality for |d| in the proof's first paragraph need not be used. The mean decreases to zero, and the reciprocal increment for w=1/u is (1+t²)/(1-(1+t²)/w), t=d/u, hence w grows between two linear bounds. At positive coupling the transverse multiplier is uniformly bounded in magnitude by a fixed number <1, so t_n² decays exponentially times at most a quadratic factor. Then Δw=1+1/w+O(w^-2+t²) gives w=n+O(log n); subtracting the increments of n+log n yields a summable error with tail O(log n/n), proving the existence and required precision of C. The interior case has a vanishing difference precisely when its factor first vanishes, and otherwise positive eventual factors with log correction -2u/λ and summable O(u²); this yields the nonzero λ^n n^(-2/λ) amplitude. At maximal coupling the product is exactly |d_0|2^n times ∏u_j; the nonzero factors have negative sign before taking magnitude. Separating u_0 and extracting 1/j for j≥1 gives 1/Γ(n), with log(ju_j)=-(log j+C)/j plus an absolutely summable remainder. The discrete sums minus the integrals converge since their interval errors are summable, giving both -(log n)^2/2 and -C log n and a strictly positive residual amplitude. At zero coupling the reciprocal differences are multiplied by factors in (0,1) whose deficits are O(n^-2), proving a nonzero limit and the n^-2 coordinate gap. This verifies the fixed-parameter claims, including extinction and nu_n→1 in all regimes.

## originality

PASS

The recurrence, scalar parabolic iteration, and generic contraction/product ideas are not claimed as new. The material result is the explicitly normalized fixed-coupling trichotomy on the displayed invariant square, in particular the nonzero factorial endpoint with its logarithmic-square factor and orbit-dependent exponent. The inspected alternative models and analytic background do not cover that theorem. Possible exact-map precedents remain an access risk; this is a best-of-knowledge judgment.

## value

PASS

At the extinction threshold the diagonal itself relaxes only parabolically, whereas changing the transverse multiplier generates qualitatively different synchronization rates. The endpoint calculation distinguishes zero derivative and a rough factorial scale from a sharp law: a small longitudinal log correction accumulates in the product into a universal log-square term, so a pure factorial fit fails even up to a power. The interior finite-hit exception, preserved rather than hidden in a zero amplitude, matters to a classification for every distinct positive pair in the specified square.

The dated certificate retains the supplied scientific assessment, sources and limitations.
