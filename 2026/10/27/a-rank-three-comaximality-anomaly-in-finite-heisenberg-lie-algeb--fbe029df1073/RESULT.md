# A rank-three comaximality anomaly in finite Heisenberg Lie algebras

## Finding
Let \(q\) be any prime power, \(r\geq1\), and \(H_{2r+1}(\mathbb F_q)\) the Heisenberg Lie algebra with one-dimensional derived centre. Form the **comaximal graph** whose vertices are its nonzero proper Lie subalgebras, joining distinct vertices \(A,B\) precisely if \(\langle A,B\rangle_{\rm Lie}=H_{2r+1}(\mathbb F_q)\). The graph has the exact vertex and edge census given below. Most notably, for independent uniformly selected **distinct** vertices, its edge probability has the remarkable large-field limit
\[
\lim_{q\to\infty}\Pr(A\sim B)=\begin{cases}4/9,&r=3,\\1,&r\ne3.\end{cases}
\]
Here the limit is over arbitrary prime powers \(q\) at fixed rank \(r\). Thus the seven-dimensional Heisenberg algebra is the unique rank in this family with a nonunit asymptotic comaximality probability.

Define Gaussian coefficients \({d\brack k}_q\) by counting \(k\)-dimensional subspaces of \(\mathbb F_q^d\), and put
\[
 I_{r,k}=\prod_{j=0}^{k-1}\frac{q^{2r-j}-q^j}{q^k-q^j}\quad(0\le k\le r),
\qquad C_{d,k}=\sum_{s=1}^k {k\brack s}_q q^{(d-k)s}\quad(1\le k<d).
\]
The first is the number of totally isotropic \(k\)-spaces in a nondegenerate symplectic \(2r\)-space. Then the **exact vertex census** is
\[
 N_{r,q}=\sum_{k=0}^{2r-1}{2r\brack k}_q+\sum_{k=1}^r I_{r,k}q^k,
\]
and the **exact unoriented edge census** is
\[
 \boxed{E_{r,q}=\frac12\sum_{k=1}^{2r-1}{2r\brack k}_q C_{2r,k}
   +\sum_{k=1}^r I_{r,k}q^k C_{2r,k}
   +\frac12 I_{r,r}q^{r(r+1)/2+2r}.}
\]
The probability is exactly \(2E_{r,q}/(N_{r,q}(N_{r,q}-1))\). For every \(r,q\), the clique and chromatic numbers both equal \((q^{2r}-1)/(q-1)\). There are exactly \((q+1)^{q+1}\) maximum-cardinality cliques when \(r=1\), and exactly one when \(r\ge2\).

## Assumptions and scope
All Lie algebras and subalgebras are linear over \(\mathbb F_q\). A vertex is required to be nonzero and proper; a subalgebra need not contain the centre. An edge means **Lie generation**, not vector-space sum of its subalgebras, although the two projected spaces must sum to the quotient by the centre. The formulas cover characteristic two: an alternating nondegenerate form still exists and defines the Heisenberg bracket. The graph is simple, so loops are excluded. The asymptotic limit holds with \(r\) fixed and \(q\to\infty\).

## Proof
Write \(H=V\oplus\mathbb F_qz\), where \(\dim V=2r\) and \([u+az,v+bz]=\omega(u,v)z\) for a nondegenerate alternating form \(\omega\). If a proper subalgebra contains \(z\), it is uniquely \(U\oplus\mathbb F_qz\) for a proper subspace \(U<V\). This includes \(U=0\), giving the central line. If it does not contain \(z\), its projection is injective with image a nonzero totally isotropic subspace \(U\) of dimension at most \(r\), and the subalgebra is the graph of an arbitrary linear functional \(U\to\mathbb F_q\). This gives \(q^{\dim U}\) lifts. Counting orthogonal ordered bases produces \(I_{r,k}\); these observations establish the vertex census.

