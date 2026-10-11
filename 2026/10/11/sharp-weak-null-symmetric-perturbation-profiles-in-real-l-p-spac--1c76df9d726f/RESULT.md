# Sharp weak-null symmetric perturbation profiles in real \(L_p\) spaces

## Finding
Let \((\Omega,\Sigma,\mu)\) be sigma-finite, with real \(L_p(\mu)\) infinite-dimensional, and let \(1<p<\infty\). For each \(x\in S_{L_p(\mu)}\), let \(x_{\mathrm{at}}\) and \(x_{\mathrm{dif}}\) be the restrictions of \(x\) to the atomic and nonatomic components. Set \(a=\|x_{\mathrm{at}}\|_p\) and \(d=\|x_{\mathrm{dif}}\|_p\), so that \(a^p+d^p=1\). For \(t\ge0\), define the sequential weak-null symmetric perturbation radius
\[
\Lambda_x(t)=\inf_{\substack{y_n\rightharpoonup0\\\|y_n\|_p\to t}}\limsup_{n\to\infty}\max\bigl\{\|x+y_n\|_p,\|x-y_n\|_p\bigr\}.
\]
The infimum is over real \(L_p(\mu)\) sequences. Its exact value is
\[
\boxed{\Lambda_x(t)^p=\begin{cases}
a^p+\dfrac{(d+t)^p+|d-t|^p}{2},&1<p<2,\\[4pt]
1+t^p,&2\le p<\infty.
\end{cases}}
\]
Both branches are attained in the sense of their defining infimum by explicit weakly null sequences of norm exactly \(t\). For \(1<p<2\) and \(t>0\), \(\Lambda_x(t)<(1+t^p)^{1/p}\) holds **exactly when** \(d>0\). Thus below the Hilbert exponent the full profile detects, and quantitatively measures, the \(L_p\)-mass of the nonatomic part of \(x\), while from the Hilbert exponent onward the profile is independent of \(x\) and of the measure's atomicity.

## Assumptions and scope
The measure is sigma-finite; it may have infinitely many atoms and/or a nonatomic part. The nonatomic component can be zero, and the atomic component can be zero. Infinite dimension is needed: in a finite-dimensional space every weakly null sequence converges in norm to zero, so the defining infimum has no admissible sequence for \(t>0\). Both signs of the perturbation are tested simultaneously, rather than separately, and the normalization \(\|x\|_p=1\) is part of the statement. The assertion is for real scalars and every fixed \(t\ge0\), with no uniform convergence claim in \(t\) or \(x\).

## Proof
Define \(A_p(d,u)=((d+u)^p+|d-u|^p)/2\) for \(d,u\ge0\). We first show that for \(1<p<2\) and \(0\le u\le v\),
\[
A_p(d,v)-A_p(d,u)\le v^p-u^p.\tag{1}
\]
Write \(q=p-1\in(0,1)\). If \(u\ge d\), concavity gives \(((u+d)^q+(u-d)^q)/2\le u^q\). If \(0<u<d\), subadditivity gives \((d+u)^q-(d-u)^q\le(2u)^q\le2u^q\). Differentiating \(A_p(d,u)\) in these two regions consequently yields \(\partial_u A_p(d,u)\le p u^{p-1}\); continuity at \(u=d\) and integration prove (1). In particular, whenever \(s^p+u^p=v^p\),
\[
s^p+A_p(d,u)\ge A_p(d,v).\tag{2}
\]

Fix any admissible weakly null sequence \((y_n)\). Sigma-finiteness makes the atomic part isometric to a countable \(\ell_p\) space. Each atomic coordinate of \(y_n\) tends to zero; \((y_n)\) is bounded. Finite-head approximation plus the elementary bound
\[
\bigl||b+c|^p-|b|^p\bigr|\le C_p\bigl(|c|^p+|c|\,|b|^{p-1}\bigr)
\]
on the small tail of the fixed sequence \(x_{\mathrm{at}}\), and Hölder's inequality, yield for either sign
\[
\|x_{\mathrm{at}}\pm y_{n,\mathrm{at}}\|_p^p
=a^p+\|y_{n,\mathrm{at}}\|_p^p+o(1).\tag{3}
\]
For \(1<p\le2\), Hanner's inequality on the nonatomic component gives
\[
\frac{\|x_{\mathrm{dif}}+y_{n,\mathrm{dif}}\|_p^p+
\|x_{\mathrm{dif}}-y_{n,\mathrm{dif}}\|_p^p}{2}
\ge A_p\bigl(d,\|y_{n,\mathrm{dif}}\|_p\bigr).\tag{4}
\]
Put \(s_n=\|y_{n,\mathrm{at}}\|_p\), \(u_n=\|y_{n,\mathrm{dif}}\|_p\) and \(v_n=\|y_n\|_p\), so \(s_n^p+u_n^p=v_n^p\). Since the larger of two nonnegative numbers dominates their average, equations (2)--(4) show for \(1<p<2\) that
\[
\max\{\|x+y_n\|_p^p,\|x-y_n\|_p^p\}
\ge a^p+A_p(d,v_n)+o(1).
\]
As \(v_n\to t\), this is the required lower bound.

