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

The claim is a deterministic all-parameter statement with an analytic proof. Key critical steps were reconstructed: (i) exact linearization and inverse mapping; (ii) at most four zeros for a nonzero degree-two trigonometric polynomial on the circle; (iii) squared affine-function second harmonics force zero planar slope; (iv) strict concavity of the square root at three distinct squared radii; and (v) the explicit gauge calculation.

The standalone standard-library checker `check_ring_geometry.py` completed 8,296 deterministic assertions, including 720 azimuthal checks of the exact gauge witness, 1,500 seeded random inverse recoveries, and 15 central-source recoveries. These numerical diagnostics do not imply the universal theorem without the analytic proof.

The stated boundary conditions are essential: strictly positive depth, known planar receiver coordinates, homogeneous wave speed, noiseless direct arrivals, and no station clock biases. The theorem guarantees identifiability but does not establish stability or an arbitrary-array minimum number of stations. No independent audit has been performed.
