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

# Reproduction and limits
Run `python checker.py` with Python 3.9 or later, from the directory containing this document and the checker. No external packages are required. The program independently enumerates the finite reachable-state graph, performs Moore partition refinement, evaluates the exact positive-carry/residue formula, verifies the dyadic closed form on accessible shifts, and computes direct outputs.

The recorded output in `checker_output.txt` gives `CHECK_OK parameters=1032 direct_inputs=132096`, followed by state counts at representative shifts. The test domain is all integer moduli from 2 to 9, shifts from 0 to 128 inclusive, and input numbers from 0 to 127 inclusive. The checker uses fixed-length 7-bit least-significant-first inputs for direct output comparisons, including high zeroes; the formal proof separately establishes correctness on all finite words including the empty input.

Independent external verification has not been performed. Finite tests are not an infinite proof: the complete symbolic argument, including distinguishability of positive-quotient residual functions, is presented in `RESULT.md`.
