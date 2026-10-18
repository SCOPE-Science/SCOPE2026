# Exact heterogeneous-weight sensitivity of finite-chain isotonic least squares

## Finding

For every integer \(n\ge1\), every strictly positive weight vector \(w=(w_1,\ldots,w_n)\), and every \(1\le p\le\infty\), let \(\Pi_w:\mathbb R^n\to\mathbb R^n\) be **weighted quadratic isotonic regression**,
\[
\Pi_w(x)=\operatorname*{argmin}_{y_1\le\cdots\le y_n}
\sum_{i=1}^n w_i(y_i-x_i)^2.
\]
The data-to-fit distance is the ordinary, *unweighted* \(\ell_p^n\) norm; the weights occur only in the least-squares objective. For \(1\le p\le\infty\), write \(q\) for the Hölder conjugate, with \(q=\infty\) if \(p=1\) and \(q=1\) if \(p=\infty\). Define \(W_B=\sum_{i\in B}w_i\) for a nonempty consecutive index block \(B\subseteq\{1,\ldots,n\}\). Then the *exact* global Lipschitz constant is
\[
\boxed{\operatorname{Lip}_{\ell_p}(\Pi_w)
=\max_{B\text{ consecutive, nonempty}}
\frac{|B|^{1/p}\|w_B\|_q}{W_B}.}
\tag{1}
\]
At \(p=\infty\), the factor \(|B|^{1/p}\) is one; at \(q=\infty\), \(\|w_B\|_q\) is the largest block weight. This finite formula is sharp even at \(p=1,\infty\), where the *regression objective remains quadratic*. It follows that
\[
\boxed{\operatorname{Lip}_{\ell_\infty}(\Pi_w)=1,\qquad
\operatorname{Lip}_{\ell_p}(\Pi_w)=1\ (1\le p<\infty)
\iff w_1=\cdots=w_n.}
\tag{2}
\]
In particular, any adjacent unequal weights produce strict amplification in every finite unweighted \(\ell_p\) metric, although the regression is nonexpansive in the Hilbert norm weighted by \(w\).

There is also an exact *worst-case weight-contrast law*. Normalize the smallest allowed weight to one, and fix \(\kappa\ge1\). Among all \(n\)-coordinate weight profiles with \(1\le w_i\le\kappa\), define \(\mathcal M_{n,p}(\kappa)=\sup_w\operatorname{Lip}_{\ell_p}(\Pi_w)\). For \(1<p<\infty\),
\[
\boxed{\mathcal M_{n,p}(\kappa)
=\max_{1\le k\le n}\max_{0\le r\le k}
\frac{k^{1/p}\bigl(r\kappa^q+k-r\bigr)^{1/q}}
{r\kappa+k-r}.}
\tag{3}
\]
The supremum is attained by a block with \(r\) weights at \(\kappa\) and \(k-r\) weights at one, the remaining coordinates arbitrary admissible weights. At the endpoints,
\[
\boxed{\mathcal M_{n,1}(\kappa)=\frac{n\kappa}{\kappa+n-1},
\qquad\mathcal M_{n,\infty}(\kappa)=1.}
\tag{4}
\]
For fixed \(1<p<\infty\) and \(\kappa>1\), the optimal profile remains uniformly bounded as the dimension grows, and its *exact limiting constant* is
\[
\boxed{\lim_{n\to\infty}\mathcal M_{n,p}(\kappa)=
\mathcal K_p(\kappa)
=\frac{(q-1)^{1-1/q}}q
\frac{\kappa^q-1}
{(\kappa-1)^{1/q}(\kappa^q-\kappa)^{1-1/q}}.}
\tag{5}
\]
The unique limiting fraction of maximal weights is
\[
\theta_*=
\frac{\kappa^q-1-q(\kappa-1)}
{(q-1)(\kappa^q-1)(\kappa-1)}\in(0,1).
\tag{6}
\]
For example \(\mathcal K_2(\kappa)=(\kappa+1)/(2\sqrt\kappa)\), the classical Kantorovich factor. The assertion of interest is its *sharp realization and finite-dimensional geometry by a nonlinear isotonic fit*, not novelty of that scalar inequality.

## Assumptions and scope

All vectors, weights, and regression outputs are real and finite-dimensional. Every weight is strictly positive, and the convex order cone consists of nondecreasing sequences. The unique optimizer exists because the positive diagonal quadratic objective is strictly convex and coercive. The Lipschitz modulus is the supremum over all distinct data vectors \(x,z\in\mathbb R^n\). For the weight-contrast optimization only, multiply all weights by a common constant so that they range in \([1,\kappa]\); this does not change the regression map. The exponents \(p=1,\infty\) refer to input and output norms, not to a change in the regression objective.

