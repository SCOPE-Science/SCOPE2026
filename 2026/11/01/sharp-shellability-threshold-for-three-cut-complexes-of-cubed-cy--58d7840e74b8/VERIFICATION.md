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
# Reproducible mathematical verification

Use Python 3 with its standard library. Place `verify.py`, `order13.txt`, and `order14.txt` in one directory and run `python3 verify.py`.

The verifier reconstructs all three-cut facets of \(C_n^3\) for \(9\le n\le14\) from induced-subgraph connectivity, with no external tables. For \(n=9,10,11,12\), it constructs all simplicial faces and exact \(\mathbb F_2\)-boundary maps, computes ranks, and confirms the only nonzero reduced mod-two Betti numbers are respectively \((3,1),(4,11),(5,1),(7,2)\), where each pair denotes degree and rank.

For \(n=13\), the shelling order has \(169\) facet rows and exactly one spanning facet. For \(n=14\), it has \(238\) rows and eight spanning facets. Every row is checked to encode an actual facet and every facet must appear exactly once. The shelling attachment criterion checks each preceding facet against every new facet. A separate direct maximal-intersection calculation (not required for package replay) also checked all attachment steps and found every maximal old intersection to have codimension one.

The executed checker concluded with `ALL_VERIFY_OK`. These finite computations do not prove the published infinite-range theorem; the latter is invoked explicitly as an external published mathematical premise. Independent audit has not been performed.
