---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For L>0 and a nonantipodal pair the normalized arguments of L+i(h±t) belong to the same right-half-plane branch. The determinant of the old and new double-angle vectors has sign given by 2t[(L−K)+(1−L)t²], and for t>0 both arguments lie strictly between 0 and pi; hence the determinant gives the actual direction of motion. The separation update is odd and increasing, and all monotone bounded orbits must approach finite fixed points. The determinant lists exactly the finite separators and settles K=L as repelling at zero for 0<L<1. The antipodal pairs are fixed and the identity is exactly the L=1,h=0 boundary. The diagonal multiplier L/K and the antipodal half-angle multiplier L give geometric convergence in the applicable cases. The midpoint defects are even and O(t²) near consensus after subtraction of the rigid increment, and O(t^−2) near antipodality, so they are summable. At L=1,h≠0, expanding the positive-t antipodal distance gives epsilon^+=1/t+(h²−1/3)/t³+O(t^−5), so t^+²=t²−2h²+O(t^−2). Uniform upper/lower bounds on the square decrement above any sufficiently large cutoff, and bounded subsequent residence in any fixed compact positive interval before hitting T, prove the escape constant. The proof's final epsilon_0 t_0 should read epsilon_0 |t_0| for both signs; by oddness the stated squared limit is correct. The midpoint angle is taken modulo 2pi and is defined off exact antipodality, where the full state instead remains fixed. Independent direct complex iteration, without executing the uploaded checker, corroborated the regime directions and the limiting escape scale (for h=±0.8, normalized times 0.78809, 0.78320, 0.78186 at |t_0|=32,64,128, versus 0.78125).

## originality

PASS

Best-of-knowledge pass for the complete relative-basin portrait and sharp marginal escape law, not for the model class, planar reduction or the existence of rotating consensus in general. In particular a rotating frame puts the exact two-token update in a subfamily of Gao–Yang–Chen's earlier model. Their inspected results leave stability regions and attraction basins open, and the nearer indexed coexisting cycles concern different matrices and dynamics.

## value

PASS

The low-dimensional family is motivated by a real limitation of alignment-based results for nonsymmetric normalized dynamics. The exact global bistability region, finite-separation separators and sharp parabolic time law distinguish what happens beyond a local Jacobian test and resolve a natural minimal planar case. No architecture-level performance claim follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
