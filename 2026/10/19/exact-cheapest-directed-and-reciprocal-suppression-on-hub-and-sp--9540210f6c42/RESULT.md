# Exact cheapest directed and reciprocal suppression on hub-and-spoke transmission networks

## Finding

A nonnegative next-generation matrix whose off-diagonal mixing graph is a weighted hub-and-spoke network has an exact, scalar non-supercriticality condition. Under linear costs, the *global* cheapest attenuation differs qualitatively between independent directional controls and enforced reciprocal controls: the former admits a fractional-knapsack solution with at most one partially attenuated spoke, whereas the latter has a unique clipped water-filling solution with no spoke fully severed. When paired directional costs coincide, reciprocity costs at most twice as much, and the factor two is sharp; without that cost symmetry the ratio can be arbitrarily large.

Specifically, for any integer \(m\ge2\), consider the \((m+1)\)-group next-generation matrix

\[
K(x,y)=\begin{pmatrix}
a & b_1x_1 & \cdots & b_mx_m\\
c_1y_1 & d_1 & &0\\
\vdots &&\ddots&\\
c_my_m &0&&d_m
\end{pmatrix}.
\]

Assume \(0\le a<1\), \(0\le d_i<1\), \(b_i,c_i>0\), and independent attenuation factors \(x_i,y_i\in[0,1]\). Set

\[
w_i=\frac{b_ic_i}{1-d_i},\qquad H=1-a,\qquad W=\sum_{i=1}^m w_i,
\]

and suppose \(0<H<W\). Then

\[
\boxed{\rho(K(x,y))\le1\quad\Longleftrightarrow\quad
\sum_{i=1}^m w_i x_i y_i\le H.}
\]

For positive directional unit costs \(p_i,q_i\), minimize \(\sum_i[p_i(1-x_i)+q_i(1-y_i)]\) subject to this threshold. Put \(B=W-H\), \(r_i=1-x_iy_i\), \(s_i=\min\{p_i,q_i\}\). The minimum is exactly the fractional-knapsack value

\[
\boxed{C_{\mathrm{dir}}=\min\biggl\{\sum_i s_i r_i:
0\le r_i\le1,\ \sum_iw_ir_i\ge B\biggr\}.}
\]

Ordering spokes by decreasing \(w_i/s_i\), one optimal policy entirely attenuates the cheaper direction on successively ranked spokes, with at most one partial spoke, leaving the other direction on each spoke unchanged. This is a complete constructive optimization law, including ties and zero transmission factors.

For the physically different policy class requiring \(x_i=y_i=t_i\) on each spoke, put \(h_i=p_i+q_i\). The unique optimizer is

\[
\boxed{t_i=\min\left\{1,\frac{h_i}{2\lambda w_i}\right\},
\qquad \sum_iw_it_i^2=H,}
\]

where \(\lambda>0\) is uniquely determined. Its minimum cost is \(C_{\mathrm{rec}}=\sum_i h_i(1-t_i)\). Every optimal reciprocal factor is *strictly positive*: forcing identical directional attenuation does not make severing one spoke optimal at any positive \(H\).

The sharp quantitative comparison is

\[
C_{\mathrm{dir}}\le C_{\mathrm{rec}},\qquad
p_i=q_i\ \forall i\ \Longrightarrow\ C_{\mathrm{rec}}\le2C_{\mathrm{dir}}.
\]

Both constants one and two are optimal universal endpoints. With unequal directional costs, no universal upper bound on \(C_{\mathrm{rec}}/C_{\mathrm{dir}}\) exists.

## Assumptions and scope

All quantities are dimensionless next-generation coefficients describing expected secondary activity over one infectious/active period, linearized at a disease-free or zero-adoption state. A hub can have within-group reproduction \(a\), each peripheral group has within-group reproduction \(d_i\), and peripheral groups interact with the hub but not directly with each other. Controls affect only the two cross-group transmission coefficients on each spoke. The costs are *specified linear implementation costs*, not inferred empirical expenditure. Independent directional factors are appropriate when susceptibility and infectiousness/influence can be modified separately; reciprocal factors describe a distinct, symmetric attenuation constraint.

