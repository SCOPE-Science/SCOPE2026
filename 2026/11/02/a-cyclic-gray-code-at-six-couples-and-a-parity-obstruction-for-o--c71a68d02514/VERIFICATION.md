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

# Reproducible checks

Run `python3 verify_menage.py` and then `g++ -std=c++17 -O2 verify_menage_alt.cpp -o verify_menage_alt && ./verify_menage_alt` with `hamiltonian_cycle.txt` in the same directory. The Python checker exhausts the valid permutations for 3 through 6 and checks components, edge counts, all-source distances, and all 80 cyclic certificate transitions. The C++ checker independently enumerates all 3-through-9 permutations to compare even/odd counts, then constructs the six-permutation graph by direct pair comparisons, checks the Hamiltonian certificate, and computes all-source distances. Output seen: `CYCLIC_MENAGE_GRAY_CODE_OK` and `ALTERNATE_HAMILTON_CYCLE_OK vertices=80 edges=207 eccentricities=5:48,6:32`.

The symbolic all-order parity proof in `RESULT.md` uses the eigenvalues of \(J_n-I_n-P_n\), so verification for finitely many \(n\) is confirmatory only. The certificate uses zero-based indices into lexicographically sorted valid six-permutations. It does not prove a Hamiltonian cycle at any other size.
