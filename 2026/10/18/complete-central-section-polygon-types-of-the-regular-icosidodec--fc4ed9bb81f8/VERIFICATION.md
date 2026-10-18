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

# Reproduction and verification

Run `python3 check_sections.py` from the directory containing the delivered files. It requires the Python standard library only.

The checker performs exact additions, multiplications, divisions and sign tests in the quadratic field \(\mathbb Q(\sqrt5)\). It reconstructs the icosahedron and its rectification, tests all 20 triangular and 12 pentagonal supporting facets against all midpoint vertices, and verifies edge incidence. It verifies that each of the 15 hyperplane reflections preserves the midpoint vertex set. It enumerates all 105 distinct mirror-plane pairs and groups their projective cross-product axes with exact rational normalization, obtaining 15 twofold, 10 threefold, and 6 fivefold lines. For every axis it counts strict edge crossings and polytope vertices already on the plane and checks section sizes 8, 6 and 10 respectively. A generic normal has 12 sides; a sample normal on precisely one wall has 10. The program prints `EXACT_SECTION_CERT_OK` upon success.

The mathematical extrapolation from a generic sample to **all** generic directions is separately justified by the proven reflection symmetries and the chamber-transitivity lemma, not by sampling. Likewise, all open mirror arcs share the ten-sided count through the centrally symmetric degree-four incident-edge argument. Euler's formula completes the spherical region count.

**Limitations:** The verification does not address metric measures of sections, noncentral planes or exact priority of every historical source. These checks are self-review with an executable finite certificate; independent audit is not performed.