For \(d>0\) the measure \(\nu(E)=\int_E|x_{\mathrm{dif}}|^p\,d\mu\) is finite, nonzero, and nonatomic, of total mass \(d^p\). Recursively bisecting its measurable sets gives symmetric independent sign functions \(r_n\in\{-1,1\}\) with \(\nu(r_n=1)=\nu(r_n=-1)=d^p/2\), and \(r_n\to0\) weak-star against every \(L_1(\nu)\) integrand. Indeed, they are orthonormal in \(L_2(\nu/d^p)\), so Bessel's inequality handles \(L_2\) integrands, and density extends the conclusion to \(L_1\). Set
\[
y_n=(t/d)\,r_n x_{\mathrm{dif}}
\]
on the diffuse part, and zero elsewhere. Then \(\|y_n\|_p=t\), and for any \(g\in L_{p'}(\mu)\), the integral \(\int g y_n\,d\mu\) tends to zero by applying weak-star convergence of \(r_n\) to the \(L_1(\nu)\) density \(g x_{\mathrm{dif}}/|x_{\mathrm{dif}}|^p\) (defined as zero at zeros of \(x_{\mathrm{dif}}\)). The two signs have the same norm power, namely \(a^p+A_p(d,t)\), as the signs split the weighted measure equally. This attains the first branch.

For \(p\ge2\), the scalar Clarkson inequality integrated over the entire measure space gives
\[
\frac{\|x+y\|_p^p+\|x-y\|_p^p}{2}\ge \|x\|_p^p+\|y\|_p^p
=1+\|y\|_p^p.\tag{5}
\]
For every infinite-dimensional sigma-finite \(L_p\) there are infinitely many pairwise disjoint measurable sets \(E_n\) of finite positive measure. Let \(y_n=t\mu(E_n)^{-1/p}\mathbf 1_{E_n}\). The sequence has norm \(t\) and is weakly null: if \(g\in L_{p'}\), then \(|\int gy_n|\le t\|g\mathbf1_{E_n}\|_{p'}\to0\). Also \(\|x\mathbf1_{E_n}\|_p\to0\). Thus
\[
\|x\pm y_n\|_p^p\to 1+t^p,\tag{6}
\]
proving equality for \(p\ge2\); the same disjoint sequence proves equality in the first branch when \(d=0\). When \(t=0\), simply take \(y_n=0\). At \(p=2\), the two expressions agree because \(a^2+d^2=1\).

Finally, for \(1<p<2\) and \(d,t>0\), strict scalar Clarkson inequality gives \(A_p(d,t)<d^p+t^p\), hence the strict detection criterion claimed above.

## Verification
The analytic argument above proves the result for all stated real exponents, measure spaces, vectors and perturbation sizes. The supplementary standalone `verify.py` checks the monotonicity inequality (1), balanced-sign identity and selected scalar inequalities numerically, over finite parameter grids; these checks cannot establish the universal statement. A replay from the included source returned `VERIFY_OK scalar_checks=13365 p_below_2=6 p_above_2=5 analytic_proof_required=True`.

## Relationship to prior work
Rodríguez and Rueda Zoca (2023 preprint) provide Rademacher-type weakly null constructions and weak almost squareness for nonatomic \(L_1\) spaces. Here the quantity measures **symmetric two-sided weak-null perturbation profiles for \(1<p<\infty\)** rather than qualitative almost squareness at the endpoint; the exact mixed atomic/nonatomic transition and the change at \(p=2\) are not implied by their \(L_1\) construction alone. Hanner's inequality (as reproduced by Ivanisvili--Stolyarov--Zatitskiy) supplies a sharp bound on pairs of vectors, but does not itself supply the weak-null attainment and the optimal placement of perturbation mass across atomic and diffuse components. Dilworth--Kutzarova--Randrianarivony--Romney study asymptotic midpoint uniform convexity and classify a qualitative \(L_p(X)\) property; their paper could not be fully compared, leaving possible terminological/equivalent coverage as a residual risk.

## Limitations
This is a sequential, pointwise infimum over weakly null perturbations; it does not determine nonsymmetric or finite-codimensional asymptotic moduli, nor apply to arbitrary Bochner-valued spaces or to finite-dimensional \(L_p\) for positive \(t\). The finite numerical checks are nonexhaustive and not a substitute for the proof. Originality remains subject to a future full comparison with inaccessible asymptotic-midpoint literature and further independent audit.

## References
1. J. Rodríguez and A. Rueda Zoca, *On weakly almost square Banach spaces*, arXiv:2301.07943v1 (first posted 2023-01-19), especially Lemma 2.1 and Corollary 2.5, https://arxiv.org/pdf/2301.07943.
2. P. Ivanisvili, D. M. Stolyarov, P. B. Zatitskiy, *Bellman VS Beurling: sharp estimates of uniform convexity for Lp spaces*, arXiv:1405.6229v1 (2014), Theorem 2 (Hanner inequalities), https://arxiv.org/pdf/1405.6229.
3. S. J. Dilworth, D. Kutzarova, N. L. Randrianarivony, M. Romney, *Sums of asymptotically midpoint uniformly convex spaces*, Bull. Belg. Math. Soc. Simon Stevin 24 (2017), 439--446, doi:10.36045/bbms/1506477692. Only abstract available for scientific comparison.
