---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Frozen RESULT.md 2acc5ddf340755f9f060097b9cde149622d53378, verify.py f99e248af2ffa61306a6d7386387cb30a65ca935 and certificate.json f2734a6dc0c44d670cd2c9948b4d294fb7467a22 inspected. Reconstructed 102 oriented tetrahedra, 204 triangle faces, 119 edges and 17 vertices of Lutz B3. Independent exact JS check reconstructed d2,d3 and integer chain matrices B(204x102), L(102x204), verified ALL d2B=0 (12138 entries), LB=I, BH=d3, det(H)=+2 by BigInt fraction-free elimination, and rank H mod2=101; checked lambda H=0 and pulled-back mod2 cocycle. Independently enumerated ALL subsets of 17 vertices of sizes 1..7 (131071? only sum through7=41225; exact script enumerated) and checked whether mod2 cycle with lambda=1 is supported there by GF(2) row-column spans. Counts [0,0,0,0,0,0,5], with exactly the five cited 7-sets. For EACH of the five induced seven-vertex complexes, a further independent exact face/link audit gives f=(7,21,14), every edge degree exactly two, all seven vertex links connected cycles, and rational rank(boundary_2)=13 on 14 triangles (hence an integral 2-cycle). Connected closed surfaces with Euler characteristic 7-21+14=0 and integral H2 nonzero are orientable tori; the nonzero ambient mod2 detector certifies the order-two integral class, not merely a mod2 phantom. This finite enumeration is exhaustive FOR THIS 17-vertex input and supported by exact chain identities; not a theorem for all flat manifolds. Lutz original Table 9 independently confirms H2(Z)=Z/2 and this f-vector.

## originality

PASS

Best-of-knowledge PASS. Lutz gives the original B3 triangulation and integral homology but neither shortest-support cardinality nor five exact torus representatives. Resultary found related B4 one-vertex Bockstein gap and 15-vertex three-torus carrier results, which have different ambient complexes/homology and do not entail five B3 supports. The proof computes an unreported minimal embedded carrier spectrum for this canonical triangulation.

## value

PASS

PASS. The least vertex-support of the unique integral torsion H2 class and the complete set of minimal embedded torus representatives are natural finite combinatorial/topological invariants of a named small triangulation. The exact cutoff 7 and multiplicity 5 are not an arbitrary slice; they show how torsion is geometrically carried and are reusable benchmarks for combinatorial systoles and integer versus mod2 homology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
