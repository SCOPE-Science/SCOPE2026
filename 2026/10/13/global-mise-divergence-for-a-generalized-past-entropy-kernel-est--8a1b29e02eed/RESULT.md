# Global MISE divergence for a generalized past-entropy kernel estimator
## Finding
Let \(X_1,\ldots,X_n\) be IID with density \(f(x)=e^{-x}\) on \(x\ge 0\). Set \(\beta=1/2\), use the standard Gaussian kernel
\[
K(u)=\frac{1}{\sqrt{2\pi}}e^{-u^2/2},
\]
and choose \(b_n=n^{-1/2}\). For the estimator
\[
f_n(x)=\frac{1}{n b_n}\sum_{j=1}^n K\!\left(\frac{x-X_j}{b_n}\right),
\qquad
F_n(t)=\int_0^t f_n(x)\,dx,
\]
\[
\overline H_n^{1/2}(f;t)
=2\log\!\left(\int_0^t \sqrt{f_n(x)}\,dx\right)-\log F_n(t),
\]
the global mean integrated squared error satisfies
\[
\mathbb E\!\left[\int_0^\infty
\left(\overline H_n^{1/2}(f;t)-\overline H^{1/2}(f;t)\right)^2\,dt\right]=\infty
\]
for every integer \(n\ge 1\). Consequently, Theorem 3.3 of Maya, Irshad, Buono, and Longobardi, which states convergence of this quantity to zero, is false as stated for an unbounded time domain.

## Assumptions and scope
The parent distribution is \(\operatorname{Exp}(1)\), so the observations are IID and therefore \(\alpha\)-mixing with mixing coefficients equal to zero at positive lags. The Gaussian kernel is nonnegative, symmetric, integrates to one, is Lipschitz, and is an order-two kernel in the standard moment sense. The bandwidth \(b_n=n^{-1/2}\) obeys \(b_n\to0\) and \(n b_n\to\infty\). The exponent \(\beta=1/2\) is inside the source's stated range \(\beta>0\), \(\beta\ne1\).

The claim concerns only the global Lebesgue-time MISE in Theorem 3.3. It does not contradict fixed-\(t\) consistency or uniform consistency on compact time intervals.

## Proof
For the exponential parent,
\[
F(t)=1-e^{-t},
\qquad
\int_0^t f(x)^{1/2}\,dx=2(1-e^{-t/2}).
\]
Hence
\[
\overline H^{1/2}(f;t)
=2\log\!\bigl(2(1-e^{-t/2})\bigr)-\log(1-e^{-t})
\longrightarrow \log 4
\]
as \(t\to\infty\).

Fix \(n\). For any realized sample, define
\[
A_n=\int_0^\infty f_n(x)\,dx,
\qquad
B_n=\int_0^\infty \sqrt{f_n(x)}\,dx.
\]
For the Gaussian kernel, \(0<A_n<1\) and \(0<B_n<\infty\). Monotone convergence of the two defining integrals gives
\[
\overline H_n^{1/2}(f;t)\longrightarrow L_n:=2\log B_n-\log A_n.
\]
It is therefore enough to show that \(L_n\ne\log4\) on an event of positive probability.

Consider first the deterministic configuration \(X_1=\cdots=X_n=c>0\). Then the kernel mixture collapses to a single shifted Gaussian with bandwidth \(b_n\). Writing \(\Phi\) for the standard normal distribution function,
\[
A_n(c)=\Phi\!\left(\frac{c}{b_n}\right),
\]
and direct Gaussian integration gives
\[
B_n(c)=\sqrt{b_n}\,2^{3/4}\pi^{1/4}
\Phi\!\left(\frac{c}{\sqrt2 b_n}\right).
\]
Thus
\[
L_n(c)=\log b_n+\log\sqrt{8\pi}
+2\log\Phi\!\left(\frac{c}{\sqrt2 b_n}\right)
-\log\Phi\!\left(\frac{c}{b_n}\right),
\]
so
\[
L_n(c)\longrightarrow \log\sqrt{\frac{8\pi}{n}}
\qquad(c\to\infty).
\]
This limiting value cannot equal \(\log4\) for an integer \(n\ge1\), because equality would require \(n=\pi/2\).

