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
The central verification is symbolic and analytic.

At the no-stem/no-progenitor equilibrium,
\[
1+ld_1=R_c.
\]
The stem and progenitor diagonal Jacobian entries are therefore
\[
\frac{R_a}{R_c}-1
\]
and
\[
g_b\left(\frac{R_b}{R_c}-1\right).
\]

The lower \((c,d)\) block has trace
\[
-g_d\left(2-\frac1{R_c}\right)
\]
and determinant
\[
g_cg_d\left(1-\frac1{R_c}\right).
\]
For \(R_c>1\), its roots have negative real part.

The bundled checker constructs the symbolic Jacobian factorization and independently evaluates the witness
\[
R_a=\frac32,
\quad
R_b=\frac65,
\quad
R_c=2.
\]
It verifies corrected upstream eigenvalues \(-1/4\) and \(-2/5\), while the two source formulas evaluate to \(1/4\) and \(1/2\).

Finite computation is not used as a substitute for the local-stability proof.
