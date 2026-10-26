# Sharp aspect-ratio law for affine projections on products of simplices

## Finding
Fix an integer \(k\ge2\). For each \(1\le i\le k\), let \(T_i\) be a nondegenerate simplex of dimension \(d_i\ge1\), and put \(\Omega=\prod_{i=1}^kT_i\) and \(N=\sum_i d_i\). All integrals use the uniform probability measure on \(\Omega\). Let \(P\) be the \(L^2\)-orthogonal projector onto the space of **globally affine** functions on \(\Omega\), namely the span of the constant function and the linear coordinate functions of the ambient product space. This is not projection onto the much larger tensor-product polynomial space.

For independent random variables \(U_i\sim\operatorname{Beta}(1,d_i)\), the exact finite-dimensional supremum norm is
\[
\boxed{\|P\|_{L^\infty\to L^\infty}=\mathbb E\left|\sum_{i=1}^k(d_i+1)(d_i+2)U_i-(N+2k-1)\right|.}
\]
The corresponding Lebesgue function is maximized at every product vertex. In particular this formula is independent of the shapes of the factor simplices.

Let the dimensions vary with fixed \(k\), \(N\to\infty\), and \(d_i/N\to w_i\ge0\), where \(\sum_iw_i=1\). If \(E_1,\ldots,E_k\) are independent unit-mean exponential variables, then
\[
\boxed{\lim_{N\to\infty}\frac{\|P\|_{L^\infty\to L^\infty}}N=F_k(w),\qquad F_k(w)=\mathbb E\left|\sum_{i=1}^kw_iE_i-1\right|.}
\]
The function \(F_k\) is strictly Schur-convex: every nontrivial balancing of two unequal weights strictly decreases it. Therefore
\[
\boxed{\frac{2k^ke^{-k}}{k!}\le F_k(w)\le\frac2e.}
\]
Equality on the left holds precisely at \(w_1=\cdots=w_k=1/k\); equality on the right holds precisely when one weight is one and all others are zero. These are sharp asymptotic constants. At equal weights the coefficient is asymptotic to \(\sqrt{2/(\pi k)}\) as \(k\to\infty\) after taking the dimension limit.

For two factors, with \(w=(a,1-a)\) and \(a\in(0,1)\setminus\{1/2\}\), a closed form is
\[
F_2(a,1-a)=2\frac{a^2e^{-1/a}-(1-a)^2e^{-1/(1-a)}}{2a-1},
\]
continuously extended by \(F_2(1/2,1/2)=4e^{-2}\) and \(F_2(0,1)=F_2(1,0)=2/e\).

## Assumptions and scope
The dimensions of individual factors are positive integers. No regularity of inputs beyond essential boundedness is imposed. The product is equipped with its usual product uniform probability measure, and the affine space has dimension \(N+1\). The theorem concerns total-degree-one projection, not the tensor-product of the factorwise affine projections. The limit holds for each fixed \(k\) and every dimension sequence with the stated weight convergence, including some bounded dimensions whose limiting weights vanish. No rate of convergence uniform in all dimension vectors is claimed. The \(k\to\infty\) statement is taken only after the fixed-\(k\) dimension limit.

## Proof
**1. Factor kernels.** Write \(\lambda_{i,0},\ldots,\lambda_{i,d_i}\) for the barycentric coordinates on \(T_i\). Their uniform-probability moments satisfy
\[
\mathbb E\lambda_{i,j}=\frac1{d_i+1},\qquad
\mathbb E(\lambda_{i,j}\lambda_{i,\ell})=\frac{1+\mathbf1_{j=\ell}}{(d_i+1)(d_i+2)}.
\]
Inverting this moment matrix, the reproducing kernel of the affine projector on factor \(T_i\), evaluated at its vertex \(v_{i,0}\), is
\[
K_i(v_{i,0},x_i)=(d_i+1)(d_i+2)\lambda_{i,0}(x_i)-(d_i+1).
\]
In the product measure the mean-zero affine subspaces associated with distinct factors are mutually orthogonal. Thus the globally affine projection is the orthogonal sum of the constants and those factorwise mean-zero spaces. Its kernel is
\[
K_\Omega(x,y)=\sum_{i=1}^kK_i(x_i,y_i)-(k-1).
\]
At the product vertex \(v=(v_{1,0},\ldots,v_{k,0})\), this reduces to
\[
K_\Omega(v,y)=\sum_{i=1}^k(d_i+1)(d_i+2)\lambda_{i,0}(y_i)-(N+2k-1).
\]
The independent random barycentric coordinates \(\lambda_{i,0}(y_i)\) have distributions \(\operatorname{Beta}(1,d_i)\), giving the claimed vertex integral. The kernel has integral one, because constants are reproduced.

**2. Vertex extremality.** For each fixed \(y\), \(K_\Omega(x,y)\) is affine in the ambient variable \(x\). Therefore its absolute value is convex in \(x\), and the Lebesgue function \(\int_\Omega|K_\Omega(x,y)|\,d\mu(y)\) is convex. Every point of the product polytope is a convex combination of product vertices; hence its Lebesgue function is bounded by the largest vertex value. Each factor's barycentric symmetry makes these vertex values equal. By the standard integral-operator norm identity, the vertex value is the exact \(L^\infty\)-operator norm. The bound is achieved in \(L^\infty\) by a sign choice of the vertex kernel; continuous functions can approximate this choice in integral norm.

