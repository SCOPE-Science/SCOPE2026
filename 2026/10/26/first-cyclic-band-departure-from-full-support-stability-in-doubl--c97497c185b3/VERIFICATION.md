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

At strict face data the face equality projection continues to satisfy all KKT conditions in a neighborhood: the positive supported coordinates and positive complementary multipliers vary continuously. The offsets 0 and 1 already connect the bipartite support graph; changing the sign on the column-vertex rows makes B a grounded incidence matrix with full row rank. Consequently the derivative is the zero extension of the orthogonal cycle-space projector Q, and its max-entry operator norm is the maximum absolute row sum. Simultaneous translation covers each edge-displacement orbit, so there are exactly 440 rows to test. Full support independently yields the tensor square of the centering projector and hence 4(1−1/n)². A fresh exact rational replay verifies strict inequality for every proper width through n=12, the unique exception (13,7), its fraction and gap, and the sign-direction witness at step 1/1000, including the exact reported positive KKT margins. The choice of step also has a qualitative margin check: the supported displacement is at most √91 by orthogonal contraction, and a missing edge's extrapolated equality-normal change is a signed sum of at most 25 supported edge values along a bipartite path, each bounded by √91. Thus the step preserves both the positive 1/7 supported coordinates and the unit complementary slack in the starting multipliers. The positive-data ratio is a global lower bound, not an exact global norm or an unrestricted first dimension.

## originality

PASS

Credit prior general active-face calculus, transfer-current machinery, and the earlier indexed proof of a first departure for a distinct nonband support family. That record also explicitly alludes to a related contiguous cyclic-band analysis with a later departure, but supplies no attribution, dimension, width, norm, or certificate for the band comparison. This is a material priority caveat for the broad idea of band departure, not established coverage of the exact finite cutoff, unique exceptional width and attaining pair. The pass is for those exact supported claims.

## value

PASS

Consecutive equal-width bands are a canonical nested family of supports, and full support is the natural tensor-product stability benchmark. The first reversal tests a plausible monotonicity heuristic about sparsifying active support. The exact small excess, unique width and explicit strictly positive pair separate a genuine finite instability from roundoff or from an artifact of nonpositive data. The exact cutoff is useful for this structured support family, independently of the earlier nonband example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
