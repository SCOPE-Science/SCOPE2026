---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For n≥3 the connected tubes of C_n include n tubes of every proper size 1..n−1 and one full tube, so W_n=Σ_T Δ_T lies in Σx_i=n(n−1)+1. A proper k-tube is a path; exactly k(k+1)/2 sub-tubes lie inside, hence its facet is x(S)=k(k+1)/2. Intrinsic normal in 1^⊥ is 1_S−(k/n)1, squared norm k(n−k)/n, and cyclic symmetry forces vertex barycenter b=(n−1+1/n)1. Its distance to a k-tube facet is [k(n−1+1/n)−k(k+1)/2]/sqrt(k(n−k)/n). Symbolic expansion and fresh exact Fraction replay n=3..200 verify the submitted identity d_k²−d_1²= (k−1)[n(n−k)²+(2n²−7n+4)(n−k)+(n−2)²(n−1)]/[4(n−k)], which is strictly positive for all k≥2 because every bracket contribution is positive/nonnegative for n≥3. The n singleton inequalities x_i≥1 sum to a sharp inradius upper bound r=(n−1)^(3/2)/sqrt(n); equality forces every center coordinate b_i, proving uniqueness and only singleton-facet tangencies. Finite checks corroborate the all-n proof, not the reverse.

## originality

PASS

Padrol–Pilaud–Poullot supply the standard graph-associahedron simplex-sum construction and tube facets, not a metric largest-ball theorem; Hohlweg–Lange emphasize other geometric realizations. Independently opened a published clock-quasi-metric cyclohedral inradius theorem: it treats zero-mean Lipschitz inequalities x_i−x_j≤rho(i,j), with a DIFFERENT Euclidean radius (n−1)²/(n sqrt2), whereas the assigned cyclic tube simplex sum has x(S)≥k(k+1)/2 and radius (n−1)^(3/2)/sqrt n. The published Loday path associahedron and binary-laminar fertilitopes likewise concern different facet systems and hypotheses. No prior result mathematically implies the assigned exact standard-cycle radius and singleton-only contact. Older unpublished metric observations remain possible.

## value

PASS

The exact Euclidean inradius, unique incenter, and complete contact shell of the standard unit simplex-sum cyclohedron are geometric invariants of a canonical naturally occurring realization, not arbitrary numeric coefficients. Derives an all-n non-obvious strict facet-distance ordering and contrasts with nonisometric classical cyclohedron models; geometric optimizers can use the precise radius and unique-center result independently.

The dated certificate retains the supplied scientific assessment, sources and limitations.
