# Fractional finite-size defect in sharp cyclic Sobolev interpolation

## Finding
For each integer \(N\ge3\), let \(C_N\) be the smallest constant for which every complex-valued or real-valued mean-zero function on the \(N\)-cycle satisfies
\[
\max_{j\in\mathbb Z/N\mathbb Z}|u_j|^2\le C_N
\left(\sum_{j=0}^{N-1}|u_j|^2\right)^{1/2}
\left(\sum_{j=0}^{N-1}|u_{j+1}-u_j|^2\right)^{1/2}.
\]
Then \(0<C_N<1\), and the exact sharp constant is
\[
 C_N=\max_{t>0}\frac{2\sqrt t}{N}
 \sum_{k=1}^{N-1}\frac{1}{t+4\sin^2(\pi k/N)}.
\]
Every maximizer of the inequality is a nonzero scalar multiple of a translation of a mean-zero cyclic resolvent column corresponding to a maximizing \(t\). For all sufficiently large \(N\), this maximizing parameter \(t_N\) is unique, and
\[
 t_N=4N^{-2/3}+4N^{-4/3}+O(N^{-2}),
\]
\[
 \boxed{C_N=1-\frac32N^{-2/3}+\frac38N^{-4/3}+\frac1{16}N^{-2}+O(N^{-8/3}).}
\]
In particular, the strict finite-periodic loss relative to the infinite-lattice sharp constant has leading order \(\frac32N^{-2/3}\), rather than an integral-power finite-size correction.

## Assumptions and scope
The vertex set is \(\mathbb Z/N\mathbb Z\), with the periodic convention \(u_N=u_0\), and \(\sum_j u_j=0\). Both norms are *unnormalized* counting-measure norms. The energy is the nearest-neighbor Dirichlet form \(E(u)=\sum_j|u_{j+1}-u_j|^2\); no edge rescaling is used. The inequality applies to all real or complex functions under these assumptions, for every integer \(N\ge3\). Big-O statements refer to integer \(N\to\infty\).

Write \(L=2I-S-S^{-1}\) for the cycle Laplacian, \(P=I-N^{-1}\mathbf1\mathbf1^*\) for the orthogonal projection onto mean-zero vectors, and \(G_t=(L+tI)^{-1}P\) for \(t>0\). All scalar multiples and cyclic translates of \(G_{t_N}e_0\) are equality cases for sufficiently large \(N\); for arbitrary \(N\), take the union of these families over every maximizing \(t\).

