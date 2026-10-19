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

# Finite verification of two four-coloring reconfiguration dynamics

The companion `verify_recolorings.py` is a self-contained Python 3 checker. Run `python3 verify_recolorings.py` with no third-party dependencies. Its actual successful output is embedded in `checker_output.txt`, with a final `VERIFY_OK` assertion marker. The program constructs the precise twenty graph edges, proves three-colorability impossible by exhaustive enumeration and enumerates all four-colorings twice: descending-degree constraint backtracking, and independent cycle/apex/shadow palette products.

For each coloring it enumerates *all* legal single-vertex recolors and all induced-bichromatic-component Kempe switches and checks every generated edge directly. Breadth-first search and disjoint-set union independently check component sizes. Each of the 24 global color permutations is checked for the claimed component-sign action. The 10 dihedral graph automorphisms are checked edgewise, and full normalized partition orbits under these operations are enumerated. Breadth-first search from one representative of each of the 56 full orbits recovers every state's eccentricity by symmetry. The complete number of reachable states is independently checked in each breadth-first search.

The program confirms 12,480 colorings; 45,240 single-recolor edges in two 6,240-state components with radius 15 and diameter 17; 87,120 Kempe edges in one component with constant eccentricity 7; 37,440 crossing Kempe edges; the displayed exact state eccentricity counts; and the global-color-permutation sign law.

**Limits.** This constitutes a complete *finite* exhaustive computation for the particular graph and four named colors, not an inference about all graphs, all Mycielski graphs, or unbounded palettes. Code correctness is supported by redundant generation and component algorithms but has not been independently audited. The known static chromatic count is not asserted to be a new discovery.
