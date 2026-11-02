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

The code is identified exactly by the nine stabilizer Pauli strings embedded in both standalone checkers. The source's 512-word stabilizer weight distribution is reconstructed and used to verify nondegeneracy up to four erased qubits.

Compile and execute `erasure_census.cpp` using C++17. It constructs the symplectic commutation matrix and independently enumerates all \(2^{20}\) erased sets with rank calculations. The output includes `FOUR_ERASURE_KERNEL_HIST 0:3840 1:970 2:35` and ends with `ERASURE_CENSUS_OK`.

Execute `python3 verify_local.py` with a standard-library Python 3 interpreter. Instead of the rank algorithm, it enumerates every one of the \(4^4\) possible Pauli operators supported on each of the \(4845\) four-sets, checks each of their commutators, and verifies the \((3840,970,35)\) histogram, 35 commuting two-generator local normalizers, and 1075 weight-four logical operators. Its output ends with `LOCAL_ENUMERATION_OK`.

The finite computation establishes only the stated finite code invariant. No external formal verification or separate mathematical audit has been performed.
