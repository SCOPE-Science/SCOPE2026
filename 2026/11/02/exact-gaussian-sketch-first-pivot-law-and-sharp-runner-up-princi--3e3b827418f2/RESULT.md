# Exact Gaussian-sketch first-pivot law and sharp runner-up principle

## Finding

For mutually orthogonal nonzero columns, the probability that a Gaussian-sketched column-pivoted QR factorization selects the wrong first column admits an exact integral for every sketch height, a finite rational expression for every even sketch height when the squared column norms are rational, and a sharp large-height equivalent depending only on the longest and second-longest squared norms and the multiplicity of the latter. In particular, the shared winning-column fluctuation does **not** destroy the leading-order additivity of the rare mis-pivot events associated with tied runners-up.

Let \(n\ge2\), \(d\ge n\), and let \(A=[a_1,\ldots,a_n]\in\mathbb R^{d\times n}\) have mutually orthogonal nonzero columns. Write \(\alpha_j=\|a_j\|_2^2\), and suppose
\[
\alpha_1>\beta:=\max_{2\le j\le n}\alpha_j>0.
\]
For an integer \(k\ge1\), take \(G\in\mathbb R^{k\times d}\) with independent standard real Gaussian entries and let \(P_k\) be the probability that the first maximum-column-norm pivot of \(GA\) does not choose column \(1\). Ties have probability zero. Put \(s=k/2\), \(r_j=\alpha_1/\alpha_j>1\), and let \(F_s(t)=\gamma(s,t)/\Gamma(s)\) be the regularized lower incomplete gamma function. Then exactly
\[
P_k=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}e^{-t}
\left(1-\prod_{j=2}^n F_s(r_jt)\right)\,dt.\tag{1}
\]
If \(k=2m\) with integer \(m\ge1\), put \(L_J=\sum_{j\in J}\ell_j\). The same number has the finite expression
\[
P_{2m}=\sum_{\varnothing\ne J\subseteq\{2,\ldots,n\}}(-1)^{|J|+1}
\sum_{(\ell_j)_{j\in J}\in\{0,\ldots,m-1\}^J}
\frac{(m+L_J-1)!}{(m-1)!}
\frac{\prod_{j\in J}r_j^{\ell_j}/\ell_j!}
{(1+\sum_{j\in J}r_j)^{m+L_J}}.\tag{2}
\]
This is a finite exact rational number whenever the squared column norms are rational.

Let \(r\) be the number of indices \(j\in\{2,\ldots,n\}\) for which \(\alpha_j=\beta\), and put \(R=\alpha_1/\beta>1\). As \(k\to\infty\) through all positive integers,
\[
\boxed{P_k\sim
\frac{r(R+1)}{(R-1)\sqrt{2\pi k}}
\left(\frac{4R}{(R+1)^2}\right)^{k/2}.}\tag{3}
\]
Thus the sharp exponential rate is \(J(R)=\log((R+1)/(2\sqrt R))\), and the exact leading multiplier remembers only the number \(r\) of tied second-largest columns. All strictly smaller columns and all simultaneous runner-up exceedances are lower order.

For every finite \(k\), the following useful comparison also holds, with \(I_x(a,b)\) the regularized incomplete beta function:
\[
I_{\beta/(\alpha_1+\beta)}(k/2,k/2)
\le P_k\le\sum_{j=2}^n
 I_{\alpha_j/(\alpha_1+\alpha_j)}(k/2,k/2)
\le(n-1)I_{\beta/(\alpha_1+\beta)}(k/2,k/2).\tag{4}
\]
For a prescribed small mis-pivot probability \(\varepsilon\), the minimum number of Gaussian sketch rows \(K(\varepsilon)=\min\{k\ge1:P_k\le\varepsilon\}\) therefore satisfies
\[
K(\varepsilon)=\frac{\log(1/\varepsilon)}{J(R)}-
\frac{\log\log(1/\varepsilon)}{2J(R)}+O(1),
\qquad\varepsilon\downarrow0.\tag{5}
\]

## Assumptions and scope

