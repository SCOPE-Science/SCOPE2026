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

The standalone C++17 certificate `verify_directed.cpp` was compiled with `g++ -O3 -std=c++17` and executed successfully. It enumerated 1, 18, and 1606 strongly connected labeled directed graphs on 2, 3, and 4 vertices, respectively, with 397956 directed-arc configurations evaluated in all their percolation states. At order four it found precisely 24 relabelings of the seven-arc exceptional graph, confirmed its exact coefficient vector, and proved all other graphs have nonpositive Bernstein coefficients. For complete transmission it enumerated 565080 strongly connected labeled digraphs on five vertices, found 15180 with a worse acquaintance-vaccination outcome, and identified precisely 120 relabelings of the unique sparsest eight-arc class. Exact witness polynomials and full-transmission means were recomputed.

These are finite exhaustive computations with explicit bitmask enumeration and integer reachability, not general statements derived from sampling. The assertions depend on the source and compilation model; independent replication and scientific audit have not been performed. No empirical epidemiological calibration or real-world effectiveness conclusion is claimed.
