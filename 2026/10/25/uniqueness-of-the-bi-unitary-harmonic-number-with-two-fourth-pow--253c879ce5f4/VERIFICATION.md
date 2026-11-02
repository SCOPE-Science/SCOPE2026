---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The prime-power formulas give H**(p^4 q^4 r)=32g4(p)g4(q)g1(r), with g4(x)=x^4/(x^4+x^3+x+1), g1(x)=x/(x+1). Sorting a<b<c and assigning the 3 possible exponent patterns covers every prime placement. Strict monotonicity bounds a<=89 via 32g1(97)g4(97)^2>31 and H<32; 72 exact rational interval comparisons exclude b>=397. For each remaining first-two-prime and integer harmonic level h, reduce 32g_{e1}(a)g_{e2}(b)=A/B. The identity hB*sigma**(c^{e3})=Ac^{e3} modulo c yields c|hB, as sigma**(c^1) and sigma**(c^4) are 1 mod c. This makes the third-prime set finite and exhaustive. Independently implemented exact rational enumeration exhausts 4644 sorted-pair/pattern branches, 44193 integer h levels, 36313 candidate last primes, and returns only (a,b,c,e1,e2,e3,h)=(2,3,7,4,4,1,12). Direct H**(9072)=12 verifies existence. Certificate factorization cutoffs and interval precision were inspected; finite search is exhaustive because the prior bounds are analytic, not because of an arbitrary cutoff.

## originality

PASS

The witness 9072 and its harmonic value 12 are explicitly in Sándor (2011) and OEIS A286325; they are not new. Manea–Minculete (2016) prove results for p q t^2 and p^2 q^2 t and certain 2^k times squarefree forms, which do not contain p^4 q^4 r for all prime orders. Resultary search found distinct two-prime bi-unitary exponent-family rigidity but not this three-prime exponent multiset. The all-prime uniqueness classification is a qualified best-of-knowledge novelty claim, not a claim of discovering 9072.

## value

PASS

An exhaustive classification for a natural minimal three-prime exponent pattern extends a known example into an all-prime uniqueness theorem, combining global rational bounds and a modular factor restriction. This closes a concrete arithmetic family beyond finite OEIS enumeration, not an arbitrary numerical recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
