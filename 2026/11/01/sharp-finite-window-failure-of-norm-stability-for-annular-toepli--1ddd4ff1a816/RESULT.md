# Sharp finite-window failure of norm stability for annular Toeplitz displacement

## Finding

Fix a real number \(0<q<1\), let \(r=\sqrt q\), and let \(H\) be the Hardy Hilbert space on \(\{r<|z|<1\}\), with each boundary circle assigned normalized angular measure of total mass one. Write \(S=M_z\) and define the bounded linear **quadratic Toeplitz displacement** on \(\mathcal B(H)\) by
\[
\mathscr D_q(T)=S^{*2}TS^2-(1+q)S^*TS+qT.
\]
For each integer \(N\ge1\), let \(\mathcal C_N\) consist of all positive diagonal operators in the orthonormal Laurent basis \(e_n(z)=z^n/(1+q^n)^{1/2}\), supported on \(\{N+1,\ldots,2N\}\), whose norm equals one. Then every \(K\in\mathcal C_N\) satisfies
\[
\operatorname{dist}(K,\ker\mathscr D_q)
=\operatorname{dist}(K,\mathfrak T_q)=\frac12,
\]
where \(\mathfrak T_q=\{P_HM_\varphi|_H:\varphi\in L^\infty(\partial A_r)\}\) denotes the bounded-symbol Toeplitz operators. Nevertheless their best possible displacement residual obeys the **sharp asymptotic law**
\[
\boxed{\lim_{N\to\infty}N\min_{K\in\mathcal C_N}\|\mathscr D_q(K)\|=2(1-q).}
\]
Consequently \(\mathscr D_q\) has **nonclosed range** on \(\mathcal B(H)\): an arbitrarily small quadratic Toeplitz residual cannot force small operator-norm distance from a genuine Toeplitz operator, even on positive finite-rank contractions. The coefficient \(2(1-q)\) is exact for the natural positive-frequency window of length \(N\).

## Assumptions and scope

All Hilbert spaces and operators are complex. The two boundary measures are normalized separately; with this convention, the Laurent basis above is orthonormal. A diagonal operator \(K\in\mathcal C_N\) has coefficients \(k_n=\langle Ke_n,e_n\rangle\) satisfying \(k_n=0\) outside \([N+1,2N]\), \(0\le k_n\le1\), and \(\max_n k_n=1\). The minimum is well-defined because this finite-dimensional coefficient set is compact. The statement holds for each fixed \(q\in(0,1)\) as \(N\to\infty\); it claims no uniformity as \(q\to1\). No assumption of selfadjointness or positivity is imposed on the operators used in computing distance to the kernel or the Toeplitz class.

## Proof

**1. The Toeplitz displacement and its diagonal kernel.** Multiplication by \(z\) acts as the bilateral weighted shift \(Se_n=w_ne_{n+1}\), where
\[
w_n^2=\frac{1+q^{n+1}}{1+q^n}.
\]
If \(T\in\ker\mathscr D_q\) and \(t_n=\langle Te_n,e_n\rangle\), put \(g_n=(1+q^n)t_n\). Taking the diagonal entries of the displacement equation gives
\[
g_{n+2}-(1+q)g_{n+1}+qg_n=0 \qquad(n\in\mathbb Z).
\]
Since the characteristic roots are \(1\) and \(q\), there are constants \(A,B\in\mathbb C\) such that
\[
t_n=\frac{A+Bq^n}{1+q^n}.
\]
Thus \(t_n\to A\) as \(n\to+\infty\), \(t_n\to B\) as \(n\to-\infty\), and \(|t_n|\le\max\{|A|,|B|\}\) for every \(n\). For \(K\in\mathcal C_N\), the diagonal of \(K\) vanishes in both tails. Hence \(\|K-T\|\ge x:=\max\{|A|,|B|\}\). At a coordinate where \(k_n=1\), \(\|K-T\|\ge|1-t_n|\ge1-x\). Consequently \(\operatorname{dist}(K,\ker\mathscr D_q)\ge1/2\). Direct substitution gives \(\mathscr D_q(I)=0\), while positivity and contractivity give \(\|K-\tfrac12I\|=1/2\). This proves the exact distance to the full kernel.

