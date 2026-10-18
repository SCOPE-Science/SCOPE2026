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

Represent the order statistics M,A=(S∓|D|)/2, S=X+Y, D=X−Y. The symmetric Skellam pmf, telescoping k I_k(z)=z(I_{k-1}−I_{k+1})/2 and I0/I1 derivatives give d=E|D|=2λq, d'(λ)=2r. Differentiate the joint Poisson series: Cov(S,|D|)=λ d'=2λr. Since Var(S)=Var(D)=2λ and Var(|D|)=2λ−d², bilinear expansion gives claimed variances. Standard fixed-order Bessel expansion yields q=(πλ)^(-1/2)(1−1/(16λ)+O(λ^-2)), r=(2√(πλ))^-1(1+1/(16λ)+O(λ^-2)); expansion proves both Fano corrections. Independently double summed all joint Poisson cells 0..89 at λ=0.5,3,9 to 35-digit accuracy for four moments. Exact proof not finite extrapolation.

## originality

PASS

Best-of-knowledge novelty assessment compares identical mathematical statements and implications, not titles or a lack of search hits. The joint quantitative formula is absent from inspected Skellam, qualitative Poisson order-statistic and Gini sources. Comparison risks remain explicitly recorded; noncoverage is not asserted from abstracts of unread whole papers.

## value

PASS

This is a motivated sharp quantitative answer to the Poisson order-statistic underdispersion question: exact finite-intensity noise for both extremes and a nontrivial universal asymptotic deficit 1/π and first-order direction. It is more than a rewording of the generic ultra-log-concavity theorem; n=2 is the first nontrivial paired-extreme case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
