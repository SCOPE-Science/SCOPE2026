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

Execute `python3 verify.py` in this directory using the Python standard library. The program (i) independently calculates all nine \(\mathbb F_3 S_3\) indecomposable sign-Hom dimensions from exact finite linear constraints; (ii) compares every coefficient of the bivariate polynomial for the modular top Betti number with the character-averaged rational formula; and (iii) checks integrality and equality on the \(1089\) ordered parameter pairs \(7\le a,b\le39\). It reports the first three examples \(1911,5726,16716\) and prints `VERIFY_OK` on success.

During the mathematical derivation, separate exact finite-field elimination of the defining injection slot relations at \(a=7,8\) gave module dimensions \(225,641\), matching the derived character formula. Their \(V\)-fixed projective and nonprojective block multiplicities and the nontrivial \(V\)-character stabilizer eigenspaces also matched. The packaged verifier checks the algebraic general identities but does not re-enumerate these large injection matrices, and the finite checks do not prove the infinite theorem independently. The proof in RESULT.md supplies the projectivity and syzygy arguments required for arbitrary parameters.

The integral universal-coefficient step deduces absence of \(3\)-primary torsion from exact equality of characteristic-three and rational **top** homology dimensions. Other coefficients, homology degrees and graph sizes are outside the result. Independent review has not been performed.
