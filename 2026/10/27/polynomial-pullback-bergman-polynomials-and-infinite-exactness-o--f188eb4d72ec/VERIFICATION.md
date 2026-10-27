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

The exact proof requires four verifiable identities: (i) the Lagrange fiber trace equals the \(z^{-1}\) Laurent coefficient of \(s(z)/(P(z)-w)\); (ii) terms of degree at least \(m\) in \(w\) have order \(O(z^{-2})\), forcing them to vanish; (iii) area substitution for degree-\(d\) polynomials yields \(d\) regular preimages and a \(1/d\) norm transfer; and (iv) the disk moment \(\int_{|w|\le R}|w|^{2k-2}dA=\pi R^{2k}/k\) plus the standard logarithmic capacity formula yields exact equality in the stated normalization.

Run `python verify.py` in the same directory; SymPy is the only nonstandard dependency. It verifies the trace from exact polynomial remainders against Laurent residues for five explicit monic integer polynomials (degrees one through five) and four exponents, then independently checks monic derivative identities. Observed output: `CHECK_OK: 130 exact polynomial-trace, Laurent-residue and derivative identities`.

The tests do not establish the infinite-degree theorem; they independently check finite instances of the decisive algebraic lemma. No interval-numeric approximation or incomplete enumeration is used as proof. The exact degree argument and change-of-variable identities in RESULT.md establish the universal quantifiers. Earliest source date uses the v1 arXiv public date, 17 October 2026. No external audit is asserted.
