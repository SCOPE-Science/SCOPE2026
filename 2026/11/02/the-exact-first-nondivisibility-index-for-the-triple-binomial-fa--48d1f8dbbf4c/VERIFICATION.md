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

For B=binom((b+3)n,3n−1), the C_n block-rotation action is free because gcd(n,3n−1)=1, proving n|B; the adjacent-binomial identity makes bn+1 divisibility equivalent to 3n|B. Kummer guarantees an extra 3-factor whenever 3∤bn+1; remaining cases use Lucas digits. If b≡0 mod3 every n succeeds; b≡2 fails at n=1; for b≡1 and s=v3(b+2), digit constraints force n≥(3^s+1)/2, and the candidate with base-three digits (2,1,...,1) attains equality. Independent exact-integer divisibility checks passed in 1917 cases and deeper witnesses; finite checks corroborate the all-b proof.

## originality

PASS

Sun defined the least failure f(a,b) and a general gcd-corrected divisor; Guo–Krattenthaler proved infinitely many failures plus a general bound for many a,b. Neither primary theorem states the precise a=3 first-index classification by v3(b+2). The full single-parameter family and arbitrary valuation depths are derived separately here.

## value

PASS

It solves an entire natural fixed a=3 family of an existing published first-nondivisibility invariant and exhibits arbitrarily long first-success segments as b=3^s−2 grows; an exact arithmetic index a researcher can cite, not an arbitrary case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
