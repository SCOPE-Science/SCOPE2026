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
# Reproducible finite checks

Place all included files in one directory and run:

```sh
c++ -std=c++17 -O2 enumerate.cpp -o enumerate
./enumerate > recomputed_stats.txt
c++ -std=c++17 -O2 verify_direct.cpp -o verify_direct
./verify_direct > recomputed_direct_output.txt
c++ -std=c++17 -O2 verify_phase.cpp -o verify_phase
./verify_phase > recomputed_phase_output.txt
python3 verify_symmetry.py > recomputed_symmetry_output.txt
cmp stats.txt recomputed_stats.txt
cmp direct_output.txt recomputed_direct_output.txt
cmp phase_output.txt recomputed_phase_output.txt
cmp symmetry_output.txt recomputed_symmetry_output.txt
```

The first program enumerates the complete \(3^{12}\)-state functional graph by indegree peeling. The direct-iterate program checks \(F^9(x)=F^6(x)\) for each state, finds entrance times and basin sizes by exact integer arithmetic, and lists all sixty six-step witnesses. A separate phase-enumeration program checks the cyclic successor-neighbor condition independently of the dynamics. The Python program verifies the full graph automorphism group and recomputes the geometric orbit-size distribution from the first program's periodic representatives. Each program prints `CHECK_OK` or asserts expected values; no probabilistic or numerical-tolerance criterion is used.

The integer code 3156 corresponds to vertex-order digits \((0,2,2,2,2,0,1,1,0,0,0,0)\). The direct iterator computes codes at times \(0\) through \(9\): 3156, 268516, 525488, 969, 1701, 177718, 423026, 157050, 217084, 423026. The first repeated three-step value occurs between times six and nine, so the six-step bound is sharp.

The finite-state verification does not certify analogous statements for larger graphs or different excitation rules. It is not an independent external audit.
