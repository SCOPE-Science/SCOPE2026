---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For a tagged proposed object at time s, exact rejection requires two accepted predecessors in its exclusion neighbourhood E with different colors. A bounded Minkowski-expanded dependency set U=E+E makes probability of >=3 earlier proposals O(s^3); the two-point Poisson term has factor r^2 s^2/2, accounting for temporal order. If predecessor centers mutually conflict (measure T(E)), they must take opposite colors under both rules; otherwise random independent available colors reject with probability 1/2 while first-available priority accepts. Hence F_random=r^2 s^2 (|E|^2+T)/4+O(s^3), F_priority=r^2 s^2 T/2+O(s^3). Campbell/Poisson insertion integration yields rho_random=rt-r^3t^3(|E|^2+T)/12+O(t^4), rho_priority=rt-r^3t^3T/6+O(t^4), and the claimed difference. Independent geometry: rods E=(-sigma,sigma) have |E|^2=4sigma^2,T=3sigma^2; independently numerically integrated disk intersection and recovered T/sigma^4=pi^2-3sqrt(3)pi/4 to 35+ digits. The exact Poisson factorial expansion establishes the continuum statement; sampling and numerical quadrature are corroborative only.

## originality

PASS

Best-of-knowledge originality of the precise final mathematical claim, not novelty of standard premises or algorithms: Random-vs-priority color selection on the same Poisson deposition field is not a label swap: non-overlapping earlier objects can take different random colors but necessarily the same priority color, changing subsequent rejection. Checked relevant primary statements and Resultary semantic results. Failed searches alone are not novelty proof; risks explicitly retained.

## value

PASS

An explicit nonzero cubic coefficient decisively invalidates a stated exact total-density equivalence between randomly selected and priority-selected colors in a continuum adsorption model. The general bounded symmetric exclusion-set formula and closed rod/disk constants quantify the first physical order of discrepancy and can correct perturbative density modeling. The result is local at short time, not an all-time jamming or density-order theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
