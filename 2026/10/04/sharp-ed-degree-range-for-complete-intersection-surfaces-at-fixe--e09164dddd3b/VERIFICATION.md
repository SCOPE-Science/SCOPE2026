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
The source formula is specialized exactly in RESULT.md. For a surface, only complete homogeneous terms of total degree at most two occur, so
\[
1+h_1+h_2=1+T+\frac{T^2+Q}{2}.
\]

The bundled checker independently enumerates nondecreasing degree tuples for every \(2\le c\le6\) and \(2c\le S\le4c\). For each fixed pair \((c,S)\), it confirms that the unique minimum is \((2,\ldots,2,S-2c+2)\) and the unique maximum is the balanced tuple whose entries differ by at most one. It also checks strict increase for every admissible unit balancing move within the census.

The enumeration is not an infinite proof. The infinite theorem rests on the exact balancing identity
\[
(B+\delta)(A-\delta)-BA=\delta(A-B-\delta)
\]
and the strict inequality \(A>B+\delta\) established in RESULT.md.

Scientific limits: generic projective ED degree, smooth complex complete-intersection surfaces, fixed codimension, fixed sum of defining degrees.
