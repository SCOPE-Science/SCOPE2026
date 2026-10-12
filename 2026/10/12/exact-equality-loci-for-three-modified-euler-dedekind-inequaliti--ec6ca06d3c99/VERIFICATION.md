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

The proof in `RESULT.md` was checked algebraically at the prime-power-block level. The critical identities are
\[
\psi(p^a)-\Psi(p^a)=\Phi(p^a)-\varphi(p^a)=p^{a-1}-1,
\]
\[
E(mp^a)=\Phi(p^a)E(m)+2A(m)+(p^{a-1}-1)(\psi(m)-\varphi(m)),
\]
and
\[
H(mp^a)=p^aH(m)+\Psi(m)-\Phi(m)
\]
for coprime \(m\) and \(p\). Their sign conditions give the two non-product equality classifications, while the product classification follows factorwise.

The standalone regression script `verify.py` factors every integer \(2\le n\le50000\), computes the four functions directly from the defining products, and checks all three biconditionals. The recorded run is:

`VERIFY_OK n_max=50000 equality_checks=149997`

No computation is used to extend a finite observation to all integers. The symbolic proof supplies the unbounded result.
