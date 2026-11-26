---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible finite-distance verification

Run `python3 verify_python.py` for complete searches on explicitly constructed switch graphs. Alternatively compile and run `g++ -std=c++17 -O2 verify_cpp.cpp -o crown_check && ./crown_check` for on-demand neighbor generation in the breadth-first searches. The recorded outputs are `verify_python.out` and `verify_cpp.out`. The per-size summary fields agree; the C++ output additionally exposes the smaller cycle-type profiles in the `types` fields.

For the first-occurrence claim, check connectedness and maximum eccentricity for each of \(n=4,5,6,7,8\). The exact diameters are \(3,4,6,7,8\), and the known nine-symbol diameter ten is also recomputed. The nine-symbol histogram and antipode census are reproduced in the output as endpoint context, not claimed as distinct new findings. There is no diameter extrapolation to arbitrary \(n\).
