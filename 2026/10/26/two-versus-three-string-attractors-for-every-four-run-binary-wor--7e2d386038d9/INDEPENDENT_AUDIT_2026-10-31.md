# Independent mathematical audit

## correctness

PASS

Every distinct factor either is constant, contains one 01 transition or contains the unique central 10 transition. The unique 10 adjacent pair forces any attractor to select its U or V position, and then all multi-transition factors are covered. Longest constant runs suffice for constant factors. One-transition 01 factors correspond to union of two integer rectangles [1,a]×[1,b], [1,c]×[1,d]. Four explicit two-position witnesses cover the aligned-maxima cases and crossed cases with one run-length excess≤1. The remaining (a>c,d>b) regime has three disjoint forced factors; for (c≥a+2,b≥d+2), a chosen central U or V leaves an explicit 01 factor inaccessible to any second position. Two explicit three-position sets cover all other words. Disjoint parameterizations of those two obstruction regions give the rational generating function and dominant pole ratio 1/2. Independent direct factor-occurrence-mask enumeration tested all 625 quadruples with lengths 1..5, plus exact coefficient comparisons for n=4..18. These are finite checks; the proof exhausts all positive run lengths.

## originality

PASS

General efficient attractor algorithms and special infinite-word results do not yield the precise two forbidden four-run inequalities or their complete composition-generating function; finite length-12 tables are not an all-length theorem.

## value

PASS

Exactly four alternating runs are the first natural run-complexity setting with a nontrivial two-versus-three alphabet-lower-bound transition. A complete four-parameter decision with explicit optimal witnesses, exact enumeration and limiting density is a self-contained useful combinatorial classification, not an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
