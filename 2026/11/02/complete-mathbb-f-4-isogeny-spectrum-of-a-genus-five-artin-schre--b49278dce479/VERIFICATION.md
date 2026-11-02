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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 standard library. The script enumerates all 192 coefficient quadruples over \(\mathbb F_4\); builds \(\mathbb F_{4^m}\) for \(1\le m\le5\) from explicitly checked irreducible binary polynomials; counts every elliptic affine pair via the Artin–Schreier absolute-trace criterion; reconstructs every genus-five Weil polynomial with Newton identities and the functional equation; computes exact slope multisets; and checks fourteen polynomial rows against `zeta_table.csv`'s contents. It also independently counts all triples \((x,y,u)\) for three representative parameters in extensions \(\mathbb F_4\), \(\mathbb F_{16}\), and \(\mathbb F_{64}\).

Expected terminal output starts with `VERIFY_OK`. A verified run produced the following summary: `192 parameter quadruples, 14 Weil polynomials, 48 supersingular and 144 (1/3,1/2,2/3)-Newton cases`. Finite point-count enumeration is exhaustive over its stated coefficient domain, not a statistical experiment or evidence about all algebraic-closure parameters. The genus and unique point at infinity have independent mathematical proofs in `RESULT.md`. The script does not independently prove the Artin–Schreier and Weil theorems used in reconstruction. Independent mathematical audit has not been performed.
