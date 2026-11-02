---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The frozen proof diagonalizes the XX dimer Hamiltonian into even states of energies ±B and odd block [[b,J],[J,-b]] with eigenvalues ±E, E=sqrt(J^2+b^2), and derives exact X-state concurrence C=[(J/E)sinh(beta E)-1]_+/(cosh(beta E)+cosh(beta B)). On the circular budget B²+b²=R², maximize t=|B| in [0,R]. For R<J, E-t>=J-R>0 uniformly; exponentially small corrections have derivative O(t beta²exp(-beta(J-R))), so the leading J/E strictly increases and unique maximizing magnitude is t=R at sufficiently large beta. For R>=J, the unique crossing E=t is s=sqrt((J²+R²)/2); a near-crossing trial s-beta^(-1/2) yields limiting J/s, forcing every maximizing sequence to t->s from below with beta(E-t)->∞. The stationary logarithmic derivative then gives exp(beta(E-t))~2 beta s and the two expansions. At R=J, b²~J log(2 beta J)/beta. Independently reconstructed 4x4 Hamiltonian eigenvalues/Gibbs concurrence using matrix algebra on 35 parameter samples and one-dimensional large-beta optimizers for R/J<,=,>1; all agreed with stated formula and logarithmic shift. This is an analytical all-parameter proof, not a numerical optimization extrapolation.

## originality

PASS

The XX and XY Gibbs concurrence formulas and their uniform/inhomogeneous-field dependence are longstanding prior results. The original Sun–Chen–Chen and Asoudeh–Karimipour papers are acknowledged for this material. The new mathematical claim is maximization under the exact Euclidean field-budget equality, identifying the R=J allocation phase boundary and logarithmic beta^-1 correction of all optimizers. General free-field Hamiltonian maximization by Kuwahara–Hatano is not the same constrained problem. Full text of Sun 2003 was unavailable behind an institutional VPN block; its abstract and comparable accessible primary Asoudeh text were read, so historical priority is qualified rather than falsely certified.

## value

PASS

The fixed RMS-field-strength budget is a natural laboratory/control-constrained optimization: fields may be redistributed but not made arbitrarily strong. The optimum shifts from homogeneous fields to an inhomogeneous, near-energy-crossing allocation and has a singular beta^-1 log(beta) boundary layer. This is a concrete sharp phase transition and quantitative finite-temperature correction, not a reparameterized fixed-field concurrence formula. It distinguishes an optimization property absent from ordinary thermal-entanglement threshold tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
