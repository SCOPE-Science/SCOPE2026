---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Disjoint integer-height slices contain (b j+1)L_P(t-j) lattice points, giving an exact convolution. Setting L_[0,a](k)=a k+1 yields n^3 coefficient ab/6, n^2 coefficient (a+b)/2, n coefficient (6+3a+3b-ab)/6; first negative iff (a-3)(b-3)>15. Put u=a-3,v=b-3, uv>=16 and AM–GM gives ab>=uv+3(u+v)+9>=49 with equality only at 7,7. For a polygon L_P=Ak²+B k/2+1, summation yields n^4=Ab/12, n^3=(4A+Bb)/12, n^2=((6-b)A+3B+6b)/12, n=(2A+(3-b)B+6b+12)/12. Pick 2A=2I+B-2 ensures positive n for b<=4, while n² positive through b<=6. For b=5 a negative n means B>2I+40 => 2A>=39, so normalized volume 2Ab>=195; triangle with B=41,I=0 attains. At b=7 the simultaneous quadratic and linear negativity conditions are contradictory; rectangle 37x4 with A=148,B=82 gives both negative at b=8 and for all larger integers. Independent symbolic summation/interpolation reproduced both formulas and witnesses; finite tests do not establish the unbounded proof.

## originality

PASS

Liu–Tao–Xin 2026 gives the generic join enumeration and an existence example, while Castillo–Liu–Nill–Paffenholz demonstrates negative Ehrhart coefficients in unrelated smooth classes. The sharp segment/segment and polygon/segment thresholds are separate from these prior works; exact formulas follow elementary specialization, so novelty rests on the complete sharp classification, not on generic convolution.

## value

PASS

The very smallest possible dimensions of standard joins of individually Ehrhart-positive factors give a naturally motivated sharp phase diagram: earliest dimension, minimum volume, universal safe segment-length cutoff and first two-sign-failure threshold. The exact inequalities classify an unbounded family without claiming all joins or all polytopes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
