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

# Reproduction and limitations

Run `python3 verify.py` using only the Python standard library. It constructs degree-three and degree-four polynomial quotient fields over \(\mathbb F_3\), exhaustively tests square restrictions of the two branch quartics on all lines \(z=sx+ty\), independently matches their quadratic square roots, counts hyperflexes, and computes the Frobenius orbit profiles. Expected final line: `VERIFY_OK`.

The verifier handles the indicated finite extensions. The accompanying proof verifies that the two parameter polynomials split completely over these extensions, that the Artin–Schreier equations admit exactly three values of \(t\) for every root of the first equation, and that no bitangents are omitted outside the chart. The discriminants and unique-tangent property supply the geometric contact-point classification. Finite enumeration alone is not used as a proof of completeness over \(\overline{\mathbb F}_3\). No independent external audit or validation has been performed.
