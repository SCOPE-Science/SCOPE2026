# A sharp mode-bypass transition for Brownian-bridge approximations of Ornstein–Uhlenbeck endpoints

## Finding

Fix a one-step Ornstein–Uhlenbeck stochastic differential equation
\[
 dX_t=-\lambda(X_t-m)\,dt+\sigma\,dW_t,\qquad X_0=x_0,
\]
with \(\lambda,h>0\), \(\sigma\ne0\), deterministic \(x_0,m\in\mathbb R\), and \(q=\lambda h\). Retain the exact Brownian increment and exactly two sine frequencies from the standard Brownian-bridge expansion, then integrate the resulting smooth-forcing differential equation exactly over the step. Among *every* pair of positive integer frequencies, the least mean-square endpoint error is attained by
\[
 S_{\mathrm{opt}}(q)=
 \begin{cases}
 \{1,3\},&0<q<q_*,\\
 \{1,2\},&q>q_*,
 \end{cases}
\]
with both pairs optimal at equality. The sole switching point \(q_*=0.9700737596015445759\ldots\) is the unique positive solution of
\[
 e^{-q_*}(2q_*^2+13\pi^2)=5\pi^2.
\]
In particular, the second harmonic is *strictly inferior* to the third harmonic throughout the low-damping regime. In that regime, for the same two Gaussian bridge coefficients, selecting \(\{1,3\}\) instead of the usual consecutive frequencies \(\{1,2\}\) lowers endpoint mean-square error by a relative proportion tending to
\[
 \frac{8/(81\pi^4)}{1/12-8/\pi^4}
 =0.8410990891189896\ldots\quad\text{as }q\downarrow0.
\]

More generally, for any fixed number \(K\ge1\) of retained bridge frequencies, an optimal set is obtained by selecting the \(K\) largest explicitly computable weights defined below. Such a set always consists of an initial segment of the odd indices together with an initial segment of the even indices. For sufficiently small positive \(q\), the unique optimal set is \(\{1,3,\ldots,2K-1\}\); for sufficiently large \(q\), it is \(\{1,2,\ldots,K\}\). These statements concern mode selection within the specified Fourier bridge basis, not optimality among arbitrary Gaussian couplings or path representations.

## Assumptions and scope

Let \(W\) be a standard Brownian motion on \([0,h]\). Set \(\xi_0=W_h/\sqrt h\), and, for each integer \(j\ge1\), set
\[
 \xi_j=\sqrt{\frac2h}\int_0^h\cos\left(\frac{j\pi s}{h}\right)dW_s.
\]
The family \((\xi_j)_{j\ge0}\) is independent standard Gaussian, by orthonormality and joint Gaussianity. For any finite \(S\subset\mathbb N\), define the smooth approximation
\[
 W_t^{(S)}=\frac{t}{\sqrt h}\xi_0+
 \frac{\sqrt{2h}}\pi\sum_{j\in S}\frac{\xi_j}{j}
 \sin\left(\frac{j\pi t}{h}\right),\qquad 0\le t\le h.
\]
It has the exact endpoints \(W_0^{(S)}=0\) and \(W_h^{(S)}=W_h\). Let \(X_h^{(S)}\) be the endpoint obtained by solving the random ordinary differential equation
\[
 \frac{dX_t^{(S)}}{dt}=-\lambda(X_t^{(S)}-m)+\sigma\frac{dW_t^{(S)}}{dt},
 \qquad X_0^{(S)}=x_0,
\]
exactly. The error \(\mathcal E_S=\mathbb E[(X_h-X_h^{(S)})^2]\) is a *strong*, same-Brownian-path endpoint error. All finite sets and all positive \(q\) are included. The Gaussian coefficients are not freely reoptimized: they are the canonical orthogonal projections of the original Brownian path.

## Proof

