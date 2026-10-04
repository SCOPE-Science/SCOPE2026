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
The finite checks in `verify_orbit.py` reproduce the group orders, orbit--stabilizer orders, and the reflection that exchanges the two diagonal squared-entry patterns. Running `python3 verify_orbit.py` must print `VERIFY_OK`.

The proof also uses one non-computational standard fact: if \(K/K_0\) is a finite Galois extension and \(v\) is a discrete valuation of \(K_0\), then the Galois group acts transitively on the extensions of \(v\) to \(K\). Here \(K=\overline{\mathbf Q}(V)\), \(K_0=\overline{\mathbf Q}(\mathbf P^2)\), and the group is the 256-element projective sign-change group.

The source establishes the premises used by this application: the full automorphism group and sign subgroup, the 64-plus-64 decomposition of \(Z_3\) into smooth rational conics, and the explicit square reflection. The verification does not attempt to classify conics outside \(Z_3\), and the result makes no such claim.
