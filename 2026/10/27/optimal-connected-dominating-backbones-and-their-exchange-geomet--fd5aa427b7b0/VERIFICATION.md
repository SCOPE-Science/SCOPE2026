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

# Finite verification record

Execute `python3 verify.py` with standard Python 3, from a directory containing the script. It constructs vertices as integers 0 through 15, uses XOR by the four unit bits for adjacency and represents subsets by length-16 bit masks.

**All-domain enumeration:** All subsets of sizes 1 through 5 are checked for joint connectedness/domination, and all 8,008 six-subsets are checked. It obtains 192 successful sets. The path-word generator independently yields the same 192 sets. All 384 cube automorphisms are explicitly generated. All 1,952 connected six-subsets partition into 11 automorphism orbits; only the 192-element orbit covers all 16 vertices.

**Graph check:** The exchange graph is constructed by symmetric-difference cardinality two, with each of its 192 vertices having four neighbors. All 192 breadth-first searches agree on the eight-entry shell vector, so both its diameter and its 18,336 unordered pair distances are exhaustively determined.

**Analytic component:** The counting contradiction for connected five-subsets, together with a size-six example, proves the minimum without relying on a numerical search alone. The finite orbit and exchange computations then prove the more detailed classification. The maximum-leaf spanning-tree consequence is the standard nonleaf connected-dominating-set equivalence.

**Limits:** The script does not verify originality, absence of unpublished earlier work, or an all-dimensions theorem. It does not perform an independent audit. A different induced path on six vertices need not dominate; the precise flip-word condition is essential.
