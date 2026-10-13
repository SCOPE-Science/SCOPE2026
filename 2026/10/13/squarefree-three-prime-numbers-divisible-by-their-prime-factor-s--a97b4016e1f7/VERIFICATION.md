---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof in `RESULT.md` is universal. The attached computation is a consistency check, not the source of the infinite conclusion.

The verifier sieves integers through
\[
2{,}000{,}000,
\]
extracts exactly those that are squarefree with three distinct prime factors
\[
p<q<r,
\]
and compares two predicates:

1. the direct divisibility test
\[
p+q+r\mid pqr;
\]

2. the theorem's criterion
\[
p=2,\ r=q+2
\]
or
\[
r=pq-p-q>q.
\]

It asserts equality of the two predicates for every tested triple and records the direct hits. It also checks that the branch formula gives the expected divisor, namely \(2r\) in the twin-prime branch and \(pq\) in the shifted-product branch.

The exhaustive finite replay cannot establish the theorem for unbounded primes. The unbounded claim is justified by the proof's exact divisor interval and case split.
