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

# Verification and scope

The analytic proof resides in `RESULT.md`. To verify the finite corroboration, run the following commands in a directory containing all packaged files:

```sh
c++ -std=c++17 -O2 verify_corona.cpp -o verify_corona
./verify_corona 10
python3 verify_compressed.py
```

`verify_corona.cpp` independently builds all neighbors of the simple graph and obtains cycles and basin sizes from the entire functional graph by indegree peeling. It checks \(1{,}398{,}096\) labelled configurations for \(2\le n\le10\), all orbit counts, all individual basin sizes, first-periodic-entry distributions, and the identity \(F_n^5=F_n^3\). `verify_compressed.py` separately enumerates the compressed update for \(2\le n\le8\) and reconstructs cycles and basins with a different traversal. Captured outputs are `cpp_verification.txt` and `python_verification.txt`; the programs produce no external-network requests. All counts reported by the submitted runs matched the analytic formulas.

The programs are finite consistency checks, not exhaustive proofs for every \(n\). Infinite-scope correctness rests on the displayed exact case formulas and the two-cycle/basin derivations. No independent external audit or formal certification has been carried out.
