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

# Finite exact verification

The sole executable artifact is `verify.cpp`, a self-contained standard C++17 program. Compile with `g++ -O3 -std=c++17 verify.cpp -o verify` and run `./verify`. The checker creates the affine evaluation code independently of the parity-check construction and checks that all thirty-two affine words are distinct, annihilated by the parity checks, and have nonzero Hamming weight at least eight. It computes the exact joint coset distance at **every** one of the \(2^{22}\) pairs of syndromes twice: first by a sixteen-step syndrome dynamic program, and second by forming canonical representatives and minimizing over all pairs of thirty-two affine words. Direct search prunes only if a proven per-row lower bound is reached or a first-row mask already meets the current best joint support.

Recorded output after compilation and execution:

```text
VERIFY_OK
code=[16,5,8]_2; number_of_two_row_cosets=4194304
R_2=9; distance_9_cosets=336; witness_syndrome=(373,207)
distribution=1,48,1080,15120,144585,858144,2359602,798000,17388,336
```

The two algorithms agree for each syndrome pair individually, not merely on their aggregate histograms. The histogram sums to 4,194,304. The verifier uses only finite integer operations; there are no floating-point tolerances, randomized choices, or external libraries. Its correct execution and the recurrence proof certify this finite case only, without asserting any infinite-parameter theorem or independent audit. No external validation has been performed.