**Generation criterion.** If two vertices project to \(U,W\le V\), they Lie-generate \(H\) if and only if \(U+W=V\). The forward implication holds after passage to the abelian quotient \(H/\mathbb F_qz\). Conversely, if \(U+W=V\), the generated subalgebra projects onto all of \(V\). Some bracket of lifted vectors must be nonzero, since otherwise \(\omega\) vanishes on their spanning space \(V\), contradicting nondegeneracy. Thus the generated subalgebra contains \(z\) as well and is all of \(H\).

**Completion count.** Fix a \(k\)-space \(U\) in a \(d\)-space. A proper subspace \(W\) satisfies \(U+W=V\) exactly when \(T=U\cap W\) has dimension \(t<k\), and \(W/T\) is the graph of a linear map \(V/U\to U/T\). There are \({k\brack t}_q\) choices of \(T\) and \(q^{(d-k)(k-t)}\) graph maps. Summing over \(t=0,\ldots,k-1\) yields \(C_{d,k}\). This proves the first edge term for pairs of centre-containing vertices (divide ordered pairs by two) and the second term for mixed pairs (no division).

**Pairs outside the centre.** Suppose both vertices omit \(z\) and their projections span \(V\). Each projection is isotropic of dimension at most \(r\), hence both are Lagrangian \(r\)-spaces and are complementary. For each fixed Lagrangian \(U\), its complementary Lagrangians are graphs of symmetric linear maps \(U^*\to U\), of which there are exactly \(q^{r(r+1)/2}\), also in characteristic two. There are \(I_{r,r}\) choices of \(U\), and each ordered pair of projections has \(q^{2r}\) functional lifts. Division by two yields the third edge term. In conjunction with the first two terms this counts every possible pair exactly once.

**Clique and chromatic numbers.** A proper subspace \(U<V\) lies in some hyperplane. Color each graph vertex using a hyperplane containing its projection. The generation criterion ensures that adjacent vertices cannot share a color, yielding at most \((q^{2r}-1)/(q-1)\) colors. The central-containing vertices projecting onto all hyperplanes are pairwise adjacent, giving equality with the clique number. A clique of that size forces the sets of containing hyperplanes of its projections to be nonempty and pairwise disjoint subsets of exactly that many hyperplanes. Every set must therefore be a singleton, so each projection is itself a hyperplane. For \(r\ge2\) hyperplanes are not isotropic and possess only the unique central-containing lift, hence the maximum clique is unique. For \(r=1\), every hyperplane is an isotropic line with \(q+1\) possible vertices (one central-containing and \(q\) graph lifts), and choosing one lift independently at each of the \(q+1\) lines gives exactly \((q+1)^{q+1}\) maximum cliques.

**Large-field limit.** At fixed rank, the unique leading monomial of \({2r\brack k}_q\) has degree \(k(2r-k)\) and leading coefficient one. Thus the central-containing population has leading term \(q^{r^2}\), arising from projection dimension \(r\). For a centre-free population of isotropic projection dimension \(k\), the leading exponent is
\[
 f_r(k)=2rk-\frac32k^2+\frac32k,
\]
again with coefficient one. For \(r=1,2\), exactly the centre-free Lagrangian stratum dominates, with exponent \(f_r(r)>r^2\). For \(r=3\), exactly three populations contribute equally, with leading term \(q^9\) each: central-containing dimension-three projections and centre-free isotropic dimension-two and dimension-three projections. For \(r\ge4\), \(f_r(k)<r^2\) for all \(1\le k\le r\), so central-containing dimension-\(r\) projections alone dominate. This strict inequality follows from the quadratic bound \(f_r(k)\le (4r+3)^2/24<r^2\) for every \(r\ge4\).

