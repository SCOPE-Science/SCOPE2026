# Independent mathematical audit

## correctness

PASS

For parabolic-longest idempotents, support of a Demazure product is the union, so if the idempotents commute their product is the parabolic-longest idempotent of the union. If a union component contains both an I-only and a J-only vertex, take a Coxeter element spelled with a path from the J-only vertex to the I-only vertex in that order. Its reduced expressions are connected by commutations alone, since every generator occurs only once and a braid of length at least 3 cannot apply. The oriented path therefore forces the J-only vertex before the I-only vertex. The reduced subword retained in scanning the two longest words would, by the Bruhat subword property, yield an expression for that Coxeter element with the opposite order, a contradiction. Conversely, a component wholly in either subset is absorbed by its own longest element, and distinct components commute. For fixed union, two choices of containing subset give 2·2^|C|−1 assignments per component. The rooted four-state recurrence counts vacant roots, occupied all-common roots, and root components with exactly one exclusive color present. In the path variables u,v with t=2v−u it reduces to (u,v)↦(2v,4v−u), so t has characteristic polynomial x²−4x+2. The branch-addition identities follow by the same recurrence in the second branch size, with bases b=0 and b=1 using (t₁,u₁,v₁)=(4,2,3). Root at a leaf to ensure at most two children in a subcubic tree. This establishes shape invariance, not merely a finite-rank check. Conditioning on the center of K₁,₄ gives 4⁴+4·3⁴−2⁴=564. Classification of the finite irreducible diagrams and direct-product multiplicativity give all stated types and the reducible formula. Frozen verify.py and VERIFICATION.md were inspected without running uploaded code. A fresh bounded check of right-Demazure multiplication in types A₁–A₅ matched every ordered pair, and a Prüfer enumeration matched all labelled subcubic trees through seven vertices; the latter totals by size were 4,14,48,164,560,1912,6528. No independent replay file was supplied for those supplementary finite checks; the frozen replay entry point is python3 verify.py in the record directory.

## originality

PASS

Best-of-knowledge pass as an assessment of prior coverage of the frozen result. There is an exact later match, not merely a similar title or integer sequence: Berenstein–Greenstein–Li arXiv:2605.09761v3 Propositions 3.33 and 3.37 contain the criterion (in an equivalent component language), the subcubic invariant, and its Coxeter consequence. That version is dated 18 November 2026 UTC. The inspected public v1 and v2 before the frozen record give partial sufficient cases and an expectation, not this theorem. No inference about independent discovery or authorship is made from chronology; this is version-specific evidence about what was publicly stated. The same-day Catalan specialization and the preexisting sequence receive no originality credit.

## value

PASS

The rank-independent commutation count is a natural invariant of a standard monoid. A uniform positive criterion reduces it to the unlabelled diagram, and the subcubic tree theorem explains why genuine branching and edge labels disappear from the answer. The degree-four witness delineates that explanation. The known numerical sequence or a few type-A computations alone would not have this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
