# Independent mathematical audit

## correctness

PASS

The rook graph K_m□K_n is L(K_{m,n}); selected rook vertices induce an acyclic graph precisely when the chosen bipartite edges form a linear forest (no degree>=3 and no cycles). For labeled path components, isolated vertices contribute x+y; balanced paths with r vertices per side contribute (xy)^r z^(2r−1), and unequal-shore paths contribute (x+y)(xy)^r z^(2r)/2. The labeled exponential formula yields exp(x+y+[xyz+xy(x+y)z²/2]/[1−xyz²]) exactly as a formal series. Every chosen edge touches a left vertex with degree<=2, giving the upper bound 2m; it is sharp for m<n via an alternating path, while m=n has at most 2m−1 edges by acyclicity. Alternating Hamiltonian paths give (m!)² square-case optima. In the rectangular case suppress degree-two left vertices; this bijects optima with labeled right-shore linear forests having m edges and a bijection of m left labels to these edges. Extract from (u+u²/[2(1−u)])^(n−m)/(n−m)! to obtain the displayed binomial sum. An independent direct rook-adjacency/union-find count matched all coefficients in cases (2,2),(2,3),(3,3),(3,4),(4,4), including the 3×3 and 3×4 displayed polynomials. Infinite parameter claims follow from the combinatorial bijection and EGF, not the five finite tests.

## originality

PASS

Barton–Brown–Pike study this precise induced-forest polynomial, but their product formula is for lexicographic graph products, not rook Cartesian clique products. The scalar rook decycling number is known and is excluded from novelty. The two-variable complete coefficient enumeration and labeled top multiplicity were not identified as already published; general bipartite path-forest enumeration is a real equivalence/priority risk.

## value

PASS

The induced-forest polynomial counts feedback-vertex-set complements, a natural graph invariant; resolving every coefficient and all optimal-set multiplicities in the entire rectangular rook family provides strictly more information than the tabulated decycling number. The connection to labeled bipartite path forests also gives a useful combinatorial translation for future exact graph enumerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