The input matrix, its columns and its norms are deterministic; columns are pairwise orthogonal and strictly positive in norm; the longest column is unique; \(n\) is fixed in the large-\(k\) limit. The sketch is one **shared** real Gaussian matrix applied to every column, with independent entries; normalization of its entries by \(1/\sqrt{k}\) does not change the pivot. The only algorithmic decision analyzed is the *first*, maximum-sketched-column-norm QR pivot, with exact arithmetic. Formula (2) is asserted for even sketch height, while (1), (3) and (4) cover every positive integer sketch height.

## Proof

**Independent gamma reduction.** For each row of \(G\), the Gaussian vector \((Ga_1,\ldots,Ga_n)\) has diagonal covariance \(\operatorname{diag}(\alpha_1,\ldots,\alpha_n)\) because the original columns are orthogonal. Joint normality implies independence of all the resulting column sketches. Consequently \(\|Ga_j\|_2^2/\alpha_j\) are independent chi-squared variables \(X_j\sim\chi_k^2\). Put \(T=X_1/2\sim\operatorname{Gamma}(s,1)\). Given \(T=t\), correct pivoting requires \(X_j\le r_jX_1\) for every \(j\ge2\), an event of conditional probability \(\prod_{j=2}^nF_s(r_jt)\). Integrating the complement gives (1), including the dependence induced in the comparison events by their common winning column.

**Finite-sum identity.** At \(s=m\in\mathbb N\), \(F_m(z)=1-e^{-z}\sum_{\ell=0}^{m-1}z^\ell/\ell!\). Expand the product in (1) by inclusion–exclusion; for every nonempty subset \(J\), expand its finite product of truncated exponential series. Each resulting monomial integrates via
\[
\frac1{\Gamma(m)}\int_0^\infty t^{m+L_J-1}
 e^{-(1+\sum_{j\in J}r_j)t}\,dt
=\frac{(m+L_J-1)!}{(m-1)!(1+\sum_{j\in J}r_j)^{m+L_J}}.
\]
This gives exactly (2). At \(k=2\) the formula simplifies to \(P_2=\sum_{\varnothing\ne J}(-1)^{|J|+1}/(1+\sum_{j\in J}r_j)\).

**One competitor and sharp beta tail.** For any \(j\ge2\), the event \(E_j=\{\alpha_jX_j>\alpha_1X_1\}\) has probability
\[
\Pr(E_j)=I_{t_j}(k/2,k/2),\qquad
 t_j=\frac{\alpha_j}{\alpha_1+\alpha_j}<\frac12,
\]
because \(X_1/(X_1+X_j)\) has the symmetric beta law. This proves (4) by inclusion and the union bound. For fixed \(t\in(0,1/2)\), direct endpoint Laplace asymptotics applied to the beta integral, together with the Stirling expansion of \(B(k/2,k/2)\), give
\[
I_t(k/2,k/2)\sim
\frac{[4t(1-t)]^{k/2}}{(1-2t)\sqrt{2\pi k}}.\tag{6}
\]
Indeed, the beta integrand is \([u(1-u)]^{k/2}/[u(1-u)]\) and its exponential phase increases strictly on \([0,t]\); the endpoint contribution is \([t(1-t)]^{k/2}/[(k/2)(1-2t)]\), while \(B(k/2,k/2)\sim 2\sqrt{2\pi/k}\,4^{-k/2}\). Equation (6) follows.

