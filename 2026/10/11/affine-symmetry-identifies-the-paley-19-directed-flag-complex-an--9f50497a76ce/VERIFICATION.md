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

Run `python3 verify.py` in the same directory. The verifier uses only the Python standard library and exact integer/modular arithmetic.

It checks the quadratic-residue definition of \(P_{19}\), verifies the doubly regular parameters, enumerates every transitive face, reproduces face vector \((19,171,684,1026,342)\) and Euler characteristic \(-152\), and computes the four simplicial boundary ranks over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{19}\). In every field the ranks are \((18,153,531,341)\) and the Betti vector is \((1,0,0,154,1)\).

It then constructs all \(171\) affine maps \(x\mapsto ax+b\) with quadratic-residue multiplier, verifies each map preserves every tournament edge, enumerates all setwise fixed transitive faces with orientation signs, and computes the signed simplicial Lefschetz number. The resulting classes are: identity, one element with \((L,\chi_3)=(-152,154)\); nonidentity translations, eighteen elements with \((0,2)\); and nontranslation affine elements, 152 elements with \((1,1)\). It finally solves the rational \(C_{19}\)-character equations to obtain trivial multiplicity \(10\) and cyclotomic multiplicity \(8\).

The supplied checked output in `verification_output.json` ends with `"status":"VERIFY_OK"`.

The homotopy equivalence itself uses the published exhaustive two-type classification for 19-vertex doubly regular tournaments; the verifier supplies the exact Paley-specific invariant that chooses the correct type and independently corroborates the Betti numbers over five fields.
