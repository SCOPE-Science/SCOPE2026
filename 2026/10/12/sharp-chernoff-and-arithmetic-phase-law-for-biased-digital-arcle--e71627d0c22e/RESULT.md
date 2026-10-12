# Sharp Chernoff and arithmetic-phase law for biased digital arclength

## Finding

Fix an integer \(q\ge2\) and a strictly positive, nonuniform digit law \(P=(p_0,\ldots,p_{q-1})\). For independent digits \(D_i\sim P\), let \(X=\sum_{i\ge1}D_iq^{-i}\), let \(F\) be its continuous distribution function, and let \(F_n\) interpolate \(F\) linearly on the base-\(q\) grid of mesh \(q^{-n}\). Write \(L_n\) for the graph's Euclidean arclength and \(\Delta_n=2-L_n\) for its positive remaining length deficit. Let \(U=(1/q,\ldots,1/q)\). Then for every integer \(n\ge1\),

\[
(2-\sqrt2)\bigl(1-d_{\mathrm{TV}}(P^{\otimes n},U^{\otimes n})\bigr)
\le\Delta_n\le
1-d_{\mathrm{TV}}(P^{\otimes n},U^{\otimes n}).
\]

In particular, with the strictly subunit Chernoff affinity

\[
Z(P,U)=\min_{0\le t\le1}\sum_{j=0}^{q-1}(1/q)^{1-t}p_j^t,
\qquad 0<Z(P,U)<1,
\]

the precise exponential convergence rate is

\[
\lim_{n\to\infty}(2-L_n)^{1/n}=Z(P,U),
\qquad \lim_{n\to\infty}\frac{-\log(2-L_n)}n=-\log Z(P,U).
\]

For \(q=2\), relabel digits to write \(p_0=p\in(1/2,1)\), \(p_1=1-p\), and define

\[
\begin{aligned}
a&=\log(2p),& b&=\log(2(1-p)),&h&=a-b=\log\frac p{1-p},\\
\alpha&=-\frac b h,& t&=\frac1h\log\frac\alpha{1-\alpha},&
Z&=\frac{e^{ta}+e^{tb}}2.
\end{aligned}
\]

Here \(0<\alpha,t<1\). Set, for real \(s\) and \(u\),

\[
\phi(s)=1+e^s-\sqrt{1+e^{2s}},\quad
g_t(s)=e^{-ts}\phi(s),\quad
H_p(u)=\sum_{j\in\mathbb Z}g_t\bigl(h(j-u)\bigr).
\]

The strictly positive, real-analytic, one-periodic function \(H_p\) has the **sharp lattice local-limit law**

\[
\boxed{\displaystyle
2-L_n=\frac{Z^n}{\sqrt{2\pi n\alpha(1-\alpha)}}
\left(H_p(\{n\alpha\})+o(1)\right),\qquad n\to\infty.}
\]

The little-\(o(1)\) error is uniform with respect to the phase argument. Moreover \(H_p\) is nonconstant for **every** \(p\in(1/2,1)\): its Fourier coefficients are explicitly

\[
\widehat H_p(m)=\frac1h\,
\frac{B\bigl(1-u_m/2,(1+u_m)/2\bigr)}{2u_m(1-u_m)},
\qquad u_m=t-\frac{2\pi i m}{h},\quad m\in\mathbb Z,
\]

and none of these coefficients vanishes. At the simple rational digit bias \(p=9/10\), the number \(\alpha=\log5/\log9\) is irrational, so the normalized length deficit

\[
\sqrt{2\pi n\alpha(1-\alpha)}\,Z^{-n}(2-L_n)
\]

has **no limit**. Its set of subsequential limits is exactly the nondegenerate interval \([\min_{u\in[0,1]}H_p(u),\max_{u\in[0,1]}H_p(u)]\).

## Assumptions and scope

The digits are independent and identically distributed, the base is an integer \(q\ge2\), and every digit weight is strictly positive. Uniform weights are excluded; in that case \(F(x)=x\), every \(L_n=\sqrt2\), and the displayed singular-limit normalization does not apply. At nonuniform weights, the digit product law is singular with respect to Lebesgue measure and the polygonal lengths increase to \(2\); the statements here quantify that convergence rather than assume its rate. No claims are made for dependent or non-identically distributed digits, or for weights zero at some digit. The binary full local-limit statement applies to fixed \(p\in(1/2,1)\), with all constants depending on that \(p\).

The values of the CDF at the endpoints of a rank-\(n\) base-\(q\) cylinder labeled by a word \(w=(w_1,\ldots,w_n)\) differ by \(P_w=\prod_{i=1}^np_{w_i}\); its horizontal width is \(U_w=q^{-n}\). Consequently, the original finite-rank arclength identity is

\[
L_n=\sum_{w\in\{0,\ldots,q-1\}^n}\sqrt{U_w^2+P_w^2},
\qquad \sum_w U_w=\sum_w P_w=1.
\]

