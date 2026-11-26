---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Antipodal invariance gives a fair direction sign conditional on the entire unoriented vector (line and radius); independence makes the conditional joint sign law a product, including after the almost surely strict projective sort. In a generic half-turn sweep, each point changes membership once, giving counts C_j=(n+s)/2-S_j, with the other half-turn giving n-C_j. A boundary with one point places each of the open/closed counts among the two adjacent generic counts, and cannot lower the minimum below the generic one. Thus the event at threshold r is exactly |s-2S_j|≤n-2r for all j. For |s|≤n-2r of the correct parity, the confinement becomes a killed walk on sites 1,…,h-1 with endpoints a=(h-s)/2, b=(h+s)/2 and h=n-2r+2. Odd image extension at 0 and h satisfies the walk recurrence with zero boundary and the correct initial delta, so the images b+2kh and -b+2kh give binomial indices (n+s)/2+kh and r-1+kh (up to reindexing). The allowed endpoints' first indices span all but the r-1 residue class, while each of the h-1 second image sums subtracts that same class. Dividing the resulting 2^n minus h times the residue sum by 2^n proves the claim. Generic antipodal counts sum to n, giving zero past floor(n/2); r≤0 is certain. At r=1 the remaining binomials are the two extremes, and at r=2, n≥5, they have indices 1 and n-1. No assumption of identical or uniform underlying laws, or of independent order statistics, is used. For planar rows in general position, any two active rows span, so testing the generic active sets suffices for the stated zero-bias application.

## originality

PASS

The Wendel first-depth law and Yuan's twofold uniform semicircle law are exact overlaps and are not credited as new. A standard two-barrier reflection kernel is also a proof ingredient, not a new kernel. The checked evidence does not supply the endpoint-summed all-depth identity or its heterogeneous distribution-free consequence; the pass is for that distinct family, not for all associated coverage/ReLU ingredients.

## value

PASS

Halfspace depth is a natural random geometric invariant and all threshold probabilities describe the robustness of center containment rather than one event. The conditional sign sweep and endpoint sum obtain a single binomial-residue formula at every threshold, even under heterogeneous direction laws; this goes beyond using a textbook onefold coverage formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
