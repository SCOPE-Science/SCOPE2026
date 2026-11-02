# Sharp edge-variation contraction of lazy walks on complete bipartite graphs

## Finding

For integers \(p,q\ge2\), let \(G=K_{p,q}\) have bipartition \(X\sqcup Y\), with \(|X|=p\) and \(|Y|=q\), and unit edge weights. Write \(M=\max\{p,q\}\). For \(0\le\alpha\le1\), consider the one-step lazy random-walk averaging operator
\[
 (T_\alpha f)(v)=\alpha f(v)+\frac{1-\alpha}{\deg(v)}\sum_{u\sim v}f(u).
\]
Define graph edge variation on real vertex signals by
\[
 J(f)=\sum_{x\in X}\sum_{y\in Y}|f(x)-f(y)|.
\]
Then the exact, attained induced seminorm on nonconstant inputs is
\[
 \boxed{\sup_{J(f)>0}\frac{J(T_\alpha f)}{J(f)}
 =\max\left\{1-2\alpha,\;1-\frac{2(1-\alpha)}M\right\}.}
\]
In particular, for every fixed pair \((p,q)\), the **unique** holding probability minimizing worst-case edge-variation amplification is
\[
 \boxed{\alpha_* =\frac1{M+1},\qquad \min_{0\le\alpha\le1}\sup_{J(f)>0}\frac{J(T_\alpha f)}{J(f)}=\frac{M-1}{M+1}.}
\]
The optimum and the entire sharp norm curve depend only on the larger bipartition size. Below the transition the indicator of one whole bipartition is extremal. Above it the indicator of a single vertex in a larger bipartition is extremal; both are extremal at the transition. These are existence statements for extremizers, not an exhaustive classification of all equality signals.

## Assumptions and scope

All signals are real, edges are unweighted, the graph is simple and complete bipartite, \(p,q\) are finite integers at least two, and the holding probability lies in the closed interval \([0,1]\). The averaging is over the **open** graph neighborhood with constant holding probability at every vertex. The graph-edge variation is the undirected sum with each edge counted exactly once; it is not total-variation distance between probability distributions or the vertex-shift discrepancy \(\|f-Pf\|_1\).

The quantity is a one-input quotient by the graph-variation seminorm. Because \(G\) is connected, \(J(f)=0\) exactly for constant signals. The assertion applies to all real inputs without positivity or normalization restrictions.

## Proof

**1. Reduction to indicators (valid for any linear constant-preserving operator).** For any real finite signal, choose \(c=\min_v f(v)\) and write
\[
 f=c\mathbf1+\int_c^{\max f}\mathbf1_{\{f>t\}}\,dt.
\]
Since \(T_\alpha\mathbf1=\mathbf1\), linearity and the triangle inequality give
\[
 J(T_\alpha f)\le\int_c^{\max f}J(T_\alpha\mathbf1_{\{f>t\}})\,dt.
\]
The edgewise coarea identity gives \(J(f)=\int_c^{\max f}J(\mathbf1_{\{f>t\}})\,dt\). Consequently the optimal quotient is the maximum over nonconstant indicator functions. This is a finite exact reduction, not a numerical approximation.

**2. Edge differences.** For an indicator of a subset containing \(r\) vertices of \(X\) and \(s\) of \(Y\), put
\[
 U=r(q-s),\quad V=(p-r)s,\quad E=pq,\quad D=U+V.
\]
Among the \(E\) oriented edges from \(X\) to \(Y\), the original difference is \(+1\) on \(U\) edges, \(-1\) on \(V\) edges and zero elsewhere. Denote its mean by \(\delta=(U-V)/E\). Every updated oriented edge difference equals
\[
 \alpha\,d_{xy}-(1-\alpha)\delta,
\]
because neighborhood averaging replaces a value in either bipartition by the mean value in the opposite one. Hence, for \(D>0\), the exact cut ratio is
\[
 R(r,s)=\frac{U|\alpha-(1-\alpha)\delta|+V|\alpha+(1-\alpha)\delta|+(E-D)(1-\alpha)|\delta|}{D}.
\]
Replacing the cut by its complement exchanges \(U,V\), preserves both numerator and denominator, and changes the sign of \(\delta\). We may therefore assume \(U\ge V\), or \(\delta\ge0\).

**3. The critical cut-size lemma.** Whenever \(U>V\), one has
\[
 U\ge\min\{p,q\}=\frac{E}{M}.
\]
To prove it when \(p\le q\), the inequality \(U>V\) is equivalent to \(qr>ps\). Thus \(q-s>q(1-r/p)\ge p-r\); integrality gives \(q-s\ge p-r+1\), whence \(U=r(q-s)\ge r(p-r+1)\ge p\) for \(1\le r\le p\). When \(q\le p\), \(qr>ps\) implies \(r>s\), hence \(r\ge s+1\) and \(U\ge(s+1)(q-s)\ge q\) for \(0\le s<q\). Both bounds are sharp: a cut or its complement isolating one vertex of a larger bipartition has \(U=E/M\), \(V=0\). In the remaining case \(U=V\), the term involving \(\delta\) vanishes.

