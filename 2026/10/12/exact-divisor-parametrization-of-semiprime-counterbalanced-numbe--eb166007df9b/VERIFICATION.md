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

The theorem in `RESULT.md` is proved algebraically and is not inferred from finite data.

The attached `verify.py` performs three exact corroborative checks.

First, for every pair of primes
\[
p<q<5000,
\]
it compares the direct condition
\[
p+q+1\mid(p-1)(q-1)
\]
with the divisor-parametrized condition
\[
p+q+1\mid(p-1)(p+2).
\]
The two predicates agree for every pair.

Second, for every prime
\[
p<5000,
\]
it verifies that
\[
p+1\nmid p(p-1),
\]
so no prime square enters the multiplicity-two layer.

Third, it directly verifies the initial counterbalanced semiprimes
\[
133,403,583,713,817.
\]

These checks test the implementation and representative data. The universal claim rests on the exact identity in the proof.
