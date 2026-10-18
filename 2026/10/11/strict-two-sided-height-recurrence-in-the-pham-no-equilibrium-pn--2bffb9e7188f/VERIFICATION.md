---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Frozen RESULT.md blob 422445f5aadf6a21f7a134746c2c1fabe1a19788 uses the exact Pham PNE1 vector field (x'=y, y'=−x+yz, z'=−x−axy−bxz+c). Direct differentiation E=(x²+y²)/2 gives E'=y²z. Generator invariance on compact support forces ∫y²z=0. If its positive and negative weighted parts both vanish, y²|z|=0 continuously on invariant support. If z is nonzero on any interval then y=0 there, hence x=0 and uniqueness extends x=y=0, while z'=c produces an unbounded complete orbit, impossible. Otherwise z≡0, x,y execute a harmonic circle but z'=0 imposes x(1+ay)=c for all time; its nonzero constant −c Fourier coefficient makes this impossible for c≠0. Therefore both weighted half-space integrals are equal and strictly positive for every compactly supported invariant μ. Every nonempty compact invariant set carries a time-average invariant measure, so it meets both z signs; periodic continuity forces plane crossings. Recomputed E' exactly and checked the harmonic constraint, not the numerical chaos evidence. At c=0 an equilibrium line defeats strictness; no recurrence existence is asserted.

## originality

PASS

PASS on bounded comparison: source-defining PNE1 paper describes dynamics numerically but does not in the directly inspected text establish a universal invariant-measure sign-straddling theorem. Structurally similar published Resultary balance for an equilibrium-line flow has a different third equation and does not imply the strict c≠0 law.

## value

PASS

For a named naturally studied no-equilibrium quadratic chaotic-flow family, the explicit strict two-sided weighted height law excludes every compact invariant set trapped on one side of z=0 for every real a,b and nonzero c. It replaces sample-orbit plots with a universal recurrence barrier and identifies exactly why the no-equilibrium perturbation matters; the c=0 boundary is a motivated failure mode.

The dated certificate retains the supplied scientific assessment, sources and limitations.
