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
The symbolic proof uses Frobenius character induction, nondegeneracy of the finite-field trace pairing, and the elementary fact that a cyclic subgroup of order \(m\) generates the subfield
\[
\mathbf F_{p^{\operatorname{ord}_m(p)}}.
\]

The packaged checker `artifacts/verify.py` constructs
\[
\mathbf F_7,\quad\mathbf F_8,\quad\mathbf F_9,\quad\mathbf F_{16}
\]
from explicit polynomial models and verifies the parameter pairs
\[
(7,3),\ (8,7),\ (9,4),\ (16,3),\ (16,5),\ (16,15).
\]

For every nonzero additive-character parameter \(a\), it checks that
\[
\dim_{\mathbf F_p}\operatorname{span}(aH)
=
\operatorname{ord}_m(p)
\]
and directly counts the simultaneous trace kernel
\[
\{x:\operatorname{Tr}(ahx)=0\ \forall h\in H\}.
\]
The observed kernel size is always
\[
p^{f-\operatorname{ord}_m(p)}.
\]

It then builds the predicted pseudo-algebra
\[
\{(d,\varphi(d)):d\mid m\}
\cup
\{(p^e,(q-1)/m)\}
\]
and verifies that the largest codegree, second-largest codegree, and multiplicity reconstruction returns the original \((q,m)\).

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.
