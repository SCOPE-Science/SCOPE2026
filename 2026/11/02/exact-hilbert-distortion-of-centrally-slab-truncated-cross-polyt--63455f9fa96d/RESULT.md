# Exact Hilbert distortion of centrally slab-truncated cross-polytopes

## Finding
For every integer \(n\ge2\) and real \(\tau>0\), let the real normed space \(X_{n,\tau}\) be \(\mathbb R^n\) with
\[
N_{n,\tau}(x)=\max\left\{\|x\|_1,\ \tau\left|\sum_{i=1}^n x_i\right|\right\}.
\]
Its Banach--Mazur distance to \(\ell_2^n\), optimized over **all** invertible real linear coordinate changes, is exactly
\[
\boxed{d_{\rm BM}(X_{n,\tau},\ell_2^n)^2=
\begin{cases}
n,&0<\tau\le1,\\[2mm]
\displaystyle\frac{n+2}{2}+\frac{n-2}{2\tau^2},&\tau\ge1,\ n\text{ even},\\[3mm]
\displaystyle\frac{n\bigl((n^2+2n-1)\tau^2+n^2-2n-1\bigr)}{2(n^2\tau^2-1)},&\tau\ge1,\ n\text{ odd}.
\end{cases}}
\]
The branches agree at \(\tau=1\). For \(\tau\ge1\), a Banach--Mazur-optimal Hilbertian quadratic norm is, up to scaling,
\[
H_{n,\tau}(x)^2=\sum_{i=1}^n x_i^2+
\frac{n(\tau^2-1)}{n^2-\delta_n}
\left(\sum_{i=1}^n x_i\right)^2,
\qquad \delta_n=\begin{cases}0,&n\text{ even},\\1,&n\text{ odd}.\end{cases}
\]
Among permutation-invariant quadratic norms, this optimal shape is unique up to scaling. For \(n=2\) the distortion is always \(\sqrt2\). For each \(n\ge3\), it decreases strictly as \(\tau\) runs from \(1\) to infinity, and its limiting square is \((n+2)/2\) when \(n\) is even, and \((n+2-1/n)/2\) when \(n\) is odd. Thus an increasingly narrow sum-coordinate slab improves the optimal Hilbert distortion but leaves a nonzero, parity-dependent finite-dimensional gap.

## Assumptions and scope
All coordinates and Hilbert spaces are **real**. The \(\ell_1\) norm is \(\|x\|_1=\sum_i|x_i|\). The Banach--Mazur distance is \(\inf_T\|T\|\|T^{-1}\|\), where \(T:X_{n,\tau}\to\ell_2^n\) ranges over linear isomorphisms. Equivalently its square is the smallest \(R\) for which some positive definite quadratic form \(Q\), after positive rescaling, satisfies \(N_{n,\tau}(x)^2\le Q(x)\le R N_{n,\tau}(x)^2\) for all real \(x\). The unit ball for \(\tau>1\) is the \(\ell_1\) cross-polytope intersected with the central slab \(\left|\sum_i x_i\right|\le1/\tau\). At \(\tau\le1\), the slab constraint is redundant and the norm is exactly \(\ell_1\).

## Proof
**1. Global symmetry reduction, with no restriction on the isomorphism.** Suppose \(Q\) is any positive definite quadratic form and \(N^2\le Q\le R N^2\). The norm \(N=N_{n,\tau}\) is invariant under all coordinate permutations. Average \(Q\) over those permutations. The inequalities survive averaging, and the averaged quadratic form is positive definite and permutation invariant; it has the form \(Q=aI+b\mathbf1\mathbf1^{\mathsf T}\) with \(a>0\), \(a+nb>0\). Rescaling gives \(Q_t(x)=\|x\|_2^2+t(\sum_i x_i)^2\) for \(t>-1/n\). Consequently the global, not merely symmetric, Banach--Mazur minimum is attained inside this one-parameter family.