**3. Exponential limit.** If \(U_d\sim\operatorname{Beta}(1,d)\), then for fixed \(s\ge0\),
\[
\mathbb P(dU_d>s)=(1-s/d)^d\longrightarrow e^{-s}
\]
for \(0\le s\le d\). Hence \(dU_d\) converges in law to a unit exponential. For every weight \(w_i>0\), the dimension \(d_i\to\infty\), and
\[
\frac{(d_i+1)(d_i+2)}N U_i\ \Longrightarrow\ w_iE_i.
\]
For \(w_i=0\), the term converges to zero in \(L^1\), since its expectation is \((d_i+2)/N\to0\). The terms have uniformly bounded second moments in aggregate: using independence, the full centered kernel divided by \(N\) has second moment
\[
\frac{1+\sum_i d_i(d_i+2)}{N^2}\le 1+\frac{2}{N}+\frac{1}{N^2}.
\]
This proves uniform integrability. Since \((N+2k-1)/N\to1\), convergence of the expectations of absolute values follows.

**4. Strict majorization law.** Fix two weights \(a,b\) with fixed sum \(s>0\), and condition on all other exponential variables, whose weighted sum is \(R\ge0\). Let \(X,Y\) be independent unit exponentials. Symmetrizing under \(X\leftrightarrow Y\) gives the identity
\[
\tfrac12\bigl(|R+aX+bY-1|+|R+aY+bX-1|\bigr)
=\max\!\left\{\left|R+\tfrac{s}{2}(X+Y)-1\right|,\tfrac{|a-b|}{2}|X-Y|\right\}.
\]
The right side is nondecreasing with \(|a-b|\). It is strictly increasing in expectation when a nonzero imbalance is introduced or increased: on a positive-probability set, \(R+s(X+Y)/2\) is arbitrarily close to one while \(X\ne Y\). This set exists even if no other weights are nonzero (take \(R=0\)); otherwise restrict all other exponentials to small positive values. Every nontrivial balancing transfer therefore strictly reduces \(F_k\). Finite sequences of such transfers establish strict Schur-convexity and force the unique minimum at equal weights and maxima only at probability-simplex vertices.

**5. Sharp constants.** Put \(Z=\sum_iw_iE_i\). Since \(\mathbb EZ=1\), \(\mathbb E|Z-1|=2\mathbb E(Z-1)_+\). At a weight vertex, \(Z\) is unit exponential and the expectation is \(2/e\). At equal weights, \(Z\) is \(1/k\) times a \(\operatorname{Gamma}(k,1)\) variable. Integrating its density over the region \(z>1\), using the incomplete-gamma recurrence, gives \(2k^ke^{-k}/k!\). Stirling's formula yields the stated large-\(k\) balanced value.

When \(k=2\) and \(a\ne b\), the convolution density of \(aE_1+bE_2\) is \((e^{-t/a}-e^{-t/b})/(a-b)\) for \(t\ge0\). Integrating \(2(t-1)\) over \(t>1\) gives the displayed two-factor expression. Its equal-weight and endpoint limits follow by continuity.

## Verification
The accompanying standalone `verify.py` checks factor moment reproduction, vertex kernel normalization, and exact rational integration of the negative part of the kernel for several small simplex products. The exact norms include \(233/108\) for two intervals, \(11/4\) for an interval times a triangle, and \(1027567/311040\) for two triangles. It separately checks the closed-form limiting values and their strict ordering for sample weights. The checker is not used in place of the proof of vertex extremality, limiting convergence, or majorization, each of which was proved for the specified infinite families above.

## Relationship to prior work
Local affine \(L^2\)-projections are standard in finite-element analysis; Duan–Lin–Saikrishnan–Tan (2006) use a local or almost-local linear projection in least-squares schemes. Chernov (2010 preprint; 2012 journal publication) treats trace and Sobolev convergence estimates for polynomial \(L^2\)-projections on a *single simplex*. A published exact norm/positivity result for the affine projector on a *single simplex* evaluates its vertex negative kernel mass via a beta distribution. Such single-factor formulas do not imply the present product formula: globally affine projection on a product is an **additive orthogonal sum**, not a tensor product, and the factor dimensions give distinct independent beta laws. The resulting exponential-mixture norm and strict aspect-ratio majorization law require additional arguments. A product-simplex geometric result about inballs concerns a different invariant, as does a published Schur-concavity theorem for block-profile anti-concentration. The inspected material does not state or imply the sharp product asymptotic and equality classification.

## Limitations
The global \(L^\infty\) norm of tensor-product polynomial projection is a different problem. The theorem provides a sharp dimension-ratio asymptotic at fixed factor count, not a uniform remainder estimate. The strict equal-weight result concerns limiting dimension proportions, not a general exact finite-dimensional monotonicity assertion. Publication searches and accessible prior records cannot establish absolute novelty; older formulations of multivariate projection constants, particularly in unindexed approximation literature or a partially inaccessible visualization-projection article, remain residual originality risks. No independent scientific audit has been performed.

## References
1. Huo-yuan Duan, Ping Lin, P. Saikrishnan, and Roger C. E. Tan, *L2-Projected Least-Squares Finite Element Methods for the Stokes Equations*, SIAM J. Numer. Anal. 44 (2006), 732–752, DOI: 10.1137/040613573 (first published online 2006-07-25).
2. Alexey Chernov, *Optimal convergence estimates for the trace of the polynomial L2-projection operator on a simplex*, INS Preprint 1002 (2010); Math. Comp. 81 (2012), 765–787, DOI: 10.1090/S0025-5718-2011-02513-5.
3. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, published mathematical research record, 2026-10-04, identifier: SCOPE-20261004-99c2b9dd9b34.
4. Mario Ohlberger and Martin Rumpf, *Adaptive Projection Operators in Multiresolution Scientific Visualization*, IEEE Trans. Vis. Comput. Graphics 5 (1999), 74–94, DOI: 10.1109/2945.765328 (abstract inspected; full text unavailable at review).
