---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For positive n and odd prime p, the binomial identity gives p E_p(n)=C-A with C=binom(n-1,2p-1) and A=(p+1)(n_1-1) times the indicator of p dividing n. Lucas modulo p gives zero if p does not divide n and n_1-1 modulo p otherwise, so p divides C-A. Since A is even and p odd, Lucas modulo 2 then gives the mask condition, also for n<2p. For the printed floor sum, fix digit e_h of j and let f_h be the h-th zero position of m-1, indexed from zero. Exactly the first r=f_h-h one positions of m contribute, with coefficient 2^(h+1) plus the terms 2^(h+a-1) for 2<=a<=r, which sums to 2^f_h even when r=1. Thus j fills exactly the complementary bits of m-1 without carries, yielding a bijection onto all 2^z mask classes, including the residue n=0 modulo 2^L via n-1. Dividing the defining equality by two gives the stated fractional part. The proof is universal; the independent limited check through p=47 and the larger author-recorded checks in VERIFICATION.md/verify.py are corroboration only; the uploaded script was inspected, not executed.

## originality

PASS

The supported distinct contribution is a proof of the full floor-sum residue-set equivalence in Rowland's printed Conjecture 2. The Lucas arithmetic and already known preliminary fractional-part reduction are not credited as the novelty. No covering proof was identified in the bounded comparisons.

## value

PASS

This resolves an explicitly posed all-prime conjecture, explaining why its floor-sum list has no duplicate residues and replacing an implicit search with a single mask test. The value lies in explaining and exhausting the exact printed parametrization, not in recomputing examples or applying Lucas alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
