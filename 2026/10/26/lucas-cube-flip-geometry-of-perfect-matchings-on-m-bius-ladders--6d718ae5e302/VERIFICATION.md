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

The two standalone checkers in this package were executed with Python 3 from the directory containing the files:

```
python3 check_direct.py > direct_output.txt
python3 check_construct.py > construct_output.txt
```

`check_direct.py` builds the graph as a literal set of edges, recursively enumerates every perfect matching by choosing the least unmatched vertex, toggles every canonical four-cycle, checks undirected switch symmetry and verifies exact component sizes for \(4\le n\le16\).

`check_construct.py` independently enumerates circular binary words, constructs each perfect matching from disjoint doubled horizontal pairs and rungs, checks every permitted single-bit flip against its two-edge switch, constructs both rung-free helical configurations at odd widths, and verifies exact counts and Hamming diameters for \(4\le n\le16\).

Both programs completed successfully and reproduced the included output files. The all-width assertions depend on the symbolic proof in `RESULT.md`; the finite programs corroborate the boundary conditions and the combinatorial interpretation and do not serve as an infinite certificate. The only move type permitted is a four-cycle switch; the exceptional six-vertex Möbius ladder and arbitrary longer-cycle moves are outside scope.
