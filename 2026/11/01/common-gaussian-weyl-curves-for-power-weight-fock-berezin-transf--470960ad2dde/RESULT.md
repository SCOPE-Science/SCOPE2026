# Common Gaussian Weyl curves for power-weight Fock Berezin transforms

## Finding

**Theorem (simultaneous singular approximate eigenvectors).** Fix \(m>2\). For every finite list \(\alpha_1,\dots,\alpha_d>0\) and every \(s\in[0,\infty]\), there exists a sequence of unit vectors \(f_n\in L^2(\mathbb C,dA)\) converging weakly to zero and satisfying

\[
\max_{1\le j\le d}\big\|(T_{\alpha_j}-e^{-s/\alpha_j}I)f_n\big\|_2\longrightarrow0,
\qquad e^{-\infty}:=0.
\]

Here \(T_\alpha\) is the Berezin integral operator of the generalized Fock space with weight \(e^{-\alpha |z|^m}\), defined precisely below. In particular, for any noncommutative complex polynomial \(P\) in \(d\) variables,

\[
\big\|P(T_{\alpha_1},\ldots,T_{\alpha_d})\big\|_{\mathrm{ess}}
\ge \sup_{s\in[0,\infty]}\big|P(e^{-s/\alpha_1},\ldots,e^{-s/\alpha_d})\big|.
\tag{1}
\]

For two distinct parameters, put \(r=\alpha/\beta\). A concrete consequence is the strictly positive quantitative noncompactness bound

\[
\boxed{\ \|T_\alpha-T_\beta\|_{\mathrm{ess}}\ \ge\ |r-1|r^{-r/(r-1)}\ >0\ }.
\tag{2}
\]

For example, the right-hand side is \(1/4\) when \(\alpha=2\beta\). No optimality of the **operator** essential-norm bounds is claimed: they are sharp maxima **along the exhibited Gaussian multiplier curve**.

## Assumptions and scope

The ambient Hilbert space is \(L^2(\mathbb C,dA)\), where \(dA\) is ordinary planar Lebesgue area. Write \(p=m/2>1\), and let

\[
\kappa_{\alpha,p}=\frac{p\alpha^{1/p}}{\pi\Gamma(1/p)},\qquad
 d\mu_{\alpha,p}(w)=\kappa_{\alpha,p}e^{-\alpha|w|^{2p}}dA(w).
\]

The holomorphic Fock space \(\mathcal F_{\alpha,p}\) has the norm induced by this probability measure. Denote its reproducing kernel by \(K_\alpha(z,w)\). The operator in the theorem is

\[
(T_\alpha f)(z)=\int_{\mathbb C}B_\alpha(z,w)f(w)\,dA(w),\quad
B_\alpha(z,w)=\kappa_{\alpha,p}
\frac{|K_\alpha(z,w)|^2}{K_\alpha(z,z)}e^{-\alpha|w|^{2p}}.
\tag{3}
\]

Boundedness of \(T_\alpha\) on this **unweighted** \(L^2\) space, and the global off-diagonal kernel bound used below, are established by Borichev–Fantolini–Youssfi [1, Proposition 4.1 and Lemma 3.2]. The theorem requires fixed \(m>2\) and finitely many fixed positive weight parameters; no parameter-uniformity is claimed.

## Proof

**1. Exact kernel normalization.** Polar integration gives, for every integer \(n\ge0\),

\[
\int_{\mathbb C}|w|^{2n}\,d\mu_{\alpha,p}(w)
=\alpha^{-n/p}\frac{\Gamma((n+1)/p)}{\Gamma(1/p)}.
\]

The orthogonality of monomials therefore yields the entire kernel identity

\[
K_\alpha(z,w)=\Gamma(1/p)\sum_{n=0}^{\infty}
\frac{\alpha^{n/p}(z\overline w)^n}{\Gamma((n+1)/p)}
=\Gamma(1/p)E_{1/p,1/p}(\alpha^{1/p}z\overline w).
\tag{4}
\]

For arguments in a fixed sufficiently narrow sector about the positive real axis, the standard Mittag–Leffler expansion used in [1, Section 3] gives

\[
K_\alpha(z,w)
= p\,\Gamma(1/p)\alpha^{1-1/p}
(z\overline w)^{p-1}e^{\alpha(z\overline w)^p}\bigl(1+o(1)\bigr)
\tag{5}
\]

as \(|z\overline w|\to\infty\), with the principal power and uniformity in such a smaller sector. In particular, \(K_\alpha(z,z)>0\), and the same formula applies on the diagonal.

**2. A local Gaussian limit.** Set \(\delta_R=R^{1-p}\), and for fixed \(u,v\in\mathbb C\) put \(z=R+\delta_Ru\) and \(w=R+\delta_Rv\). The exact leading coefficient obtained from (3)–(5) is

