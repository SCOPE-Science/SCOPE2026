# Four-agent breakdown of core–periphery structure under arbitrarily small Katz link-cost heterogeneity

## Finding

Consider unilateral sponsorship of undirected network links, with player-specific linear link costs and Katz walk centrality. **The four-vertex graph comprising a triangle and an isolated vertex is a strict pure Nash-equilibrium graph for an open set of positive player costs, however close to homogeneous costs one wishes in relative terms.** Four vertices are minimal: no graph outside the core–periphery family can occur at Nash equilibrium with at most three players, whatever their positive costs. For the particular triangle-plus-isolate graph, the *exact minimum supporting ratio of largest to smallest link cost* is

\[
R(q)=\frac{(1-2q)(1-2q^2)}{1-3q}=1+q+O(q^2),\qquad 0<q<\frac13.
\]

Thus no fixed positive percentage of cost heterogeneity protects the homogeneous-cost core–periphery characterization uniformly as attenuation tends to zero. The displayed graph is **not** claimed to be a new graph-theoretic construction: it appears under a different, nonlinear payoff function in Example 1 of the motivating paper. The result concerns its exact support in the *Katz* game with nearly identical **player-specific** link costs.

## Assumptions and scope

Let \(N=\{1,\ldots,n\}\), with \(n\ge2\). Each player \(i\) chooses \(s_i\subseteq N\setminus\{i\}\) and pays \(c_i|s_i|\), where \(c_i>0\). An undirected edge \(\{i,j\}\) exists when either endpoint sponsors it. Write \(A(s)\) for the induced symmetric zero-diagonal adjacency matrix. For a common attenuation \(0<q<1/(n-1)\), define

\[
b_i(s)=\left[(I-qA(s))^{-1}{\bf1}\right]_i-1
       =\sum_{k\ge1}q^k\left[A(s)^k{\bf1}\right]_i,
\quad u_i(s)=b_i(s)-c_i|s_i|.
\]

A pure Nash equilibrium has no profitable unilateral replacement of any whole sponsorship set. A *strict* equilibrium makes every different strategy strictly worse. A graph is *core–periphery* here precisely if some \(C\subseteq N\) satisfies \(\{i,j\}\in E\) exactly when at least one of \(i,j\) lies in \(C\). In particular, a triangle plus an isolate is not core–periphery.

For \(n=4\), fix the cyclic sponsorship profile

\[
s_1=\{2\},\quad s_2=\{3\},\quad s_3=\{1\},\quad s_4=\varnothing.
\]

Write \(a=c_1=c_2=c_3\), \(b=c_4\) and define

\[
\ell(q)=\frac{q(1-q)^2}{(1-2q)(1-q-3q^2+q^3)},\qquad
U(q)=\frac{q}{(1-2q)(1-2q^2)},\qquad
V(q)=\frac{q}{1-3q}.
\]

For every \(0<q<1/3\), this profile is a Nash equilibrium **if and only if**

\[\ell(q)\le a\le U(q),\qquad b\ge V(q).\]

It is strict **if and only if** all three inequalities are strict. These strict inequalities also permit sufficiently small independent perturbations of the three triangle players' costs, yielding an open set of four-dimensional cost vectors.

## Proof

**1. Exact Katz comparisons.** A vertex of the triangle has gross centrality

\[B(q)=\frac{2q}{1-2q}.\]

If a triangle player deletes the one edge she sponsors, she becomes a leaf of a three-vertex path, with gross centrality

\[L(q)=\frac{q(1+2q)}{1-2q^2}.\]

Thus retaining the edge is optimal against its deletion precisely if \(a\le B-L=U\). If the player keeps her sponsored edge and adds a link to the isolate, she becomes the degree-three vertex of a triangle with one pendant; solving the four resolvent equations gives

\[P(q)=\frac{q(3+2q-q^2)}{1-q-3q^2+q^3}.\]

Consequently she does not profit from this addition precisely if \(a\ge P-B=\ell\). The remaining nonredundant switch deletes her sponsored triangle link and adds the pendant link. It produces a four-vertex path, in which her degree is two. Every vertex of that path starts at most \(2^k\) walks of length \(k\), while every triangle vertex starts exactly \(2^k\); at length two the inequality is strict. Because every Katz weight is positive, the switched graph gives her strictly less benefit than the original triangle at the *same cost*. A player never benefits from additionally sponsoring an edge already sponsored by its other endpoint. These possibilities exhaust her deviations.

**2. The isolated player's deviations.** If player \(4\) sponsors a subset \(T\subseteq\{1,2,3\}\), her gross centrality \(F(T)\) is a nonnegative weighted sum over walks, each term occurring exactly if all edges incident to \(4\) used by that walk belong to \(T\). Each such indicator is a supermodular set function. Hence \(F\) is supermodular and, by symmetry among the three triangle vertices, its values \(F_t\) for \(|T|=t\) are discretely convex. Since \(F_0=0\), the ratios \(F_t/t\) increase with \(t=1,2,3\), strictly so because walks using two distinct isolate-to-triangle edges have positive weights. With three new links the graph is \(K_4\), so

\[F_3=\frac{3q}{1-3q}.\]

Therefore no deviation by player \(4\) is profitable precisely if \(b\ge F_3/3=V\), and all nonempty deviations are strictly worse precisely if \(b>V\). Combining with Step 1 proves the necessary and sufficient thresholds, including strictness.

**3. A nonempty open strict-equilibrium region and near-homogeneity.** Elementary rational simplification yields

\[
U(q)-\ell(q)=\frac{q^2\bigl((1-3q)(1+q)+2q^3\bigr)}{(1-2q)(1-2q^2)(1-q-3q^2+q^3)}>0
\]

