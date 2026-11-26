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

Write f(x)=h(x²), h(t)=(t+1)t²Q(t+t⁻¹), with Q(u)=u²+(a-1)u+(b-a-1). Because h(0)=1, the only failures are repeated Q roots, ramification at t=±1, or overlap with t=-1. In characteristic 3, Q(2)=a+b+1, Q(-2)=b-1, and disc(Q)=a²-a+2-b. A repeated root lowers the genus of the double-cover normalization from four. The two displayed involutions generate a group of order eight: the square of their product is the hyperelliptic involution. On the indicated basis, the coefficient matrix consists of two 2-by-2 blocks after grouping odd and even indices; both block determinants are a(b-1). At a=0 there are two rank-one blocks, each product of its Frobenius twists retaining rank one iff b is nonzero; at b=0 both blocks square to zero. This establishes the stable ranks and a-numbers, not just ordinary matrix ranks. For rank two, a slope other than 1/2 among the four residual slopes would require denominator at least three and its complementary slope, together at least six slopes. For the origin, independently of the Hermitian argument, on F_81 the image of the tenth-power map on nonzero elements is F_9^× and each fiber has ten elements. All nonzero F_9 elements are squares in F_81, so there are ten x values with x^10+1=0, two y values at every other x, and two points at infinity. Thus #C(F_81)=154, the maximal count, giving all Frobenius eigenvalues -9 and all slopes 1/2. The forbidden b values 1,-a-1,a²-a+2 coincide pairwise only at a=1,-1,0 respectively (in the order pairs 1–2, 1–3, 2–3); no triple collision occurs. Removing the two forbidden b at a=0 and separating the origin yields all of the marked counts, including an empty rank-two row over F_3.

## originality

PASS

Pass for the full characteristic-three Newton, rank and a-number stratification with all-extension marked counts, not for novelty of the automorphism family or the supersingular curve in isolation. The exact normal form is known in the inspected classification in characteristic at least seven. The closest indexed characteristic-three census is for a different pencil; it shares the origin model but neither its hypotheses nor its classification give the rank-two line or the two-parameter count.

## value

PASS

The known dihedral locus has a simple but non-generic characteristic-three behavior: ordinary away from a line, rank two on its smooth nonzero part and supersingular but not superspecial at the origin. Identifying all three Newton strata and where they occur, including the disappearance of the rank-two stratum over the prime field, gives a usable complete classification for this standard normal form, beyond recomputing individual Cartier ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
