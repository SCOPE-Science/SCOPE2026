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

The source file `verify_debruijn_decks.cpp` contains a standalone C++17 replay. Execute:

```sh
g++ -std=c++17 -O3 verify_debruijn_decks.cpp -o verify_debruijn_decks
./verify_debruijn_decks
```

Observed on the packaged source: `VERIFY_OK`. The program enumerates all \(2^{16}\) feedback permutations, checks every valid length-\(32\) state orbit, and independently generates and deduplicates Euler tours of the order-four binary overlap graph. The resulting sets of \(2{,}048\) canonical words are exactly equal. For every canonical word it computes the entire length-\(k\) scattered-subsequence set by both the inductive dynamic recurrence and an independent earliest-match algorithm at all \(8\le k\le14\). It compares complete deck bitsets, never just hashes. It verifies the seven class counts, the exact length-\(13\) class-size profile, the length-\(14\) singleton property, and the two-bit-distance pattern of all ambiguous pairs. The generated list coincides with `ambiguous_pairs.csv`.

An independent Python earliest-subsequence control evaluated both members of the example pair (`05634ef9`, `05634fb9`) and confirmed equality at \(k=12,13\), inequality at \(k=14\), and a distinguishing subsequence `10001000011110`. These are finite exhaustive checks and not an all-order proof. External mathematical audit has not been performed.
