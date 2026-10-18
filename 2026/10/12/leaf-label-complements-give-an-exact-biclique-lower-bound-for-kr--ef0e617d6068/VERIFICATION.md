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

Under the stated uniform admissible restriction distribution, for each D of size 2d+1 and R of size 2d, the restriction complement has equal sizes n-2d and precisely (n-2d)! bijections, giving independent uniform D,R. If the finite set S of all possible leaf labels misses D×R, any tree output is outside valid residual rectangle for every compatible design, hence E>=Pr(S misses D×R). This event is exactly the K_(2d+1,2d) density in complement of S; the union bound over S gives 1-|S|ab/(n(n+1)), and a p-ary depth-e tree has <=p^e leaves. Zero error implies complement K_a,b-free. Independently enumerated all 315 residual rectangles at n=6,d=2 with three selected labels and counted 27 misses. The only relevant source premise not independently read in full is the exact uniform sampling definition of Omega(n,d); the theorem states that premise explicitly.

## originality

PASS

The standard rectangle-hitting/Zarankiewicz language and elementary union bound are established combinatorics, not novel on their own. The narrower claim is their exact connection to the output-support component of the 2026 reduced PHP search-tree error, including its distinction from path-sensitive feasibility. Resultary did not yield an already published SCOPE equivalent. The most relevant 2026 primary text could not be accessed in full through legal routes (institutional VPN disconnected); noncoverage of its appendix is NOT asserted. Best-of-knowledge O PASS is qualified by substantial exact-source overlap risk.

## value

PASS

A newly formalized reduced proof-complexity search-tree error has a natural support-only obstruction that can be studied without the path predicate. Identifying its exact complete-bipartite density and zero-error Zarankiewicz threshold is a motivated structural diagnostic: it delineates exactly where label-support lower bounds stop and where stronger path-sensitive reasoning is needed. This does not claim new extremal-graph estimates or an AC0[p]-Frege lower bound, and the simple union-bound calculation alone is not presented as value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
