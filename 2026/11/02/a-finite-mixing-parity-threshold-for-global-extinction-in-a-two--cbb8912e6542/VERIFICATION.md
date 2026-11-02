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

# Reproducible checks

The proof is given in `RESULT.md`; it does not rely on a finite computation. Run `python3 verification/check_parity.py` using the Python standard library. The program re-computes \(P^k\) exactly for four rational migration rates and all integers \(1\le k\le17\), giving 68 exact matrix-power checks, and verifies the Jacobian trace and determinant with exact rational arithmetic. It also evaluates the analytically derived Perron root and numerically iterates the nonlinear map at the source–sink witness \(r_1=2\), \(r_2=1/5\), \(p=9/10\), \(a_i=r_i\).

Observed sequence: \(k=1,3,5,7\) has invasion multipliers below one and iterates converge toward zero; all tested even \(k\) and odd \(k\ge9\) have invasion multipliers above one and trajectories approach positive equilibria. The program tests a critical eigenvalue equal to one at \(k=1\), \(p=4/7\); its iterates decrease slowly, consistent with the proved strict Lyapunov descent. Results are numerical checks on a finite collection of parameters and do not certify the universal theorem or originality.
