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

The two-site mismatch in each W off-diagonal gives phase attenuation (1-p)^2; under amplitude damping each excitation survives with weight 1-p, with the lost weight going to the vacuum. For PD the transverse generator has no support-to-support entries, so the ordered-pair SLD expression reduces to 4 tr(rho J_x^2): the pure W value is 3N-2 and the uniform excitation mixture gives N. For AD the squared transverse matrix elements on the vacuum–W and W–two-excitation edges are N/4 and (N-1)/2. With their SLD weights this gives N(1-2p)^2+2(N-1)(1-p), including when either occupied weight becomes zero. Commutation with J_z and rotation about z give F(J_u)=(1-u_z^2)F(J_x). Factoring F_AD-N as 2(1-p)(N-1-2Np) verifies the threshold and equality points, and the convex quadratic has the stated interior minimizer and positive minimum. The N=3 comparisons agree with the 2014 channel and per-qubit conventions. The proof suffices for all N. The finite-grid program artifacts/verify.py was inspected, not executed; VERIFICATION.md supplies an expected output, not an independent numerical replay.

## originality

PASS

The supported distinct result is the exact all-N matched-channel correction, including the collective optimum and the damping/shot-noise boundaries, not the general rank-deficient SLD identity or the first qualitative observation of robustness. No implication-equivalent claim was established by the closest comparisons.

## value

PASS

Corrects a specific discontinuous/zero prediction under identical channel and observable conventions. The all-size formulas separate loss of metrological enhancement from disappearance of QFI, and give the exact AD optimum axis, minimum and threshold; these are usable checks for decohered collective probes rather than merely an exercise in restating the spectral formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
