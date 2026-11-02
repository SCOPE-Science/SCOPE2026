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

# Exact finite verification

The two standalone C++17 programs exhaustively enumerate all binary words of lengths one through twenty-three, using one reversal-orbit representative at a time and adding its one- or two-word multiplicity. The first computes substring composition counters by incremental right-endpoint extension; the second computes them by differences between prefix ones-counts. Equality is tested on all the counter bytes. Both were run with the embedded `data/census.csv` and `data/fourfold_23.tsv` and reported successful completion; the independent checker printed `CROSSCHECK_OK all orders 1..23, including every length-23 collision class`.

For every length, the checker validates the exact number of spectra, all observed fiber-size counts, the largest observed fiber, and the total number of input words. For length twenty-three it also independently recreates and matches the complete list of 160 exceptional four-element classes. The consistency identity for that length is \(4{,}096+2\cdot4{,}191{,}936+4\cdot160=8{,}388{,}608\).

To replay, compile `build_census.cpp` and `verify_independent.cpp` with a C++17 compiler (for example, `c++ -O3 -std=c++17`), then run the first program with paths to the two bundled data files as output arguments and the second with those files as input arguments. The programs require substantial memory at length twenty-three (roughly two gigabytes); their completion is finite, not asymptotic verification. The code and tables are self-contained and do not import third-party libraries.

Known limits: no claim for length twenty-four or higher, no result for noisy or partial composition information, and no independent scientific validation performed.
