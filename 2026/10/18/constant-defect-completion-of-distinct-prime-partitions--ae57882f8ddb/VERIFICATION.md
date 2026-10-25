---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For k the largest number of initial distinct primes with sum ≤n, choose j=k−t with t∈{4,5} of parity n. Then R=n−S_j is sufficiently large odd with R∼t p_j. The Matomäki–Maynard–Shao residue-uniform almost-equal ternary-prime proof can assign admissible three different classes mod 7 for every R mod 7, guaranteeing three DISTINCT q_i=(R/3)+O(R^θ)>p_j for θ∈(11/20,1). Appending these q_i to the first j primes gives k−1 or k−2 exact summands, proving 0≤k−L≤2. If n≡k mod 2, a k-part representation cannot contain prime 2 and its minimum sum is S_{k+1}−2; parity and n<S_{k+1} show iff exactly that endpoint. The published bounded-sum primorial envelope P_k≤H≤P_{k+1} and the constructed exact product ≥P_j give H/M≤p_{k+1}^6≤(2n)^6. PNT and AM–GM then show K/k→1 and log M∼√(n log n). Fresh dynamic programming checked representative n=301..1500 parity cases; finite checks do not establish the sufficiently-large threshold.

## originality

PASS

The near-equal ternary Goldbach proof, primorial bounded-sum envelope and Campbell discrepancy are compared by their actual implications: none asserts a two-part deficit to the initial-prime packing bound plus exact-product completion and parity classification. Distinct admissible residues mod7, used through the source uniform residue argument, are the critical added step.

## value

PASS

Distinct-prime additive partitions and prime-product maximization are classical extremal questions. Constant loss of at most two parts for ALL sufficiently large integers, a parity-branch exact criterion and a polynomial multiplicative exact-sum completion bound are substantive quantitative bridges between different natural extremal objectives; neither follows from routine PNT estimates alone, requiring a deep almost-equal primes construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
