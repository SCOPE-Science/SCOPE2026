---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a spider with center \(c\), any set containing \(c\) power-dominates every arm. Without \(c\), a selected vertex in a touched arm propagates along that arm to the center; once the center is observed it can enter a last untouched arm exactly when at most one arm is untouched. If at least two arms are untouched the center sees at least two unobserved first vertices and forcing stalls. This proves the all-set criterion and therefore the product-sum polynomial. For fixed total arm length and \(x>0\), writing \(t=1+x\) and \(u_m=t^m-1\), the contribution depending on two arm lengths \(a,b\) of fixed sum is an affine decreasing function of \(X=t^a+t^b\). Balancing unequal parts strictly lowers \(X\) and raises the polynomial; concentrating two parts strictly raises \(X\) and lowers it. Repetition gives the unique balanced maximum and concentrated minimum. The verifier independently exhausts hundreds of small spiders and checks exact rational extremizers for all partitions through total arm length twenty.

## originality

PASS

The complete 2018 power-domination-polynomial paper computes several standard graph families but explicitly identifies trees as a future all-set counting direction; its decomposition theorem excludes the endpoint path attachment that would be needed to read a spider off directly. Later spider literature located in this run concerns the power-domination number or Mycielskian constructions rather than the full polynomial of arbitrary arm lengths. No Resultary hit or inspected primary source supplies either the product-sum spider polynomial or the all-positive-\(x\) balanced/concentrated extremal theorem.

## value

PASS

Spiders are the canonical one-branching-vertex tree family and were not covered by the defining polynomial paper's standard-family formulas. The result gives both the entire feasible-set enumerator and a sharp shape optimization valid for every positive evaluation point: balancing arms uniquely maximizes while concentrating length uniquely minimizes. That combination is a natural structural and extremal theorem, not a mere formula lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