\[
\delta_R^2B_\alpha(R+\delta_Ru,R+\delta_Rv)
\longrightarrow
G_\alpha(u-v),\qquad
G_\alpha(h)=\frac{\alpha p^2}{\pi}e^{-\alpha p^2|h|^2}.
\tag{6}
\]

The convergence is locally uniform in \((u,v)\). To check both exponent and constant rather than just their orders, Taylor expansion about the positive real axis gives

\[
2\operatorname{Re}(z\overline w)^p-|z|^{2p}-|w|^{2p}
=-p^2|u-v|^2+o(1),
\]

where \(R^{2p-2}\delta_R^2=1\). The algebraic prefactor in (3)–(5) is

\[
\kappa_{\alpha,p}\cdot
p\Gamma(1/p)\alpha^{1-1/p}\cdot
\delta_R^2R^{2p-2}=\frac{\alpha p^2}{\pi}.
\]

**3. Strong localization for compactly supported probes.** Let \(U_R:L^2(\mathbb C)\to L^2(\mathbb C)\) be the unitary

\[
(U_RF)(z)=\delta_R^{-1}F\bigl((z-R)/\delta_R\bigr).
\]

We claim that every \(F\in C_c^\infty(\mathbb C)\) obeys

\[
\big\|U_R^{-1}T_\alpha U_RF-G_\alpha*F\big\|_2\longrightarrow0.
\tag{7}
\]

Here is a tail argument completing the local convergence (6). Put \(B_{\alpha,R}(u,v)=\delta_R^2B_\alpha(R+\delta_Ru,R+\delta_Rv)\); its integral operator is \(U_R^{-1}T_\alpha U_R\). For fixed \(L<\infty\) and \(|v|\le L\), [1, Lemma 3.2, equation (3.9)] bounds the original kernel by a constant times

\[
\frac{e^{-c d_\alpha(z,w)^2}}{\tau_\alpha(z)\tau_\alpha(w)},
\qquad\tau_\alpha(w)\asymp R^{1-p}.
\]

For \(|z-R|<R/4\), the metric comparison [1, equation (2.1)] yields \(d_\alpha(z,w)\gtrsim R^{p-1}|z-w|\), and \(\tau_\alpha(z)\asymp R^{1-p}\). Consequently, uniformly for \(|v|\le L\) and sufficiently large \(R\),

