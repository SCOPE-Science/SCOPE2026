---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS: For n>=2 uniform unordered increasing trees, the rooted forest species equation T_z=v-1+exp(T) integrates to T(vz;v^-1)=T(z;v)+(1-v)z. Marking root degree gives A_n from v-1+exp(uT); marking the unique root subtree containing newest n gives B(z)=v exp(u[T+(1-v)z]). Coefficient extraction yields A_n(u,v)=v^n B_n(u,v^-1), proving full bivariate distribution reflection. The n=1 root-is-leaf exception and Hoppe n=3 iff theta=1 boundary are explicit. Conditional leaf recursion gives Cov(R,L)=(n-2)/(2(n-1)) and Cov(D,L) negative thereof. Independently enumerated every labeled recursive tree for n=2..8; joint integer-count tables agree. Finite enumeration is supplementary to the formal proof.

## originality

PASS

The full reflected root-degree/leaf versus newest-depth/nonleaf joint distribution is stronger than known separate marginals and root-degree/leaf covariance; no inspected published statement was shown to imply it. Historical equivalence via classical Eulerian/Stirling polynomial transformations is a substantial residual priority risk, particularly inaccessible Carlitz–Scoville 1974.

## value

PASS

The finite-n joint symmetry transfers all conditional distributions and mixed moments between natural growth-tree statistics. The explicit nonunit Hoppe-weight counterexample demonstrates a structural uniform-attachment boundary, rather than a trivial single covariance or isolated enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