and

\[
V(q)-U(q)=\frac{q^2(1-2q+4q^2)}{(1-3q)(1-2q)(1-2q^2)}>0.
\]

All denominators are positive for \(0<q<1/3\). For example, choose \(a=(\ell+U)/2\), \(b=V+q^3\). Then the profile is strict, and the cost ratio \(b/a\) tends to \(1\) as \(q\downarrow0\), because \(\ell,U,V=q+O(q^2)\). The strict comparison margins persist under sufficiently small independent changes to the four costs.

**4. Exact least cost dispersion supporting this graph.** Let any Nash-equilibrium sponsorship profile yield \(K_3\sqcup K_1\). Duplicate sponsorship of the same triangle edge is impossible because its removal would save a positive cost without changing benefits. Hence each triangle edge has exactly one sponsor. At least one triangle vertex sponsors one or two edges. A vertex sponsoring one edge must have \(c_i\le U\), by deleting that edge. A vertex sponsoring both incident edges must have \(2c_i\le B\), by deleting both, and \(B/2=q/(1-2q)<U\). The isolate must have \(c_4\ge V\), since sponsoring all three links would make the complete graph and give gross benefit \(3V\). As \(V>U\), every supporting vector satisfies

\[
\frac{\max_i c_i}{\min_i c_i}\ge\frac{V}{U}
=\frac{(1-2q)(1-2q^2)}{1-3q}.
\]

The cyclic profile attains equality with \(c_1=c_2=c_3=U\) and \(c_4=V\). The infimum among *strict* supporting equilibria equals the same ratio, approached from above.

**5. Four players are necessary.** Every graph on at most two vertices is core–periphery. On three vertices the only graph that is not core–periphery is \(K_2\sqcup K_1\). At equilibrium its edge cannot be doubly sponsored, so some endpoint \(i\) alone sponsors the edge. Let \(B_2=q/(1-q)\) be its original gross benefit. Deleting the edge implies \(c_i\le B_2\). If this endpoint also sponsors an edge to the isolate, she becomes the center of a three-vertex path, with gross benefit \(C_3=2q(1+q)/(1-2q^2)\). But

\[
C_3-2B_2=\frac{2q^3}{(1-q)(1-2q^2)}>0,
\]

so the new link produces an incremental benefit \(C_3-B_2>B_2\ge c_i\), a profitable deviation. Here \(0<q<1/2\) suffices. This excludes the only possible smaller obstruction, with arbitrary positive player-specific costs.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. Its exact-rational Gaussian elimination recomputes Katz values from the defining resolvent, independently enumerates every unilateral strategy for both an interior strict profile and a boundary weak profile, and checks the displayed rational identities at seven attenuation values in \((0,1/3)\). It also checks all eight orientations of triangle sponsorship for necessary cost bounds and independently checks the three-agent centrality inequality. The 392 strict/weak unilateral comparisons and other exact calculations pass. These finite checks corroborate the **symbolic proof above**; they are not a substitute for its universal quantifiers.

## Relationship to prior work

Arieli, Correia-da-Silva, Hann-Caruthers and Rubinchik (2026), Theorem 1, prove the core–periphery property for the same undirected unilateral-link, walk-centrality model with a **common** linear cost. Their Section 7 characterizes which core sizes are supportable for that common cost. The present result changes exactly one assumption—allowing costs to depend on the sponsoring player—and proves exact support thresholds, a sharp four-agent boundary and a vanishing relative cost gap. Importantly, their Example 1 **already** exhibits the same triangle-plus-isolate graph under a *different non-Katz*, degree-neighbor nonlinear benefit with common costs; that example does not imply its Katz support or the quantitative player-cost threshold established here.

Balaji, Wankhede and Tallapragada (2026) study Katz maximization with weighted, generally directed budget-constrained outgoing connections, not the present undirected OR-sponsorship game with per-edge linear payment. Charoensook (2022) studies partner-dependent information and cost with shortest-path decay, not Katz walk counts and an exact near-homogeneous cost ratio. Tatko and Griffin (2012) consider Katz-related centrality and link cost under a bilateral pairwise-stability protocol, again distinct from unilateral Nash stability. These are substantive related frameworks, but their stated results do not settle the displayed four-player Katz cost interval.

## Limitations

The result does not classify all four-player equilibrium graph architectures under arbitrary heterogeneous costs. The exact ratio is specific to supporting \(K_3\sqcup K_1\), and small heterogeneity is achieved as the attenuation parameter approaches zero; it is **not** claimed for every fixed positive attenuation. The construction uses unweighted undirected edges created unilaterally, symmetric Katz attenuation, and player-dependent rather than edge-dependent costs. Mathematical priority remains subject to literature not indexed or inspected; no independent validation is claimed.

## References

1. I. Arieli, J. Correia-da-Silva, W. Hann-Caruthers and A. Rubinchik, *Strategic Centrality and the Emergence of Core-Periphery Networks*, arXiv:2609.02357 (first public September 2, 2026). https://arxiv.org/abs/2609.02357
2. Balaji R, P. Wankhede and P. Tallapragada, *A Network Formation Game for Katz Centrality Maximization: A Resource Allocation Perspective*, arXiv:2604.03056 (2026). https://arxiv.org/abs/2604.03056
3. B. Charoensook, *A Note on Partner Heterogeneity and Strict Nash Networks*, Theoretical Economics Letters 12 (2022), 1207–1220, DOI:10.4236/tel.2022.124064. https://www.scirp.org/journal/paperinformation?paperid=119571
4. R. Tatko and C. Griffin, *Game Theoretic Formation of a Centrality Based Network*, arXiv:1209.4022 (2012). https://arxiv.org/abs/1209.4022
