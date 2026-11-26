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

Checked the labeled count over all odd prime powers. The determinant of x and Q(x)=m(x,x) maps the six structure constants onto the four coefficients (b,2d-a,f-2c,-e), with kernel exactly Q(x)=ell(x)x; odd characteristic permits recovery of m by polarization. Thus every cubic has q^2 lifts. The zero cubic is either the zero multiplication or has an idempotent. At a rational projective root a nonzero square Q(u)=lambda u gives the idempotent u/lambda; two independent square-zero lines leave at most the mixed product spanning V^2, incompatible with perfection. A nonzero cubic with no rational root is irreducible, and each lift is perfect since a rank-one product would give D=h(x)det(x,w) with a rational linear factor. This gives q^2(q-1)(q^3-q)/3. With one rational root, either the remaining quadratic is irreducible or the cubic has a triple root. Evaluation of ell at the root is onto, so exactly q lifts make the root square-zero. In the linear-times-irreducible case, a rank-one lift would have image on the unique rational root line and quadratic factor h nonzero there, a contradiction. In the triple case choose the root as e1: e1^2=0 and the cubic is -e t^3 with e nonzero; coefficient comparison gives d=0, f=2c. The two other product columns have determinant 2c^2, so exactly one lift is excluded. The irreducible-quadratic and triple-root counts are (q+1)(q-1)(q^2-q)/2 and (q+1)(q-1) cubics, giving the other two summands after lifting. The denominator counts two independent rows of length three, and the degree-six leading coefficient of the numerator is 1/3. An invertible basis change transforms D by an invertible change of variables and a nonzero scalar, preserving its factorization type. A fresh bounded census independently reproduced the perfect totals 624 and 14880 and strata (144,72,16) and (4000,1200,96), totaling 232 and 5296. Replay for p=3,5: enumerate F_p^6, retain a table iff some pair of basis-product columns has nonzero determinant, and test Q(u) for nonzero proportionality to u on (1,t) and (0,1). For the remaining tables count the rational cubic roots on these representatives; for one root [x:y], compare the cubic to all nonzero multiples of (-ys+xt)^3 to split the last two strata. This verifies only the two sample fields; the symbolic argument establishes the general count. The frozen verifier was inspected but not executed.

## originality

PASS

The supported distinct claim is the exact all-odd-field, fixed-basis perfect idempotent-free count with its three eigenline-cubic strata. The cubic idempotent test, ambient perfect count, isomorphism classification/counting, and existence or probability results on evolution-algebra subclasses are not credited as new. The strongest actual same-day match counts the ambient set by a different invariant and does not imply the filtered census. This is a bounded best-of-knowledge decision, not a priority claim.

## value

PASS

Perfect commutative products on a two-dimensional space form a natural finite sample space, and rational nonzero idempotent existence is a basic structural distinction. The count is complete on that sample space and explains which eigenline degeneracies can remove all rational idempotents without losing perfection, including the triple-root rank-one exclusion. Its exact proportions and strata would be useful in comparing idempotent behavior across finite-field algebra families; neither the cubic test for a specified algebra nor an existence example answers this quantitative question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
