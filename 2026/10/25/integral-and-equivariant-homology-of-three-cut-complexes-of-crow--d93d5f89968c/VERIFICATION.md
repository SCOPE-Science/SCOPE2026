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

For crown G_n=K_(n,n) minus a perfect matching (n>=5), a disconnected induced triple is exactly the obstruction defining the Alexander dual L of the ordinary three-cut complex X. A subset of L with at least three vertices must have at most two from each part and at most one from each omitted pair, hence L is the two-row capacity-two, one-per-column multiple chessboard B_n together with n extra isolated-in-2-skeleton edges a_i b_i. The cited published shellability theorem applies for n>=5, making B_n a pure three-dimensional wedge of b_n=1+n(n-2)(n-3)(n-5)/4 three-spheres. Since adjoining n edges creates n free independent 1-cycles, L has free reduced homology Z^b_n in degree3 and Z^n in degree1. Integral Alexander duality on 2n vertices yields free reduced H_{2n-6}(X)=Z^b_n and H_{2n-4}(X)=Z^n, no other degrees. The former non-top homology obstructs shellability of pure X. Signed fixed-face enumeration of the chessboard core gives T_0=Q(c1)-2c2P(c1)+c2(c2-1) and T_1=1-2c2+4 binom(c2,2)-2c4. Equivariant Alexander duality adds vertex permutation orientation (-1)^{n eps}, while the extra edges give (-1)^eps c1; the stated two full rational characters follow. Independent complete A/B subset counts for n=5,6,7 reproduced chessboard f-vectors, the n exceptional edges, and b_n=1,19,71.

## originality

PASS

Best-of-knowledge original contribution: The claim is not a trivial substitution of a known chessboard theorem; the extra-edge decomposition, Alexander dual, and S_n×C2 action have to be supplied. Historical general cut theorem coverage is bounded by inspected material.

## value

PASS

This gives a complete all-n integral and equivariant homology classification for a canonical connected bipartite graph family and detects non-shellability despite purity. Two separated homological degrees and complete S_n×C2 characters make it a structural cut-complex result, not a recomputation of the shellable chessboard core.

The dated certificate retains the supplied scientific assessment, sources and limitations.
