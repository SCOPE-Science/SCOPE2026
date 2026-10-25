---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Folding the min(x,t) kernel of JJ* about x=1/2 yields even/odd Green diagonal blocks and rank-one coupling; the eigenvalue boundary equations reduce to cos(t)-a cos(at)=0, with a=1 limit cos(t)-t sin(t). Real-rootedness follows from differentiation of sin(t)-sin(at)=2cos((1+a)t/2)sin((1-a)t/2) in Laguerre-Pólya; no zero at 0 and root simplicity follows squaring the two simultaneous equations (exceptional +/-1 checked separately). Hadamard order-one factorization with D(0)=1 gives the Fredholm determinant, not just secular zeros. Comparing quadratic and quartic coefficients yields only {a,b}={0,-1} as a distinct isospectral pair. The finite-rank correction to two scalar Green blocks gives Weyl counting constant max(1,|a|)/π and Schatten thresholds. Independently discretized J and output reflection for 6 real parameters, checking Hilbert-Schmidt traces and products at two z each; inspected verify_reflection.py. Numerical tests cannot establish the asymptotic result alone.

## originality

PASS

Fresh comparison of exact statements and implications, with inspected primary mathematical sources, bounded Resultary searching, and recorded inaccessible potentially relevant sources. Knowledge of J singular numbers or generic 1/j asymptotic does not determine the exact real-parameter Fredholm entire function, coefficient-based ambiguity classification or flat weak-Schatten plateau. Radial symmetry of rank-one corrections is not an operator identity for (I+aR)J.

## value

PASS

An exactly solvable nonnormal reflected-Volterra family is a natural model for mixed triangular-Hankel integral operators. The unique nontrivial isospectral pair shows inverse nonidentifiability despite spectral completeness, and the flat weak-Schatten coefficient identifies information lost by leading asymptotics. These are structurally meaningful beyond a textbook norm computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
