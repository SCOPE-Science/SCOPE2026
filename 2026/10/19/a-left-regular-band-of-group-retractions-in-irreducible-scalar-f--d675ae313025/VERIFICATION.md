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

Verified the classification directly. The unique Sylow p-subgroup V receives the image of V under any endomorphism, since all images of its elements are p-elements. The kernel of the restriction is stable under α and is an F_p-subspace. The minimal polynomial of α has degree ord_m(p)=d, hence F_p[α]=F_q and that restriction has zero kernel or is zero. For an idempotent with zero kernel on V, the restriction is the identity. Conjugating each v∈V by the image of (0,α) now gives the same scalar α, so the induced map on the quotient is the identity by faithfulness. The whole map is then injective and idempotent, hence the identity. Every other endomorphism under consideration kills V and factors through C_m. If (0,α) maps to (w,α^a) with a=0, its order divides m and p, so w=0. For a≠0 the affine power law gives translation label t=w/(1−α^a) and F(v,α^j)=(t(1−α^(ja)), α^(ja)). Composing retains the left translation and multiplies the quotient exponents. The idempotent condition is exactly a²=a modulo m, so the CRT residues are precisely those stated; nonempty support yields q distinct maps, and support intersection gives closure and FGF=FG. The quotient power image has order m_S and its translation conjugation preserves this order. For |S|=s there are 2^(r−s)−1 nonempty disjoint supports allowing all q labels and 2^r−2^(r−s) intersecting supports allowing exactly one label, plus the two universal maps. For ordered support pairs, 3^r assignments avoid intersection before removing empty supports, leaving 3^r−2^(r+1)+1 nonempty disjoint pairs and 4^r−3^r intersecting pairs. Adding 4+4q(2^r−1) ordered pairs involving a universal map verifies the census and its r=1,2 reductions. This is the centralizer within the band only. The frozen script and its finite checks were inspected, not executed; the conclusion uses the all-parameter proof.

## originality

PASS

The supported distinct claim is the entire idempotent endomorphism band for arbitrary irreducible faithful scalar complements, including proper complements over nonprime fields, with joint composition, image and commutation invariants. Exact matches in the full affine and prime-kernel subfamilies are credited as overlaps. The inspected broader automorphism theorem concerns only units, and the retract criterion does not supply the classification or explicit multiplication for arbitrary proper scalar complements.

## value

PASS

Retractions need not form a subsemigroup in general. A complete multiplication for this natural Frobenius family describes when closure and left regularity occur here, and separates the band isomorphism type (q and the number of complement primes) from the embedding-sensitive image orders (full prime-power sizes). The support description gives exact commutation data uniformly, including proper irreducible complements outside the two comparatively well-described subfamilies. The numerical census is useful as a consequence of this structure rather than an isolated CRT exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
