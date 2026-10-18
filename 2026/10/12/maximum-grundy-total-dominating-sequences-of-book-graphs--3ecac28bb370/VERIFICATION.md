---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Bipartition L={u,b_i},R={v,a_i} separates the open-neighborhood legality constraints, because L choices footprint only R and vice versa. On L, either choose all n b_i in arbitrary order or n-1 b_i then u last (if u chosen earlier it exhausts R); these are all length-n side sequences and there are n!+n(n-1)!=2n!. Symmetric for R. Any interleaving preserves legality and total domination; thus at most 2n, equality sets omit one vertex per part and count (n+1)^2. Ordered sequences count binom(2n,n)(2n!)^2=4(2n)!. Independent full sequence enumeration for n=1,2,3 gives (length,sets,ordered)=(2,4,8),(4,9,96),(6,16,2880), not proof of general n.

## originality

PASS

Foundational Brešar–Henning–Rall paper defines the open-neighborhood process; their later graph-products article bounds path/cycle Cartesian products, not star prisms or all maximum set/count. Published Resultary complete-multipartite result concerns ordinary closed-neighborhood Grundy domination of different graphs. Skew-zero-forcing scalar duality does not enumerate ordered sequences.

## value

PASS

Complete natural extremizer and ordering classification for the standard book family; the closed formula 4(2n)! and structural bipartition complement are independent combinatorial facts stronger than the scalar value, useful for graph-sequence enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
