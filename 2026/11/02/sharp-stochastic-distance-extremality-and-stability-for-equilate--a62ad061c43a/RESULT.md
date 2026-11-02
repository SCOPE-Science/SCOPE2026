# Sharp stochastic distance extremality and stability for equilateral metric trees

## Finding

Fix an integer \(m\ge3\). Give every edge of a finite combinatorial tree \(T\) with \(m\) edges length one, and sample \(X,Y\) independently using normalized arclength on its geometric realization. Write \(D_T=d_T(X,Y)\). Let \(S_m\) be the \(m\)-edge metric star and \(P_m\) the \(m\)-edge metric path. Then the *whole laws*, not only the means, satisfy first-order stochastic ordering

\[
\Pr(D_{S_m}>t)\le \Pr(D_T>t)\le \Pr(D_{P_m}>t)\qquad\text{for every real }t.
\]

Equality in distribution on the left characterizes stars, and equality on the right characterizes paths. More precisely, put

\[
A(T)=\sum_{v\in V(T)}\binom{\deg_T(v)}{2},\qquad
Q(T)=\sum_{g\in E(T)}a_g b_g,
\]

where \(a_g,b_g\) are the numbers of edges in the two components of \(T\setminus\{g\}\); thus \(a_g+b_g=m-1\). For \(0<t<1\), the exact left-tail and its sharp extremal gaps are

\[
\Pr(D_T\le t)=\frac{2t}{m}+\frac{A(T)-m}{m^2}t^2,
\]
\[
\Pr(D_T\le t)-\Pr(D_{P_m}\le t)=\frac{A(T)-(m-1)}{m^2}t^2,
\quad
\Pr(D_{S_m}\le t)-\Pr(D_T\le t)=\frac{\binom m2-A(T)}{m^2}t^2.
\]

The one-Wasserstein gaps between these one-dimensional distance laws are exactly

\[
W_1(D_{S_m},D_T)=\frac{2Q(T)}{m^2},\qquad
W_1(D_T,D_{P_m})=\frac{2}{m^2}\left(\binom m3-Q(T)\right).
\]

Every nonstar tree satisfies the *sharp stability bound*

\[
W_1(D_{S_m},D_T)\ge\frac{2(m-2)}{m^2}.
\]

Equality holds precisely for a star with one of its edges subdivided once (equivalently, a double star with adjacent vertex degrees \(2\) and \(m-1\)); this includes the three-edge path at \(m=3\). In particular,

\[
\mathbb E D_{S_m}=1-\frac{2}{3m},\qquad
\mathbb E D_{P_m}=\frac m3,
\qquad
W_1(D_{S_m},D_{P_m})=\frac{(m-1)(m-2)}{3m}.
\]

## Assumptions and scope

A *tree* here is finite, connected, simple, and acyclic. Its edges are intervals of *equal positive length*, scaled to length one. Sampling is continuous (vertices have measure zero); the probability of selecting a given edge for either sample is \(1/m\). All distances are intrinsic shortest-path distances in the geometric realization, not distances between graph vertices. The number \(m\) is fixed across comparisons. The notation \(W_1\) refers to the usual 1-Wasserstein distance between probability laws on the real line, with ground cost \(|x-y|\), not a transportation metric on the original tree.

An edge \(g\) is *internal* when both its endpoints have degree at least two. For a leaf edge, one of \(a_g,b_g\) vanishes. The one-subdivision extremizer is understood up to graph isomorphism. Nothing is claimed for unequal lengths, cycles, or disconnected networks.

## Proof

**1. Exact edge-pair disintegration.** Let \(e,f\) be distinct edges and define \(\delta_T(e,f)\) as the number of intermediate edges on the unique path linking them; equivalently, the minimum graph distance between one endpoint of \(e\) and one endpoint of \(f\). If \(X\) is uniform on \(e\) and \(Y\) on \(f\), the tree's unique connecting path enters these edges through their uniquely determined nearest endpoints. Therefore

\[
d_T(X,Y)\overset{\mathrm d}=\delta_T(e,f)+U+V,
\]

where \(U,V\) are independent uniform variables on \([0,1]\). If the same edge is selected twice, the conditional distance has law \(|U-V|\). Let

\[
H(t)=\begin{cases}0&t\le0,\\2t-t^2&0<t<1,\\1&t\ge1,\end{cases}\qquad
G(t)=\begin{cases}0&t\le0,\\t^2/2&0<t<1,\\1-(2-t)^2/2&1\le t<2,\\1&t\ge2.\end{cases}
\]

Then \(H\) and \(G\) are respectively the CDFs of \(|U-V|\) and \(U+V\), so the exact continuous distance CDF of *every* such tree is

