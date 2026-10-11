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

For an exponent-p extraspecial group, \(V=G/Z(G)\) is a nondegenerate \(2n\)-dimensional symplectic space. Every noncentral projective point lifts to \(p\) distinct noncentral cyclic subgroups in its elementary abelian preimage, while the trivial subgroup and center contribute two more, so \(|L_1(G)|=pN+2\). Two noncentral cyclic subgroups permute exactly when their projective points are symplectically orthogonal. A fixed projective point has exactly \(R\) projective points in its orthogonal hyperplane, giving \(pR+2\) commuting partners for each noncentral cyclic subgroup and all partners for the two central vertices. Summing ordered pairs gives the claimed numerator. Independent substitution at \(p=3,n=2\) gives \(N=40,R=13\) and csd \(=4684/135?\) [numerically about 0.34695], consistent with the exact formula; the actual verifier exhaustively constructs the Heisenberg model for \((p,n)=(3,1),(3,2),(5,1),(5,2)\).

## originality

PASS

The foundational csd paper gives only the order-\(p^3\) exponent-p extraspecial value, explicitly as a small section obstruction. No formula for arbitrary extraspecial rank was found. The audited theorem replaces that isolated case by a uniform projective-symplectic count and derives the new fixed-p limit.

## value

PASS

Extraspecial groups are a canonical infinite p-group family and csd is the invariant introduced by the cited source. Extending the lone rank-one value to every symplectic rank gives a clean exact formula and a nontrivial asymptotic limit \(1/p\), so the result is a natural complete classification for this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
