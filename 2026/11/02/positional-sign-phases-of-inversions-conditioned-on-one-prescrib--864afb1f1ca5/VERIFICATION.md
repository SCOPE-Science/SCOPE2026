---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For the required event Pi(i)=j and Pi(j)=i, the other n-2 images are uniformly permuted on the remaining labels; pairwise inversion probabilities split into the fixed pair (one), two free positions (one half), and x=i-1,y=j-i-1,z=n-j mixed positions. Their contributions (y+2z)/d,(d+y)/d,(2x+y)/d with d=n-2 yield Delta=1/2+[y^2-(x-z)^2]/d, algebraically the claimed factorization. The event probability is 1/[n(n-1)], and summing local covariance gives Cov(I,C2)=1/12. Riemann-area sign analysis applies away from u=1/2 or v=1/2; n=3 is covered by d=1. Independent direct enumeration through n=7 corroborates exact formulas, not the asymptotic proof.

## originality

PASS

Qualified PASS: class-averaged inversion expectation (Hultman, Lemma 6.1/Theorem 6.2) already establishes the aggregate but averages away location of a specified transposition. The fixed labeled-pair saddle and sign fraction are a genuinely different conditional statistic, not a corollary of the class average alone; no matching stronger primary theorem identified in the material inspected.

## value

PASS

PASS: conditioning on one specified two-cycle is canonical in permutation cycle statistics; the exact location-dependent sign reversal, midpoint phase diagram and cancellation to a tiny aggregate covariance explain a structural dependence phenomenon that class-average statistics miss. The formula holds for all sizes, not a tiny arbitrary table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
