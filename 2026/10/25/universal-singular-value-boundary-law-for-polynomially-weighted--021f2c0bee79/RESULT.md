# Universal singular-value boundary law for polynomially weighted Fock dilations

## Finding
Fix real \(\alpha>0\), \(m>0\), an integer \(k\ge1\), and a complex polynomial \(P(z)=\sum_{j=0}^{k}c_jz^j\) with \(c_k\ne0\). On the radial-power weighted Fock Hilbert space \(F^2_{\alpha,m}\), let \(W_\varepsilon f(z)=P(z)f(e^{-\varepsilon}z)\), \(\varepsilon>0\). Define
\[
\gamma=\frac{k}{m},\qquad C=|c_k|\left(\frac{2}{m\alpha}\right)^\gamma,\qquad g(x)=Cx^\gamma e^{-x}\quad(x\ge0),\qquad M=C\left(\frac{\gamma}{e}\right)^\gamma.
\]
Every \(W_\varepsilon\) belongs to every Schatten quasi-ideal \(\mathcal S_p\) for \(0<p<\infty\). Its complete leading-order singular-value distribution as \(\varepsilon\downarrow0\) is independent of all lower-degree coefficients of \(P\): for every \(y>0\),
\[
\lim_{\varepsilon\downarrow0}\varepsilon\,\#\{j\ge1:\varepsilon^\gamma s_j(W_\varepsilon)>y\}
=\big|\{x>0:g(x)>y\}\big|=:L(y).
\]
Here \(s_1\ge s_2\ge\cdots\) are singular values with multiplicity, and the vertical bars on the right denote Lebesgue measure. If \(0<y<M\), the measure has the explicit two-branch formula
\[
L(y)=\gamma\left[W_0(-\xi_y)-W_{-1}(-\xi_y)\right],\qquad
\xi_y=\frac{(y/C)^{1/\gamma}}{\gamma},
\]
where \(W_0\) and \(W_{-1}\) denote the principal and lower real Lambert \(W\) branches. For \(y\ge M\), \(L(y)=0\). In particular,
\[
\lim_{\varepsilon\downarrow0}\varepsilon^\gamma\|W_\varepsilon\|=M,
\qquad
\lim_{\varepsilon\downarrow0}\varepsilon^{\gamma+1/p}\|W_\varepsilon\|_{\mathcal S_p}
=C\left(\frac{\Gamma(\gamma p+1)}{p^{\gamma p+1}}\right)^{1/p}\quad(0<p<\infty).
\]
For every fixed \(\tau>0\), there is a unique \(y_\tau\in(0,M)\) satisfying \(L(y_\tau)=\tau\), and the optimal rank-\(\lfloor\tau/\varepsilon\rfloor-1\) approximation error obeys
\[
\lim_{\varepsilon\downarrow0}\varepsilon^\gamma s_{\lfloor\tau/\varepsilon\rfloor}(W_\varepsilon)=y_\tau.
\]
The index is positive for sufficiently small \(\varepsilon\).

## Assumptions and scope
The weighted Fock space consists of entire functions with squared Hilbert norm
\[
\|f\|^2_{\alpha,m}=\frac{m\alpha^{2/m}}{2\pi\Gamma(2/m)}\int_{\mathbb C}|f(z)|^2e^{-\alpha|z|^m}\,dA(z),
\]
where \(dA\) denotes the ordinary planar area measure. The normalized monomials \(e_n=z^n/\nu_n\), \(n\ge0\), form an orthonormal basis, with
\[
\nu_n^2=\frac{\Gamma((2n+2)/m)}{\alpha^{2n/m}\Gamma(2/m)}.
\]
The polynomial is fixed while \(\varepsilon\to0^+\), and \(\alpha,m,k,p,\tau,y\) are fixed as explicitly quantified above. The result does not assert uniformity when the polynomial degree or exponent varies with \(\varepsilon\). In particular, the leading coefficient is required nonzero and \(k\ge1\).

