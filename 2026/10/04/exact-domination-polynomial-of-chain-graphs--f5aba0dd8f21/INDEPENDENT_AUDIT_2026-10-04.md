# Independent mathematical audit

## correctness

PASS

The proof is exhaustive and boundary-safe. Any dominating set meeting both bipartition sides has a unique largest selected \(A\)-class index \(i\) and smallest selected \(B\)-class index \(j\). Domination forces all \(A_t\) with \(t<j\) and all \(B_t\) with \(t>i\), and feasibility is exactly \(j\le i+1\). The case \(j=i+1\) gives the unique cut set \(A_1\cup\cdots\cup A_i\cup B_{i+1}\cup\cdots\cup B_p\); the case \(j\le i\) gives nonempty choices in \(A_i,B_j\), arbitrary choices in intervening classes, and the displayed monomial shift. One-sided dominating sets are precisely the two endpoint cuts. The resulting cases are disjoint and exhaustive. Independently, 77 canonical instances with \(p\le3\) and all class sizes in \(\{1,2\}\) were brute-force enumerated over every vertex subset and matched the closed polynomial exactly.

## originality

PASS

General domination-polynomial papers provide recurrence and splitting machinery, while the recent chain-graph paper found in search concerns the independent domination polynomial. Neither supplies or implies the audited ordinary all-twin-class formula. Resultary searches over published SCOPE findings returned this record and several other domination variants on chain graphs, but no earlier ordinary-domination formula with equivalent boundary-pair content.

## value

PASS

Ordinary domination is a standard graph invariant and chain graphs are a canonical hereditary bipartite class. The result completely enumerates all dominating sets for arbitrary twin-class multiplicities, not merely the minimum size, and yields the total count and domination number as immediate consequences. The extremal-class decomposition is a reusable structural description rather than an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