For bounded \(\varphi\) on the two boundary circles, the Toeplitz matrix is
\[
\langle T_\varphi e_k,e_j\rangle=\frac{a_{j-k}+r^{j+k}b_{j-k}}{\sqrt{1+q^j}\sqrt{1+q^k}},
\]
where \(a_m,b_m\) are the outer and inner Fourier coefficients [1, Eq. (2.1)]. Substituting this expression into the two-step displacement gives zero: each boundary term is annihilated by its respective scalar polynomial factor. Thus \(\mathfrak T_q\subseteq\ker\mathscr D_q\). Since \(\tfrac12 I\) is a Toeplitz operator, its distance is also exactly \(1/2\).

**2. Exact scalar reduction.** For diagonal \(K\), the displacement is diagonal with coefficients
\[
d_n=\frac{(1+q^{n+2})k_{n+2}-(1+q)(1+q^{n+1})k_{n+1}+q(1+q^n)k_n}{1+q^n}.
\]
Define the unweighted recurrence residual \(\ell_n=k_{n+2}-(1+q)k_{n+1}+qk_n\). Elementary algebra gives the **exact identity**
\[
d_n-\ell_n=(1-q^2)\frac{q^n}{1+q^n}(k_{n+1}-k_{n+2}).
\]
The difference can be nonzero only for \(n\ge N-1\). Because the coefficients belong to \([0,1]\),
\[
\big|\|\mathscr D_q(K)\|-\sup_n|\ell_n|\big|\le(1-q^2)q^{N-1}.
\]
This error is exponentially small at fixed \(q\).

**3. Universal sharp lower bound.** Define increments \(a_j=k_j-k_{j-1}\). Then \(\ell_n=a_{n+2}-qa_{n+1}\). The increments vanish to the left of the support, so iteration of this recurrence yields \(\sup_j|a_j|\le\sup_n|\ell_n|/(1-q)\). Every coefficient profile in \(\mathcal C_N\) rises from zero to one and returns to zero. Its total variation across its \(N+1\) potentially nonzero increments is at least two. Hence
\[
2\le\sum_{j=N+1}^{2N+1}|a_j|\le\frac{N+1}{1-q}\sup_n|\ell_n|,
\]
and therefore
\[
\min_{K\in\mathcal C_N}\|\mathscr D_q(K)\|\ge \frac{2(1-q)}{N+1}-(1-q^2)q^{N-1}.
\]
Taking \(N\to\infty\) gives the claimed lower limit.

**4. Matching construction with endpoint boundary layers.** For \(0<\delta<1/4\), put \(c=2/(1-2\delta)\) and define a continuous, compactly supported piecewise-linear function \(g_\delta\) by
\[
g_\delta(t)=\begin{cases}
0,&t\notin[0,1],\\
ct/\delta,&0\le t\le\delta,\\
c,&\delta\le t\le\tfrac12-\delta,\\
-c(t-\tfrac12)/\delta,&\tfrac12-\delta\le t\le\tfrac12+\delta,\\
-c,&\tfrac12+\delta\le t\le1-\delta,\\
-c(1-t)/\delta,&1-\delta\le t\le1.
\end{cases}
\]
Let \(F_\delta(t)=\int_{-\infty}^{t}g_\delta(s)\,ds\). Direct integration and antisymmetry show that \(F_\delta\) is supported in \([0,1]\), has values in \([0,1]\), and has maximum one at \(t=1/2\). It is continuously differentiable; \(\|F_\delta'\|_\infty\le c\) and \(\operatorname{Lip}(F_\delta')\le c/\delta\). For sufficiently large \(N\), choose \(\delta=N^{-1/2}\), sample \(F_\delta\) at \(j/(N+1)\) for \(0\le j\le N+1\), and divide by the largest sampled value \(M_N\). Since the nearest grid point is within \(1/(2(N+1))\) of \(1/2\),
\[
1\ge M_N\ge1-\frac{c}{8\delta(N+1)^2}=1-o(1).
\]
Set \(k_{N+j}=F_\delta(j/(N+1))/M_N\) for \(1\le j\le N\), and all other coefficients to zero. This defines an element of \(\mathcal C_N\). The derivative and second-difference bounds give
\[
\sup_n|\ell_n|\le\frac{(1-q)c}{M_N(N+1)}+\frac{c}{\delta M_N(N+1)^2}.
\]
Together with step 2, this proves
\[
\limsup_{N\to\infty}N\min_{K\in\mathcal C_N}\|\mathscr D_q(K)\|\le2(1-q).
\]
The lower bound from step 3 completes the proof.

