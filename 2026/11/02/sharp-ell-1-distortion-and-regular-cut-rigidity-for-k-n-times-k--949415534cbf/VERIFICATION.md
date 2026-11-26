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

For n≥3 the graph has distance 1 on transverse pairs and 2 on same-coordinate pairs; a common neighbor is obtained by avoiding both coordinate values. For a cut of size K, T=K(n²−K) is its total separated-pair count, U+V are those sharing a row or column, and W=T−U−V are transverse. The class populations give the factors used in the proof. Expansion of row and column variances gives exactly 2T−n(U+V)=n times the sum of their squared deviations from K/n. Thus the linear gap is nonnegative and vanishes precisely on cuts whose rows and columns all sum to K/n. Integrating threshold cuts coordinatewise gives the nonnegative cut decomposition (finitely many cut types on this finite space, also for countable ℓ1). With canonical noncontracting normalization, minimum stretch one, the row/column averages are each at least 2 and the transverse average at most the distortion. This yields D≥2(n−2)/(n−1). A uniform permutation cut separates same-coordinate pairs with probability 2/n and transverse pairs with probability 2/n−2/[n(n−1)]; multiplying by n realizes the bound, including the isometry at n=3. Equality forces all three averages to the relevant per-pair bounds, hence all individual image distances as claimed, and in every nonnegative decomposition every positively weighted cut must have zero gap. Discarding the trivial zero cuts gives the exact asserted regular incidence restriction. Independent direct pair enumeration tested 512 cut inequalities at n=3 and 156 matching-metric pairs at n=3,4, separate from the general proof.

## originality

PASS

Vallentin's prior Euclidean formula implies the exact numerical lower bound on ℓ1 distortion after taking the square root of the cut metric. The distinct content is that this bound is attained in the cut cone by permutation cuts at every size, and that its exposed optimal cut structure is precisely row/column regularity with a unique optimal normalized distance profile. Neither Euclidean tightness nor the closely related balanced-block or Kneser results supplies that cut-cone realization and classification for this graph.

## value

PASS

The vertex metric on the square complement-rook family is a natural two-distance object for which a Euclidean spectral bound need not supply a cut-cone upper bound. Realizing that bound for every size and identifying every eligible positive cut through balanced row/column incidence provide both a sharp invariant and usable structure on its optimizers; the result is more than a scalar evaluation of an existing spectral formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
