---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: The full one-block zip map Fτ on Z^{negative}×S^{nonnegative} is onto with pointwise inverse degree δ(x)=|τ^-1(x_{-1})|=d_{x_-1}, a topological-conjugacy invariant by bijection of inverse fibers. Exactly |S| fixed points are indexed by constant forward symbol s and have degree d_{τ(s)}; hence Iτ(v)=Σ_z d_z v^{d_z}. Its coefficient at v^d divided by d recovers the number of target fibers of size d. Equal multisets permit explicit bijections α:S→S′ and β:Z→Z′ with ρ∘α=β∘τ, giving coordinatewise conjugacy of the full zip systems. Thus conjugacy classes at |S|=N are partitions of N. Periodic words w∈S^n yield exactly N^n fixed points; degree-weighted sums factor as (Σ_z d_z^{r+1})^n, giving rational ζ_{τ,r}. The projection from full bilateral S-shift proves natural extension and entropy logN. Independently enumerated all finite surjections with 1≤N≤5 and recovered 1,2,3,5,7 distinct inverse-degree polynomials, equal to partition counts; bounded checks are not the all-N proof.

## originality

PASS

PASS (qualified): intrinsic fixed-point inverse-degree polynomial as a COMPLETE conjugacy invariant over all full one-block zip systems, with p(N) class count, is stronger than prior examples separating uniform inverse degrees and general zip-shift constructions. General finite-to-one local homeomorphism classification might imply it, which remains a residual risk.

## value

PASS

PASS: Topological classification of a natural noninvertible shift family is a substantive exact structural result. The degree polynomial distinguishes systems with identical entropy, ordinary periodic counts and natural extensions; the p(N) census and rational refined zetas make the distinction explicit and reusable. It is not an arbitrary finite sample or a relabeling-only invariant: the inverse-degree argument rules out all non-block-code conjugacies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