**5. Nonclosed range.** If the range of the bounded linear map \(\mathscr D_q\colon\mathcal B(H)\to\mathcal B(H)\) were closed, the bounded inverse theorem for its induced bijection on \(\mathcal B(H)/\ker\mathscr D_q\) would provide a constant \(C<\infty\) with \(\operatorname{dist}(T,\ker\mathscr D_q)\le C\|\mathscr D_q(T)\|\) for all \(T\). The constructed \(K_N\) have distance \(1/2\) and residual tending to zero, a contradiction.

## Verification

The accompanying Python 3 script `check.py` performs exact rational checks of the weighted recurrence identity, the scalar correction, positivity, normalization and the universal finite-window lower bound for \(q\in\{1/4,1/2,3/4\}\) at window sizes \(N\in\{16,25,49,100,225,400\}\). The executed script reported `EXACT_ASSERTIONS_PASSED 2607`. It also prints diagnostic products \(N\|\mathscr D_q(K_N)\|\); these are illustrative finite tests, **not** substitutes for the uniform analytical estimates and limiting proof.

## Relationship to prior work

Das and Narayanan [1] give the Hardy-annulus Laurent basis and Toeplitz matrix formula; their principal results concern zero products and compact Hankel operators, not norm-stability of a shift-polynomial residual. The quadratic displacement here follows directly from their two-boundary matrix formula. Earlier annular Hardy-space operator theory [2] supplies background. Jain and Sarkar [3], published after the motivating 2025 source, characterize exactly the zero set of the same quadratic equation and compact perturbations; their theorem concerns **exact vanishing**, not the finite-window minimax residual or the lack of norm stability with coefficient \(2(1-q)\). The new theorem does not claim that every approximate solution is close to a Toeplitz operator: it proves the opposite. Searches of mathematical records did not identify an equivalent sharp finite-window stability obstruction, but absence from search results is not proof of priority.

## Limitations

The sharp asymptotic is for diagonal positive contractions on one specified positive-frequency block, with the annulus radius fixed. Neither a general finite-\(N\) closed-form minimizer nor the optimal modulus among arbitrary non-diagonal operators is claimed. The result does not settle stability in weaker topologies, Schatten-norm geometries, or classes with additional regularity constraints. Any claim of publication priority requires independent literature validation.

## References

[1] S. Das and E. K. Narayanan, *Zero Products of Toeplitz operators on the Hardy and Bergman spaces over an annulus*, arXiv:2504.04270 (first posted 2025-04-05), especially §2, Eq. (2.1), https://arxiv.org/abs/2504.04270.

[2] D. Sarason, *The \(H^p\) spaces of an annulus*, Memoirs of the American Mathematical Society, 1965.

[3] S. Jain and J. Sarkar, *Characterizations of Toeplitz operators on the annulus*, arXiv:2610.40118v1 (first posted 2026-10-29), especially Theorems 2.2 and 4.2, https://arxiv.org/abs/2610.40118.
