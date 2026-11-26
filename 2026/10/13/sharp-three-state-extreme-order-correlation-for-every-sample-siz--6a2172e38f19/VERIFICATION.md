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

On {0,t,1}, each extreme is t times its indicator of being at least t plus (1-t) times its indicator of being 1. With a=3^-n and b=(2/3)^n the two minimum-threshold probabilities are b,a and the maximum ones are 1-a,1-b. The cross-covariance matrix of the threshold indicators has diagonal ab, upper entry b^2-a and lower entry a^2. This gives C(z)=ab+[(b-a)^2-a]z, z=t(1-t). Reflection gives V_U(t)=V_L(1-t); their product P in z is quadratic and positive on [0,1/4] (including both-support-merge limits, where the extremes still vary). Thus the squared correlation has derivative C*H/P^2, with H=2hP-CP' affine and h=(b-a)^2-a. Set x=b-a and r=a/x^2. Consecutive ratios are (2+1/(2^n-1))/3 for x and 3/(2+1/(2^n-1))^2 for r, so the stated bounds by their n=3 values hold, and h>0. Independent expansion gives H(0)=2ab(1-b)(h+ab)>0 and H(1/4)=r*x^5*B(r,x) with the stated B. For x<1/3 the first bracket is positive, the second is between 0 and 4x, the third is negative, and 2r^4*x^5<=x/4 using r<3/5. These yield B>=1/10+(133/100)x-3x^2>0, proving positivity everywhere by affinity. The strict increase in z gives precisely t=1/2. Evaluating C and the variance there gives R_n, including R_4=104/625. Since a/b^2=(3/4)^n tends to 0, the numerator is asymptotic to b^2 and the denominator to b, giving the stated equivalence. The proof also works at n=3; that is not necessary for the asserted n>=4 theorem.

## originality

PASS

The supported distinct result is the unique midpoint optimizer among all geometries of a uniform three-point parent for every n>=4. The exact correlation at the midpoint, and its asymptotic scale, already follow by substitution in the indexed symmetric-mass formula; do not count them independently as discoveries. The indexed mass comparisons fix the midpoint geometry, the published discrete Terrell theorem covers two draws, and the three-draw companion supplies no general-n implication in the reverse direction. The closest primary discrete-maximal-correlation full text remains inaccessible; no inspected statement implies the all-n common-geometry optimization.

## value

PASS

Three atoms are the smallest support admitting a non-affine geometry change. The all-n result resolves the corresponding extreme-rank case of a stated lattice-optimality question and proves unique optimal geometry with no search over probabilities. The exact midpoint formula is useful because the geometry theorem identifies it as the true optimum. Its exponential decay is qualitatively sharper than the general 1/n bound, but is not a separate new asymptotic for the fixed lattice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
