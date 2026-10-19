# Strict fourth-cumulant positivity for finite linear networks driven by Brownian reset reservoirs

## Finding

A Poisson-reset Brownian reservoir, when passed through **any nonzero exponentially stable real linear response**, produces a strictly positive stationary fourth cumulant, even if the impulse response changes sign. This is an all-observable statement, not merely a positivity statement for a particular oscillator coordinate or an assertion based on finite-chain numerics.

Precisely, for the stable finite-dimensional system and independent reservoir processes defined below, put \(h_\ell(s)=c^{\mathsf T}e^{As}b_\ell\), \(s\geq0\). If at least one \(h_\ell\) is not identically zero, then the stationary scalar observation \(Z=c^{\mathsf T}U\) satisfies

\[
\boxed{\operatorname{cum}_4(Z)=\mathbb E[Z^4]-3\mathbb E[Z^2]^2=3\sum_{\ell=1}^{q}\operatorname{Var}(V_\ell)>0.}
\]

For each reservoir, write its reset times backwards from the observation instant as \(0=T_{\ell,0}<T_{\ell,1}<\cdots\), with independent exponential gaps of rate \(r_\ell\). The positive random mixing variance in this exact identity is

\[
\boxed{V_\ell=2D_\ell\sum_{j=0}^{\infty}\int_{T_{\ell,j}}^{T_{\ell,j+1}}\left(\int_{T_{\ell,j}}^{u}h_\ell(s)\,ds\right)^2du.}
\]

More strongly, replacing each Brownian reset reservoir by an independent stationary Gaussian Ornstein–Uhlenbeck reservoir with the **same full two-time covariance function** preserves every stationary second-order spatiotemporal statistic of the linear network, but the replacement model is Gaussian and has zero fourth cumulant. Independent additive Gaussian thermal forcing changes neither fourth cumulant.

## Assumptions and scope

Let \(A\in\mathbb R^{n\times n}\) be Hurwitz (every eigenvalue has negative real part), let \(b_\ell,c\in\mathbb R^n\), and let \(D_\ell,r_\ell>0\) for \(\ell=1,\ldots,q\), where \(n,q\) are arbitrary finite positive integers. Each \(X_\ell(t)\) is the stationary two-sided process that undergoes Brownian diffusion with generator \(D_\ell\partial_{xx}\) between the points of an independent stationary rate-\(r_\ell\) Poisson clock, and is returned to zero at each clock point. Brownian paths and clocks are mutually independent across reservoirs.

The network obeys \(dU_t=A U_t\,dt+\sum_{\ell=1}^q b_\ell X_\ell(t)\,dt+\Sigma\,dW_t\), where \(W\) is an independent standard finite-dimensional Brownian motion and \(\Sigma\) is any fixed compatible real matrix; \(\Sigma=0\) is allowed. Define \(Z_t=c^{\mathsf T}U_t\). A response is called *observable* if \(h_\ell(s)=c^{\mathsf T}e^{As}b_\ell\) is nonzero at some \(s\ge0\). No sign, monotonicity, symmetry, or positivity-preserving assumption is placed on the response.

The claim concerns the unique stationary finite-dimensional solution and its scalar observations. If all responses vanish identically, the reset-induced contribution is zero, and the theorem does not assert strict positivity. The fourth cumulant is not standardized by the variance; independent Gaussian noise can dilute standardized excess kurtosis without changing its unstandardized value.

## Proof

**1. Existence, moments, and second-order covariance.** The stationary reset Brownian process \(X_\ell\) has mean zero, variance \(2D_\ell/r_\ell\), and finite fourth moment \(24D_\ell^2/r_\ell^2\), by mixing the Gaussian Brownian position over its exponential stationary age. Its stationary covariance is

\[
\mathbb E[X_\ell(t)X_\ell(t+s)]=\frac{2D_\ell}{r_\ell}e^{-r_\ell|s|}.
\]

