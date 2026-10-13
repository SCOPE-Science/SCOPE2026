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

The proof is analytic for every integer \(n\ge2\). The finite checker is an independent replay of the critical identities, not the basis for extending a finite experiment to all \(n\).

The checker exhausts every permutation through \(n=9\). It verifies the global identity \(\operatorname{Cov}(C_n,\operatorname{Inv}_n)=-(2n-1)/12\), and for every position pair verifies both
\[
\operatorname{Cov}(C_n,I_{a,b})=-\frac{2(b-a)-1}{2n(n-1)}
\]
and the corresponding conditional mean. It separately verifies the two-prescribed-edge completion lemma for every admissible pair of positions and distinct images through \(n=7\).

Observed checker totals are 1,624 partial-completion checks, 240 local conditional-mean/covariance checks, 8 global covariance checks, and 409,112 enumerated permutation states. All arithmetic used for these checks is exact rational arithmetic.

The checker does not test the literature-originality claim, does not establish any higher mixed moment, and does not replace the analytic contraction argument for arbitrary \(n\).
