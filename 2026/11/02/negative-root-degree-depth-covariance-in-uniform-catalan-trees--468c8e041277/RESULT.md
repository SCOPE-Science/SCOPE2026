# Negative root-degree/depth covariance in uniform Catalan trees

## Finding

Let \(T_n\) be uniformly distributed among all rooted ordered (plane) trees with exactly \(n\) edges. Let \(D_n\) be the number of children of the root and let \(H_n\) be the sum of distances of all vertices from the root. For every integer \(n\ge2\), with \(C_n=\frac{1}{n+1}\binom{2n}{n}\),

\[
\boxed{\operatorname{Cov}(D_n,H_n)=\frac{3\cdot4^n/C_n-(2n+1)(n+3)}{n+2}<0.}
\]

Moreover,

\[
\operatorname{Cov}(D_n,H_n)=-2n+3\sqrt{\pi n}-3+O(n^{-1/2})\quad(n\to\infty).
\]

The negative dependence is non-negligible in absolute terms: the root degree has a bounded limiting mean, whereas the mean total root-to-vertex distance is of order \(n^{3/2}\); the covariance is of order \(-n\). The single-edge case has zero covariance because both quantities are deterministic.

## Assumptions and scope

Trees are unlabelled but ordered: siblings have a left-to-right order and distinct shapes are equally likely. The size parameter is *edges*, not vertices. Distances use edge lengths one and include the root with depth zero. No increasing-label or recursive-growth distribution is imposed. The result is a finite exact identity and a standard asymptotic expansion, without distributional ordering, concentration or causal claims.

In the contour/Dyck-path bijection, an upward step of starting height \(h\) corresponds to a child at tree depth \(h+1\). Therefore the Dyck area \(A_n\), defined as the sum of the starting heights of all upward steps, satisfies \(H_n=A_n+n\). The number of primitive Dyck excursions (returns to height zero after a nonempty excursion) is exactly \(D_n\), hence \(\operatorname{Cov}(D_n,H_n)=\operatorname{Cov}(D_n,A_n)\).

## Proof

Write \(F(z,q)=\sum_{P}z^{|P|}q^{A(P)}\), summing all Dyck paths and using \(|P|\) for the number of upward steps; \(F(z,1)=C(z)\), where \(C(z)=1+zC(z)^2=2/(1+s)\) and \(s=\sqrt{1-4z}\). A primitive excursion is an upward step, an interior Dyck path, and a downward step. Elevating the interior increases the height of every interior upward step by one. Thus its bivariate generating function is

\[
P(z,q)=zF(qz,q),\qquad F(z,q)=\frac{1}{1-P(z,q)}.
\]

