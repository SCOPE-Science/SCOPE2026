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

Final file /workspace/repairs/1/RESULT.md. The frozen proof at line 118 incorrectly gives coefficient 2 directly after the first odd spike when t=3 and r≥6. The shifted block contributes 1 there, so the coefficient is 3; it is still strictly between the two coefficients 4 in the sense of a dip in the sequence. The repair gives the exact coefficients and spells out the Gorenstein chart cases. Weights are unordered, so take a≤b. The Gorenstein condition gives positive integral Reid–Tai ages in both weight charts; the repeated unit weights with r≥2 rule out pseudoreflections. With x=Q/a≥y=Q/b, integrality and r>0 give y≥2, x≥3. An age-one element exists at y=2 or x=y=3; when y>2 and x>3, the strict inequalities r>d and r+d>a, with d=b−a, exclude age one as detailed in the repair, including d=0 and weight-one charts. The converse family has x=t+2,y=2, or x=y=3. The Ehrhart floor exponents reduce to ceil(m/2)−floor(m/(t+2)); the even period t+2 adds t/2, the odd period 2(t+2) adds t. In the odd base block the two length-(t+2) ranges abut at degree (t+1)/2, giving spike 4 and interior coefficients 2 elsewhere; the equal case writes m=3j+s. These facts give all the stated products. For odd t≥3 the two spikes and the corrected dip give failure iff there are ≥2 blocks. For even t=2c≥6, one block is unimodal; two have a single central overlap of heights 3,3, and three or more give 3,3,2,3 at c,c+1,c+2,2c. Direct block overlap gives a single rise/plateau/fall for t=1,2,4 and for (r,r). Thus all thresholds are unchanged. The supplied script is finite exact regression (coefficient comparison to r=400, age scan to r=60); no fresh replay or formal certification is claimed.

## originality

PASS

PASS applies to the exact unimodality classification, not to the parametrization or factorizations credited as inputs in the repaired file. The strongest distinct exact-scope comparator, ecdefed7e8e0, contains the same three products, but its theorem classifies unit-circle root behavior, not the sharp coefficient thresholds. Its reference to a previously recorded unimodality classification does not independently state those thresholds or settle the priority of the two same-day records. The overlaps are substantial and expressly retained in the repaired attribution.

## value

PASS

Unimodality is a standard question for reflexive simplex h* and the canonical/non-terminal locus is a geometrically defined full boundary, not an arbitrary cutoff. The threshold determines exactly where this locus gives infinite non-unimodal families and separates them from the unimodal cases. The repaired contribution is the classification across all boundary parameters, not the already overlapping geometric parametrization or product formulas in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
