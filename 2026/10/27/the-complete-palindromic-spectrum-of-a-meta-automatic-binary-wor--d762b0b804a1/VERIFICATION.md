---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For the exact 4-uniform morphism φ(0)=0112, φ(1)=1230, φ(2)=2301, φ(3)=3023 with coding 0,2↦0 and 1,3↦1, the set of all adjacent state-letter pairs is T={01,02,03,11,12,13,21,22,23,30}: all occur in φ⁴(0), and checking factors of φ(xy) for xy∈T proves closure under further substitution. Every binary factor of length ≤18 occurs within or across one boundary of 64-symbol φ³-coded blocks, so it is present in one of the ten coded 128-symbol φ³(xy) words, and conversely every word appears in the true fixed point. Direct exhaustive enumeration of that globally justified finite cover yields P(1..18)=(2,2,2,2,2,2,2,2,2,3,0,3,0,2,0,2,0,0), total 28 palindromes and exactly two length-16 examples. Absence of length-11 odd and length-18 even central palindromes forbids every longer odd/even palindrome, so finite coverage proves the infinite classification. All 28 first occur by prefix length 196, with the last length-16 occurrence beginning at index 180; the length-195 prefix has 27, establishing Def(u[0,N))=N−28 for N≥196 with sharp onset. Independently reconstructed φ iterates, exact T-closure, the 10×128 cover, palindrome sets, and sharp first occurrence; this check relies on proof of global factor coverage rather than treating a finite prefix as exhaustive.

## originality

PASS

Best-of-knowledge original contribution as delimited by the final assigned theorem, not novelty of its foundational method. Direct original statements and implications were compared against the checked primary results and the published-finding search. Highly relevant inaccessible works remain named as residual priority risks; no failed search or abstract alone proves whole-document noncoverage.

## value

PASS

A complete palindromic complexity function, longest palindromes and exact prefix-defect stabilization for a naturally constructed new automatic word are motivated combinatorial invariants. The global finite bound is structurally nontrivial: it uses substitution pair closure and the central palindrome obstruction, not a routine small sample or a known OEIS table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
