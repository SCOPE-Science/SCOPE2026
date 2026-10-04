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
# Verification

The bundled script `verify_distortion_line_scrolls.py` uses exact symbolic polynomial arithmetic with SymPy.

It checks:

- restriction of the published ambient \(2\times6\) determinantal ideal to representative lines in each coefficient stratum yields exactly the standard determinantal ideals of \(S(2,3)\), \(S(1,3)\), and \(S(1,2)\);
- the family ideals for \(V(t a+b)\) and \(V(t b+c)\) are unchanged by exact \(t\)-saturation, using elimination with an auxiliary inverse variable;
- the first special-fiber ideal equals the intersection of the embedded \(S(1,3)\) ideal with the base-plane ideal;
- the second special-fiber ideal equals the intersection of the embedded \(S(1,2)\) ideal with the same base-plane ideal;
- each component intersection is a projective line by exact equality of the summed ideals with a coordinate-line ideal.

A successful replay prints `VERIFY_OK` followed by the three scroll types, their degrees, and the two flat-limit decompositions.

The computation verifies the displayed ideal identities over the rational numbers. Smoothness and degree of the standard rational normal scrolls are used as standard algebraic-geometric facts, consistent with the source's general scroll construction. No claim is made about arbitrary coefficient paths or positive characteristic.