Indeed, if a reset occurs between the two times, their Brownian excursions are centered and independent; otherwise the later value is the earlier value plus independent centered Brownian increments. Because \(A\) is Hurwitz, \(h_\ell\) is a real analytic exponentially decaying function. Therefore \(Z_t=\sum_\ell\int_0^\infty h_\ell(s)X_\ell(t-s)\,ds+Z_t^{\rm th}\) exists in \(L^4\), and \(Z^{\rm th}\) is an independent centered Gaussian stationary linear response to the \(\Sigma\)-noise. The stationary solution is unique by exponential contraction.

**2. Gaussian conditioning and the exact mixing variance.** Condition on the complete Poisson reset clock of one reservoir and take the observation time to be zero. On each backward interval \((T_j,T_{j+1})\), the driving Brownian increments form an independent Gaussian excursion. A Brownian increment at backward age \(u\in(T_j,T_{j+1})\) contributes to the filtered observation with deterministic conditional coefficient \(\int_{T_j}^{u}h(s)\,ds\): only observation times lying between that increment and the next reset can depend on it. Stochastic Fubini and Itô isometry consequently give, conditional on the clock,

\[
Y_h:=\int_0^\infty h(s)X(-s)\,ds\ \sim\ N(0,V_h),\qquad
V_h=2D\sum_j\int_{T_j}^{T_{j+1}}\left(\int_{T_j}^{u}h(s)\,ds\right)^2du.
\]

The finite fourth moment of \(Y_h\) implies \(\mathbb E[V_h^2]<\infty\), since \(\mathbb E[Y_h^4\mid\mathcal P]=3V_h^2\). Hence

\[
\mathbb E[Y_h^4]-3\mathbb E[Y_h^2]^2
=3\bigl(\mathbb E[V_h^2]-(\mathbb E V_h)^2\bigr)=3\operatorname{Var}(V_h).
\]

Independence of the reservoirs and of thermal Gaussian forcing makes fourth cumulants additive, giving the displayed formula for \(Z\).

**3. Nondegeneracy for every nonzero signed response.** We prove a Poisson-gap lemma. Let \(h\) be any real continuous, exponentially decaying function not identically zero, and let \(V_h(\mathcal P)\) be the formula above for a rate-\(r>0\) Poisson point set \(\mathcal P\subset(0,\infty)\). Suppose for contradiction that \(V_h(\mathcal P)=v\) almost surely for a deterministic constant \(v\).

By the elementary Poisson add-one (Mecke) identity, for each finite \(L>0\),

\[
r\int_0^L\mathbb P\{V_h(\mathcal P\cup\{t\})\ne v\}\,dt
=\mathbb E\!\sum_{t\in\mathcal P\cap(0,L)}\mathbf1_{\{V_h(\mathcal P)\ne v\}}=0.
\]

Thus, almost surely, inserting a reset at Lebesgue-almost every \(t>0\) leaves \(V_h\) unchanged. Choose a Poisson-free gap \((a,b)\), where \(a\ge0\) and \(b<\infty\). Write \(F(t)=\int_a^t h(s)\,ds\). Splitting this gap by inserting a reset at \(t\in(a,b)\) changes **only its one summand** of \(V_h\), by the exact amount

\[
\Delta(t)=2D\,F(t)\left[(b-t)F(t)-2\int_t^bF(u)\,du\right].
\]

