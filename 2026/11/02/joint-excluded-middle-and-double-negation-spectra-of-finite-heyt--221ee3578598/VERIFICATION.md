---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Via the finite Birkhoff ideal representation J(P), the pseudocomplement is the downset whose principal ideals avoid I. The Boolean center is exactly unions of comparability components, giving 2^c excluded-middle solutions; every negation depends only on membership among m minima and its image equals the double-negation fixed set, giving 2^m regular elements and q/p=2^(m-c). Connected components with t minima admit precisely N>=2^t+1 ideals if t>=2 (star with upper chain realizes each), and N>=2 when t=1. Products yield the entire pair spectrum. The inequality g(a)g(b)>=2g(a+b-1), g(1)=2, g(t)=2^t+1, proves sharp positive-defect envelopes, with equality one top above k+1 minima plus isolated points; zero defect nonboolean gives at most 2/3. Independently enumerated all naturally ordered posets of sizes 1..5, counts 1,2,7,40,357, verifying formulas and relevant envelopes. Reviewed verify_joint.py which extends checks to 5231 posets through size 6; finite checks are not universal proof.

## originality

PASS

Best-of-knowledge PASS for COMPLETE simultaneously attainable (p,q) pairs, all positive-defect envelopes and equality cases. Bumpus–Kocsis already supply Boolean center/regular structure, 2/3 nonboolean bound and first 2/5 split, explicitly discussing relative satisfiability-degree classification; these are acknowledged. The exact joint spectrum is not stated or directly implied by the primary theorem passages inspected without an additional realizability/ideal-count argument.

## value

PASS

A natural pair of one-variable logical identities in a finite algebra has a full same-element joint law, complete realization spectrum and sharp defect-specific inequalities. The gap addressed is a motivated algebraic classification arising from a published general degree-of-satisfiability program, not a trivially renamed inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