**2. Outer quadratic extremum.** Fix \(\tau\ge1\) and put \(p=\tau^2\), \(a_p=(p+1)/2\). The \(N\)-unit ball \(K\) is the intersection of \(B_1^n\) with \(|\sum_i x_i|\le1/\tau\). For \(\tau>1\), all \(2n\) original cross-polytope vertices lie outside the slab; each new vertex lies on an old edge joining \(e_i\) to \(-e_j\) with \(i\ne j\). Conversely every such edge meets the slab boundary and produces a vertex. Thus, up to a sign and permutation, the vertices are
\[
 u e_i-v e_j,\qquad
 u=(1+\tau^{-1})/2,\quad v=(1-\tau^{-1})/2,
 \qquad i\ne j.
\]
At \(\tau=1\), they reduce to \(\pm e_i\). Since \(Q_t\) is convex, its maximum over \(K\) is attained at a vertex; all listed vertices give the same value. It follows, for every \(t>-1/n\), that
\[
A(t):=\sup_{N(x)\le1}Q_t(x)=\frac{a_p+t}{p}.
\]
The formula remains valid at \(\tau=1\).

**3. Inner quadratic extremum.** The inverse matrix of \(Q_t\) is
\[
Q_t^{-1}=I-\frac{t}{1+nt}\mathbf1\mathbf1^{\mathsf T}.
\]
By duality for a Euclidean ellipsoid and \(\|x\|_1=\max_{\varepsilon_i=\pm1}\sum_i\varepsilon_i x_i\),
\[
B(t):=\sup_{Q_t(x)\le1}N(x)^2
=\max\left\{\max_{\varepsilon\in\{\pm1\}^n}\left(n-\frac{t(\sum_i\varepsilon_i)^2}{1+nt}\right),\frac{pn}{1+nt}\right\}.
\]
For \(-1/n<t\le0\), the second entry dominates (because \(p\ge1\)). For \(t\ge0\), the minimum possible squared sign sum is \(\delta_n\), yielding
\[
B(t)=\max\left\{n-\frac{\delta_n t}{1+nt},\frac{pn}{1+nt}\right\}.
\]
The squared distortion of \(Q_t\) is \(R(t)=A(t)B(t)\).

**4. Sharp one-variable minimization.** The entries in the maximum in Step 3 meet at
\[
t_*=\frac{n(p-1)}{n^2-\delta_n}\ge0.
\]
For \(-1/n<t\le t_*\), the active entry is \(pn/(1+nt)\), so
\[
R(t)=\frac{n(a_p+t)}{1+nt},\qquad
R'(t)=\frac{n(1-na_p)}{(1+nt)^2}<0.
\]
For \(t\ge t_*\), the active entry is \(n-\delta_n t/(1+nt)\). If \(n\) is even, \(R(t)=n(a_p+t)/p\) is strictly increasing. If \(n\) is odd (hence \(n\ge3\)), then
\[
R'(t)=\frac{n-a_p+2(n^2-1)t+n(n^2-1)t^2}{p(1+nt)^2}.
\]
The numerator increases for nonnegative \(t\), and at \(t=t_*\) it is at least
\[
 n-a_p+2(n^2-1)t_*=
 \frac{(4n-1)p-2n-1}{2}\ge n-1>0.
\]
Thus \(R\) is strictly decreasing up to \(t_*\) and strictly increasing afterward. Its unique symmetric optimum is \(t_*\); evaluating \(R(t_*)\) gives the two stated parity-dependent rational expressions. Step 1 proves their **global** optimality over every real Hilbertian pullback. For \(\tau\le1\), the norm equals \(\ell_1^n\). Average any admissible ellipsoid sandwich over the full signed-permutation group: the resulting quadratic form is a scalar multiple of \(\|x\|_2^2\). The sharp inequalities \(\|x\|_2\le\|x\|_1\le\sqrt n\|x\|_2\), with both endpoint equalities achieved, therefore give globally optimal squared distance \(n\).

