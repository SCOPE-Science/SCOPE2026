# Independent mathematical audit

## correctness

PASS

For x_i=f(a_i) and y_i=f(b_i), the equations are x_i+sum_(j>=i)y_j=0 and y_i+sum_(j<=i)x_j=0. Their consecutive differences force (x_(i+1),y_(i+1))=(x_i+y_i,-x_i), and the two endpoint equations are x_1+y_1=x_n+y_n=0. Conversely the consecutive differences and endpoints recover every original equation, including n=1. The transfer matrix has cube -I and sixth power I. From (t,-t) the six states are (t,-t),(0,-t),(-t,0),(-t,t),(0,t),(t,0); the last endpoint is satisfied for t nonzero precisely when n=1 mod 3. Restricting x_1 to the allowed labels gives t in {-1,0,1}, and every entry in the orbit is then allowed. The successive weight terms 0,-t,-t,0,t,t cancel per period and leave zero at n=1 mod 6 and -2t at n=4 mod 6. This proves the full classification and maximum. Independent direct closed-neighborhood enumeration of 597870 ternary assignments for n=1 through 6 gives the same full solution sets and weights; exact rational rank checks through n=20 give the predicted real nullity 0 or 1.

## originality

PASS

The closest inspected balanced-domination literature gives the closed-neighborhood kernel framework. The two same-day chain/half-graph records actually impose other labeling constraints, not this invariant. The supported distinct claim is the complete normalized ternary solution family and weight phase for the canonical half graph, not the kernel reformulation or a claim to priority for detecting the eigenvalue -1. Exact eigenvector coverage in the inaccessible chain-graph spectral literature remains a specific risk.

## value

PASS

The half graph is a natural canonical chain graph for the established balanced-domination invariant. The result goes beyond detecting a nonzero kernel: it identifies every feasible labeling and shows why two real-kernel-positive residues give different optimal weights. The exact phase and complete family are useful for distinguishing balanced domination from mere adjacency singularity at -1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
