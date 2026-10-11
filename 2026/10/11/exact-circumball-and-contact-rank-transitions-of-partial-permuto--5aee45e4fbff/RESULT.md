# Exact circumball and contact-rank transitions of partial permutohedra

## Finding
For every pair of integers \(m,n\ge1\), the unique smallest enclosing Euclidean ball of the partial permutohedron
\[
\mathcal P(m,n)=\operatorname{conv}\left\{x\in\{0,1,\ldots,n\}^{m}:\text{all nonzero entries of }x\text{ are distinct}\right\}
\]
can be determined with at most \(\min(m,n)+1\) rational candidate evaluations. The result gives its center, squared radius, and *all* touching vertices, including exact changes in their nonzero-coordinate ranks.

Set \(K=\min(m,n)\), and for integers \(0\le k\le K\) define
\[
S_k=\sum_{j=0}^{k-1}(n-j)=\frac{k(2n-k+1)}2,\qquad
Q_k=\sum_{j=0}^{k-1}(n-j)^2,\qquad S_0=Q_0=0.
\]
Define closed intervals
\[
I_0=[n/2,\infty),\quad
I_k=[(n-k)/2,(n-k+1)/2]\ (1\le k<K),\quad
I_K=[0,(n-K+1)/2].
\]
(The first and last intervals meet at \(n/2\) when \(K=1\).) Let \(t_k\) be the Euclidean projection of the rational number \(S_k/m\) onto \(I_k\), and put
\[
H_k=mt_k^2+Q_k-2t_kS_k.
\]
Then \(H_* = \min_{0\le k\le K}H_k\) is the **exact squared enclosing radius**. Every index attaining this minimum has the same \(t_k\), denoted \(t_*\). The **unique** smallest enclosing ball has center
\[
\boxed{c_*=t_*\mathbf1_m,\qquad R_*^2=H_*.}
\]
All quantities are rational except for the optional square root in \(R_*\). No numerical optimization or vertex enumeration is needed.

For \(0\le k\le K\), let \(\mathcal O_k\) consist of all coordinate permutations of \((n,n-1,\ldots,n-k+1,0,\ldots,0)\). The **complete set of sphere-contacting vertices** is
\[
\boxed{\bigcup_{\substack{0\le k\le K\\ mt_*^2+Q_k-2t_*S_k=R_*^2}}\mathcal O_k.}
\]
There is either exactly one contact-rank orbit or exactly two consecutive contact-rank orbits. Orbit \(k\) has cardinality \(m!/(m-k)!\).

Two sharp boundary regimes follow. If \(m\le2\), then
\[
t_*=n/2,\qquad R_*^2=mn^2/4,
\]
with contact ranks \(0\) and \(1\). Define \(S=n(n+1)/2\) and \(Q=n(n+1)(2n+1)/6\). If \(m\ge n(n+1)\), then
\[
\boxed{t_*=S/m,\qquad R_*^2=Q-S^2/m.}
\]
At equality \(m=n(n+1)\), contact ranks are \(n-1,n\); strictly above it, **only rank \(n\)** contacts occur. The inequality \(m>n(n+1)\) is necessary and sufficient for this full-rank-only contact phenomenon.

For fixed \(m\), the rescaled center and radius have the cubical limit
\[
\lim_{n\to\infty}\frac{t_*}{n}=\frac12,\qquad
\lim_{n\to\infty}\frac{R_*}{n}=\frac{\sqrt m}{2}.
\]
For fixed \(n\), the large-\(m\) radius satisfies \(R_*^2=Q-S^2/m\) exactly once \(m\ge n(n+1)\).

## Assumptions and scope
Both parameters \(m,n\) are arbitrary positive integers. Distances, radii and projections use the standard Euclidean inner product on the **full ambient** space \(\mathbb R^m\). A touching vertex means a vertex on the boundary of the unique smallest enclosing ball; no facets are claimed to be tangent to that ball. The formulas concern the specified consecutive positive labels, not arbitrary nonconsecutive label sets or an affine-equivalent realization under a nonorthogonal map.

