---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: Derived transient first-step equations from states 11,10,01,00: (c+x+r)T10=1+cT, (c+y+r)T01=1+cT, (x+y+r)T=1+yT10+xT01. Solved N=(c+r+x+y)^2-xy and D=r(c+r+x+y)^2+xy(x+y+2c+r)>0. Independently differentiated sympy rational N/D, confirmed exact mixed derivative -2(c+r+x)(c+r+y)P(r)/D^3 as zero polynomial identity with P quartic from RESULT.md. P nonconstant coefficients strictly positive for x,y,c>0 and constant xy[xy-c(x+y)-2c²], forcing exactly one positive root in complementary case, none otherwise. Checked x=y=c=1 root 0.1833841130792549 and finite reductions give opposite signs at r=0 vs r=1. This establishes local h,k->0 complementarity/substitutability, not all finite interventions or general metapopulations.

## originality

PASS

PASS best-of-knowledge: The standard extinction-time backward equations and conservation reasoning are prior. Etienne–Heesterbeek (2001) and Ross–Pollett (2010) study metapopulation management; Johst–Drechsler (2003) study correlated disturbances. The inspected abstracts/review sections do not supply this model's complete exact mixed local-extinction sensitivity or unique catastrophe-rate threshold. The closest 2001 and 2003 primary full texts were inaccessible through authorized channel; absence of exact claim there cannot be asserted. This uncertainty remains explicit, not a fail solely from lack of access.

## value

PASS

PASS: A structural finite-state exact perturbation theorem proves a single switch from complementary to substitutable local habitat protection as catastrophe intensity increases; criterion xy<c(x+y)+2c² is sharp over an unrestricted positive-parameter region, including a boundary equality case. Motivated conservation-sensitivity question and analytic phase classification go beyond a textbook mean-time formula, although the result does not validate field or global-budget decisions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
