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

A unit response using a remote coordinate has limiting c₀ distance equal to max(a(s),a(t)); c₀ vanishing makes this simultaneous for any fixed finite source list. For the reverse bound use source pairs (s,±a(s)e₁). With b the absolute first response coordinate and c the tail supremum, the branch distances are the values of the convex nondecreasing function r↦√((s−t)²+max(r,c)²) at |a(s)−b| and a(s)+b; Jensen and their mean max(a(s),b) give exactly the claimed kernel as a lower bound. A response on e₂ realizes it for these pairs. Equal-weight empirical measures are dense, and continuity is uniform against the compact response set, yielding the attained maximum over measures. Reflection and concavity justify symmetric sources; the resulting response is even. In each variable of K, on either side of the max-switch the normed vector has speed at most one, so the summands are separately 1-Lipschitz, including at zero norm by the reverse triangle inequality. The mesh error is π/(4N), not twice that: rounding a continuous source to the grid bounds one direction; allowing continuous replies against the optimized grid source bounds the other. For thinness a fresh eₙ gives the upper bound and the two scalar poles give the lower bound. For μ₁, averaging replies 0 and 1 yields the strict upper bound by compactness (the two summands cannot attain √2 at the same source radius). For the half-zero/half-poles source, its response function is strictly concave in q=√(1−t²), with equal endpoints. The ±1/√2 perturbation strictly improves both endpoints; continuity gives endpoint neighborhoods and a compact interior gap that persist for a suitably small mixture weight.

## originality

PASS

The index definition, general possibility of μ₁<t, and related mixed-sum thinness results are prior. The supported distinct claim is the sharp scalar kernel and actual equality of the lower average-distance game for this mixed sum, with its certified finite computation and space-specific strict bounds. None of the inspected comparisons implies that equality.

## value

PASS

The lower index is a natural Banach-space invariant that cannot be read off from thinness. Reducing the infinite-dimensional problem to a single scalar coordinate with matching adversaries gives an exact object usable for optimization, and the uniform finite-LP error makes it computable to a requested precision. The proof identifies a strict mean-versus-worst-case separation in this elementary mixed space rather than merely computing an arbitrary grid example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
