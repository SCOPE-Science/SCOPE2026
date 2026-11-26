---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The exact block loss difference is half the squared head Gram residual plus ||YZ^T||_F^2-||Z||_F^2+||ZZ^T||_F^2/2. The gradient vanishes at each collapsed orientation, and k+1 columns suffice for exact fit by disjoint supports. If the minimum head entry is strictly above 1/sqrt(m), it remains so in a neighborhood; nonnegative rows z give ||Yz^T||_2^2 >= m(min Y_ij)^2||z||_2^2. This proves local optimality for all feasible perturbations there, with nonstrictness from nearby positive unit orientations. Below threshold, inserting one entry t in a minimizing column of one tail row gives a negative quadratic coefficient and a positive t^4/2; head scaling also supplies an increasing direction. At equality the displayed Hessian coefficient is nonnegative on the full tangent cone (head arbitrary, tail nonnegative, gradient zero). Reducing the minimizing squared orientation coordinate by t^2/m and transferring that mass to another coordinate keeps the head Gram fixed; the same tail insertion now gives exactly -t^4/2 at distance t+O(t^3). The critical construction needs r>=2; the stronger r>=k+1 hypothesis ensures zero global loss. The balanced vector uniquely maximizes the minimum coordinate, so a local minimum in this family exists exactly for m>r. The source's exact-rational checks are finite; its script was inspected, not executed.

## originality

PASS

Credit Zhang for the same target and balanced spurious minimum, as the frozen original does. The supported distinct claim is the sharp classification over the whole positive unit orientation family, including opposite local behavior at an identical Gram matrix and the second-order stationary but quartically descending boundary.

## value

PASS

The example isolates a genuine ambiguity in judging constrained factor landscapes from fitted Gram matrices or first derivatives alone. A sharp threshold on the full positive orientation fiber and explicit fourth-order descent at a second-order stationary point convey more than another isolated spurious minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
