# Conditional correlation signs and compatible-family association in uniform polygon triangulations

## Finding

Let \(P\) be a fixed labeled convex polygon with \(N\ge4\) vertices and let \(T\) be a uniformly random triangulation of \(P\). For a noncrossing set \(S\) of internal diagonals write \(E_S=\{S\subseteq T\}\) and \(W(S)=|\{T:S\subseteq T\}|\). A diagonal is *admissible after* \(S\) if it is not in \(S\) and does not cross any element of \(S\).

**Conditional two-diagonal sign law.** Condition on \(E_S\). For two distinct admissible diagonals \(e,f\), their indicators are independent exactly when they lie in different polygonal cells of \(P\setminus S\). When both lie in one cell, their covariance is strictly positive if \(e,f\) do not cross and strictly negative if they cross. In particular the unconditioned sign is positive for compatible diagonals and negative for crossing diagonals.

**Compatible-family inequality.** For any noncrossing diagonal sets \(A,B\) whose union is noncrossing,
\[
 W(A\cup B)W(A\cap B)\ge W(A)W(B).
\]
Equality holds exactly when every cell of the subdivision by \(A\cap B\) contains diagonals from at most one of \(A\setminus B\) and \(B\setminus A\). Consequently, whenever \(A,B\) are nonempty and their union is noncrossing, the inclusion events \(E_A,E_B\) have *strictly positive* covariance. These statements describe compatible prescribed-diagonal events, not general increasing events on the full diagonal indicator vector.

## Assumptions and scope

All polygon vertices are in strictly convex position with a fixed cyclic order. The random object is uniform over the \(C_{N-2}\) maximal noncrossing sets of internal diagonals. A partial triangulation is any noncrossing set of diagonals, possibly empty or complete. The Catalan numbers are \(C_k=(k+1)^{-1}\binom{2k}{k}\), with \(C_0=1\). A polygonal cell with \(k+2\) vertices has \(k\) triangles in a triangulation and \(C_k\) possible triangulations. No independence across incompatible diagonals is asserted.

## Proof

**1. Product decomposition.** Conditioning on \(E_S\) leaves one independent uniformly random triangulation in each polygonal cell of the dissection by \(S\): every choice of cell triangulations gives exactly one global triangulation extending \(S\). Therefore
\[
 W(S)=\prod_{F\in\mathcal F(S)}C_{|V(F)|-2}.
\]
Every admissible diagonal lies in one such cell. Its indicator is nondegenerate because it belongs to some, but not all, triangulations of that cell.

**2. The exact local covariance.** Consider two distinct admissible diagonals in the same cell, which has \(k+2\) vertices. If they cross, their simultaneous inclusion is impossible, so the covariance is the strictly negative product of their two positive inclusion probabilities. If they are noncrossing, they dissect the cell into three subpolygons containing \(a,b,c\ge1\) triangles, with \(a+b+c=k\); label the middle subpolygon with \(b\) triangles. Direct Catalan counting yields
\[
 \Pr(e,f)=\frac{C_aC_bC_c}{C_k},\qquad
 \Pr(e)=\frac{C_aC_{b+c}}{C_k},\qquad
 \Pr(f)=\frac{C_{a+b}C_c}{C_k},
\]
and hence
\[
 \operatorname{Cov}(\mathbf1_e,\mathbf1_f)
 =\frac{C_aC_c}{C_k^2}\bigl(C_bC_k-C_{a+b}C_{b+c}\bigr)>0.
\]
Indeed, the consecutive Catalan ratios satisfy \(C_{j+1}/C_j=4-6/(j+2)\), strictly increasing in \(j\ge0\). Applying these ratios to the two length-\(a\) products gives \(C_bC_{b+a+c}>C_{b+a}C_{b+c}\) for \(a,c\ge1\). The conditional covariance is zero for diagonals in different cells by step 1. This proves every conditional sign and every boundary case.

**3. Monotonicity under compatible information.** Suppose \(S\) is noncrossing and \(d,e\) are distinct additional diagonals compatible with \(S\) and each other. The sign law gives
\[
 \Pr(d\in T\mid E_{S\cup\{e\}})\ge \Pr(d\in T\mid E_S),
\]
with strict inequality exactly when \(d,e\) lie in the same cell after \(S\). Successively adding any compatible diagonals preserves this inequality. Importantly, conditioning on \(S\) still permits all extensions used in the argument.