## Proof
**1. Exact vertex structure.** The vertices of \(\mathcal P(m,n)\) are precisely the sets \(\mathcal O_k\) for \(0\le k\le K\). This follows from the partial-permutohedron vertex theorem of Heuer--Striker and is restated as Proposition 2.7 of Behrend et al. Within any \(\mathcal O_k\), the coordinate sum and squared norm are respectively \(S_k\) and \(Q_k\).

**2. Symmetry and uniqueness of the center.** For arbitrary \(c\in\mathbb R^m\), the squared covering-radius objective is
\[
F(c)=\max_{v\in\operatorname{vert}(\mathcal P(m,n))}\|v-c\|_2^2
=\|c\|_2^2+\max_v\bigl(\|v\|_2^2-2\langle v,c\rangle\bigr).
\]
The second term is convex and the first strictly convex, so \(F\) has a unique global minimizer. Permutation of coordinates preserves the vertex set and \(F\). Uniqueness forces the minimizer to be fixed by every permutation, hence \(c=t\mathbf1_m\). Its scalar parameter is nonnegative: at negative \(t\), each \(Q_k-2tS_k\) is nonincreasing in \(t\), while \(mt^2\) also decreases as \(t\) increases toward zero. In fact the optimizer is positive because the right derivative of the objective at zero is negative.

**3. One-dimensional exact reduction.** At \(c=t\mathbf1_m\), every vertex of rank \(k\) has the same squared distance
\[
f_k(t)=mt^2+Q_k-2tS_k.
\]
Thus \(F(t\mathbf1_m)=\max_{0\le k\le K}f_k(t)\). The adjacent differences factor as
\[
f_{k+1}(t)-f_k(t)=(n-k)(n-k-2t).
\]
For \(t\ge0\), these signs show that rank \(k\) maximizes the distance precisely on the interval \(I_k\), with ties at common endpoints. Consequently the intervals partition \([0,\infty)\) up to endpoints, and on \(I_k\) the objective is the single quadratic \(f_k(t)\). Its minimum on \(I_k\) occurs at the projection \(t_k\) of its stationary point \(S_k/m\). Minimizing the finitely many exact values \(H_k=f_k(t_k)\) proves the announced formula. Strict convexity shows that all winning interval candidates coincide in their center \(t_*\).

**4. Complete contact set and constructive global certificate.** The adjacent-difference signs permit only one maximal rank or a tie of two consecutive ranks. If a single rank \(k\) contacts, stationarity gives \(mt_*=S_k\). If ranks \(k,k+1\) contact, the subgradient condition at their common boundary gives
\[
S_k\le mt_*\le S_{k+1}.
\]
Because the mean of the vertices in \(\mathcal O_k\) is \((S_k/m)\mathbf1_m\), in the two-orbit case mix the uniform measures on \(\mathcal O_k\) and \(\mathcal O_{k+1}\) with weight
\[
\theta=\frac{mt_*-S_k}{n-k}\in[0,1]
\]
on the second orbit. The resulting distribution is supported exclusively on touching vertices and has mean exactly \(c_*\). In either case, for any center \(y\in\mathbb R^m\), averaging squared distances under this distribution gives the *exact identity*
\[
\mathbb E\|V-y\|_2^2=R_*^2+\|y-c_*\|_2^2.
\]
Thus \(\max_{v\in\mathcal P(m,n)}\|v-y\|_2^2\ge R_*^2+\|y-c_*\|_2^2\), proving global optimality, uniqueness, and the precise contact classification without imposing symmetry on competing balls.

**5. Sharp transitions.** At \(t=n/2\), only ranks \(0,1\) are farthest, with values \(S_0=0,S_1=n\). Their subgradient balance is equivalent to \(mn/2\le n\), namely \(m\le2\). For \(m\ge n\), all \(n\) positive labels are at maximum distance and strictly preferred to omitting any label exactly when \(t<1/2\). A one-orbit center then satisfies \(mt=S\); hence \(t<1/2\) exactly when \(m>2S=n(n+1)\). Equality makes label \(1\) neutral and yields precisely ranks \(n-1,n\). Substitution yields \(Q-S^2/m\). This also proves necessity of the full-rank-only threshold.