## Proof
**1. Exact singular spectrum of each monomial component.** Write \(T_{j,\varepsilon}f(z)=z^j f(e^{-\varepsilon}z)\), \(j\ge0\). Then
\[
T_{j,\varepsilon}e_n=w_{n,j,\varepsilon}e_{n+j},\quad
w_{n,j,\varepsilon}=e^{-\varepsilon n}\alpha^{-j/m}
\left(\frac{\Gamma((2n+2j+2)/m)}{\Gamma((2n+2)/m)}\right)^{1/2}.
\]
These nonnegative weights are exactly the singular values (before decreasing rearrangement) of \(T_{j,\varepsilon}\), since its images of basis vectors are pairwise orthogonal. The elementary gamma-ratio estimate \(\Gamma(t+a)/\Gamma(t)\sim t^a\) as \(t\to\infty\), together with a global upper bound by a constant multiple of \((1+t)^a\), gives
\[
w_{n,j,\varepsilon}=\alpha^{-j/m}\left(\frac{2}{m}\right)^{j/m}n^{j/m}e^{-\varepsilon n}(1+o(1))\quad(n\to\infty),
\]
where the little-oh term is independent of \(\varepsilon\). In particular, \(T_{j,\varepsilon}\) is compact and belongs to every \(\mathcal S_p\) for positive \(p\).

**2. Scalar continuum limit at the top degree.** For \(j=k\), set \(b_{n,\varepsilon}=|c_k|w_{n,k,\varepsilon}\). Uniformly for \(x=\varepsilon n\) in compact subsets of \((0,\infty)\),
\[
\varepsilon^\gamma b_{n,\varepsilon}\longrightarrow g(x)=Cx^\gamma e^{-x}.
\]
The global gamma-ratio bound yields \(\varepsilon^\gamma b_{n,\varepsilon}\le K(\varepsilon(n+1))^\gamma e^{-\varepsilon n}\), with \(K\) independent of small \(\varepsilon\). Consequently, for any positive level \(y\), indices contributing \(\varepsilon^\gamma b_{n,\varepsilon}>y\) stay in a common compact interval of the scaled variable \(\varepsilon n\); the small- and large-\(x\) tails cannot contribute. The superlevel set \(\{x:g(x)>y\}\) has boundary of Lebesgue measure zero, including at \(y=M\); Riemann sums therefore give
\[
\varepsilon\sum_{n\ge0}\mathbf 1_{\{\varepsilon^\gamma b_{n,\varepsilon}>y\}}\longrightarrow L(y).
\]
Since \(g\) has its unique maximum at \(x=\gamma\), maximization gives \(\varepsilon^\gamma\|c_kT_{k,\varepsilon}\|\to M\). Taking \(p\)-th powers, the same global bound makes the tail uniformly integrable and gives, for all real \(p>0\),
\[
\varepsilon^{\gamma p+1}\|c_kT_{k,\varepsilon}\|_{\mathcal S_p}^p\to
\int_0^\infty C^p x^{\gamma p}e^{-px}\,dx
=\frac{C^p\Gamma(\gamma p+1)}{p^{\gamma p+1}}.
\]
The equation \(g(x)=y\), \(0<y<M\), has two positive roots \(-\gamma W_0(-\xi_y)\) and \(-\gamma W_{-1}(-\xi_y)\). The difference of these roots is exactly \(L(y)\).

**3. Lower polynomial terms do not affect the leading spectral law.** Decompose
\[
W_\varepsilon=c_kT_{k,\varepsilon}+R_\varepsilon,
\qquad R_\varepsilon=\sum_{j=0}^{k-1}c_jT_{j,\varepsilon}.
\]
For each \(j\ge0\) and each fixed \(0<p<\infty\), the gamma-ratio bound and a comparison with \(\sum_{n\ge0}(n+1)^a e^{-p\varepsilon n}\) show
\[
\|T_{j,\varepsilon}\|=O(\varepsilon^{-j/m}),\qquad
\|T_{j,\varepsilon}\|_{\mathcal S_p}=O(\varepsilon^{-j/m-1/p}).
\]
For \(j=0\), the first estimate means \(O(1)\). Thus
\[
\varepsilon^\gamma\|R_\varepsilon\|\to0,
\qquad
\varepsilon^{\gamma+1/p}\|R_\varepsilon\|_{\mathcal S_p}\to0.
\]
For \(p\ge1\), ordinary triangle and reverse triangle inequalities preserve the leading Schatten limit; for \(0<p<1\), apply the \(p\)-triangle inequality to the \(p\)-th powers in both directions. The norm limit follows similarly.

Every singular-value rank satisfies the Lipschitz perturbation estimate
\[
|s_j(W_\varepsilon)-s_j(c_kT_{k,\varepsilon})|\le\|R_\varepsilon\|,
\]
by the variational description of singular values as optimal finite-rank approximation errors. Therefore, for any \(y>0\) and small enough \(\varepsilon\), writing \(\delta_\varepsilon=\varepsilon^\gamma\|R_\varepsilon\|\to0\), the top-degree counting functions at levels \(y+\delta_\varepsilon\) and \(y-\delta_\varepsilon\) sandwich the full counting function. The continuous limiting length \(L\) implies the stated all-level limit, including \(y=M\).

