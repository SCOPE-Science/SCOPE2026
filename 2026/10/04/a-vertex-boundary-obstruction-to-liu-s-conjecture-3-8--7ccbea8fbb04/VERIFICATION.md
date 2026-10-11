---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The standard internal angle-bisector identity gives \(w_c^2=ab((a+b)^2-c^2)/(a+b)^2\). As an interior point tends to \(C\), \(R_1\to b\), \(R_2\to a\), \(R_3\to0\), \(w_1,w_2\to0\), and \(w_3\to w_c\). Hence the defect tends exactly to \(b[ac^2-(a-b)(a+b)^2]/(a+b)^2\). The strict side condition makes this negative, and continuity supplies an actual open interior neighborhood of counterexamples. For \(a,b,c=(5,4,3)\), the limit is \(16-160/9=-16/9\). No finite numerical sampling is needed for the quantified conclusion.

## originality

PASS

The 2012 source was freshly inspected at the page containing Conjecture 3.8 and states the universal inequality contradicted here. The highly relevant 2016 open-access follow-up and 2018 full paper by the same author were also checked for their Oppenheim/Barrow refinements; neither supplies this boundary disproof. Fresh Resultary search returns the audited record as the exact hit and other, different Liu counterexamples, but no earlier theorem covering Conjecture 3.8's vertex obstruction.

## value

PASS

Refuting a published geometric conjecture with a structural open family is intrinsically motivated. The side-length criterion explains a mechanism of failure and the canonical \(3\)-\(4\)-\(5\) specialization makes the obstruction transparent; this is materially stronger than an isolated numerical point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