## Proof
**1. Exact sharpness and equality.** The nonconstant Fourier eigenvalues of \(L\) are \(\lambda_k=4\sin^2(\pi k/N)\) for \(1\le k\le N-1\). The diagonal resolvent value, independent of vertex, is
\[
 g_N(t):=\langle e_0,G_te_0\rangle
 =\frac1N\sum_{k=1}^{N-1}(\lambda_k+t)^{-1}.
\]
On the mean-zero subspace, Cauchy--Schwarz in the positive operator \(L+tI\) gives
\[
 |u_j|^2\le g_N(t)\big(E(u)+t\|u\|_2^2\big),
\]
with equality exactly when \(u\) is a scalar multiple of \(G_te_j\). Given \(u\ne0\), substitute \(t=E(u)/\|u\|_2^2>0\). This yields
\[
 \frac{\|u\|_\infty^2}{\|u\|_2\sqrt{E(u)}}
 \le 2\sqrt t\,g_N(t)\le\max_{s>0}2\sqrt s\,g_N(s).
\]
The function \(H_N(t)=2\sqrt t\,g_N(t)\) is continuous, positive, and tends to zero at \(t\downarrow0\) and \(t\uparrow\infty\), hence has an interior maximum. At any maximum \(t_*\), differentiation gives \(g_N(t_*)+2t_*g_N'(t_*)=0\). For \(u=G_{t_*}e_j\), spectral calculus yields
\[
 \|u\|_2^2=-g_N'(t_*),\qquad
 E(u)=g_N(t_*)+t_*g_N'(t_*)=t_*\|u\|_2^2.
\]
Thus the initial Cauchy--Schwarz inequality and the substitution are simultaneously equalities, proving the sharp formula and the complete equality classification.

**2. Closed cyclic Green function and strict loss.** Define \(y=\operatorname{arsinh}(\sqrt t/2)>0\). The infinite-line resolvent kernel at separation \(m\) is \(\exp(-2y|m|)/\sqrt{t(t+4)}\). Periodizing it around the cycle and subtracting the constant Fourier mode gives the exact identity
\[
 g_N(t)=\frac{\coth(Ny)}{\sqrt{t(t+4)}}-\frac1{Nt},
\qquad
 H_N(t)=\operatorname{sech}(y)\coth(Ny)-\frac1{N\sinh y}.
\]
Since \(\coth x<1+1/x\) for \(x>0\), and \(\tanh y\le y\),
\[
 H_N(t)<\operatorname{sech}(y)+\frac{\operatorname{sech}(y)}{Ny}-\frac1{N\sinh y}
 \le\operatorname{sech}(y)<1.
\]
Consequently \(C_N<1\) for every finite \(N\).

**3. Localization of the maximizing spectral parameter.** Set \(\varepsilon=N^{-2/3}\). The Green identity becomes
\[
 H_N(t)=(1+t/4)^{-1/2}-\frac2{N\sqrt t}+R_N(t),
 \quad R_N(t)=\frac{2(1+t/4)^{-1/2}}{e^{2Ny}-1}.
\]
Choosing \(t=4\varepsilon\) shows \(C_N\ge1-\frac32\varepsilon+O(\varepsilon^2)\), so \(C_N\to1\). Let \(t_N\) be any global maximizing parameter. The preceding strict upper bound \(H_N(t)\le(1+t/4)^{-1/2}\) then implies \(t_N=O(\varepsilon)\).

Next \(Ny(t_N)\to\infty\). Otherwise take a subsequence with \(Ny\to x\in[0,\infty)\). In the closed formula \(H_N\) tends to \(\coth x-1/x<1\) if \(x>0\), and to zero if \(x=0\), contradicting \(C_N\to1\). Therefore the remainder obeys \(R_N(t_N)=o(1/(N\sqrt{t_N}))\). From the displayed identity and \(C_N\ge1-2\varepsilon\) for large \(N\), one obtains \(2\varepsilon\ge1-C_N\ge(2-o(1))/(N\sqrt{t_N})\). Hence \(t_N\ge c\varepsilon\) for some absolute \(c>0\). Together, all maximizing \(s_N=t_N/\varepsilon\) lie in one fixed compact interval of \((0,\infty)\), once \(N\) is large.

**4. The fractional-power expansion.** Uniformly with all derivatives in \(s\) on compact subintervals of \((0,\infty)\), the exponential remainder is smaller than every power of \(\varepsilon\), and Taylor expansion at \(t=s\varepsilon\) gives
\[
 H_N(s\varepsilon)=1-\varepsilon F(s)+\varepsilon^2J(s)+\varepsilon^3K(s)+O(\varepsilon^4),
\]
\[
 F(s)=\frac s8+\frac2{\sqrt s},\qquad
 J(s)=\frac{3s^2}{128},\qquad K(s)=-\frac{5s^3}{1024}.
\]
The strictly convex function \(F\) has unique minimum at \(s=4\), with \(F(4)=3/2\), \(F''(4)=3/64\). Localization implies \(s_N\to4\). On the compact interval containing every maximizer, \(\partial_s^2H_N=-\varepsilon F''(s)+O(\varepsilon^2)<0\) for sufficiently large \(N\). Thus the maximizing parameter is eventually unique. Dividing its stationarity equation by \(\varepsilon\) and applying the implicit-function theorem around \((s,\varepsilon)=(4,0)\) gives
\[
 s_N=4+\frac{J'(4)}{F''(4)}\varepsilon+O(\varepsilon^2)
 =4+4\varepsilon+O(\varepsilon^2).
\]
Inserting this into the expansion, and using \(J(4)=3/8\), \(K(4)=-5/16\), yields the third coefficient
\[
 K(4)+4J'(4)-8F''(4)=-\frac5{16}+\frac34-\frac38=\frac1{16}.
\]
This proves the claimed three-term asymptotic and parameter expansion.

## Verification
The attached standard-library Python script `verify_cycle_sobolev.py` numerically compares the Fourier resolvent sum with its hyperbolic closed form, reconstructs the exact cyclic Green extremizer in physical coordinates, and checks its norm quotient and energy-to-norm ratio. All scripted comparisons pass for \(N=3,4,5,6,7,9,12,20,30,50,80\). It checks the asymptotic expression and optimizing parameter through \(N=100000\). The analytical proof above, not these finite experiments, supplies the all-\(N\) and asymptotic assertions.

## Relationship to prior work
Nagai, Kametaka, Yamagishi, Takemura and Watanabe (2008) explicitly identify the best homogeneous Dirichlet-energy constant \((N^2-1)/(12N)\) on the same mean-zero cyclic space, rather than the present sharp *multiplicative* constant. Yamagishi et al. (2012) compute additive-energy resolvent constants with a mass parameter, the appropriate starting point for the sharp interpolation problem, but the mixed-norm optimization and its fractional finite-size asymptotic are not presented in the examined results. Ilyin, Laptev and Zelik (2014) establish the infinite-lattice sharp multiplicative constant \(1\) and develop Green-function optimization for discrete Sobolev interpolation on \(\mathbb Z\); they do not state the finite mean-zero cycle's \(N^{-2/3}\) deficit. These methods are related, and the exact resolvent representation can be obtained from earlier general theory; the specific claimed contribution is the sharp three-term finite-size defect, parameter scaling and equality analysis.

## Limitations
The theorem concerns only nearest-neighbor cycles with unnormalized energy and mean-zero data; no weighted, higher-dimensional, or nonperiodic extension is asserted. Uniqueness of the maximizing parameter is shown for all sufficiently large \(N\), not asserted for every \(N\ge3\). The complete formula nevertheless covers small cycles. The 2009 article by Nagai, Kametaka and Watanabe on discrete Sobolev constants was identified but was unavailable in full text; whether it contains an equivalent higher-order finite-size expansion remains an unresolved literature risk.

## References
1. A. Nagai, Y. Kametaka, H. Yamagishi, K. Takemura, K. Watanabe, *Discrete Bernoulli Polynomials and the Best Constant of the Discrete Sobolev Inequality*, Funkcialaj Ekvacioj 51 (2008), 307–327, DOI: 10.1619/fesi.51.307 (publicly available 2008-08-01), https://www.jstage.jst.go.jp/article/fesi/51/2/51_2_307/_pdf.
2. H. Yamagishi, A. Nagai, K. Watanabe, K. Takemura, Y. Kametaka, *The Best Constant of Discrete Sobolev Inequality Corresponding to a Bending Problem of a String*, Kumamoto Journal of Mathematics 25 (2012), 1–15, https://www.sci.kumamoto-u.ac.jp/~kjm/BKI/kjmpdf/KJM-25/v25-1-yamagishi.pdf.
3. A. Ilyin, A. Laptev, S. Zelik, *Sharp interpolation inequalities for discrete operators and applications*, arXiv:1407.0675v1 (2014-07-02), https://arxiv.org/abs/1407.0675; Bull. Math. Sci. 5 (2015), 19–57, DOI: 10.1007/s13373-014-0060-8.
4. A. Nagai, Y. Kametaka, K. Watanabe, *The best constant of discrete Sobolev inequality*, J. Phys. A 42 (2009), 454014, DOI: 10.1088/1751-8113/42/45/454014 (abstract inspected; full text unavailable).
