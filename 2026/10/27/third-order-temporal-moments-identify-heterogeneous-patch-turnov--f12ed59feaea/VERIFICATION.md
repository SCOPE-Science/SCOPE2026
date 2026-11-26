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

Conditioning on the middle time and using Y_i^2=c_i+(1-2*pi_i)Y_i for each centered Bernoulli Y_i gives c_i(1-2*pi_i)z_i^(2j); independence cancels every term with a singleton site index. This also gives the correct coincident-time moment at j=0. H_0 and H_1 factor through the same invertible Vandermonde matrix, and positive c_i give nonsingular H_0; the pencil recovers the distinct z_i with H_1 using at most C_(2n-1). The covariance and squared-node Vandermonde systems recover the positive c_i and signed d_i, respectively, hence pi_i and both rates for each z_i (known h>0). In the witness, complementing each pi_i leaves c_i=3/16 and the mean invariant and reverses T_1=(3/32)(1/4-1/9)=5/384, without permuting the fixed distinct turnover rates. Identical added patches with new rates preserve the obstruction. For n=1 the mean fixes pi_1 and C_1/C_0 fixes z_1. The mean is supplied and defines centering, not claimed minimal as a separate datum. The exact-rational finite forward examples and alias were independently checked by `python3 /workspace/branches/check_patch_examples.py`; the two certificate annihilators are the products of the stated linear factors. The universal proof is algebraic, not a finite-trajectory inference or numerical conditioning result.

## originality

PASS

The distinct contribution supported here is the explicit uniform finite design and rate reconstruction at arbitrary site count with distinct turnovers. The earlier two-patch blind spot, its sharp third-order resolution, and the resulting general lower bound by padding must not be credited as new; neither is the Prony step.

## value

PASS

A uniform exact finite experiment design for any prescribed number of independent heterogeneous sites is useful when site labels are unavailable: it specifies how many lags, how they should be arranged, and how to associate signed occupancy orientation with each estimated decay in the exact model. The known two-patch obstruction motivates the design but does not solve the multi-component assignment. This is a structural identifiability result, not a new general interpolation algorithm or a stability claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
