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

After n steps at x, white count 1+(n-x)/2, blue count (n+x)/2, hence P(next x+1)=(n+2-x)/(2(n+1)); on survival x>=1 this is <=1/2. The killed first moment A_n=nE[X_n 1_{tau>n}] satisfies the EXACT identity A_{n+1}=A_n+u_n with u_n=P(tau>n), because a move from x=1 to zero carries zero weighted mass. Coupling surviving paths to a fair simple random walk above them, and reflection principle, gives u_{2n}<=2A_n/[n sqrt(n+1)]. Since u_n decreases, u_j<=b_j A_floor(j/2), b_j=O(j^-3/2) summable. Choose J with sum_{j>=J}b_j<=1/2: A_{N+1}<=A_J+(1/2)A_{N+1}, so A_n bounded; hence u_n=O(n^-3/2) and E tau<infinity. Independent exact rational killed-chain DP verified recurrence, mass, monotonicity to 70 steps (u70~0.01655614). Finite DP does not prove infinite tail.

## originality

PASS

Best-of-knowledge solves Balaji–Mahmoud stated finite-mean first-return conjecture in their precise initialized opposite-addition model, with additional O(n^-3/2) survival upper bound. Closest elephant and urn drift papers address different initializations/positive drift recurrence classifications, not this killed-moment mean theorem; inaccessible entire Bertoin 2022 primary creates acknowledged overlap risk.

## value

PASS

Resolves a specifically published finite-mean-first-return conjecture for a canonical negative-reinforcement urn walk, and proves a useful O(n^-3/2) survival upper bound through a structurally motivated killed-moment recurrence and summable renewal bootstrap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
