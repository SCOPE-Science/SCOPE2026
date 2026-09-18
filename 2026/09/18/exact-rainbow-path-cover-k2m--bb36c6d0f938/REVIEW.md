# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**  The proof reduces all possible colour repetitions to a partial
injection \(\phi\) between the two injective colour lists at the degree-\(m\)
vertices of \(K_{2,m}\).

For \(m=2t\), the first bijection \(\sigma:M\to S\) avoids one partial matching.
For the second bijection \(\tau\), the forbidden pairs are the union of three
matchings: equality with \(\sigma\), the restricted inverse of \(\phi\), and
the restricted inverse of \(\phi\) composed with \(\sigma\).  Hence the allowed
balanced bipartite graph has minimum degree at least \(t-3\).  When \(t\ge6\),
this is at least \(t/2\), and Hall's theorem gives \(\tau\).

The six pairwise comparisons among the four colours on
\(\sigma(u)-x-u-y-\tau(u)\) were checked explicitly.  Three follow from
properness/injectivity and the other three are precisely the avoided
\(\phi\)-relations.  Bijectivity of \(\sigma,\tau\) then shows that every edge
is used exactly once.  The odd case removes one large-side vertex and adds its
rainbow two-edge path.  The matching lower bound is elementary: a simple path
contains at most two edges incident with a fixed degree-\(m\) vertex.

No computation is required for the theorem.

## Originality

**PASS, to the best of our knowledge.**  The nearest direct source located is
Liu--Xu--Yang, arXiv:2609.18740 (submitted 2026-09-16).  Their Theorem 1.2
determines the rainbow path-cover number of complete multipartite graphs only
asymptotically.  Specializing their displayed multipartite formula to
\(K_{2,m}\) yields \((1+o(1))m/2\), not the exact eventual value or the
prescribed-role rainbow \(P_5\)-decomposition proved here.

Searches used the exact object \(K_{2,m}\)/\(K_{2,n}\), "rainbow path cover",
"rainbow path decomposition", "rainbow P5 decomposition", "complete
bipartite", and equivalent proper-edge-colouring formulations.  They found the
Liu--Xu--Yang preprint and older literature on the different question of
existence/avoidance of a single rainbow path, but no result implying the
statement here.  The current SCOPE archive was also checked by object and claim
family, with no overlapping record found.

Residual risk remains because the motivating paper is extremely recent and a
parallel result may not yet be indexed.  No inaccessible paper was identified
whose title or available description specifically suggests the same exact
\(K_{2,m}\) cover/decomposition theorem.

## Value

**PASS.**  The result turns the recent asymptotic complete-multipartite estimate
into an exact formula in the highly unbalanced infinite family \(K_{2,m}\).
It proves more than a cover bound: for even \(m\ge12\) it gives a full rainbow
\(P_5\)-edge-decomposition with an arbitrary prescribed set of middle
large-side vertices, via two elementary perfect matchings.  This also gives a
polynomial-time construction.

## Limitations

The threshold \(m\ge12\) is sufficient rather than optimized, and the finite
range \(m<12\) is not classified here.  No exact result for \(K_{r,m}\) with
\(r\ge3\) is claimed.  Cross-model or independent validation has not been
performed.
