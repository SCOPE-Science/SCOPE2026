# Independent mathematical audit

## correctness

PASS

The word model h+v+2d=n, rank v+d and precisely the covers H→V, HH→D and D→VV were reconstructed from RESULT.md and verifier code. For every lower rank pair the integer-capacity source-to-upper flow saturates iff all subsets satisfy normalized matching (Hall/max-flow min-cut). The H/V order-reversing involution gives upper halves; on odd sizes the first-unmatched-H to V bijection supplies the equal-size central pair. Independent Python Dinic checked every lower-half comparison n=0..10; independently reconstructed C++ integer-flow verifier completed n=0..13, n=14..17, and n=18 in disjoint k=0..5,6,7..8 runs (largest exact flow 1837659219795). All capacities and tested totals fit int64. Finite exhaustive proof is limited to n<=18; no statement for n>=19.

## originality

PASS

Chen and Dong first posed normality for these size-indexed Delannoy lattices and established n<=5, so the verified complete finite extension to n=18 is a distinct progression, not the conjecture for all n. The older fixed-endpoint Delannoy path lattice has different rank universe and does not directly cover this union of endpoints. No stronger indexed Resultary record was retrieved. The directly relevant source full text was not accessible; record priority risk rather than claim comprehensive noncoverage.

## value

PASS

A substantial exact finite cutoff n<=18 for every normalized matching inequality advances a natural explicit open conjecture from n<=5. The complete max-flow certificate makes the all-subsets result meaningful, without extrapolating to all sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
