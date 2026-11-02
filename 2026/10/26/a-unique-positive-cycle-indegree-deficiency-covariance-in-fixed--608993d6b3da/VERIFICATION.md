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

For n>=3, 1<=k<=n-2, each loop-free row chooses a uniform k-subset independently. For a specified directed simple l-cycle J, P(J)=p^l and any of its l vertices cannot have indegree zero. For outside v, conditional avoidance probability at a cycle source is (n-k-1)/(n-2)=q(n-1)/(n-2), hence E[Z|J]=(n-l)q^{n-1}A^l. Summation over (n)_l/l rotations yields the stated exact Cov. f_l=(n-l)A^l strictly decreases for l>=2 with f_2-n=1/(n-2)>0 and f_3-n=-(2n-3)/(n-2)^3<0, giving unique positive l=2; k=n-1 Z=0. Independent-arc model and fixed-k asymptotics follow separately. Independent exact rational exhaustive checks passed n,k=(3,1),(4,1),(4,2),(5,1),(5,2), all l. Finite checks support rather than replace all-n proof.

## originality

PASS

Previously located k-out graph connectivity, inhomogeneous row-selection and motif expectation sources concern global connectivity, isolated undirected components or expected subgraph counts, not the cross-covariance with zero-indegree vertices and its sign for every cycle length. A stronger joint-moment formula in older random mappings remains possible.

## value

PASS

The sign reversal for reciprocal directed two-cycles relative to equal-mean independent-arc sampling isolates the effect of without-replacement row constraints. Exact all-cycle covariance and triangular cancellation at l=3 are natural finite-sample network-motif statistics, useful in choosing graph null models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