Finally, \(L:(0,M)\to(0,\infty)\) is continuous and strictly decreasing, with endpoints \(+\infty\) and \(0\). Inverting the counting limit on either side of \(y_\tau\) yields the ranked singular-value assertion. On a Hilbert space, the optimal rank-\(j-1\) approximation error is exactly \(s_j\), so this is also the claimed approximation-number law.

## Verification
The accompanying self-contained `verify.py` computes exact monomial-basis matrix entries from gamma ratios and checks the finite Hilbert–Schmidt identity, singular-value perturbation inequality, limiting norm and Schatten constants, and the two-branch counting formula. It tests multiple radial exponents and nonmonomial complex polynomials. All 42 supplementary checks passed when run against the packaged code. The infinite-dimensional statements follow from the proof above; finite experiments do not establish an infinite limit.

For an independent analytic cross-check, when \(m=2\), \(\alpha=1\), and \(P(z)=z^2\), the monomial weights are \(e^{-\varepsilon n}\sqrt{(n+1)(n+2)}\). Thus
\[
\|W_\varepsilon\|_{\mathcal S_2}^2
=\sum_{n=0}^\infty(n+1)(n+2)e^{-2\varepsilon n}
=\frac{2}{(1-e^{-2\varepsilon})^3},
\]
so \(\varepsilon^3\|W_\varepsilon\|_{\mathcal S_2}^2\to1/4\), agreeing with the general formula \(\gamma=1\), \(C=1\), \(p=2\).

## Relationship to prior work
Barik–Sen–Paul (arXiv:2607.17170, first posted 19 July 2026) introduce and analyze exactly the radial-power Fock normalization used here, describe boundedness, compactness and Hilbert–Schmidt criteria, and explicitly discuss monomial weights \(z^k\) with linear symbols \(\lambda z\). Those results establish qualitative membership facts, not the scaled continuum distribution, Lambert-branch approximation-number curve, or sharp near-boundary all-\(p\) constants proved here.

Mengestie (2013, 2015) and Mengestie–Takele (2023) establish Schatten-class *membership* criteria on various generalized weighted Fock spaces, including \(0<p<\infty\) regimes. No new assertion that compactness implies Schatten membership in this family is claimed. Their criteria do not themselves supply the quantitative two-branch spectral counting law. Lechner–Li–Queffélec–Rodriguez-Piazza (2018) study approximation numbers of weighted composition operators on Hardy space, with a different geometry and symbols.

## Limitations
The result applies to fixed polynomials of degree at least one with a strict radial dilation and to the specified Hilbert norm; it does not extend without proof to entire nonpolynomial weights, affine translations, quasi-Banach Fock norms, or parameter regimes with degree growing as the dilation approaches the identity. The leading asymptotics intentionally discard lower-order polynomial corrections. The counting law does not give finite-\(\varepsilon\) error constants or the limiting multiplicity at the single maximizer. Publication priority should be verified independently; a potentially relevant 2015 trace-ideal full text was not accessible, and search results cannot prove uniqueness.

## References
1. S. Barik, A. Sen, K. Paul, *Weighted composition operators on weighted Fock spaces*, arXiv:2607.17170v1 (19 July 2026), https://arxiv.org/abs/2607.17170. Primary MSC2020 47B38.
2. T. Mengestie and M. H. Takele, *Integral and Weighted Composition Operators on Fock-type Spaces*, Bull. Malays. Math. Sci. Soc. 46, 80 (2023), https://doi.org/10.1007/s40840-023-01476-4, particularly Theorem 3.2.
3. T. Mengestie, *Schatten class weighted composition operators on weighted Fock spaces*, Arch. Math. 101 (2013), 349–360.
4. T. Mengestie, *On trace ideal weighted composition operators on weighted Fock spaces*, Arch. Math. 105 (2015), 453–459, https://doi.org/10.1007/s00013-015-0827-5.
5. G. Lechner, D. Li, H. Queffélec, L. Rodriguez-Piazza, *Approximation numbers of weighted composition operators*, J. Funct. Anal. 274 (2018), 1928–1958, https://doi.org/10.1016/j.jfa.2018.01.010.
