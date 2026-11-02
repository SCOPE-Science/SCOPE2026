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

# Reproducible finite certificate

Build the included standalone `verify.cpp` with a C++17 implementation supporting 64-bit unsigned integers, e.g.

```sh
g++ -O3 -std=c++17 verify.cpp -o verify
./verify 32768 2
./verify 49152 32769
./verify 57344 49153
./verify 65536 57345
```

All four commands were executed and succeeded. The first completed 32,767 denominators and the other three completed 16,384, 8,192, and 8,192 denominators. The reported block totals, in order, were:

```text
PASS grids=32767 total_states=536920062 total_edges=1073608932 global_max_shortest_path=25 first_at_N=30432
PASS grids=16384 total_states=671113216 total_edges=1342100940 global_max_shortest_path=26 first_at_N=35684
PASS grids=8192 total_states=436219904 total_edges=872375708 global_max_shortest_path=26 first_at_N=50131
PASS grids=8192 total_states=503328768 total_edges=1006592960 global_max_shortest_path=27 first_at_N=58789
```

For selected denominators the source prints the following exact figures:

```text
N=255 states=256 edges=510 missing=0 max_path=12
N=256 states=257 edges=481 missing=2 max_path=12
N=65535 states=65536 edges=131070 missing=0 max_path=25
N=65536 states=65537 edges=130561 missing=2 max_path=25
```

The verifier builds the graph from **every integer state** using exact floors/ceilings, runs a complete reverse BFS from zero, and verifies the exact predicted nonreaching vertices. No random seed, trajectory length, floating-point approximation, statistical threshold or timeout inference is involved in its claim. A separate Python/SciPy strongly connected-components calculation for these four sample denominators found closed components \(\{0\}\) or \(\{0\},\{3/4\}\) as appropriate. The elementary final implication from the complete reachability certificate to Markov-chain recurrent classes and absorption is supplied in `RESULT.md`.

The Wasserstein formula follows independently from the continuum arcsine density, two-atom nearest-site transport, and the exact split at \(3/8\). High-precision numerical quadrature checked the reported decimal, but the result is the analytic integral and its closed form.

**Limits:** Certification is exhaustive only over 2..65536, not over all natural numbers. Reproduction depends on a conforming C++17 toolchain, sufficient memory for adjacency arrays, and running all four commands. Probability paths are mathematical Markov transitions with independent fresh randomness, not pseudo-random finite-period traces. No external or independent mathematical audit has been performed.
