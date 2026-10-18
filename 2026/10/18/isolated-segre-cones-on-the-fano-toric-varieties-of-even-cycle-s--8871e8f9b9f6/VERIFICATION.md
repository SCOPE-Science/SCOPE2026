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
# Reproduction and verification

Run `python3 check.py` with Python 3 and no third-party modules. The finite checker enumerates exact polar vertices for \(3\le n\le10\), checks the count of polar vertices, verifies each active facet-ray set, evaluates every codimension-one maximal determinant by fraction-free exact integer elimination, confirms balanced circuit relations in even lengths, and tests balanced semigroup pairing in low degrees. A successful execution prints eight dimension summaries followed by `VERIFY_OK`.

Expected even-cycle fixed singular counts at \(n=4,6,8,10\): respectively \(6,20,70,252\). Expected multiplicities: respectively \(2,6,20,70\). Expected odd-cycle singular counts at \(n=3,5,7,9\): zero.

The general proof is symbolic and does not depend on enumeration: it classifies all vertices of the integer-slab cube polar, identifies the primitive lattice circuit, computes its dual affine semigroup, and presents that semigroup algebra by the rank-one matrix minors. The Segre degree identity supplies the infinite multiplicity formula. Finite agreement is a consistency check, not a substitute for proof.

The local class group and the normal/Cohen–Macaulay/Gorenstein assertions use standard properties of the cone over \(\mathbb P^{r-1}\times\mathbb P^{r-1}\) with \(\mathcal O(1,1)\). The singularity claim is about the face-fan variety over an algebraically closed field, with no restrictions on characteristic. The previously known odd-cycle smoothness criterion is credited, not presented as original. No independent audit or independent validation has been performed.
