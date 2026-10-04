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

The proof was checked symbolically against the finite-report definitions of the cited source. The essential identities are:

1. On \(s\in[W_{q-1},W_q]\), \(\Psi_h(s)=D_{q-1}+d_q(s-W_{q-1})\).
2. Therefore the AI-first information-cost point at \(s\) lies exactly on the segment between adjacent breakpoint modes.
3. Adding idle mass converts the pool inequality into a convex-combination identity, so the minimum is the lower convex envelope evaluated at \(T/N\).
4. Every mode has per-item information at most \(J\), and the direct-human mode attains \(J\).
5. Concavity with \(\Psi_h(0)=0\) makes \(\Psi_h(s)/s\) nonincreasing, yielding the stated iff threshold from its right limit \(d_1\).
6. A perspective of a piecewise-affine hull is affine in \(N\) between transformed hull breakpoints, so the outer maximum is piecewise affine with additional breakpoints only at crossings.

`verify.py` performs exact-rational checks on a three-report instance and on a two-direction outer benchmark. It verifies the original perspective calculation and hull calculation agree at a non-breakpoint escalation rate, checks the two-mode interpolation, verifies full-escalation domination and the selective-value threshold, and compares the finite-candidate outer minimizer with direct integer enumeration.

Limits: the executable checks representative finite instances only. They do not establish the universal theorem by enumeration; the universal argument is the proof in `RESULT.md`. No independent audit has been performed.
