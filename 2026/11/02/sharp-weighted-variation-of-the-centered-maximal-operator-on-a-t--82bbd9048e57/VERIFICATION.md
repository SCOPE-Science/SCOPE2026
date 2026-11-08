---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Read pinned RESULT.md and exact-rational verify.py. Translate positive data by a common baseline and reduce to x=f(a)-f(c), y=f(b)-f(c), with h,u,v>0. The centered ball averages relative to baseline are Mc=max(0,H), Ma=max(x,alpha*x,H), Mb=max(y,beta*y,H) where H=(ux+vy)/(h+u+v), alpha=u/(h+u), beta=v/(h+v). Four quadrant analysis of gain (|Ma-Mc|+|Mb-Mc|)/(|x|+|y|) shows nonnegative/opposite-sign maxima 1-L/W. In the negative quadrant, switching lines yield the other sharp value U(h+2L)/[(h+2U)(h+L)]; explicit leaf spike and opposite-offset negative pair attain both. First branch strictly increases with h and second decreases, crossing uniquely at h³+(2U+L)h²+U²h-2UL²=0. For u=v=w this gives h/w=(sqrt5-1)/2 and minimized constant same. Independent 28,160 exact rational diamond quotient checks corroborated, not the symbolic continuum proof. Counting h=u=v yields 2/3.

## originality

PASS

Best-of-knowledge PASS for exact continuous positive mass P3 centered maximal BV norm and optimizing center-mass phase transition. Soria–Tradacete arXiv:1410.6204 studies ℓp graph maximal norms under counting measure, not the weighted BV seminorm. González-Riquelme–Madrid arXiv:2005.03146 gives known equal-weight 2/3 for a 3-vertex star, not arbitrary vertex masses or negative-sector phase branch. Resultary related monotone P_n counting-measure theorem handles a restricted input type and does not dominate all real inputs here. A previously published weighted-star BV theorem might cover the result, retained as risk.

## value

PASS

Complete explicit mass-sensitive sharp regularity norm on the smallest nontrivial noncomplete path with negative-sector extremizers, unique optimal center weight and a golden-ratio transition. This is a motivated canonical test case for weighted graph averaging, not merely the n=3 known counting constant, and the two competing extremizer families are structurally informative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