Choose a finite \(c_n\) large enough that \(L_n(c_n)\ne\log4\). The map from the sample vector \((x_1,\ldots,x_n)\) to \(A_n\) is continuous. The map to \(B_n\) is also continuous: pointwise continuity of the Gaussian mixture together with \(\sqrt{a_1+\cdots+a_n}\le\sqrt{a_1}+\cdots+\sqrt{a_n}\) supplies an integrable Gaussian envelope on a neighborhood of \((c_n,\ldots,c_n)\), so dominated convergence applies. Therefore \(L_n\) is continuous there. Some open neighborhood \(U_n\) of \((c_n,\ldots,c_n)\) consequently satisfies
\[
|L_n-\log4|>\delta_n
\]
for a constant \(\delta_n>0\).

The IID exponential law has a strictly positive density on \((0,\infty)\), so \(P((X_1,\ldots,X_n)\in U_n)>0\). On this event,
\[
\overline H_n^{1/2}(f;t)-\overline H^{1/2}(f;t)\longrightarrow L_n-\log4,
\]
whose absolute value is at least \(\delta_n\). The squared error is therefore bounded below by a positive constant for all sufficiently large \(t\), and
\[
\int_0^\infty
\left(\overline H_n^{1/2}(f;t)-\overline H^{1/2}(f;t)\right)^2\,dt=\infty
\]
on an event of positive probability. Its expectation is consequently infinite. This holds for every integer \(n\ge1\).

## Verification
The source defines the estimator in equation (2.4), allows nonnegative symmetric Lipschitz kernels with \(b_n\to0\) and \(n b_n\to\infty\), and defines the generalized past entropy for \(\beta>0\), \(\beta\ne1\). Theorem 3.3 integrates squared error over \((0,\infty)\) and claims that the resulting MISE tends to zero. The example above satisfies the stated estimator conditions and uses the Gaussian kernel also used by the source in its numerical work.

As an independent internal consistency check, the source's displayed equation (3.11) contains a nonnegative variance contribution proportional to
\[
\int_0^\infty \frac{\beta^2}{F(t)}\,dt.
\]
For any unbounded-support distribution with \(F(t)\to1\), this integral diverges. This observation is not used as the proof of the counterexample; the positive-probability tail argument above proves divergence directly from the estimator definition.

## Relationship to prior work
Maya, Irshad, Buono, and Longobardi introduce the estimator and state Theorem 3.3 in the 2025 online version of their article. Their Theorem 3.2 is explicitly restricted to compact subsets of the support interior, whereas Theorem 3.3 integrates over the entire positive half-line. The counterexample isolates that change of domain as the obstruction.

A 2014 paper by Maya, Abdul-Sathar, and Rajesh studies nonparametric kernel estimation of generalized past entropy with censored dependent data. Its accessible abstract establishes that it treats the same entropy object and kernel-estimation theme, but the full text was not available in the checked open sources. No accessible source located in the searches states the Gaussian-tail counterexample above or a correction of Theorem 3.3.

## Limitations
The finding does not determine the weakest conditions under which a corrected integrated-consistency result holds. Restricting \(t\) to a fixed compact interval, or replacing Lebesgue measure \(dt\) by a finite integrable weight, removes the specific infinite-tail mechanism but requires a separate proof. No claim is made here about the validity of the source's pointwise asymptotic-normality theorem or its compact-interval strong-consistency theorem.

## References
1. R. Maya, M. R. Irshad, F. Buono, and M. Longobardi, “Non-parametric estimation of the generalized past entropy function under α-mixing sample,” *Probability in the Engineering and Informational Sciences* 40(2), 272–287. First published online 2025-11-05. doi:10.1017/S0269964825100132.
2. R. Maya, E. I. Abdul-Sathar, and G. Rajesh, “Non-parametric estimation of the generalized past entropy function with censored dependent data,” *Statistics & Probability Letters* 90 (2014), 129–135. doi:10.1016/j.spl.2014.03.012.
