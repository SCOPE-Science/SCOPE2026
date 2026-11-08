---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The palindrome factor cap is one traversal of the circle. Two runs yield n+floor(a/2)+floor(b/2). Four runs have only palindromes of one, three or five symbol runs; enumerating center run and full flanking blocks gives four exact cases. Parity of unequal opposite runs yields equality counts; rotation maps ordered quadruples in two-element orbits for equality tuples. A known six-run family attains 10t-2 for n=6t and beats the bound for t>=3. Independent definition-level enumeration verified 1,001 ordered positive four-run compositions with n<=14, and t=2..8 six-run witnesses. Proof, not samples, supports every length.

## originality

PASS

Simpson 2014 full accessible primary proves general <5n/3 and exhibits the near-extremal six-run Biggles family, explicitly prior; its Lemma 6 and Theorem 7 do not imply the stronger conditional <=3n/2, exact four-run enumeration and equality census. OEIS A247000 tracks unrestricted maximum values but not this all-length run-stratified identity.

## value

PASS

A sharp threshold in the number of cyclic symbol blocks is a natural structural explanation for when the standard 3n/2 palindrome barrier can fail. Complete formulas, equality classification, and six-run sharp obstruction are usable independently in combinatorics on words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
