# Exact interval-projection norms for weighted Cantor Lipschitz-free spaces

## Finding
Let \(\alpha=(\alpha_j)_{j\geq1}\) be any strictly positive summable real sequence. On the binary Cantor space \(K=\{0,1\}^{\mathbb N}\), equip the base point \(o=(0,0,\ldots)\) and metric
\[
 d_\alpha(x,y)=\sum_{j\geq1}\alpha_j|x_j-y_j|.
\]
Let \(p_n\) retain the first \(n\) binary coordinates and replace the others with zero, and let \(P_n\) be the induced linear operator on the **real** Lipschitz-free space \(\mathcal F(K,d_\alpha)\). Put \(P_0=0\) and \(P_\infty=I\). For all integers \(1\leq n<m\leq\infty\), set
\[
 a_n=\min_{1\leq j\leq n}\alpha_j,\qquad
 B_{n,m}=\sum_{n<j\leq m}\alpha_j,
\]
where \(B_{n,\infty}=\sum_{j>n}\alpha_j\). Then the **entire canonical interval-projection norm profile** is
\[
 \boxed{\ \|P_m-P_n\|=\max\left\{1,\ 2\min\left(1,\frac{B_{n,m}}{a_n}\right)\right\}.\ }
\]
For \(1\leq m\leq\infty\), \(\|P_m-P_0\|=1\). The \(P_n\) form a nested sequence of norm-one finite-rank projections, with \(\operatorname{rank}P_n=2^n-1\) for finite positive \(n\), and \(P_n\to I\) strongly. Their differences \(Q_n=P_n-P_{n-1}\) give a monotone finite-dimensional Schauder decomposition with \(\operatorname{rank}Q_n=2^{n-1}\).

In particular, every interval projection is contractive, equivalently this canonical decomposition is bimonotone, **if and only if**
\[
 \boxed{\ \sum_{j>n}\alpha_j\leq \frac12\min_{1\leq j\leq n}\alpha_j\quad\text{for every }n\geq1.\ }
\]
The norm formula and its endpoints require no monotonicity assumption on the weights.

## Assumptions and scope
The field is real; \(K\) is the full infinite binary product with its weighted \(\ell_1\) metric. Every \(\alpha_j\) is positive and \(\sum_j\alpha_j<\infty\); the weights need not decrease. The free space is the completion of the linear span of evaluation molecules \(\delta_x\), where \(\delta_o=0\), equipped with the dual norm from the unit ball of pointed Lipschitz functions. The norm of \(\delta_x-\delta_y\) is \(d_\alpha(x,y)\). The interval \((n,m]\) is inclusive at \(m\), and the special upper index \(m=\infty\) denotes the identity rather than a finite-rank projection.

## Proof
**1. Coordinate filtration.** The map \(p_n\) is base-point-preserving and \(1\)-Lipschitz, since dropping coordinates cannot increase their weighted \(\ell_1\) distance. It fixes each point of the finite set \(K_n=p_n(K)\), which contains \(2^n\) points, so its linearization \(P_n\) is a projection with norm exactly one. Independence of distinct nonbasepoint evaluation vectors on a finite metric space gives \(\operatorname{rank}P_n=2^n-1\). The identities \(p_mp_n=p_np_m=p_{\min(m,n)}\) transfer to the linearizations. For every \(x\in K\),
\[
 \|\delta_x-P_n\delta_x\|=d_\alpha(x,p_nx)\leq\sum_{j>n}\alpha_j\longrightarrow0.
\]
Uniform boundedness of the projections and density of the evaluation span imply strong convergence. Thus \(Q_n=P_n-P_{n-1}\) are mutually annihilating finite-rank projections whose sum converges strongly to the identity. The rank difference is \(2^{n-1}\).

**2. Four-atom transportation lemma.** For any four points \(A,B,C,D\) in a metric space, including possible coincidences, the real free-space norm satisfies
\[
 \|\delta_A+\delta_D-\delta_B-\delta_C\|
 =\min\{d(A,B)+d(D,C),\ d(A,C)+d(D,B)\}.
\]
Indeed, a free-space norm of a finitely supported zero-mass signed measure equals its minimum transport cost. In this two-source, two-sink instance, all transport plans have the form of a \(2\)-by-\(2\) bistochastic matrix. The cost is affine in its single free entry, so a minimum occurs at one of the two permutation matrices, giving the two displayed matchings. This transport characterization follows directly from the molecular norm (replace any intermediate chain of transported mass by its endpoints using the triangle inequality) and the Lipschitz dual, equivalently finite-dimensional transport linear-program duality. The statement remains valid when points coincide, by cancellation or by the same coupling argument.

**3. Exact upper bound.** Fix \(1\leq n<m\leq\infty\) and \(x\ne y\) in \(K\). Decompose their weighted distance into the first \(n\) coordinates \(p\), the next \((n,m]\) coordinates \(h\), and the coordinates after \(m\), \(e\), so that \(d_\alpha(x,y)=p+h+e\), with \(e=0\) for \(m=\infty\). Let \(u=p_nx\), \(v=p_ny\), \(X=p_mx\), \(Y=p_my\), with \(p_m=\mathrm{id}\) if \(m=\infty\). Let \(a=d_\alpha(X,u)\) and \(b=d_\alpha(Y,v)\). These are the masses of the nonzero block coordinates of \(x\) and \(y\), so \(a,b\leq B_{n,m}\). The four-atom formula applied to
\[
 (P_m-P_n)(\delta_x-\delta_y)=\delta_X+\delta_v-\delta_u-\delta_Y
\]
gives the **exact molecule-image norm**
\[
 \|(P_m-P_n)(\delta_x-\delta_y)\|
 =\min\{a+b,\,2p+h\}.
\]
If \(p=0\), the image is \(\delta_X-\delta_Y\), with norm \(h\leq d_\alpha(x,y)\). If \(p>0\), at least one of the first \(n\) coordinates differs, so \(p\geq a_n\), whence
\[
 \frac{\|(P_m-P_n)(\delta_x-\delta_y)\|}{d_\alpha(x,y)}
 \leq\min\left\{\frac{2B_{n,m}}{p},\,2\right\}
 \leq 2\min\left\{1,\frac{B_{n,m}}{a_n}\right\}.
\]
A bounded linear map on a free space has norm equal to the supremum of these ratios over all nontrivial molecules. We obtain the stated upper bound, including the floor at one.

