---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The inverse branch lengths add to the output length, giving a doubly stochastic transition matrix and the asserted uniform average of row entropies. In fact the stationary law is unique: full-branch cylinders shrink uniformly and map onto the interval, so every input cell contains a cylinder from which every output cell is reached along a positive-measure orbit segment, giving a positive-probability path in the resampled chain. In N-scaled coordinates, complete input cells have the given one-branch density, and shifting their index by s translates their images by the integer L, leaving entropy unchanged. When the turn is not aligned (equivalently L does not divide N by coprimality), the only leftover row is obtained by adding the two branch masses in each bin, not their entropies; both images are anchored at the integer output endpoint N, so the reflected bins and τ determine this row without any additional N dependence. Increasing N by L adds p and q full rows and keeps this row unchanged. This yields the exact recursion and all residue constants, including the aligned case N=L and N=1. Each full row has positive entropy because its image length is greater than one scaled output bin. An independent replay at (p,q,N)=(1,4,4), intersecting each input cell with clipped output-bin preimages [k/20,(k+1)/20] and [1−(k+1)/5,1−k/5] and multiplying by 4, gave rows (1,1,1,2)/5, (0,0,2,3)/5, (0,3,2,0)/5, (4,1,0,0)/5. The four full right-branch rows in a period contribute two binary entropies at each of 1/5 and 2/5, and the left gives log 5. This yields the stated H∞ and C_4=(2/25)log(32/27)>0, with C_1=−H∞<0. The fixed sign repeats by the exact recursion, not finite extrapolation. Frozen verification notes and verify.py were read, not executed; their broader finite checks do not prove the unrestricted statement.

## originality

PASS

Yano already treats the same entropy, gives the full-cell row formula and computes the limit, including the stated limit in the sign example. Credit those ingredients to Yano. The distinct result supported here is the exact scaled finite-resolution bias for all rational skew tents and its explicit two-sided sign witness in the same map. The prior limit argument discards relevant boundary information and does not supply that bias or witness.

## value

PASS

This determines the signed leading discretization bias exactly in a standard expanding family and supplies a strict witness against one-sided or monotone convergence, in both directions infinitely often for the same map. The periodic correction is useful for selecting unbiased grid sizes and cannot be recovered from the limiting entropy alone. The scientific claim is restricted to the resampled chain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
