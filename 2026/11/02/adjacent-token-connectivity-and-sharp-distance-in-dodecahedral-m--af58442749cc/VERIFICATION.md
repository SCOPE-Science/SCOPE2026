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

# Reproducible finite verification

The two enclosed source programs reconstruct the simple \(20\)-vertex dodecahedral graph independently, then enumerate all \(\binom{20}{6}=38760\) candidate minimum feedback vertex sets using exact integer bit masks. The first program uses a union-find cycle check and generates each legal slide by replacing a selected vertex with a neighbor. The second uses a separate edge list with an explicit isomorphism, leaf-removal acyclicity, and examines every unordered pair of eligible masks for one-vertex symmetric differences along original graph edges.

Run `python3 verify.py`; it checks the local graph's vertex count \(2520\), edge count \(8880\), connectedness, internal stratum connectedness, stratum edge counts \((1620,3120,4140)\), and exact all-source eccentricity census \((8:120,9:2340,10:60)\). Run `g++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt` to perform the separate enumeration and all-source shortest paths. Successful executions terminate with `FINITE_CERTIFICATE_OK` and `ALTERNATE_CERTIFICATE_OK` respectively.

The unrestricted token-jump reconstruction is present only as a check against pre-existing background data; it is not part of the new novelty claim. A finite all-pairs enumeration suffices for this finite graph but does not prove any statement for arbitrary graph families. No independent human or external audit is claimed.