\[
F_T(t)=\frac1mH(t)+\frac{2}{m^2}\sum_{\{e,f\}\subset E(T)}G\bigl(t-\delta_T(e,f)\bigr).\tag{1}
\]

No discrete sampling approximation enters this identity.

**2. A uniform domination for all edge-separation thresholds.** Define

\[
N_k(T)=\#\{\{e,f\}:e\ne f,\ \delta_T(e,f)\ge k\},\quad k\in\mathbb Z_{\ge0}.
\]

We prove, simultaneously for every tree with \(m\) edges and every \(k\ge0\),

\[
0\le N_k(T)\le\binom{m-k}{2},\tag{2}
\]

where the binomial coefficient on the right is defined to be zero when \(m-k<2\). For the unit-edge path, \(\delta(e_i,e_j)=j-i-1\) for \(i<j\), so (2) is an equality for every \(k\). In a star, every distinct-edge pair has separation zero.

For induction, delete a pendant edge \(e\), obtaining a tree \(T'\) with \(m-1\) edges. The separations between surviving edges do not change. If any surviving edge \(f\) satisfies \(\delta_T(e,f)\ge k\), the path from \(e\) to \(f\) has at least \(k\) intervening edges; these \(k\) distinct surviving edges all have separation \(<k\) from \(e\). Consequently, at most \(m-1-k\) of the \(m-1\) surviving edges can have separation \(\ge k\) from \(e\). (If no such \(f\) exists, the assertion holds trivially.) Hence for \(0\le k\le m-2\)

\[
N_k(T)\le N_k(T')+m-k-1\le\binom{m-k-1}{2}+m-k-1=\binom{m-k}{2}.
\]

For \(k\ge m-1\), no edge pair qualifies. The one-edge base is immediate, completing induction. It follows from (2) that if an unordered pair of distinct edges is sampled uniformly, its nonnegative integer separation is stochastically bounded below by zero and above by its separation in a path. Since \(s\mapsto G(t-s)\) is nonincreasing for each fixed \(t\), (1) yields

\[
F_{P_m}(t)\le F_T(t)\le F_{S_m}(t)\quad\text{for every }t\in\mathbb R,
\]

as claimed. This is a comparison of *entire distributions*.

**3. Exact local tail and uniqueness.** If \(0<t<1\), the only distinct-edge terms in (1) that contribute are those with \(\delta(e,f)=0\), exactly the incident pairs. Two edges of a simple tree are incident at at most one vertex, so the number of unordered incident pairs is \(A(T)\). Inserting \(H(t)=2t-t^2\) and \(G(t)=t^2/2\) gives

\[
F_T(t)=\frac{2t-t^2}{m}+\frac{A(T)}{m^2}t^2.
\]

For every tree, \(A(T)\ge m-1\), with equality iff every vertex has degree at most two, hence iff \(T\) is a path. One proof is the exact identity

\[
A(T)-(m-1)=\sum_{v\in V(T)}\binom{\deg_T(v)-1}{2};
\]

it follows from \(\sum_v(\deg_T(v)-1)=m-1\). Also \(A(T)\le\binom m2\), with equality iff all pairs of edges are incident; for a tree of at least three edges this is equivalent to being a star. Therefore both claimed local gaps are exact and strictly positive for the nonextremal topology. In particular, only a star and only a path can match the corresponding extremal distribution.

**4. Exact Wasserstein distances.** Conditioned on two different edges \(e,f\), the mean of their separation law is \(\delta(e,f)+1\). Conditioned on the same edge it is \(1/3\). Thus

\[
\mathbb E D_T=1-\frac{2}{3m}+\frac2{m^2}\sum_{\{e,f\}}\delta(e,f).\tag{3}
\]

For each edge \(g\), delete \(g\), leaving components containing \(a_g\) and \(b_g\) other edges. The edge \(g\) occurs as an *intermediate edge* on the path between exactly \(a_gb_g\) unordered pairs \(\{e,f\}\). Double counting shows

\[
\sum_{\{e,f\}}\delta(e,f)=\sum_g a_gb_g=Q(T).\tag{4}
\]

For the star \(Q(S_m)=0\); for the path, \(Q(P_m)=\sum_{j=1}^m(j-1)(m-j)=\binom m3\). Substitution into (3) gives the stated exact means. Since step 2 already proves stochastic ordering, the one-dimensional identity \(W_1(\mu,\nu)=|\mathbb E_\mu Z-\mathbb E_\nu Z|\) applies to these ordered distributions and yields the exact formulas. That identity follows directly by integrating the nonnegative CDF difference, or from the monotone quantile coupling.

**5. Sharp stability against the star.** A nonstar tree has at least one internal edge \(g\). For that edge, \(a_g,b_g\) are positive integers with sum \(m-1\), so \(a_gb_g\ge m-2\), with equality only when \(\{a_g,b_g\}=\{1,m-2\}\). Since all other products are nonnegative, \(Q(T)\ge m-2\). Equality forces exactly one internal edge (any second one would add a positive contribution). A tree having exactly one internal edge must consist of two adjacent nonleaf vertices, all other vertices leaves; the component-size equality forces the vertices' degrees to be \(2\) and \(m-1\). Conversely, the star obtained by subdividing one edge once has precisely this structure and \(Q=m-2\). Combining with step 4 proves the optimal W1 gap and all equality cases. \(\square\)

## Verification

`CHECK.py` is a standalone, standard-library Python checker. Run `python CHECK.py` in the directory containing that file. It constructs all labeled trees on two through seven vertices by Prüfer codes (18,248 trees before the additional witnesses), computes exact edge separations, exact rational CDFs on a grid, the small-threshold formulas, cut contributions, and the proposed Wasserstein identities. It independently cross-checks point-to-point geodesics through endpoint routing on rational coordinate grids and tests the sharp nonstar family through seventeen edges. It prints the number of tested trees and raises on any failed assertion. The finite tests validate the algebra and indexing conventions but do not serve as proofs for all sizes or real thresholds; the universal proof is above.

## Relationship to prior work

The continuous *mean*-distance star/path inequality for uniform metric trees is Proposition 4.4 of Garijo, Márquez and Silveira, *Continuous Mean Distance of a Weighted Graph* (arXiv:2103.11676; Results in Mathematics, 2023). Baptista, Kennedy and Mugnolo, *Mean Distance on Metric Graphs* (2024), establish mean-distance extremal principles for metric graphs. These results are credited, not claimed here. The present statement orders every threshold probability and every increasing cost functional; in particular, the claimed distribution order does not follow merely from ordering means. The proof also provides exact local branching signatures and a sharp nonstar transport gap.

Tratnik and Žigert Pleteršek (arXiv:1609.04182) relate vertex and edge Hosoya polynomials of trees. Zmazek and Žerovnik (2007) study weighted-tree Hosoya-Wiener polynomials. These are relevant combinatorial edge-distance encodings; their available statements are not the continuous sampled-point stochastic order or the W1 stability theorem. Dahl (2007) studies root-to-vertex majorization rather than independent arclength samples. Jelen (2002) studies distance-related dominance and Wiener measures for discrete trees; the inspected dissertation does not state the present continuous arclength theorem. The full text of Doyle and Graver's 1982 *Mean Distance for Shapes* could not be obtained; historical priority remains an uncertainty.

## Limitations

All extremal assertions require identical total *numbers of unit edges* and therefore identical total arclength. They do not extend automatically to weighted trees or to graphs with cycles. Stochastic ordering does not imply variance ordering, which is not claimed. Neither the literature searches nor the finite checker can establish absolute priority; the inaccessible older literature is a residual risk. No result from the literature on mean distances is presented as new.

## References

1. B. Zmazek and J. Žerovnik, *The Hosoya-Wiener Polynomial of Weighted Trees*, Croatica Chemica Acta 80 (2007), 75–80; public record dated 2007-03-11, https://hrcak.srce.hr/12827.
2. G. Dahl, *Majorization and distances in trees*, Networks 50 (2007), 251–257, DOI 10.1002/net.20202; first published 2007-09-04.
3. N. Tratnik and P. Žigert Pleteršek, *Relationship Between the Hosoya Polynomial and the Edge-Hosoya Polynomial of Trees*, arXiv:1609.04182; first submitted 2016-09-14.
4. P. Garijo, A. Márquez and A. Silveira, *Continuous Mean Distance of a Weighted Graph*, arXiv:2103.11676, Results in Mathematics (2023), DOI 10.1007/s00025-023-01902-w.
5. L. N. Baptista, J. B. Kennedy and D. Mugnolo, *Mean Distance on Metric Graphs*, J. Geom. Anal. 34 (2024), 137, DOI 10.1007/s12220-024-01574-0.
6. F. Jelen, *Superdominance Order and Distance of Trees*, RWTH Aachen dissertation (2002), https://publications.rwth-aachen.de/record/52768.
7. J. K. Doyle and J. E. Graver, *Mean Distance for Shapes*, J. Graph Theory 6 (1982), DOI 10.1002/jgt.3190060410. Full text not accessible for this comparison.