Mark the number of primitive factors by \(u\): \(F(z,q,u)=(1-uP(z,q))^{-1}\). Define \(A(z)=\partial_qF(z,q,1)|_{q=1}\), \(R(z)=\partial_u F(z,1,u)|_{u=1}\), and \(M(z)=\partial_u\partial_qF(z,q,u)|_{u=q=1}\). Differentiating the primitive relation gives \(P_q(z,1)=z(A(z)+zC'(z))\). Consequently,

\[
A(z)=zC(z)^2(A(z)+zC'(z))
=\frac{2}{1+s}-\frac{3}{2s}+\frac{1}{2s^2},
\]

\[
R(z)=C(z)^2-C(z),\qquad
M(z)=A(z)(1+2zC(z)^2)
=3C(z)+2C(z)^2-\frac{13}{2s}+\frac{3}{2s^2}.
\]

The standard coefficient identities \([z^n]C(z)^2=C_{n+1}\), \([z^n]s^{-1}=\binom{2n}{n}\), and \([z^n]s^{-2}=4^n\) yield exact *un-normalized* sums over all \(C_n\) trees:

\[
\begin{aligned}
\sum_T A(T)&=C_n-\tfrac32\binom{2n}{n}+\tfrac12 4^n,\\
\sum_T D(T)&=C_{n+1}-C_n,\\
\sum_T D(T)A(T)&=3C_n+2C_{n+1}-\tfrac{13}{2}\binom{2n}{n}+\tfrac32 4^n.
\end{aligned}
\]

Divide by \(C_n\) to obtain the three expectations, then subtract the product of the first two. Simplifying with \(C_{n+1}/C_n=2(2n+1)/(n+2)\) and \(\binom{2n}{n}/C_n=n+1\) gives the stated covariance.

It remains to establish its strict sign for *every* size. Put \(b_n=4^{-n}\binom{2n}{n}\) and \(t_n=3(n+1)/((2n+1)(n+3))\). The covariance is negative exactly when \(b_n>t_n\). At \(n=1\) they are equal, while for every integer \(n\ge1\),

\[
\frac{b_{n+1}}{b_n}-\frac{t_{n+1}}{t_n}
=\frac{n(2n+1)}{2(n+1)(n+4)(2n+3)}>0.
\]

Induction on the successive ratios proves \(b_n>t_n\) for all \(n\ge2\), giving strict negativity without an asymptotic argument. Finally, the central-binomial expansion \(\binom{2n}{n}=4^n(\pi n)^{-1/2}(1-1/(8n)+O(n^{-2}))\) in the exact covariance formula gives the stated expansion.

## Verification

A standalone `verify.py` checks an independently derived recursion from primitive-path concatenation against the three exact coefficient formulas, including the covariance, for every integer \(1\le n\le100\). It also enumerates all balanced nonnegative Dyck paths through \(n=10\) and checks the area, primitive-factor, mixed-moment and conditioned-area identities directly. It checks the rational ratio inequality for \(1\le n\le100\). This produces 760 exact integer/rational assertions; finite tests corroborate, but do not replace, the all-size proof above. Invoke `python verify.py` with Python 3, without external packages.

As an additional check on interpretation, fixing \(D_n=r\) gives a coefficient identity for the area sum: for \(1\le r<n\),

\[
\mathbb E[A_n\mid D_n=r]
=\frac{r\,[z^{n-r-1}]C(z)^r/(1-4z)}{[z^{n-r}]C(z)^r},
\]

and for \(r=n\) the conditional area is zero. This follows directly from \(P_q(z,1)=z^2C(z)/(1-4z)\). No all-size monotonicity of these conditional means is asserted.

## Relationship to prior work

Blanco and Petersen's study of Dyck area and noncrossing-partition *rank* supplies an earlier area-refinement context. That rank statistic is not the number of primitive excursions: their rank is transported from the noncrossing partition lattice, whereas the present second statistic counts the root's children. Dershowitz and Rinderknecht's Catalan-tree analysis develops the root-degree counts and average path-length machinery separately; the relevant inspected sections do not state their mixed covariance or an all-size strict sign. General enumerative treatments also provide the underlying Catalan/primitive-path identities. The claim of additional content is the exact finite mixed moment and strictly negative, linearly growing covariance with its correction term, **not** the classical Catalan enumeration or the area generating function.

## Limitations

This is a self-review, not an independent validation or historical priority certification. A general earlier bivariate rooted-tree enumerator could imply the identity after differentiation, even without its exact wording; such implicit coverage is a residual risk. Earlier general tree-pattern enumerations could not all be inspected in full. The result is restricted to *uniform plane trees*, and gives covariance, not stochastic ordering or a multivariate limit theorem. The exact identities are proved for all finite admissible sizes; the standalone checks cover finite sizes only.

## References

1. S. A. Blanco and T. K. Petersen, *Counting Dyck Paths by Area and Rank*, arXiv:1206.0803, first posted 2012-06-05. https://arxiv.org/abs/1206.0803
2. N. Dershowitz and C. Rinderknecht, *The Average Height of Catalan Trees by Counting Lattice Paths*, Mathematics Magazine 88 (2015), 187–195, DOI:10.4169/MATH.MAG.88.3.187. Readable preprint: https://oeis.org/A136439/a136439.pdf
3. N. Dershowitz and S. Zaks, *Applied Tree Enumerations*, CAAP 1981, pp. 180–193; historical background on root-degree enumerations. https://dblp.org/rec/conf/caap/DershowitzZ81
