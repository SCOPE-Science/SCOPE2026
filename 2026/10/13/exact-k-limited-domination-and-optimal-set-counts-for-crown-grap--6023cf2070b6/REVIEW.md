# Self-review

## Correctness
PASS. The proof reduces every feasible set to the two deleted-matching index supports. A selected vertex sees \(n-t\) outside neighbors when its mate is selected and \(n-t-1\) otherwise, giving exact lower bounds rather than estimates. Intersecting supports force \(s,t\ge n-k\); disjoint supports force \(s,t\ge n-k-1\), while domination independently forces \(s,t\ge2\). These constraints yield the stated saving window and the exceptional endpoint \(k=n-2\). The constructions attain the bounds, and the support descriptions give the optimum-set counts. A direct finite replay confirms values and counts on all tested cases.

## Originality
PASS. The closest primary source introduces \(k\)-limited domination, gives the exact complete-bipartite formula, and proves the regular-graph equivalence with \((1,t)\)-domination, but its full text has no crown or matching-deletion treatment. Searches under the invariant name, \((1,t)\)-domination, pitchfork terminology, crown/deleted-matching aliases, the exact phase-transition expression, and optimum-set counting language found no covering theorem. A prior exact complete-multipartite result does not apply to crown graphs. The residual risk is an older or poorly indexed equivalent formulation under an alias.

## Value
PASS. The result gives a complete two-parameter evaluation on the canonical graph obtained by deleting one perfect matching from \(K_{n,n}\), exactly quantifies when that deletion changes the newly introduced invariant, and classifies and counts every optimum set. The intermediate-capacity saving window is a structural transition, not a routine recomputation.

## Closest literature and limitations
The closest source is Božović–Radić–Kovijanić-Vukićević–Tepeh, which gives \(\gamma_k^{\mathrm L}(K_{n,n})=2(n-k)\) for \(1\le k<n\) and the regular-graph bridge \(\gamma_k^{\mathrm L}=\gamma_{1,d-k}\). Recent follow-ups concern Cartesian products, Sierpiński graphs, complexity, and cubic Goldberg graphs. The theorem here is limited to crowns; arbitrary partial matching deletions remain open in this analysis. Finite checks do not replace the analytic proof.

Self-review: passed. Independent audit: not yet performed.
