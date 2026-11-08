---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For positive homogeneous valuations of weights (1,1,1,rho), each directed individual inter-EF1 condition is x_i >= x_j−1 because each value per good is a positive constant. Thus all counts differ by at most one: m=4t+r has r large t+1 counts. Item-based realized-center EF1 is exactly a+b>=c+d−1 and c+rho*d>=a+b−1 (including empty centers). Let u be count of large bundles in A: 2u>=r−1, so least u=0 for r0,1 and u=1 for r2,3, which maximizes centre-B realized slack. Assign any large B bundle first to B1 (unit valuer); four extremal vectors r0(t,t,t,t), r1(t,t,t+1,t), r2(t+1,t,t+1,t), r3(t+1,t,t+1,t+1) have centre-B slack respectively 1−t(1−rho), 2−t(1−rho), 1−t(1−rho), 1−t+rho(t+1). These are necessary and sufficient for every m≥1; hence r0,2: t rho≥t−1; r1: t rho≥t−2; r3: (t+1)rho≥t−1. All m<=7 feasible, m8 impossible for rho<1/2, m9 always feasible, m10 again impossible for rho<1/2. Direct exhaustive count-vector enumeration m=1..16 across 60 rational rho settings reproduced the threshold formula; universal claim follows from the integer proof.

## originality

PASS

PASS qualified: Deligkas et al arXiv:2607.27743 Theorem 11 studies exactly two 2-agent centres with three unit-valuers and one epsilon-valued agent, establishing a 12-good impossibility. That already proves nonexistence in this model, but not first failure at 8, reentrance at 9 or the exact all-m coefficient-residue law. Lucet et al address matroid-rank preferences and a different valuation convention. More general bivalued frameworks might subsume some cases but no directly implying theorem was identified.

## value

PASS

The same natural toy family used for an existing delegated-fairness impossibility theorem has a sharp residue-dependent feasibility classification over every item count and exceptional ratio. The first obstruction at eight and nonmonotonic recovery at nine are mathematically motivated, checkable and strictly more informative than a known twelve-good witness. Value is limited to this specific homogeneous-outlier family, which is stated honestly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
