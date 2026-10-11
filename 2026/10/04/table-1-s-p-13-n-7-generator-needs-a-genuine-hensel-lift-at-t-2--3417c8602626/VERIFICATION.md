---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the printed \(p=13,n=7\) Table 1 component polynomials, exact division modulo \(169\) gives nonzero remainders \(26+13x+39x^2+117x^4\) from \(x^7-1\) and \(13x^3+13x^4\) from \(x^7+1\), so the literal printed coefficients are not valid \(t=2\) divisors. Exact multiplication-matrix reduction gives ideal cardinalities \(13^9\) and \(13^8\), hence \(13^{17}\) for the direct sum rather than the advertised \(13^8\). The corrected lifts \(\widehat f=(168,6,134,35,163,1)\) and \(\widehat g=(1,29,164,164,29,1)\) divide the two modulus polynomials with cofactors \((1,6,1)\) and \((1,140,1)\), reduce to the printed polynomials mod \(13\), and generate free rank-two components. Fresh exact enumeration reproduces the component weight distribution \(1+1176z^6+27384z^7\); the Gram determinants \(46\) and \(154\) are units modulo \(169\), proving LCD. Thus the corrected direct sum has size \(13^8\), distance \(6\), and meets the Singleton bound.

## originality

PASS

The current primary article's Table 1 explicitly labels the displayed objects as generator polynomials over \(\mathbb Z_{p^t}[i]\) and prints the \(p=13,n=7\) row with the coefficient strings audited here and parameters \((7,13^{4t},6)\). The paper invokes Hensel lifting generally but supplies no \(t\)-dependent corrected coefficients in that row. Targeted Resultary and web searches found no corrigendum, published corrected lift, or report of the \(13^{17}\) literal-generator cardinality. The earlier order-\(p^2\) Gaussian-code paper covers the \(t=1\) baseline, not this \(t=2\) lift. The audited correction therefore survives implication comparison.

## value

PASS

The result corrects a concrete published generator for an advertised ACD MDS family and supplies an explicit valid Hensel lift restoring the claimed code, rather than merely flagging a typo. Exact generator data are essential for reproducibility in finite-ring coding theory, so this is a motivated finite correction with a complete replacement certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
