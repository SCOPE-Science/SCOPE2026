# A bulk–edge transition for high-degree Bergman Hankel leakage

## Finding

Consider the big anti-analytic Hankel operators \(H_k=(I-P_\alpha)M_{\overline z^{\,k}}\) on the normalized weighted analytic Bergman disk, with \(\alpha>-1\) fixed and integer \(k\to\infty\). Put \(p=\alpha+1>0\). Their complete squared singular-value multiset is

\[
 d_{n,k}=\frac{\mu_{n+k}}{\mu_n}
 -\mathbf 1_{\{n\ge k\}}\frac{\mu_n}{\mu_{n-k}},\qquad
 \mu_n=\frac{\Gamma(p+1)\Gamma(n+1)}{\Gamma(n+p+1)},\quad n\ge0.
\]

The genuinely large-symbol-degree regime has the continuous profile

\[
 F_p(x)=\left(\frac{x}{1+x}\right)^p-
 \mathbf1_{\{x>1\}}\left(\frac{x-1}{x}\right)^p,\qquad x\ge0,
\]

where the second term is zero for \(0\le x\le1\). Specifically, \(d_{\lfloor kx\rfloor,k}\to F_p(x)\) for every \(x\ge0\). For every fixed \(q>1\), the complete Schatten-mass asymptotic is

\[
 \boxed{\lim_{k\to\infty}\frac{\|H_k\|_{S_q}^{q}}{k}
 =\int_0^\infty F_p(x)^{q/2}\,dx.}
\]

For each fixed squared-singular-value threshold \(0<\tau<M_p:=\max_{x\ge0}F_p(x)\), its counting function obeys

\[
 \boxed{\lim_{k\to\infty}\frac1k
 \#\{j:s_j(H_k)^2>\tau\}
 =\left|\{x>0:F_p(x)>\tau\}\right|.}
\]

The limiting operator norm has a **sharp weight-dependent maximizing-degree transition**:

\[
 \boxed{\lim_{k\to\infty}\|H_k\|^2
 =M_p=\begin{cases}
 2^{-p},&0<p\le1,\\
 \displaystyle\left(\frac{x_p}{1+x_p}\right)^p-
 \left(\frac{x_p-1}{x_p}\right)^p,&p>1,
 \end{cases}}
\]

where \(x_p>1\) is the unique solution of

\[
 \left(1-\frac1{x_p}\right)^{p-1}
 \left(1+\frac1{x_p}\right)^{p+1}=1.
\]

Every choice of indices \(n_k\) maximizing \(d_{n,k}\) satisfies \(n_k/k\to1\) if \(-1<\alpha\le0\), and \(n_k/k\to x_p>1\) if \(\alpha>0\). For the unweighted Bergman space \(\alpha=0\), the **finite-degree exact identity** is \(\|H_k\|^2=1/2\), attained only at \(n=k-1\). At \(\alpha=2\), the optimal ratio is the golden ratio \(x_3=(1+\sqrt5)/2\), with \(M_3=5\sqrt5-11\).

A further exact normalization, valid for every \(k\ge1\) and \(\alpha>-1\), is \(\|H_k\|_{S_2}^2=k\); this is the familiar Dirichlet/Hilbert–Schmidt trace identity in the present monomial setting, **not** an originality claim. In particular, \(\int_0^\infty F_p(x)\,dx=1\) for all \(p>0\).

## Assumptions and scope

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and set

\[
 dA_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dA(z),\qquad \alpha>-1.
\]

The space \(A^2_\alpha(\mathbb D)\) is the analytic closed subspace of \(L^2(dA_\alpha)\); \(P_\alpha\) is its orthogonal projection. Multiplication by \(\overline z^{\,k}\) is bounded. The operator \(H_k\) maps \(A^2_\alpha\) into the orthogonal complement. The singular values \(s_j(H_k)\) are arranged in nonincreasing order with multiplicity and are indexed by \(j\ge1\). All limits in \(k\) keep \(\alpha\), the Schatten exponent \(q\) and any counting threshold fixed. Every \(H_k\) is compact.

## Proof

**1. Exact singular values.** Orthogonality of monomials and the beta integral give \(\|z^n\|_{A^2_\alpha}^2=\mu_n\). With \(e_n=z^n/\sqrt{\mu_n}\), the function \(\overline z^{\,k}e_n\) has angular frequency \(n-k\). Consequently, the vectors \(H_ke_n\) have pairwise distinct angular frequencies and are orthogonal. The squared norm of the unprojected vector is \(\mu_{n+k}/\mu_n\). The analytic projection vanishes for \(n<k\); for \(n\ge k\) its squared norm is \(\mu_n/\mu_{n-k}\). This proves the displayed formula for \(d_{n,k}\), including multiplicities and the absence of off-diagonal Gram terms.

