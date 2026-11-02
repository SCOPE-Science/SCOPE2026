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

# Reproducibility and limitations

`check_incidence.py` independently assembles the binary incidence adjacency matrix, raises it to consecutive powers, performs finite-field row reduction, and compares predicted ranks, rigidity, and exact first-entry counts. It enumerates every connected labelled simple graph on \(2\le n\le6\) vertices and finds exactly one nilpotent-in-three base graph for each even order (the complete one), none for odd orders. It checks clique ranks for \(2\le n\le14\), and exact state censuses for \(2\le n\le5\). The recorded result ends with `VERIFICATION_OK`.

`check_states.cpp` separately implements neighbor-sum updates as explicit bit-mask transitions, enumerates all states on \(S(K_n)\) for \(2\le n\le6\), and compares periodicity, entry times and eventual periods with the theorem. Its largest test checks all \(2^{21}=2,097,152\) configurations on \(S(K_6)\). Recorded output ends with `CPLUSPLUS_VERIFICATION_OK`.

Only source text and recorded ordinary output are supplied; C++ may be compiled with a standard C++17 compiler. These computations are not exhaustive in graph size or field order and do not prove the statements for arbitrary sizes or finite characteristic-two fields. Those limits are resolved for correctness by the symbolic proof in RESULT.md, not by extrapolation from checks. No independent audit has been performed.
