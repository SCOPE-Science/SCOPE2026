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
The universal proof is independent of finite enumeration.

The critical structural checks are:

- fixed-point-freeness implies \(p\nmid m\), hence semisimplicity;
- every nonzero kernel conjugacy class is a free \(C_m\)-orbit;
- every coset \(Vh^j\), \(j\ne0\), is one conjugacy class;
- kernel-kernel and outside-outside class pairs cannot be adjacent;
- a mixed pair is adjacent exactly when \(\gcd(j,m)=1\) and the kernel representative is a cyclic module vector;
- a cyclic vector exists exactly when every irreducible constituent occurs with multiplicity one;
- in that case there are \(\prod_i(p^{d_i}-1)\) cyclic vectors.

The packaged checker `artifacts/verify.py` constructs five explicit semidirect products, computes every conjugacy class, and tests every representative pair for generation. It verifies the predicted active graph in each case:
\[
K_{1,1},\quad K_{1,2},\quad K_{1,6},\quad K_{12,2},
\]
and the empty active graph in the repeated-constituent example.

It returns `VERIFY_OK`.

Finite computation is not used to prove the universal theorem.
