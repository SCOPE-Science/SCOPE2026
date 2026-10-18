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

The six and only factorizations with 1<=Omega(n)<=3 are p, p², pq, p³, p²q, pqr. Multiplicativity gives all claimed congruences exactly: for p prime σ(p)+φ(p)=2p; p² gives 2p²+1 mod3 so iff p!=3; pq gives 2(pq+1) mod4 so both odd; p³ gives 2p³+p+1 mod4 so p=1 mod4; p²q gives q(2p²+1)+2p+1 mod6 yielding q odd and (p=1 mod3 or p=3 and q=2 mod3); odd pqr has both σ,φ multiples of8, while 2qr divisibility mod8 iff q,r opposite mod4. Independent exact integer computation checked every 2<=n<=25000 with Omega<=3 against the six-shape criterion, 15,448 tested numbers (2,762+6,265+6,421), no counterexample. The unbounded theorem follows from shape exhaustion and modular algebra, not from this finite test.

## originality

PASS

The OEIS A055464 sequence defines precisely τ(n) | σ(n)+φ(n), gives raw terms and related σ+φ=nτ prime characterization, but does not classify its first three Ω layers by residue conditions in material inspected. Relevant Resultary query identified other τ and multiplicity constraints, not this exact mixed sum and all six shapes. Congruence deductions are elementary and can be folklore, specifically stated as residual risk; nothing found that already implies the full stated six-case classification.

## value

PASS

Natural classical divisor-count divisibility has a published sequence but no structural low-multiplicity description in checked references. Exhausting all six factorizations with Omega<=3 produces unbounded congruence families distinguishing primes, prime powers, semiprimes, and even versus odd three-prime products. This is an independently useful classification of low arithmetic complexity, not an ad hoc finite data cutoff; elementary proof alone does not negate value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
