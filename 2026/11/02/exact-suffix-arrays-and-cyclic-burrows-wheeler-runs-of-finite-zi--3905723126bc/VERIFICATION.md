---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Z_n=Z_{n-1}a_nZ_{n-1} with strictly increasing distinct alphabet interleaves a1 at all even positions and shifted alphabet symbols at odd positions. Lexicographic even/odd splitting gives S_n=(2L)||(2S_{n-1})||(2S_{n-1}+1), L=2^(n-1)-1. Proper-suffix prefix ties under cyclic wrap preserve order because a1 continues the shorter suffix while a larger odd-position symbol follows in the longer. Predecessor characters and zero-position row recursion give exact sentinel-free cyclic BWT blocks and original row n; rank-two adjacent a1 blocks merge, yielding r=1,2,2n-1 for n=1,2,n>=3. Independent direct suffix/rotation sorts and BWT/run comparisons succeeded for ranks 1..8 (length through 255); the all-n result rests on the interleaving proof, not finite extrapolation.

## originality

PASS

Known BWT basic results, fully clustered word descriptions, morphic Thue–Morse/Fibonacci/Tribonacci formulas, and the shared low-rank example abacaba do not determine the full expanding-alphabet Zimin suffix array and cyclic BWT expression. The precise no-sentinel convention and two-block alphabet pattern differ. Prior scattered higher Zimin examples remain a risk.

## value

PASS

Finite Zimin words are canonical recursively unavoidable patterns. Their complete suffix order and exactly 2n-1 cyclic BWT runs quantify logarithmic run-compressibility for an alphabet whose size grows with word rank; a concrete structural fact relevant to text indexing and compression, beyond simply noticing that each symbol must occupy a run.

The dated certificate retains the supplied scientific assessment, sources and limitations.
