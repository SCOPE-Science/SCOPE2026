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
# Verification
Run `python3 artifacts/verify.py` from any directory with Python 3 and a C++17-capable `g++` compiler. The script uses local source paths, recompiles both standalone programs, compares all sixteen totals with `artifacts/expected_counts.tsv`, and checks canonical histograms, normalized counts and the predicted two highest multiplicities from length four through sixteen. Both full enumerations must terminate successfully; no network access, random seeds, external packages or historical files are required.

The first method generates every restricted-growth ternary equality pattern. The second independently generates all ternary words whose first letter is zero; alphabet relabeling guarantees full coverage. These algorithms use distinct Parikh implementations, and their deduplicated counts agree on the exact observation signatures. The generic identity defining the observation and the proof of uniqueness of restricted-growth representatives explain why this constitutes exhaustive verification rather than sampling.

The all-length extremal assertion follows from the combinatorial branch argument in `RESULT.md`, not from matching the finite histogram. The enumeration explicitly stops at length sixteen; larger totals and lower-tier all-length fiber patterns are not claimed. No independent audit has been performed.
