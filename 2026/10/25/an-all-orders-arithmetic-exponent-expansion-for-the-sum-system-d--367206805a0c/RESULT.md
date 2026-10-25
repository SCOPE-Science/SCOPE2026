# An all-orders arithmetic exponent expansion for the sum-system Dirichlet threshold

## Finding
For every integer \(m\ge2\), let \(r_m>1\) be the unique real solution of
\[
\zeta(r_m)=\frac{m}{m-1}.
\]
This is the convergence threshold of the Dirichlet series counting labeled \(m\)-part sum systems. Put \(M=m-1\), \(a=\log 2\), \(b=\log3\), and \(\lambda_n=\log_2(n/2)\) for integers \(n\ge3\). Define the additive semigroup
\[
\mathcal S=\left\{\lambda_{n_1}+\cdots+\lambda_{n_k}: k\ge1,\ n_i\ge3\right\}\subset(0,\infty).
\]
For every fixed real \(B>0\), there are unique recursively computable real constants \(c_\lambda\), for \(\lambda\in\mathcal S\cap(0,B)\), such that
\[
 r_m=\log_2 M+\sum_{\lambda\in\mathcal S,\,\lambda<B}c_\lambda M^{-\lambda}+O_B(M^{-B})\qquad(m\to\infty).
\]
Each displayed sum is finite. The constants are compatible as \(B\) increases: they form a unique all-orders generalized-power asymptotic expansion.

In particular, with \(\beta=\log_2(3/2)\), \(\gamma=\log_2(5/2)\), and \(\theta=\log_2(7/2)\), the first six terms, ordered by decreasing magnitude, are
\[
\begin{aligned}
 r_m=\log_2 M
 &+\frac{M^{-\beta}}{a}
 +\frac{M^{-1}}{a}
 +\left(\frac{1}{2a}-\frac b{a^2}\right)M^{-2\beta}
 +\frac{M^{-\gamma}}{a}\\
 &-\frac b{a^2}M^{-(1+\beta)}
 +\frac{a^2/3-3ab/2+3b^2/2}{a^3}M^{-3\beta}
 +O(M^{-\theta}).
\end{aligned}
\]
The exponent \(1+\beta\) is the first resonance: it comes both from the integer \(6\) in the zeta tail and from interaction of the terms for \(3\) and \(4\). The resulting coefficient is \(-b/a^2\), not the separate \(1/a\) contribution of \(6\).

## Assumptions and scope
All logarithms without a subscript are natural. The asymptotic variable is the integer \(m\to\infty\), and every cutoff \(B>0\) is fixed independently of \(m\). The expansion describes the unique real threshold defined above; it does not assert uniformity when \(B\) grows with \(m\). The underlying counting object is the \(m\)-part sum system described in Huxley--Lettington--Schmidt (2026): a labeled family of finite sets of nonnegative integers whose unique-representation Minkowski sum is an initial integer interval.

## Proof
**Step 1: identify the threshold and normalize its equation.** For fixed \(m\ge2\), the Stirling identity \((m-1)!S(L-1,m-1)=\sum_{j=0}^{m-1}(-1)^{m-1-j}\binom{m-1}{j}j^{L-1}\) gives \(m!S(L-1,m-1)\sim m(m-1)^{L-1}\) as \(L\to\infty\). At \(s=r_m\), each summand of the positive sum over \(L\) in the source Dirichlet-series formula tends to \(m/(m-1)\), hence it diverges; for real \(s>r_m\) it converges by the geometric majorant in the source. Thus \(r_m\) is the exact real absolute-convergence boundary. Since \(\zeta(s)\) decreases strictly from infinity to \(1\) on \((1,\infty)\), \(r_m\) exists uniquely. Put \(r_m=\log_2 M+\delta_M\). Multiplying \(\zeta(r_m)-1=1/M\) by \(M\) yields the exact equation
\[
 F_M(\delta_M):=e^{-a\delta_M}+\sum_{n\ge3}M^{-\lambda_n}e^{-(\log n)\delta_M}-1=0.
\]
For sufficiently large \(M\), \(F_M(0)>0\) and \(F_M(1)<0\), since the sum from \(n\ge3\) tends to zero. Thus \(0<\delta_M<1\). On \([0,1]\),
\[
 -F_M'(\delta)\ge a e^{-a\delta}\ge a/2.
\]
The leading tail is \(O(M^{-\lambda_3})\), so the mean-value theorem also gives \(\delta_M=O(M^{-\lambda_3})\).

**Step 2: local finiteness and recursive coefficient construction.** The smallest positive generator of \(\mathcal S\) is \(\lambda_3=\beta>0\). There are finitely many generators below any fixed \(B\), since \(\lambda_n<B\) implies \(n<2^{B+1}\); no sum of more than \(B/\beta\) generators is below \(B\). Consequently \(\mathcal S\cap(0,B)\) is finite.

