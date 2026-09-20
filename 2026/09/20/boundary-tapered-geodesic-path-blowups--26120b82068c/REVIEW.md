# Same-model scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.  In a path blow-up, distinct-layer endpoint pairs have exactly one free
choice in every intermediate layer, giving the product term in (1).  Same-layer
pairs have distance two and their geodesics are in bijection with vertices in
the two adjacent layers, giving the second term.  These cases exhaust all
unordered endpoint pairs.

For the tapered sequence \((1,2,3,\ldots,3,2,1)\), the recurrence
\(E_j=a_j(1+E_{j-1})\) evaluates the distinct-layer contribution exactly, while
the same-layer contribution is \(18(q-2)+2\).  The resulting closed form was
algebraically checked against the exact equal-layer formula from Proposition 3
of Knor et al.; their difference is \(10\cdot3^{q-2}-15>0\) for every \(q\ge3\).

A separate finite verification constructs the graphs explicitly and counts
shortest paths by breadth-first search for \(3\le q\le8\).  It also exhausts all
path-blow-up compositions for \(n=9,12,15,18\).  The computation agrees with the
closed forms.  The proof, not the finite computation, establishes the infinite
family.

## Originality

PASS, to the best of our knowledge.  The directly inspected primary source is
Knor--Sedlar--Škrekovski--Zhang (2026).  Proposition 3 treats equal-size
sequential joins \(G_{k,t}\), and Problem 14 explicitly asks for a graph whose
geodesic subpath number exceeds the \(G_{3,n/3}\) benchmark and/or for a better
general upper bound.  The present unequal-layer path blow-up gives such a graph
for every \(n=3q\), \(q\ge3\).

Searches using the exact invariant name, the source title and Problem 14,
sequential joins, unequal layer sizes, path blow-ups, and equivalent language
about counting shortest paths did not locate a later paper containing the
formula for arbitrary path blow-ups or the boundary-tapered family.  The main
residual risk is the recency of the invariant: a follow-up may be incompletely
indexed or may use different terminology.  No claim of exhaustive literature
coverage is made.

## Value

PASS.  The result answers one side of an explicit open problem from the
foundational paper on this invariant.  It improves the leading constant in the
best construction exhibited there by the factor \(121/81\), while keeping the
same \(3^{n/3}\) exponential scale.  The general path-blow-up formula also gives
a reusable exact expression for searching and comparing unequal layer profiles.

## Evidence and limitations

The proof is self-contained once the definition of the invariant and the
published formula for \(G_{3,q}\) are fixed.  The finite checks are supporting
evidence only.  The result does not prove optimality of the tapered family among
all path blow-ups or all graphs, does not address orders not divisible by three,
and does not improve the universal upper bound.  Originality is to the best of
our knowledge.
