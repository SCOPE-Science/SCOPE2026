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

The proof of infinite order uses two exact good reductions rather than a bounded-height point search.

The bundled `verify.py` checks the identity
\[
y_*^2=q^3\cdot1116-3888,
\]
the degree-one specializations
\[
\theta\equiv12\pmod{17},\qquad \theta\equiv13\pmod{23},
\]
the resulting reduced points
\[
\overline P_{17}=(2,8),\qquad \overline P_{23}=(17,17),
\]
and their exact group-law orders \(9\) and \(4\). It also checks that the denominators are units and the elliptic curve has good reduction at both primes.

The replay does not attempt to enumerate \(E(L)\). The full Mordell--Weil group and saturation index of the critical-value submodule remain unproved limits. The module-theoretic conclusion uses the mathematical fact that a nonzero elliptic-curve endomorphism has finite kernel.

The saved output must end in `VERIFY_OK`.
