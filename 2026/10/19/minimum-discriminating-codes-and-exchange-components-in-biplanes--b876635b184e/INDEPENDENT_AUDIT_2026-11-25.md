# Independent mathematical audit

## correctness

PASS

There are only 15 nonempty subsets of four selected points, so at least five are required. For exactly five, counting blocks, selected incidences and selected pairs in blocks gives sums 16,30,20 for the trace-size weights 1,j,binom(j,2). Nonempty distinct traces force r1≤5. Eliminating yields r1=8−r4−3r5 and r3=6−3r4−6r5; r1≤5 and r3≥0 then give r5≥1, and r5≤1 by uniqueness of the full trace. Thus r5=1 and r4=r3=0. Conversely for C=B∖{p}, the second block on each of the 15 pairs in B is distinct because each other block meets B in exactly two points. These pairs give exactly five singleton and ten doubleton traces, and B gives C. Thus each of the 16 blocks supplies six distinct codes, and the same block never shares a 5-subset with another block. Same-block punctures intersect in four points; different-block punctures intersect in at most two. Thus the exchange graph is 16K6 with 240 edges. The proof uses the design axioms uniformly and does not require the classification of realizations or an exhaustive program.

## originality

PASS

Bailey's versioned Proposition 14 proves the punctured-block separation construction in any biplane, and nonemptiness follows at once from two-point block intersections. This already implies the minimum size and a known family of 96 candidates at these parameters, using the elementary information bound. The supported distinct claim is the converse for nonempty traces, hence the exhaustive count and exchange decomposition, not the construction. The closest Resultary match also counts 96 size-five codes but uses closed neighborhoods of the Shrikhande graph and has 16 cycles instead of 16 cliques. The available statements do not establish an equivalent classification. Earlier inaccessible design-catalogue literature remains a named bounded risk.

## value

PASS

The parameter set is a natural small biplane family and the minimal code model is independently defined by nonempty distinct incidence signatures. The converse resolves the full equality structure for every realization, ruling out any optimal single-point reconfiguration between block families. That exact structural information is useful beyond a numerical census or the prior construction, even without a theorem for larger biplanes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
