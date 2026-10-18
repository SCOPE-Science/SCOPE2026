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
# Reproduction instructions

Execute the bundled `verify_cycles.py` and `verify_deletion.py` using Python 3, without third-party packages. Both files independently construct the same twenty-four-vertex LCF graph and compute the required finite statistics. Their complete expected output appears in `verify_cycles.out` and `verify_deletion.out`. Both scripts were executed, finished normally and printed `VERIFY_OK`.

The first enumerator roots each simple cycle at its least vertex, removes reversal duplicates by comparing the second and last vertices, checks no cycles of length three through six, and records exactly thirty-two cycles of length seven. The incidence bound of at most ten cycles per vertex proves the lower bound without an experimental extrapolation. It then checks all \(\binom{24}{4}=10626\) candidate transversals against every cycle using exact integer bitmasks. Complete agreement with the stated family is asserted by the code. The exchange is checked directly.

The independent verifier computes girths of all induced vertex-deletion graphs by breadth-first search, without importing or using the cycle list of the first program. It checks all \(\binom{24}{3}=2024\) triple deletions, all \(10626\) quadruple deletions, the explicit twenty-set classification, residual girth eight, the exchange edge count and component sizes.

The two source programs themselves are the verifiable finite certificates; the text outputs are replay comparisons, not substitutes for algorithms. The result does not establish any asymptotic assertion, infinite-case theorem, global publication priority or external certification.