## Proof

**1. Exact deficit and comparison with product overlap.** Put \(f(z)=1+z-\sqrt{1+z^2}\) for \(z>0\). Direct rationalization and symmetry \(f(z)=zf(1/z)\) give

\[
\Delta_n=\sum_w U_w f(P_w/U_w),\qquad
(2-\sqrt2)\min(1,z)\le f(z)\le\min(1,z).
\]

Indeed \(f(z)/z\) decreases from \(1\) to \(2-\sqrt2\) on \(0<z\le1\), since \(f(z)=2z/(1+z+\sqrt{1+z^2})\); the identity \(f(z)=zf(1/z)\) handles \(z\ge1\). Thus \(\Delta_n\) is within universal fixed factors of \(\sum_w\min(U_w,P_w)=1-d_{\rm TV}(P^{\otimes n},U^{\otimes n})\). In particular its positivity is strict.

**2. Exponential rate without invoking any unproved large-deviation limit.** Let

\[
\Psi(t)=\sum_{j=0}^{q-1}(1/q)^{1-t}p_j^t
=\frac1q\sum_j(qp_j)^t,\quad 0\le t\le1.
\]

The derivatives of \(\log\Psi\) at the endpoints are respectively \(-D(U\Vert P)<0\) and \(D(P\Vert U)>0\). Strict positivity of the variance of \(\log(qp_j)\) under every exponential tilt makes \(\log\Psi\) strictly convex. Hence it has a unique minimizer \(t\in(0,1)\), and \(Z=\Psi(t)\in(0,1)\). Define the tilt \(T_j=(1/q)^{1-t}p_j^t/Z\), and for a word define \(S_n(w)=\sum_{i=1}^n\log(qp_{w_i})\). Under \(T^{\otimes n}\), \(\mathbb ES_n=0\), \(\operatorname{Var}S_n=n\sigma^2\) with \(\sigma^2>0\). The overlap rewrites exactly as

\[
\sum_w\min(U_w,P_w)
=Z^n\mathbb E_{T^{\otimes n}}
\min\bigl(e^{-tS_n},e^{(1-t)S_n}\bigr).
\]

The overlap is at most \(Z^n\). Chebyshev's inequality gives \(\Pr_T(|S_n|\le\sqrt{2n\sigma^2})\ge1/2\); on that event the last minimum is at least \(\exp[-\max(t,1-t)\sqrt{2n\sigma^2}]\). Therefore

\[
\frac{Z^n}{2}\,e^{-\max(t,1-t)\sqrt{2n\sigma^2}}
\le1-d_{\mathrm{TV}}(P^{\otimes n},U^{\otimes n})\le Z^n.
\]

The fixed-factor inequalities from step 1 prove the root and logarithmic limits.

**3. Binary tilted binomial representation.** Assume \(q=2\) and \(p>1/2\). The two values of \(\log(2p_j)\) are \(a>0\) and \(b<0\), separated by \(h>0\). Mean zero of the tilt requires probability \(\alpha=-b/h\) on the first digit. The tilt formula yields \(\alpha/(1-\alpha)=(p/(1-p))^t\), establishing the displayed expression for \(t\). If \(K\sim\operatorname{Bin}(n,\alpha)\) is the tilted number of first digits, then \(S_n=h(K-n\alpha)\). Since \(f(e^s)=\phi(s)\), the **exact** identity is

\[
\Delta_n=Z^n\mathbb E\,g_t\bigl(h(K-n\alpha)\bigr).
\]

The kernel decays exponentially in both tails: as \(s\to+\infty\), \(g_t(s)\sim e^{-ts}\); as \(s\to-\infty\), \(g_t(s)\sim e^{(1-t)s}\). Thus the phase series \(H_p\) and all its real derivatives converge absolutely and uniformly on compact sets; the same estimates extend analytically to a sufficiently narrow complex horizontal strip.

**4. A uniform lattice local limit.** Write \(m_n=\lfloor n\alpha\rfloor\), \(u_n=\{n\alpha\}\), and \(K=m_n+j\). For each fixed integer \(j\), Stirling's formula gives, uniformly for \(u_n\in[0,1]\),

\[
\sqrt{2\pi n\alpha(1-\alpha)}\,
\Pr\{K=m_n+j\}=1+o(1).
\]

The maximum mass of \(\operatorname{Bin}(n,\alpha)\) is bounded by \(C_{\alpha}/\sqrt n\), uniformly in \(n\ge1\). Multiplying this bound by the exponentially decaying kernel controls the contributions from \(|j|>J\), uniformly in both the sample size and the phase, by \(C\sum_{|j|>J}e^{-c|j|}\). First fix \(J\), apply the local approximation, and then let \(J\to\infty\). The announced sharp asymptotic follows, including a phase-uniform \(o(1)\).

**5. Explicit Fourier transform and nonvanishing.** For complex \(u\) with \(0<\Re u<1\), consider the absolutely convergent Mellin integral

