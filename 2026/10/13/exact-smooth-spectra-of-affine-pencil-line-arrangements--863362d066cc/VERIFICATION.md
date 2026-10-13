---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The definitions were checked against arXiv:2609.38103v1. For an affine pencil \(P_n\), there is one singular point, so if \(g_i\) are the meridian images and \(S=\sum_i g_i\), the entire anti-admissibility condition is that the \(g_i\) span and every pair \(\{g_i,S\}\) is linearly independent.

For \(k=2\) and \(p=2\), the three nonzero vectors are \(a,b,a+b\). Independence from \(S\) forces the used vectors to be the other two directions. The total sum is independent from both exactly when both multiplicities are odd, hence exactly when \(n\) is even.

For \(k=2\) and \(p\ge3\), choose \(r=1\) unless \(n\equiv1\pmod p\), in which case choose \(r=2\). Mapping \(r\) meridians to \(e_1\) and the rest to \(e_2\) gives a total sum with both coordinates nonzero.

For \(k\ge3\), map the first \(k\) meridians to the standard basis and all remaining meridians to \(e_1\). The total sum has \(e_2\)- and \(e_3\)-coordinates equal to \(1\), so it is not collinear with any meridian image.

A finite stress test checked these formulas for \(2\le n\le14\), all admissible ranks, and primes \(2,3,5,7,11\). This test is corroborative only; the proof above is uniform.

Limits checked: projective pencils, non-elementary-abelian targets, and general supersolvable arrangements are outside the claim.
