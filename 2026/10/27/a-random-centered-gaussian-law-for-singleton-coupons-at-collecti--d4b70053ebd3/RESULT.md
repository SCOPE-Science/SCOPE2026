# A random-centered Gaussian law for singleton coupons at collection completion

## Finding

Take independent uniformly selected coupons from \(n\ge2\) types, and stop on the first draw at which every type has appeared. Let \(T_n\) be that draw index and \(S_n\) the number of types that have appeared **exactly once** at that time. Define
\[
L_n=\log n,\qquad X_n=\frac{T_n}{n}-L_n,\qquad
Y_n=\frac{S_n-L_ne^{-X_n}}{\sqrt{L_n}}.
\]
As \(n\to\infty\), the two-scale joint limit is
\[
\boxed{(X_n,Y_n)\ \xrightarrow{\ d\ }\ (G,e^{-G/2}Z),}
\]
where \(G\) is standard Gumbel, \(\mathbb P(G\le x)=\exp(-e^{-x})\), and \(Z\sim N(0,1)\) is **independent** of \(G\). Equivalently, the fully observed, randomly studentized pair satisfies
\[
\boxed{\left(X_n,\ \frac{S_n-L_ne^{-X_n}}{\sqrt{L_ne^{-X_n}}}\right)\ \xrightarrow{\ d\ }\ (G,Z).}
\]
Thus the singleton count has \(\sqrt{\log n}\)-scale asymptotically Gaussian fluctuations after its \(\log n\)-scale random fluctuations have been removed using the actual completion time. The center \(L_ne^{-X_n}\) is observable without any auxiliary Poisson clock.

An exact supporting identity, not claimed here as independently novel relative to the known finite joint-law work, is
\[
\mathop{\mathrm{Cov}}(T_n,S_n)
=n\bigl(H_n^{(2)}-H_n\bigr),\qquad
H_n=\sum_{j=1}^{n}\frac1j,\quad H_n^{(2)}=\sum_{j=1}^{n}\frac1{j^2}.
\]
In particular the covariance is negative for \(n\ge2\), while the correlation converges to \(-\sqrt6/\pi\). These supporting identities distinguish two scales but are not the originality target of the finding.

## Assumptions and scope

All draws are mutually independent and exactly uniform on \(n\) types. The stopping rule is the **first** completed collection; \(S_n\) includes the last newly observed type, which is necessarily a singleton. The limit is joint weak convergence in \(\mathbb R^2\), not almost sure convergence or a uniform Berry--Esseen bound. For clarity, \(N(0,1)\) means a centered unit-variance Gaussian. The theorem concerns the classical single-coupon-per-draw model; it does not assert the same normalization for unequal coupon weights, bulk package draws, or delayed collection.

## Proof

**1. An exact binomial conditional law.** Attach to the independent coupon labels independent inter-draw waiting times that are exponential with rate \(n\). The pooled process has rate \(n\), and the arrivals of each coupon type form independent rate-one Poisson processes. Let \(W_n\) be the time when all \(n\) types have appeared, and let \(E_i\) be the first arrival time of type \(i\). Then \(E_1,\ldots,E_n\) are independent \(\operatorname{Exp}(1)\) random variables and \(W_n=\max_i E_i\). Also \(S_n\) counts the types having exactly one arrival up to \(W_n\).

Condition on \(W_n=t\) and on the (almost surely unique) type that attains this maximum. That type contributes one singleton. Every other type is an independent rate-one Poisson process conditioned on having its first arrival before \(t\). The chance it has exactly one event by \(t\) is
\[
q(t)=\frac{\mathbb P\{N(t)=1\}}{\mathbb P\{N(t)\ge1\}}
=\frac{t e^{-t}}{1-e^{-t}}=\frac{t}{e^t-1}.
\]
Independence of the remaining \(n-1\) conditioned processes is preserved. Consequently,
\[
\boxed{\quad S_n\mid W_n=t\ \stackrel{d}{=}\ 1+\operatorname{Bin}\bigl(n-1,q(t)\bigr).\quad}\tag{1}
\]
This identity is valid for every \(n\ge2\) and \(t>0\), as a regular conditional distribution. The density of \(W_n\) is \(n e^{-t}(1-e^{-t})^{n-1}\).

