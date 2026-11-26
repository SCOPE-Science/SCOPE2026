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

The positive-real representation is onto: the exponential of the holomorphic primitive reconstructs a normalized f with nowhere-zero f′, and the tilted real part equals cos β times Re p. Expanding that exponential through order three gives the exact determinant in (1), with perturbation coefficients +1/144 for τ c₁²c₂ and −1/144 for τ²c₁⁴ after removal of τ². The Herglotz and two Schur steps exhaust the moments, including |y|=1 and x=0 or 1. For fixed t=x² and r=|y| the remaining Schur parameter can be aligned with the complex quadratic. I checked the resulting concave quadratic in cos θ, its maximizing cosine and the signs of the two exterior branches. As r increases the cosine vertex decreases; the interior and last branches are nondecreasing in r, while the first is at most 2. To certify that cap I independently converted h(x)=2−3x−2x²+3x³+x⁴ to Bernstein degree 10 using q_k=Σ_{i=0}^{min(k,4)}[x^i]h·binom(k,i)/binom(10,i); all eleven fractions match the printed positive certificate. At r=1 the transition solves 4t²+5t−2=0; the first envelope 2+t−4t² peaks at t=1/8, and the matching second envelope decreases. The explicit degree-two Blaschke choice realizes the negative value −33/16. Division by 18 gives 11/96, and |c_j|≤2 gives the uniform normalized perturbation c/18+c²/9. The same explicit choice gives the lower bound by the reverse triangle inequality, so the sidedness of β does not change the limit.

## originality

PASS

The Carathéodory, Herglotz and Schur reductions are classical. The supported distinct result is the exact moment supremum with this coefficient ratio, and hence the sharp grazing coefficient and a two-sided error bound in the stated planar class. The closest prior indexed record has the identical class and functional but a different limiting regime. Do not treat the quoted 17/144 coefficient as a valid sharp or uniformly established benchmark: it is a coefficient of the stated prior bound, for which the small-angle record reports a counterexample away from the grazing regime.

## value

PASS

The degeneration of this existing analytic class at cos β→0 makes the attainable leading coefficient, not just an upper bound, the relevant comparison. An exact nontrivial optimization over all realizable three-moment data supplies that coefficient, an explicit realizable extremizing family for the asymptotic, and a uniform quantitative error. Finite-angle estimates and low-angle expansions cannot substitute for these conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
