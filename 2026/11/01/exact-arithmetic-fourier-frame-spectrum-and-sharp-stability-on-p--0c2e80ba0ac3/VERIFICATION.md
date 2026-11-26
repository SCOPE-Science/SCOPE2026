---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The word-period Möbius sieve is pointwise. On words that repeat a block of length n/d, independent uniform block coordinates make the pair moment nonzero only for equal character labels and n/d dividing the lag. Fourier transformation in the lag gives d times the indicator of d dividing k; counting residues by their prime support proves the stated multiplicities. The sum of squared coordinate-character sums proves B_m(S)≥0, and adding a prime p subtracts pB_(m/p)(S). The one-exceptional-letter primitive word gives strict positivity for m≥3; the remaining cases give exactly one zero eigenvalue at (q,n)=(2,2). The union bound on these squares gives the stated uniform bound: prime n is sharp only at (2,3), n=4,6,8 are below it, the bound n log₂(n)/2^(n/2+1) decreases below 3/4 after n=8, and n=2 with q≥3 has ratio at most 3. Unit diagonal implies the constant lies between the extrema. Bounding the same weighted prime sum and the primitive-word count gives the claimed asymptotic spectral deviation. Independent enumeration of seven small parameter cases (including q=2,n=2 and q=2,n=3, and composite alphabet q=4,n=3) checked exact moments and characteristic polynomials; e.g. the nonconstant block at (2,3) has eigenvalues 1/3,4/3,4/3. The frozen checker and verification notes were inspected, not executed. The condition number is asserted only in the injective cases.

## originality

PASS

The supported distinct content is the general q-ary primitive-word coordinate-band arithmetic spectrum and the uniform sharp bound across lengths and alphabets. The binary prime cases, including both exceptional parameters, are exact equivalents of the same-day onto-word spectrum. They are not distinct formulas in isolation, and the catalogue date does not assign priority. There is exact overlap on composite binary lengths with a separate later-dated record. Neither of those statements nor the classical necklace count gives the full primitive-alphabet classification.

## value

PASS

Conditioning on primitivity breaks product orthogonality but retains arithmetic symmetries, so the exact spectrum and the global worst-case stability bound are meaningful benchmarks for this natural restriction map. The prime-indexed levels and the identification of the sole dependency answer more than a necklace count or a finite rank test. The exact recovery of the sharp bound from a sum-of-squares sieve is useful uniformly across composite lengths and alphabets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
