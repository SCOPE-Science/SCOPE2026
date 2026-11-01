---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

A zero-free point belongs exactly to the Sturmian minimal aperiodic subshift, so periodic points always have recognizable zero markers. Cyclic marker cuts are uniquely decomposed into finite Sturmian factors; counting length-m labeled periodic points with k distinguished markers gives P_m=m/k [z^m]F(z)^k. Summing yields zeta=1/(1-F). Rational F has an eventually recurring integer coefficient sequence and the Skolem–Mahler–Lech zero-set theorem gives eventual periodic S; the converse follows by arithmetic-geometric summation. For nonperiodic S, nonrational integer F of exact radius one invokes Pólya–Carlson, and a meromorphic continuation of zeta across any unit-circle arc would analytically continue F on a subarc. Marker-free Sturmian part precludes soficity. The statement correctly distinguishes unit-circle natural boundary from Taylor radius.

## originality

PASS

Best-of-knowledge novel part: Periodic zeta rationality versus Sturmian nonsoficity in decorated gap shifts. Generic/overlapping prior results are expressly credited and exact statement implications examined; inaccessible related papers remain explicit risks, not proof of noncoverage.

## value

PASS

The theorem completely separates finite-state recognizability and periodic-orbit regularity: every shift is nonsofic, yet zeta rationality is controlled exactly by eventual periodicity of the gap set. It also identifies an analytic boundary in the complementary case, supplying useful invariant calculations beyond the entropy of the original decorated-gap construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
