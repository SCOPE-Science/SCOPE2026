---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Direct differentiation gives \(H=x_3+x_1^2/(2a)\) and \(\dot H=b-x_1^2\) exactly. Boundedness makes the endpoint correction divided by time vanish, proving the long-time mean-square law and excluding negative forcing. At zero forcing, recurrence returns the continuous nonincreasing H to its initial value, forcing \(x_1\equiv0\), then the vector field forces \(x_2=x_4=0\) and constant \(x_3\). For compact invariant measures, the Lie derivatives of \(x_4,x_1,H,x_3\) give the four stated moment identities. Positive variance and zero mean force both signs; periodic-orbit RMS then gives the zero crossing and amplitude lower bound.

## originality

PASS

Best-of-knowledge originality passes. The introducing 2020 full article gives the exact sine-modified vector field, translated-attractor mechanism, and numerical bounded/chaotic regimes, but the inspected material does not state the coboundary \(\dot H=b-x_1^2\) or its recurrence and stationary-moment consequences. The closest 2016 predecessor uses a different modification and remained only abstract-accessible, so it is a named residual risk rather than negative evidence.

## value

PASS

The introducing paper relies on numerical evidence for its bounded recurrent regimes. The exact balance gives a global, parameter-selected consistency law for every bounded trajectory and compact stationary state, including a sharp forcing-sign trichotomy. This is a structural restriction on the source's principal dynamical objects rather than another simulation statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
