---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For a binary palindrome w length N>=3 with endpoints 1 and no internal 11, the circular join is the unique 11. A wrap-crossing palindromic factor contains this pair once; reflection forces it to occupy the two central positions, hence it has even length 2d and is exactly suf_d(w) pre_d(w). Palindromicity makes each of these words symmetric; their 11 prevents occurrence inside w and their distinct lengths make the union disjoint. For Cantor iterate C_{k+1}=C_k 0^{3^k} C_k, induction produces N existing palindromes plus 2N distinct new words through zero-only, zero-padded smaller Cantor and central-bridge families. The general at-most-word-length palindromic bound then proves exhaustiveness. Combining ordinary length spectrum with exactly one new even-length circular palindrome yields the stated piecewise 1/2/3 spectrum and (3N-1)/2 total. Independently enumerated every admissible palindromic word through N=12 and literal Cantor circular palindrome spectra through rank k=4. This is an all-rank proof beyond finite tests.

## originality

PASS

Crucial prior-coverage correction: Simpson 2014 Proposition 13 ALREADY proves the sharp upper bound ceil((3N-1)/2) for *every palindromic word*, so the Cantor total (3N-1)/2 by itself is not a novel bound. Glen–Justin–Widmer–Zamboni already recognize the infinite Cantor word as rich. What survives is the distinct circular-factor LANGUAGE via unique boundary 11 for every word in the specified boundary-isolated family and the complete finite Cantor lengthwise spectrum; neither is given by Simpson’s aggregate bound or richness alone. A direct implication from additional uninspected finite Cantor factor enumeration remains a residual historical risk.

## value

PASS

An explicit transfer rule for literal circular palindromic languages and a full finite Cantor length spectrum supply usable detailed information beyond classical rich-word maximality and Simpson’s count bound. The theorem isolates a natural unique-boundary mechanism rather than an arbitrary small computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
