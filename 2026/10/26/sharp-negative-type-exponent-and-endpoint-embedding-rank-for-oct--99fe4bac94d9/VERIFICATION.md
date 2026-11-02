---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For the 24 orientation-preserving signed permutation matrices, independently formed all principal relative-rotation angles using the integer trace. The central distance-power matrix has the S4 character scalars (divided by pi^p) -3+8(2/3)^p-6(1/2)^p (dimension 1), 3-4(2/3)^p (multiplicity 4), 1-2(1/2)^p (multiplicity 9), and -3+2(1/2)^p (multiplicity 9). The 2D scalar changes sign exactly at p*=log(4/3)/log(3/2). Below that cutoff the other three are strictly negative: p*<1, b=(2/3)^p>=3/4, a=2^-p>1/2, b<sqrt(a) and 2sqrt(a)<=1+a. Above p* the positive 2D scalar obstructs conditional negative type. The centered Gram -HD_pH/2 therefore has rank 23 in the open admissible range and rank 19 at the endpoint. Schoenberg embedding and strict finite Gaussian positivity follow for distinct embedded points. For p>p*, the Gaussian is indefinite for small positive bandwidth by first-order expansion, yet tends to identity for large bandwidth. The independent 24x24 matrix computation at seven p-values matched all character spectra and ranks; numerical checks are corroborative only.

## originality

PASS

The octahedral S4 angle-power cutoff with four-dimensional endpoint rank drop is not stated by the inspected general finite-metric negative-type or ambient projective-space results. This is a qualified best-of-knowledge originality assessment; a comprehensive check of specialized finite rotation-group metric literature remains outstanding.

## value

PASS

The finite rotation group is canonical, its intrinsic angular metric arises from SO(3) geometry, and supremal negative type and the least Euclidean squared-distance embedding dimension are standard geometric metric invariants. An exact cutoff with a precise rank defect explains a genuine boundary phenomenon, not a one-off computed instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
