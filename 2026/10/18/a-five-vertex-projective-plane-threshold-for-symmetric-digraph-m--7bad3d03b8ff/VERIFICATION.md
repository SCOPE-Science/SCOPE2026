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

# Reproducibility and verification

The research object is the multipath simplicial complex of the symmetric digraph on \(K_2\vee\overline K_3\). Run the bundled scripts from their shared directory, with Python 3 and SymPy installed:

```sh
python verify_census.py
python verify_homotopy.py
```

`verify_census.py` independently enumerates every graph-isomorphism type on one through five graph vertices; its expected type totals are 1, 2, 4, 11 and 34. It independently enumerates all multipaths, constructs every integer simplicial boundary, computes Smith invariant factors and checks the unique torsion case, seven edges, 140 nonempty simplices, ranks 13, 41, 12 and one invariant factor 2. Its canonical graph mask is 127. Expected output is `census_output.txt`.

`verify_homotopy.py` reconstructs the 140 faces without using the census enumerator; it checks the complete 65-pair list in `morse_certificate.json`, verifies an acyclic orientation of all 336 face-poset cover relations by topological sorting, performs exact unit-pivot integer cancellations and checks the residual attaching-degree vector against the sole critical one-cell. It checks the Morse differential squares to zero. Expected output is `homotopy_output.txt`.

The two-dimensional Morse CW model has one zero-cell, one one-cell and eight two-cells, attached with degrees \((0,0,0,-2,0,0,-2,0)\). The nonzero gcd of 2 and seven zero invariant directions give \(\mathbb{RP}^2\vee\bigvee^{7}S^2\). A Smith calculation alone would not justify that homotopy type; the complete acyclic matching plus degree calculation does. The finite exhaustive census proves uniqueness only within the stated small, symmetric, loopless simple-graph class, not an all-order or all-digraph claim.

Independent scientific audit has not been performed.
