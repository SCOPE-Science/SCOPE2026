---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Over a fixed labelled poset, one-point extensions are precisely disjoint ideal/filter pairs L,U with all L<U. In Q=A⊕B there are 2^(a+b) middle placements and 2^a-1 and 2^b-1 upper/lower placements. Removing u<v permits two previously forbidden placements and disallows 2^(a+b-2) formerly permitted u<x<v placements. Thus c(Q)=2^(a+b)+2^a+2^b-2, c(P)=3·2^(a+b-2)+2^a+2^b and the difference=2^(a+b-2)-2 for a,b>=1, including the negative a=b=1 case. Independently reconstructed an exhaustive generator of transitively closed strict labelled posets and tested all n<=4 and all legal directed added comparabilities, obtaining labelled poset counts (1,3,19,219), 1044 additions at n=4, 120 positive changes, none for n<=3. The last six-isomorphism-class multiplicity breakdown was reported by supplied verifier but was not separately canonicalized in this run.

## originality

PASS

Best-of-knowledge, subject to explicitly documented priority risks: searched the available Resultary records and primary literature, compared the exact claimed quantifiers/invariants to prior implications rather than matching titles, and did not treat inaccessible full text as proof of noncoverage.

## value

PASS

A single relation making a finite order more constrained can nevertheless increase the number of labeled one-point extensions by an exponentially growing amount; this reverses a plausible monotonicity expectation and gives the sharp four-point threshold. The exact jump is independently useful in random-poset type counting and one-point-extension enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
