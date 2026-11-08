# Independent mathematical audit

## correctness

PASS

For every smooth y²=x⁷+a x⁵+b x³+x over algebraic closure F5, the Cartier/Hasse coefficient rule from f² gives H=[[2b,0,1],[0,2(ab+1),0],[1,0,2a]], det=-2(ab+1)². On ab=-1 its outer block has rank one and twisted second Frobenius coefficient 2(b^5+a) is zero precisely at b^6=1; otherwise rank one persists, giving a-number/rank (2,0) at six roots and (2,1) elsewhere, versus (0,3) off divisor. The cubic discriminant Delta=a³+a²b²+3ab+b³+3 restricts to (b³-2)²/b³ and its three excluded zeros do not meet b^6=1. Six roots distinct; Frobenius sends b to b^-1 and gives orbits 1,1,2,2. Explicit scaling and inversion exchange all marked exceptions. Actual verify_symbolic.py and verify_fields.py were inspected; separate independently regenerated exact coefficient/determinant/discriminant computations verify critical identities. Finite F5/F25 counts are supplementary.

## originality

PASS

PASS best-of-knowledge for complete coefficient-marked 2-parameter double Hasse divisor and the six stable-rank-zero fibers; related hyperelliptic point-count results concern a different model, while standard Cartier theory supplies method but not these strata.

## value

PASS

A complete algebraic stratification of a natural genus-three automorphism-rich two-parameter family, including a scheme-theoretic double nonordinary divisor and the deeper finite stable-rank-zero locus. These precise invariants and marked-versus-isomorphic distinction can be reused in arithmetic geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
