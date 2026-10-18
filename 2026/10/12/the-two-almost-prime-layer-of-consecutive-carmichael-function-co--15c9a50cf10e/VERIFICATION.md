---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For n≥2 and Ω(n),Ω(n+1)≤2, the even member is either 2, 4, or 2p with p odd prime. Direct λ values of (2,3),(3,4),(4,5) leave only (3,4). For even e=2p, λ(e)=p−1; odd adjacent o=2p±1 is prime, an odd square r², or qr with odd primes q<r. A prime o has λ(o)=o−1>p−1. For square o=2p−1, λ(o)=r(r−1)>(r²−1)/2=p−1; for o=2p+1, equality reduces to r²−2r+3=0 with negative discriminant. For distinct qr set d=gcd(q−1,r−1)≥2≤q−1. Equating λ(qr)=(q−1)(r−1)/d with p−1 yields (2−d)qr=2q+2r−2−d (o=2p−1) or (2−d)qr=2q+2r−2−3d (o=2p+1). Left side ≤0 but both RHS >0, using d≤q−1. Exhausts all cases. Independent separate exact Carmichael factorization enumerated n=2..9999 with only n=3 under Ω bounds, corroborating but not proving the infinite case.

## originality

PASS

Compared low-complexity consecutive coincidence against Ford–Luca–Pomerance’s value-set result and Lebowitz-Lockard–Vandehey’s work on maximal constant λ-runs. Neither a global λ image theorem nor bound on lengths of unrestricted constant runs determines which adjacent prime/semiprime pairs can coincide. Resultary’s seemingly close Ω≤2 theorem concerns σ(n)=σ(n+1), which has unique (14,15), not λ; another Carmichael result corrects a false prime-power formula, not the low-layer classification. Exact prime-square and odd semiprime cases require the dedicated gcd/lcm argument. Priority best of knowledge; short observations may be unindexed.

## value

PASS

The union of prime/semiprime pairs is the first natural nontrivial multiplicative-complexity layer for a difficult consecutive-value question. Its complete empty-except-(3,4) classification gives an exact structural obstruction to such coincidences and a lower bound of three prime factors in every larger equal pair, not just a small computational cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
