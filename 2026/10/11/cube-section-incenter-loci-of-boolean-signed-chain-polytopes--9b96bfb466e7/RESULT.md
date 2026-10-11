# Cube-section incenter loci of Boolean signed-chain polytopes

## Finding

Let \(d\ge1\) be an integer. In the Boolean inclusion poset \(B_d=2^{[d]}\), let \(Q_d\subset\mathbb R^{2^d}\) be the centrally symmetric signed-chain polytope
\[
Q_d=\left\{x=(x_S)_{S\subseteq[d]}:
\left|\sum_{S\in C}x_S\right|\le1
\quad\text{for every nonempty chain }C\subseteq B_d\right\}.
\]
All Euclidean distances use the standard orthonormal basis indexed by subsets. Write
\[
h=d+1,\qquad a_d=1-\sqrt{\frac d{d+1}}.
\]
The exact maximum-inscribed-ball radius and its complete set of centers are
\[
\boxed{\rho(Q_d)=\frac1{\sqrt{d+1}}},\qquad
\boxed{\mathcal I(Q_d)=
\left\{x:x_S=t_{|S|},\ \sum_{k=0}^d t_k=0,\ |t_k|\le a_d\ \text{for every }k\right\}.}
\]
Thus the incenter set is affinely equivalent to the central hyperplane section of the \((d+1)\)-cube \([-a_d,a_d]^{d+1}\) and has affine dimension exactly \(d\), despite the ambient dimension \(2^d\). The number of its vertices is
\[
\boxed{f_0(\mathcal I(Q_d))=
\begin{cases}
\displaystyle\binom{d+1}{(d+1)/2},&d\text{ odd},\\
\displaystyle(d+1)\binom d{d/2},&d\text{ even}.
\end{cases}}
\]
The first case consists of all balanced assignments \(t_k\in\{\pm a_d\}\). In the second, exactly one rank coordinate is zero, and the remaining rank coordinates consist of equally many \(+a_d\) and \(-a_d\).

## Assumptions and scope

A chain is a nonempty sequence of distinct subsets strictly increasing under inclusion. The signed-chain halfspaces are two-sided sums, **not** the distinct inequalities \(\sum_{S\in C}|x_S|\le1\) defining the enriched chain polytope, nor the nonnegative one-sided inequalities of the ordinary chain polytope. The two-sided chain construction is the classical-poset specialization of the signed-chain framework described by Hlavacek and by Beck–Hlavacek. All ranks \(0,\ldots,d\) occur; the empty subset and full subset are genuine coordinates. The polytope is full-dimensional since zero strictly satisfies every inequality; it is bounded by its singleton-chain inequalities. Inradius and incenter are taken in this full ambient Euclidean space, without affine or lattice renormalization.

## Proof

**1. Sharp radius.** Every maximal chain \(C\) of \(B_d\) has \(h=d+1\) elements, and the corresponding two supporting halfspaces have unit normal proportional to its incidence vector \(\mathbf1_C\), of Euclidean norm \(\sqrt h\). A ball of center \(c\) and radius \(r\) contained in \(Q_d\) necessarily satisfies
\[
\left|\sum_{S\in C}c_S\right|+r\sqrt h\le1.
\]
Thus \(r\le h^{-1/2}\). The ball of this radius centered at zero satisfies every chain inequality, because every chain has at most \(h\) elements. Hence \(\rho=h^{-1/2}\).

**2. Maximal chains force rank-constant centers.** At any optimal center \(c\), the preceding inequality is an equality in its radius term for every maximal chain, so \(\sum_{S\in C}c_S=0\). Identify a maximal chain with a permutation of \([d]\), whose successive prefixes have ranks \(0,1,\ldots,d\). Two permutations differing by one adjacent transposition give maximal chains sharing every coordinate except one intermediate rank-\(k\) subset. Subtracting the zero chain-sum identities gives
\[
c_{U\cup\{i\}}=c_{U\cup\{j\}}
\quad\text{whenever }|U|=k-1,\ i,j\notin U.
\]
For each rank \(1\le k\le d-1\), these are the edges of the connected Johnson graph on \(k\)-subsets. The bottom and top ranks are already singletons. Therefore \(c_S=t_{|S|}\) for some \(d+1\) scalars \(t_k\), and every maximal-chain sum gives \(\sum_{k=0}^d t_k=0\).

**3. Chains with one omission determine the coordinate bounds.** Take any maximal chain and remove its rank-\(k\) member. The remaining \(h-1=d\) members form a chain. At the optimal radius, this chain imposes
\[
\left|\sum_{j\ne k}t_j\right|+\frac{\sqrt{h-1}}{\sqrt h}\le1.
\]
By the zero total sum, this is exactly \(|t_k|\le 1-\sqrt{(h-1)/h}=a_d\), for each \(k\in\{0,\ldots,d\}\).

