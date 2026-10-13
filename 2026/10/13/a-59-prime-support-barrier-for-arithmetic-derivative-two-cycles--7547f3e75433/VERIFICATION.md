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

The proof uses one published structural premise: a nontrivial positive two-cycle of the arithmetic derivative has squarefree members with disjoint prime supports. The full source containing that result was inspected.

For squarefree cycle members,
\[
A=\frac{D(n)}n=\sum_{p\mid n}\frac1p,
\qquad
B=\frac{D(m)}m=\sum_{q\mid m}\frac1q.
\]
The cycle equations give
\[
AB=1,
\]
so
\[
A+B\ge2.
\]

The attached checker then performs the only finite computation used by the new argument. It generates primes by exact integer trial division and computes reciprocal sums as reduced rational numbers. It verifies
\[
P_{58}=271,\qquad P_{59}=277,
\]
\[
\sum_{i=1}^{58}\frac1{P_i}<2,
\]
and
\[
\sum_{i=1}^{59}\frac1{P_i}>2.
\]

It also verifies the exact rational numerator and denominator printed in `RESULT.md`. No floating-point comparison is used for acceptance.

The computation does not search for arithmetic-derivative cycles. It certifies only the finite extremal reciprocal-sum threshold needed by the universal proof.
