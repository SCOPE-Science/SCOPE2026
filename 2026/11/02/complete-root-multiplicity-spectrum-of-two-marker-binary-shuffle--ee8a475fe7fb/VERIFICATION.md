---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For each W=0^a1 0^b1 0^c with a+b+c=2n−2, a root has exactly one 1: 0^u1 0^(n−1−u). Assign the ordered markers to two identical copies and count zeros before, between and after them. The iff conditions produce L=max(ceil(a/2),n−1−c) and U=min(a,floor((a+b)/2)), so R(W)=max(0,U−L+1). If R≥r, all three gaps have at least 2(r−1) zeros; removing those changes L by r−1 and U by 2(r−1), and creates a bijection to words with ≥1 root at half-length n−3(r−1). Counting r=1 by forbidden separation and adjacent-ones parity gives H(m)=1+3m(m−1)/2. Difference of tails and maximal r follow. Independent length-by-length dynamic-programming interleavings and histograms (n≤9) agree; finite tests are cross-checks, not infinite proof.

## originality

PASS

Best-of-knowledge original contribution is the exact statement in Complete root-multiplicity spectrum of two-marker binary shuffle squares; previously established general mechanisms/base results are credited. Actual fresh semantic query and primary-text comparisons found no implication covering the precise result. This is qualified historical priority, not proof of absolute novelty.

## value

PASS

The fixed-two-marker layer is a natural minimal nontrivial slice of the shuffle-square problem and was already studied for membership. The exact inverse-degree histogram of all distinct roots is not determined by either membership or counts of outputs from each root; it resolves a precise combinatorial multiplicity question at all n and gives a nontrivial three-gap contraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