**4. Attaining both lower bounds.** First choose \(x,y\) that differ only in one coordinate \(j\in(n,m]\). Then \(p=0\), \(e=0\), and the image molecule equals the input molecule, giving ratio exactly one. Next choose a coordinate \(i\leq n\) with \(\alpha_i=a_n\); let \(x,y\) differ only in coordinate \(i\) among their first \(n\) coordinates, give both points the same value \(1\) in every coordinate of \((n,m]\), and set every coordinate above \(m\) to zero. For \(m=\infty\), this means all subsequent coordinates are \(1\), which is a legitimate point because the weights are summable. Here \(p=a_n\), \(h=e=0\), and \(a=b=B_{n,m}\). The four-atom formula gives ratio
\[
 \frac{2\min\{B_{n,m},a_n\}}{a_n}
 =2\min\left\{1,\frac{B_{n,m}}{a_n}\right\}.
\]
This proves equality for every finite or infinite interval. For \(n=0\), \(P_m\) is already a norm-one projection for finite positive \(m\), and \(P_\infty=I\).

**5. Bimonotonicity criterion.** All initial projections have norm one. For a fixed \(n\), the interval weight \(B_{n,m}\) increases to \(B_{n,\infty}\); the exact formula shows that \(\|I-P_n\|=1\) if and only if \(B_{n,\infty}\leq a_n/2\). This condition for all \(n\) is equivalent to contractivity of all interval projections. In particular, the single-level projection satisfies \(\|Q_{n+1}\|=\max\{1,2\min(1,\alpha_{n+1}/a_n)\}\).

## Verification
The argument proves infinitely many intervals for every positive summable real weight sequence; no finite check is used to extrapolate this result. The included `check_intervals.py` forms the complete finite weighted binary cube, enforces every \(1\)-Lipschitz constraint as a linear inequality, fixes the potential at the base point, and solves a dual linear program for every ordered pair of points and every interval. It checks \(48\) exact finite-cube interval norms across six ordered and nonmonotone weight configurations, with maximum numerical discrepancy below \(9\cdot10^{-16}\). Run `python check_intervals.py` with Python 3, NumPy, and SciPy installed; the deterministic output is included as `check_intervals_results.txt`.

As a useful boundary check, for geometric weights \(\alpha_j=r^j\) with \(0<r<1\), each single-level \(Q_{n+1}\) is contractive if and only if \(r\leq1/2\), whereas **all tails and intervals** are contractive if and only if \(r\leq1/3\), because \(B_{n,\infty}/a_n=r/(1-r)\). In particular, at \(r=1/2\) every single-level block is contractive while every tail projection \(I-P_n\) has norm two.

## Relationship to prior work
Talimdjioski studied approximation properties as the compatible metric on Cantor space varies, including a residual metric-approximation-property result. Doucha and Kaufmann previously established the metric approximation property for all compact metrizable groups with compatible invariant metrics, **which already covers the MAP assertion here**, since this weighted Hamming cube is a compact group with invariant metric. Lancien and Pernecká established monotone finite-dimensional decompositions for free spaces over \(\ell_1\) and finite-dimensional \(\ell_1\), using interpolation operators. Cúth and Doucha studied projections induced by compact group actions. These are relevant existence and projection mechanisms; their inspected statements and constructions do not determine the exact norms of **every prescribed coordinate interval projection** in this weighted Cantor family. In particular, mere contractivity of \(P_n\) yields only the general upper bound two for their differences, without the sharp weight-dependent formula or bimonotonicity threshold.

## Limitations
The quantitative formula applies only to the particular **coordinate-truncation filtration** on full binary products with a summable weighted Hamming metric. It does not give minimal projection constants over all decompositions, an unconditional basis, or a characterization of all compatible Cantor metrics. The metric approximation property is acknowledged as previously known for this group-invariant subclass. The norm formula has an analytic proof, but its originality relative to unindexed literature has not received an independent assessment.

## References
1. F. Talimdjioski, *Lipschitz-free spaces over Cantor sets and approximation properties*, arXiv:2305.07591v1 (first public version 2023-05-12), https://arxiv.org/pdf/2305.07591.
2. M. Doucha and P. L. Kaufmann, *Approximation properties in Lipschitz-free spaces over groups*, arXiv:2005.09785v2 (2021), Theorem 3.5, https://arxiv.org/pdf/2005.09785.
3. G. Lancien and E. Pernecká, *Approximation properties and Schauder decompositions in Lipschitz-free spaces*, arXiv:1207.1583v1 (2012), Theorem 3.1, https://arxiv.org/pdf/1207.1583.
4. M. Cúth and M. Doucha, *Projections in Lipschitz-free spaces induced by group actions*, arXiv:2104.11519v1 (2021), https://arxiv.org/pdf/2104.11519.
