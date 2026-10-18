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

Place `verify.py` beside `morse_certificate.json` and run `python3 verify.py` with Python 3.10 or later. Both are standalone and use no third-party packages.

The script reconstructs the two explicit 16-vertex adjacency matrices, checks the 4-regularity of each, and computes their full characteristic-polynomial coefficients by exact integer Faddeev–LeVerrier recurrence. It enumerates all \(65{,}536\) vertex masks of each graph using the graph-edge condition. It reports the nine-term independence-polynomial coefficient tables and confirms their difference is \(4z^5\).

For the Morse certificate, it reconstructs all pivot pairs from the universal rule. The JSON certificate stores every matched pair, every critical-face mask, and a linear order of every nonempty face. The script verifies these data against freshly generated face sets; it reconstructs *all* \(2836\) Hoffman and \(2816\) four-cube nonempty-face Hasse incidences, orients them using the matching, and checks the stored order increases strictly along each incidence. A separate complete topological-sort traversal again establishes acyclicity. The critical cells are exactly one zero-cell and three three-cells for the Hoffman graph, respectively one zero-cell and seven three-cells for the cube.

Independently, binary Gaussian elimination of every simplicial boundary gives the reduced boundary-rank vectors \((1,15,73,135,90,42,14,2)\) for the Hoffman graph and \((1,15,73,135,86,42,14,2)\) for the cube, with corresponding sole nonzero reduced mod-two Betti ranks three and seven in degree three. The integral wedge homotopy types follow from the acyclic Morse certificates, **not** from these field calculations alone.

A successful replay prints `VERIFY_OK_HOFFMAN_Q4_SPECTRAL_INDEPENDENCE_HOMOTOPY`. Assertions, enumeration and the explicit certificate are the evidence; an output log on its own is not a proof. This is an exact exhaustive finite calculation on two graph definitions, not a claim for all graphs with sixteen vertices or other cospectral pairs.
