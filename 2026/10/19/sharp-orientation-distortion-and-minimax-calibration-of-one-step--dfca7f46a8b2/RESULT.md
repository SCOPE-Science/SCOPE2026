# Sharp orientation distortion and minimax calibration of one-step Hybrid LSLU regularization

## Finding

The first projected ridge solve of pivoted **Hybrid LSLU** can have a dimension-dependent regularization scale even when the forward matrix has condition number one. Precisely, let integers \(2\le n<m\) be fixed, let \(A\in\mathbb R^{m\times n}\) have orthonormal columns, let \(u\in\mathbb R^n\setminus\{0\}\), and let \(e\in\ker A^{\mathsf T}\setminus\{0\}\). Apply the pivoted rectangular Hessenberg stage of Hybrid LSLU to \(b_\varepsilon=Au+\varepsilon e\) with \(x_0=0\), full largest-magnitude pivoting, and fixed projected Tikhonov parameter \(\mu>0\). Denote the first regularized iterate by \(x_{1,\varepsilon}(\mu)\). For every sufficiently small \(\varepsilon>0\), the first stage is nonbreakdown, and

\[
\lim_{\varepsilon\downarrow0}x_{1,\varepsilon}(\mu)=\frac{u}{1+\mu^2q^2},\qquad q=\frac{\|u\|_\infty}{\|Au\|_\infty}.
\]

The effective Tikhonov parameter is therefore \(\mu q\), with the **sharp** orientation range

\[
\frac1{\sqrt n}\le q\le\sqrt m.
\]

Both endpoints occur for matrices with \(A^{\mathsf T}A=I_n\), so the effective squared ridge penalty ranges sharply from \(\mu^2/n\) to \(m\mu^2\), independently of the spectral condition number.

More strongly, compare with ordinary Euclidean Tikhonov regularization at parameter one, whose exact solution for every \(b_\varepsilon\) is \(u/2\). Among **all scalar** projected parameters \(\mu>0\) chosen without reference to the orientation of \(A,u\), the sharp worst-case normalized first-iterate discrepancy is

\[
\boxed{\inf_{\mu>0}\sup_{A,u,e}\lim_{\varepsilon\downarrow0}\frac{\|x_{1,\varepsilon}(\mu)-u/2\|_2}{\|u\|_2}
=\frac{\sqrt{mn}-1}{2(\sqrt{mn}+1)}.}
\]

The **unique** minimizer is \(\mu=(n/m)^{1/4}\). Thus universal scalar retuning cannot remove the orientation bias: the optimal error tends to \(1/2\) as \(mn\to\infty\). In contrast, the orientation-dependent choice \(\mu=\|Au\|_\infty/\|u\|_\infty\) exactly restores the classical parameter-one filter in the zero-noise limit. This final observation is a one-stage calibration identity, not a statement about an adaptive regularization strategy.

## Assumptions and scope

Use Algorithm 4's complete pivoting and Algorithm 5's projected ridge step of Brown, Chung, Nagy and Sabaté Landman, with the projected minimization \(\min_y\|\beta e_1-H_{2,1}y\|_2^2+\mu^2\|y\|_2^2\). The dimensions satisfy \(m>n\ge2\). All matrices and vectors are real, arithmetic is exact, and \(\varepsilon\downarrow0\) is taken with \(A,u,e,\mu\) fixed. Ties in maximum-magnitude pivots can be resolved arbitrarily: the limit is independent of that choice. The noise vector \(e\) is orthogonal to the column space of \(A\), so \(A^{\mathsf T}b_\varepsilon=u\) for every \(\varepsilon\). We do not assert that the source pseudocode emits a regularized iterate at **exactly** \(\varepsilon=0\), because the generalized Hessenberg process can then break down. Every theorem statement about the algorithm uses genuinely nonzero perturbations and then takes their limit.

## Proof

