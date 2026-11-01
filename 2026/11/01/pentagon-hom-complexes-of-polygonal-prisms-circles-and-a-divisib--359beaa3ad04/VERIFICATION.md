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

# Verification and limits

The exact all-parameter proof checks the following: (i) the signed sum on every prism square is an integer zero; (ii) the two rims have one common winding, and all parity-admissible windings occur; (iii) recolorings preserve winding; (iv) strict windings admit no directed cycles because a nonzero horizontal winding of \(m\) requires at least \(n|m|\) horizontal edges; (v) integer potential heights for two same-winding colorings differ by an exact integral cochain; their coordinatewise-minimum and source-raising argument gives connectivity; (vi) extreme windings give ten rigid colorings for each sign; and (vii) the source orientation criterion of Fujii et al., Theorem 5.1, identifies nonextreme components as circles. The proof does not infer infinite statements from finite checking.

The standalone Python 3 code `artifacts/verify_prism_hom.py` uses the standard library only and exhaustively checks \(3\le n\le10\). It independently generates graph homomorphisms, constructs the single-vertex recoloring graph, computes connected components, labels them by signed rim winding, and counts compatible product-cube cells using independent-set polynomials to calculate their Euler characteristics. It asserts exactly one Euler-zero component per strictly feasible winding and ten isolated Euler-one components for each extreme winding sign. Its actual recorded stdout is embedded in `artifacts/verification_output.txt`.

Observed full homomorphism counts for \(n=3,4,5,6,7,8,9,10\): \(0,190,20,1410,560,11070,8280,89550\). The reported success marker is `PRISM_C5_COMPONENTS_AND_CUBICAL_EULER_VERIFIED`. This confirms finite cases only; the identification of each nonextreme component with \(S^1\) relies on the cited published theorem, not merely on its Euler characteristic.

The work has received self-review but has **not** received independent audit or independent validation. Scope is limited to the undirected pentagon target and the indicated prism family.
