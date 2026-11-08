---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

A fresh independently implemented C++ exact base-three enumerator traversed all 3^12=531441 states from the actual graph edge list, verified F^9=F^6 for each state, and reconstructed the 7-column period1/period3 entrance table and 60 extremal states. A separate independent Python phase-condition enumerator found 145200 3-periodic states, 48400 temporal orbits, and used the complete 120 automorphisms to recover 473 classes with size spectrum {5:2,20:4,30:11,40:10,60:99,120:347}. These enumerations cover the COMPLETE finite space, not a sample. The all-rotating successor-neighbor phase characterization and full automorphism order bound were checked in the mathematical package.

## originality

PASS

Qualitative fixation and 3-cycle activity were already understood through circulation criteria; the best-knowledge contribution is the sharp labelled all-state arithmetic and complete 473-class geometric quotient, not existence of three-color excitation or its general period restriction.

## value

PASS

The icosahedron is a canonical minimal 5-regular Platonic graph. Exact transient cutoffs, cycle basins, and full spatial symmetry quotient give natural graph-specific nonlinear dynamical invariants; all 60 longest transient states forming one geometric orbit is a meaningful structural feature beyond qualitative periodicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
