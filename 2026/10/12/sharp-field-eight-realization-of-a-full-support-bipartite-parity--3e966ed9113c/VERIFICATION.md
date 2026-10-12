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
# Reproducibility

Run `python3 verify.py` with standard Python 3. The code enumerates every subset of size one to five among the 36 edge columns, performs exact Gauss elimination over the irreducible binary field polynomial `0b1011`, and checks a rank-five six-column dependence. It also checks all four-cycle minors and full row ranks in four prescribed bipartite masks, and independently rejects all 720 possible field-seven third-row permutations after normalization. The expected final line ends in `VERIFY_OK`.

This exhaustive computation is finite evidence for the concrete \(\mathbb F_8\) instance only; the all-prime-power family and the field-size minimality rely on the explicit proofs in `RESULT.md`. The field-seven contradiction is symbolic, not inferred from a failed random search. No separate external validation has been conducted.
