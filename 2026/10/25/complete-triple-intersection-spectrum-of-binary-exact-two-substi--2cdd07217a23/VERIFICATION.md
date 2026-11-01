---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The exact-two condition forces all pairwise center distances to be positive even and <=4, yielding exactly eight coordinate profiles after XOR normalization. For three centers with disagreement sizes (a,b,c) and A common-zero positions, the linear constraints i+j+l+r=2, j+r=(a+c)/2 and l+r=(b+c)/2 give J=n-2,4,3,1 in the four profile classes. Multinomial counts summed over all first centers and divided by six produce precisely 2^n*[C(n,3),3C(n,4),10C(n,5),15C(n,6)] unordered triples; coincident exponents combine. For n=3 maximum one, n=4,5 maximum four, n=6 tie at four, n>=7 maximum n-2. Exactly max J distinct outputs can leave three candidates, so max J+1 threshold sharp. Positive mass ~n^6/(8*4^n). Independent brute-force n=3..6 enumerated all triples from actual sphere masks, reproducing histograms (n=6 positive J counts 960,3840,4160 at J=1,3,4). Finite checks are not the all-n proof.

## originality

PASS

Best-of-knowledge novelty of the whole unordered-center population polynomial, not of per-triple Hamming sphere/ball intersection methods. General q-ary per-instance formulas and fixed-distance extremizers predate the record, but do not by themselves count the number of all center triples with each J-value. An older sphere classification or newer v2 specialization may cover it.

## value

PASS

Exact-two binary substitutions are a natural reconstruction model; the full all-n distribution of three-center ambiguity, not just its maximum, gives both sharp two-list read threshold and exponentially small frequency of ambiguous center triples. The four populations are an exact natural classification; no coding-rate claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
