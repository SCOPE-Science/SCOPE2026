---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The edge relation is w_j/w_i=a_ij/a_ji, whose cycle products give necessity and whose path products give a gauge component by component. The Stratonovich rule cancels the two force terms in H_W exactly, and the Itô corrections also agree. Equivalently the change (x,v)↦(W^(1/2)x,W^(1/2)v) makes the stiffness symmetric, replaces each thermostatted temperature by w_iT_i and replaces injected heat Q_i by w_iQ_i. At calibration the thermostat generators are symmetric for the Gibbs density; the divergence-free Hamiltonian part is skew and changes sign under velocity reversal. For the chain, energy dissipation puts every drift eigenvalue in the closed left half-plane. A nonzero imaginary-axis eigenmode has zero velocity and position at the frictional endpoint; the nonzero tridiagonal edge entries propagate zero through the chain. Zero frequency is excluded by confining stiffness. Hurwitz drift plus the positive-definite Gibbs covariance gives a positive noise Gramian via the Lyapunov integral, and mixing follows. Stationary energies at the two ends of the observation interval therefore become independent Gamma(N,Θ), giving the characteristic function stated. Conversely, with positive friction at every site, comparing reversed-adjoint velocity derivatives forces the velocity Maxwellian with local temperatures; stationarity then gives ∇log f=−diag(1/T_i)Φx, requiring symmetry and positive definiteness for a normalizable density. The all-site necessity is not asserted for partially thermostatted graphs. /workspace/review_checks/check_4.py independently checks an unequal-mass, unequal-coupling chain with endpoint-only noise using its stationary Lyapunov residual and the Gaussian two-time quadratic-form determinant. This is finite corroboration, not a proof for arbitrary graph or time.

## originality

PASS

Pass for the explicit arbitrary-length endpoint-chain heat coboundary, including off-calibration, and the order-one stationary limit of that identified heat combination at calibration. The cycle condition is classical. The all-site thermal edge condition is substantially anticipated in the earlier overdamped result, and reciprocal scaling and heat-increment rescaling already occur for a pair, including an underdamped extension. Neither those passages nor the same-chain collective SCGF establish the compared arbitrary-length endpoint-bath theorem. The generic reciprocal energy-balance and equilibrium Gamma factors are not independently new.

## value

PASS

The directed edge products select a concrete measured heat combination whose finite-time fluctuations are a boundary energy even at unequal gauge temperatures. At calibration its exact stationary law identifies the fluctuations invisible to the same model's extensive SCGF. This makes the order-one channel usable without reconstructing the entire joint heat law and distinguishes it from vanishing average current or a two-particle mapping alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
