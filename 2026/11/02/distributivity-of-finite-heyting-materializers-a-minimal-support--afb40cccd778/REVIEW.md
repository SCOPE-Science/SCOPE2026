# Independent mathematical audit

## correctness

PASS

On U, membership of a satisfying consequent J is determined by the test S_p ⊆ J∩I; on Q, J can be any ideal L containing the forced predecessors D(J∩I). Thus the coordinate meet is intersection and the join adds D(K₁∪K₂) to the second coordinate. Union preservation makes this a sublattice of the coordinate product. Conversely a newly forced q witnesses failure of the meet-over-join law by meeting with (∅,↓_Q q). For a given q the trigger is an OR over its support family. A minimal principal trigger in a union occurs in one summand; a nonprincipal minimal support splits into the ideal left after removing a maximal point and that point’s principal ideal, neither of which can trigger q alone. This also handles empty families and I or Q empty. A failed trigger supplies two incomparable points in I and a third point q incomparable to both, below a common p. Restriction onto this induced four-point poset is surjective on ideals, and any extra r makes restriction noninjective: ↓r and the downclosure of its restriction differ at r. Thus equality at nine ideals forces exactly that poset. Only the three two-minimum antecedents can fail there, and each gives the displayed seven-element witness. The separate three-point example has Q empty and a Boolean intrinsic lattice with nonambient join. Support comparisons and greatest-element tests are polynomial in the poset size. A separate finite check (python3 /workspace/review_checks.py, boundary) used direct implication and join tables through five poset points with at most nine ideals; it found only the three (4 points, 9 ideals, 7 materializers) antecedents. This is corroboration, not the all-size proof; the supplied verifier was inspected, not executed.

## originality

PASS

Pass for the exact intrinsic-distributivity criterion and sharp minimum/equality classification, not for the materializer definition, the existence of intrinsic joins, or the four-point example in isolation. A distinct indexed record of the same date gives the identical witness and a closure representation but tests ambient joins; same-day dating does not resolve priority and that witness is not credited as distinct.

## value

PASS

This decides a natural question about a named Heyting equality class without enumerating the ambient lattice when given its poset, and explains exactly which extra join obligations destroy distributivity. The nine-ideal boundary and equality classification are useful beyond exhibiting a single counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
