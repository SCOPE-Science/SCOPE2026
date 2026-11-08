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

The prime-product upper bounds force p,q,r=(3,5,7),(3,5,11),(3,5,13). Coordinatewise monotonicity of prime-power sigma indices and exact rational boundary comparisons yield precisely eight minimal abundant exponent triples. Independently constructed the distinct-divisor bitset (start 1; for each d, B|=B<<d) for each actual eight bases and verified every sum in the inclusive [23,sigma-23] and the sharp missing 22 at n=7425; this is exhaustive for those finite bases, not merely sampled. Verified the two-prime cofactor monotonicity of Delta(d)=2d-sigma(d) by its exponent-increment formula. The interval-extension lemma adds each new p^{a+1}d in order and proves overlap under sigma(pN)-2pN>=45; monotone minimal abundance >=26 gives this at every extension. Consequently the claim covers the unbounded exponents. The proper-divisor complement proves semiperfectness; parity of sigma is equivalent to an equal-sum divisor partition (Zumkeller) in this class.

## originality

PASS

Best-of-knowledge PASS for the exact universal central subset-sum interval and optimal endpoint. The eight primitive abundance threshold numbers are known, but arithmetic tables do not imply the claimed coverage for all exponents. Jokar’s almost-practical results specialize to prime support 3,5,7 and do not cover the r=11/13 sharp family. Fang examines finite odd-weird searches rather than this unbounded central interval.

## value

PASS

The uniform best central interval is a mathematically natural stronger invariant than mere semiperfectness for the infinite odd-three-prime abundant family; the sharp 7425 obstruction and exact endpoint 23 are informative. The threshold/base decomposition plus rigorous propagation solves an infinite question, not a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
