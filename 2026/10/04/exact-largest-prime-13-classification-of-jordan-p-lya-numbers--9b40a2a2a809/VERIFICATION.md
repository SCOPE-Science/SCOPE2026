---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

With prime rows \(2,3,5,7,11,13\), the valuation columns of \(2!,3!,5!,7!,11!,13!\) form an upper-triangular unimodular basis. Independent recomputation gives coordinates \(u=(1,-1,-1,1,0,1)\) for \(14!\), \(v=(-2,-1,0,1,0,1)\) for \(15!\), and \(16!=15!(2!)^4\). Because any factorial factor in a number with largest prime divisor 13 is at most \(16!\), the whole stratum is exactly \(\mathbb N^6+\mathbb N u+\mathbb N v\). Writing \(t=r+s\), coordinate nonnegativity yields the displayed inequalities. The lower bounds in \(r\) are monotone, so \(r=r_0=\max(0,-c_3)\) is optimal, and feasibility is exactly the stated bound with \(m=\min(c_4,c_6)\). Choosing \(t=m\) reconstructs the canonical factorization.

## originality

PASS

The 2020 primary paper defines the prime-factorial submonoid, proves uniqueness there, records \(14!\) as lying outside it, and lists the classical \(16!=2!\cdot5!\cdot14!\) identity; it does not classify all Jordan--Pólya numbers with largest prime divisor 13. The closest published SCOPE result proves free prime-factorial normal forms only through support 11 and stops at the \(14!\) obstruction. Fresh Resultary and web searches did not locate the two-generator support-13 semigroup, its necessary-and-sufficient valuation inequalities, or the canonical factorization. The new theorem therefore closes the first failure stratum rather than restating the known obstruction.

## value

PASS

Largest prime 13 is the first natural support where the unique prime-factorial normal form breaks. Classifying the entire next stratum, identifying exactly two new generators, and eliminating them to a closed membership test and canonical factorization is a motivated complete boundary classification with a plausible template for later supports.

The dated certificate retains the supplied scientific assessment, sources and limitations.
