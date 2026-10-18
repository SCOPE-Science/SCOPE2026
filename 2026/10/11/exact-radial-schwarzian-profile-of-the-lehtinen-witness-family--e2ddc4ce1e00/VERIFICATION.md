---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Source formula yields weighted Schwarzian −[A w(z)²+b conjugate(z)w(z)+3 conjugate(z)²/2], with A=(alpha²−1)/2>0, b=alpha−1>0 and w=(1−r²)/(1−z). Reverse triangle gives |w|≤1+r and triangle inequality the circle bound; at z=r all three terms align exactly, so upper bound achieved. If r>0, strict |1−z|>1−r unless z=r yields unique maximizer. Profile derivative 2A(1+r)+b(1+2r)+3r positive, limit norm 4A+2b+3/2. Deficit factors (1−r)[A(3+r)+b(2+r)+3(1+r)/2]. Near-max sequence must have r→1 and |w|→2, so (1−r)/|1−z|→1 implies angular direction→0 and z→1. alpha=1 endpoint deliberately excluded from angular uniqueness; nonattainment for alpha>1 clear.

## originality

PASS

Read original Efraimidis–Hernández 2026 full open-access text with Schwarzian formula and their bound. They prove harmonic inner-radius upper bound and state norm ≤2(alpha²−1)+2(alpha−1)+3/2, not the sharp circlewise equality, uniqueness of radial maximizer, or all extremizing boundary sequences. Wang–Liu–Rasila–Sun original witness establishes noninjectivity but not this later Schwarzian radius calibration. Search results contain only present mirror for exact polynomial/radial claim. No stronger same-object published profile identified.

## value

PASS

Calibrates sharpness of a canonical noninjective counterexample used to bound harmonic univalence inner radius, identifies unique asymptotic boundary concentration and exact linear first-order excess near alpha=1. The exact witness norm and location are natural invariants, though they do not settle the conjectured lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