**Simultaneous runner-up events are exponentially negligible.** Let \(j\ne\ell\) be two runner-up columns, both of squared norm \(\beta\). If both \(E_j\) and \(E_\ell\) occur, then \(\beta(X_j+X_\ell)>2\alpha_1X_1\). For \(0<w<1\), the chi-squared moment-generating function and Markov's inequality yield
\[
\Pr(E_j\cap E_\ell)
\le(1-w)^{-k}(1+2Rw)^{-k/2}.
\]
The choice \(w=(R-1)/(3R)\) minimizes the right side and gives
\[
\Pr(E_j\cap E_\ell)\le
\left(\frac{27R^2}{(2R+1)^3}\right)^{k/2}
=e^{-kJ_2(R)},\quad
J_2(R)=\frac12\log\frac{(2R+1)^3}{27R^2}.
\]
The rate is strictly larger than the one-competitor rate \(J(R)\), because
\[
4(2R+1)^3-27R(R+1)^2=(R-1)^2(5R+4)>0.
\]
If \(\alpha_j<\beta\), then its beta-tail exponent \(J(\alpha_1/\alpha_j)\) is strictly greater than \(J(R)\), because \(J'(R)=(R-1)/(2R(R+1))>0\). Therefore all lower-column events and all intersections of runner-up events are negligible relative to a single runner-up tail. The first two terms of inclusion–exclusion for the union of the \(r\) runner-up events, followed by (6), prove (3).

**Row count.** Equation (3) gives \(\log P_k=-kJ(R)-\frac12\log k+O(1)\). It also implies \(P_{k+1}/P_k\to e^{-J(R)}<1\); hence \(P_k\) is eventually strictly decreasing and the minimizing integer in (5) is well defined for sufficiently small \(\varepsilon\). Solving the logarithmic threshold equation, with a bounded integer-rounding error, proves (5).

## Verification

The accompanying `verify.py` performs exact-rational finite-sum evaluations for five sets of squared column norms and sketch heights \(2,4,6,8\), independently integrates formula (1), checks the beta comparison bounds, verifies the strict-exponent polynomial identity symbolically, and simulates the *actual* Gaussian-sketch first-pivot decision with fixed random seeds. The resulting 80 checks passed. For example, at squared norms \((9,4,1)\) and two sketch rows, the exact failure probability is \(2077/6370\). These finite tests illustrate the result; they are not substitutes for the analytic proof of the all-parameter and asymptotic statements.

## Relationship to prior work

Melnichenko, Balabanov, Murray, Demmel, Mahoney and Luszczek (arXiv:2311.08316, first posted 2023-11-14) use a single sketch to find pivots in CQRRPT and analyze rank revelation, embedding and numerical stability. Their Sections 1.4, 2.2–2.3 and 4 motivate identifying concrete pivot-decision probabilities, but do not give the fixed-orthogonal-column formula (2) or runner-up equivalent (3).

Duersch and Gu (arXiv:1509.06820, 2015) analyze Gaussian sampled column norms and conditional truncated chi-squared laws after pivoting; their Section 3 does not calculate this exact multi-competitor first-pivot probability or the joint-exceedance asymptotic. Xiao, Gu and Langou (arXiv:1804.05138, 2018), Section III-C, provide a Johnson–Lindenstrauss-based high-probability QR pivot reliability result rather than the exact failure law on the stated canonical input family. The independent gamma and symmetric beta distributions used here are standard classical facts; the assessed specific contribution is their multi-candidate first-pivot synthesis, exact finite expression, and rigorous sharp runner-up multiplicity rule.

## Limitations

Only the first pivot is covered, not subsequent dependent QR pivots, pivoted factorization error, numerical precision effects, structured/sparse sketching distributions, nonorthogonal column systems or growing numbers of columns. The sharp equivalent assumes fixed positive squared column norms with one strict maximum and a fixed number of candidates. The exact integral remains true under all stated conditions, but it should not be applied without modification to ties at the maximum. The independence assumption comes specifically from orthogonality and jointly Gaussian sketch coordinates. Publication-priority uncertainty remains for specialized gamma-order-statistic literature; independent external validation has not been carried out.

## References

1. M. Melnichenko, O. Balabanov, R. Murray, J. Demmel, M. W. Mahoney and P. Luszczek, *CholeskyQR with Randomization and Pivoting for Tall Matrices (CQRRPT)*, arXiv:2311.08316v1 (2023-11-14), https://arxiv.org/abs/2311.08316.
2. J. A. Duersch and M. Gu, *Randomized QR with Column Pivoting*, arXiv:1509.06820v1 (2015-09-23), https://arxiv.org/abs/1509.06820.
3. J. Xiao, M. Gu and J. Langou, *Fast Parallel Randomized QR with Column Pivoting Algorithms for Reliable Low-rank Matrix Approximations*, arXiv:1804.05138v1 (2018-04-13), https://arxiv.org/abs/1804.05138.
