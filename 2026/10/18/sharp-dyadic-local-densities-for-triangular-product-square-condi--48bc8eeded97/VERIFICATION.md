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

For even a=2b, T(a)=b(2b+1); differences factor as (b-c)(2(b+c)+1), making the map of b bijective on every residue ring and hence Haar-preserving. The odd class is identified with the even class by a↦-1-a, which preserves T. Condition on the valuation j of U=T(a), of mass 2^(-j-1). Then UV is uniform on 2^j Z_2, since V=T(b) is independent Haar and the unit of U is invertible. For n=2^h u and j<=h, the translated law is still Haar on 2^j Z_2, so the conditional square probability is 1/6 for even j and 1/12 for odd j by even valuation and odd unit 1 mod 8. At n=0 this sums over all j to 5/36. For odd h, j>h brings no squares and the truncated sum is (5/36)(1-2^(-h-1)). For even h the sum through h is 5/36-2^-h/18; for j=h+1,h+2, and j>=h+3 the conditional square probabilities are 1/4, (1/2)1_{u=1 mod 4}, and 1_{u=1 mod 8}, respectively. Their weighted additions are 2^-h times 1/16, 1_{u=1 mod 4}/16, and 1_{u=1 mod 8}/8. This gives exactly the stated c(u), with no change for negative n. Zero is null. The odd branch is minimized only at h=1; in the even branch the positive correction is largest only for h=0 and u=1 mod 8. Independent modular counting at 2^10 gave 299/2048,171/512,27/256,75/512,107/512 for n=0,1,2,3,5; these upper approximations count congruence squares, not necessarily actual 2-adic squares. The analytic disintegration, not the truncation, establishes the exact formula.

## originality

PASS

The distinct result is the complete parameter-dependent projected mass and both sharp equality classes for a fixed additive shift, equivalently for the product of two Haar integers. The triangular uniformity reduction is known in indexed work, and dyadic solvability in the same equation is known. Those overlaps are not new contributions; neither determines the square probability, its valuation and unit dependence, or its extremizers. Relevant available primary passages and the closest indexed results were checked; no matching full density theorem or exact table was found in those sources.

## value

PASS

A natural projected local mass sharpens the existing yes/no congruence result. It quantifies uniformly how prevalent admissible pairs are under the index Haar law, and distinguishes shifts with identical local solubility but different valuation/unit biases. The exact parameter classification and sharp attained bounds give useful information for dyadic local calculations, rather than an isolated residue example or a claimed theorem about ordinary integer density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
