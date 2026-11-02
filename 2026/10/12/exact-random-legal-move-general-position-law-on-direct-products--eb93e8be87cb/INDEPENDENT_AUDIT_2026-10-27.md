# Independent mathematical audit

## correctness

PASS

For m,n>=3, K_m x K_n is connected of diameter 2: any distinct same-row or same-column cells have a common neighbor because the other coordinate has at least 3 options. A GP violation is exactly an induced 3-vertex path, equivalently the chosen induced graph being not a disjoint union of cliques. Fix first cell. The second is same row (n-1 choices), same column (m-1), or adjacent diagonal ((m-1)(n-1)), out of mn-1 uniformly legal options. From a same-row pair, third-legal cells comprise n-2 remaining row cells and 2(m-1) crossed-column cells; analogously m-2+2(n-1) for same-column pair. From adjacent diagonal pair, third legal cells are (m-2)(n-2) pairwise new row/column cells giving a 3-clique and two crossed corners giving a rectangle. The row/column third-case forces all later choices within that row/column; 3-clique forces only unused-row and unused-column completions to a size-k rook clique; crossed 3-corners force the fourth corner and terminate. Thus probabilities p_R=(n-1)/(mn-1)*(n-2)/(n+2m-4), p_C=(m-1)/(mn-1)*(m-2)/(m+2n-4), p_M=(m-1)(n-1)/(mn-1)*(m-2)(n-2)/((m-2)(n-2)+2), p_Q=1-others. The row-column relabeling group acts transitively within each labeled terminal type; hence within-type uniformity and binomial labeled counts. Terminal PGF uses sizes (n,m,min(m,n),4), even if exponents collide, and q=3 is correctly included. For m=n=q>=4, p_Q=4(q-1)/((q+1)(3q-4))+2(q-1)/((q+1)((q-2)^2+2)), hence q*p_Q ->4/3, (q-4)*p_Q ->4/3 and (q-4)^2*p_Q(1-p_Q)/q ->4/3. At fixed m and n to infinity, p_R->1/m, p_M->(m-1)/m, and p_C,p_Q->0, giving normalized Bernoulli(1/m). Independent exact rational recursion using induced 2-edge-path tests (not the package distance verifier) computed all reachable states for 3x3 (103), 3x4 (212), 4x4 (477), 4x5 (960), 5x5 (2306) with exact agreement, and symbolic algebra checked square formula and all three limits. Those finite checks corroborate, not prove, the unrestricted statement.

## originality

PASS

Best-of-knowledge: The same-graph complete feasible-set classification and polynomial are known (Rather Theorem 5.3), as are scalar extreme cardinalities and adversarial playable-vertex rules. However the stated transition kernel chooses uniformly among currently addable GP vertices; none of the inspected prior statements yields the exact type absorption probabilities, terminal-size PGF, or contrasting balanced/asymmetric random-process limits without an additional history-sensitive argument. Multiple targeted primary and published-record searches revealed no exact stochastic coverage, but negative search is not proof of priority.

## value

PASS

A uniform random legal-move analogue of the established general-position achievement game is a natural random saturation process. For every K_m x K_n with m,n>=3, the exact terminal-type probabilities identify an infinite-family output distribution not determined by the static maximal-set inventory, and reveal a non-obvious asymptotic contrast: on qxq boards P(short terminal rectangle)~4/(3q) yet mean size loss tends to 4/3 and variance grows ~4q/3; at fixed width the normalized size tends to a nondegenerate Bernoulli(1/m). The exact finite-board probability generating function supplies all moments and per-labeled-terminal-set probabilities. This is motivated stochastic-combinatorial structural information rather than a table recomputation or unmotivated tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
