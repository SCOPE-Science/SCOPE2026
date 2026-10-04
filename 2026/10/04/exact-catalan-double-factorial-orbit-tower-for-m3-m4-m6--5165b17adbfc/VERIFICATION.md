---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The bundled `verify.py` independently generates the relevant finite labeled trees.

For rooted non-plane binary trees it recursively enumerates unordered bipartitions of the leaf-label set. Through seven leaves it obtains
\[
1,1,3,15,105,945,10395,
\]
matching \((2n-3)!!\).

For plane rooted binary trees it recursively enumerates ordered root splits through six leaves. It then forgets the left/right order at every internal vertex and verifies that every rooted non-plane tree has exactly \(2^{n-1}\) plane preimages.

For the root-forgetting step, the checker takes every rooted labeled tree through seven leaves, suppresses its root, and canonically records the resulting unrooted tree by its edge-split set. It obtains \((2n-5)!!\) distinct unrooted classes, and every class has exactly \(2n-3\) rooted preimages.

Finally it checks the displayed injective profiles through arity seven and computes the Stirling transforms, obtaining
\[
(1,3,19,207,3211,64383,1581259),
\]
\[
(1,2,7,41,346,3797,51157),
\]
and
\[
(1,2,5,17,86,647,6665)
\]
for \(M_3,M_4,M_6\), respectively. The replay ends with `VERIFY_OK`.

The checker validates the finite combinatorial reduction and enumeration. It does not independently reprove the published definability statements identifying the hypergraph automorphism groups with \(\operatorname{Aut}(M,C,<)\), \(\operatorname{Aut}(M,C)\), and \(\operatorname{Aut}(M,D)\). No independent audit has been performed.
