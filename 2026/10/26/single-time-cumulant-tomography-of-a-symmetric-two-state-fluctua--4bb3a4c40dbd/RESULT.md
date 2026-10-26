# Single-time cumulant tomography of a symmetric two-state fluctuating diffusivity

## Finding

A single fixed observation time suffices to identify **both** positive diffusivity levels and the switching rate of an equilibrated symmetric two-state diffusion, provided one measures displacement cumulants of orders two, four, and eight. Specifically, write \(V=\kappa_2(X_t)\), \(C=\kappa_4(X_t)\), and \(E=\kappa_8(X_t)\). Put
\[
f(x)=x-1+e^{-x},\qquad I(x)=\frac x2-\frac54+(x+1)e^{-x}+\frac14e^{-2x},\quad x>0.
\]
The dimensionless ratio
\[
Q=-\frac E{C^2}=\frac{140 I(x)}{f(x)^2}
\]
is a **strictly decreasing bijection** from \((0,\infty)\) onto \((0,70/3)\). Thus the three cumulants identify all three model parameters, rather than merely their combinations.

Conversely, a triple \((V,C,E)\) of real measurements is *exactly realizable* as the indicated three cumulants of this model with both diffusivity levels strictly positive if and only if
\[
V>0,\quad C>0,\quad E<0,\quad 0<-E/C^2<70/3,\quad C<6V^2f(x)/x^2,
\]
where \(x\) is the unique positive solution of \(140I(x)/f(x)^2=-E/C^2\). The final inequality is essential: it enforces positivity of the smaller diffusivity. These are exact-population claims, not statistical confidence guarantees.

## Assumptions and scope

Fix a known \(t>0\). Let \(S_s\in\{+1,-1\}\) be a continuous-time Markov chain started in its stationary distribution \((1/2,1/2)\), switching from either state to the other at rate \(k>0\). Let \(W\) be an independent standard Brownian motion. Fix \(\mu>a>0\) and define
\[
X_t=\sqrt2\int_0^t\sqrt{\mu+aS_s}\,dW_s.
\]
The instantaneous diffusivities are \(D_+=\mu+a\) and \(D_-=\mu-a\); both must be strictly positive. Labels are interchangeable. We use the standard convention \(\kappa_j(Z)=\left.\frac{d^j}{du^j}\log\mathbb E e^{uZ}\right|_{u=0}\). The time \(t\) is known, and all assertions concern the population distribution of \(X_t\), not a finite empirical sample.

## Proof

**1. Reduction to integrated telegraph occupation.** Set \(\lambda=2k\), \(x=\lambda t\), \(Y_t=\int_0^t S_s\,ds\), and \(A_t=\mu t+aY_t\). Conditional on the telegraph trajectory, \(X_t\) is centered Gaussian of variance \(2A_t\), so
\[
\log\mathbb E e^{uX_t}=\log\mathbb E e^{u^2A_t}=\mu t u^2+\log\mathbb E e^{au^2Y_t}.
\]
The stationary symmetric telegraph chain has \(Y_t\overset d=-Y_t\). Hence its odd cumulants vanish and, beyond the variance, all displacement cumulants of order \(4m+2\) for integers \(m\ge1\) vanish identically. More generally,
\[
\kappa_{2m}(X_t)=\frac{(2m)!}{m!}\,\kappa_m(A_t),\qquad m=1,2,3,\ldots.
\]

**2. Exact fourth and eighth displacement cumulants.** The telegraph correlation is \(\mathbb E(S_sS_u)=e^{-\lambda|s-u|}\). Direct integration gives
\[
\kappa_2(Y_t)=2\int_0^t(t-v)e^{-\lambda v}\,dv=\frac{2f(x)}{\lambda^2}.
\]
For ordered times \(s_1<s_2<s_3<s_4\), the four-point *connected* spin correlation is
\[
\operatorname{cum}(S_{s_1},S_{s_2},S_{s_3},S_{s_4})=-2\exp\{-\lambda[(s_2-s_1)+2(s_3-s_2)+(s_4-s_3)]\}.
\]
Indeed the four-spin expectation pairs successive Markov increments, and subtracting all three pair contractions leaves precisely the displayed expression. Integrating over all \(4!\) time orderings and scaling the successive gaps by \(\lambda\) yields
\[
\kappa_4(Y_t)=-\frac{48}{\lambda^4}\int_{\substack{u,v,w\ge0\\u+v+w\le x}}(x-u-v-w)e^{-u-2v-w}\,du\,dv\,dw=-\frac{48I(x)}{\lambda^4}.
\]
The triple integral has Laplace transform (in \(x\)) \(1/[p^2(p+1)^2(p+2)]\); elementary partial fractions give exactly the stated \(I(x)\). In particular \(f(x)>0\) and \(I(x)>0\) for \(x>0\). Applying the Gaussian-mixture cumulant identity gives
\[
\boxed{\kappa_2(X_t)=2\mu t,\quad\kappa_4(X_t)=\frac{24a^2f(x)}{\lambda^2},\quad\kappa_8(X_t)=-\frac{80640a^4I(x)}{\lambda^4}.}
\]
Equivalently, use \(\lambda=x/t\) to obtain the asserted formulas involving \(t\).

