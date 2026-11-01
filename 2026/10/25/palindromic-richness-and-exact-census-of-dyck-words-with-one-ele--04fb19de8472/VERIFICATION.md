---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Every W=(01)^u 0(01)^a1 (01)^v has exactly one 00 and one 11. An even palindrome containing one such double pair must be centered there; other palindromes are odd alternating factors. Direct arm-length maxima give the four-term P(W) formula. Splitting the cases u≤v across u<a, u=a<v, a<u≤v and equality u=v=a gives richness exactly min(u,v)<a or u=v=a. Counting pairs u+v=n-a-1 gives R_n=t(t+1)+(n-t-1)(n-t)/2+1_{3|n-1}. Independently enumerated all palindromic substrings for 1210 triples a=1..10,u,v=0..10 and all n=2..25; each matched, while the unrestricted theorem is the combinatorial argument.

## originality

PASS

Classical rich-word characterization is acknowledged. Currie–Mol–Rampersad study infinite rich words that avoid 14/5 powers and their repetition threshold; the present finite Dyck subclass often has arbitrarily long (01)^u powers and violates that hypothesis. Their structural theorem does not supply this three-parameter palindrome count or exact semilength census.

## value

PASS

The one-elevated-excursion Dyck family is a canonically defined complete subfamily of height-two Dyck words. Exact richness conditions and census resolve a natural finite-language palindromic statistic for every semilength; not merely a few tiny examples. The restriction and its limits are explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
