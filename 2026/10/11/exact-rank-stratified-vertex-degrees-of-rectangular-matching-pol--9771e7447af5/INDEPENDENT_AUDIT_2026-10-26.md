# Independent mathematical audit

## correctness

PASS

For every integer a,b>=1 and rank 0<=k<=min(a,b), full-dimensional bipartite matching-polytope vertices are precisely partial permutation matrices. The established edge criterion equates neighbors to exactly one connected alternating path/cycle. With p=a-k,q=b-k, mutually exclusive classes contribute alpha_k (matched-matched paths), pq(1+alpha_k) (unmatched-unmatched), (p+q)alpha_k (one unmatched end), and beta_k=sum_{t>=2}binom(k,t)(t-1)! (alternating cycles; directed cyclic order matters). This yields pq+(p+1)(q+1)alpha_k+beta_k, all rank multiplicities, and the handshake count. The recurrence alpha_(k+1)=(k+1)(alpha_k+1) gives the stated exact degree increment; k=0, k=1, k>=2 and the only potentially negative coefficient p=q=1,k=2 were checked symbolically. It is positive for min(a,b)>=2 except the tie (2,2) at ranks 1/2, while min(a,b)=1 is a simplex of constant degree. An INDEPENDENT edge test based on ranks of common tight coordinate/row/column facet equations, not the path/cycle criterion, exhaustively matched degrees and multiplicities for a,b=(1,4),(2,2),(2,3),(2,4),(3,3),(3,4), altogether 153 actual matching vertices. Exact integer strictness/equality checks covered 1275 pairs with 1<=a<=b<=50. These are supporting finite checks, not the proof of all parameters.

## originality

PASS

Best-of-knowledge PASS for the complete bivariate rank-stratified local-degree numbers and sharp strictness/tie classification, not for established matching adjacency or general weak monotonicity. The exact theorem for all graphs of Abreu et al. expresses d(M) as a graph-dependent count of admissible paths and cycles, but the inspected full primary text does not evaluate the complete-bipartite rank profile or prove its global strictness and unique exceptions. The all-parameter four-class ordered-path/cycle enumeration and rank-difference case proof are additional mathematics. Heuer-Striker identifies exactly the rectangular polytope and cites older enumerations of rook-polytope edges/faces; that source and the inaccessible Cao-Chen square faces article leave material historical priority risk, but abstracts/citations alone do not establish coverage. No priority certification.

## value

PASS

The complete-bipartite matching/rectangular doubly-substochastic polytope is a canonical full-dimensional 0/1 polytope. Its complete one-skeleton local-degree multiset is a natural invariant. This all-parameter factorial rank classification gives every vertex degree and multiplicity, exact edge count without explicit exponential skeleton enumeration, rank-strictness, and the unique 2x2 tie. These are mathematical structural facts beyond an arbitrary small instance; the prior general path/cycle adjacency and weak inclusion monotonicity are acknowledged. The unknown exact closed bivariate rank profile and its sharp equality cases make a plausible independently reusable invariant, without needing a broader new theorem or paper-sized downstream application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
