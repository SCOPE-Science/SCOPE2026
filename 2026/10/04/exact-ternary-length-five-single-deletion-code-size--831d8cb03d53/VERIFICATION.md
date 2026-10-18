---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For each ternary five-word x, D1(x) is the SET of its distinct length-four subsequences by one deletion. The explicit 24 codewords have pairwise disjoint D1 shadows, giving lower bound 24. The pinned verify.py gives 81 positive integer weights c_z with sum 348, scale 14; independently reconstructed all 243 input deletion shadows and checked min_x sum_{z in D1(x)}c_z =14, and verified disjointness of the 24 source witnesses (using 78 distinct output words). Any code then satisfies 14|C|≤348; integer |C|≤24. Finite enumeration exhausts the exact 3^5 domain, not a partial sample. This establishes N(5,3,1)=24.

## originality

PASS

Kulkarni–Kiyavash arXiv:1211.3128 Table I(b) gives q=3,n=5 fractional rounded upper bound 24 but best listed construction size 17, so the exact equality and code of size 24 are not prior claims. Full licensed eight-page Li–Houghten CIT 2012 primary text newly read: Table IV gives ternary Tenengolts size 17 at n=5 and examines extensions, without proving N(5,3,1)=24. Neighbor Resultary ternary n4 and quinary n4 optimum or ternary n5 covering numbers are distinct. Residual earlier unindexed specialized code constructions remain possible.

## value

PASS

Exact natural ternary length-5 one-deletion optimum closes a specific documented seven-codeword construction gap (17 to 24) against the existing rounded fractional upper bound. The constructive primal witness plus independently checkable exact dual is useful as a small synchronization-code benchmark, even without a general family or census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
