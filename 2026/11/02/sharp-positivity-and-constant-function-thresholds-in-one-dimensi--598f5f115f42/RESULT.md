# Sharp positivity and constant-function thresholds in one-dimensional Chebyshev–Korobov quadrature

## Finding

For each integer \(n\ge 2\), put \(t_j=j/n\) on \(\mathbb T=\mathbb R/\mathbb Z\), for \(0\le j<n\), and consider the strictly positive-definite periodic kernel
\[
K_\gamma(t)=1+\gamma\sum_{h\in\mathbb Z\setminus\{0\}}\frac{e^{2\pi iht}}{h^2},\qquad \gamma>0.
\]
The target probability density is \(\mu(t)=\frac\pi2|\sin(2\pi t)|\). Let \(G_{ij}=K_\gamma(t_i-t_j)\), \(b_i=\int_0^1K_\gamma(t_i-y)\mu(y)\,dy\), and \(w=G^{-1}b\). These are the unique optimal kernel quadrature weights for these fixed nodes.

Define the nonnegative periodic tent masses, the auxiliary quantities, and a parity-dependent integer by
\[
\phi_j(t)=\bigl(1-n\operatorname{dist}_{\mathbb T}(t,t_j)\bigr)_+,
\quad q_j=\int_0^1\phi_j(t)\mu(t)\,dt,
\quad d_n=\begin{cases}n,&n\text{ even},\\2n,&n\text{ odd},\end{cases}
\]
\[
B_n=\frac{\pi^2}{3n^2},\qquad
A_n=\frac{\pi}{d_n}\cot\frac{\pi}{d_n}+\frac{\pi^2}{3d_n^2}-1<0,
\qquad q_0=\frac12-\frac{n}{4\pi}\sin\frac{2\pi}{n}>0.
\]
Then, **for every** \(n\ge2\) and \(\gamma>0\), the full vector of optimal weights satisfies the exact identity
\[
\boxed{w_j=q_j-\frac{\gamma(B_n-A_n)}{n(1+\gamma B_n)},\qquad 0\le j<n.}
\]
Moreover \(\min_jq_j=q_0\). Hence the **sharp all-weight positivity threshold** is
\[
\boxed{\Gamma_{\mathrm{pos}}(n)=\frac{nq_0}{B_n-A_n-nq_0B_n}.}
\]
Every weight is strictly positive for \(0<\gamma<\Gamma_{\mathrm{pos}}(n)\); every weight is nonnegative exactly when \(0<\gamma\le\Gamma_{\mathrm{pos}}(n)\); and at least one is negative for \(\gamma>\Gamma_{\mathrm{pos}}(n)\). At equality the weight at the zero-density node vanishes. The threshold has the sharp two-term asymptotic
\[
\boxed{\Gamma_{\mathrm{pos}}(n)=n+\frac{\pi^2}{3}+O(n^{-1}).}
\]
For any sequence \(\gamma_n/n\to\rho\in[0,\infty)\),
\[
\boxed{n^2w_0\longrightarrow\frac{\pi^2}{3}(1-\rho).}
\]
In particular every fixed \(\gamma>0\) yields eventually positive weights, while ratios \(\rho>1\) yield eventually negative weights at a density minimum.

A **separate later transition** governs the rule's value on the positive constant function:
\[
\boxed{\sum_{j=0}^{n-1}w_j=\frac{1+\gamma A_n}{1+\gamma B_n}.}
\]
This value is negative exactly when \(\gamma>\Gamma_{\mathrm{mass}}(n):=-1/A_n\), with
\[
\boxed{\Gamma_{\mathrm{mass}}(n)\sim\frac{45d_n^4}{\pi^4}.}
\]
Thus the two natural sign thresholds live on different scales, order \(n\) and order \(n^4\), and the second carries a factor-sixteen even/odd parity effect at equal \(n\). For \(n\ge3\), \(\Gamma_{\mathrm{pos}}(n)<\Gamma_{\mathrm{mass}}(n)\); for \(n=2\), equality holds.

## Assumptions and scope

The interpolation space is the real periodic reproducing-kernel Hilbert space associated with the explicitly normalized \(K_\gamma\), containing constants and once-differentiable functions of finite periodic Sobolev energy. The entire one-dimensional equispaced lattice is used (no subsampling), with one exact kernel-mean integral per node. The target density is the explicitly normalized half-periodic sine density above. All statements are exact-arithmetic identities; positivity means positivity of the **optimal unconstrained** weights, not weights obtained by subsequently imposing a sign constraint. The source's more general smoothness and dimensional settings are not asserted to satisfy these formulas.

## Proof

