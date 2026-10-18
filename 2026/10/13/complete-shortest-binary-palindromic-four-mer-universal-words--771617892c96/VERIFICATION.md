---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Reversal partitions the sixteen binary 4-mers into ten classes, four fixed and six paired. The unoriented reflected binary de Bruijn graph on six reversal classes of 3-mers has vertex degrees 3,5,2,5,2,3, hence four odd vertices and no Euler trail through the ten edge classes once. Mirror factors exclude lengths ≤21 by cardinality, and at lengths 22 or 23 the first ten factor positions would require a ten-edge Euler trail, impossible. For length 24, each palindrome W=U rev(U), |U|=12, corresponds bijectively to its length-14 prefix P with palindromic terminal 4-mer; all sixteen 4-mers appear iff the eleven length-4 windows of P hit all ten reversal-orbits. Exhausting all 2^14 length-14 binary P once gives exactly six. Independently also enumerating every binary palindrome through length 24 recovers no smaller cover and precisely six at the optimum. The lower bound itself is explicitly credited to 2016 work; new claim is the full equality list.

## originality

PASS

Burris–Motta–Shipman already derive the length-24 lower bound from an unoriented de Bruijn parity obstruction and construct an order-four instance; it does not enumerate all optimal globally palindromic binary words. The six exact equality cases, with three bit-complement pairs, are the contribution. Orenstein studies reversal-covering peptide templates, which do not require one linear word globally palindromic and do not specify this exact six-list.

## value

PASS

The equality-case census closes the natural extremizer classification at the first non-Eulerian unoriented de Bruijn order. It gives explicit templates and the exact diversity of shortest palindrome covers, a natural finite combinatorial invariant beyond the known minimum length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
