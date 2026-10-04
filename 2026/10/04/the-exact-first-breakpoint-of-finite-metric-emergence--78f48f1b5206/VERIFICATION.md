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

The theorem was checked from the stated definitions and cited source results, with no numerical or finite-exhaustion step.

For correctness, the decisive calculation is the exact \(N-1\)-prototype distortion. Any set of at most \(N-1\) centers forces two of the \(N\) empirical-limit atoms to use the same center. If their weights are \(p_i\le p_j\), their two distortion contributions are at least \(p_i d_W(\nu_i,\nu_j)\) by the triangle inequality. Minimizing over pairs gives the global lower bound \(\Delta\). Deleting the smaller-weight atom from a pair attaining \(\Delta\) gives an explicit center set with distortion at most \(\Delta\), hence equality.

The argument was also checked for boundary cases. The theorem assumes \(N\ge2\). Every basin weight is positive, since a zero-weight basin could be removed without affecting the empirical-limit law and would contradict the minimal finite small-scale value. Distinctness of the finitely many empirical limits makes \(\Delta>0\). Because the emergence definition requires distortion strictly below \(\varepsilon\), the value remains \(N\) at \(\varepsilon=\Delta\).

No assertion is made about the exact emergence value after the first drop, nor about \(k\le N-2\) quantization errors. Those are outside the proved scope.
