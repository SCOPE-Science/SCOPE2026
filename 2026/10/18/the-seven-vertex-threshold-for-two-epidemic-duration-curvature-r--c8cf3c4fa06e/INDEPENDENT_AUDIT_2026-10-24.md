# Independent mathematical audit

## correctness

PASS

Rooted-tree unique-path percolation coupling identifies last infected generation with maximum depth of root open-edge component. Exact recursion Q_k(v)=1−∏_children(1−p Q_(k−1)(child)) and tail sum F=Σ_{k≥1}Q_k yield correct polynomials. Completeness for n≤7 follows from all Prüfer sequences for labeled trees and root choices, collapsed by canonical recursively sorted subtree code; 84 isomorphism classes in total. Each F was independently recomputed by a new NetworkX nonisomorphic-tree generator and independent branch-tail recursion and exact SymPy polynomial root counting, yielding frequencies n=2:(1,0,0), n=3:(2,0,0), n=4:(3,1,0), n=5:(5,4,0), n=6:(12,8,0), n=7:(28,19,1). Source CENSUS.csv has exactly one two-root row: 7-vertex three-armed spider (3,2,1), F=3p−p²+2p³−p⁴, Fʺ=−2+12p−12p² with two simple roots (3±√3)/6 and strict −,+,− signs. No statement about n>7.

## originality

PASS

Existing general SIR tree message passing and exact Markov equations are frameworks for expected dynamics, not the finite classification of changes in duration curvature. The 1990 collective Reed–Frost article is only abstract-inspected; it does not establish noncoverage throughout. Targeted Resultary search returned nonlinear SIRS dynamical work but no equivalent minimal-tree cutoff. Potential reliability-polynomial aliases remain priority risks.

## value

PASS

Expected last-infection generation is an interpretable network-process statistic, and its second derivative describes changing sensitivity to per-contact transmissibility. A sharp first occurrence and unique minimizing rooted topology are motivated structural boundaries, contrasting with simpler monotonicity/convexity behaviors of expected infection totals; the result is a complete finite classification rather than a cherry-picked polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
