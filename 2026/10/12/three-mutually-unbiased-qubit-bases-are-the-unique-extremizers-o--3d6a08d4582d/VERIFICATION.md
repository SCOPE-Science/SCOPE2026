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

The universal statement is verified analytically in RESULT.md. In particular:

1. The binary entropy reduction \(H(s)=h((1+\sqrt s)/2)\) satisfies \(H''(s)<0\) on \(0,1\), because \(x/(1-x^2)>\operatorname{artanh}x\) for \(0<x<1\).
2. For an orthonormal Bloch frame, \(s_1+s_2+s_3=1\); strict concavity fixes the maximum at \(s_1=s_2=s_3=1/3\), and concavity fixes the minimum at a simplex vertex.
3. For a nonsingular arbitrary frame, the exact sign average is \(\frac13\operatorname{tr}((AA^T)^{-1})\ge1\). Strict inequality holds away from an orthonormal frame and gives a pure state whose three absolute overlaps are all below \(1/\sqrt3\).
4. A singular frame has a common orthogonal Bloch direction and therefore cannot attain the MUB certainty ceiling.
5. Equality in the uncertainty-floor bound forces pairwise orthogonality by testing eigenstates of each measurement.

The accompanying checker confirms the closed-form constant, the sign-vector identity on deterministic frames, representative strict witnesses, and sampled MUB bounds. These computations are finite consistency checks only; they are not used to infer the universal inequalities.

Scientific limits: the result concerns three equally weighted rank-one projective measurements on a qubit and Shannon entropy. It does not establish the higher-dimensional or variance conjectures.
