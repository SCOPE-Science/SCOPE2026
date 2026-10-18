---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For squarefree n=pqrs with p<q<r<s, sigma(n)=2phi(n) becomes H(p)H(q)H(r)H(s)=2, H(t)=(t+1)/(t-1) strictly decreasing. Even n and p=3 are excluded; p>=13 gives product <(7/6)^4<2. Ordered q/r monotone bounds leave exactly p,q in (5,11),(5,13),(5,17),(7,11) and 15 eligible triples. For any triple A=H(p)H(q)H(r), fourth prime is uniquely s=(2+A)/(2-A) if A<2. Independent rational branch enumeration reproduced exactly eight prime quadruples: (5,11,23,109), (5,13,17,127), (5,13,19,71), (5,13,23,43), (5,13,29,31), (5,17,19,31), (7,11,13,29), (7,11,17,19). The packaged exact verifier was read, but infinite exhaustiveness is from the displayed inequalities, not a blind size cutoff.

## originality

PASS

The exact eight-element support-four classification is not established by the inspected prior sources. Broughan–Delbourgo (2013) exhaust solutions with at most three distinct primes; Broughan–Zhou (2014) Table 3 offers one support-four example rather than a classification. OEIS A062699 lists all eight near its beginning but does not establish their exhaustiveness within this constrained support class. Best-of-knowledge PASS with explicit risk of unindexed elementary enumeration.

## value

PASS

Four prime factors are the first squarefree-support size beyond the published support-at-most-three exact theorem. Its unbounded, exact eight-solution classification is a natural next case, explains the database prefix, and closes a motivated invariant rather than an arbitrary numeric cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
