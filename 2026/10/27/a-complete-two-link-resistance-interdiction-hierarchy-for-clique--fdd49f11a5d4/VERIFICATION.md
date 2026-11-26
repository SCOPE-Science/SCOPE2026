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

Connectivity follows because each K_(m+1) is m-edge-connected. At the common cut vertex, resistances add in series across blades, so each blade has the local resistance sum plus c=(t−1)m times its hub-to-leaf sum, with no cross term between different blades. On the blade's constant-orthogonal space put b=m+1, M=b−2, W=bI+cL(star). For deleted-edge incidence matrix B, inversion of bI−BB^T and tracing against W yields the frozen loss. Write H=B^TWB. The singleton loss is H_ii/(bM); for an adjacent pair orient to make the incidence inner product +1, giving the interaction (H_11+H_22+2M H_12)/(bM(M²−1)). The star diagonal forms are m+3 (spoke) and 2 (rim), and oriented adjacent cross forms are m+2,1,1 for SS,SR,RR. These produce the quoted s,r and all three positive increments. Disjoint incidences give exact additivity within the blade, as does the series decomposition across blades even when the global hub is shared. Exhaustion is by edge type, common blade and common endpoint. In the order comparisons SR_+−SS_0 has the sign of 2−m(m−3)(t−1); SR_0−RR_+ has numerator 3t−11 for m=3 and is positive from the minimum 14 at (4,2) for m≥4. The comparison SS_0−RR_+ needed at m=3,t=2,3 simplifies to 2t−10/3>0. Other adjacent comparisons follow from s−r=m(t−1)/(m−1)>0, the positive increments, and SS_+−SR_+=(m+1)(t−1)/(m−2)>0. Counting same-blade spoke pairs, incident spoke–rim pairs and different-blade spoke pairs gives the stated multiplicities. Independent replay: python3 /workspace/review-evidence/check_frozen_math.py 3 tested all 685 edge pairs and all singletons in four parameter cases by exact grounded inverses and direct voltage-drop sums, including all regime boundaries; the unbounded ordering follows from the analytic inequalities. Frozen verification's 57 comparisons are recorded evidence, not the independent run.

## originality

PASS

Credit general complete-graph edge-defect formulas, ordinary windmill resistance, and resistance-based assessment. The distinct supported contribution is the exact all-pair hierarchy with its sharp changes of rank and multiplicities for equal unit-conductance blades. The closest specialized windmill paper remains an access risk, not negative evidence. Comparison does not claim priority for the inverse method or universal priority for the ranking.

## value

PASS

This resolves a motivated two-edge sensitivity question for a canonical cut-vertex graph family with explicit ranks and multiplicities. The runner-up switch by blade size and the distinction between local adjacency and sharing only the global hub are structural information not read off from the isolated-edge ranking. The result is about unweighted finite graphs; it does not model actual power grids or distinguish dynamics under failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
