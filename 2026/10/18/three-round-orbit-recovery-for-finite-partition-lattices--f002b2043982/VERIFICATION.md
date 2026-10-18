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

# Verification of the finding

The mathematical proof is in `RESULT.md`, Steps 1–4. The critical premises are (a) a partition with \(k\) blocks has exactly \(B_k-1\) strict coarsenings, (b) at fixed block count, a unique one-large-block type maximizes the number of strictly finer atoms, and (c) known one-large-block predecessor counts invert to the complete block-size profile. The proof gives a statement for every integer \(n\ge1\).

Executable checks, which are finite corroboration only:

- `python3 check_partition_lattice.py 8` constructs all \(\Pi_n\), \(1\le n\le8\), builds every pair in the full strict refinement relation, performs three synchronous counting-refinement steps on both in-neighbour and out-neighbour colours, and checks exact agreement with the block-size-type partition. The included `check_output8.txt` records successful checks of 5,295 total vertex instances.
- `python3 check_moments.py` independently tests binomial-moment inversion and the extremal atom-count recognition for every integer-partition type through \(n=30\). The included `moments_output.txt` records its complete check and success indicator.

The checks cannot establish the all-size theorem or publication priority; those questions depend on proof and literature comparison, respectively. No independent audit has been performed. In particular, no assertion is made that the three-round depth is optimal, or that the same depth holds for cover graphs or arbitrary finite partial orders.