**4. Two exhaustive sign regimes.** Set \(k=1-\alpha\). If \(\alpha\ge k\delta\), the displayed absolute values reduce to
\[
 R(r,s)=\alpha+k\frac{U-V}{U+V}\left(1-\frac{2U}{E}\right).
\]
For \(U>V\), the prefactor is between zero and one and the lemma gives \(U/E\ge1/M\). Since \(M\ge2\), the product is bounded by \(1-2/M\), even when its second factor is negative. The \(U=V\) case gives \(R=\alpha\), which also satisfies the bound. Therefore
\[
 R(r,s)\le1-\frac{2(1-\alpha)}M.
\]
If instead \(\alpha<k\delta\), necessarily \(\alpha<1/2\), and the numerator simplifies exactly to \((1-2\alpha)(U-V)\). Thus
\[
 R(r,s)=(1-2\alpha)\frac{U-V}{U+V}\le1-2\alpha.
\]
The two bounds cover all cuts and hence, by Step 1, all real signals.

**5. Sharpness and unique optimum.** The indicator of the entire \(X\) side has constant original edge difference \(+1\) and updated edge difference \(2\alpha-1\), attaining \(1-2\alpha\) whenever \(\alpha\le1/(M+1)\). A singleton in a side of size \(M\) has exactly \(E/M\) nonzero original edge differences and attains \(\alpha+(1-\alpha)(1-2/M)\) whenever \(\alpha\ge1/(M+1)\). Thus the maximum of the two affine expressions is exact, including the shared breakpoint. The first affine function is strictly decreasing and the second is strictly increasing; they meet only when \(\alpha=1/(M+1)\), giving the unique minimizer and the displayed minimum. \(\square\)

## Verification

The included dependency-free `verify_bipartite.py` uses exact rational arithmetic. Its execution reports 31,468 independently evaluated nonconstant binary-input inequalities across bipartition sizes 2 through 5, 2,536 cross-comparisons between direct graph calculations and the displayed cut formula, 1,200 random exact-rational nonbinary input checks, and 814 explicit sharpness examples. All comparisons are exact rather than tolerance-based. Invoke `python verify_bipartite.py` from a directory containing the file. The all-size theorem rests on the preceding analytic reduction and integer cut-size lemma, not these finite tests.

## Relationship to prior work

Sandryhaila and Moura (2013, arXiv:1307.0468) study graph signal filtering and define a **different** shift-based vertex variation \(\|f-A_{\mathrm{norm}}f\|_1\); their inspected sections on variation and filter design do not imply the edgewise seminorm formula here. Feneuil (2014, arXiv:1404.1353) develops \(L^p\) estimates for discrete Markov and Littlewood–Paley operators on graphs; the inspected introduction, main results and estimates do not give a sharp finite-biclique edge-BV contraction coefficient. Chen et al. (2014, arXiv:1411.7414) examine graph-signal recovery by variation minimization, with a focus on quadratic regularization, not a sharp one-step neighbor-averaging operator norm. Kirisits, Scherzer and Setterqvist (2018, arXiv:1807.10514) consider graph-edge TV denoising and nonlinear TV flow, not the linear Markov averaging filter here.

The indicator/coarea reduction is a standard consequence of graph-edge \(\ell^1\) variation; no novelty is claimed for it in isolation. The specific all-size sharp maximum of two branches, its extremizing cuts, the dependence exclusively on the larger side, and the uniquely optimal holding parameter are the claims at issue.

## Limitations

There is no claim for arbitrary bipartite graphs, nonuniform edge weights, time-inhomogeneous or multistep filters, nonuniform holding probabilities, or nonlinear maximal operators. The result does not establish faster mixing in stationary-distribution metrics, which differ from graph-edge variation. The literature comparison was broad but cannot exclude unpublished or differently named older equivalent calculations. Equality inputs are explicitly exhibited, not exhaustively classified.

## References

1. A. Sandryhaila and J. M. F. Moura, *Discrete Signal Processing on Graphs: Frequency Analysis*, arXiv:1307.0468, first submitted 2013-07-01, https://arxiv.org/abs/1307.0468.
2. J. Feneuil, *Littlewood-Paley functionals on graphs*, arXiv:1404.1353, first submitted 2014-04-04, https://arxiv.org/abs/1404.1353.
3. S. Chen, A. Sandryhaila, J. M. F. Moura and J. Kovačević, *Signal Recovery on Graphs: Variation Minimization*, arXiv:1411.7414, first submitted 2014-11-26, https://arxiv.org/abs/1411.7414.
4. C. Kirisits, O. Scherzer and E. Setterqvist, *Invariant \(\varphi\)-minimal sets and total variation denoising on graphs*, arXiv:1807.10514, first submitted 2018-07-27, https://arxiv.org/abs/1807.10514.
