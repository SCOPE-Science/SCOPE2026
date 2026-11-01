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

# Reproducible exact finite checks

Use Python 3.10 or later to run `python3 verify.py` in the directory containing this file. No network access or third-party packages are needed. A complete, successful execution prints `ROOK_SHRIKHANDE_FOUR_CUT_INTEGRAL_HOMOLOGY_VERIFIED` as its final line; the complete contemporaneous output is provided in `verification_output.txt`.

The checker constructs each graph from an explicit vertex formula and verifies all strongly regular parameters; independently enumerates two equivalent descriptions of the Alexander dual on all 65535 nonempty subsets; counts all faces of the *original* four-cut complex separately; checks that every matched pair is a codimension-one incidence; orients and topologically sorts every Hasse incidence; forms signed integer simplicial chain boundaries; checks \(\partial^2=0\); cancels all matching pairs over the integers using unit pivots and checks \(\partial^2=0\) again; reduces every residual integer matrix using row and column operations with unit invariant factors and zero remainders; calculates mod-two boundary ranks independently from the original dual complex; and checks Alexander-duality indexing and reduced Euler characteristics. This verifies integral homology, not homotopy type or any unstated family result.

The finite checks do not establish that the calculation was unpublished and do not constitute external independent validation. Reproduction should be performed with the provided source bytes; expected numerical values are explicitly asserted and full intermediate outputs are printed.
