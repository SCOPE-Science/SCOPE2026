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

# Exact finite verification

Run `python3 verify.py` from any working directory with `verify.py` and `kernel_certificate.json` in the same folder. Python 3.9+ standard library is sufficient; no downloaded datasets or third-party modules are required.

The graph is rebuilt as the disjointness graph on ten pairs from a five-set. Its fifteen edges are ordered lexicographically, and all ordinary matchings of size 1 through 5 are enumerated. Integer simplicial boundaries use the alternating face-deletion signs. Exact integer multiplication checks that consecutive boundaries compose to zero. Bitwise elimination gives the four mod-two boundary ranks \((14,61,79,6)\).

The certificate provides eleven sparse integer third-cycle columns, eleven row indices, and a two-sided integer coordinate inverse. All 11 vectors are checked as integer cycles, the inverse equations are checked exactly, and the fourth-boundary image is verified to occupy exactly their first six-dimensional span. The resulting rational dimensions and characters therefore follow from explicit linear algebra over the integers and rationals, not floating-point approximations.

For every one of the 120 permutations of the five labels, the program checks the full transformed cycle coordinates, all signed simplicial-chain traces, the degree-three kernel-minus-boundary character, and the degree-two Hopf-trace identity. It compares these with the closed character formulas in `RESULT.md` and checks full- and alternating-group invariant dimensions. Expected final marker: `FULL_S5_HOMOLOGY_REPRESENTATIONS_VERIFIED`.

These computations prove the finite rank and character statements because every face and group element is exhausted. They do not establish a new integral lattice decomposition, a general graph-family theorem, a homotopy-equivariant wedge splitting, or absence of prior equivalent publications.
