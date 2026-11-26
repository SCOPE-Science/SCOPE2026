---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At fixed N=n−3, the two-one coordinates A=3a+b and B=2(b+c) determine the third two-one coordinate and S=sum p_i=A+B/2 for the three zero-prefix counts. The one-one-coordinate C=[001] fixes sum p_i^2=2C+S; then [010]=(N−1)S−2C and [100]=3 binom(N,2)−C−[010]. The all-zero and all-one counts depend only on N. A,B and the total force gap shifts (t,−3t,3t,−t), so the change in C is t(c−b+3t), from the squared-prefix changes (t,−2t,t). Its unique possible nonzero root forces the middle gaps to swap, with nonnegativity the only extra constraint. Orienting t>0 avoids all double counting and gives N=a+d+2c+4t in the theorem’s parameters. Subtracting one per doubleton yields the displayed rational series, including zero terms below n=3. The first pair has N=4 and is exactly the stated pair of length-seven words. The doubleton series has leading pole 1/[8(1−z)^4] at 1; other poles have order at most two. It follows that there are N^3/48+O(N^2) doubletons, establishing both the coefficient 7/48 for distinct decks and the 1/4 ambiguous-word limit. An independent direct positional count for 0–8 zeros, 495 words, found 472 fibers and 23 doubletons, all as predicted.

## originality

PASS

The generating function as a conjecture, the gap-line direction, the binomial difference underlying the collision test and the cubic-order result all have antecedents in Chrisnata et al. Credit the completed equivalence for the entire deck, the exhaustive nonredundant enumeration of doubletons, and hence the proved identity, not the original ingredients or the formula's conjectural discovery. Several separately indexed records give equivalent proofs or classifications and are recorded as material coverage; their catalogue paths are later than the frozen record's, but path dates alone do not establish priority or independent discovery. No earlier established proof surfaced in the evidence inspected.

## value

PASS

This solves a specifically posed exact enumeration question and explains the source of every lost count, rather than just determining the leading order. The collision classification also answers word-level reconstruction at weight three, with the sharp first ambiguity and the limiting failure fraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
