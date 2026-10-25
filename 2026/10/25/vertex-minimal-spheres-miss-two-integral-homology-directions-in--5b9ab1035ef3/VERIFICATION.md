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

The exact finite certificate is `certificate.json`. Run `python verify_icosahedral.py certificate.json` after installing the packages pinned in `requirements.txt`. Successful execution prints `VERIFY_OK_ICO_MINIMAL_60_SPHERES_CODIMENSION_TWO` to standard error.

The verifier constructs the icosahedral graph, its 12 open neighborhoods and all nonempty simplices. It checks the two chain-composition identities and ranks \(49,48,12\) modulo \(101\) for the boundaries in degrees \(2,3,4\). The degree-four injection and signed unit-minor certificates turn these modular bounds into integral conclusions.

It enumerates all four- and five-vertex supports and computes exact rational local cycle generators, clearing denominators to integer cycles. Each is mapped through an explicitly unimodular-basis inverse into **integral** homology coordinates. The program confirms zero relevant four-vertex supports and precisely sixty five-vertex supports, each with a one-dimensional nonzero image. It checks all sixty six-triangle bipyramid cycles, the full 120-element symmetry action, and the two eight-triangle octahedral cycles.

It exhibits separate determinant-one maximal minors of sizes \(69\) and \(71\), establishing respectively the primitive rank-\(21\) smallest-support lattice and full primitive rank-\(23\) homology basis. Since no infinite quantification is asserted, the exhaustive enumeration ranges are complete for this fixed twelve-vertex complex. Independent audit has not been performed. The result does not classify every larger support or prove uniqueness among unindexed literature.