For any two dominant projection strata whose dimensions sum to at least \(2r\), random independent projections are complementary with probability tending to one. In the cases used here this follows quantitatively by comparing the explicit graph-completion count \(C_{2r,r}\) with the Gaussian count of \(r\)-spaces, and the complementary-Lagrangian count \(q^{r(r+1)/2}\) with \(I_{r,r}\); analogous estimates for a random \(r\)-space paired with a Lagrangian follow by the same quotient-graph calculation. In rank three, the two different centre-free strata of dimensions two and three *cannot* generate, nor can two dimension-two projections generate; only pairs among the two size-\(q^9\) dimension-three strata (one centre-containing and one centre-free) generate asymptotically. Hence four of the nine asymptotically equiprobable ordered stratum pairs are edges, giving \(4/9\). For \(r\ne3\), both dominant projections have dimension \(r\), and the complement probability tends to one. Passing from independent draws to uniformly chosen distinct vertices does not change the limit, since \(N_{r,q}\to\infty\).

## Verification
The standalone `verify_heisenberg.py` constructs finite-field subspaces in reduced row-echelon form, explicitly tests isotropy, creates **all** Lie subalgebra lifts, and verifies adjacency using iterative Lie-bracket closure rather than the projection-sum criterion. It independently evaluates all three exact edge sums. It exhaustively checks \((r,q)=(1,2),(1,3),(1,5),(2,2),(2,3)\) and validates hyperplane coloring and clique witnesses. The respective vertex/edge pairs are \((10,27)\), \((17,96)\), \((37,540)\), \((156,3805)\), and \((691,100905)\). Large-parameter arithmetic checks include \((r,q)=(3,2),(3,3),(4,2)\), without asserting exhaustive adjacency enumeration there. The code requires only Python's standard library and runs via `python verify_heisenberg.py`.

## Relationship to prior work
Towers, Zuleta and Gutierrez, *Comaximal Graphs of Finite-Dimensional Lie Algebras over Finite Fields: Triangle Counts and Structural Invariants* (arXiv:2608.16575, initially public 2026-08-17), provide the recent graph framework, low-dimensional cases and Frattini quotient techniques. Their earlier *Comaximal Graphs of Lie Algebras* (arXiv:2605.09583) includes the three-dimensional Heisenberg case. Das, *Subspace Sum Graph of a Vector Space* (arXiv:1702.08245), develops the underlying subspace graph; coloring by hyperplanes and unweighted subspace-sum reasoning belong to this background. Earlier finite-Heisenberg analyses already supply the five-dimensional degree census and the induced graph on centre-free subalgebras, including complementary Lagrangian pairs. The present contribution is the **combined full all-rank weighted edge census and the sharp rank-three large-field discontinuity**; the separately known pieces are not presented as independent discoveries. Existing results on *subalgebra commutativity degree* count permuting subalgebra pairs, which is a different adjacency relation and do not yield the comaximal probability.

## Limitations
The theorem concerns only Heisenberg Lie algebras over finite fields and only fixed-rank large-field limits. It is not a classification of comaximal graphs of general nilpotent Lie algebras, nor an assertion about rank increasing with field size. Generic Gaussian-coefficient and symplectic-complement facts are standard. Equivalent or stronger unindexed literature is a residual originality risk; the exact all-rank formula may be more readily deducible from general weighted Frattini-quotient principles than its asymptotic phase change suggests. Finite computation corroborates but is not an infinite proof. The review is self-review only; independent validation has not been performed.

## References
1. D. Towers, Y. Zuleta and I. Gutierrez, *Comaximal Graphs of Finite-Dimensional Lie Algebras over Finite Fields: Triangle Counts and Structural Invariants*, arXiv:2608.16575 (initial version 2026-08-17), https://arxiv.org/abs/2608.16575.
2. D. Towers and collaborators, *Comaximal Graphs of Lie Algebras*, arXiv:2605.09583, https://arxiv.org/abs/2605.09583.
3. A. Das, *Subspace Sum Graph of a Vector Space*, arXiv:1702.08245, https://arxiv.org/abs/1702.08245.
