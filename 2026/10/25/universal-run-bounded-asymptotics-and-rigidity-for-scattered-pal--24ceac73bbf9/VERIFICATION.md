---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Every palindromic run symbol sequence has an odd number of runs, and a subsequence has no more runs than its parent. For words with <=2k+1 runs, a palindrome with <=2k-1 runs is specified by <=k initial symbol/length choices and contributes only E(w)<=q sum_{j<k}(q-1)^j n^{j+1}=O_{q,k}(n^k). A 2k+1-run palindrome must select every parent run; it exists only for a 2k+1-run palindromic skeleton and has exactly L(w)=r_{k+1} product_{i<=k} min(r_i,r_{2k+2-i}) distinct strings. Set t_i=min(...) and c=r_center; 2 sum t_i+c<=n. AM–GM bounds L<=n^{k+1}/[2^k(k+1)^{k+1}]. Alternating two-symbol palindrome skeleton with each flank length floor(n/[2(k+1)]) and center length n-2k floor(...) attains the leading term. The equality-case stability follows from compactness and AM–GM uniqueness; the n-2sum t_i-c deficit is the sum of absolute differences in mirrored run lengths. This proves the iff rigidity with fixed q,k and excludes a mere finite extrapolation. Fresh dynamic enumeration directly counted distinct PALINDROME STRINGS in 21,690 word/k instances, confirming top-run formula.

## originality

PASS

Mahalingam–Pandoh (2021) study distinct scattered palindromes but optimize by different-letter count and general Fibonacci-type bounds; a fixed run-budget leading coefficient and run-length rigidity were not found in its inspected theorems. Liron–Langberg (2012) give extremal counts for arbitrary fixed-length deletion subsequences, which ignore palindromicity. Resultary related sequence coding results do not imply this all-length palindrome count. The sharp leading coefficient and stability under a natural run constraint are qualified original.

## value

PASS

A natural structural complexity constraint (number of runs) leads to an alphabet-independent universal sharp leading growth law plus a complete characterization of asymptotic extremizers; this rigidity is a substantive exact combinatorial phenomenon rather than a routine substitution into a known maximum-length palindrome bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
