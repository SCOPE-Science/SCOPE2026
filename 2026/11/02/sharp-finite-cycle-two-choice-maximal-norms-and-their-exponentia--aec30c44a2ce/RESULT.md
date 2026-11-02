# Sharp finite-cycle two-choice maximal norms and their exponential finite-size deficit

## Finding

For every integer \(N\ge2\) and every \(0<\theta<1\), the two-choice cyclic maximal operator
\[
(\mathcal M_{N,\theta}f)(j)=\max\left\{|f(j)|,\left|(1-\theta)f(j)+\theta f(j-1)\right|\right\},\qquad j\in\mathbb Z/N\mathbb Z,
\]
acting on complex \(\ell^2(\mathbb Z/N\mathbb Z)\), has squared optimal norm equal to the *unique real zero greater than one* of an explicit degree-\(N\) polynomial described below. All nonzero maximizing vectors are complex scalars times cyclic translates of one strictly positive vector. The extremizing choice pattern uses the unaveraged value at precisely one site, and the two-point average at all other sites.

Writing \(b=\theta\), \(a=1-b\), \(t=ab\), \(c=a^2+b^2\), form the real symmetric matrix
\[
J_N=\begin{pmatrix}
1+b^2&t&0&\cdots&0\\
t&c&t&\ddots&\vdots\\
0&t&\ddots&\ddots&0\\
\vdots&\ddots&\ddots&c&t\\
0&\cdots&0&t&a^2
\end{pmatrix},
\]
where, for \(N=2\), only its first and last diagonal entries and their connecting off-diagonal entry are present. Then
\[
\boxed{\|\mathcal M_{N,\theta}\|_{\ell^2\to\ell^2}^2=\lambda_N:=\lambda_{\max}(J_N).}
\]
An entirely algebraic specification uses \(D_0(X)=1\), \(D_1(X)=X-1-b^2\),
\[
D_k(X)=(X-c)D_{k-1}(X)-t^2D_{k-2}(X)\quad(2\le k<N),
\]
\[
D_N(X)=(X-a^2)D_{N-1}(X)-t^2D_{N-2}(X).
\]
The equation \(D_N(X)=0\) has precisely one real zero \(X>1\), namely \(\lambda_N\).

At each fixed \(0<\theta<1\), the constants increase strictly with \(N\) and satisfy the sharp exponential asymptotic
\[
\boxed{\lim_{N\to\infty}\frac{\dfrac2{2-\theta}-\lambda_N}{\left(\dfrac{1-\theta}{2-\theta}\right)^{2N}}=\frac{\theta(3-2\theta)^2}{2(2-\theta)^2(1-\theta)^2}.}
\]
In particular, for equal two-point averaging (\(\theta=1/2\)),
\[
\lim_{N\to\infty}3^{2N}\left(\frac43-\|\mathcal M_{N,1/2}\|^2\right)=\frac{16}{9}.
\]

## Assumptions and scope

Coordinates are indexed modulo \(N\), all norms use counting measure (normalization of both input and output by \(1/N\) gives the same operator norm), and \(0<\theta<1\). The nonlinearity places the absolute value *after* the two-point complex average, rather than inside it. For nonnegative real inputs these conventions coincide; the norm is identical for the variant with averages of moduli, while the complex equality classification is specifically for the displayed phase-sensitive operator. All eigenvalue and polynomial statements quantify over every real parameter in the stated interval and every integer \(N\ge2\).

## Proof

**1. Linearization and active-pattern components.** For every binary pattern \(\varepsilon=(\varepsilon_j)_{j\in\mathbb Z/N\mathbb Z}\), define the linear operator \(L_\varepsilon\) whose row \(j\) is the identity row if \(\varepsilon_j=0\) and the row of \(aI+bS\), \((Sf)(j)=f(j-1)\), if \(\varepsilon_j=1\). Pointwise maximization of nonnegative squared moduli gives the exact identity
\[
\|\mathcal M_{N,b}f\|_2^2=\max_{\varepsilon\in\{0,1\}^N}\|L_\varepsilon f\|_2^2.
\]
Finite interchange of maxima yields \(\|\mathcal M_{N,b}\|^2=\max_\varepsilon\lambda_{\max}(L_\varepsilon^*L_\varepsilon)\). The all-zero pattern gives one; the all-one pattern also gives one, since \(\|aI+bS\|=a+b=1\).

