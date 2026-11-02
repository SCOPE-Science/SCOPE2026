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

Adding the three infected equations eliminates symptom transfers and gives I-dot=(κS+δd−κ)I; subtracting ρ times S-dot gives d-dot=−(a+BI)d−ρ(1−ρ)δSI, d(0)=0, hence d≤0. Since S≤1−ε, I≤εe^(−κεt). For a>0, |d|≤ρ(1−ρ)δε/a; using z=R, S=1−z−I, the integrated exact balance ε=Z²/2+∫I dz−(δ/κ)∫d dz bounds corrections by O_a(ε√ε), proving Z/√ε→√2. At a=0 the two S_j are exponentials in R, giving curvature M2>1 and √(2/M2). Uniform exponential remaining-infection bound proves continuity in a for fixed ε. Independent high-precision final-size roots for the ρ=1/4 example confirmed M2=76/49 and the boundary amplitude.

## originality

PASS

Best-of-knowledge novelty of the exact final statement after explicit comparison with related stronger/alternate formulations; any inaccessible source is recorded as a residual risk, not assumed noncovering.

## value

PASS

A natural singular order-of-limits issue in a published epidemiological model: the exact threshold final-size amplitude differs between static heterogeneous classes and arbitrarily slow positive switching, despite pointwise continuity in switching for every positive seed. This is not merely an R0 restatement and has an explicit analytically controlled boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