**1. Fourier diagonalization and the tent identity.** The kernel has strictly positive Fourier coefficients \(\lambda_0=1\) and \(\lambda_h=\gamma/h^2\) for \(h\ne0\). The circulant Gram matrix therefore has strictly positive eigenvalues \(n\sum_{h\equiv r\pmod n}\lambda_h\) for all \(0\le r<n\), so \(w\) is uniquely defined. Write \(\widehat\mu(h)=\int_0^1\mu(t)e^{-2\pi iht}\,dt\). Direct integration of \(|\sin|\) gives
\[
\widehat\mu(0)=1,\quad\widehat\mu(h)=0\ (h\text{ odd}),\quad
\widehat\mu(h)=-\frac{1}{h^2-1}\ (h\ne0\text{ even}).
\]
Let \(\mathcal F_nv(r)=\sum_{j=0}^{n-1}v_j e^{-2\pi irj/n}\). Circulant diagonalization of \(Gw=b\) yields
\[
\mathcal F_nw(r)=
\frac{\sum_{h\equiv r\,\mathrm{mod}\, n}\lambda_h\widehat\mu(h)}
{\sum_{h\equiv r\,\mathrm{mod}\, n}\lambda_h}.
\]
The periodic tent \(\phi_0\) has Fourier coefficients
\[
\widehat\phi_0(h)=\frac1n\left(\frac{\sin(\pi h/n)}{\pi h/n}\right)^2
\]
(with the value at \(h=0\) interpreted by continuity). Since \(q_j=(\phi_0*\mu)(t_j)\), aliasing gives \(\mathcal F_nq(r)=n\sum_{h\equiv r\pmod n}\widehat\phi_0(h)\widehat\mu(h)\). For \(r\ne0\) the identity
\[
\sum_{h\equiv r\,\mathrm{mod}\,n}\frac1{h^2}
=\frac{\pi^2}{n^2\sin^2(\pi r/n)}
\]
shows term by term that \(\mathcal F_nw(r)=\mathcal F_nq(r)\). Thus \(w_j-q_j\) is a common constant, determined entirely by the zero Fourier mode.

**2. Evaluation of the zero mode.** Put
\[
B_n=\sum_{\ell\ne0}(n\ell)^{-2}=\frac{\pi^2}{3n^2},
\qquad A_n=\sum_{\ell\ne0}\frac{\widehat\mu(n\ell)}{(n\ell)^2}.
\]
Only even nonzero frequencies contribute to \(A_n\). With \(d_n=n\) for even \(n\) and \(d_n=2n\) for odd \(n\), this becomes
\[
A_n=-2\sum_{m=1}^{\infty}\frac{1}{(d_nm)^2((d_nm)^2-1)}.
\]
Using the classical Mittag–Leffler sum for \(\pi\cot(\pi z)\) yields the displayed closed form for \(A_n\), and in particular \(A_n<0\). Because the tents form a partition of unity, \(\mathcal F_nq(0)=\sum_jq_j=1\), while \(\mathcal F_nw(0)=(1+\gamma A_n)/(1+\gamma B_n)\). The common difference is therefore \(-\gamma(B_n-A_n)/[n(1+\gamma B_n)]\), proving the exact weight and total-mass identities.

**3. Sharp location of the minimum.** The density \(\mu\) has period \(1/2\) and is increasing as a function of circular distance from zero on the circle of circumference \(1/2\). Fold the tent onto that circle, setting \(\Psi_n(t)=\phi_0(t)+\phi_0(t+1/2)\). It is nonnegative, symmetric, and nonincreasing with circular distance \(s\) from zero, \(0\le s\le1/4\). Indeed \(\Psi_2(s)=1\); \(\Psi_3(s)=1-3s\) for \(0\le s\le1/6\) and \(1/2\) for \(1/6\le s\le1/4\); and for \(n\ge4\), \(\Psi_n(s)=(1-ns)_+\). The function \(g=\pi/2-\mu\) is nonnegative, symmetric and nonincreasing on the same circle. By the layer-cake representation, \((g*\Psi_n)(t)\) is a positive superposition of intersection lengths of pairs of centered circular arcs; each is maximal when the arc centers coincide. Therefore \((g*\Psi_n)(t)\le(g*\Psi_n)(0)\). The folded convolution \(q_j=(\mu*\Psi_n)(t_j)\) is consequently minimal at \(t_j=0\). Finally, direct integration of \(\mu(t)(1-n|t|)\) over \(|t|\le1/n\) gives \(q_0=1/2-n\sin(2\pi/n)/(4\pi)\).

