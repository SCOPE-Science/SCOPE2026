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

PASS. Read frozen RESULT.md and verification.py. Full-branch transfer P h=a h(ax)+(1−a)h(1−(1−a)x) has simple isolated stationary eigenvalue on BV, analytic twisted eigenvalue ρ(t) near t=0. Differentiating through third order solves zero-mean polynomial h1,h2,h3 because 1−[a^(j+1)+(−1)^j(1−a)^(j+1)] never vanishes for j≥1 and 0<a<1. Independent SymPy substitution checked all three polynomial recurrence residuals vanish identically and yields K2=a/[12(1−a)], K3=−a/[24(1−a)²], K4=a[19+6a(1−a)]/[720(1−a)³]. Also exact rational checks verified G²=3/[a(1−a)], H=6/5+(19/15)G² at four a. Spectral gap, not finite orbit counts, justifies limits and cumulant derivative interchange; symmetric a=1/2 is included but previously known.

## originality

PASS

PASS at best knowledge. Smith (2022) computed the symmetric tent-map cumulants K3(1/2)=−1/12 and K4(1/2)=41/360, and used the same spectral perturbation method. The inspected main text and Appendix E do not give full 0<a<1 formulas or the G–H line. Specialist skew-tent bifurcation literature remains a risk because one full article was abstract-only.

## value

PASS

PASS. Parameter-wide exact higher temporal cumulants of a canonical chaotic dynamical system form a natural complete classification, including the qualitative distinction between zero two-time covariance and nonzero higher cumulants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
