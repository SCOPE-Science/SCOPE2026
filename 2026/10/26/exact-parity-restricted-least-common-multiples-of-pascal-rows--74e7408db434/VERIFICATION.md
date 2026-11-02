---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For every prime p, Kummer borrowing shows max_k ν_p(C(N,k))=floor(log_p(N+1))−ν_p(N+1); an index p^r−1 attains the maximum. Odd N is handled by k↔N−k. At even N, all odd-prime maxima occur at even k; the even-index two-adic maximum equals the full-row two-adic maximum of row m by ν_2(C(2m,2j))=ν_2(C(m,j)). Odd-index two-adic maximum is attained by k=2^r−1. At an odd p, odd k=p^r−2 or modified digit k=p^r−1−p^j retains the full p-adic maximum except when N+2=2p^r; there the unique full-maximizer k=p^r−1 is even and the best odd k loses one p. This exhausts base-p digit patterns. Fresh independent exact LCM computation for N≤400 agrees, but the infinite theorem is proved by the borrow cases.

## originality

PASS

Farhi gives the complete-row LCM and Kummer gives local valuations. Huber studies optimizing chosen entries and asymptotic supports, not the preassigned complete parity subrows. Prescribed parity-restricted quotients and their odd-prime-power exception were not located in inspected prior results.

## value

PASS

The all-N two-class restriction is a natural arithmetic refinement of the familiar Pascal-row LCM. It yields unexpectedly sharp complementary prime-loss laws, one purely 2-adic and the other triggered precisely by odd prime powers; neither quotient follows by routine substitution into the full-row identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
