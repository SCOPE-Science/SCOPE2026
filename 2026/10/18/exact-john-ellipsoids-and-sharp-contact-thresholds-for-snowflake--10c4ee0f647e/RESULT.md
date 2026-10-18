# Exact John ellipsoids and sharp contact thresholds for snowflaked bipartite Lipschitz dual balls

## Finding
For integers \(2\le p\le q\), set \(N=p+q\) and \(d=N-1\). Partition \(N\) labelled points into \(A\) of size \(p\) and \(B\) of size \(q\). At parameter \(1\le t\le2\), distances between distinct points in the same class equal \(t\), and cross-class distances equal \(1\). Let \(Q_{p,q,t}\) be the unit ball of the **real Lipschitz dual**, represented as zero-sum vertex potentials in the intrinsic Euclidean hyperplane \(H=\mathbf 1^\perp\subset\mathbb R^N\).

Write \(P_A\) and \(P_B\) for the orthogonal projections onto the within-class zero-sum subspaces of dimensions \(p-1\) and \(q-1\), and \(P_C\) for the projection onto the remaining one-dimensional between-class contrast. Put
\[
 T=\frac{t^2}{2},\quad \alpha=\frac{p-1}{p},\quad\beta=\frac{q-1}{q},\quad\gamma=\frac{N}{pq},\qquad
 T_1=\frac{q}{2q-1},\quad T_2=\frac{q}{N-1}.
\]
Then the unique maximum-volume inscribed ellipsoid is
\[
 E_{p,q,t}=\{x\in H:\langle x,S^{-1}x\rangle\le1\},\qquad S=aP_A+bP_B+cP_C,
\]
where \(S^{-1}\) means the inverse on \(H\), and the squared semiaxes are
\[
 \boxed{
 (a,b,c)=\begin{cases}
 \left(T,T,\dfrac{1-(\alpha+\beta)T}{\gamma}\right),&\frac12\le T\le T_1,\\[5pt]
 \left(1-\beta T,T,\dfrac qN(1-\beta T)\right),&T_1\le T\le T_2,\\[5pt]
 \left(\dfrac p{N-1},\dfrac q{N-1},\dfrac{pq}{N(N-1)}\right),&T_2\le T\le2.
 \end{cases}}
\]
The formulas agree at their boundaries, including \(T_1=T_2\) when \(p=q\). In the intrinsic Euclidean measure on \(H\), the exact volume is
\[
 \boxed{\operatorname{vol}_{d}(E_{p,q,t})=\frac{\pi^{d/2}}{\Gamma(1+d/2)}\sqrt{a^{p-1}b^{q-1}c}.}
\]
Every cross-class inequality is tangent to the ellipsoid. The within-\(A\) inequalities are tangent exactly for \(T\le T_1\), and the within-\(B\) inequalities exactly for \(T\le T_2\). At the transition values, tangent constraints may have zero optimality multiplier. Thus the two distinct contact transitions occur for \(p<q\), and coincide when \(p=q\).

**Exact saturation:** the John ellipsoid becomes independent of \(t\) precisely at
\[
 \boxed{t_*=\sqrt{\frac{2q}{p+q-1}}<2.}
\]
It then equals the John ellipsoid for the unit-edge complete bipartite graph. In contrast, the underlying Lipschitz balls are strictly increasing with \(t\) throughout \([1,2]\). The John-ellipsoid volume increases strictly before \(t_*\) and is constant thereafter.

## Assumptions and scope
The metric is real, finite, symmetric and satisfies the triangle inequality because \(t\le2\). A vertex potential is represented by the unique translation having total coordinate sum zero. Thus
\[
 Q_{p,q,t}=\{x\in H:|x_i-x_j|\le t\ (i,j\text{ in the same class}),\ |x_i-x_j|\le1\ (i,j\text{ in different classes})\}.
\]
The Euclidean structure here is the restriction of the standard inner product of \(\mathbb R^N\), not the generally different Euclidean structure obtained after arbitrarily anchoring one vertex. All volumes, projectors and ellipsoids refer to that fixed normalization. Both class sizes are at least two; exchanging class names allows \(p\le q\). For \(t=1\) the metric is equilateral; for \(t=2\) it is the shortest-path metric of \(K_{p,q}\).

