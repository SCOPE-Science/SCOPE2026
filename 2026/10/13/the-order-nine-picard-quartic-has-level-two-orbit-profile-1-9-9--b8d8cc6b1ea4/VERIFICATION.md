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

The verification target is the order-nine plane quartic
\[
C:\ y^3z=x(x^3-z^3)
\]
and the algebraic deductions used in the orbit proof.

Running `python3 verification.py` under SymPy \(1.14.0\) checks exactly that the cubic
\[
f(u)=u^3-96u^2+48u+64
\]
is irreducible and has nonzero discriminant, that the substitutions
\[
u=-36t^2-12t+104,
\qquad
t=-\frac{u^2}{48}+2u-\frac23
\]
identify it with \(t^3-3t+1\), and that \(\Phi_9(T)=T^6+T^3+1\) is irreducible modulo two. It also verifies
\[
\gcd(\Phi_9(T),T^k-1)=1\qquad(1\le k\le8)
\]
over \(\mathbf F_2\), and the orbit totals \(28=1+3\cdot9\), \(36=4\cdot9\), and \(63=7\cdot9\).

The script does not replace the geometric proof that \(z=0\) is the only bitangent stabilized by the order-three subgroup, nor the local regularity argument for the holomorphic differential basis. Those arguments are written explicitly in `RESULT.md`.
