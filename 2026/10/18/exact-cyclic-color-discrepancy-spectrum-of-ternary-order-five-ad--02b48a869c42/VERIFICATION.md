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

# Reproduction and boundaries

From the package directory, run the two independently organized exhaustive enumerators and the direct witness checker:

```sh
c++ -O2 -std=c++17 verify_dfs.cpp -o verify_dfs
./verify_dfs
c++ -O2 -std=c++17 verify_pairings.cpp -o verify_pairings
./verify_pairings
python3 verify_witnesses.py
```

The first enumerator roots a directed Eulerian edge walk at the unique `01010` factor and explores every unused outgoing edge. The second selects and exhausts all 16,777,216 local pairings of incoming and outgoing edges, accepts only permutations that form a 48-cycle, and computes discrepancy independently. They independently produce the vector `23700,420924,341808` at discrepancy values `3,4,5`, with exact total `786432`. The third reconstructs all 48 permissible cyclic five-factors and computes all cyclic intervals from scratch for the three provided witnesses. The code detects unexpected values or different histograms with a nonzero exit status.

The enumeration-to-cycle bijections and prefix-range identity are proved in RESULT.md. This finite exhaustive computation is an exact finite argument only for the specified graph; it proves no theorem at larger orders. No independent external audit or independent validation has occurred.
