---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Necessary σ(n)>=2n rules out ≤4 distinct odd primes because the maximal abundance at 3,5,7,11 is 2304/1155<2. For 5 prime factors, monotone abundance forces 3,5,7,s,t with s in {11,13,17,19}; σ=192(s+1)(t+1), so t<=floor[192(s+1)/(18s-192)], namely 384,64,30,25. Exactly 71+12+3+1=87 prime t cases. Since n=105st is squarefree, its 16 complementary pairs correspond to divisors d|105s, with weights d+(105s/d)t. A complement-closed selection sums to 2n iff these weights have a subset sum 2n. Independently re-enumerated all 87 and rejected exact subset sums using a fresh meet-in-middle implementation over directly enumerated complementary divisors; this exhausts all 5-prime candidates *because of the unbounded abundance reduction*, not an arbitrary cutoff. For n=937365 direct products and omitted pair sum 60630, σ=1935360, yield retained sum 2n. The six-prime witness is explicitly prior.

## originality

PASS

Wang–Zelinsky 2026 full 17-page primary paper explicitly records odd squarefree 937365 and surveys restrictions, plus tables of odd examples; it does not state a universal exclusion of all odd squarefree five-prime numbers in the read theorem/table sections. Prior Resultary exact theorem Ω(n)<=3 is weaker and different. The contribution is the sharp five-prime exclusion via complete reduction to 87 candidates, not the six-factor example or the general complement-pair test.

## value

PASS

Sharp minimal distinct-prime support is a natural arithmetic invariant for a divisor-selection property; the known squarefree example with six primes specifically motivates deciding whether five suffice. The result completes this extremal layer with a mathematically exhaustive finite certificate and an attained bound, a useful fact beyond isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
