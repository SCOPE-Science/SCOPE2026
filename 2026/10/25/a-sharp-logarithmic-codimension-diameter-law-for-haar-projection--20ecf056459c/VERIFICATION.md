---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS. For S_m=conv(e_i), Haar discarded k-plane of H_m is represented by centered m-by-k Gaussian rows; pairwise discarded squared edge length is (Z_i-Z_j)^T(Z^T C Z)^{-1}(Z_i-Z_j). Since every simplex diameter is realized by a vertex pair, Delta²=2-min discarded square. Wishart Frobenius second-moment bound gives spectral uniform replacement by |Z_i-Z_j|²/m because k~c log m. Each pair distance is 2 chi²_k, rate I(s)=(s−1−log s)/2. Counting m² pairs yields threshold c I(s)=2; the second-moment lower side handles dependent overlapping pairs with Chernoff q<=exp(-k J(s)) and exact identity 4(J−3I/2)=H(s)>0. Independent sympy log algebra verified identity and H'(s)=−(1−s)²(s+3)/[s(3−s)(1+s)]<0 for 0<s<1. Therefore k^{-1} min pair distances -> 2s_c and (m/k)(sqrt2−Delta)->s_c/sqrt2, where s_c−1−log s_c=4/c. No fixed-k/linear-k or CLT claim.

## originality

PASS

PASS, best knowledge: the Gaussian realization of projected regular simplices and fixed-dimensional minimum interpoint distance law are classical. The new statement is the near-full-dimensional projected simplex diameter at logarithmically growing discarded dimension with exact rate root and dependence-corrected sharp constant. The fixed-d theorem inspected does not imply the moving-d limit; the 1994 Baryshnikov–Vitale exact same simplex/Gaussian relationship is not fully accessible, so its unknown scope remains a priority risk.

## value

PASS

PASS. Diameter is an intrinsic metric invariant of random regular-simplex projections; the logarithmic codimension is a natural extreme-pair transition scale. The explicit rate root and dependence-sensitive second moment supply an all-c classification inaccessible from fixed-dimensional spacing laws. It offers a sharp benchmark for near-full-dimensional random geometric projection, not an arbitrary constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
