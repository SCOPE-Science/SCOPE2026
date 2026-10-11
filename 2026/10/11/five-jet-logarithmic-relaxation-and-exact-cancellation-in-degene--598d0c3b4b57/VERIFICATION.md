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

# Reproduction and analytical limits

The theorem is established analytically by the energy law, the smooth center-manifold invariance equation, an exact transverse equation and a convergent inverse-square remainder. `lienard_critical_checker.py` is included to check finite polynomial identities only; it does not certify the infinite-time dynamics and requires SymPy as stated in `requirements.txt`.

Actual replay of the included checker: `python lienard_critical_checker.py` returned `CHECK_OK`. It verifies the exact third/fifth center-graph coefficients, \(\Gamma=d/c-b/a+3c/a^2\), the polynomial cofactor identity, the iff cancellation relation \(b=ad/c+3c/a\), and the signs \(3,0,-3\) for the admissible examples \((a,c,d)=(1,1,0)\), \(b=0,3,6\).

Separately, numerical forward integrations over \(t\in[0,5000]\) yielded empirical logarithmic slopes approximately \(2.9766\), \(0\), and \(-3.0166\) for those examples. The small discrepancies at finite time are expected from the integrable \(O((\log t)/t^2)\) residual. These finite experiments are not exhaustive and are not used as the proof of asymptotic or global statements.

Only the smooth odd/even positive-damping regime is proved. The exceptional fast trajectories require the strong stable manifold; their inverse-square quantity does not satisfy the slow logarithmic law. The exact cubic invariant curve is a special polynomial case and is not asserted for general smooth forces.
