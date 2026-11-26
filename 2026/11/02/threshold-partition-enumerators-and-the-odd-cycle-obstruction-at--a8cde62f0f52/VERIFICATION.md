---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At degree at most two, the forbidden induced graphs leave just isolates and at most one edge-bearing component, which must be P2, P3 or C3. On a path, fixing the start of a unique long monochromatic run of length 2 or 3 uniquely determines the rest, yielding n-1 and n-2 choices. With two long runs the number at k total runs is 2 floor(k^2/4) for each ordered pair of lengths. Summing at k=n-2,n-3,n-4 with multiplicities 1,2,1 gives 2(n-3)^2; the inactive terms at n=3 are zero. On a cycle, one long run has parity-forced length and n choices of first vertex. With two, an admissible pair of excesses e1,e2 has 2k=n-e1-e2 runs; boundary double counting gives nk and the permissible excess pairs give n(n-3), including C4. C3 has four assignments activating each color, counting the two monochromatic assignments. Forbidden cross-component 2K2s are precisely the x^2 and y^2 terms. Each odd cycle consumes one color's defect budget; two odd cycles can use distinct colors and three cannot. Proper three-colorability supplies the upper bound. The alternating reformulation is about acyclicity within each color class, not the stronger cross-class requirement. Independently corroborated by branches/d46b48ce-6757-4165-9f07-a40aaa9e5096/independent_threshold_check.py: 26 single graphs, 134 disconnected unions, 24 triangle/5-cycle mixtures and arithmetic formula checks through order 1000. Finite checks do not establish the general result; the argument in RESULT.md lines 63–86 does. The source verifier was inspected, not executed.

## originality

PASS

The exact count of named two-color threshold partitions on arbitrary degree-two graphs, and the associated two-defect budget criterion, are distinct from the strongest checked results. The equivalence to the alternating chromatic number is already known and is not credited as new. Complete multipartite graphs overlap only in small or edgeless cases; general hardness and proper-coloring results do not imply the classified family.

## value

PASS

The four-state exact invariant solves a natural disconnected counting problem where locally valid restrictions need not combine: two disjoint edges in one color invalidate the union. The path and cyclic counts give reusable factors, and the single budget per named color explains why the third odd-cycle component, not the first, forces a third class. This is more informative than the known equivalence, proper coloring, or decision feasibility alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
