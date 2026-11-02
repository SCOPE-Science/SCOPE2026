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
# Reproducibility

Run `python3 checks/reproduce.py` from this package's extracted root. The checker uses only Python standard-library exact rational arithmetic. Its tests independently reconstruct the two exponential return rates, both capture rates, mobile travel time and independent Gaussian timing variance from six theoretical cumulants for 729 positive distinct-rate parameter sets. It also checks the five-moment shape identities, positivity preconditions, and an explicit distinct positive model having exactly the same first five but not the same sixth cumulant.

The sample input has cumulants \((7/2,31/12,19/3,220/9,3260/27,19480/27)\). It reconstructs mobile time \(2\), capture rates \((1/2,3/4)\), return rates \((1,3)\), and clock variance \(1/4\). The strict five-cumulant upper bound on clock variance is \(87/220\).

The universal claims are established in `RESULT.md` by exact cumulant identities, exhaustive positive two-node moment parameterization, strictly signed derivatives, and a bijective sixth-moment formula. Neither finite computations nor sample data constitute an infinite proof. The verification is not independent validation, and no external certificate has been issued.
