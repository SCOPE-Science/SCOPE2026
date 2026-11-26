# Independent mathematical audit

## correctness

PASS

Let D(X,Y) be inclusive disjunction and let J take all nonempty joins. J is idempotent by flattening joins; dividing any nonempty generating set by its two source sets gives D(JX,JY)=J(X∪Y), including when either set is empty. Thus the right side is J(P(X)∪P(Y)). The left side applies J to P(D(X,Y)); its extra permitters come only from pairs x∨y, and G licenses each in J(P(X)∪P(Y)). This proves equality, and singleton atomic valuations (allowed by binary join closure) give necessity for all t,u. The proof needs arbitrary joins, not finiteness, and does not involve negative content or preclusion. The O(n^4) test checks each of n^3 triples by joining all eligible witnesses below the prospective generated state s; a nonempty such set with join s is equivalent to generation. In the Boolean diamond the specified permission relation fails C1 at the incomparable operands a,b, but their permitters jointly generate top. A smaller complete join-semilattice cannot contain incomparable points, since their join and bottom would give two further points. Independent exhaustive evaluation of all 65,536 relations and all pairs of 14 admissible contents confirmed 42,448 G/schema-valid, 38,416 C1 and 4,032 strict. An analytic replay gives the same counts: the bottom permission column is free (16 choices); at each state there are 7 joint assignments to the other three entries under C1, giving 16*7^4. A strict relation includes top in P({top}) but not in P({a})∪P({b}); this union must contain both a and b. There are 6 choices at each of a,b and 7 at bottom, giving 16*6^2*7 strict cases. The finite packaged replay is artifacts/verify.cpp.

## originality

PASS

The exact positive frame criterion and its cardinality-minimal strict separation from C1 are distinct from the established sufficiency theorem and from correspondence theorems in other semantics. Credit the inclusive clauses and C1 implication to the prior work. The Boolean counts supplement the exact correspondence, rather than supplying its proof.

## value

PASS

A necessary-and-sufficient frame condition pinpoints which exact-permission behavior is actually needed for a natural modal law. The minimal strict witness rules out equating validity with the older sufficient condition, and the finite decision bound and census make that separation testable and concrete. This is a frame correspondence, not an axiomatization or a negative-content result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
