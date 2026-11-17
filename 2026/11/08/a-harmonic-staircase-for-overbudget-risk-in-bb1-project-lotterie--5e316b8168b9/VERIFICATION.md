---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

With H indicator for expensive project and Z count of unselected cheap ones, E[H]=q, E[Z]=c q and total expenditure k-Z+cH. For c=m+f noninteger, below-budget expensive outcomes require Z>=t=m+1, capped expensive outcomes require Z>=ell=max(0,ceil(c-delta)); thus r>=q(t-c)/(t-ell) or infeasible if delta<f. Three outcome types (H,Z)=(0,0),(1,ell),(1,t), with masses 1-q,r,q-r, satisfy the bound with equality. Cyclic averaging of omitted blocks ensures every cheap marginal; direct addition/removal checks BB1 and cap. For integer c omit exactly c when H=1, giving zero risk. Independent full-outcome LP at k=5,c=7/2,q=1/2 confirms optimum 1/4,1/8,1/12,1/16 at caps 1/2,3/2,5/2,7/2; infinite theorem follows analytical bound/construction.

## originality

PASS

Aziz et al. prove general BB1 marginal-preserving implementation, but not the minimum strict-overbudget probability subject to a hard overspend cap. General dependent rounding/joint mixability and Bernoulli risk optimization can formulate coupling problems, without an identified logical implication giving this explicit staircase. Primary Aziz full text was examined; more remote risk-coupling literature is not fully excluded. Best-of-knowledge originality passes provisionally.

## value

PASS

Under BB1, existence of a lottery alone does not control risk frequency. The complete sharp feasibility/risk tradeoff with explicit finite-support optimal distributions answers a natural policy-design question for a motivated symmetric cost family rather than an arbitrary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