**6. Cubical limit.** For fixed \(m\), \(n^{-1}\mathcal P(m,n)\) lies in \([0,1]^m\). Conversely, for every cube vertex \(\mathbf1_A\), assign \(|A|\) distinct labels among \(n-|A|+1,\ldots,n\) to its occupied coordinates. The resulting point of \(n^{-1}\mathcal P(m,n)\) tends to \(\mathbf1_A\) uniformly over the finitely many subsets \(A\). Hence these polytopes converge in Hausdorff distance to \([0,1]^m\). Uniqueness and continuity of the Euclidean smallest enclosing ball under Hausdorff convergence give the stated limits, since the cube's center and radius are \(\mathbf1_m/2\) and \(\sqrt m/2\).

## Verification
A standalone Python 3 checker using only the standard library and exact fractions reproduces the candidate search and verifies its convex-center condition. It tests all \(3{,}600\) parameter pairs with \(1\le m,n\le60\), exhaustively checks the stated complete vertex-contact pattern for all \(m\le5,n\le6\), and checks the sharp large-dimension formulas, with \(1{,}352\) individual vertices examined in the exhaustive subcases. It also tests rational cubical-limit error bounds for sixteen larger-label cases. Run `python3 verify.py`. The finite tests are independent corroboration of, not a substitute for, the general proof above.

For example, \((m,n)=(5,10)\) gives \(t_*=4\), \(R_*^2=109\) and contacting ranks \(2,3\), giving \(5!/3!+5!/2!=80\) contacting vertices. For \((m,n)=(10,2)\), the formulas give \(t_*=3/10\), \(R_*^2=41/10\), with only rank \(2\) contacting.

## Relationship to prior work
Heuer and Striker (arXiv:2012.09901, Section 5.1) introduce partial permutohedra and determine their rank-indexed vertices and facets. Behrend et al. (arXiv:2207.14253, Sections 2.5--6 and Appendix A) study their face structure, Ehrhart data and volume, and record the precise vertex description used above. Hanada, Lentfer and Vindas-Meléndez (arXiv:2212.06885) relate generalized parking-function polytopes to partial permutohedra and determine enumerative properties. Bayer and collaborators (arXiv:2403.07387) study generalized parking-function polytopes using face, building-set, and polymatroid descriptions, with combinatorial and circuit-diameter bounds.

These source results provide the combinatorial input, but their inspected metric statements do not supply the Euclidean *smallest enclosing ball*, its rational minimax parameter, its full contact-rank classification or the sharp \(m=n(n+1)\) change. Generic smallest-enclosing-ball algorithms for polytopes address a different level of generality and do not, by themselves, state this parameterized classification. Euclidean diameter and minimum-volume enclosing ellipsoid are different invariants and do not independently determine the smallest Euclidean enclosing ball of this family.

## Limitations
The formula does not establish a new formula for polytope volume or the minimum-volume enclosing ellipsoid. The result is tied to the standard Euclidean realization and consecutive label set. No extension to arbitrary label weights, other norms, or nonorthogonal affine images is claimed. The literature comparison supports an originality assessment, not independent proof of bibliographic priority; equivalent earlier results under sparse permutation, anti-blocking polytope, or discrete Chebyshev-center terminology remain possible.

## References
1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first posted 2020-12-17; Section 5.1, especially Proposition 5.7 and Theorem 5.10. https://arxiv.org/abs/2012.09901
2. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris, and E. Insko, *Partial permutohedra*, arXiv:2207.14253, first posted 2022-07-28; Proposition 2.7. https://arxiv.org/abs/2207.14253
3. M. Hanada, J. Lentfer, and A. R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885, first posted 2022-12-13. https://arxiv.org/abs/2212.06885
4. M. M. Bayer and collaborators, *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387, first posted 2024-03-12. https://arxiv.org/abs/2403.07387
5. J. Elzinga and D. Hearn, *The minimum sphere covering a convex polyhedron*, Naval Research Logistics Quarterly 21 (1974), 715--718, DOI:10.1002/nav.3800210414.
