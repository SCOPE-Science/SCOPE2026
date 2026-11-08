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

For finite trees with exactly m>=2 original leaves and all unordered distinct leaf-pair geodesics as vertex-subset concepts, the trivial Ldim <= floor(log2 binom(m,2)) is correct and query responses are vertex-membership. Every depth-five shattering tree on m=9 must begin with >=16 positive and negative hypotheses; enumerating all integer partitions of nine leaves gives only (3,6),(4,5),(1,2,6). The (3,6) cross-path positive version space factors as two rooted leaf-path concept classes on disjoint sides, giving Ldim<=floor(log2 3)+floor(log2 6)=3. The other two partitions force a 16-concept negative branch and an 8+8 second split; the resulting six 4-leaf pair paths plus two disjoint singleton paths cannot split 4+4 into two depth-two branches (eight-hypothesis lemma), so depth five is impossible for ANY subdivided nine-leaf tree. I independently retrieved and parsed the complete certificates.json from the exact Git blob, reconstructed every witness path and branch decision, and confirmed 0 violations, full distinct witnesses for depths 0..5 and 32 distinct witnesses for m=10. Combining certificates and universal bounds gives U(2..10)=(0,1,2,3,3,4,4,4,5). The three-point path Helly-style incidence obstruction and four leaf choices establish VC=0/1/2 for m=2/3/>=4. The proof makes no unjustified infinite-size inference from finite certificates.

## originality

PASS

Qualified acceptance for the first unattainable entropy ceiling at nine leaves in the fixed-host tree leaf-pair path incidence class; standard general Littlestone results and one-endpoint rooted-path results are prior work.

## value

PASS

The 9-leaf obstruction is a sharp, universal first failure of the information-theoretic hypothesis-count bound for a geometrically natural online-learning class; the bound becomes attainable again at ten. The mathematical reason is a three-partition first-query bottleneck and an eight-hypothesis path lemma, not a brute-force scan of arbitrarily many finite trees. This first cutoff and accompanying VC separation form a useful self-contained structural benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
