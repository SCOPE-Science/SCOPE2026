# Independent mathematical audit

## correctness

PASS

PASS: Exact 3-round Ehrenfeucht–Fraïssé recursion records the complete atomic equality and multiplication diagrams over zero and three chosen elements, recursively collecting all possible child-type sets. The inspected C++ source implements structural equality of these diagrams and nested sets; compiled and independently executed for all n=1..26, obtaining root classes 0,1,...,8,8,...,8. A separately implemented immutable Python recursion agrees for n=1..10. For arbitrary n,m>=26 a 3-move order game selecting up to two new endpoints per move has gap cutoff t_r=3t_(r-1)+2: 2,8,26; ordered equalities of selected six endpoints determine every relational multiplication atom. Thus tail equivalence is proved by induction, and the exact finite bridge U9~U26 gives the all-n sharp classification.

## originality

PASS

PASS best-of-knowledge: The equivalent positive-length path semigroup was searched explicitly. Existing logical EF results on word omega-terms, directed successor paths, small nilpotent-semigroup enumerations and full Brandt matrix units do not assert this rank-three classification or imply its n=9 threshold. The complete 2010 Distler thesis was not read and remains a priority risk.

## value

PASS

PASS: Complete finite-depth first-order classification of a natural growing family of nilpotent matrix-unit/path semigroups, with surprising stabilization at nine indices despite unbounded nilpotence indices and a sharp minimal 37-element class representative. A mathematically reusable exact logical invariant, not a raw small-order table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
