---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Let J_U indicate r-subset U is exactly an isolated K_r component, and T_s sum all s-clique indicators. With q=E J_U=p^{r(r−1)/2}(1−p)^{r(n−r)}, conditioned on J_U all edges inside U are present, cross-edges absent and complement edges remain iid Bernoulli; therefore E[T_s|J_U]=C(r,s)+C(n−r,s)p^{s(s−1)/2}. Subtract E T_s=C(n,s)p^{s(s−1)/2}, multiply by q, sum over C(n,r) U gives exact covariance. For s≤r, A=C(r,s)>0, B=C(n,s)−C(n−r,s)>A when n>r, so unique crossing (A/B)^{1/C(s,2)} in (0,1); s>r has A=0 and always negative. B=Σ_{j=0}^{r−1}C(n−j−1,s−1)~r n^{s−1}/(s−1)! yields n^{−2/s} and eventual threshold ordering for fixed r. n=7,r=6,s5 vs s6 yields 30th powers 8/343 and 7/343, finite reversal. Independent rational enumeration of graph edge masks n=5 for r=3,s=2 at p=1/3,2/3 matched formula; inspected source check.py full n≤6 enumeration logic (not rerun in entirety).

## originality

PASS

Best-of-knowledge PASS, with meaningful reservation that this is an elementary conditioning calculation. The exact covariance relates *isolated clique connected components* to *all embedded cliques*, not total components or maximal cliques; named prior texts focus on different joint observables or graph laws. No inspected explicit all-(n,r,s) crossing hierarchy, but general joint generating-function literature might imply the formula directly and should be checked before priority certification.

## value

PASS

A naturally motivated exact covariance between two standard but competing combinatorial counts establishes sharp negative/positive sign domains, multiple n^{−2/s} sparse thresholds and a finite reversal in their ordering. The simplicity of the conditional-expectation proof does not eliminate the utility of this exact natural graph-statistic invariant; originality against broad joint-moment literature is the principal risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
