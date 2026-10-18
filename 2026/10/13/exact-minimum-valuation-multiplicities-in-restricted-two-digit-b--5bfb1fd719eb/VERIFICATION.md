---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For p prime, m>=3 dividing p+1, N=p^s+p^t>m, t-s odd, zero-borrow binomial indices are exactly 0,p^s,p^t,N and none is a proper multiple of m. Kummer gives h>=1. Exactly one borrow ends immediately below s or t, with adjacency handled separately; modular conditions d+e=0 mod m or d=0 mod m give h=1 and H=(a-1) times 1,3,2,4 according to gap/s. At m=p+1 one-borrow residues are impossible; an exhaustive classification of two adjacent or separate borrow positions gives h=2 and H=(p-1) times 1,3,2,3,5 with stated boundary branches. The impossible N=m exception is excluded. Independent Legendre-factorial arithmetic exhaustively checked 70 valid small parameter cases and exact minimizing indices, not an unrestricted proof.

## originality

PASS

Detailed implication comparison to primary prior work, using all four separate originality checks. No identified prior theorem or table implies the exact newly stated invariant; findings are best-of-knowledge with residual risks.

## value

PASS

A restricted binomial gcd determines only the smallest valuation, not how many Pascal-row positions attain it. The exact minimal-valuation-layer multiplicities and complete minimizer parametrization answer a natural refinement of the original number-theoretic extremal question for sparse two-digit rows; stabilization by parity gap is a motivated structural phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
