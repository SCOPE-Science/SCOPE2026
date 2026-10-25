---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

On 9th roots only the cubic convolution degrees 0 and 9 alias, giving exact sum of squared convolution coefficients plus 2Re(c0³ conj(c3³)). Taking coefficient moduli bounds every cyclic convolution bin. The aperiodic autocorrelation cubic expression is S³+6S∑R_i²+6R1²R2+12R1R2R3; the period-nine alias adds 2R3³. At fixed energy S, pair-RMS reflection (A,B,B,A) increases R1,R2,R3 via Cauchy–Schwarz/AM–GM, proving global reduction, not guessed symmetry. Its F9(t) has derivative -3t(5t^5+20t^4+5t^3-30t-19)/[2(1+t²)^4], whose unique positive root follows Descartes and signs; boundary values below an interior trial. Equality in the autocorrelations enforces symmetric positive magnitudes; ordinary convolution coefficient phase equality imposes affine phases, and the sole alias restricts η^9=1. Independent symbolic polynomial convolution and differentiation exactly reproduced F9 and derivative; 2,000 random complex coefficient tests stayed below K9 and all nine claimed phases saturated by direct ninth-root sums. These finite tests do not prove the universal inequality.

## originality

PASS

The complete nearest published four-frequency sixth-moment theorem solves continuous-circle/no-alias case, with distinct root, constant 9.203526 and a continuous equality phase circle. The ninth cyclic group introduces a new collision, changes the norm constant, and locks equality to nine points. Other published four-frequency fourth-moment and three-frequency sixth-moment theorems change a structural parameter and do not imply this exact four-frequency ninth-grid sixth moment as a corollary. Standard majorant and symmetrization are prior, but the exact alias threshold and global equality classification survive.

## value

PASS

Ninth roots are the first sampling period where cubic sums of a four-mode polynomial collide (degrees 0 and 9), making the case structurally singled out rather than an arbitrary tiny grid. Sharp constant and all equality phases provide an exact first-alias test for finite Fourier restriction/norm geometry and expose discrete torsion-induced rigidity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
