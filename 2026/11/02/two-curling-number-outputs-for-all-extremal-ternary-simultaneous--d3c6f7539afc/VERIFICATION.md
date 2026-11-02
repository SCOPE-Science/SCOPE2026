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

# Reproducibility and verification

Run `python3 verify_canonical.py` in this directory. It enumerates one first-occurrence-normalized representative for each global alphabet-permutation class; its terminal outputs are in `canonical_output.txt`. It checks that every terminal representative uses all three letters and that no valid length-85 continuation exists. The distribution is 1008 representatives, with output frequencies 672 and 336, hence 6048 labeled inputs with frequencies 4032 and 2016.

Compile `verify_full.cpp` using `c++ -O2 -std=c++17 verify_full.cpp -o verify_full` and execute `./verify_full`; the recorded combined standard output/error is `full_output.txt`. Unlike the first program, it traverses all three labeled letters at every extension and obtains curling numbers from the general largest-suffix-power definition. The second program reports identical 84-step output strings and 4032/2016 fibers, as well as 0 admissible length-85 sources. It explicitly checks the two outputs share exactly 83 initial positions.

These are finite exhaustive checkers for the stated length, not extrapolations to an infinite family. The primary theorem's sharp length and total terminal word count are also independently reproduced, but those prior results are not presented as new. An independent audit has not been performed.
