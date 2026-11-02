---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Independently reconstructed the four pair-vs-cycle overlap types under row-wise hypergeometric sampling without replacement: outside/outside zero; exactly one shared vertex contributes ℓ(n−ℓ)p^ℓ(q−p²); nonconsecutive inside pair contributes ℓ(ℓ−3)p^(ℓ−2)(q²−p⁴)/2; adjacent inside contributes ℓ(p^(ℓ−1)q−p^(ℓ+2)). Here p=k/(n−1), q=k(k−1)/((n−1)(n−2)), distinct rows independent. Summing over (n)_ℓ/ℓ oriented cyclic words yields exact Cov(C2,Cℓ)=−(n)_ℓ k^ℓ(n−k−1)²(2n−ℓ−1)/[2(n−1)^(ℓ+2)(n−2)²]. Fresh rational arithmetic verified all 440 n,k,ℓ strata for 3≤n≤12, 1≤k<n, 3≤ℓ≤n. Positivity of 2n−ℓ−1 proves strictly negative when k≤n−2 and zero for k=n−1. ER shared-arc argument gives (n)_ℓ p^(ℓ+1)(1−p)>0. Fixed-k and dense limits follow algebraically; no asymptotic claim for variable ℓ.

## originality

PASS

PASS (qualified): The published random K-out and automaton analyses inspected focus on undirected connectivity or repeated-neighbor/random-mapping cycles, not this uniformly without-replacement oriented pair-vs-every-ℓ covariance. The four-pattern derivation could be implicit in a more general enumeration for binary contingency tables or random fixed-row digraphs; exact priority remains open.

## value

PASS

PASS: The model is a standard fixed-outdegree analogue of directed Erdős--Rényi. Exact all-length negative reciprocal/long-cycle covariance, its strict finite-size range including Hamiltonian cycles, and opposite sign in independent-arc sampling at equal expected degree yield a substantive structural dependence distinction, not just a small-sample sign test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
