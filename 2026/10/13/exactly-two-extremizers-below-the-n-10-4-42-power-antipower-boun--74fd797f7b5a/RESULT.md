# Exactly two extremizers below the \(N(10,4)=42\) power-antipower boundary
## Finding
A binary \(10\)-power is a factor consisting of ten consecutive copies of the same nonempty block. A binary \(4\)-antipower is a factor consisting of four consecutive equal-length blocks that are pairwise distinct.

The published exact threshold is \(N(10,4)=42\). The complete length-\(41\) equality layer consists of exactly two words:
\[
\mathtt{00101010101010101010001010101010101010100}
\]
and
\[
\mathtt{11010101010101010101110101010101010101011}.
\]
They are bitwise complements, so the whole extremal layer is one complement orbit of size \(2\). Both extremizers are palindromes.

## Assumptions and scope
For integers \(k,r>1\), \(N(k,r)\) is the least length such that every binary word of that length contains either a \(k\)-power or an \(r\)-antipower as a contiguous factor.

The scalar value \(N(10,4)=42\) is prior work from Riasat's exact table. The claim here is only the complete classification of the longest avoiding words at that known boundary.

## Proof
Both forbidden properties are factorial, so prefix generation is exhaustive. From a valid prefix, append either bit. Any newly created forbidden factor must end at the new final position. Testing all possible suffix block lengths therefore decides whether the extension remains valid.

This exhaustive generation gives survivor counts
\[
40,34,30,26,18,14,10,6,4,2,0
\]
at lengths \(32,33,\ldots,42\). Hence precisely two words survive at length \(41\), the displayed pair, and none survives at length \(42\).

A second exhaustive engine does not use the suffix invariant: after every extension it rescans every factor of the whole candidate for every possible \(10\)-power and \(4\)-antipower. Its complete levels agree exactly with the first engine. Direct comparison then proves that the two surviving words are complements and that each equals its reversal.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs every avoidance level through length \(42\) by two independent factor-testing implementations, checks the complete survivor-count sequence, checks the exact two length-\(41\) words and the empty length-\(42\) level, and verifies complement symmetry and palindromicity. It also checks that both one-letter extensions of each extremizer are forbidden.

## Relationship to prior work
Riasat's 2019 thesis defines \(N(k,r)\), gives an exact computed table, and records \(N(10,4)=42\). Appendix B supplies a search program whose stated output is the lexicographically least longest binary word avoiding the two forbidden patterns. Thus the scalar boundary and existence of a longest witness are prior work, but the thesis does not enumerate or count all longest avoiding words.

Fleischer, Riasat, and Shallit later report \(N(k,4)=4k\) for \(11\le k\le30\) and conjecture the equality for all \(k\ge11\). The parameter \(k=10\) is the immediately preceding table entry and is exceptional because \(N(10,4)=42>40\).

Exact-string, extremizer-count, and equivalent-formulation searches located no published complete length-\(41\) equality layer. OEIS A275061 counts binary words avoiding \(4\)-antipowers alone, so it does not determine the simultaneous \(10\)-power/\(4\)-antipower extremizers.

## Limitations
This is a finite equality classification at one published threshold. It does not settle the conjecture for \(k\ge11\) or classify longest avoiding words for other values of \(k\).

The public thesis contains search code that could be modified to enumerate all extremizers, so unpublished or unindexed computations may contain the same two-word classification even though the inspected sources do not state it.

## References
1. S. Riasat, “Powers and Anti-Powers in Binary Words,” M.Math. thesis, University of Waterloo, publicly available 2019-08-28, handle 10012/14974.
2. L. Fleischer, S. Riasat, and J. Shallit, “New Bounds on Antipowers in Words,” arXiv:1912.08147v1, first public version 2019-12-17; Information Processing Letters 164 (2020), 106021, DOI 10.1016/j.ipl.2020.106021.
3. OEIS A275061, “Number of binary strings of length \(n\) avoiding \(4\)-antipowers.”
