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

# Direct reproducibility
Run `python3 verify.py` in this directory. The sole required dependency is Python 3.8+ with its standard library. The file `verification_output.txt` is the captured expected output.

The checker enumerates all \(65536\) possible labeled binary four-cube colorings, with every geodesic realized as an ordering of differing bits. All \(24\) accepted colorings are independently retested with a breadth-first shortest-path search, and all are confirmed to be eight/eight, antipodally symmetric, and in one coordinate-permutation/bit-flip orbit. Direct breadth-first tests verify the two- and three-cube witnesses and the four classes on the five-cube.

The exact lower bound \(\chi_{\mu_{\mathrm d}}(Q_5)\ge4\) uses the published theorem \(\mu_{\mathrm d}(Q_5)=10\) in Korže and Vesel, *Variety of mutual-visibility problems in hypercubes*, Theorem 3.14. This external result was read in its full-paper context and is not independently recomputed or certified here; the finite checker is not proof of that separate published computation. No higher-dimensional exact value or independent audit is asserted.