**3. Strict monotonicity, including both boundaries.** Let \(N(x)=I'(x)f(x)-2I(x)f'(x)\). A direct expansion, not a numerical sign test, yields
\[
2e^{2x}N(x)=(4-x)e^{2x}-(2x^2+8)e^x+(x+4)=:P(x).
\]
The Maclaurin coefficients of \(P\) vanish through order five. For every integer \(n\ge6\), its coefficient of \(x^n\) equals
\[
\frac{2^{n-1}(8-n)-2n(n-1)-8}{n!}.
\]
This is strictly negative for \(n=6,7\), and manifestly negative for every \(n\ge8\). Thus the *convergent entire series* gives \(P(x)<0\), and \(Q'(x)=140N(x)/f(x)^3<0\), for every \(x>0\). As \(x\downarrow0\), \(f(x)\sim x^2/2\) and \(I(x)\sim x^4/24\), so \(Q(x)\to70/3\). As \(x\to\infty\), \(f(x)\sim x\) and \(I(x)\sim x/2\), so \(Q(x)\to0\). This proves the sharp bijection.

**4. Necessity, sufficiency, and uniqueness of inversion.** Necessity of \(V,C>0\), \(E<0\), and the sharp ratio interval follows from steps 2–3. The ratio determines the unique positive \(x\), and hence \(k=x/(2t)\). Algebraically,
\[
\mu=\frac V{2t},\qquad a=\frac xt\sqrt{\frac C{24f(x)}}.
\]
The strict inequality \(a<\mu\) is exactly \(C<6V^2f(x)/x^2\). Conversely, if all stated conditions hold, these formulas define \(\mu>a>0\), \(k>0\), and substitution reproduces the prescribed second, fourth, and eighth cumulants. Every admissible model must use these same parameters; uniqueness follows. Exchanging \(D_+\) with \(D_-\) amounts only to relabeling the hidden states. When \(a=0\), all cumulants beyond two vanish and no switching-rate identification from \(X_t\) is possible; that boundary is therefore excluded.

## Verification

The accompanying standalone Python program `verification/checker.py` uses symbolic algebra to verify the inverse Laplace transform, the explicit derivative identity, the first six zero Maclaurin coefficients and subsequent sample coefficients, and both boundary limits. Separately, it computes cumulants from an independent two-by-two telegraph matrix-exponential moment-generating function at four positive parameter points with 70-digit precision, then reconstructs the original parameters. The exact proof above establishes the infinite sign claim; finite symbolic or numerical checks alone do not.

To run: `python verification/checker.py`. Requires Python 3, SymPy and mpmath.

## Relationship to prior work

Chubynsky and Slater (2014) motivate Gaussian displacement mixtures from a fluctuating diffusivity and the coexistence of linear mean-square displacement and non-Gaussian displacement statistics. Miyaguchi, Akimoto and Yamamoto (2016) provide two-state fluctuating-diffusivity renewal analysis and fourth-moment/non-Gaussian observables, with power-law-sojourn cases emphasized. A particularly important later, stronger **forward** result is Guéneau, Majumdar and Schehr (2025), which provides finite-time even displacement moments for switching diffusivities, including specializations from which the forward cumulants above may be calculated. We do not claim novelty for those forward formulas in isolation. The specifically assessed contribution here is the nontrivial strict monotonicity and full \(0<Q<70/3\) image of a fixed-time eighth-to-fourth cumulant ratio, followed by the necessary-and-sufficient *positive-diffusivity* realization test and one-time inverse identifiability. No theorem directly supplying that classification was found in the inspected primary material; literature priority remains subject to broader review.

## Limitations

The underlying environmental process must be stationary, symmetric and Markovian, with equal switching rates, and noise independent of the environment. The observation time must be known. Unobserved-state relabeling is not resolvable. General asymmetric switching, continuously distributed diffusivities, drift, resetting, and measurement noise are not covered. Finite-data estimation of eighth cumulants can be unstable, particularly near the fast-switching or zero-contrast limits; this is a population-identifiability theorem and offers no sample-complexity or confidence statement. The forward cumulants are consequences of pre-existing general formulae; the strict inverse classification is the assessed result. Independent external verification and an exhaustive historical priority search have not occurred.

## References

1. M. V. Chubynsky and G. W. Slater, “Diffusing diffusivity: A model for anomalous and anomalous yet Brownian diffusion,” arXiv:1404.3573, first public 14 April 2014; https://arxiv.org/abs/1404.3573 .
2. T. Miyaguchi, T. Akimoto and E. Yamamoto, “Langevin equation with fluctuating diffusivity: a two-state model,” arXiv:1605.00106, first public 30 April 2016; https://arxiv.org/abs/1605.00106 .
3. M. Guéneau, S. N. Majumdar and G. Schehr, “Large Deviations in Switching Diffusion: from Free Cumulants to Dynamical Transitions,” arXiv:2501.13754, first public 23 January 2025; https://arxiv.org/abs/2501.13754 .
