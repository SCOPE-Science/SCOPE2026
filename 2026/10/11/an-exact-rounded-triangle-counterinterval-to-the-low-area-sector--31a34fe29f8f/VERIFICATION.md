---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For sectors with 1<=theta<theta_star<pi/3, diameter equals radius, so at diameter 1: perimeter 2+theta, area theta/2. For K_t=tT+(1-t)B/2, Steiner and diameter addition give D=1, p=pi-(pi-3)t, a=pi/4+(3-pi)t/2+(pi+sqrt(3)-6)t^2/4. Exact symbolic differentiation confirms q=a/p^2 has q′=t(pi*sqrt(3)-9)/(2p^3)<0. At t_s=(pi-2-theta)/(pi-3), the area defect simplifies EXACTLY to g=[4-pi-(6-pi-sqrt(3))t_s^2]/4, increasing with theta, negative at theta=1 and zero only at theta_star. Hence q(t_s)<q_sector<q(0) for every theta in [1,theta_star), so a unique t_theta in (0,t_s) has equal q. Since p decreases in t, p(t_theta)>2+theta, and scaling to any common P yields equal area and strictly smaller diameter. All domain conditions t_s in (0,1], theta_star<pi/3 and endpoint strictness were checked. The proof holds on a continuum by elementary monotonicity/IVT; finite numerical samples are only corroboration.

## originality

PASS

Best-of-knowledge: the exact rounded-triangle counterinterval and its explicit transition angle were not found independently. The 2025 (P,A,D) diagram theory already gives abstract continuity and numerical lower-envelope evidence, so qualitative nonoptimality near theta=1 may not be new. What remains noncovered is the canonical Steiner rounded-equilateral witness for every theta in the explicit nontrivial interval with unique equal-q parameter and exact threshold for this mechanism. The inspected 2008 theorem solves the upper-area branch, and the neighboring published disk-triangle Steiner theorem fixes a different width/offset problem. Inaccessible Nandakumar full text and Kubota original remain documented risks.

## value

PASS

The fixed-area fixed-perimeter minimum-diameter question is a natural, published geometric extremal problem. A rigorous interval of genuine equal-P equal-A strictly lower-diameter counterexamples is mathematically substantive, especially because the modern exact lower boundary for normalized perimeter above 3 is unavailable. The exact threshold and canonical rounded-equilateral family are reproducible, while a narrow affected area interval is acceptable for a motivated counterexample. The result does not solve the minimization problem or claim its interval is globally maximal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
