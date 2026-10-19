# Exact Green–Kubo variance and a singular critical limit for the Pelikan random map

## Finding
Let \(X_{n+1}=T_{\omega_n}(X_n)\) on \([0,1)\), with independent map choices \(T_D(x)=2x\bmod 1\) of probability \(p\) and \(T_C(x)=x/2\) of probability \(q=1-p\). For \(1/2<p\leq1\), initialize \(X_0\) in the absolutely continuous invariant probability. Define \(\mu_p=\mathbb E[X_0]\), \(S_N=\sum_{j=0}^{N-1}(X_j-\mu_p)\), and the annealed Green–Kubo intensity \(\Gamma(p)=\lim_{N\to\infty}N^{-1}\operatorname{Var}(S_N)\), where variance includes both initial state and independent map choices.

**Theorem.** For every \(1/2<p\leq1\), the limit exists, and
\[
\boxed{\Gamma(p)=\frac{-12p^4+50p^3-43p^2+14p-1}{(3p-1)^3(5p-1)}.}
\]
It decreases strictly with \(p\), from \(\lim_{p\downarrow1/2}\Gamma(p)=4\) to \(\Gamma(1)=1/4\). At \(p=1/2\), the invariant atomic state \(\delta_0\) instead has \(\Gamma=0\). Moreover the absolutely continuous invariant measures converge weakly to \(\delta_0\) as \(p\downarrow1/2\); thus the critical behavior is a genuine noncommutation of the stationary-parameter and long-observation-time limits.

The single-time stationary variance is
\[
\operatorname{Var}(X_0)=\frac{(2p-1)(6p^2-3p+1)}{3(3p-1)^2(5p-1)},
\]
so the integrated normalized correlation time \(\Gamma(p)/\operatorname{Var}(X_0)\) diverges as \(9/[2(2p-1)]\) on approach to criticality, although the instantaneous variance vanishes.

## Assumptions and scope
All statements about \(\Gamma(p)\) for \(p>1/2\) concern the unique absolutely continuous stationary law described by Yan et al. The random choices are independent of one another and of \(X_0\). Endpoints of dyadic intervals have probability zero. Invariant atomic dynamics at the critical parameter is used only to compare its variance; it is not substituted for the nonnormalizable critical invariant density. The deterministic endpoint \(p=1\) is included.

For each integer \(k\geq0\), put \(I_k=(2^{-k-1},2^{-k})\), \(r=2q/p\), and \(a_k=\frac{2p-1}{p}\sum_{j=0}^k r^j\). The stationary density is \(h_p(x)=a_k\) on \(I_k\). Its coefficient generating function is
\[
A(s)=\sum_{k\geq0}a_ks^k=\frac{2p-1}{p(1-s)(1-rs)}.
\]
Consequently \(\int h_p=\frac12A(1/2)=1\), \(\mu_p=\frac38 A(1/4)=(2p-1)/(3p-1)\), and \(\mathbb E[X_0^2]=\frac7{24}A(1/8)=4(2p-1)/[3(5p-1)]\). Direct substitution in the annealed Perron–Frobenius operator verifies invariance.

## Proof
**Exact affine-shell transfer.** The Perron–Frobenius operator on densities is
\[
(\mathcal L f)(x)=\frac p2[f(x/2)+f((x+1)/2)]+2q\,\mathbf1_{x<1/2}f(2x).
\]
Let \(g_n=\mathcal L^n(xh_p)\). Its restriction to \(I_k\) is affine: \(g_n(x)=u_{k,n}+v_{k,n}x\). Initially \(u_{k,0}=0\), \(v_{k,0}=a_k\). Writing a prime for the next time step, direct inverse-branch substitution gives, for \(k\geq1\),
\[
\begin{aligned}
u'_k&=\frac p2(u_{k+1}+u_0+v_0/2)+2q u_{k-1},\\
v'_k&=\frac p4(v_{k+1}+v_0)+4qv_{k-1},
\end{aligned}
\]
whereas \(u'_0=\frac p2(u_1+u_0+v_0/2)\) and \(v'_0=\frac p4(v_1+v_0)\). Each equation is at the same time level before the prime.

