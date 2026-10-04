# General position polynomials of spiders and the smallest nonunimodal spider
## Finding
Let \(T=S(\ell_1,\ldots,\ell_k)\) be a spider tree with \(k\ge3\) arms, positive arm lengths \(\ell_i\), \(L=\sum_i\ell_i\), and order \(n=L+1\). A vertex set of size at least three is in general position if and only if it avoids the center and contains at most one vertex from each arm. Hence, writing \(e_j\) for the elementary symmetric polynomial in \(\ell_1,\ldots,\ell_k\), its general position polynomial is \[\psi(T;x)=1+n x+\binom{n}{2}x^2+\sum_{j=3}^k e_j(\ell_1,\ldots,\ell_k)x^j.\] Among all spiders of order at most \(22\), every one of order at most \(21\) has a unimodal general position polynomial, while at order \(22\) there is exactly one nonunimodal isomorphism type, namely \(S(1,1,1,1,2,15)\), with coefficient sequence \((1,22,231,226,249,137,30)\). Moreover, for the infinite family \(S_m=S(1,1,1,1,2,m)\), \(\psi(S_m;x)\) is nonunimodal if and only if \(m\ge15\).

## Assumptions and scope
A spider tree \(S(\ell_1,\ldots,\ell_k)\) is a tree with one center \(c\) of degree \(k\ge3\), whose deletion leaves \(k\) paths; \(\ell_i\ge1\) is the number of edges on arm \(i\). A general position set is a vertex set containing no three vertices on a common geodesic. The general position polynomial \(\psi(T;x)\) counts general position sets by cardinality.

## Proof
Let \(A\) be a general position set with \(|A|\ge3\). If \(c\in A\), then two further selected vertices either lie on different arms, in which case \(c\) lies on their unique geodesic, or lie on one arm, in which case the nearer selected arm vertex lies on the geodesic from \(c\) to the farther one. Thus \(c\notin A\).

If two selected vertices lie on one arm and a third selected vertex lies anywhere else, then the selected vertex nearer the center lies on the unique geodesic joining the farther selected arm vertex to the third vertex. Three selected vertices on one arm also violate general position. Hence a general position set of size at least three contains at most one vertex from each arm. Conversely, if the center is absent and at most one vertex is selected from each arm, then a geodesic between two selected vertices uses only their two arms and the center, so it cannot contain a third selected vertex. This proves the structural characterization.

Every set of size zero, one, or two is automatically in general position. For \(j\ge3\), choose \(j\) distinct arms and then one of the \(\ell_i\) vertices on each chosen arm. Therefore the degree-\(j\) coefficient is \(e_j(\ell_1,\ldots,\ell_k)\), while the first three coefficients are \(1\), \(n\), and \(\binom n2\). Equivalently,
\[
\psi(T;x)=\prod_{i=1}^k(1+\ell_i x)+x+\left(L+\sum_{i=1}^k\binom{\ell_i}{2}\right)x^2.
\]

For the one-parameter family \(S_m=S(1,1,1,1,2,m)\), direct expansion gives
\[
\psi(S_m;x)=1+(m+7)x+\binom{m+7}{2}x^2+(14m+16)x^3+(16m+9)x^4+(9m+2)x^5+2m x^6.
\]
The tail satisfies \(16m+9>14m+16\) exactly when \(m\ge4\). Also
\[
\binom{m+7}{2}-(14m+16)=\frac{m^2-15m+10}2,
\]
which is positive for every integer \(m\ge15\) and negative for \(1\le m\le14\). For \(m\le3\) the coefficients increase through degree three and then decrease; for \(4\le m\le14\) they increase through degree four and then decrease. Hence this family is nonunimodal exactly for \(m\ge15\).

For the minimum-order statement, a spider isomorphism type is determined by the multiset of its positive arm lengths. The included exact enumeration lists every integer partition of \(n-1\) into at least three positive parts for each \(4\le n\le22\), computes the coefficients from the proved formula, and tests unimodality. It checks all \(3374\) spider types through order \(22\): none of the \(2593\) types through order \(21\) is nonunimodal, and among the \(781\) order-\(22\) types the unique failure is \(S(1,1,1,1,2,15)\), whose coefficients are \(1,22,231,226,249,137,30\).

## Verification
The included `verify.py` performs two independent checks. First, for all \(103\) spider isomorphism types of orders four through eleven, it constructs the tree, computes all graph distances, tests every one of \(112080\) vertex subsets directly against the no-three-on-a-geodesic definition, and matches the resulting size counts against the formula. Second, it exhaustively enumerates all \(3374\) spider types through order twenty-two and verifies the stated unique cutoff. The separate `cutoff_certificate.json` records the number of spider types and nonunimodal types at every order from four through twenty-two.

## Relationship to prior work
Iršič, Klavžar, Rus, and Tuite introduced the general position polynomial in 2024 and explicitly asked for structural information about unimodality. Their paper gives two special three-arm trees with equal general position polynomials and derives the polynomial of broom graphs, which are the special spiders having one long arm and all other arms of length one. Their smallest nonunimodal broom is \(B_{17,6}\), of order \(24\). The theorem here treats arbitrary spider arm lengths and identifies a unique nonunimodal spider already at order \(22\).

A 2026 follow-up studies complete multipartite graphs, brooms, combs, and coronas in greater detail. Its full text contains no spider or subdivided-star treatment beyond the broom family, and it retains \(B_{17,6}\) as the displayed broom counterexample. Targeted searches using the aliases “spider,” “starlike tree,” and “subdivided star” did not locate the all-spider formula or the order-\(22\) cutoff.

## Limitations
The exact minimum-order statement is within the class of spider trees, not within all trees. The cutoff through order twenty-two is a finite exhaustive classification over integer partitions and depends on the proved all-spider formula; the direct graph-level exhaustive check is independently carried out only through order eleven. Search coverage cannot exclude differently phrased or non-indexed prior work.

## References
1. V. Iršič, S. Klavžar, G. Rus, J. Tuite, “General Position Polynomials,” arXiv:2401.05696v1, submitted 11 January 2024; Results in Mathematics 79 (2024), Article 110, DOI 10.1007/s00025-024-02133-3.
2. B. A. Rather, “Explicit Formulas and Unimodality Phenomena for General Position Polynomials,” arXiv:2603.06930v1 (2026).
