---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The stated Radau IIA tableau yields R(z)=(6−2z)/(z²+4z+6) on negative real arguments of the usual RK stability function, written here as positive diffusion parameter z. The four invariant subspaces are the constants, the two within-part contrasts, and the contrast of part means, with eigenvalues 0,q,p,n. The off-diagonal entry across parts is (1−R(nh))/n>0; within the p-part it is h²q[h²qn+6hp+12hq+18]/[D(qh)D(nh)] with D(z)=z²+4z+6, also positive (swap p,q for the other block). Clearing these positive denominators on the diagonal gives the two stated quartics. The global scalar minimum (5−3√3)/2 and constant projection diagonal 1/n give a positive diagonal lower bound for n≤11. At h=8/q the first diagonal is strictly negative for n≥12: the denominator is positive and the sign is minus that of a quadratic with leading coefficient 15 and discriminant −128(25n²+480n−8712)<0. Interchanging the parts supplies the other witness. The quartic coefficient signs are +,−,arbitrary,+,+, so there are at most two positive roots counted with multiplicity; positivity at 0 and infinity and the strictly negative witness force two simple roots. Independent symbolic checks reproduced the quartics, off-diagonal factorization, and witness; exact signs at the supplied rational brackets establish the disjoint and overlapping examples. At h=0 the endpoint is the identity.

## originality

PASS

The distinct claim is the all-step entrywise classification for unequal parts, including the two potentially disjoint negative intervals. The closest same-day balanced result shares the order-12 threshold and off-diagonal behavior in its own domain but has a single diagonal class. A broader multipartite threshold result dated later covers only part of this claim. No inspected earlier or same-day statement establishes equivalently the full unequal classification.

## value

PASS

Nonnegative endpoint values are required for preserving nonnegative inputs in diffusion. The exact threshold and two-quartic criterion decide admissibility for every unbalanced profile and step, not just in a safe small-step regime. Three separated admissible windows on K_{2,10} are a structural phenomenon absent with one diagonal class, and the contrasting K_{5,7} example shows it is not universal once imbalance is permitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
