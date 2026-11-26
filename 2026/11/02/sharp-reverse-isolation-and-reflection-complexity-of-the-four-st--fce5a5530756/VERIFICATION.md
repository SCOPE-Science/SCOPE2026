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

For the infinite four-symbol fixed point, the classes {a,d} and {b,c} alternate. In a factor window the first and last letters of each image are injective on the known source parity class. Complete images recover the internal letters, and classwise injectivity recovers the partial endpoints. This proves the two factor-count recurrences (even length 2m with m>=2, odd length 2m+1 with m>=1); P(1)=4 and P(2)=8 then yield P(n)=8n-8 for n>=2. All eight alternating ordered pairs occur in sigma^4(a). Every length-at-most-eight window lies in sigma^3(xy) for an occurring pair xy, and conversely each such block pair occurs. Independent enumeration gave P=(4,8,16,24,32,40,48,56), reversible counts (4,8,16,16,16,8,4,0), and palindrome counts (4,0,8,0,8,0,4,0). At length seven the four words acabaca, babdbab, cdcacdc and dbdcdbd are all palindromes. A separate implementation using translate and consecutive pairs in sigma^4(a) regenerated the exact 504 bytes of factors8.txt (SHA-256 2aa97abe490366aad190ec88b638589d77046f871f0d6b69982810e4a6ec0fb4). Any longer reversed pair would give a length-eight reversed pair. Subtracting half the number of reversible nonpalindromes from P gives all stated reflection counts. The frozen verifier was inspected, not executed; no prefix extrapolation, formal verification or expert attestation is used.

## originality

PASS

The supported distinct claim is the full literal four-letter reflection profile and its sharp cutoff at eight, for the specified unprojected substitution. Checked binary and ternary results are not equivalent. This is a bounded assessment, not priority certification.

## value

PASS

The four-state precursor is a natural presentation of a canonical automatic sequence. The exact threshold is the shortest observation length at which the forward language and its reversal are disjoint. That fact and the last admissible reversed words are lost under binary projection, and the calculation resolves the entire reflection invariant rather than an arbitrarily truncated factor list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
