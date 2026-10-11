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

Put \(r=\beta/\alpha\). The proof uses only norm inequalities and two explicit Birkhoff-orthogonal constructions.

For \(0<r\le1\), \(\|x+r y\|_\infty\le1+r\) and \(\|r x-y\|_\infty\ge1-r\), so the objective is at most \(2r\); Proposition 1 of the defining paper gives the independent bound \(1\). For \(0<r\le1/2\), \(x=(1,-1)\), \(y=(2r-1,-1)\) attains \(2r\). For \(r\ge1/2\), \(x=(1,-1)\), \(y=(1,0)\) attains \(1\). Both Birkhoff conditions are checked directly for all real \(\lambda\), not by sampling.

For the boundary-segment obstruction, a line segment in the boundary of the square lies in a face. If \([x,y]\subset S_X\), some coordinate has \(x_j=y_j=s\in\{-1,1\}\). The endpoint \(x-(2/r)y\) then has coordinate \(s(1-2/r)\), whose magnitude exceeds \(1\) for \(r<1\). Therefore the second required segment cannot lie in the unit sphere for any \(r<1\).

The bundled `verify.py` checks the algebraic constructions on rational parameter grids and the endpoint obstruction. Its output is a regression check only; it is not a finite certificate for the quantified theorem.

The literature verification used the full open-access defining article, including the exact definition and Theorem 2, and targeted searches for equivalent forms and corrections. The principal remaining risk is an unindexed later correction or duplicate computation.
