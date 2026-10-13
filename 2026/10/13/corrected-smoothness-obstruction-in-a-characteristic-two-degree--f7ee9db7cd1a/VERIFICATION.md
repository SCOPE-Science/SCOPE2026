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

The proof uses the exact characteristic-two derivatives of
\[
F=w^2+(x^2+yz)w+\lambda xyz(y+z)+ay^4+by^3z+cy^2z^2+dyz^3+ez^4.
\]
On \(x^2+yz=0\), use \([x:y:z]=[uv:u^2:v^2]\). Then
\[
F_x=\lambda u^2v^2(u+v)^2,
\]
so for \(\lambda\ne0\) a singular point can occur only over \(u=0\), \(v=0\), or \(u=v\). These are the three base points \([0:0:1]\), \([0:1:0]\), and \([1:1:1]\).

At those points, the remaining derivative equations force \(w=d\), \(w=b\), and \(w=\lambda+b+d\), respectively. Substitution into \(F\) gives the three exact obstruction values
\[
d^2+e,\qquad b^2+a,\qquad \lambda^2+b^2+d^2+a+b+c+d+e.
\]
Their simultaneous nonvanishing is therefore equivalent to smoothness inside family (1)(a).

The bundled `verify.py` checks two separating parameter vectors over \(\mathbf F_2\): one satisfies all printed nonzero conditions but has a singular point, while the other violates the printed disputed condition but satisfies all exact obstruction values. It also directly evaluates \(F,F_w,F_x,F_y,F_z\) at the singular witness.

The checker does not establish originality, does not inspect downstream classification tables, and does not replace the symbolic exhaustion proof.
