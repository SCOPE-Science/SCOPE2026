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

For n>=2 and A Smith-equivalent to diag(I_(n-1),0), a bordered unit-entry matrix realizes A+EdF stably equivalent to I_(n-2) plus C=[[1+dvu,df],[-e,0]]. The two-by-two Smith exponents are i=min(alpha,beta,gamma), j=min(t,beta+gamma-i), including alpha=beta=gamma=t and zero divisors; rank-one update cannot affect the n-2 unit factors. For uniform u in R^(n-1), the primitive event has probability 1-q^(-(n-1)); conditional on it v.u is uniform in R, otherwise 1+v.u is a unit. Consequently alpha has mass b_m,t(0)=1-(1-q^-m)/q and b_m,t(k)=(1-q^-m)a_t(k) for k>=1, independent of beta,gamma, which have a_t(k). Summing their joint masses over valuation triples gives the complete Smith-type law and q^(2nt) times probability the ordered pair count, independent of chain-ring isomorphism or d unit. The statement concerns structured corank-one update, not arbitrary matrices.

## originality

PASS

Prior-work comparisons credit foundational techniques and potential broader theorems. No actually inspected source has a theorem that entails the complete claimed new invariant/formula at the assigned parameters; real full-text gaps are identified as residual risk. The exact mathematical implication comparison is given in four named checks.

## value

PASS

The complete cokernel elementary-divisor profile of uniformly sampled rank-one repairs of a natural one-dimensional corank defect is a structured random-matrix invariant. General invertibility tests collapse every noninvertible Smith type into one outcome. Exact all-q,t,n probabilities distinguish the torsion stratification and supply a benchmark for random low-rank perturbations over local rings. This is not merely a determinant calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