\[
B_{\alpha,R}(u,v)\le C e^{-c'|u-v|^2}
\qquad (|\delta_Ru|<R/4).
\]

On the complementary region \(|z-R|\ge R/4\), the same intrinsic-distance estimates imply

\[
d_\alpha(z,R+\delta_Rv)^2\gtrsim R^{2p}+|z|^{2p},
\]

while \(\tau_\alpha(z)^{-1}\lesssim(1+|z|)^{p-1}\). Thus the \(L^2(du)\) norm of the rescaled kernel on that complementary region tends to zero uniformly for \(|v|\le L\): after changing variables to \(z\), its square is bounded by a constant times

\[
\int_{\mathbb C}(1+|z|)^{2p-2}
 e^{-c''(R^{2p}+|z|^{2p})}\,dA(z)=o(1).
\]

The local uniform limit (6), the Gaussian bound on the inner region, and this outer tail establish (7), by dominated convergence and Minkowski's integral inequality.

**4. Simultaneous wave packets.** Identify \(\mathbb C\) with \(\mathbb R^2\) and use the Fourier convention \(\widehat F(\xi)=\int e^{-i\xi\cdot u}F(u)\,du\). The probability density \(G_\alpha\) has multiplier

\[
\widehat G_\alpha(\xi)
=e^{-|\xi|^2/(4\alpha p^2)}.
\tag{8}
\]

Choose \(\chi\in C_c^\infty(\mathbb R^2)\) with \(\|\chi\|_2=1\). For \(L\ge1\) and \(\xi\in\mathbb R^2\), set \(F_{L,\xi}(u)=L^{-1}\chi(u/L)e^{i\xi\cdot u}\). Then \(\|F_{L,\xi}\|_2=1\) and, by the translation bound \(\|\chi(\cdot-h)-\chi\|_2\le|h|\|\nabla\chi\|_2\),

\[
\big\|G_\alpha*F_{L,\xi}-e^{-|\xi|^2/(4\alpha p^2)}F_{L,\xi}\big\|_2
\le\frac{\|\nabla\chi\|_2}{L}
\int_{\mathbb C}|h|G_\alpha(h)\,dA(h)
=\frac{\sqrt\pi\,\|\nabla\chi\|_2}{2Lp\sqrt\alpha}.
\tag{9}
\]

For finite \(s\), fix \(\xi=(2p\sqrt s,0)\), so that every multiplier in (8) equals \(e^{-s/\alpha}\). For \(s=\infty\), instead take \(|\xi_L|\to\infty\), so that all these multipliers tend to zero. In either case take \(L_n\to\infty\), and **after choosing each individual** \(F_{L_n,\xi_n}\), use (7) to choose a sufficiently large \(R_n\) such that

\[
\max_j\|U_{R_n}^{-1}T_{\alpha_j}U_{R_n}F_{L_n,\xi_n}
-G_{\alpha_j}*F_{L_n,\xi_n}\|_2<1/n
\]

and the supports of \(U_{R_n}F_{L_n,\xi_n}\) leave every fixed compact set. The latter follows from \(\delta_{R_n}L_n=o(R_n)\) upon increasing \(R_n\). Then \(f_n:=U_{R_n}F_{L_n,\xi_n}\) is a unit, weakly null common approximate eigenvector sequence by (9). No uniform-in-frequency convergence in (7) is assumed: the choice of \(R_n\) occurs *after* fixing the frequency and envelope at each index.

**5. Essential bounds.** For every noncommutative monomial, replace each \(T_{\alpha_j}\) acting on the vectors just constructed by its corresponding scalar, one factor at a time. Boundedness of all \(T_{\alpha_j}\) gives

\[
\big\|[P(T_{\alpha_1},\ldots,T_{\alpha_d})
-P(e^{-s/\alpha_1},\ldots,e^{-s/\alpha_d})I]f_n\big\|_2\to0.
\]

If \(C\) is compact, then \(\|Cf_n\|_2\to0\) because \(f_n\rightharpoonup0\). Taking infima over compact perturbations and suprema over \(s\) proves (1). For (2), put \(t=e^{-s/\alpha}\). The scalar difference is \(|t-t^r|\), \(0\le t\le1\); differentiation gives its unique interior maximum at \(t=r^{-1/(r-1)}\), with value \(|r-1|r^{-r/(r-1)}\).

## Verification

The reproducible supplementary script `CHECK.py` evaluates the **exact** normalized Fock kernel using its Mittag–Leffler power series, checks polar moments by independent numerical quadrature, compares rescaled kernels at two large radii with the normalized Gaussian density, verifies its Fourier multiplier by integration, and tests (2)'s scalar maximization independently. The delivered version reports `CHECK_OK 67`. These finite checks validate critical normalizations and examples; they do not certify the uniform asymptotic, Hilbert-space convergence, or novelty. The infinite statements follow from steps 1–5 and the explicitly cited published kernel bounds.

To run: `python CHECK.py` with the numerical dependencies in `requirements.txt`.

## Relationship to prior work

Borichev, Fantolini, and Youssfi [1] prove boundedness and noncompactness of each \(T_\alpha\), compactness of \([T_\alpha,T_\beta]\), and infinite rank for distinct-parameter commutators. Their Section 3 provides the local kernel asymptotic and Gaussian intrinsic-distance bound required here, but their inspected Sections 1–6 do not assert common singular approximate eigenvectors, the multiplier curve (8), or the lower bound (2). Those are new deductions from the kernel asymptotics, not assumed literature results.

Tian [2] studies algebraic equalities among products of generalized Fock Berezin transforms, rather than their joint asymptotic spectral response modulo compact operators. The earlier commutativity characterization [3] likewise neither determines the curve in (1) nor entails the explicit essential-norm gap. Searches also considered aliases such as common Weyl sequences, Calkin-algebra spectral curves, limit operators, and semiclassical Fock heat multipliers. The inspected sources do not settle the claim by implication; an unknown general limit-operator theorem specialized to these weights remains a residual literature risk.

## Limitations

This is a lower-bound and approximate-point-spectrum result. It does **not** claim an exact essential norm for arbitrary polynomial combinations, equality in (2), a characterization of the entire joint essential spectrum, essential self-adjointness, parameter-uniform error bounds, or analogous results for \(m\le2\). Kernel localization and the boundedness of the original Berezin operators are imported from [1], not reproved as independent lemmas. No independent mathematical audit has been performed.

## References

[1] A. Borichev, G. Fantolini, and E.-H. Youssfi, *Berezin Transform Commutators*, arXiv:2610.33937v1, publicly submitted 2026-10-24. https://arxiv.org/html/2610.33937v1 (Sections 2–6, especially equations (2.1), (3.2)–(3.9), and Proposition 4.1).

[2] H. Tian, *Products of Berezin Transforms on Generalized Fock Spaces*, arXiv:2610.14599v1, publicly submitted 2026-10-10. https://arxiv.org/abs/2610.14599.

[3] A. Borichev, G. Fantolini, and E.-H. Youssfi, *On the Commutativity of the Berezin Transform*, arXiv:2510.07887v1, publicly submitted 2025-10-09. https://arxiv.org/abs/2510.07887.