**5. Endpoint behavior.** The formula is constant \(2\) in dimension \(n=2\). For even \(n\ge4\), its squared value drops from \(n\) to \((n+2)/2\) as \(p\) rises from \(1\) to infinity. For odd \(n\ge3\), differentiating the stated rational expression gives a strictly negative derivative for \(p\ge1\) (its numerator is proportional to \(-n(n^4-2n^3+2n-1)\), and \(n^4-2n^3+2n-1>0\) for \(n\ge3\)). Its limit is \((n+2-1/n)/2\). This proves the threshold, strictness and limits. The half-integer parity effect comes from the smallest possible signed coordinate sum, zero for even \(n\) and one in absolute value for odd \(n\).

## Verification
The complete proof is symbolic and holds for every integer \(n\ge2\) and every real \(\tau>0\). The standalone Python 3 program in `artifacts/verify_slab.py` independently computes the outer extremum from explicitly enumerated polytope vertices and the inner extremum from all sign vectors, with exact rational arithmetic. It checks the closed formula in \(60\) rational cases across dimensions \(2\) through \(11\), and compares the candidate ellipsoid with nine exact rational alternatives in each case. It prints `CHECK_OK exact_slab_cases= 60 exact_parameter_comparisons= 600`. This finite replay cannot establish the universal result, which is supplied by the proof above.

## Relationship to prior work
Kobos and Varivoda, arXiv:2305.06427v1 (first public 2023-05-10), study the Banach--Mazur distance between the cube and cross-polytope in dimensions three and four. Their introduction and theorem summaries, together with a searchable full-text comparison, do not yield the present exact ellipsoid for a cross-polytope **truncated by a coordinate-sum slab** in arbitrary dimension. Vasil'eva, arXiv:2303.13147v1 (first public 2023-03-23), studies Kolmogorov widths of intersections of mixed-norm balls, a different invariant and a different family of bodies. A later general treatment of distance ellipsoids by Grundbacher and Kobos (2025) gives useful characterizations but not this specific parity-dependent parameter law. A public research record on quadratic \(\ell_1\)–\(\ell_\infty\) mixtures treats \((\|x\|_\infty^2+t\|x\|_1^2)^{1/2}\), which is different from the maximum of \(\|x\|_1\) and the rank-one sum functional here. The standard \(\sqrt n\) bound on the \(\ell_1^n\) endpoint is not presented as new. No directly implying earlier formula was identified in the consulted sources; this is **not** a proof that no such formula exists elsewhere.

## Limitations
This is a real finite-dimensional result, not a complex or infinite-dimensional theorem. The shape of an optimal **permutation-invariant** ellipsoid is unique up to scaling, but no uniqueness is asserted among all nonsymmetric optimal ellipsoids. The endpoint \(\tau\le1\) is classical. The material inspected from two potentially relevant 2023 primary papers covered their theorem statements and relevant early sections, not every proof page; an overlooked equivalent old result under a different convex-geometric name remains possible. The standalone finite verification is corroborative only. No independent mathematical audit has been performed.

## References
1. T. Kobos and M. Varivoda, “On the Banach–Mazur Distance in Small Dimensions,” arXiv:2305.06427v1, 2023-05-10, https://arxiv.org/abs/2305.06427.
2. A. A. Vasil'eva, “Estimates for the Kolmogorov widths of an intersection of two balls in a mixed norm,” arXiv:2303.13147v1, 2023-03-23, https://arxiv.org/abs/2303.13147.
3. F. Grundbacher and T. Kobos, “On certain extremal Banach–Mazur distances and Ader's characterization of distance ellipsoids,” first online 2025-12-04, DOI 10.1112/mtk.70062.
4. “Exact Hilbert distortion of quadratic \(\ell_1\)–\(\ell_\infty\) mixtures,” public mathematical record e46a89ab87db (2026), a comparison concerning a different quadratic norm family.
