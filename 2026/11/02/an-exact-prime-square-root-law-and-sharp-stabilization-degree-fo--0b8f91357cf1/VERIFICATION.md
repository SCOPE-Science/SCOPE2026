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

Conditioned on reduction mod p, every simple root lifts exactly once, and each distinct repeated residue root yields all p lifts or zero, independently with probability 1/p by Vandermonde evaluation of free lift digits (number repeated ≤d/2). Reweighting p linear monic irreducibles and cancelling their ordinary Euler factors gives the displayed coefficient extraction. The polynomial u-numerator has degree 2p and nonzero leading term B_p(z)^p, proving the exact last jump and stabilization. At z=1 B_p=B_p′=0, B_p″=p−1; derivatives yield mean one, second factorial moment 2(1−1/p) for d≥2. Non-squarefree reductions are O(1/p) for fixed d, and falling factorial moments count permutation fixed points; rare singular fibers cause second-moment defect. Independent direct exhaustive enumeration agrees for 9 coefficient spaces (p=2,3,5), and sharp boundary checked p=2,3,5,7. d=0,1 and p=2 boundaries explicitly accounted for.

## originality

PASS

Best-of-knowledge priority: compared actual claims and implications of identical/nearby primary sources, searched semantic published record corpus and theorem aliases, and explicitly separated existing methodology/qualitative findings from the exact new result. No located prior implication dominates this final scoped theorem; genuine inaccessible and general-coverage risks remain recorded.

## value

PASS

A complete exact distribution of natural finite congruence roots at every prime and degree, with a provably sharp stabilization threshold and explicit variance; explains rare high-multiplicity singular events. Resolves a motivated prime-power analogue of finite-field root-count distributions without claiming the broader unrestricted ensemble problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