## Proof

**1. Local block structure.** The weighted pooled-adjacent-violators principle partitions the unique fitted sequence into consecutive constant blocks. On each maximal block \(B\), the fitted level is the weighted mean \(\mu_B(x)=\sum_{i\in B}w_ix_i/W_B\). Indeed, the different fitted levels at neighboring blocks have strict gaps, so one can perturb each common level in both directions without violating the order; scalar quadratic stationarity gives the weighted mean. Thus \(\Pi_w\) agrees at each point with one of finitely many linear maps \(J_{\mathcal B}\), indexed by consecutive-block partitions \(\mathcal B\), taking weighted block means. Uniqueness and standard strongly convex minimization imply that \(\Pi_w\) is continuous. Moreover, the quadratic active-set/KKT system shows it is continuous piecewise linear: within each partition chamber, every block mean is linear and all feasibility and complementary inequalities are linear in the data. Restriction to any line segment can be split into finitely many linear pieces, apart from harmless boundary-contained subsegments. Alternatively, a continuous finite selection of uniformly Lipschitz maps is uniformly Lipschitz along every segment. Hence the global modulus is bounded by the largest \(\ell_p\) operator norm of any block-partition map.

**2. Exact partition norm.** On a nonempty block \(B\) of size \(k\), its rank-one averaging map is
\[
J_Bh=\frac{\sum_{i\in B}w_ih_i}{W_B}\,\boldsymbol1_B.
\]
Hölder duality, with both endpoint conventions, gives
\[
\|J_B\|_{\ell_p(B)\to\ell_p(B)}=
\frac{k^{1/p}\|w_B\|_q}{W_B}.
\]
A direct sum of such maps on disjoint blocks has norm equal to the maximum block norm, including \(p=\infty\). Thus the right side of (1) is an upper bound.

**3. Every block is locally realizable.** Fix a chosen consecutive block \(B=\{a,\ldots,b\}\) of size at least two. Set \(x_i=-i\) on \(B\), with weighted mean \(\bar x_B\); choose the coordinates to its left strictly increasing and uniformly far below \(\bar x_B\), and those to its right strictly increasing and uniformly far above \(\bar x_B\). For strictly decreasing data inside \(B\), each proper prefix has weighted mean greater than the full-block mean. Consequently the KKT prefix multipliers for a wholly pooled fit on \(B\) are strictly positive. The external gaps are also strict. These strict inequalities persist under small input perturbations, so \(B\) is exactly one maximal fit block throughout an open neighborhood, and the local derivative there contains precisely the map \(J_B\). Perturb within \(B\) along a Hölder-extremal direction, with zero perturbation elsewhere. This produces pairs of distinct data whose output/input norm ratio is exactly \(\|J_B\|\) for sufficiently small perturbations. A singleton is realized by strictly increasing data and gives ratio one. Maximizing over all \(B\) completes (1).

**4. Exact nonexpansivity cases.** All block weights are positive, so every weighted mean is a convex combination and has \(\ell_\infty\) modulus one; translation by a constant vector gives the matching lower bound. For \(p<\infty\), Hölder gives \(\|w_B\|_q\ge W_B/k^{1/p}\), with equality precisely when the weights on \(B\) are equal (for \(p=1\), the same conclusion follows from \(k\max_B w_i\ge W_B\)). Every adjacent unequal pair yields a strict inequality on its two-element block; if every pair is equal, all weights are equal and all block constants equal one. This proves (2).

**5. Extreme-weight reduction.** Fix \(1<p<\infty\) and a block size \(k\). Write \(F(w)=\|w\|_q/\sum_i w_i\) for \(w_i\in[1,\kappa]\). With every coordinate but one held fixed, this is \((A+t^q)^{1/q}/(B+t)\), where \(A\ge0\) and \(B>0\) collect the other coordinates; for \(k=1\), \(F=1\). Its derivative has the sign of \(Bt^{q-1}-A\), which changes at most once and only from negative to positive. Therefore any coordinatewise maximum occurs at \(t=1\) or \(t=\kappa\); pushing coordinates to endpoints successively yields an extreme-point maximizer. Let \(r\) coordinates take \(\kappa\), the other \(k-r\) take one. The resulting block norm is the expression in (3). A block of any size \(k\le n\) and any such endpoint profile can be placed consecutively, and Step 3 realizes its norm. This proves the exact global envelope.

For \(p=1\), a block of size \(k\ge2\) has norm at most \(k\kappa/(\kappa+k-1)\), attained by exactly one maximal and \(k-1\) minimal weights. This expression increases with \(k\) if \(\kappa>1\), yielding (4) at \(k=n\). When \(\kappa=1\) the value is one. The \(p=\infty\) assertion follows from Step 4.