**First-stage reconstruction.** Let \(b^0=Au\). Let \(p\) be the largest-magnitude measurement pivot, \(\beta=(b_\varepsilon)_p\), and \(d_1=b_\varepsilon/\beta\). Since \(A^{\mathsf T}e=0\), the initial right-vector calculation is \(A^{\mathsf T}d_1=u/\beta\). Choosing any largest-magnitude coordinate \(g\) of this vector gives \(W_{11}=u_g/\beta\ne0\) and \(l_1=u/u_g\). Thus

\[
v=Al_1=\frac{b^0}{u_g},\qquad h_1=v_p=\frac{b^0_p}{u_g},\qquad v-h_1d_1=\frac{\varepsilon(e_p b^0-b^0_pe)}{\beta u_g}.
\]

The last vector vanishes at position \(p\) and cannot vanish identically when \(\varepsilon>0\), \(e\perp b^0\), and \(e\ne0\). Its maximum remaining coordinate is the nonzero subdiagonal Hessenberg entry \(h_2\); this provides an actual completed first-stage projected problem. Moreover \(h_2=O(\varepsilon)\). The projected ridge minimizer is

\[
y=\frac{\beta h_1}{h_1^2+h_2^2+\mu^2},\qquad x_{1,\varepsilon}(\mu)=l_1y
=\frac{\beta b^0_p}{(b^0_p)^2+u_g^2(h_2^2+\mu^2)}\,u.
\]

As \(\varepsilon\downarrow0\), a selected \(p\) must lie among the coordinates maximizing \(|b^0_p|\), and every selected \(g\) maximizes \(|u_g|\). Consequently \(\beta b^0_p\to\|b^0\|_\infty^2\), \((b^0_p)^2\to\|b^0\|_\infty^2\), and \(u_g^2=\|u\|_\infty^2\), proving the asserted limit uniformly across pivot ties.

**Sharp geometry.** The isometry gives \(\|Au\|_2=\|u\|_2\). The elementary norm inequalities imply

\[
\frac{\|u\|_\infty}{\|Au\|_\infty}\ge\frac{\|u\|_2/\sqrt n}{\|Au\|_2}=\frac1{\sqrt n},\qquad
\frac{\|u\|_\infty}{\|Au\|_\infty}\le\frac{\|u\|_2}{\|Au\|_2/\sqrt m}=\sqrt m.
\]

For the upper endpoint choose \(u=e_1\) and an isometry whose first column is the flat vector \((1,\ldots,1)^{\mathsf T}/\sqrt m\), then extend it by any \(n-1\) orthonormal columns. For the lower endpoint choose \(u=(1,\ldots,1)^{\mathsf T}/\sqrt n\) and any isometry mapping \(u\) to the first coordinate vector of \(\mathbb R^m\). Such extensions exist because \(n<m\). Nonzero noise orthogonal to the chosen column spaces exists and supplies nonbreakdown first steps. Thus both endpoint filters are actual limits of algorithmic iterates.

**Exact minimax obstruction.** Since \(A^{\mathsf T}b_\varepsilon=u\), the ordinary parameter-one Tikhonov minimizer of \(\|b_\varepsilon-Ax\|_2^2+\|x\|_2^2\) is identically \(u/2\). Set \(z=\mu^2>0\). By the previous two parts, the exact worst-case limiting discrepancy, divided by \(\|u\|_2\), is

\[
E(z)=\max\left\{\left|\frac1{1+z/n}-\frac12\right|,\ \left|\frac1{1+mz}-\frac12\right|\right\}.
\]

Indeed, \(s\mapsto(1+zs)^{-1}\) is monotone for \(s\in[1/n,m]\), and both endpoints are attainable. For \(z<1/m\), increasing \(z\) lowers \(E\); for \(z>n\), decreasing \(z\) lowers \(E\). On the intervening interval, the upper-filter deviation decreases strictly with \(z\) while the lower-filter deviation increases strictly. They are equal precisely when

\[
\frac1{1+z/n}+\frac1{1+mz}=1
\quad\Longleftrightarrow\quad \frac mn z^2=1.
\]

Hence the unique optimum is \(z=\sqrt{n/m}\), or \(\mu=(n/m)^{1/4}\), and substitution gives \(E=(\sqrt{mn}-1)/(2(\sqrt{mn}+1))\). The orientation-dependent choice \(\mu=1/q\) makes \(\mu q=1\) in the first displayed limit, proving the calibration identity.

