---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The polynomial g=1+x^2+x^4+x^5+x^6+x^10+x^11 has degree 11 and divides x^23+1, so all 2^12 messages with degree<12 map injectively to 4096 distinct codewords. For each nonconstant codeword its cyclic zero-run lengths r give w_b=23-sum max(r-b+1,0); the 81-class run census therefore determines all 23 complete b-symbol distributions. Inspected actual GENERATE.py, VERIFY.py, both CSVs. A separate independently written enumerator generated 4096 words, computed every one of 23 cyclic-window spectra and all 81 zero-run multiplicities, confirming all values and the 23 common cyclic-generator-orbit minimizers for b=3..11. The ordinary b=1 code weight enumerator, known minimum b distances and saturated 12..23 widths were checked separately. This is a finite exhaustive computation for the exact code, with an injectivity proof; it asserts no general arbitrary-code result.

## originality

PASS

The b-symbol minimum-distance values for widths 1–11 were published explicitly by Guan et al, Example 4, using the reciprocal Golay generator. Wide-width stabilization is general prior theory and the run-to-window identity is elementary/known. The surviving novel claim is the nontrivial full weight-multiplicity spectra and 81-class run-partition refinement, plus equality of all width-3..11 minimizing word sets with one 23-word orbit. No inspected prior table yields those stronger multiplicity statements, but code-table priority risk remains.

## value

PASS

This is a complete and independently reproducible symbol-read spectrum for the canonical perfect binary Golay code, useful for enumerator-based error-detection/coding analyses. Full multiplicity profiles distinguish codes/read lengths with identical minimum distance, and the common-minimizer orbit identifies exact extremizers. A complete finite classification of a central natural object has scientific value despite no general b-symbol theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
