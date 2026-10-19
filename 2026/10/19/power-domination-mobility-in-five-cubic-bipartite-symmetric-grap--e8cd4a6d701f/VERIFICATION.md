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

# Reproduction

Python 3 standard library: `python3 power_main.py --json --certificate`. Outputs: `power_main_summary.json`, `power_certificate.json`, and the recorded `power_main.out`.

Independent C++17 compilation: `g++ -std=c++17 -O3 power_crosscheck.cpp -o power_crosscheck` followed by `./power_crosscheck`. The recorded result is `power_crosscheck.out`.

The Python implementation enumerates every vertex subset up to the first feasible size, uses closed-neighborhood initialization and repeated unique-white-neighbor forcing, and generates every one-token exchange. It evaluates every source for smaller graphs and an explicit sixteen-orbit representative system under six-symbol permutations for Tutte–Coxeter. The C++ implementation separately enumerates every candidate bitmask, rebuilds both reconfiguration graphs and evaluates shortest paths from every state, including all 6540 Tutte–Coxeter minima.

A certificate record contains the labeled original graph edges, all minimum sets as integer masks in **their stored order**, and undirected exchange pairs as zero-based indices into that stored list. Every exchange requires exactly two differing mask bits, and every sliding edge also requires adjacency of the exchanged vertices in the original graph. No solver, network service, external data files or prior result is needed to reproduce the certificate and numerical claims.

The experiments exhaust all finite cases in the claimed domain; they do not prove any extension beyond the five named graphs. Independent external scientific audit has not been performed.
