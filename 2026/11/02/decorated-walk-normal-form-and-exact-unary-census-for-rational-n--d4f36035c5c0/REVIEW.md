# Independent mathematical audit

## correctness

PASS

Structural induction under constants, negation, clipped rational shifts, min and max leaves only affine components of slopes -1,0,1 and intercepts integral/d. Pairwise crossings lie on the half-grid, so each full 1/d cell must be a +/-1 step or one of allowed flat/up-tent/down-tent stays. Conversely the clipped component lines are definable and Ovchinnikov’s max–min representation realizes every compatible decorated path. Summation of walks gives 1^T A_d^d 1; independent transfer calculations reproduce the listed counts for d=1..8. The upper bound (d+1)5^d and Doob/maximal inequality lower bound 5^d(d-O(sqrt d)) prove asymptotic d5^d. Ovchinnikov theorem is in the source paper as its main Theorem 4.1, though this package cites theorem number 2.1; bibliographic numbering needs correction, not a change to the mathematical claim.

## originality

PASS

Qualified PASS: the non-expansive fuzzy-logic papers give syntax/interpolation constructions, and Ovchinnikov gives general lattice-polynomial representation, but neither enumerates semantic unary functions for fixed rational denominator nor obtains the decorated-walk transfer matrix and d5^d asymptotic. Searches for term clones/finite automata found no equivalent enumeration; historical clone-language coverage remains possible.

## value

PASS

A complete semantic normal form is an independently useful exact expressivity and equivalence-decision invariant for a motivated non-expansive fuzzy term language. Enumeration is nontrivial since functions agree on a continuum, not merely a finite truth table; the asymptotic d5^d quantifies growth of the restricted clone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