Define, for real \(t\ge0\),

\[
 r_k(t)=\prod_{j=1}^{k}\frac{t+j}{t+j+p}.
\]

Then \(d_{n,k}=r_k(n)-\mathbf1_{\{n\ge k\}}r_k(n-k)\). Every factor increases in \(t\), so all \(d_{n,k}\) are strictly positive. For each fixed \(k\), \(r_k(n)\to1\) and \(d_{n,k}\to0\), proving compactness and attainment of the norm by an index \(n\).

**2. Scaled shape, including the endpoints.** The standard gamma-ratio estimate \(\Gamma(t+p+1)/\Gamma(t+1)=t^p(1+O_p(t^{-1}))\) as \(t\to\infty\), applied to the exact moment ratios, gives \(r_k(\lfloor kx\rfloor)\to(x/(1+x))^p\) for \(x>0\), uniformly on compact subintervals of \((0,\infty)\). For \(x>1\), the shifted term tends to \(((x-1)/x)^p\). At \(x=1\), that shifted ratio equals \(r_k(0)=\mu_k/\mu_0\to0\); for \(x<1\) it is absent. At \(x=0\), \(r_k(0)\to0\). Thus the asserted pointwise shape limit holds at every \(x\ge0\).

For later uniformity, the gamma-ratio bounds imply, with a constant depending only on \(p\),

\[
 0\le d_{n,k}\le r_k(n)\le C_p
 \left(\frac{n+1}{n+k+1}\right)^p.
\]

Hence all scaled indices \(n\le\delta k\) contribute at most \(C_p(\delta+k^{-1})^p\). On the far tail, differentiation of the finite product gives

\[
 0<r_k'(t)=r_k(t)\sum_{j=1}^k
 \frac{p}{(t+j)(t+j+p)}\le\frac{pk}{t^2}\quad(t>0).
\]

Integrating from \(n-k\) to \(n\) shows that, for every \(n\ge2k\),

\[
 0<d_{n,k}\le \frac{pk^2}{n(n-k)}\le\frac{2pk^2}{n^2}.
\]

These inequalities together with gamma-ratio convergence prove uniform convergence of \(d_{n,k}\) to \(F_p(n/k)\) on each bounded scaled-degree interval and control the region \(n/k\to\infty\).

**3. Operator-norm maximizer.** The profile is continuous, vanishes at \(0\) and tends to \(0\) at infinity. It strictly increases on \((0,1)\). For \(x>1\), direct differentiation yields

\[
 F_p'(x)=\frac{p}{x^2}\left[(1+x^{-1})^{-p-1}-(1-x^{-1})^{p-1}\right].
\]