**6. Dimension-free limit.** For a \(k\)-block containing fraction \(\theta=r/k\) of maximal weights, the expression in (3) simplifies to
\[
F_{p,\kappa}(\theta)=
\frac{\bigl(1+\theta(\kappa^q-1)\bigr)^{1/q}}
{1+\theta(\kappa-1)}.
\]
The union of grids \(\{r/k:0\le r\le k\le n\}\) becomes dense in \([0,1]\), while its associated maxima grow monotonically with \(n\). Therefore \(\mathcal M_{n,p}(\kappa)\uparrow\max_{0\le\theta\le1}F_{p,\kappa}(\theta)\). For \(\kappa>1\), strict Hölder makes \(F>1\) for \(0<\theta<1\), whereas \(F(0)=F(1)=1\). The sign of its derivative is that of the affine function
\[
(\kappa^q-1)-q(\kappa-1)
-(q-1)(\kappa^q-1)(\kappa-1)\theta.
\]
It follows that the maximizer is the unique interior point (6). Substitution and elementary simplification yield exactly (5). The case \(p=2\) reduces to the displayed Kantorovich factor. No uniformity in \(p\) as it approaches its endpoints is asserted.

## Verification

Run `python verify_weighted_iso.py` with Python 3 and its standard library. The script checks weighted pooled-adjacent-violators fits against exact candidate constants and small-perturbation block witnesses over randomized weights and seven norms. It also checks the exact finite weight-contrast envelope, its endpoint formula, and the large-dimension limiting scalar optimization. A successful run prints `WEIGHTED_ISOTONIC_VERIFY_OK 5252`. This is a finite consistency test, not an exhaustive verification of real data, weights, or all dimensions. Steps 1–6 above are the argument for the universal assertions.

## Relationship to prior work

Luss and Rosset (arXiv:1104.1779v1, publicly posted 2011-04-10) develop generalized isotonic regression using block optimality and KKT systems, but do not give sharp input-to-fit Lipschitz moduli under a *fixed weighted quadratic objective measured in ordinary* \(\ell_p\). Németh and Németh (arXiv:1503.08458v1) study isotonic and order-preserving Hilbert projections, including weighted quadratic formulations, without the heterogeneous-weight amplification profile (1)–(6). Kyng, Rao, and Sachdeva (arXiv:1507.00710v1) give algorithms for isotonic regression with various loss exponents, not the sharp perturbation constant of one fixed weighted least-squares map. Yang and Barber (arXiv:1706.01852) establish \(\ell_p\)-contractivity of *unweighted* least-squares isotonic regression, corresponding to the all-equal-weight case of (1), and do not imply (1)–(6) with unequal weights.

The rank-one block norm from Hölder duality and the classical Kantorovich factor are acknowledged antecedents. A known unweighted metric projection with a nonquadratic \(\ell_p\) objective has a different sensitivity law and cannot imply this one by merely changing notation. The new content claimed here is the *global nonlinear, all-block exact formula*, its equality classification, and its sharp finite- and infinite-dimension heterogeneity envelopes, not those standard scalar inequalities in isolation.

## Limitations

Only real data on a finite totally ordered chain and strictly positive diagonal least-squares weights are treated. There is no claim about graph orders, complex inputs, general nonquadratic objectives, continuum isotonic fits, or stability under simultaneous perturbations of the weights. The finite-dimensional envelope concerns weights in a fixed contrast interval; its limiting formula is pointwise for fixed \(1<p<\infty\) and fixed \(\kappa>1\). The general weighted-isotonic sensitivity literature and classical contractive projection theory leave a residual possibility of equivalent earlier results under other terminology. There has been no independent mathematical or historical-priority audit.

## References

1. R. Luss and S. Rosset, *Generalized Isotonic Regression*, arXiv:1104.1779v1, first posted 10 April 2011. https://arxiv.org/abs/1104.1779 .
2. A. B. Németh and S. Z. Németh, *Isotonic Regression and Isotonic Projection*, arXiv:1503.08458v1, first posted 29 March 2015. https://arxiv.org/abs/1503.08458 .
3. R. Kyng, A. Rao and S. Sachdeva, *Fast, Provable Algorithms for Isotonic Regression in all* \(\ell_p\) *Norms*, arXiv:1507.00710v1, first posted 2 July 2015. https://arxiv.org/abs/1507.00710 .
4. F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852, first posted 2017. https://arxiv.org/abs/1706.01852 .
5. Q. F. Stout, *Weighted* \(L_\infty\) *isotonic regression*, Journal of Computer and System Sciences 91 (2018), 69–81; DOI:10.1016/j.jcss.2017.09.001. This treats a weighted maximum-error regression objective, not the quadratic map above.
