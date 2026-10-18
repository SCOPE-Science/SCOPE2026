---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For complex m>=3 and any partition lambda=(d_i) with at least two parts, the finite multiplication map from product P(Sym^{d_i}V*) has pullback O(1,...,1) and generic degree prod_e(mu_e!), since generic factors are irreducible and their only ambiguity is permutation among equal degrees. Its source dimension D=sum_i[binom(m+d_i-1,m-1)-1], and the top intersection coefficient is D!/prod_i N_i!, so dividing by the generic degree proves the complete formula. The top-dimensional component for the full reducible locus is (d-1,1), as in Catalisano et al.; d=2 requires degree-two symmetry, d>=3 no symmetry. Independent integer checks reproduced projective degrees (m,d)=(3,2):3,(4,2):10,(3,3):21,(4,3):220,(3,4):55. No extension to binary forms, Chow rings or secant degrees is claimed.

## originality

PASS

Best-of-knowledge PASS: the 2021 Catalisano et al. Section 9 explicitly poses the degree of reducible-hypersurface varieties beyond plane curves as an unavailable generalization and gives the finite multiplication parametrization. The present closed formula addresses all partitions by a generic-fiber quotient and top intersection. Previously known split forms and plane-curve instances are special cases rather than new claims; no checked stronger source supplies the all-partition formula. Because the derivation is short from classical intersection theory, unindexed folklore and post-2021 work are retained risks, not treated as disproved by negative search.

## value

PASS

PASS: Projective degree is a natural enumerative invariant of each irreducible factorization-type locus, and the initiating geometry paper explicitly identifies its unknown generalization as a natural gap. The all-partition closed form and the degree of the full reducible-hypersurface locus are reusable exact invariants beyond isolated numerical special cases despite their concise proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
