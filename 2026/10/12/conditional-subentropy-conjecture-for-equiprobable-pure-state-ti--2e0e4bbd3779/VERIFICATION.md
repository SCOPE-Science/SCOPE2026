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

The proof is analytic. The reproducibility script `verify.py` performs the following finite consistency checks:

1. It constructs explicit Fourier unit-norm tight frames for several integers \(n\ge d\ge1\) and numerically verifies
\[
\sum_x|\psi_x\rangle\langle\psi_x|=\frac nd I_d.
\]
2. It verifies that \(E_x=(d/n)|\psi_x\rangle\langle\psi_x|\) is a POVM and that its success probability is \(d/n\).
3. It evaluates \(H_n-H_d\) exactly using rational arithmetic on a grid of \((n,d)\), confirming that the gap is zero exactly for \(n=d\) and positive for \(n>d\).
4. It checks numerically that the displayed formulas for \(H_{\min}(X|B)\) and \(Q(X|B)\) differ by that exact harmonic gap.

A successful replay prints `VERIFY_OK`.

The script does not numerically prove the beta-moment identity or exhaust the continuous class of frames. Those facts are established in the proof: the simplex marginal is beta distributed, its first logarithmic moment is evaluated analytically, and the POVM bound holds for every frame satisfying the stated operator identity.
