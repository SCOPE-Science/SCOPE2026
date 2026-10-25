---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For n,k positive, graph distance in P_n^k is ceil(|u-v|/k). On each modulo-k residue class, between endpoints a<c with c-a a multiple of k, the shortest path must make only +k jumps and is uniquely the intervening residue chain. Thus a mutually visible color class contains at most two of each residue (size<=2k), and a noncomplete graph needs at least two classes. If n<=k+1 the graph is complete. For k+2<=n<=2k two contiguous cliques suffice; for n>2k put t=ceil(n/(2k)) and divide P_{2kt}^k into t classes, each two length-k blocks t blocks apart. For cross-block offsets alpha,beta, the constructed monotone internal route avoids both blocks and has length t+1_{beta>alpha}, including t=2,beta<alpha special route, so is shortest. Truncate prefix to n: monotone geodesics remain inside endpoints. Independent forbidden-internal-vertex BFS verified construction for all 520 pairs 1<=k<=8,1<=n<=65; it is a diagnostic, not infinite proof.

## originality

PASS

Known mutual-visibility colorings on ordinary trees include k=1 paths, but the all-k exact path-power formula requires new geodesic blocking and two-block constructions. Path powers are graph powers, not Cartesian/strong products of paths, and independent variants are different constraints. Best-of-knowledge PASS with residual index risk.

## value

PASS

The k-th powers of paths are canonical proper-interval graph families. Exact all-parameter visibility chromatic number is structurally nontrivial: a geodesic residue obstruction is tight only after constructing two-block geodesic-avoiding color classes; the threshold at n=4k and unbounded gap from ordinary chromatic number are natural consequences. This is not a routine substitution into a tree result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
