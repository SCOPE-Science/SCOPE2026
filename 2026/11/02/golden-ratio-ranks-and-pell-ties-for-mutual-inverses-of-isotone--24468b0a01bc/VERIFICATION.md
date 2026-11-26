---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Re-audited the narrowed RESULT.md in repairs/4. The known pair weight is valid: the two inverse restrictions pair the ordered images with the opposite kernel intervals; each one-sided marked-kernel count has generating function z^r/(1−z)^{2r}. The first-moment identity in the earlier record gives the same squared weight on multiplication by the number of rank-r maps, and rank one is n² by direct counting. The consecutive square-root weight ratio is (n²−r²)/(2r(2r+1)), crossing one at τ_n, with the single rank at n=1 handled separately. A tie requires norm-one Pell equation (5r+1)²−5n²=1, and the unit 9+4√5 has constant part −1 mod 5; exactly its even powers qualify. At the first even power n=72 and r=32. The uniform interior Stirling prefactor for the squared weight is x/[πn(1−x²)]; the unique saddle is x*=1/√5 with 2h(x*)=4 log φ and (2h)″(x*)=−5√5. The repair bounds endpoints by binomial entropy and intermediate tails by Gaussian domination, justifying the lattice normalization and weak convergence. The cubic error on |r−nx*|≤a_n=o(n^{2/3}) is O(a_n³/n²)=o(1), giving a uniform relative local law after normalization. Both total and product-measure probability constants follow; in particular dividing by |O_n|² multiplies the total by 4πn/16^n asymptotically.

## originality

PASS

The frozen treatment of the ordered finite pair count as a new part of the contribution fails originality: the earlier inverse-degree moment formula implies it, and a distinct same-day record states it outright. The repaired finding credits it and the exact sum as known inputs; the accepted distinction is the classification of ties for the most likely rank of a uniformly drawn valid pair and the sharp normalization/local and global fluctuation laws for that rank. No matching Pell classification or relative local law was found in the inspected comparisons. The residual priority judgment is bounded, especially for applications of the equivalent classical triangle.

## value

PASS

The repaired result answers the distributional question for a natural edge-weighted sample of the inverse relation rather than a fixed-rank vertex sample. It locates all rank ties, including a sparse nontrivial Pell family, quantifies concentration down to individual ranks in a moderate window, and computes the exponential rarity and its prefactor under independent sampling. These two analyses explain finite-size modes and fluctuations that the known enumeration alone does not describe. The ordinary idempotent count and exact sum are useful inputs, not claimed advances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
