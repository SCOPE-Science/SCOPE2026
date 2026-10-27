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
# Reproducible checks and mathematical limits

Run `python3 verify.py` with a current Python 3 interpreter. No external packages are required. The complete coefficient arithmetic is performed modulo five. `verify.py` constructs \(f^3\) symbolically, checks the three relevant coefficients \(\alpha_i\), builds the polynomial \(H\), and checks every term against the eleven-term expansion. It also verifies that the specialized quadratic has the stated form and that the polynomial has the required weighted degree.

The irreducibility certificate has one theoretical step not reducible to a finite calculation: the specialized discriminant \(a_3^8(a_3^2+3)\) has two simple roots in characteristic five. Therefore it is not a square over an algebraically closed field; using UFD square descent and Gauss's lemma, the unspecialized primitive quadratic is absolutely irreducible. The detailed proof is in RESULT.md.

The code enumerates all 3125 monic quintics with coefficients in \(\mathbb F_5\). Exactly 2500 are squarefree, of which 700 satisfy \(H=0\) and 1800 satisfy \(H\ne0\). For each smooth quintic the script independently counts points on its cyclic cubic cover over \(\mathbb F_{25}\) and verifies \(\#C(\mathbb F_{25})-1+2H\equiv0\pmod5\). It also verifies two illustrative smooth cases with point counts 36 and 42. This is an exact finite-field regression test, not a substitute for the universal Cartier-operator proof or the absolute irreducibility argument.

The tests and theorem do not establish Ekedahl–Oort types, Newton polygons or independent scientific validation. A close later 2025 a-number paper was only available as an abstract; its complete matrix calculations remain an unresolved literature-comparison risk.
