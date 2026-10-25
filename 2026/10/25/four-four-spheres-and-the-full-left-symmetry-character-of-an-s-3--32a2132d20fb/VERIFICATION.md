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
# Verification

`verify.py` reconstructs all twelve right Cayley arcs of the group with presentation \(r^3=s^2=1\), \(srs=r^{-1}\); it does not rely on imported graph libraries or cached face tables. All \(4096\) arc subsets are checked against independent predecessor-walk and directed topological-sort criteria. Exactly \(432\) are faces counting the empty face, with cardinality counts \((1,12,57,134,156,72)\).

For nonempty faces, an exact ascending-arc-index matching pairs \(213\) facet incidences, leaving one critical zero-cell and four critical four-cells. A full topological sort of the modified Hasse graph over \(431\) nonempty faces and \(1500\) cover incidences verifies that no closed gradient path exists. This is a finite complete certificate for the wedge of four four-spheres via discrete Morse theory, not a sampling argument.

The same executable enumerates every left multiplication as a permutation of the twelve arcs, verifies face-set preservation, computes all signed fixed-face simplicial chain traces, and derives the character \((4,-2,1)\) on identity, transposition, and three-cycle. The standard rational character table gives multiplicities zero trivial, two sign and one standard. Separate simplicial boundary reductions over the primes \(101\) and \(103\) give ranks \((1,11,46,88,68)\), consistent with the Morse description but not a substitute for its integral proof.

Run with `python3 verify.py`. An actual run is recorded in `VERIFY_OUTPUT.txt` and ends in `VERIFY_OK`. This documents a complete finite mathematical check; it is not an independent scientific audit. The rational representation description does not classify the integral module lattice, and possible unindexed published overlap remains a scientific limitation.
