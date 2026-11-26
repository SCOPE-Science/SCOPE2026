---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Distances on the full unweighted crown are 2 within a side, 1 across a present edge and 3 on a deleted matched pair; n≥3 permits the requisite paths. Counting cut separations and substituting v=k+ℓ, z=k−ℓ gives h n(n−1)(U−(h−1)S/h)=(n−h)v−v²/2+(h−1/2)z²+2ht. Complementation allows v≤n. The even expression is visibly nonnegative; in the odd case v=n is the only potentially negative size and z is then odd. The zero cases give exactly the stated balanced selections of one vertex per matched index, and in odd order also the balanced selections omitting one index. After the distortion normalization d≤m≤Dd, the finite cut decomposition extends the inequality to m. The balanced-subset construction gives separation probability h/(2h−1), so total weight 2(2h−1)/h yields the required within-class, edge and matched-pair distances; the last lies between 3 and 3D. The equality chain at the optimum forces each within-class distance and each edge distance individually and forces equality for every nonconstant cut in any positive cut decomposition. The claim does not require classifying all matched-pair distances.

## originality

PASS

The closest same-graph results determine negative type or a Poincaré quotient, not the distortion, and the nearest indexed exact distortion result concerns K₃,ₙ, not a crown. In particular, even the sharp same-object Poincaré inequality optimizes a different linear combination and has different odd-order equality cuts. The inspected record and primary-literature comparisons do not cover the exact distortion and cut equality theorem. This is a qualified conclusion, not priority certification.

## value

PASS

A crown is a natural highly symmetric nontrivial graph metric. The result quantitatively separates the two isometric cases from the rest, yields a sharp parity staircase and an explicit optimal embedding, and proves which distances and cut-support restrictions every optimal embedding satisfies. A qualitative nonisometry result or a general graph embedding bound cannot be used in place of those data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
