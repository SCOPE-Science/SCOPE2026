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
# Reproduction checks

The three files `witness.txt`, `verify_witness.py`, and `solve_upper.py` are standalone. The first checker uses explicit length-nine binary tuples and validates every possible zero-error or one-overwrite received word for every one of 78 claimed codewords. It reports `WITNESS_OK` only after checking exact pairwise disjointness; the reproduced distinct-output count is 396.

The second checker constructs all 256 possible length-nine words beginning with zero and all 2816 conflicting pairs by output-set intersection. It optimizes the resulting 256-variable binary independence program with SciPy/HiGHS and requires global optimality status, objective 39, matching dual bound, and zero gap before reporting `UPPER_BOUND_OK`. It does not assume that a timed-out run disproves any code size.

The complement operation transfers the certified 39-word half-code bound to the other leading-bit half. The two halves can coexist because the first received bit cannot change. Accordingly the sum 78 is exact if the solver's global optimality report is correct.

The upper-bound argument is computational and solver-dependent. There is no separate formal integer-optimization certificate or independent mathematical audit. The result makes no claim about correcting two grain errors, any larger block length, or the performance of practical stochastic media.