**4. Both exact thresholds.** The common offset from Step 2 is strictly increasing in \(\gamma\), ranging from zero to \((B_n-A_n)/(nB_n)\). Thus all weights are nonnegative precisely when \(q_0\ge\gamma(B_n-A_n)/[n(1+\gamma B_n)]\), equivalent to the displayed \(\Gamma_{\mathrm{pos}}(n)\). Its denominator is positive, since \(nq_0\le\sum_jq_j=1\) and \(-A_n>0\). The sign of \(\sum_jw_j\) is the sign of \(1+\gamma A_n\). To compare thresholds, observe
\[
\frac{\Gamma_{\mathrm{pos}}(n)}{\Gamma_{\mathrm{mass}}(n)}
=\frac{-A_n\,nq_0}{B_n(1-nq_0)-A_n}<1
\]
whenever \(nq_0<1\); that strict inequality holds for \(n\ge3\), while \(nq_0=1\) at \(n=2\). No numerical approximation is used for these sign classifications.

**5. Asymptotic scales.** Taylor expansions yield
\[
q_0=\frac{\pi^2}{3n^2}-\frac{\pi^4}{15n^4}+O(n^{-6}),\qquad
A_n=-\frac{\pi^4}{45d_n^4}+O(d_n^{-6}).
\]
Substitution into the exact formulas gives \(\Gamma_{\mathrm{pos}}(n)=n+\pi^2/3+O(n^{-1})\), \(\Gamma_{\mathrm{mass}}(n)\sim45d_n^4/\pi^4\), and for \(\gamma_n/n\to\rho\), \(n^2w_0\to(\pi^2/3)(1-\rho)\). The expansions have uniform algebraic remainders across the two parity classes because \(n\le d_n\le2n\).

## Verification

The companion standalone file `verify.py` requires Python 3 with `mpmath` and runs via `python verify.py`. It solves the finite Gram systems directly from the Bernoulli-polynomial kernel and a separately integrated kernel mean; independently integrates the tent masses; compares the two full weight vectors and sign transitions at 65-digit precision. It also checks the sum of weights, the parity-dependent thresholds and the asymptotic scales. The provided run passed 174 supplementary finite checks for sample sizes \(2\le n\le12\) and additional large-grid tests. These experiments support, but do not replace, the analytic proof for all \(n\) and \(\gamma\).

## Relationship to prior work

Bartel, Gilbert, Griebel, Kuo and Sloan (2026), arXiv:2610.01113v1, formulate kernel-interpolatory integration of a periodized function against a nonsmooth Chebyshev-derived density and discuss unresolved general positivity of their optimal weights. The object here is a precisely normalized one-dimensional full-lattice smoothness-one model, with a sharp finite-grid positivity boundary, a constant-function sign boundary, and a parity-sensitive scale separation; no general high-dimensional positivity claim is made.

The classic equivalence of kernel quadrature with integrated kernel cardinal functions, as well as nontrivial general positivity and Sobolev weight-magnitude estimates, appears in Karvonen, Kanagawa and Särkkä (2019). Novak and Zhang (2016) study optimal one-dimensional Sobolev quadrature with general weights under different exactness and norm conventions. Kaarnioja et al. (2021) develop periodic kernel-based lattice interpolation. These known frameworks motivate the calculation but the inspected relevant results do not state the complete two-parameter, parity-sensitive threshold formulas above. An older equivalent special-case spline or kernel-quadrature identity may exist outside the inspected literature; historical priority is not certified.

## Limitations

Only the specified one-dimensional density, smoothness-one periodic Sobolev kernel, full equispaced design, and exact Gram-solve weights are covered. The density is not smooth at its zeros, and the smallest nodal masses are of order \(n^{-2}\); changing the density, kernel normalization, smoothness order, subsampling, or dimension can change both thresholds. The large-\(n\) limit of \(n^2w_0\) at \(\gamma_n/n\to1\) does not settle the sign in that critical second-order scaling. No claims are made about numerical floating-point conditioning, optimality of node placement, or universal positive-weight cubature. Historical priority of any equivalent earlier periodic-spline analysis remains a residual risk.

## References

1. F. Bartel, A. D. Gilbert, M. Griebel, F. Y. Kuo and I. H. Sloan, *A higher order lattice-based method for high-dimensional numerical integration using periodization*, arXiv:2610.01113v1 (first public 2026-10-01). https://arxiv.org/abs/2610.01113
2. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, Statistics and Computing 29 (2019), 1317–1333. https://doi.org/10.1007/s11222-019-09901-0
3. E. Novak and S. Zhang, *Optimal Quadrature Formulas for the Sobolev Space H1*, arXiv:1609.01146 (2016). https://arxiv.org/abs/1609.01146
4. V. Kaarnioja, Y. Kazashi, F. Y. Kuo, F. Nobile and I. H. Sloan, *Fast approximation by periodic kernel-based lattice-point interpolation with application in uncertainty quantification*, Numerische Mathematik (2021). https://doi.org/10.1007/s00211-021-01242-3
