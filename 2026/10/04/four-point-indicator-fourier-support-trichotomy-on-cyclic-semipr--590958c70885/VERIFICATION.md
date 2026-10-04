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

The proof is symbolic and applies to every odd prime \(p\). Its critical steps are:

- a vanishing sum of four unimodular numbers splits into two antipodal pairs;
- a nonzero even frequency on \(\mathbb Z_{2p}\) has odd character order and therefore cannot vanish on a four-point indicator;
- \(k=p\) vanishes exactly for two-even/two-odd supports;
- every other odd frequency is a unit modulo \(2p\), so vanishing is equivalent to the support being a union of two antipodal pairs;
- the resulting three structural classes have the stated binomial counts.

The standalone verifier uses exact integer arithmetic in cyclotomic quotient rings. It constructs cyclotomic polynomials recursively, reduces each Fourier sum exactly modulo the appropriate cyclotomic polynomial, and compares the resulting zero set against the theorem. It exhausts every four-subset for \(p\in\{3,5,7,11,13\}\): 23,491 subsets and 565,834 frequency tests. The expected terminal line is `VERIFY_OK`.

Finite replay is corroborative only; no bounded enumeration is used to justify the theorem for arbitrary \(p\).
