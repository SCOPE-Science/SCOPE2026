---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For one and the same uniform π∈S_n, n≥1, the Ewens tilt Pθ(π)∝θ^{C_n(π)} has d/dθ Pθ(I_{n,j}=1)|1=Cov(C_n,I_{n,j}). At size m=j the last-position record iff π(j)=j, an Ewens singleton probability θ/(θ+j−1). When inserting new value m into the cycle of an Ewens permutation, insertion after one of j−1 earlier sites destroys the record, after j forces the new max at j, after a later site or as singleton leaves it unchanged; this gives p_m=[(θ+m−1−j)p_{m−1}+1]/(θ+m−1). At θ=1 p=1/j, differentiated forcing terms cancel, p′_m=(m−j)p′_{m−1}/m. Iteration yields (j−1)/(j² binom(n,j)) exactly, with zero j=1 and n=1. Sum of independent marginal record/cycle Bernoulli variances is H_n−H_n^(2); isolating j=n and bounding binom(n,j)≥binom(n,2) for 2≤j≤n−2 shows covariance∼1/n and corr∼1/(n log n). Independent exact rational enumeration n=3..7 of both statistics on each permutation corroborates all positionwise identities. No Foata-transform identification is used.

## originality

PASS

The exact *same-permutation*, positionwise cycle-count/left-to-right-record covariance is distinct from equidistribution of marginal cycle and record counts under the Foata correspondence and from conjugation-invariant record limit laws. Best-of-knowledge primary-source comparison did not expose the finite formula, but older joint generating functions remain a risk.

## value

PASS

Two canonical but non-identical permutation statistics—disjoint cycles and one-line records—have the same marginals but subtle dependence. Exact positive positional covariance and its near-complete localization at the last index, together with 1/(n log n) correlation, answer a natural joint-statistics problem quantitatively; this is not a mere equidistribution restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