More explicitly, \(P_A\) has its \(A\)-by-\(A\) block \(I_p-\mathbf1_p\mathbf1_p^{\mathsf T}/p\) and zero elsewhere; \(P_B\) is analogous. With \(v=(\mathbf1_p/p,-\mathbf1_q/q)\in H\), one has \(P_C=vv^{\mathsf T}/\gamma\), and \(P_A+P_B+P_C=I_H\). Hence \(a,b,c\) are directly the squared Euclidean semiaxes, with multiplicities \(p-1,q-1,1\), respectively.

## Proof
**1. Reduction to three variables without assuming a symmetric competitor.** The full-dimensional compact convex body \(Q_{p,q,t}\) is centrally symmetric. Its maximal inscribed ellipsoid is unique, so central symmetry forces its center to be the origin. Uniqueness also forces invariance under each permutation in \(S_p\times S_q\). The three subspaces described above are pairwise inequivalent invariant summands for this group. Every invariant symmetric positive definite operator on \(H\) consequently equals \(S=aP_A+bP_B+cP_C\) for unique positive \(a,b,c\). These deductions apply to the globally optimal ellipsoid, not only to ellipsoids assumed invariant at the outset.

For an origin-centered ellipsoid with shape \(S\), the maximum of \(|\langle e_i-e_j,x\rangle|\) is \(\sqrt{(e_i-e_j)^{\mathsf T}S(e_i-e_j)}\). Direct use of the three projector blocks gives squared support \(2a\) on within-\(A\) differences, \(2b\) on within-\(B\) differences, and \(\alpha a+\beta b+\gamma c\) on any cross-class difference. Its containment in \(Q_{p,q,t}\) is therefore equivalent to
\[
 0<a\le T,\quad0<b\le T,\quad c>0,\quad\alpha a+\beta b+\gamma c\le1.
\]
Its Euclidean volume is the unit-ball volume multiplied by \(\sqrt{\det_H S}\). Thus maximizing volume is equivalent to maximizing the strictly concave function
\[
 F(a,b,c)=(p-1)\log a+(q-1)\log b+\log c
\]
over this convex feasible domain. Since the objective increases with \(c\), every maximizer has the cross constraint at equality.

**2. Exact Karush–Kuhn–Tucker solution.** Use multiplier \(\lambda\ge0\) for the cross constraint and \(\mu_A,\mu_B\ge0\) for the upper bounds on \(a,b\). Stationarity is
\[
 \frac{p-1}{a}=\lambda\alpha+\mu_A,\quad
 \frac{q-1}{b}=\lambda\beta+\mu_B,\quad
 \frac1c=\lambda\gamma.
\]
Complementarity demands \(\mu_A(T-a)=\mu_B(T-b)=0\). If both upper bounds are active, \(a=b=T\) and \(c=[1-(\alpha+\beta)T]/\gamma\); the resulting multipliers are nonnegative exactly until the smaller threshold \(T_1=q/(2q-1)\) is reached (the bound for the second class is \(p/(2p-1)\), no smaller because \(p\le q\)). The first class then becomes inactive. With \(\mu_A=0\) and \(b=T\), stationarity yields \(\lambda=p/a\), \(c=qa/N\) and \(a=1-\beta T\); the remaining multiplier \(\mu_B\) is nonnegative precisely until \(T_2=q/(p+q-1)\). For \(T\ge T_2\), both upper-bound multipliers vanish. Stationarity and the cross equality now give \(\lambda=d\), \(a=p/d\), \(b=q/d\) and \(c=pq/(Nd)\). These values obey \(a\le T\) and \(b\le T\). All three positive triples satisfy the KKT conditions in their stated ranges. Strict concavity makes them the unique invariant optimizer, hence the unique global John ellipsoid. The determinant formula proves the displayed volume.

**3. Contact and saturation.** The three squared support values are \(2a,2b,1\). The exact equalities \(a=T\) and \(b=T\) give the two contact thresholds, including equality at their respective boundaries. Once \(T\ge T_2\), all three semiaxes are constant, so both shape and volume equal those at \(t=2\). For \(T<T_2\), the upper-bound multipliers give a strictly positive directional derivative of the optimal log-volume in \(T\) on the nonempty regimes, proving the saturation threshold is sharp.

