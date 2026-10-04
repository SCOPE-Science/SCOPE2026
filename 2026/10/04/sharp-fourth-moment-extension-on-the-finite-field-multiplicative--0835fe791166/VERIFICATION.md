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

The analytic proof applies to every finite field of odd order. The standalone script `verify_hyperbola.py` is a finite corroboration of the collision decomposition and equality witnesses, not an exhaustive proof of the infinite family.

It enumerates ordered pairs on \(H\) for every odd prime through \(101\), groups them by vector sum, and verifies
\[
E(H)=3(q-1)(q-2).
\]
It also checks that the zero vector has exactly \(q-1\) ordered representations, that every nonzero pair-sum fiber has size at most two, and that deterministic sign data with constant modulus and common antipodal product phase attain
\[
Q(g)=\frac{3(q-2)}{q-1}\left(\sum_t|g(t)|^2\right)^2.
\]

The critical infinite steps not delegated to computation are: cancellation of \(s=a+b\ne0\) in the inverse-sum equation, the exact exceptional-fiber correction, phase alignment, the bound \(p_j\le s_j/2\), and Cauchy--Schwarz across antipodal pairs.
