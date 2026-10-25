---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Permutation symmetry reduces the complete two-shell first Walsh Gram matrix to ES=0 and ES^2=n for S=sum coordinates; positive masses on s and -t solve these exactly when st=n, with parity s=t=n mod2 and 1<=s,t<=n. Hence n odd or 4|n. The number of sample vertices is the sum of two binomial shell sizes, yielding the exact divisor minimum for all odd n. Independent exact binomial computation for each odd dimension up to 201 confirms first strict improvement at n=51, pair (3,17), 244362982488625 versus 247959266474053. The analytic all-n progression follows from the positive-polynomial identity for 3/4-R_(r+1)/R_r, whose numerator is 3(13r^4+65r^3+138r^2+144r+60); independently verified polynomially. Finite counts do not establish the infinite recurrence.

## originality

PASS

Best-of-knowledge compared exact implications, relevant general theorems, primary materials actually read, and current published mathematical research records; specific prior ingredients credited and uninspected plausible full texts named explicitly.

## value

PASS

Exact tight recovery of the full affine Walsh band from symmetric complete-shell measurements is a natural quadrature/frame problem. The arithmetic existence criterion, all-odd-dimension sample-cost optimization and first support transition at n=51 give precise structural and resource thresholds, not a randomly sliced table. The result does not optimize arbitrary irregular supports.

The dated certificate retains the supplied scientific assessment, sources and limitations.