**4. Arbitrary compatible families.** Fix noncrossing \(A,B\) with noncrossing union, and set \(S=A\cap B\), \(U=A\setminus B\), \(V=B\setminus A\). Given \(E_S\), expand \(\Pr(E_V\mid E_{S\cup U})\) by the chain rule over an arbitrary ordering of \(V\). In each factor, compare the conditional probability after adding the diagonals of \(U\), one by one, with the factor conditioned only on previously added diagonals of \(V\). Step 3 makes every factor no smaller. Thus
\[
 \Pr(E_U\cap E_V\mid E_S)
 \ge\Pr(E_U\mid E_S)\Pr(E_V\mid E_S).
\]
Multiplying by \(W(S)^2\) and using the product decomposition yields the displayed inequality for \(W\).

For the equality criterion, decompose given \(E_S\) over its independent cells. If no cell receives both a member of \(U\) and a member of \(V\), the events are independent. Otherwise choose, in one shared cell, a member of \(V\) as the first chain-rule term and a member of \(U\) as the first added condition. Their strict positive conditional covariance from step 2 makes that factor strictly larger; all subsequent additions can only increase it. Hence the inequality is strict precisely in the asserted case.

Finally, if \(A,B\) are nonempty and \(S=\varnothing\), they both contribute diagonals to the sole initial cell, giving strict inequality. If \(S\ne\varnothing\), then \(0<\Pr(E_S)<1\), and the family inequality implies
\[
 \Pr(E_{A\cup B})\ge\frac{\Pr(E_A)\Pr(E_B)}{\Pr(E_S)}
 >\Pr(E_A)\Pr(E_B).
\]
This proves the unconditional strict event association.

## Verification

The standalone standard-library program `check.py` recursively enumerates every triangulation of every labeled convex polygon with \(4\le N\le9\). It independently checks Catalan extension counts, the compatible-family inequality for every pair of subsets of every triangulation, and the complete three-valued conditional covariance signs for all feasible partial triangulations and additional diagonal pairs. It also checks \(12{,}635\) instances of strict Catalan log-convexity. It reports **1,983,545 exact assertions passed**. These finite checks supplement, but do not replace, the unrestricted algebraic proof above. Run with `python check.py`.

## Relationship to prior work

The Catalan enumeration of convex-polygon triangulations and their independent subdivision into fixed-diagonal cells are classical. Eppstein and Frishberg, *Improved mixing for the convex polygon triangulation flip walk* (arXiv:2207.09972, first posted 2022-07-20), derive modern sampling and associahedron-decomposition bounds, including products of smaller Catalan classes. Black et al., *Sampling planar tanglegrams and pairs of disjoint triangulations* (arXiv:2304.05318, first posted 2023-04-11), develop a distinct paired-triangulation sampling model and its flip graph. The inspected principal results and pertinent arguments do not state the complete conditional sign law or the compatible-family inequality with its equality classification. The theorem here is a probabilistic consequence of classical Catalan counting, not a new enumeration or a claim about mixing time.

## Limitations

The result applies to uniform triangulations of a convex polygon, not weighted triangulations, arbitrary point sets, random planar maps, or pairs of triangulations conditioned to be disjoint. Compatibility of the *union* is essential: crossing prescribed sets can have zero joint probability. No claim is made that the full distribution is FKG or MTP2; crossing diagonal indicators are negatively correlated. Historical-priority assessment is limited to the cited and searched literature, and no independent review has been performed.

## References

1. D. Eppstein and D. Frishberg, *Improved mixing for the convex polygon triangulation flip walk*, arXiv:2207.09972 (2022), https://arxiv.org/abs/2207.09972.
2. A. E. Black, K. Liu, A. Mcdonough, G. Nelson, M. C. Wigal, M. Yin, Y. Yoo, *Sampling planar tanglegrams and pairs of disjoint triangulations*, arXiv:2304.05318 (2023), https://arxiv.org/abs/2304.05318.
3. Classical Catalan enumeration of convex-polygon triangulations, used solely as a known counting identity.