Write \(y=x^{-1}\) and \(g_p(y)=(p-1)\log(1-y)+(p+1)\log(1+y)\). The sign of \(F_p'(x)\) is the opposite of that of \(g_p(y)\). If \(0<p\le1\), both terms of \(g_p(y)\) are nonnegative and the second positive, so \(F_p\) decreases on \((1,\infty)\). If \(p>1\),

\[
 g_p'(y)=\frac{2(1-py)}{1-y^2}.
\]

Thus \(g_p\) starts at zero, rises to its only maximum at \(y=1/p\), and falls to minus infinity as \(y\uparrow1\); it has exactly one zero in \((1/p,1)\). It follows that \(F_p\) has a unique global maximizer \(x_p>1\), characterized by the displayed root equation. Uniform convergence on compact scaled-degree ranges, together with the small- and large-index bounds in Step 2, implies the norm limit and convergence of **all** maximizing-degree ratios.

For \(p=1\), \(\mu_n=(n+1)^{-1}\), so the exact finite-degree sequence is

\[
 d_{n,k}=\begin{cases}
 (n+1)/(n+k+1),&0\le n<k,\\
 k^2/[(n+1)(n+k+1)],&n\ge k.
 \end{cases}
\]

The first branch strictly increases to \(1/2\) at \(n=k-1\); the second strictly decreases and starts below \(1/2\). For \(p=3\), the root equation reduces to \((1-y)(1+y)^2=1\) for \(y>0\); its root is \(y=(\sqrt5-1)/2\), yielding the stated golden-ratio values.

**4. Counting laws and Schatten masses.** Because \(F_p\) is strictly increasing before its unique maximum and strictly decreasing thereafter, every nontrivial superlevel set has at most two boundary points and finite length. The uniform local profile convergence and the global tail bounds therefore give the counting-function limit by Riemann sums. For \(q>1\), the far-tail bound gives, for \(R\ge2\),

\[
 \limsup_{k\to\infty}\frac1k\sum_{n\ge Rk}d_{n,k}^{q/2}
 \le C_{p,q}R^{1-q}\xrightarrow[R\to\infty]{}0.
\]

Ordinary Riemann sums on \([0,R]\) and then \(R\to\infty\) prove the Schatten-mass limit. The hypothesis \(q>1\) is sharp for each fixed \(k\), because \(d_{n,k}\sim pk^2/n^2\) as \(n\to\infty\), a fixed-symbol Schatten threshold already known in Bergman Hankel theory.

Finally, the exact finite trace telescopes:

\[
 \sum_{n=0}^{N}d_{n,k}
 =\sum_{n=N-k+1}^{N}r_k(n),\qquad N\ge k.
\]

Since \(r_k(n)\to1\), the infinite sum is \(k\), the claimed Hilbert–Schmidt identity. The continuous integral of \(F_p\) is also exactly \(1\): subtracting the two integrals after translating \(x\mapsto x-1\) leaves \(\int_{R-1}^{R}(x/(1+x))^p\,dx\to1\).

## Verification

The standalone `checker.py` uses only Python's standard library. It performs exact rational beta-moment comparisons and finite checks of the \(p=1\) norm formula, scaled spectral convergence, the finite trace telescoping identity, and the explicit golden-ratio maximum. Run `python checker.py`. These finite tests supplement, but do not replace, Steps 1–4. The infinite limits and uniqueness statements are proved analytically.

## Relationship to prior work

Peláez and Rättyä study Bergman projections and BMO/Bloch mapping properties; they establish the analytic-function-space framework, not a degree-growing singular-value law [1]. Bourass, El-Fallah, Marrhich and Naqos derive anti-analytic Hankel singular-value estimates and sharp fixed-symbol **singular-index** asymptotics, including the critical \(1/j\) decay [2]. Their fixed-symbol limit holds with the symbol held fixed, whereas the present limit sends the monomial symbol degree to infinity together with singular degrees of order \(k\), and determines a different spectral observable: a macroscopic distribution, its exact norm peak and weight-dependent displacement. Peláez, Perälä and Rättyä establish boundedness characterizations for Hankel operators under radial weights [3]; those criteria do not state the present counting/profile formulas.

The explicit fixed-degree moment diagonalization, individual Schatten membership, and Hilbert–Schmidt trace identity are background facts, **not** claimed discoveries. The contribution assessed here is their nontrivial uniform high-symbol-degree spectral consequence, specifically the sharp bulk–edge phase diagram and all-threshold asymptotics.

## Limitations

All parameters \(\alpha\) and \(q\) are fixed before the limit \(k\to\infty\); no claim concerns varying weights or a joint \(q\)-limit. The counting theorem excludes threshold values outside \((0,M_p)\). The theorem gives leading order only, not a uniform error rate for the maximizing index. The originality comparison covers the identified major primary sources and published nearby records, but cannot rule out an equivalent historical theorem under different terminology. Independent mathematical audit has not been performed.

## References

[1] J. Á. Peláez and J. Rättyä, *Bergman projection and BMO in hyperbolic metric: improvement of classical result*, arXiv:2207.01086 (initial public posting 2022-07-03); *Mathematische Zeitschrift* **305**, article 19 (2023), doi:10.1007/s00209-023-03343-1. Primary MSC2020: 30H20.

[2] M. Bourass, O. El-Fallah, I. Marrhich and H. Naqos, *On singular values of Hankel operators on Bergman spaces*, arXiv:2102.01743 (initial public posting 2021-02-02).

[3] J. Á. Peláez, A. Perälä and J. Rättyä, *Hankel operators induced by radial Bekollé–Bonami weights on Bergman spaces*, arXiv:1806.09854 (initial public posting 2018-06-26); *Mathematische Zeitschrift* **296**, 211–238 (2020), doi:10.1007/s00209-019-02412-8.

[4] J. Arazy, S. D. Fisher and J. Peetre, *Hankel operators on weighted Bergman spaces*, *American Journal of Mathematics* **110**, 989–1053 (1988).