Introduce \(\mathcal U(s,z)=\sum_{n,k\geq0}u_{k,n}s^kz^n\), \(\mathcal V(s,z)=\sum_{n,k\geq0}v_{k,n}s^kz^n\), \(u(z)=\mathcal U(0,z)\), and \(v(z)=\mathcal V(0,z)\). Summing the shell recurrences yields
\[
\begin{aligned}
\mathcal V(s,z)&=\frac{A(s)+\frac{zp}{4}\frac{2s-1}{s(1-s)}v(z)}{1-z(\frac{p}{4s}+4qs)},\\
\mathcal U(s,z)&=\frac{\frac{zp}{2}\frac{2s-1}{s(1-s)}u(z)+\frac{zp}{4(1-s)}v(z)}{1-z(\frac{p}{2s}+2qs)}.
\end{aligned}
\]
These identities are initially formal power series in \(z\) with coefficients analytic near \(s=0\). Both apparent kernel poles must cancel. Define the small kernel root
\[
t(z)=\frac{1-\sqrt{1-4pqz^2}}{8qz}=\frac{pz}{2(1+\sqrt{1-4pqz^2})},
\]
with \(t(z)=z/4\) when \(p=1\). The two kernel roots are \(t(z)\) and \(2t(z)\). Cancellation gives
\[
v(z)=-\frac{4t(1-t)A(t)}{zp(2t-1)},\qquad
u(z)=-\frac{t\,v(z)}{4t-1}.
\]
Thus the two generating functions are explicit algebraic functions.

**Stationary two-time resolvent.** Write \(M(z)=\sum_{n\geq0}\mathbb E[X_0X_n]z^n\). Since \(\int_{I_k}x\,dx=3\cdot4^{-k}/8\) and \(\int_{I_k}x^2\,dx=7\cdot8^{-k}/24\),
\[
M(z)=\frac38\mathcal U(1/4,z)+\frac7{24}\mathcal V(1/8,z).
\]
Substitution followed by cancellation, with \(t=t(z)\) and \(z=4t/[p+16qt^2]\), yields the exact identity
\[
M(z)=\frac{(2p-1)(16pt^2-p-16t^2)(16pt^2+13pt-8p-16t^2+7t)}{6(5p-1)(2t-1)(4t-1)(2pt+p-2t)^2}.
\]
These resolvent identities are needed here to evaluate an infinite covariance sum; no claim of priority for finite-lag autocorrelation representations is made.

Let \(C(z)=M(z)-\mu_p^2/(1-z)=\sum_{n\geq0}\operatorname{Cov}(X_0,X_n)z^n\). The factor \(4t-1\) cancels algebraically from \(C(z)\). After cancellation its only possible \(t\)-dependent denominator factors, up to nonzero parameter constants, are \(2t-1\), \(p-2qt\), and \(p-4qt\). The algebraic branch \(t(z)\) has nonnegative Taylor coefficients, and for \(p>1/2\) satisfies \(|t(z)|\leq t(1)=1/4\) when \(|z|\leq1\). All three factors are nonzero in that disk, since \(p-4q/4=2p-1>0\). The branch points at \(|z|=1/(2\sqrt{pq})\) also lie strictly outside the unit disk; for \(p=1\), \(t=z/4\) is entire. Compactness therefore gives analyticity on \(|z|<1+\epsilon_p\) for some \(\epsilon_p>0\). In particular the stationary covariances decay exponentially and are absolutely summable.

Now \(t(1)=1/4\). The removable-value evaluation in the preceding rational expression gives
\[
\sum_{n\geq0}\operatorname{Cov}(X_0,X_n)=C(1)=\frac{51p^3-51p^2+17p-1}{3(3p-1)^3(5p-1)}.
\]
From stationarity, \(\operatorname{Var}(S_N)=N C_0+2\sum_{k=1}^{N-1}(N-k)C_k\), where \(C_k=\operatorname{Cov}(X_0,X_k)\). Absolute summability implies \(\Gamma=2C(1)-C_0\). Inserting the explicit instantaneous variance proves the stated rational formula.

