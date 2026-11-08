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

Four labelled report copies on R/Z with geodesic distance admit a globally optimal report because the piecewise-linear total-distance function only jumps upward at reports. The optimality slope inequalities and reflection yield normalized (-a,0,b,c), 0<=a<=1/2, 0<=b<=c<=1/2 with OPT=a+b+c. For four-agent EPCD, probability of clockwise report zi is (g_{i+1}+g_{i+2})/2; expressing full social costs and splitting according to a+c<=1/2, a+b<=1/2<=a+c, or a+b>=1/2 yields three exact algebraic identities for F=5OPT-4C_E, each nonnegative, and equality only at (-1/4,0,0,1/4) for OPT>0. RD triangle inequality gives <=3OPT/2 and same witness attains both bounds, so every fixed mixture has exact sharp ratio (5+lambda)/4 for lambda in [0,1], including EPCD 5/4 and equal mixture 11/8. Independent rational input checks verified the direct random-deletion EPCD formula and all three case identities; they are corroboration, not proof over continuum.

## originality

PASS

Chan–Lin–Wang introduce even-population EPCD and show 3/2 for the equal-weight mixed mechanism uniformly in population size, not the 4-agent exact 11/8 from accessible abstract. Their unrestricted strategyproof 4-agent lower bound is about a different minmax object. Prior 3-agent PCD results and odd-population mixtures cannot be directly used for four-agent deletion+full-cost evaluation. Their complete 2026 primary paper remains inaccessible, hence a material priority risk but not evidence of coverage.

## value

PASS

The exceptional n=4 case is the smallest even population for the mechanism and tests sharpness of a population-independent guarantee. Exact 5/4, 11/8, and an affine interpolation law, with an equality-classification witness, quantify the mechanism-performance gap rather than merely supplying another loose bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
