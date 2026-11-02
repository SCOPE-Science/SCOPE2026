---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS: Partition every palindromic scattered subsequence by j=0,1,2,3 copies of the symbol 1. Zero-only contributes m+1; one-one contributes h+1 via union of three initial length intervals; two-one words 0^i 1 0^j 1 0^i form three down-closed rectangles whose union is a base (x+1)(b+c+1) plus exactly E excess lattice points. Three-one words 0^i1 0^j1 0^j1 0^i contribute (x+1)(y+1). The resulting formula m+2+h+(x+1)(b+c+1)+(x+1)(y+1)+E covers all zero gaps. Symmetric case a=d=u,b=c=v reduces to 3uv+5u+6v+4, strictly concave in integer u at fixed s=u+v, uniquely maximized by u=floor(s/2). Independently enumerated all distinct subsequence strings for 495 gap tuples (up to 8 zeros) and checked the symmetric extremum through s=79. Finite tests are corroboration; case partition proves unrestricted zero-gap identity.

## originality

PASS

PASS (best-of-knowledge): No equivalent fixed-content scattered-palindrome formula was identified. General palindrome-string algorithms may compute instances but do not supply the stated four-variable identity and unique symmetric optimizer. A general count algorithm applies to this family but is not mathematically the same closed expression or extremal classification. Unread appendices of the 2008 work remain a priority risk. No inspected prior conclusion implies the all-parameter sparse-word palindrome count or symmetric unique optimum. Stronger uninspected exact subsequence theorems could remain. Specific priority and access qualifications are recorded below.

## value

PASS

PASS: Exact distinct palindromic-scattered-subsequence counts for a natural fixed-weight word family and a full equality classification within symmetric source words give a non-tabular structural result. Rectangular lattice-union decomposition isolates asymmetric zero gaps and avoids full-word dynamic programming. No unproved unrestricted optimum is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