Treat \(t=M^{-1}\) as a formal small parameter. Suppose all coefficients below \(\lambda\in\mathcal S\) have already been determined, and write
\[
 X_{<\lambda}(t)=\sum_{\mu\in\mathcal S,\,\mu<\lambda}c_\mu t^\mu.
\]
In a generalized formal series, let \([t^\lambda]\) extract the coefficient of exponent \(\lambda\). Set
\[
 c_\lambda=\frac1a[t^\lambda]\left(e^{-aX_{<\lambda}(t)}+
 \sum_{n\ge3}t^{\lambda_n}e^{-(\log n)X_{<\lambda}(t)}-1\right).
\]
Only finitely many integers and Taylor terms contribute to a fixed exponent. If \(X_{<\lambda}\) is augmented by \(c_\lambda t^\lambda\), the coefficient of exponent \(\lambda\) in the normalized equation changes by exactly \(-a c_\lambda\), because all other appearances of the new coefficient have higher exponent. The recursion therefore cancels every coefficient in increasing order and is unique.

**Step 3: turn the formal cancellation into a uniform error estimate.** Fix \(B>0\) and let \(X_B(t)=\sum_{\lambda<B}c_\lambda t^\lambda\). Since \(X_B(M^{-1})=O(M^{-\beta})\), it lies in \([0,1]\) for all sufficiently large \(M\): it is identically zero if \(B\le\beta\), while otherwise its first nonzero coefficient is \(1/a>0\). Choose a fixed integer \(N\ge3\) such that \(\lambda_N\ge B\). For \(r_0=\log_2 M>2\), the tail obeys
\[
 \sum_{n\ge N}M^{-\lambda_n}e^{-(\log n)X_B(M^{-1})}
 \le M\left(N^{-r_0}+\frac{N^{1-r_0}}{r_0-1}\right)=O_B(M^{-B}).
\]
Expand the finitely many remaining exponentials through a Taylor order \(K\) for which \((K+1)\beta\ge B\). All powers below \(B\) belong to \(\mathcal S\) and vanish by the recursion, so \(F_M(X_B(M^{-1}))=O_B(M^{-B})\). Applying the derivative bound from Step 1 between the exact root and this approximation gives
\[
 \delta_M-X_B(M^{-1})=O_B(M^{-B}).
\]
This proves the all-orders assertion and its compatibility for different cutoffs.

**Step 4: evaluate the first coefficients and the resonance.** In order below \(\theta=\lambda_7\), the exponents in \(\mathcal S\) are exactly
\[
 \beta,\quad 1,\quad 2\beta,\quad \gamma,\quad 1+\beta=\lambda_6,\quad 3\beta.
\]
Writing \(u=M^{-\beta}\), \(v=M^{-1}\), \(w=M^{-\gamma}\), substitute
\[
 \delta=\frac ua+\frac va+A u^2+\frac wa+Cuv+D u^3
\]
into the equation from Step 1. The coefficients at \(u^2\), \(uv\), and \(u^3\) give, respectively,
\[
 A=\frac1{2a}-\frac b{a^2},\qquad C=-\frac b{a^2},\qquad D=\frac{a^2/3-3ab/2+3b^2/2}{a^3}.
\]
For \(uv\), the \(n=6\) summand contributes \(+uv\), while the main exponential, the \(n=3\) term, and the \(n=4\) term contribute \(+uv\), \(-(b/a)uv\), and \(-2uv\), respectively. Their cancellation yields \(C=-b/a^2\). The general theorem at cutoff \(B=\theta\) supplies the stated remainder.

## Verification
The included `verify.py` independently solves the defining zeta equation at high precision for five increasing values of \(M\), compares the exact normalized root with the explicit six-term expansion, and scales the residual by \(M^\theta\). The computations supplement, rather than replace, the infinite proof above. The coefficient recursion and tail bound, not the finite numerical examples, establish the asymptotic statement.

## Relationship to prior work
Huxley, Lettington and Schmidt (2026), Theorem 5.3, give the exact implicit zeta equation defining \(r_m\), identify its role in the Dirichlet convergence condition for sum-system counts, and provide bounds showing \(r_m\) has logarithmic order. Their Remark 5.4 explicitly discusses improving the estimate. The result here does **not** claim discovery of the implicit equation or the definition of sum systems: it resolves the large-\(m\) precision problem through an all-orders exponent semigroup and computes the first resonance coefficient. Lettington and Schmidt (2019/2020) establish underlying counting formulas but do not state this large-parameter expansion. Priority remains conditional on wider searches of unindexed literature.

## Limitations
No error constant uniform in the cutoff \(B\) is proved. The recursively defined coefficients need not all be nonzero. No separate asymptotic for the number of sum systems as a function of its size is established here: the claim concerns the convergence threshold as the number of parts grows. The method uses the already-known implicit equation and does not claim an independent derivation of the sum-system Dirichlet series. The novelty assessment is based on accessible literature and is not independent priority certification.

## References
1. M. N. Huxley, M. C. Lettington and K. M. Schmidt, *On Divisor Function Polynomials and Dirichlet Series*, arXiv:2610.13864v1, first posted 9 October 2026, Theorem 5.3 and Remark 5.4, https://arxiv.org/html/2610.13864v1.
2. M. C. Lettington and K. M. Schmidt, *Divisor Functions and the Number of Sum Systems*, arXiv:1910.02455 (2019); *Integers* 20 (2020), A61, https://arxiv.org/abs/1910.02455.
