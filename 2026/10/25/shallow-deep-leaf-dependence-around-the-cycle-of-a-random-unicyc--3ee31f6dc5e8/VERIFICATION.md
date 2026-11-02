---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Fix the k cycle vertices and cyclic order. Removing its cycle edges leaves a uniformly distributed forest with k specified roots and F(n,k)=k*n**(n-k-1) for n>k (1 for n=k). For r labeled J-leaves and s labeled H-leaves, deleting the leaves and reattaching gives k**r (m-r-s)**s F(n-r-s,k) completions per ordered distinct marked tuple; summation produces all (m)_(r+s) factorial moments. The r,s=(1,0),(0,1),(1,1) cases give the displayed covariance. For m>=3, the exact E[JH]/(E[J]E[H]) equals (m-2)/m*(n/(n-1))**2*(1-1/(n-1)**2)**(m-3)<1 because m<=n-3 and m(n-1)**2-(m-2)n**2=2n(n-m)+m>0. At m=2, E[JH]=0; m<=1 gives zero covariance. Expansion for k/n->alpha in (0,1) gives -alpha*(1-alpha)**2*(1+alpha**2)*exp(-2(1-alpha)). Independent exact rooted-forest enumeration through n=7 checked 65 mixed moments across 1425 forests. This is analytic for every admissible n,k; finite tests are corroboration only.

## originality

PASS

PASS qualified: fixed-root forest counts and total-leaf marginal are prior art, but neither directly determines the parent-on-cycle versus parent-off-cycle joint law, and the inspected random-graph articles address component/cycle sizes. A possible historical multitype forest generating function that directly implies the whole joint law remains a priority risk.

## value

PASS

The conditional two-type leaf statistic is a natural local/global interface statistic of the unicyclic graph model; the exact finite joint law and universally negative covariance (with explicit linear-order limit) are complete distributional information absent from an uncolored total-leaf count. This is a motivated structural dependency result rather than an arbitrary graph instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
