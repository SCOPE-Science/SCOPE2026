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

The proof is algebraic. The accompanying exact-integer script performs independent finite checks of its critical counting step.

It constructs the fibers of
\[
(t_1,t_2,t_3)\longmapsto
\left(\sum_jt_j,\sum_jt_j^2,\sum_jt_j^3\right)
\]
over \(\mathbb F_p\) for \(p=5,7,11\), verifies that fiber sizes are exactly \(1,3,6\) according to the multiplicity pattern of the triple, and checks
\[
J_{3,3}(p)=p(6p^2-9p+4).
\]
It also checks the Chinese-remainder product formula for representative squarefree moduli by multiplying the verified local factors.

The finite computations do not prove the theorem for all primes. The infinite proof rests on Newton identities, exact multiset enumeration, and the Chinese remainder theorem. The published affine-symmetry moment identity is used only after that exact arithmetic count has been established.

No independent audit has been performed.