The result concerns the condition \(\rho(K)\le1\) for *non-supercritical initial growth*. Equality is critical and is not claimed to imply exponential extinction or absence of infections. The result does not establish nonlinear final epidemic size, prevalence minimization, stochastic outbreak probabilities, or efficacy of particular real-world interventions. The assumptions \(H>0\) and \(W>H\) deliberately exclude trivial already controlled configurations and a hub whose own reproduction is supercritical.

## Proof

**Spectral reduction.** For every real \(z>\max_i d_i\), a block determinant gives

\[
\det(zI-K)=\prod_i(z-d_i)
\left[z-a-\sum_i\frac{b_ic_ix_iy_i}{z-d_i}\right].
\]

The term in brackets is strictly increasing in \(z\ge1\) (its derivative is \(1+\sum_i b_ic_ix_iy_i/(z-d_i)^2>0\)). Its value at \(z=1\) is \(H-\sum_iw_ix_iy_i\). If this value is negative, continuity and divergence of the bracket give a real eigenvalue larger than one. If zero, one is an eigenvalue and no real eigenvalue exceeds one. If positive, no real eigenvalue exceeds one. The spectral radius of every nonnegative matrix is a nonnegative real eigenvalue, including for reducible matrices. This proves the claimed iff criterion without an irreducibility assumption or a hidden strict-positivity condition on controls.

**Independent directional optimum.** For each spoke and all \(x_i,y_i\in[0,1]\),

\[
\begin{aligned}
p_i(1-x_i)+q_i(1-y_i)
&\ge s_i[(1-x_i)+(1-y_i)]\\
&\ge s_i(1-x_iy_i)=s_ir_i.
\end{aligned}
\]

The second inequality is equivalent to \((1-x_i)(1-y_i)\ge0\). Conversely, for every \(r_i\in[0,1]\) equality in both bounds is attained by \((x_i,y_i)=(1-r_i,1)\) when \(p_i\le q_i\), or by \((1,1-r_i)\) otherwise. Thus the matrix optimization is exactly a linear program over reductions \(r_i\). Since \(0<B<W\), positive costs force \(\sum_iw_ir_i=B\) at optimum. Exchanging a small positive weighted reduction from a smaller \(w_i/s_i\) spoke to a larger one never raises cost, so greedy descending ratio order yields a global optimum with at most one \(r_i\) strictly between zero and one. More explicitly, if \(i_1,\ldots,i_m\) is that order and \(j\) is the least index with \(\sum_{k=1}^j w_{i_k}\ge B\), the optimal value is

\[
C_{\mathrm{dir}}=\sum_{k<j}s_{i_k}
+\frac{s_{i_j}}{w_{i_j}}
\left(B-\sum_{k<j}w_{i_k}\right).
\]

**Reciprocal optimum.** Taking \(x_i=y_i=t_i\), the problem is to maximize \(\sum_i h_i t_i\) over the compact convex set \(0\le t_i\le1\), \(\sum_iw_it_i^2\le H\). A strictly feasible positive vector exists, and \(t_i=1\) for all \(i\) is infeasible because \(H<W\). Karush--Kuhn--Tucker conditions are therefore sufficient, and their quadratic-constraint multiplier is strictly positive. For fixed \(\lambda>0\), the strictly concave separable Lagrangian \(\sum_i(h_it_i-\lambda w_it_i^2)\) has the unique box maximizer \(t_i=\min\{1,h_i/(2\lambda w_i)\}\); the lower endpoint never binds because \(h_i>0\). The continuous sum of squares decreases strictly from \(W\) to zero as \(\lambda\) traverses the relevant interval. For \(0<H<W\) it has a unique solution. Strict concavity of this optimizing Lagrangian also establishes uniqueness of the constrained optimizer.

**Sharp price of reciprocity.** A reciprocal profile is also a feasible independent directional profile, so \(C_{\mathrm{dir}}\le C_{\mathrm{rec}}\). If \(p_i=q_i\), start from an optimal independent reduction vector \(r_i\) and choose the feasible reciprocal \(t_i=\sqrt{1-r_i}\). Then

\[
C_{\mathrm{rec}}\le\sum_i2p_i(1-\sqrt{1-r_i})
\le2\sum_ip_ir_i=2C_{\mathrm{dir}}.
\]

For two identical spokes with \(w_i=w>0\), \(2w\le1\), \(p_i=q_i=p>0\), and \(H=2wu\) for \(0<u<1\), choose \(a=1-H\), \(d_i=0\), \(b_i=c_i=\sqrt w\). The exact ratio is