Suppose the pattern has at least one zero. Each zero cuts the cycle edge in the positive tridiagonal matrix \(L_\varepsilon^*L_\varepsilon\). Between successive zeros, a run containing \(L\) vertices contributes one block \(J_L\): when \(L=1\), this block is \([1]\); for \(L\ge2\), its first diagonal is \(1+b^2\), its last is \(a^2\), every internal diagonal is \(c\), and each nearest-neighbor off-diagonal is \(t>0\). The block lengths add to \(N\). Consequently every such pattern has top eigenvalue \(\max_i\lambda_{\max}(J_{L_i})\).

For \(L\ge2\), the leading \(L\)-by-\(L\) principal matrix of \(J_{L+1}\) agrees with \(J_L\) except that its last diagonal is larger by \(b^2>0\). By the strictly positive top eigenvector of \(J_L\), the Rayleigh quotient increases strictly on extension by zero. Also \(\lambda_{\max}(J_2)>1=\lambda_{\max}(J_1)\). Hence \(\lambda_{\max}(J_L)\) strictly increases with \(L\). Among all patterns, exactly those with one zero achieve the largest norm, \(\lambda_N\).

**2. Equality and algebraic formula.** The matrix \(J_N\) is entrywise nonnegative and irreducible. Its Perron eigenvalue is simple and its eigenvector \(v=(v_0,\ldots,v_{N-1})\) is strictly positive, uniquely determined up to positive scaling. All maximizing vectors for \(\mathcal M_{N,b}\) are precisely \(\gamma\) times cyclic translates of \(v\), where \(\gamma\in\mathbb C\setminus\{0\}\) and the coordinates of \(v\) follow the path from the unique unaveraged site. Indeed, equality requires an optimal binary pattern and a top eigenvector of its positive Gram matrix; conversely every listed vector attains the finite maximum. The determinant recurrence for \(J_N\) is exactly \(D_N\).

To show that precisely one eigenvalue exceeds one, compare \(J_N\) with the constant-coefficient tridiagonal path matrix \(Q_N\) having diagonal \(c\) and off-diagonal \(t\). Its spectral maximum is \(c+2t\cos(\pi/(N+1))<c+2t=1\). Since \(J_N=Q_N+(1-a^2)e_0e_0^* -b^2e_{N-1}e_{N-1}^*\), a rank-one positive perturbation followed by a negative one can create at most one eigenvalue above one. The first Rayleigh diagonal equals \(1+b^2>1\), so exactly one exists.

**3. Strict upper bound and convergence.** Set
\[
r=\frac{a}{2-b},\qquad \lambda_\infty=\frac2{2-b},\qquad h_j=r^j\quad(0\le j<N).
\]
The identities \(\lambda_\infty=1+b^2+tr=c+t(r+r^{-1})\) give the exact ground-state representation, for any complex vector \(u\),
\[
\lambda_\infty\|u\|_2^2-\langle J_Nu,u\rangle
=t\sum_{j=0}^{N-2}h_jh_{j+1}\left|\frac{u_j}{h_j}-\frac{u_{j+1}}{h_{j+1}}\right|^2
+(b^2+tr)|u_{N-1}|^2.
\]
Both coefficients are strictly positive; the right-hand side vanishes only for \(u=0\). Therefore \(1<\lambda_N<\lambda_\infty\). Taking \(u=h\) in the Rayleigh quotient further gives
\[
0<\lambda_\infty-\lambda_N\le\frac{(b^2+tr)r^{2N-2}}{\sum_{j=0}^{N-1}r^{2j}}=O_b(r^{2N}),
\]
so \(\lambda_N\nearrow\lambda_\infty\) (strict monotonicity follows from Step 1).