**2. Random conditional mean and a Gaussian scale.** Put \(G_n=W_n-L_n\). Its distribution satisfies
\[
\mathbb P\{G_n\le x\}=\bigl(1-e^{-x}/n\bigr)^n\longrightarrow e^{-e^{-x}}
\]
for fixed real \(x\), so \(G_n\Rightarrow G\) and \(G_n=O_{\mathbb P}(1)\). Let \(m_n(t)=(n-1)q(t)\). Uniformly on every compact \(g\)-interval,
\[
\frac{m_n(L_n+g)}{L_n}\longrightarrow e^{-g},\qquad
m_n(L_n+g)-L_ne^{-g}=g e^{-g}+o(1).
\tag{2}
\]
Conditional on \(G_n=g\), the variable \(S_n-1\) is binomial with parameters \(n-1,q(L_n+g)\). Since its mean is asymptotic to \(L_ne^{-g}\), its Bernoulli success probability tends to zero and its centered characteristic function obeys, uniformly on compact \(g\)-sets,
\[
\mathbb E\left[\exp\left(iu\frac{S_n-1-m_n(W_n)}{\sqrt{L_n}}\right)\Bigm|G_n=g\right]
\longrightarrow\exp\left(-\frac{u^2e^{-g}}2\right).
\tag{3}
\]
For example, expand \(\log\{1+q(e^{iu/\sqrt{L_n}}-1)\}-iuq/\sqrt{L_n}\), multiply by \(n-1\), and use \(m_n/L_n\to e^{-g}\) and \(q\to0\). The error is uniform when \(g\) ranges over a compact set. Tightness of \(G_n\), boundedness of characteristic functions and equation (3) give, for every real \(u,v\),
\[
\mathbb E\exp\left(ivG_n+iu\frac{S_n-1-m_n(W_n)}{\sqrt{L_n}}\right)
\longrightarrow
\mathbb E\exp\left(ivG-\frac{u^2e^{-G}}2\right).
\]
This is the joint characteristic function of \((G,e^{-G/2}Z)\), with \(Z\) independent of \(G\). By (2), the deterministic difference between \(1+m_n(W_n)\) and \(L_ne^{-G_n}\) is \(O_{\mathbb P}(1)=o_{\mathbb P}(\sqrt{L_n})\). Thus
\[
\left(G_n,\frac{S_n-L_ne^{-G_n}}{\sqrt{L_n}}\right)
\Rightarrow (G,e^{-G/2}Z).
\tag{4}
\]

**3. Removing the auxiliary continuous clock.** Given the label sequence and its stopping index \(T_n\), the \(T_n\) waiting times have independent \(\operatorname{Exp}(n)\) distributions, independent of the labels. Hence
\[
\mathbb E\left(W_n-\frac{T_n}{n}\right)^2
=\frac{\mathbb ET_n}{n^2}
=\frac{H_n}{n}.
\tag{5}
\]
Here \(\mathbb ET_n=nH_n\), by the usual decomposition into geometric waiting times for successive unseen types. Equation (5) implies
\[
L_n\left|G_n-X_n\right|\ \xrightarrow{\mathbb P}\ 0,
\]
since \(L_n^2H_n/n\to0\). Because \(G_n=O_{\mathbb P}(1)\), the mean-value theorem gives
\[
L_n\left|e^{-G_n}-e^{-X_n}\right|=o_{\mathbb P}(1).
\]
Replacing \(G_n\) by \(X_n\) in (4), including its random center, gives the first asserted joint limit. Division of the second coordinate by \(e^{-X_n/2}\), a positive continuous function of the first coordinate, gives the independent-Gaussian studentized limit. This completes the proof.

**4. Supporting finite covariance and correlation.** Equation (1) and the density of \(W_n\), integrated with \(y=e^{-t}\), yield
\[
\mathbb ES_n=H_n,\qquad
\mathop{\mathrm{Cov}}(W_n,S_n)=H_n^{(2)}-H_n.
\]
Independence of exponential waiting times and labels implies \(\mathop{\mathrm{Cov}}(T_n,S_n)=n\mathop{\mathrm{Cov}}(W_n,S_n)\). For \(n\ge3\), a second beta integral gives
\[
\mathbb E[(S_n-1)(S_n-2)]
=2\left[\left(H_n-\frac32\right)^2+H_n^{(2)}-\frac54\right].
\]
Thus \(\mathop{\mathrm{Var}}(S_n)\sim (\log n)^2\). The independent geometric waiting stages give \(\mathop{\mathrm{Var}}(T_n)=n^2H_n^{(2)}-nH_n\). These relations imply \(\mathop{\mathrm{Corr}}(T_n,S_n)\to-\sqrt6/\pi\), as asserted. No inference from finite computation to an infinite limit is used.

