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

For convolution r with r_1,r_3>0, the key polynomial identity reduces to r_1 r_2 r_3-r_4 r_1^2-r_0 r_3^2 = be[r_1 r_3+(af-cd)^2]. Indeed (f r_1-d r_3)(c r_1-a r_3)=-be(af-cd)^2 by substitution; expanding its left side proves the identity. At TV <= 1/10 every atom is at least 1/10, and simultaneous reversal allows t=r_1/r_3>=1. Dividing the identity yields D=r_0/t-r_2+t r_4<=0. The TV dual test for 1<=t<=2 has weights (1/t,(t-2)/(2t),-1,(2-t)/2,t), with middle off-center terms canceling in D, sum (t+1)/2, and range t+1. Thus D >= (t+1)(1/10-TV). For t>=2, zeroing those two weights gives at TV=1/10 the lower bound (t-1)(t-2)/(10t), strict for t>2; TV<1/10 makes both regimes strictly positive. At TV=1/10 and 1<t<=2, the unique dual maximum and minimum occur at 4 and 2; equality forces r_1=r_3=1/5, impossible for t>1. At t=1 equality places surplus only at 2 and deficits only at 0,4, giving r_1=r_3=1/5, r_2=3/10 and r_0,r_4 in [1/10,1/5] summing to 3/10. Equality in the factored identity forces be=0. After a factor swap if needed, b=0, and r_1=r_3 gives a=c=1/2 and e=2/5. This yields exactly the stated interval, including endpoints, which attains the bound by direct convolution. The independent replay `python3 /workspace/branches/frozen_math_checks.py` tested 4,356 ordered pairs on the 1/10 simplex mesh, finding exactly the six ordered grid members of the family. Only the proof covers the full simplex.

## originality

PASS

The attaining family and numerical upper bound are prior (Metya–Mukherjee, Eq. 22), as is the conjectured optimum. The established distinct contribution is the universal n=3 lower bound and the proof that there are no other minimizers. No inspected Resultary or primary-literature claim gives those conclusions. This is bounded evidence, not a priority guarantee.

## value

PASS

The record resolves the first open support size of a specific Manhattan projection conjecture. It supplies the exact TV obstruction and a continuum of all optimal factorizations rather than only the previously known examples, by a useful nonnegative-coefficient identity and a sharp dual test. This is a natural complete case; nothing for n>=4 is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
