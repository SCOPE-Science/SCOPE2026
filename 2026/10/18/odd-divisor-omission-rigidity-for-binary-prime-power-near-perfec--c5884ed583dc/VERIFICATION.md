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

For n=2^k p^e, k≥1,e≥2,p odd prime, factor σ(n)−2n = (2^{k+1}−p)Q−1 with Q=1+p+⋯+p^{e−1}. Writing arbitrary odd omitted set T as selected powers p^j (0≤j≤e), use p^e≡1 (mod Q). Let r be number selected from endpoint j∈{0,e} and R=1+r+Σ_{1≤j≤e−1, selected}p^j. Equation forces Q|R, while 1≤R≤Q+2<2Q as p≥3 and Q≥4; thus R=Q. Reduction mod p gives r≡0 mod p with 0≤r≤2<p, hence r=0. Positivity forces every internal power selected and neither endpoint. Substitution in the exact identity gives p=2^{k+1}−1; converse holds for every e, including e=2. This simultaneously proves quantified uniqueness among ALL subsets of odd divisors, not among even-divisor omissions. A fresh separate brute-force test checked 20,832 candidate subsets for k=1..6, odd primes p≤47, e=2..6, yielding precisely 15 predicted matching cases; the argument, not the finite box, proves the infinite statement.

## originality

PASS

Known two-deletion Mersenne cases e=2 and e=3 are credited to published 2-near-perfect classification. The claim quantifies over arbitrary-size sets consisting entirely of odd divisors and every e≥2; for e≥4 it gives a unique e−1-member set and hence an unbounded-cardinality family at fixed prime support. Best-of-knowledge priority remains conditional on uninspected 2016 Adajar thesis and alternate multi-omission terminology.

## value

PASS

For the standard near-perfect-number sum-of-divisors problem, omission number and parity are intrinsic arithmetical stratifiers. On natural minimal two-prime-support numbers the theorem determines the ENTIRE odd-only omitted-subset spectrum and shows its unique structure for every e, including unbounded cardinality e−1 for each fixed Mersenne prime. This exact set classification closes a meaningful gap left by two-omission results and is neither a small sample nor simply their numerical recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