\[
J(u)=\int_{-\infty}^{\infty}e^{-us}\phi(s)\,ds
=\int_0^\infty z^{-u-1}(1+z-\sqrt{1+z^2})\,dz.
\]

Integrating twice by parts is legitimate because \(f(z)\sim z\) at zero and \(f(z)\to1\) at infinity, while \(f''(z)=-(1+z^2)^{-3/2}\). It yields

\[
J(u)=\frac{1}{u(1-u)}\int_0^\infty
\frac{z^{1-u}}{(1+z^2)^{3/2}}\,dz
=\frac{B(1-u/2,(1+u)/2)}{2u(1-u)}.
\]

Periodizing \(g_t\) at step \(h\) gives \(\widehat H_p(m)=h^{-1}J(t-2\pi im/h)\). Since Euler's gamma function has no zeros and both beta arguments have positive real parts, none of these Fourier coefficients vanishes. In particular the coefficient at \(m=1\) is nonzero, proving that \(H_p\) is not constant.

**6. Actual nonconvergence at a rational bias.** For \(p=9/10\), \(b=-\log5\) and \(h=\log9\), hence \(\alpha=\log5/\log9\). If \(\alpha\) were rational and positive, unique factorization would imply \(5^r=9^s\) for positive integers \(r,s\), impossible. Thus \(\{n\alpha\}\) is dense in \([0,1]\). The uniform phase local limit in step 4 transfers this density to the exact cluster set \(H_p([0,1])\), a nondegenerate compact interval by step 5 and continuity. This completes the proof.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. Run `python3 verify.py`. It reproduces the direct word-by-word arclength formula against a grouped binomial expression in 40 cases; verifies the defect/product-overlap comparison for 15 small multi-category cases; compares exact tilted binomial expectations with the phase asymptotic at seven sample sizes up to 2000; and checks a positive nonconstant phase profile numerically for the rational bias \(p=9/10\). The printed large-sample relative discrepancies decay in magnitude, reaching approximately \(0.0026\) at \(n=2000\). These finite diagnostics do not prove either the all-parameter theorem or the nonzero Fourier coefficient; the analytic steps above do.

## Relationship to prior work

Pfeffer, Smith and Severa (arXiv:2309.07366, Theorem 4.2) obtained the exact finite-rank piecewise-linear arclength identity, and Corollary 4.1 proved convergence to total arclength \(2\) for a nonuniform die. Section 5.1 specifically motivates quantitative understanding of the iterative length gain; those facts and the underlying self-similar construction are *not* newly claimed here. The additional statements proved here are the Chernoff exponent for every strictly positive nonuniform alphabet law and, for every biased binary law, a sharp nonconstant lattice-prefactor formula, its explicit beta-function Fourier coefficients, and nonconvergence for an elementary rational bias.

The product-testing Chernoff expression, Stirling local limits, and beta/gamma identities are standard probabilistic and analytic ingredients, rather than separately novel claims. Herbst, Møller and Svane (2024) study the limiting distribution of **scaled digit remainders** for absolutely continuous parent laws, including total-variation rates, not graph arclength of the singular stationary biased-digit CDF. Cornean and coauthors (2022) characterize stationary digit laws and their Lebesgue decomposition; these structural results do not imply the quantitative graph-length statements by a cited formula. The link through hypothesis-testing overlap is proved here at the precise level needed to apply those ingredients.

## Limitations

The rate \(Z\) is an exponential rate, not a universal prefactor for arbitrary \(q\), and there is no asserted nonlattice multivariate local-limit classification for \(q\ge3\). The explicit phase law assumes binary, fixed strictly positive bias. For extremely small bias, constants in the asymptotic estimates depend on that bias and no uniform approach to \(p=1/2\) or \(p=1\) is asserted. The graph length of the limiting singular CDF is not recomputed independently of the known theory: the deficit identity and bound already establish convergence directly. The proof does not establish scientific priority against every historical source using different singular-function terminology; earlier equivalent arclength asymptotics remain a bibliographic risk. No inference method for observed physical digits or hardware data is claimed.

## References

1. D. T. Pfeffer, J. D. Smith and W. Severa, *Induced Distributions from Generalized Unfair Dice*, arXiv:2309.07366 (initial posting 14 September 2023; Theorem 4.2, Corollary 4.1, Section 5.1). https://arxiv.org/html/2309.07366v2
2. I. W. Herbst, J. Møller and A. M. Svane, *How Many Digits are Needed?*, Methodology and Computing in Applied Probability 26, article 5 (2024); arXiv:2307.06685, DOI:10.1007/s11009-024-10073-2.
3. H. D. Cornean, I. W. Herbst, J. Møller, K. S. Sørensen and B. B. Støttrup, *Characterization of random variables with stationary digits*, Journal of Applied Probability 59 (2022), 931–947, DOI:10.1017/jpr.2022.6.
