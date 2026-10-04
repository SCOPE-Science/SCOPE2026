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

The proof is symbolic and valid for every finite field of characteristic different from \(2\) and \(3\). The bundled verifier is a finite corroboration, not an exhaustive proof.

It performs exact collision counts for 24 prime fields from \(5\) through \(101\), skipping characteristic \(3\), and for quadratic extensions of orders \(25\), \(49\), and \(121\). In each case it checks
\[
E(C_4)=3q^2-q-1-(q-1)(1+\chi(-3))^2
\]
and the equivalent \(q\bmod3\) form. It also checks the algebraic factorization
\[
(s^4-4us^2+2u^2)-(s^4-4vs^2+2v^2)=2(u-v)(u+v-2s^2)
\]
on a finite integer grid.

Successful replay prints `VERIFY_OK prime_fields=24 quadratic_extensions=3 max_prime=101`. The finite checks do not establish the universal theorem; universality comes from the character-sum proof in `RESULT.md`.
