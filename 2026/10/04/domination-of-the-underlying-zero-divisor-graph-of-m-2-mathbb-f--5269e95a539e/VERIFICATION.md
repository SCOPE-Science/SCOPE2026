---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Every nonzero singular \(2\times2\) matrix has rank one and is determined up to \(q-1\) nonzero scalars by its image line \(L\) and kernel line \(K\). For types \((L,K)\), \((L',K')\), adjacency is exactly \(L'=K\) or \(L=K'\). One diagonal representative per projective line gives a dominating set of size \(q+1\). For \(q>2\), the support-deficit rectangle argument forces any hypothetical support below \(q+1\) into the equality pattern where a selected off-diagonal type has no selected type-neighbor; because its fiber has at least two scalar copies, an unselected copy remains undominated. For \(q=2\), fibers are singletons and the displayed two projective types dominate all nine vertices, while no vertex is universal. Independent finite reconstruction of the actual \(q=2,3\) matrix graphs agrees with \(2\) and \(4\).

## originality

PASS

Jafari--Jafari Rad prove directed out- and in-domination \((q^n-1)/(q-1)\); at \(n=2\) this is \(q+1\). Passing to the underlying undirected graph adds all reverse-arc adjacencies, so their directed lower bound does not transfer. The audited binary case, where the undirected value is \(2\) instead of \(3\), explicitly demonstrates non-implication. Resultary searches found no prior exact theorem for this undirected symmetrization.

## value

PASS

The result gives the exact undirected counterpart of a classical matrix-ring domination problem and isolates the unique binary failure of invariance under forgetting arc direction. The image/kernel projective model and the scalar-fiber obstruction are reusable structural tools rather than a numerical curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