**1. Complete cosine representation.** Put \(g(s)=e^{-\lambda(h-s)}\). Variation of constants gives
\[
 X_h=m+(x_0-m)e^{-q}+\sigma\int_0^h g(s)\,dW_s.
\]
The normalized constant and cosine functions form a complete orthonormal basis of \(L^2[0,h]\). By Itô isometry and completeness, the stochastic integral is the \(L^2\)-convergent sum of its Gaussian basis coefficients. Differentiating the finite smooth bridge expansion and solving the random ordinary differential equation yields precisely the same terms for indices \(0\) and \(S\). Thus the omitted coefficients give the entire error.

The constant coefficient is \(\sqrt h\,(1-e^{-q})/q\). For \(j\ge1\), an elementary exponential-cosine integral gives
\[
 c_j=\sqrt{\frac2h}\int_0^h g(s)\cos\left(\frac{j\pi s}{h}\right)ds
 =\sqrt{2h}\,q\,\frac{(-1)^j-e^{-q}}{q^2+\pi^2j^2}.
\]
In consequence, with \(w_j(q)=2q^2[(-1)^j-e^{-q}]^2/(q^2+\pi^2j^2)^2\),
\[
 \boxed{\mathcal E_S=\sigma^2h\sum_{j\ge1,\,j\notin S}w_j(q).}
\]
The series converges absolutely, since its terms decay as \(O(j^{-4})\). Equivalently, Parseval and the exact integral of \(g^2\) give a formula requiring only the retained indices:
\[
 \frac{\mathcal E_S}{\sigma^2h}=
 \frac{1-e^{-2q}}{2q}
 -\left(\frac{1-e^{-q}}q\right)^2-\sum_{j\in S}w_j(q).
\]

**2. Optimal sets.** Since every retained frequency subtracts its own positive weight and all Gaussian coordinates are orthogonal, minimization over subsets of cardinality \(K\) is exactly selection of the \(K\) largest \(w_j(q)\). The common numerator within each parity class and the strictly increasing denominators show strict decrease with the frequency within each parity class. Hence each optimal set may be chosen as a union of initial odd and even segments (ties between different parities can give more than one optimal set).

For any odd \(a\) and larger even \(b>a\), both the numerator and reciprocal denominator of \(w_a\) exceed those of \(w_b\), so \(w_a>w_b\). In particular \(w_1\) always dominates all other weights. The second-largest weight must therefore be one of \(w_3\) and \(w_2\). Their positive square roots satisfy
\[
 \sqrt{\frac{w_3}{2q^2}}=
 \frac{1+e^{-q}}{q^2+9\pi^2},\qquad
 \sqrt{\frac{w_2}{2q^2}}=
 \frac{1-e^{-q}}{q^2+4\pi^2}.
\]
Cross multiplication shows \(w_3>w_2\) precisely when
\[
 e^{-q}(2q^2+13\pi^2)>5\pi^2.
\]
The left side decreases strictly on \((0,\infty)\), because its derivative equals
\[
 -e^{-q}\bigl(2(q-1)^2+13\pi^2-2\bigr)<0.
\]
It starts at \(13\pi^2\), ends at zero, and crosses \(5\pi^2\) exactly once. This proves the sharp two-mode classification, including the tie at equality.

**3. All fixed budgets and the small-damping gain.** For odd \(j\), \(w_j(q)/q^2\to8/(\pi^4j^4)\) as \(q\downarrow0\); for even \(j\), the same ratio tends to zero. For any fixed \(K\), the first \(K\) odd weights have a positive limiting minimum after division by \(q^2\), while every even weight is bounded above by its \(j=2\) counterpart, which is \(o(q^2)\), and every larger odd weight is below the last chosen odd weight. This proves the small-\(q\) optimal set. For \(q\to\infty\), put \(t=e^{-q}\). Every \(j\le K\) has \(\sqrt{w_j/(2q^2)}\ge(1-t)/(q^2+K^2\pi^2)\), while every \(j>K\) has \(\sqrt{w_j/(2q^2)}\le(1+t)/(q^2+(K+1)^2\pi^2)\). The former bound is larger for all sufficiently large \(q\), since the difference of the cross-multiplied numerators is \((2K+1)\pi^2-t(2q^2+(K^2+(K+1)^2)\pi^2)>0\) eventually. Thus \(\{1,\ldots,K\}\) is the unique large-\(q\) optimal set.

