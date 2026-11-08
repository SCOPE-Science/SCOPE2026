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

For every n>=3, classify cuts by (a,b) where a=0,1,2,3 in the three-vertex part and b=0..n in the other part. Their average distances are U=a(3-a)/3, V=2b(n-b)/(n(n-1)), W=[a(n-b)+b(3-a)]/(3n). In a=1 case (W−V/2)/U equals convex F_n(b)=[n(n−1)−(2n+1)b+3b²]/[2n(n−1)] with minimizing integer k=floor((n+1)/3). a=2 is its complement; a=0,3 yield nonnegative remainders. This proves W>=alpha U+V/2 for every cut and hence every L1 distance. After noncontracting normalization U,V>=2, W<=D gives D>=2alpha+1. A constructive nonnegative metric 3Delta_(1,k)+tDelta_(0,1), t=n−3k(n−k)/(n−1)>=0, has U=V=2, W=2alpha+1, giving equality and the mod-three staircase. Since alpha>0, equality in averages forces every individual same-part distance 2 and every cross distance D (rigidity). Independent exact rational checks cover all a,b n=3..60 and mixture, 7540 inequalities. Finite checks only corroborate the all-n cut proof.

## originality

PASS

The novel assertion is the sharp fixed-unit-edge K_(3,n) L1 metric distortion 2−k(2n+1−3k)/(n(n−1)) and the rigidity of all optimal distance matrices, not any weighted K_(2,n) supremum or Hilbert Banach–Mazur invariant. Searches and inspected primary/published mathematical results found no implication; conditional best-of-knowledge, not priority proof.

## value

PASS

The complete natural family K_(3,n) has a nontrivial mod-three staircase approaching 5/3; optimal cut geometry is rigid. An exact metric-embedding invariant, all-parameter classification and extremizing cut ensemble are independently useful beyond small graphs or generic estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