**4. No shorter chain adds a restriction.** Conversely, suppose \(\sum_{k=0}^{h-1}t_k=0\) and \(|t_k|\le a_d\). Every chain uses distinct ranks, say a subset \(J\) of \(\{0,\ldots,h-1\}\) of size \(s\). Since both the selected sum and its complement differ only by sign,
\[
\left|\sum_{k\in J}t_k\right|\le a_d\min(s,h-s).
\]
For real \(z\in[0,h]\), put \(F(z)=1-\sqrt{1-z/h}\), a convex function with \(F(0)=0\). Its convexity gives \(F(m)\ge mF(1)=m a_d\) for integers \(m\ge0\). With \(m=\min(s,h-s)\), we obtain
\[
a_d\min(s,h-s)\le
1-\sqrt{\frac{\max(s,h-s)}h}
\le1-\sqrt{\frac sh}.
\]
Thus \(\big|\sum_{S\in C}c_S\big|+\rho\sqrt{|C|}\le1\) for every chain \(C\); the radius-\(\rho\) ball centered at \(c\) is contained in \(Q_d\). Steps 1–4 give the claimed **entire** incenter locus.

**5. Dimension and vertices.** The hyperplane \(\sum t_k=0\) has dimension \(h-1=d\), and its central point is interior relative to the coordinate bounds because \(a_d>0\). A vertex of this hyperplane section has at least \(h-1\) independent active coordinate bounds. When \(h\) is even, the zero-sum constraint forces all \(h\) entries to be saturated, with \(h/2\) of each sign. When \(h\) is odd, one entry must remain at zero while all other \(h-1\) entries are saturated and balanced. Conversely every listed point has \(h-1\) independent active coordinate bounds and is a vertex. The formulas follow by choosing its sign pattern and, in the odd-\(h\) case, the zero coordinate.

## Verification

The included, standard-library-only program `artifacts/verify_signed_boolean_incenters.py` checks ranks over exact rational arithmetic of all maximal-chain incidence matrices, the complete combinatorial vertex census of the claimed cube sections, and the maximum-ball slack for every rank-subset chain at all section vertices, for \(1\le d\le6\). It confirms rank \(2^d-d\) in each instance and incenter vertex counts \(2,6,6,30,20,140\), respectively. A separate numerical linear-program calculation for \(1\le d\le4\) compared the optimal inradius with \(1/\sqrt{d+1}\). These finite tests are checks only; the proof establishes every \(d\ge1\).

## Relationship to prior work

Hlavacek's 2023 dissertation, Chapter 5, presents the signed-chain construction, and Beck–Hlavacek (2023), Section 6, develops signed chain polytopes, antichains, and reflexivity. Those results concern combinatorial, lattice, and Ehrhart geometry rather than the full Euclidean incenter set. Stanley's ordinary chain polytope and the enriched chain polytope defined by absolute sums are **different convex bodies**. For example, on a two-element chain, the present two-sided sum inequalities give a hexagon with a nontrivial segment of incenters, whereas the enriched chain body is a diamond with a unique incenter. An inradius formula for an enriched chain body can also give the common radius here by containment, but cannot imply the higher-dimensional incenter classification or its parity-dependent vertex counts.

## Limitations

The result concerns the standard-coordinate Euclidean metric and the Boolean inclusion poset with all ranks; it does not determine incenter loci for arbitrary signed posets or other metrics. The central cube-section description is an affine identification, not an ambient Euclidean isometry to an unweighted \((d+1)\)-coordinate section, because ranks have different multiplicities. Mathematical proof, rather than computational extrapolation, supports arbitrary \(d\). No claim is made about uniqueness of this result in every unpublished manuscript.

## References

1. M. L. Hlavacek, *Ehrhart Theory of Combinatorially Defined Polytopes*, PhD dissertation, University of California, Berkeley (public date 2023-08-01), Chapter 5. Public dissertation record: https://escholarship.org/uc/item/84g603xd ; institutional date record: https://pantheon.math.berkeley.edu/publications/ehrhart-theory-combinatorially-defined-polytopes .
2. M. Beck and M. Hlavacek, *Signed Poset Polytopes* (first arXiv release 2023-11-08), Section 6, especially Definitions 6.4–6.5 and Proposition 6.7. https://arxiv.org/abs/2311.04409v1 .
3. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, for the ordinary one-sided chain polytope.
