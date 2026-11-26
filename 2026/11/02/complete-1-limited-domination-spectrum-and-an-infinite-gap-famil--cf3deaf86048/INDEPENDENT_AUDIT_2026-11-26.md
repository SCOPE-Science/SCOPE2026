# Independent mathematical audit

## correctness

PASS

The local inequality uses three distinct neighbors for n>=3, including the triangle layer at n=3; it requires at least one selected neighbor outside D and at least two inside D. An indexed mask sequence fixes a unique based closed walk, so the trace has no division by n. An exact independent signed-subset determinant computation on all 16 states gives the stated factorization (16 nonzero terms). There is also a small algebraic check: on the ten recurrent states the odd layer-swap sector has determinant 1-tz+t^2 z^3; eliminating unit pivots in the even sector gives (1-tz-t^2 z^3)(1-tz^2-(t^3+t^4)z^4)-2t^3 z^5=(1-tz)Q. The cut bounds give the sharp minimum n; equality forces exactly one crossing edge at each vertex, giving the two layers or the four phases of 0011. In the normalized characteristic factors the nonzero base roots are simple within each factor; roots vanishing at z=0 contribute only from degree n onwards. Direct expansion at 1,-1,i,-i in the quintic gives the four recorded Taylor rows, so summing n-th powers proves the two near-minimum formulas even at n=3. For even n a full layer plus an adjacent pair in the other layer witnesses positivity at n+2, establishing the internal gap and non-unimodality.

## originality

PASS

Pass relative to the inspected antecedents for the labelled size distribution and the explicit low layers and parity gap, not for the scalar minimum or the transfer-matrix method. A distinct Nov. 8 Resultary entry states exactly the same full series and minimum count; it is equivalent coverage and entails the parity gap, not merely a similar topic. It is indexed after the Nov. 2 frozen entry and supplies no evidence of pre-existing coverage of that entry. No independence or first-discovery claim follows from these dates.

## value

PASS

A natural constrained domination polynomial on a canonical cubic family is determined exactly. The near-minimum coefficients reveal a genuine infinite support gap, explaining why the intuition from ordinary domination polynomials fails under this selected-vertex constraint. This is more informative than either a generic bounded-width transfer construction or the scalar minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
