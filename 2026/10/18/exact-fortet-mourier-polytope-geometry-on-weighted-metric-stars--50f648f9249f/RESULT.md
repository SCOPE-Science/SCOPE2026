# Exact Fortet–Mourier polytope geometry on weighted metric stars

## Finding

Let \(m\geq 1\) and let \(\rho_1,\ldots,\rho_m\) be arbitrary positive real numbers. Give \(S=\{o,1,\ldots,m\}\) the weighted-star metric \(d(o,i)=\rho_i\) and \(d(i,j)=\rho_i+\rho_j\) for distinct leaves. On real functions on \(S\), consider the Fortet–Mourier norm
\[
\|f\|_{\mathrm{FM}}=\max\{\|f\|_\infty,\operatorname{Lip}(f)\}.
\]
The unit ball \(B_\rho\) has exactly \(2(m+1)+2k\) facets, where \(k=\#\{i:\rho_i<2\}\). They are the nonredundant inequalities \(-1\leq f(o),f(i)\leq 1\) and, for each \(\rho_i<2\), \(|f(i)-f(o)|\leq\rho_i\).

Here is a complete, finite classification of *all* vertices, including coincident lengths and transition values. For \(t\in[-1,1]\), put
\[
L_i(t)=\max\{-1,t-\rho_i\},\qquad U_i(t)=\min\{1,t+\rho_i\}.
\]
Every vertex has center value \(t\) in
\[
\{-1,1\}\cup\mathcal A,\qquad
\mathcal A=\{1-\rho_i,\rho_i-1:\rho_i<2\}\cap(-1,1),
\]
and every leaf value is independently one of \(L_i(t),U_i(t)\). At \(t=\pm1\), all \(2^m\) endpoint choices are vertices. At an interior anchor \(t\in\mathcal A\), an endpoint choice is a vertex *if and only if* at least one leaf satisfies
\[
[t=1-\rho_i\ \text{and}\ f(i)=1]\quad\text{or}\quad
[t=\rho_i-1\ \text{and}\ f(i)=-1].
\]
To count them without duplicates, let \(s(t)\) be the number of distinct leaves for which one or both displayed anchoring equalities are possible. If some leaf has *both* anchoring equalities at \(t\) (necessarily \(\rho_i=1,t=0\)), there are \(2^m\) vertices over \(t\). Otherwise there are \(2^m-2^{m-s(t)}\) vertices over \(t\). Thus the total number is exactly \(2^{m+1}\) plus these contributions over the *distinct* interior anchors.

In particular, for all lengths in \((0,2)\) satisfying \(\rho_i\ne1\), pairwise distinctness, and \(\rho_i+\rho_j\ne2\) for \(i\ne j\), the number of vertices is
\[
\boxed{(m+2)2^m}.
\]
This is the largest possible number for any positive length vector with \(m\) leaves. All nongeneric collisions are handled by the exact anchor-counting rule above; for instance, when every length equals one, the count falls to \(3\cdot2^m\), and when all lengths are at least two, the ball is a cube with \(2^{m+1}\) vertices.

For *every* real signed atomic measure \(\mu=\alpha_0\delta_o+\sum_{i=1}^m\alpha_i\delta_i\), set \(p_i=\max\{\alpha_i,0\}\) and \(q_i=\max\{-\alpha_i,0\}\). Its exact dual norm is
\[
\boxed{\|\mu\|_{\mathrm{FM}}^*=\max_{t\in\{-1,1\}\cup\mathcal A}
\left[\alpha_0t+\sum_{i=1}^m\bigl(p_iU_i(t)-q_iL_i(t)\bigr)\right].}
\]
The maximum can be computed with \(O(m\log m)\) comparisons and arithmetic operations by sorting at most \(2m\) breakpoints and sweeping the slopes of one concave piecewise-affine function. No positivity or equal-mass assumption on the measure is needed.

## Assumptions and scope

All vector spaces and measures are real. The vertex and facet claims cover every integer \(m\ge1\) and every vector of *strictly positive* arm lengths; the arm lengths may be arbitrarily unequal, may exceed two, and may coincide. Distances are the shortest-path distances of the star, not arbitrary distances between leaves. The norm is the maximum of the supremum norm and the Lipschitz seminorm, *not* their sum. The dual formula is for all real coefficients, with no zero-total-mass restriction. The complexity bound counts exact real arithmetic operations and comparisons, not bit operations.

## Proof

**1. Reduction to a fibered polytope.** Write \(t=f(o)\) and \(x_i=f(i)\). On a star, the inequalities \(|x_i-t|\le\rho_i\) imply \(|x_i-x_j|\le\rho_i+\rho_j=d(i,j)\); hence all leaf-pair Lipschitz constraints are redundant. The remaining conditions are exactly
\[
-1\le t\le1,\qquad L_i(t)\le x_i\le U_i(t),\quad 1\le i\le m.
\]
Every fiber is an \(m\)-dimensional rectangle of positive side lengths, since \(\rho_i>0\). The origin is interior, so the polytope is full-dimensional.

**2. Facets.** The inequalities \(\pm t\le1\), \(\pm x_i\le1\), and \(\pm(x_i-t)\le\rho_i\) define the polytope. If \(\rho_i\ge2\), the last pair follows from the cube inequalities. Every other indicated inequality is a facet: one can find a point where it alone is active. For \(t=1\), choose every \(x_i=1-\min\{\rho_i,1\}/2\); the negative case is symmetric. For \(x_i=1\), take \(t=1-\rho_i/2\) when \(\rho_i<2\), and \(t=0\) otherwise; set every other leaf equal to \(t\). Again use symmetry for \(x_i=-1\). For \(x_i-t=\rho_i\) with \(\rho_i<2\), take \(t=-\rho_i/2\), \(x_i=\rho_i/2\) and all other leaves equal to \(t\); the opposite sign is symmetric. In each case every other displayed inequality is strict. Since a full-dimensional polytope has no further facet-defining inequalities beyond an irredundant halfspace description, the facet count is \(2(m+1)+2k\).

**3. Vertices.** Fix a point \((t,x_1,\ldots,x_m)\) in the ball. If any leaf coordinate lies strictly between \(L_i(t)\) and \(U_i(t)\), it can be perturbed in both directions and the point is not extreme. Therefore, a vertex selects one endpoint in every fiber. When \(t=\pm1\), the center is fixed by a cube face and each chosen leaf endpoint is fixed by one supporting inequality; their \(m+1\) independent active equations make every corner a vertex.

Now suppose \(-1<t<1\). Away from the breakpoints \(1-\rho_i\) and \(\rho_i-1\), every selected endpoint is locally a single affine function of \(t\), so the entire corner admits small feasible perturbations in both directions of \(t\). The same holds at a breakpoint if no selected endpoint is *doubly active*: no chosen leaf then simultaneously meets a cube face and a leaf-center Lipschitz face. In contrast, if a selected upper endpoint equals one at \(t=1-\rho_i\), its two active equations \(x_i=1\) and \(x_i-t=\rho_i\) fix \(t\); a selected lower endpoint equals minus one at \(t=\rho_i-1\) and likewise fixes \(t\). The other selected endpoints fix every remaining leaf. These are \(m+1\) independent equations, proving sufficiency and the asserted if-and-only-if characterization.

**4. Vertex counts and maximum.** At a fixed interior anchor, each of the \(m\) leaf intervals has two distinct endpoints. If a leaf permits both pinning signs, either endpoint pins \(t\), so all \(2^m\) corners are vertices. Otherwise each of the \(s(t)\) anchor leaves has exactly one pinning endpoint; exactly \(2^{m-s(t)}\) corners avoid all pins. This proves the collision formula. Each individual elementary anchoring event contributes at most \(2^{m-1}\) corners. There are at most \(2k\) such events, so the total is at most \(2^{m+1}+2k2^{m-1}\le(m+2)2^m\). Under the stated generic assumptions the \(2m\) anchor values are distinct; each has exactly one event, attaining the upper bound.

**5. Dual optimization.** Fix \(t\). Maximizing \(\sum_i\alpha_i x_i\) over the rectangular fiber picks \(U_i(t)\) for \(\alpha_i>0\), \(L_i(t)\) for \(\alpha_i<0\), and any value for zero coefficients. The maximized functional is
\[
F_\mu(t)=\alpha_0t+\sum_i[p_i\min\{1,t+\rho_i\}-q_i\max\{-1,t-\rho_i\}].
\]
This is a continuous concave piecewise-affine function on \([-1,1]\); its only possible interior slope changes occur at \(1-\rho_i\) and \(\rho_i-1\). The maximum is therefore achieved at an endpoint or one of those breakpoints. Sorting these values and integrating the initial slope \(\alpha_0+\sum_{\rho_i<2}p_i\), with downward jumps \(p_i\) at \(1-\rho_i\) and \(q_i\) at \(\rho_i-1\), gives the stated \(O(m\log m)\) algorithm and exact dual formula.

## Verification

The accompanying self-contained Python program `check_fm_star.py` performs exhaustive exact-rational active-set vertex enumeration for ten two-/three-leaf length vectors and three four-leaf length vectors, including generic lengths, repeated lengths, complementary lengths, lengths equal to one and two, and inactive Lipschitz constraints. Independently constructed fiber corners coincide with the full active-set results. Exact rational facet witnesses, vertex counts, and dual support-function calculations were checked; the dual calculation was performed in three independent ways: breakpoints, exhaustive vertices, and a sorted slope sweep. The program completed 897 assertions. These finite checks supplement, but do not substitute for, the all-dimensional proof above.

## Relationship to prior work

Hille and Theewis (2022, arXiv:2206.12234) give general convex-optimization algorithms for atomic Fortet–Mourier norms and explicit formulas in a single-Dirac regime; Section 4 notes the absence of comparably explicit general formulas for sums of multiple positive Diracs. The present claim is a star-specific exact finite-breakpoint rule for *arbitrary signed* atomic measures, together with a complete extremal-polytope classification rather than a general existence or optimization reduction.

Hille and Theewis (2023, arXiv:2305.08500) study norming families and extreme points for the maximum-type Fortet–Mourier norm and the *different*, sum-type bounded-Lipschitz norm. Their Sections 1, 5 and 6 provide relevant general geometry and explain why explicit finite-space extreme sets matter, but do not state the weighted-star counts or their collision formula.

Gordon and Petrov (arXiv:1608.06848, published 2017) compute a universal face vector for **generic strict metrics**. The Fortet–Mourier ball is also the pointed Lipschitz polytope obtained by adjoining an apex at distance one from every star point and truncating original distances to \(\min\{d,2\}\). When \(m\ge2\), this augmented metric is never strict: for any two leaves, the truncated distance is attained by a two-edge route through the center or through the apex. Consequently their generic-strict theorem does not yield the all-length vertex counts. (For \(m=1\), its generic three-point case is compatible with the six vertices above.) Farmer (1994) supplies a general qualitative extremality characterization for Lipschitz balls; it does not by itself state the explicit weighted-star arithmetic and algorithm here. Unindexed equivalent polytope descriptions remain a bibliographic possibility.

## Limitations

The results concern finite, scalar-valued real metric stars only; they do not assert analogous counts on general trees, general metrics, vector-valued functions, or the sum-normalized bounded-Lipschitz ball. The comparison with prior literature is based on the accessible primary material described above; the full text of Farmer (1994) was not available in the present bibliography check, and a differently phrased equivalent result could exist. The computational checks do not constitute an independent mathematical audit.

## References

1. S. C. Hille and E. S. Theewis, *Explicit expressions and computational methods for the Fortet–Mourier distance to finite weighted sums of Dirac measures*, arXiv:2206.12234 (first submitted 24 June 2022), Sections 2–4.
2. S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500 (first submitted 15 May 2023), Sections 1, 5–6.
3. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848 (first submitted 24 August 2016), Arnold Mathematical Journal **3** (2017), 205–218.
4. J. D. Farmer, *Extreme points of the unit ball of the space of Lipschitz functions*, Proceedings of the American Mathematical Society **121** (1994), 807–813, doi:10.1090/S0002-9939-1994-1195718-7.