**4. Exact finite-size exponential coefficient.** For the unique \(\lambda_N>1\), let \(z_N\in(0,1)\) solve \(\lambda_N=c+t(z_N+z_N^{-1})\). Step 3 implies \(r<z_N<1\) and \(z_N\to r\). The eigenvector recurrence has solutions \(A z^j+B z^{-j}\). Its first and last rows are equivalent to ghost-boundary conditions \(u_{-1}=Hu_0\) and \(u_N=-Ku_{N-1}\), where \(H=(2-b)/a=1/r\) and \(K=b/a\). Eliminating \(A,B\) gives the exact equation
\[
(H z_N-1)(1+Kz_N)=z_N^{2N}(H-z_N)(z_N+K).
\]
Step 3 already yields \(z_N-r=O_b(r^{2N})\) by strict nonzero derivative \(\lambda'(r)=t(1-r^{-2})\), so \((z_N/r)^{2N}\to1\). Expanding the last equation at \(z=r=1/H\) gives
\[
\lim_{N\to\infty}\frac{z_N-r}{r^{2N}}=
\frac{(H-r)(r+K)}{H(1+Kr)}.
\]
Multiplying by \(-\lambda'(r)=t(r^{-2}-1)\) and simplifying exactly gives \(b(3-2b)^2/[2(2-b)^2(1-b)^2]\). This proves the asserted sharp limit.

## Verification

Run `python CHECK.py` after installing `requirements.txt`. The checker independently constructs all binary row-selector matrices for a range of cycle lengths and averaging parameters, compares their Gram eigenvalues to the claimed Jacobi eigenvalue, checks that precisely the one-hole patterns optimize, verifies the finite characteristic recurrences over rational parameters, checks the secular equation, and symbolically simplifies the asymptotic coefficient. It checks finitely many cases, not the universal limit. The proof of universal assertions is the preceding argument.

## Relationship to prior work

The recent sharp norm theorem of Madrid concerns the continuous, centered Hardy–Littlewood maximal operator with *all* centered radii; its optimal constant comes from martingale constructions. The present finite-cycle operator selects only the identity or a single weighted one-sided mean and has a different exact norm and optimizer geometry. Liao–Madrid–Palsson–Weigt study higher-order variation and derivatives of a discrete uncentered maximal operator, not this cyclic two-choice spectral problem. Zhang–Liu–Zhang study directed-graph maximal functions formed from *all* graph balls and give sharp results for special stars; the present two-radius cycle and its exponential spectral defect are not their stated norm calculation. A separate infinite-lattice two-choice calculation gives the limiting constant \(2/(2-\theta)\), but does not imply the strict finite-cycle values, their unique active patterns, or the coefficient of the exponentially small gap.

## Limitations

No assertion is made for more than two averaging choices, for arbitrary irregular directed graphs, or for exponents different from two. Near-parameter endpoints \(\theta\to0\) or \(\theta\to1\), the fixed-parameter asymptotic is not uniform. The phase-sensitive and positive maximal variants have identical norms but not identical complex equality families. Earlier unindexed equivalent finite-cycle calculations remain a priority risk; no independent review is claimed.

## References

1. J. Madrid, *The norm of the centered Hardy–Littlewood maximal operator*, arXiv:2609.12440, first publicly posted 2026-09-11, https://arxiv.org/abs/2609.12440 .
2. S.-Y. Liao, J. Madrid, E. Palsson and J. Weigt, *Sharp higher order regularity of discrete maximal functions*, arXiv:2607.10753, first publicly posted 2026-07-12, https://arxiv.org/abs/2607.10753 .
3. X. Zhang, F. Liu and H. Zhang, *Sharp Inequalities for the Hardy–Littlewood Maximal Operator on Finite Directed Graphs*, Mathematics **9** (2021), article 946, https://doi.org/10.3390/math9090946 .
