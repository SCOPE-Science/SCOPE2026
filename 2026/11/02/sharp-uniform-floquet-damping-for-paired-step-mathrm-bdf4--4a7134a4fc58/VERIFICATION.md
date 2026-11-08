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

Genuine degree-four Lagrange interpolation at varying time nodes yields α0=sum(1/dj)>0 and the 3×3 difference companion first row of cumulative α2..α4. Four matrices give cubic z³-A(t)z²/D(t)+B(t)z/D(t)-C(t)/D(t), t=r+1/r≥2. Independent SymPy computation from interpolation agreed exactly for r=1/7,1/2,1,3/2,3,9 (not alone an all-r certificate). Rescaling by sqrt(21) and cubic Schur criterion reduces strict root bound to P1,P2,P3 shifted coefficient positivity with 4<sqrt21<5 and positive-coefficient polynomial P4; independently rechecked all these polynomial coefficient certificates. As t→∞ the limiting cubic z(z²-2z/15+1/21) has conjugate roots modulus 1/sqrt21, establishing sharpness and nonattainment at finite r. Does not prove arbitrary-step norm stability.

## originality

PASS

Best-knowledge PASS qualified: 1983–1990 BDF specialist work gives restrictions for variable steps and could have a hidden periodic classification. Wang–Ruuth 2008 sufficient adjacent-ratio bound does not imply this unbounded-r paired four-step result; no exact same cubic/supremum found in inspected abstracts or published-finding query. Inaccessible old primary texts materially limit priority confidence.

## value

PASS

An exact uniform sharp spectral damping constant despite arbitrarily extreme fixed periodic ratios is a substantive numerical-stability phenomenon, distinguishing zero-stability of a repeated paired mesh from standard adjacent-step sufficient conditions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