## Verification

The standalone `verify.py` independently solves the absorbing finite-state chain for counts of unseen types and types seen once, with exact rational arithmetic. For every \(2\le n\le14\), it calculates \(\mathbb ES_n\), \(\mathbb ES_n^2\), and \(\mathbb E[T_nS_n]\); it compares them with the stated harmonic identities, including the exact covariance, and checks the factorial second moment for \(3\le n\le14\). Additional numerical diagnostics for sizes \(100,1000,10000,100000\) check the variance and correlation scale. Reproduce with `python3 verify.py`; no third-party packages are required.

These finite calculations check moment consequences and error-prone algebra, not the infinite-dimensional weak convergence. The latter is established by conditional characteristic functions, uniform compact control, and the clock-depoissonization calculation in the proof.

## Relationship to prior work

Myers and Wilf (2003) supply the **full exact joint distribution** of the discrete collection time and singleton count (their formula (44), section 4); this dominates the marginal singleton law and permits finite mixed moments to be computed. We do not assert novelty for the exact covariance by itself or for the underlying finite joint distribution. Their section does not state the random-centered \(\sqrt{\log n}\)-scale Gaussian theorem above.

Ilienko's preprint, publicly posted 2020-02-03 and later published in 2026, establishes the first-order joint coupon-brotherhood limit of singleton vacancies at the completion time: \(S_n/\log n\Rightarrow E\), where \(E\) is exponential, and explains its coupling to the coupon-completion Gumbel extreme through a point-process limit (Theorem 2.1, proof in section 5). This **covers the first-order part** of the present analysis; neither that theorem nor its point-process formulation gives the residual Gaussian fluctuation after subtracting the observable random center.

Mahmoud and Smythe (2012) prove joint normal limits for coupon-frequency counts at **deterministic** collection lengths, in sublinear and linear phases; their article explicitly excludes the superlinear phase containing the \(n\log n\)-scale cover time from those Gaussian results. Betken and Thäle (2022 preprint, 2023 journal article; primary MSC2020 60C05) give normal and Poisson approximations for **uncollected** coupon counts at deterministic drawing times. Both are close statistically, but neither establishes the stopping-time-centered, mixed-normal second-order result.

The distinct contribution assessed here is solely the joint second-order random-centered theorem and its asymptotically independent, observable Gaussian pivot; known first-order limits and exact finite distribution are credited.

## Limitations

The limit provides no convergence rate, uniformity across heterogeneous coupon probabilities, or higher-order Edgeworth expansion. The conditional binomial representation and mean-centering estimates rely on uniform equal rates. Historical mathematical-priority risk remains because the complete finite joint law and general Poisson point-process constructions are powerful and could contain an equivalent second-order specialization not located in the inspected statements. The asymptotically Gaussian residual is a **conditional fluctuation scale**; the uncentered singleton count divided by \(\log n\) has an exponential, not Gaussian, limit. The studentizing expression is asymptotic and not an exact pivot at finite \(n\).

## References

1. A. Ilienko, *Limit theorems in the extended coupon collector's problem*, arXiv:2002.00650, first submitted 2020-02-03; published 2026, DOI 10.15559/26-VMSTA306. Theorem 2.1 and proof of its first-order exponential limit.
2. A. N. Myers and H. S. Wilf, *Some new aspects of the coupon-collector's problem*, arXiv:math/0304229, first submitted 2003-04-16; *SIAM Journal on Discrete Mathematics* 17 (2003), 1--17. Formula (44) for the joint distribution of completion time and singletons.
3. H. M. Mahmoud and R. T. Smythe, *On the joint behavior of types of coupons in generalized coupon collection*, *Advances in Applied Probability* 44 (2012), 429--451, DOI 10.1239/aap/1339878719.
4. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485, first submitted 2022-02-15; *Journal of Applied Probability* 60 (2023), 1352--1366, DOI 10.1017/jpr.2023.6.