**Strict monotonicity and singularity.** Differentiation and factorization give
\[
\Gamma'(p)=-\frac{2p(267p^3-371p^2+197p-29)}{(3p-1)^4(5p-1)^2}.
\]
The cubic factor is positive for \(p\geq1/2\): at \(p=1/2\) it is \(81/8\), while its derivative \(801p^2-742p+197\) is positive for every real \(p\) because its discriminant is \(-80624\). The endpoint evaluations give \(4\) and \(1/4\). Also \(\operatorname{Var}(X_0)\sim (8/9)(2p-1)\), hence \(\Gamma/\operatorname{Var}(X_0)\sim9/[2(2p-1)]\). Finally, \(0\leq X_0\leq1\) and \(\mu_p\to0\) imply \(\nu_p\Rightarrow\delta_0\) by Markov's inequality. For each fixed \(N\), Cauchy–Schwarz and stationarity give \(N^{-1}\operatorname{Var}(S_N)\leq N\operatorname{Var}(X_0)\to0\) as \(p\downarrow1/2\). Thus \(\lim_{N\to\infty}\lim_{p\downarrow1/2}N^{-1}\operatorname{Var}(S_N)=0\) while \(\lim_{p\downarrow1/2}\lim_{N\to\infty}N^{-1}\operatorname{Var}(S_N)=4\). The point mass at zero has identically zero Birkhoff-sum variance for all \(p\).

## Verification
Run `python verify.py` using Python 3 and SymPy. The standalone checker independently reconstructs the two-variable transfer resolvent, factors the stationary covariance subtraction, evaluates the Green–Kubo sum and its derivative, verifies both parameter limits, and compares 24 exact rational raw two-time moments obtained by direct enumeration of random map words against an independently implemented shell recurrence. The 24 checks use \(p\in\{3/5,2/3,3/4,9/10\}\) and \(0\leq n\leq5\). Its symbolic identities hold with indeterminate \(p\); finite tests alone are not claimed to establish the infinite-time theorem. The analytical cancellation and singularity bounds above establish it.

## Relationship to prior work
Yan, Majumdar, Ruffo, Sato, Beck, and Klages identify the invariant-density phase transition and stationary coordinate autocorrelations; their Section III computes the first few lags exactly, uses simulations for longer times, and explicitly motivates Green–Kubo transport coefficients. Earlier exact finite-lag stationary autocorrelation representations also determine all coefficients in principle; **the claim here is not their recovery**, but the closed evaluation of the *infinite* covariance sum, strict parameter monotonicity, and noncommuting critical variance limit.

Monthus subsequently derives a full time-Laplace transform for an explicitly **uniform-initial**, nonstationary coordinate correlation. That initial law is different from the invariant law used here; its large-time limiting product is \(\frac12\mu_p\), rather than \(\mu_p^2\). Neither quantity is substituted for the stationary Green–Kubo sum. Generic Green–Kubo existence formulas likewise do not provide this rational parameter evaluation.

## Limitations
The result is annealed and observable-specific. It neither proves a central limit theorem nor describes quenched variances, higher cumulants, or a uniform joint \(p\downarrow1/2\), \(N\to\infty\) crossover. The critical comparison uses the absorbing invariant atom \(\delta_0\), not a normalizable absolutely continuous stationary distribution at criticality. Although the exact infinite covariance sum can be evaluated from known finite-lag formulas in principle, this work asserts an explicit summation and its sharp critical behavior, not independence from those earlier representations. Historical priority of an equivalent unpublished variance evaluation has not been excluded.

## References
1. J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, and R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269 (first posted 2023-08-18), particularly Sections II–III and Eqs. (16)–(20). https://arxiv.org/abs/2308.09269
2. C. Monthus, *Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region*, arXiv:2409.19999 (first posted 2024-09-30), particularly Section VII and Eqs. (199)–(211). https://arxiv.org/abs/2409.19999
