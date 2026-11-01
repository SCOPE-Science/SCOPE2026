---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For each even m>=4, K=I+11^T maps any balanced sign vector s to itself. With z±=π1±δs, h sinδ=2δ (unique 0<δ<π for h>2) gives exact prime-two exchange. Both Jacobians are I−h cosδ K, with eigenvalues 1−h cosδ (m−1 times) and 1−(m+1)h cosδ. Squared two-return eigenvalues are <1 exactly for δ_m<δ<π/2, where (m+1)δ_m cotδ_m=1, equivalently h_m<h<π. At h_m or π a unit multiplier precludes strict linear attraction; for h>π the branch repels. Signs modulo s↔−s count C(m,m/2)/2 distinct cycles, with disjoint local basins. IFT continues each hyperbolic cycle for small positive edge-weight perturbations at fixed m,h. From δ_m=π/2−2/[π(m+1)]+O(m^-2) one obtains π−h_m=4/[π(m+1)]+O(m^-2). Not all cycles are classified.

## originality

PASS

The motivating Huygens paper establishes the phase map and small-step dynamics; its accessible theorem scope does not imply exponentially many stable two-cycles for all even-leaf stars in h_m<h<π. Published related phase-network findings concern distinct couplings or local asymptotics. This is best-of-knowledge, qualified by inability to inspect all antecedent pages.

## value

PASS

A shared sharp stability window supporting C(m,m/2)/2 distinct attracting period-two star-network states is a motivated dynamical phenomenon, exponentially growing in leaf count and robust to individual edge-weight perturbations. It is not merely a finite numerical observation or renaming of the small-step theorem. The result establishes this explicit family, not global enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
