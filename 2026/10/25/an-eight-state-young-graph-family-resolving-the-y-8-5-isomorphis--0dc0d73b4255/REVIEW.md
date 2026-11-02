# Independent mathematical audit

## correctness

PASS

The paired reverse-multiplication carry equations for each outer digit pair are k u+R=v+g Rnext and k v+Lnext=u+g L, with carries in [0,k-1], digits in [0,g-1]. For g=n^2-1 and k=n^2-n-1, n^2=1 mod g and g-k=n; substitution shows a unique digit v for each u and two admissible successors of each of the eight proposed states, after a shift h=v-L constrained to 0<=h<=n. The symbolic inequalities force h to the two listed values for each state; no other states are reachable, and the 16 edges, initial nonzero edge, reversal symmetry and even/odd pivots are explicitly verified. The boundary n=3 gives exactly g=8,k=5, with eight distinct states. The common adjacency matrix has four even and four odd pivot targets and the path counts are 2^(t-2) for each parity at digit lengths 2t and 2t+1, t>=2, exactly Sloane's rational generating series. I independently enumerated all legal outer digit transitions, reachability, pivot sets and counts for n=3..24, with all cases passing. This finite range is corroboration; the universal bounds on h and congruence prove all n>=3.

## originality

PASS

L. H. Kendrick (2015), Section 6.1, Conjecture 3 states the exact family Y(n^2-1,n^2-n-1) is isomorphic to Y(8,5); I inspected the original PDF page with the literal statement. Kendrick's proved theorems cover 1089 graphs, complete graphs and other categories, but not this family: k+1=n(n-1) does not divide g=(n-1)(n+1) for general n>=3, while asymmetric carry states exclude the complete/symmetric graph cases. N. J. A. Sloane (2013), Section 4, had already computed the reference Y(8,5) graph with eight states and sixteen edges and the generating series. Those are not original. Holt's carry and shifted-symmetry conditions similarly differ. No inspected subsequent full proof of the published Conjecture 3 was identified. The new transfer is the uniform symbolic graph isomorphism, not the known reference enumeration.

## value

PASS

The result resolves a precise conjecture published in 2015, giving a parameter-uniform graph structure rather than a table of checked pairs or arbitrary numeric pattern. Its explicit eight-state graph and pivot correspondence transfer a known enumeration to an unbounded quadratic base/multiplier family and make exact counting formulas uniform. Does not classify all Young graph isomorphism classes or assert digit-label identities across bases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
