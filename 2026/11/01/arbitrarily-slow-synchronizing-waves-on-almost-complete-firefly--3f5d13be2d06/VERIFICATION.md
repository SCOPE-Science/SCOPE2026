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

The proof is the all-parameter exact trajectory induction in `RESULT.md`, not an extrapolation of finite tests. It checks the graph's open neighborhoods, the case of a one-site suffix, the final release, and strict non-synchrony before the terminal uniform state. The path and core may have arbitrary sizes within the theorem's scope.

The independent adjacency-list C++ program `direct_replay.cpp` was compiled with a standard C++17 compiler and its output is embedded in `direct_replay.log`. The separate Python checker `verify_wave.py` evaluates the symbolic states against direct vertex updates; its output is in `verify_wave.log`.

Finite checks support but cannot alone certify every parameter. The source comparison identified prior path and tree synchronization theorems, not the stated almost-complete high-connectivity slow-wave construction. No external independent audit has occurred.
