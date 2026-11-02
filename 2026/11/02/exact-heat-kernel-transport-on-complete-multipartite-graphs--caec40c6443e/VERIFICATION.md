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

# Reproducibility and limits

Execute `python verify.py` in the same directory. The code requires only Python 3 standard-library modules and uses exact fractions throughout. It generated `CERTIFICATE_OK rational_instances=111 pair_tests=1605` when run on the included file.

The checker constructs the heat matrix from spectral components and, independently, enumerates all integer graph-Lipschitz potentials with an anchored vertex for all integer part partitions of orders 2 through 7 and heat-exponential bases 1, 1/2 and 2/3. It checks all unordered vertex pairs, including same-part pairs. Total unimodularity of the edge-incidence constraint matrix and diameter at most two justify exhaustion of the finite potential search for these particular graphs. The proof for arbitrary order and arbitrary real time is the self-contained transport/spectral argument in `RESULT.md`; the finite tests alone cannot establish that infinite statement.

The public source comparisons were confined to inspected relevant sections and accessible materials, so publication priority beyond them is not certified. No independent scientific audit has been performed.
