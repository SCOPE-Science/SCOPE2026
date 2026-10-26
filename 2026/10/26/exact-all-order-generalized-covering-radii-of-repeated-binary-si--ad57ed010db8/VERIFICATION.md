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

# Finite checks and mathematical limits

The command `python3 verify_repeated_simplex.py` completed without assertion failures. The final line was `REPEATED_SIMPLEX_VERIFY_OK histograms=104498 matrices=8840 randomized=960`.

The verifier exhaustively enumerates all ordered triples of length-\(Q\) nonnegative integer histograms of mass \(m\), for \((t,m)\) ranging over \(t=1,1\le m\le7\); \(t=2,1\le m\le4\); \(t=3,1\le m\le2\); and \(t=4,m=1\). Because every target matrix is represented by exactly such a triple up to permutation within each generator block, this is exhaustive for each selected parameter pair. The program also performs genuinely separate raw target-matrix enumeration for six small parameter pairs: \((t,m)=(1,1),(2,1),(1,2),(2,2),(3,1),(4,1)\), covering 8,840 matrices. Explicit extremal constructions and 960 further fixed-seed random histogram targets were checked across orders up to eight and repetitions up to 64.

The two essential proof steps checked mathematically are: (i) a maximum first-block frequency plus an average across the other two blocks forces at least \(\lceil m/2^t\rceil+\lceil2m/2^t\rceil\) agreements; and (ii) index-two subgroup/coset placements of residual occurrences prevent simultaneous alignment of all three extras when the remainder does not exceed half the alphabet. The proof, not the finite computations, establishes the universal formula. An independent mathematical audit has not been performed.
