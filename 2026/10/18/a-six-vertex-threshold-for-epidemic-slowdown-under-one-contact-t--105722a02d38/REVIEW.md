# Scientific review

**Claim.** For the exactly defined uniform-seed, one-contact, one-generation SIR process, adding a hub-to-hub edge to \(K_{2,m}\) changes the mean cumulative outbreak by \(-\frac{m^2-3m-2}{2(m+1)^2(m+2)}\). The first strictly decreasing example under any connected-graph single-edge addition has six vertices.

## Correctness — PASS

The transition is a random walk stopped at its first revisit; exact first-step conditioning proves the finite, acyclic Bellman recurrence for the cumulative infection count. Counting survival through successive newly infected vertices gives four explicitly checked hub/peripheral expectations. Rational simplification yields the uniform-root formulas and the sign threshold for all positive integers \(m\). A standalone standard-library verification program reproduces the formulas for \(1\le m\le16\). The minimal-order assertion is independently backed by enumeration of **all labelled** connected simple graphs of orders \(2,3,4,5\) and every missing-edge insertion: \(1,4,38,728\) graphs and \(0,3,84,3140\) comparisons, with zero decreases. Two distinct exact computations—subset Bellman recursion and terminal path-weight summation—agree on each graph. Finite checks certify only the bounded enumeration, not an infinite extrapolation.

## Originality — PASS, with bounded residual uncertainty

Source inspection compared equivalent one-out epidemic-percolation formulations (Kenah–Robins, 2006), one-neighbor contact processes (Gómez et al., 2009), exact final-size algorithms for acyclic time-expanded contagion (Enright–Kao, 2016), and empirical SIR outbreak size sensitivity (Holme, 2015). These supply model context or general-purpose methods but not the specific uniform-seed contact-budget edge-insertion sign law or its sharp six-vertex minimum. Additional scientific-result searches addressed aliases including random walks stopped at a first repeat, stochastic epidemic final size, degree-normalized contact choice, complete-bipartite hub joins, and finite minimality. The closest independently published mathematical findings concern two-patch SEIR reproduction thresholds, threshold-burning source optimization, contact-law consistency, graph-indexed walk ranges, and convex ellipsoids on the same book-graph family; each uses a distinct statistic or process and does not imply the claim. Searches cannot prove global novelty; equivalent but unindexed work remains a risk. No unresolved primary statement inspected directly covers the claim.

## Value — PASS

Ordinary independent-edge epidemic transmissibility increases when new contacts are made available, whereas a *fixed per-person contact budget* redistributes probabilities over neighbors. This distinction matters for how network interventions are interpreted. The exact infinite family locates a nontrivial sign change at four peripherals, the sharp minimum order is established without sampling, and the explicit first counterexample supplies a reproducible boundary to an intuitive monotonicity heuristic. The magnitude \(1/150\) in the smallest case is small, so the claim is a qualitative model-choice boundary, not an assertion of large epidemiological impact. Neither correctness of code alone nor novelty of a graph identity is used as the value argument.

## Closest literature and limits

Kenah & Robins, arXiv:q-bio/0610057 (sections on SIR outcomes and epidemic percolation networks); Gómez et al., arXiv:0907.1313 (one-contact kernel but reinfectious SIS stationary analysis); Enright & Kao, DOI:10.1016/j.epidem.2016.05.002 (exact expected size on directed acyclic contagion); Holme, DOI:10.1038/srep14462 (SIR final sizes under changing contact-pattern information). None states this claim. Larger graph orders, other contact budgets, nonuniform seeding, and higher contact success probabilities are not classified. The named first-size bound is exhaustively proven only via transparent finite exact enumeration through five vertices plus a witness at six; no general large-order enumeration is claimed.

Self-review: passed. Independent audit: not yet performed.
