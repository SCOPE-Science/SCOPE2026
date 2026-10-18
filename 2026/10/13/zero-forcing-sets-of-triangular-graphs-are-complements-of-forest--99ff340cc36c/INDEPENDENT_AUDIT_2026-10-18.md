# Independent mathematical audit

## correctness

PASS

For every n>=2, ordinary ZFS on triangular graph J(n,2)=L(K_n) corresponds exactly to initially white K_n edges forming a forest with an isolated complete-graph vertex. If white edges contain a cycle, any blue K_n edge is adjacent to 0 or at least two edges of that cycle, so no cycle edge can ever be first forced; if white subgraph has no isolate and any white edge, each blue K_n edge meets a distinct white edge at both endpoints, so no first force exists. Conversely with isolated label s and a white forest, choose an endpoint u of degree 1 in a nontrivial white component; the blue edge su has exactly one white neighbor uv, forces it, preserves an isolated label and the forest, so inductively clears all. Cayley component count f_j(t) gives the labeled forest recurrence, inclusion-exclusion at least one isolate gives g_n(t)=Σ_{j>=1}(-1)^(j-1) C(n,j) f_(n-j)(t), hence Z(T_n;x)=x^m g_n(x^(-1)); exponential formula yields (1-e^(-u))exp(Σ_k k^(k-2)t^(k-1)u^k/k!). For n>=3 maximizing white edges gives a tree on n-1 labels with one isolate, min Z=m-n+2 and multiplicity n(n-1)^(n-3), with n=2 handled separately. Independently computed direct zero forcing vs DSU forest/isolated criteria for every initial state n=2..6 (33,866 states), checked all coefficients and minimum count. Finite checks only corroborate infinite cycle/isolate proof.

## originality

PASS

The ordinary zero forcing number m-n+2 of J(n,2) is known from Abiad–Simoens–Zeijlemaker, and Cayley labeled tree counts are classical. The full iff characterization of all successful sets as forest complements with isolate and the resulting complete size polynomial/EGF have distinct stronger mathematical content. The 2024 Johnson failed-zero-forcing number paper addresses a different extremal measure; only abstract/metadata, not full text, was accessible and is an explicit priority risk.

## value

PASS

An exact characterization of every successful forcing set on a standard Johnson family produces the full zero-forcing polynomial, minimum-set count and formal generating function from a natural labeled-forest class. A future researcher needing zero-forcing-set distribution or counting can directly use this stronger invariant, independently of the already-known minimum. The forest obstruction and constructive leaf forcing proof supply structural mathematical explanation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
