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

For uniform iid q-ary W (q>=2,n>=2), the deterministic two-deletion cardinality B_2(w)=binom(r,2)+k-t follows by appending one letter and checking the exact intersection of two deletion-output sets, including overlapping singleton runs. With Xi=1{Wi!=Wi+1}, S=sum Xi, Q=sum adjacent XiXi+1, E=X1+Xm and T=number of ABA interior singleton returns, get B2=binom(S+2,2)-E-Q-T. The initial letter and q-cyclic increments are independent uniform; Xi iid Bernoulli p=(q-1)/q; conditioning on Xi makes each ABA cancellation a constraint on independent nonzero increments. Every subset of the eligible adjacent constraints is a forest, so these indicators are mutually independent Bernoulli a=1/(q-1), proving T|X~Binomial(Q,a), including q=2 degeneracy. Squarefree centered-Bernoulli orthogonal expansion and law of total variance yield the displayed mean and three-term variance for every n, including n=2 zero variance. Independent full output-set enumeration over small q,n confirmed both conditional and moment statements.

## originality

PASS

The q=2 case is entirely covered by the prior published exact binary two-deletion variance result and is expressly excluded as an original component. The q>2 exact variance and conditional binomial ABA count are the surviving novelty. Swart–Ferreira and Liron–Langberg provide binary run-based predecessors; generic Levenshtein radius-one ball sizes are different observables. Any stronger general alphabet moment formula, if found, could supersede this assessment.

## value

PASS

Two-deletion output-set size measures local degrees in a central deletion-channel reconstruction graph. Its exact nonbinary variance quantifies graph nonregularity on cubic n scale, while the conditional ABA law reveals a reusable independence mechanism with precise q-dependence; both are natural statistics rather than artificial slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