## Verification

The accompanying standalone `verify.py` reconstructs the first-stage pivots, the rectangular Hessenberg residual, and the projected ridge solve directly. It checks two explicit \(4\times2\) exact isometries, verifies their nonzero-noise expressions at rational noise sizes, checks the two endpoint limits symbolically, and confirms the balancing identity. All computation checks pass in SymPy. The endpoint theorem for arbitrary dimensions and the minimax identity are proved above; finite tests are not used to infer their universal validity.

In one explicit upper-endpoint example, the first two columns are \((1,1,1,1)^{\mathsf T}/2\) and \((1,-1,1,-1)^{\mathsf T}/2\), the true signal is \((1,0)^{\mathsf T}\), and the orthogonal perturbation is \(\varepsilon(1,0,-1,0)^{\mathsf T}\). The limiting hybrid filter with \(\mu=1\) is \(1/5\), versus the ordinary Tikhonov filter \(1/2\). In an exact lower-endpoint example, the columns are \((1,1,0,0)^{\mathsf T}/\sqrt2\) and \((1,-1,0,0)^{\mathsf T}/\sqrt2\), the true signal is \((1,1)^{\mathsf T}/\sqrt2\), and the perturbation is \(\varepsilon(0,0,1,0)^{\mathsf T}\). The limiting hybrid filter is \(2/3\).

## Relationship to prior work

Brown, Chung, Nagy and Sabaté Landman [1], Sections 2.2 and 3, introduce the rectangular Hessenberg/LSLU algorithm, its complete pivoting and the projected regularization objective. In particular, their Eq. (28) directly supplies the one-dimensional projected ridge problem used here; their Theorem 3.1 bounds regularized residuals using a basis condition number. These are **prior results**, not contributions of the present finding. Brown, Sabaté Landman and Nagy [2], Section 4, develop related hybrid CMRH regularization on square problems with nonorthogonal Krylov bases. Sabaté Landman and coauthors [3], Section 3, discuss sketched LSLU methods and coordinate-sensitive residual criteria. None of the inspected passages provides the exact isometric first-step orientation filter, both sharp dimension endpoints, or its universal scalar-calibration minimax theorem. The general observation that a nonorthogonal basis changes a coordinate-space penalty is not presented as new.

## Limitations

The claim concerns exactly the first nonbreakdown rectangular Hessenberg stage, with full pivoting and a **fixed input** ridge parameter, as the orthogonal perturbation tends to zero. It does not assert an algorithm output at exact consistent-data breakdown, any behavior for later iterations, or an impossibility result for GCV, data-adapted choices, or sketched ridge implementations. The forward matrix is an isometry; no ill-conditioned inverse problem is required for this phenomenon. The minimax criterion is normalized **solution discrepancy** against the classical parameter-one ridge solution, not residual norm, Bayesian risk, or reconstruction from stochastic noise. Infinite-dimensional or finite-precision extensions are not proved. Bibliographic priority beyond the inspected sources remains subject to independent review.

## References

[1] A. N. Brown, J. Chung, J. G. Nagy, and M. Sabaté Landman, *Inner Product Free Krylov Methods for Large-Scale Inverse Problems*, arXiv:2409.05239 (first public arXiv version, 2024-09-08), Sections 2.2–4. https://arxiv.org/abs/2409.05239

[2] A. N. Brown, M. Sabaté Landman, and J. G. Nagy, *H-CMRH: a novel inner product free hybrid Krylov method for large-scale inverse problems*, arXiv:2401.06918 (2024-01-12), Section 4. https://arxiv.org/abs/2401.06918

[3] M. Sabaté Landman, A. N. Brown, J. Chung, and J. G. Nagy, *Randomized and Inner-product Free Krylov Methods for Large-scale Inverse Problems*, arXiv:2502.02721 (2025-02-04), Sections 3.1–3.3. https://arxiv.org/abs/2502.02721
