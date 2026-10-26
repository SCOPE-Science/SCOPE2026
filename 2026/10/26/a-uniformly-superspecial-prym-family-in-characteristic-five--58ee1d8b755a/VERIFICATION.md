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
# Reproducibility

`verify.py` requires Python 3 only. It multiplies sparse bivariate polynomials in \(\mathbb F_5[a,x]\), verifying the exact Cartier contributions: the degree-\(4\) and degree-\(14\) coefficients of \(f_a^3\) vanish, while the degree-\(9\) coefficient equals \(a^3+a\); the sole nonzero relevant coefficient for \(x^i f_a\) equals \(a\) for \(i=1\). Independently, it verifies the four entries of the genus-two Cartier–Manin matrix from \(h_a(t)^2\). Finally, it constructs \(\mathbb F_{25}\) and counts \(66\) points on the superspecial member \(C_0\).

Reproduce by executing `python verify.py`. This checks the critical parameter-uniform polynomial identities and one point-count sanity test, not the general theory of the Cartier operator, the tame double-cover/Prym identification, or historical novelty. Those standard inputs and logical deductions are given in `RESULT.md`. All calculations refer to the embedded program shipped with this finding, not an external log or a different version. The scientific conclusion is conditional only on the explicit smoothness assumption \(a^2\ne4\).