Finally, dominated convergence applied to the absolutely summable weights gives
\[
 \lim_{q\downarrow0}\frac{\mathcal E_{\{1,2\}}}{\sigma^2h q^2}
 =\frac8{\pi^4}\sum_{j\ge3,\,j\text{ odd}}j^{-4}
 =\frac1{12}-\frac8{\pi^4},
\]
using \(\sum_{j\ge1,\,j\text{ odd}}j^{-4}=\pi^4/96\). Subtracting the retained third-mode contribution gives
\[
 \lim_{q\downarrow0}\frac{\mathcal E_{\{1,3\}}}{\sigma^2h q^2}
 =\frac1{12}-\frac8{\pi^4}-\frac8{81\pi^4}.
\]
Both constants are strictly positive. Their difference divided by the first is the claimed \(84.1099\ldots\%\) improvement. This completes the proof.

## Verification

The included standalone standard-library script `verify_modes.py` checks the coefficient integral by independent Simpson quadrature, global frequency rankings on sampled parameter grids, the exact Parseval residual against truncated positive series with a controlled tail, the crossover equation, and the small-parameter limit. The complete script passes 127 checks. These numerical checks are not used to infer the infinite-frequency result or the unique boundary; both follow from the analytic proof.

## Relationship to prior work

Binkowski, Christian, Götschel and Minion (first available October 16, 2026) motivate smooth Brownian-bridge truncations for spectral-deferred-correction SDE solvers, and discuss the effect of the number of retained modes. The present result addresses a different decision: which frequencies to retain for the exact OU endpoint at a fixed small coefficient budget. Koskela and Relton (2020, Theorem 6) give an orthogonal truncation-error decomposition for a *different*, half-integer-frequency Karhunen–Loève expansion of unconditioned Brownian motion, with consecutive truncation. Their orthogonality mechanism is consistent with this proof but does not supply the sharp bridge-basis two-frequency crossover. Foster, Lyons and Oberhauser (2020) optimize a polynomial Brownian approximation with path-level weighted error and iterated-integral criteria, rather than selecting two frequencies in a sine bridge expansion to minimize the OU endpoint error. Foster and Habermann (2022) give the standard sine bridge expansion and analyze Fourier and polynomial approximations of Brownian Lévy area, but not the present Ornstein–Uhlenbeck endpoint objective or the two-mode crossover.

## Limitations

This is not a proof of efficiency for a complete spectral-deferred-correction implementation: the random differential equation is assumed solved exactly, and numerical quadrature, adaptivity, global accumulation, and nonlinear drifts are excluded. An exact scalar OU transition can be simulated directly from one Gaussian random variable; the claim is about strong approximation *under a prescribed Brownian-path Fourier coupling*, which is relevant as a calibration for more general smooth-forcing SDE integrators. The chosen subset need not minimize mean-square error of the full Brownian path, and no superiority is asserted over polynomial, adaptive, non-Gaussian, or freely chosen linear-functional approximations. Historical priority among less-indexed Fourier-bridge SDE studies remains uncertain. Independent external mathematical validation has not been performed.

## References

1. L. Binkowski, M. R. Christian, S. Götschel and M. L. Minion, *Toward Spectral Deferred Correction Methods for Stochastic Differential Equations*, arXiv:2610.23693v1 (public October 16, 2026), https://arxiv.org/abs/2610.23693.
2. A. Koskela and S. D. Relton, *Sampling of Stochastic Differential Equations using the Karhunen–Loève Expansion and Matrix Functions*, arXiv:2004.05687v1 (2020), https://arxiv.org/pdf/2004.05687.
3. J. Foster, T. Lyons and H. Oberhauser, *An Optimal Polynomial Approximation of Brownian Motion*, arXiv:1904.06998, SIAM J. Numer. Anal. 58 (2020), https://arxiv.org/pdf/1904.06998.
4. J. Foster and K. Habermann, *Brownian bridge expansions for Lévy area approximations and particular values of the Riemann zeta function*, Combinatorics, Probability and Computing 32 (2023), first online November 3, 2022, https://doi.org/10.1017/S096354832200030X.
