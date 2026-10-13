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
The standalone checker `artifacts/verify.py` uses independent symbolic coordinates for the first fixed Heisenberg bracket and the second arbitrary alternating operation. It reconstructs the full mixed-Jacobi and ordinary Jacobi equations before performing any elimination. It also checks the reduced formula after imposing the compatibility constraint.

For each of \(\mathbf F_3\), \(\mathbf F_5\), and \(\mathbf F_7\), it exhaustively enumerates all seven nonlinear coordinates after eliminating the fixed mixed constraint and factors in the freely varying eighth coordinate. In addition, it directly enumerates all \(3^9=19683\) original bracket tables over \(\mathbf F_3\), independently checking every unreduced coordinate equation before elimination.

Recorded counts:
\[
\begin{array}{c|r|r|r}
q & \#\text{compatible brackets} & \#\text{nonzero-vector stratum} & \#\text{component intersection}\\\hline
3&945&216&99\\
5&18625&3000&725\\
7&134113&16464&2695
\end{array}
\]
The program exits successfully with the marker `VERIFY_OK`.

These enumerations are finite replay checks. The characteristic-uniform result follows from the symbolic reduction and the exact vector-bundle/rank-one incidence argument, not from extrapolation of the three examples.
