# Independent mathematical audit

## correctness

PASS

Use 0 as opening and 1 as closing parenthesis and forbid factors with exponent strictly greater than 7/3 (not factors exactly at 7/3). The 24-letter witness 001001100100110110011011 is balanced, has nonnegative prefix heights of maximum 4, is reverse-complement invariant, contains 1001001 of period 3 and length 7 (exact exponent 7/3), and has no factor with 3*length > 7*period. An independent prefix construction exhausts every Dyck word at every even length 2..24, pruning only already-created forbidden suffixes: there are no level-4 survivors below 24 and at 24 precisely 40 level2,36 level3 and ONE level4 survivor, the witness. The original certificate and verifier code were inspected; the independent enumeration regenerated its count table. The finite classification is an exhaustive proof of the bounded minimality/uniqueness claim, not an unbounded theorem about all nesting levels.

## originality

PASS

Best-of-knowledge original narrow result after comparing actual mathematical implications with primary source and adjacent literature: Theorem 2.1 rules out 7/3-power-free height4 (exponents >=7/3 forbidden); a different strict >7/3 predicate permits the 24-word boundary witness. The source's 228-letter construction does not establish 24 as minimal or unique.

## value

PASS

The original threshold paper proves height <=3 for non-strict 7/3 avoidance and existence at arbitrary nesting for strict 7/3+ avoidance, giving level 4 through a much longer substitution witness. The least first-new-height witness (24) and uniqueness at the critical exact-boundary repetition are natural unknown sharp invariants, independently useful in combinatorics on words even without a formula for all heights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
