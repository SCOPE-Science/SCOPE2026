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

The unrestricted theorem is proved symbolically in `RESULT.md`.

The packaged checker performs finite corroboration only. It enumerates odd composite
integers through a fixed bound, computes
\[
k=\frac{n-1}{\sigma(n)-n-1}
\]
when the denominator is positive and divides \(n-1\), selects odd integral
\(k>1\), and verifies:
\[
\nu_2(\sigma(n))=1,
\]
exactly one prime exponent is odd, and the corresponding prime and exponent are
both congruent to \(1\pmod4\).

It also verifies the defining equation and the same structural conclusions for
the known odd-index examples \(325\), \(10693\), \(51301\), \(214273\), and
\(306181\).

The finite sweep is not used to infer the infinite theorem. No assertion is made
that every odd-index hyperperfect number is odd or that every such number has
only two distinct prime factors.