\[
\frac{C_{\mathrm{rec}}}{C_{\mathrm{dir}}}
=\frac{2}{1+\sqrt u},
\]

which tends to two as \(u\downarrow0\) and to one as \(u\uparrow1\). For the same model with \(u=1/4\), \(p_i=1\), and \(q_i=M>0\) with \(M\ge1\), direct cost is \(3/2\) while reciprocal cost is \(M+1\), giving unbounded ratio \(2(M+1)/3\) as \(M\to\infty\).

## Verification

The standalone `verify.py` included with this result uses rational arithmetic to check the Schur determinant identity for weighted four- and five-group examples under zero, half, and full attenuation on every directed spoke; it also checks exact cost certificates on a three-spoke boundary example and a family realizing the sharp reciprocity ratio. Execute `python3 verify.py` without external packages. These finite checks are not a proof for arbitrary group counts; the foregoing arguments are.

For an exact worked instance, take three spokes, \(a=1/4\), all \(d_i=0\), all \(b_i=c_i=1\), and all \(p_i=q_i=1\). Here \(W=3\), \(H=3/4\), and independent optimization has reductions \((1,1,1/4)\), cost \(9/4\). Reciprocal optimization has \(t_i=1/2\) on every spoke and cost \(3\). Both policies satisfy \(\rho(K)=1\), with a genuine cost difference of \(3/4\).

## Relationship to prior work

Bellingeri, Bilge, Peker-Dobie and Harman (2026) formulate multi-group social/epidemic propagation using next-generation matrices and examine no-propagation boundaries for two and three groups, as well as contact-attenuation scenarios. Their analyzed matrix families do not furnish the arbitrary-star, two-policy global cost minimizers or the price-of-reciprocity bound proved here. The exact spectral decomposition of star-type matrices, linear-programming greedy allocation and quadratic KKT optimization are standard ingredients; originality is claimed only for their *combined cost-optimal classification in the stated heterogeneous next-generation transmission design problem*.

Zhang, Lu and Pei (2018) give geometric-programming resource-allocation formulations for heterogeneous directed-network SEIS dynamics, with node-level rate and cost restrictions. Their broad optimization framework is not asserted to be superseded; it does not state the exact directional/spoke knapsack law, reciprocal water-filling law, or sharp cost ratio for this edge-controlled model. Preciado and collaborators (2013) study convex node-vaccination allocation for SIS networks, while Saha and collaborators (2015) give approximation algorithms for discrete edge or node deletions in undirected graphs; neither result is an exact optimizer for the present pair of continuous edge-control constraints.

## Limitations

This is an exact result for one star-shaped, nonnegative next-generation matrix and specified linear marginal attenuation costs. It is not a theorem for arbitrary mixing networks, nonlinear epidemic trajectories, time-dependent vaccination, stochastic outbreaks, threshold ties interpreted as strict exponential stability, or physical contact systems whose asymmetric controls violate feasibility constraints. Arbitrary general convex optimization literature may offer alternate derivations of some steps; no claim of universal priority over unindexed specializations is made. Independent validation and peer review have not been performed.

## References

1. M. Bellingeri, A. H. Bilge, A. Peker-Dobie, S. Harman, *Threshold analysis of multi-group SIR models with heterogeneous mixing*, Frontiers in Physics **14** (2026), 1755888, DOI 10.3389/fphy.2026.1755888. Public release 2026-06-16. https://doi.org/10.3389/fphy.2026.1755888
2. W. Zhang, S. Lu, Y. Pei, *A geometric programming approach for optimal resource allocation to control epidemic outbreaks in arbitrary networks*, Communications in Mathematical Biology and Neuroscience (2018), article 1, DOI 10.28919/cmbn/3388. https://doi.org/10.28919/cmbn/3388
3. V. M. Preciado, M. Zargham, C. Enyioha, A. Jadbabaie, G. J. Pappas, *Optimal vaccine allocation to control epidemic outbreaks in arbitrary networks*, 2013 preprint, arXiv:1303.3984. https://arxiv.org/abs/1303.3984
4. S. Saha, A. Adiga, B. A. Prakash, A. K. S. Vullikanti, *Approximation algorithms for reducing the spectral radius to control epidemic spread*, SIAM SDM (2015), 568–576, DOI 10.1137/1.9781611974010.64. https://doi.org/10.1137/1.9781611974010.64