**4. The bodies themselves do not saturate.** For any \(1\le t<t'\le2\), choose \(s\in(t,t')\). Give two vertices of \(A\) potential values \(s/2,-s/2\) and all other vertices potential zero, then subtract the global mean. Every cross-class difference is at most \(s/2\le1\), while the largest within-\(A\) difference is \(s\). This potential belongs to \(Q_{p,q,t'}\) but not \(Q_{p,q,t}\). Therefore all inclusions are strict even throughout the entire ellipsoid-saturation interval. \(\square\)

## Verification
The accompanying standalone `check_john.py` runs with Python's standard library and no external data. It constructs the three orthogonal projector blocks in exact rational arithmetic, checks positive semiaxes, every pairwise squared support bound, cross-contact equalities and KKT stationarity, dual feasibility and complementarity. In 2,580 rational parameter configurations with \(2\le p\le11\), \(p\le q\le13\), including exact transition points and interior samples in all regimes, it reports `PASS 2580 full rational matrix, support, and KKT checks; phases {1: 900, 2: 780, 3: 900}`. These finite checks are not a proof for all integer sizes and all real parameters; the group-invariance and strict-concavity proof above supplies the general argument.

## Relationship to prior work
Alexander, Fradelizi, García-Lirola and Zvavitch (arXiv:1911.10642) give the basic finite-metric Lipschitz-free polytope framework and analyze volume products, extreme molecules and Hanner structures. Cobollo, Guirao and Montesinos (arXiv:2304.13183) study a different Banach invariant, the numerical index, and furnish a functional-analytic setting with MSC 46B20. Suliman and Weinstein (arXiv:2302.05966) develop general graph-optimal-design and ellipsoid machinery; the symmetry reduction and logarithmic determinant method here use standard convex optimization principles rather than claiming them as new.

A closely pertinent published result, *Sharp facet-count transitions for snowflaked complete bipartite metrics* (2026), treats exactly the metric family used here, proving an endpoint/interior facet-count classification. Its inspected full result does not compute an inscribed ellipsoid. A separate published result, *Maximal Hilbert distortion for complete-bipartite transportation spaces* (2026), computes a Banach–Mazur distance at \(t=2\), and its explicit invariant form supports the known endpoint; that endpoint is **not** independently claimed as novel here. The present claim is the continuously parameterized optimal ellipsoid, its two contact thresholds and its strict pre-endpoint saturation. Other nearby ellipsoid classifications for tripartite symmetric edge polytopes concern different graph families and optimizations.

## Limitations
This theorem concerns **real** finite metric spaces of exactly two nontrivial classes, a common within-class distance \(1\le t\le2\), and the *intrinsic zero-sum Euclidean* John ellipsoid. It does not classify ellipsoids for arbitrary multipartite or independently weighted classes, give a Banach–Mazur optimum over all ellipsoid embeddings, or calculate the body's volume. A change to an arbitrary anchored Euclidean coordinate normalization changes the ellipsoid spectrum and volume. General optimization tools, endpoint geometry and the same-metric facet classification are prior work. Although targeted records and relevant primary texts were compared, an equivalent ellipsoid formula in unindexed literature cannot be excluded without external bibliographic validation. No independent scientific audit has been performed.

## References
1. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first publicly posted 2019-11-24), https://arxiv.org/abs/1911.10642 .
2. A. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966 (first publicly posted 2023-02-12), https://arxiv.org/abs/2302.05966 .
3. Ch. Cobollo, A. J. Guirao and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183 (first publicly posted 2023-04-25; 2020 MSC 46B20), https://arxiv.org/abs/2304.13183 .
4. *Sharp facet-count transitions for snowflaked complete bipartite metrics*, published mathematical result (2026-10-11); full result inspected for the same objects and invariant comparison.
5. *Maximal Hilbert distortion for complete-bipartite transportation spaces*, published mathematical result (2026-10-11); complete graph-metric endpoint proof inspected.
