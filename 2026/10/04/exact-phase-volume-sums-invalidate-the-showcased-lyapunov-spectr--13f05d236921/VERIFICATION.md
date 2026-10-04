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

The exact checker is `verify.py`. It evaluates the uncontrolled trace \(c-a-b\), the controlled trace \(c-a-b+r_1+r_2+r_3+r_4\), and the sums of all five printed exponent vectors using exact decimal arithmetic. A successful replay ends with `VERIFY_OK`.

The supporting numerical script `qr_replay.py` integrates the state and variational equations for the uncontrolled parameter choice \(a=40\), \(b=2\), \(c=22\), \(e=1/2\), starting from \((1,1,1,1)\). It uses fourth-order Runge–Kutta with step \(0.002\), an \(80\)-time-unit burn-in, a \(100\)-time-unit accumulation window, and QR orthogonalization every \(0.02\) time units. The replay obtained finite-time rates approximately \((1.0824255160,0.0927137433,-0.0209768592,-21.1541613287)\), summing to \(-19.9999989286\). This numerical run is not an infinite-time certificate and is not used to prove the contradiction.

The exact proof limit is: any true finite-time singular-value exponent sum, and any asymptotic Lyapunov spectrum when defined, must satisfy the trace identity. The verification does not establish the uniqueness of an attractor, does not prove or disprove hyperchaos, and does not certify the source's bifurcation calculations.