This continuous function vanishes almost everywhere in the gap and hence everywhere. On any nonempty connected component of the open set \(\{t:F(t)\ne0\}\), the bracket must vanish. Differentiation gives \((b-t)F'(t)+F(t)=0\), so \(F(t)=C(b-t)\) on that component. At its left endpoint, either \(a\) or a zero of \(F\), continuity gives \(F=0\), forcing \(C=0\), a contradiction. Thus \(F\equiv0\) on the gap, and \(h\equiv0\) there. Every positive time except the countably many Poisson points belongs to such a gap; continuity forces \(h\equiv0\) on \([0,\infty)\), contrary to assumption. Therefore \(\operatorname{Var}(V_h)>0\), even for sign-changing \(h\).

**4. Exact Gaussian covariance match.** Replace each \(X_\ell\) by the independent stationary Gaussian process solving \(dG_\ell=-r_\ell G_\ell\,dt+\sqrt{4D_\ell}\,dB_\ell\). Its stationary covariance is exactly \((2D_\ell/r_\ell)e^{-r_\ell|s|}\). Applying the same deterministic linear response preserves every two-time output covariance, including covariance between different observed network coordinates and different time lags. The Gaussian replacement solution is jointly Gaussian and therefore has vanishing fourth cumulant. This completes the theorem.

## Verification

The accompanying standalone `verify.py` uses exact SymPy arithmetic to check a nontrivial scalar case by **two independent methods**: stationary generator moment equations and the conditional-variance Poisson perpetuity. For \(\dot Y=-\kappa Y+X\), it finds

\[
\operatorname{Var}(Y)=\frac{2D}{\kappa r(\kappa+r)},\qquad
\operatorname{cum}_4(Y)=\frac{24D^2(3\kappa+7r)}{\kappa r^2(\kappa+r)^2(2\kappa+r)(3\kappa+r)}>0.
\]

The code also checks a *signed* response \(h(s)=e^{-s}-2e^{-2s}\), realized as an observable of a stable two-mode network with \(D=r=1\). It obtains exact variance \(1/9\) and fourth cumulant \(481/33075>0\), plus four other signed or unsigned combinations. All symbolic checks passed in the packaged program. Finite symbolic examples check normalization and algebra but do **not** substitute for the general Poisson-gap proof.

## Relationship to prior work

Guéneau, Majumdar, and Schehr (arXiv:2306.09453, first posted 15 June 2023) studied the scalar harmonic response driven by resetting Brownian noise via a Kesten-variable recurrence and provided explicit low stationary moments (their Appendix E). The scalar formula above is an algebraic consequence of those already published low moments and is **not** claimed as independently new. The conditional Gaussianity of Brownian excursions is also a standard ingredient, not a new probabilistic tool.

Sarkar and Roy (arXiv:2307.06127, first posted 12 July 2023) studied harmonic chains driven by two resetting Brownian walls. Their finite-size velocity-kurtosis findings, including numerically positive examples and bulk decay, are prior results. The present theorem instead proves an exact strict sign for every nonzero **signed** scalar linear response of every finite Hurwitz network, with any number of independent reset reservoirs, and proves that its full two-time covariance is indistinguishable from a corresponding Gaussian colored-reservoir model. It does not claim that finite-chain non-Gaussianity or positive examples were previously unknown.

## Limitations

The strict result requires independent Brownian excursions with independently resetting Poisson clocks, linear stable finite-dimensional dynamics, and at least one observable reservoir-to-output path. It does not cover nonlinear interactions, non-Brownian excursions, correlated reset clocks, infinite networks lacking integrability, or parity-sensitive physical entropy production. Strict positivity can coexist with an arbitrarily small excess kurtosis, and no lower bound uniform over all filters or network sizes is asserted. The statement's literature priority has not undergone independent audit; broad results on Gaussian variance mixtures could subsume aspects of the proof.

## References

1. M. Guéneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453, initial submission 2023-06-15, especially §§2, 4.1–4.2 and Appendix E, https://arxiv.org/abs/2306.09453.
2. R. Sarkar and P. Roy, *Stationary state of harmonic chains driven by boundary resetting*, arXiv:2307.06127, initial submission 2023-07-12, especially §§2–4, https://arxiv.org/abs/2307.06127.
3. G. Last and M. Penrose, *Lectures on the Poisson Process*, Cambridge University Press (2018), Poisson Mecke/add-one formula; a standard reference for the identity used in the nondegeneracy lemma.
