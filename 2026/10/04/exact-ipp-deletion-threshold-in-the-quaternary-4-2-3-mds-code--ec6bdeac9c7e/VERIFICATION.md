---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

An independent exact replay reconstructed \(\mathbb F_4\), all 16 displayed codewords, and minimum Hamming distance 3. It derived forbidden sets directly from IPP1/IPP2, finding no bad triples and 144 bad four-word subsets, then checked all \(2^{16}=65536\) subcodes. The exact optimum is 8 with 48 maximizers. Independently reconstructing all 20 affine lines of \(\operatorname{AG}(2,4)\) gives exactly 24 maxima with profile \(\{4^2,2^{16},0^2\}\) and 24 with \(\{3^8,2^4,1^8\}\). This is exhaustive finite verification, not sampling.

## originality

PASS

Originality passes at the stated fixed-code level. Blackburn--Etzion--Ng give the standard IPP1/IPP2 criterion, general upper bounds, and the prolific length-four classification, including exclusion of quaternary prolific codes. Their full analysis does not determine the maximum IPP subset of this particular 16-word quaternary MDS code, enumerate all maximizers, or give the two affine-line profiles. Fresh semantic and exact-parameter searches did not surface a covering theorem.

## value

PASS

The fixed ambient code is the natural quaternary length-four MDS object immediately beyond the unique ternary prolific example in the foundational classification. Determining exactly how much of it survives the IPP constraint, how many extremizers occur, and their affine incidence profiles is a meaningful finite boundary classification rather than a tiny arbitrary subset test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
