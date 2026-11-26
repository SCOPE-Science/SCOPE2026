---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For an appended generator [G|B] of a shortest LCD embedding, rank(B) is at least the hull dimension ell: rank(GG*)=k-ell and the rank of the Gram update BB* is at most rank(B), while the embedded Gram has rank k. Since B has ell columns, projection Q has rank ell (over the stated Euclidean/Hermitian fields). Puncturing is an isomorphism of k-dimensional codes. For any r-subcode U with t=dim Q(U), its old-coordinate image has dimension r and contains an (r-t)-subcode of K=P(ker Q). Its support is at least max(d_r(C),d_(r-t)(K)); its disjoint new support is at least t. Rank-nullity gives exactly the numerical limits on t, with d_0=0 including t=r. Lifting a minimizing r-subcode gives the upper bound; surjectivity makes all ell new coordinates contribute at r=k; for ell=k only t=r is allowed. The argument includes ell=0 and uses no finite experiment. The frozen binary/ternary verifier was inspected, not executed, and does not test all embeddings or quaternary codes.

## originality

PASS

The supported distinction is the generalized-support lower bound conditioned on the kernel of the new-coordinate projection, not the shortest length, structural normal form, or routine upper bound. The closest primary theorem gives the needed rank, not the kernel-conditioned generalized-weight estimate; the closest higher-support extension record treats a different code construction. No covering result was identified in the inspected sources.

## value

PASS

The result determines when the hull forces higher-support growth under every shortest LCD repair, and the kernel term is not just notation. For example take disjoint binary generators u,v,w of weights 2,2,5, append one separate new coordinate to each of u and v and none to w. The Gram becomes the identity, ell=2, K=<w>, and for r=2 the parent weight is 4. The rank-only lower bound is 5, but both admissible t=1,2 in the kernel bound give 6, attained in the embedding by the span of the first two lifted generators. This is a strict, attained improvement at a genuine higher weight with a nonzero rank-only correction. No claim of universal sharpness is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
