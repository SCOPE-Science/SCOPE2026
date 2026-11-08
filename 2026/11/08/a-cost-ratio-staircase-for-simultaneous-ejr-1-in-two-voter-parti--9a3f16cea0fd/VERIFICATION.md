---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible finite verification

Run `python3 verify_ejr.py` using Python 3's standard library; there are no external packages or data files.

The checker directly enumerates all \(2^{2k+2}\) labeled project outcomes for each tested parameter cell, filters by the total budget, lists every set \(T\) cohesive for each of the three nonempty voter groups, and checks the original existential EJR-1 condition separately for cost and cardinality satisfaction. Rational costs are represented exactly as numerator/denominator integers. It does not invoke the theorem's inequalities when determining whether an individual outcome passes.

Observed run: \(72\) parameter cells for \(k\in\{3,4,5\}\) and \(24\) rational values of \(c\) were checked; every zero/nonzero and exact count agreed with the stated theorem. Five additional parameter cells for \(k=6\) also agreed. Representative exact counts: \(N_4(7/2)=8\), \(N_4(4)=0\), \(N_4(6)=32\); \(N_5(9/2)=10\), \(N_5(5)=0\), \(N_5(8)=50\). The checker also verified positive compatibility for sampled \(0<c<3\).

Limits: finite enumeration is only a computational cross-check, not a proof for arbitrary positive real costs or arbitrarily many projects. The general argument is given in RESULT.md. Source inspection and literary priority checks are described in REVIEW.md and AUDIT.json. Independent external audit: not performed.
