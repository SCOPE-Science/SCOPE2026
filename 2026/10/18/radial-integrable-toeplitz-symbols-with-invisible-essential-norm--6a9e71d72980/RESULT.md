# Radial integrable Toeplitz symbols with invisible essential norm

## Finding

For every \(\varepsilon>0\) there exists an explicitly specified **real radial** symbol \(f\in L^1(\mathbb D,dA)\), where \(dA\) is normalized area measure, such that
\[
\|f\|_{L^1}<\varepsilon,\qquad
0\le T_f,\qquad \|T_f\|\le \frac{128}{15},\qquad
\|T_f\|_{\mathrm{ess}}\ge1,
\]
while its Berezin transform satisfies
\[
\lim_{|z|\uparrow1}\widetilde{T_f}(z)=0.
\]
Here the initially defined Toeplitz sesquilinear form on holomorphic polynomials has a unique bounded extension to the standard Hilbert Bergman space \(A^2(\mathbb D)\); positivity refers to that **operator**, not to the signed symbol. Thus boundary vanishing of the Berezin transform does not characterize compactness even among positive Toeplitz operators induced by real radial globally integrable symbols. The small symbol norm is simultaneous with a fixed, positive essential norm.

The construction and all estimates are explicit. For every integer \(N\ge2\), put
\[
h_N(u)=4^Ne^{-u}\sum_{k=0}^{N-1}
(-1)^k\binom{N-1}{k}\frac{u^{N+k}}{(N+k)!}
\quad(u\ge0),
\qquad
\Phi_N(x)=\left(\frac{4x}{(1+x)^2}\right)^N\quad(x>0).
\]
For integers \(M\ge1\) and \(j\ge1\), let
\[
N_j=(j+1)^4,\qquad K_j=M16^j8^{N_j},\qquad
f(z)=\sum_{j=1}^{\infty} h_{N_j}\!\left(K_j\log\frac1{|z|^2}\right)
\quad (0<|z|<1).
\]
The series is interpreted as an \(L^1\)-limit and defines \(f\) up to area-null sets. Any integer \(M>1/(30\varepsilon)\) suffices. The value at \(z=0\) is immaterial.

## Assumptions and scope

Use the unweighted analytic Bergman Hilbert space \(A^2(\mathbb D,dA)\) and normalized area \(dA=\pi^{-1}dx\,dy\). The orthonormal basis is \(e_n(z)=\sqrt{n+1}\,z^n\) for integers \(n\ge0\). For a real radial integrable \(f\), the form
\[
\langle T_fp,q\rangle=\int_{\mathbb D}f(z)p(z)\overline{q(z)}\,dA(z)
\]
is initially defined for holomorphic polynomials \(p,q\). A bounded extension is asserted and established below, not assumed. The normalized reproducing kernel at \(w\in\mathbb D\) is
\[
k_w(z)=\frac{1-|w|^2}{(1-\overline wz)^2},\qquad
\widetilde{T_f}(w)=\langle T_fk_w,k_w\rangle.
\]
No assertion is made for nonradial general symbols, positive symbols, weighted Bergman spaces, or stronger localization criteria. The constructed real symbol may change sign; its associated operator is positive.

## Proof

**1. Laplace building block and controlled symbol mass.** Gamma integration and the binomial identity give, for \(x>0\),
\[
\begin{aligned}
\int_0^\infty h_N(u)e^{-xu}\,du
&=4^N\sum_{k=0}^{N-1}(-1)^k\binom{N-1}{k}(1+x)^{-N-k-1}\\
&=\frac{4^Nx^{N-1}}{(1+x)^{2N}}
=\frac{\Phi_N(x)}{x}.
\end{aligned}
\]
By the triangle inequality and exact gamma integrals,
\[
\int_0^\infty|h_N(u)|\,du
\le4^N\sum_{k=0}^{N-1}\binom{N-1}{k}
=\frac{8^N}{2}.
\]
For \(f_{N,K}(z)=h_N(K\log|z|^{-2})\), the substitutions \(t=|z|^2\) and \(u=K\log(1/t)\) yield
\[
\|f_{N,K}\|_{L^1(dA)}
=\frac1K\int_0^\infty|h_N(u)|e^{-u/K}\,du
\le\frac{8^N}{2K}.
\]
Consequently the defining sum for \(f\) converges absolutely in \(L^1\) and
\[
\|f\|_{L^1}\le\sum_{j\ge1}\frac{8^{N_j}}{2K_j}
=\frac1{2M}\sum_{j\ge1}16^{-j}
=\frac1{30M}<\varepsilon.
\]

**2. Exact nonnegative Toeplitz eigenvalues and uniform boundedness.** Angular integration makes the polynomial form diagonal. For every integer \(n\ge0\),
\[
\begin{aligned}
\langle T_{f_{N,K}}e_n,e_n\rangle
&=(n+1)\int_0^1h_N(K\log(1/t))t^n\,dt\\
&=\frac{n+1}{K}\int_0^\infty h_N(u)e^{-(n+1)u/K}\,du
=\Phi_N\!\left(\frac{n+1}{K}\right).
\end{aligned}
\]
Absolute \(L^1\)-convergence allows termwise polynomial pairings, so the full diagonal is
\[
\lambda_n=\sum_{j\ge1}\Phi_{N_j}\!\left(\frac{n+1}{K_j}\right),\qquad \lambda_n\ge0.
\]
Since \(0<4x/(1+x)^2\le1\) and \(N\ge1\),
\[
0\le\Phi_N(x)\le\min\{1,4x,4/x\}.
\]
Successive scales satisfy \(K_{j+1}/K_j\ge16\). For any \(m=n+1\ge1\), splitting the sum according to \(K_j\le m\) and \(K_j>m\) gives
\[
\sum_{K_j\le m}\Phi_{N_j}(m/K_j)
\le\frac4m\sum_{K_j\le m}K_j\le\frac{64}{15},
\]
\[
\sum_{K_j>m}\Phi_{N_j}(m/K_j)
\le4m\sum_{K_j>m}K_j^{-1}\le\frac{64}{15}.
\]
It follows that \(0\le\lambda_n\le128/15\) for all \(n\). Hence the polynomial form extends uniquely to a bounded positive diagonal operator with norm at most \(128/15\). At each integer \(n_j=K_j-1\),
\[
\lambda_{n_j}\ge\Phi_{N_j}(1)=1.
\]
Because \(n_j\to\infty\), the operator is not compact, and the diagonal essential-norm formula gives \(\|T_f\|_{\mathrm{ess}}=\limsup_{n\to\infty}\lambda_n\ge1\).

**3. A summable global bound for the Berezin transforms of individual building blocks.** Put \(s=|w|^2\). From the normalized reproducing-kernel expansion,
\[
B_{N,K}(s):=\widetilde{T_{f_{N,K}}}(w)
=(1-s)^2\sum_{m\ge1}m\,\Phi_N(m/K)s^{m-1}.
\]
For all \(m\ge1\) and \(0\le s<1\), differentiation (or direct maximization) yields
\[
m(1-s)^2s^{m-1}\le\frac4m,
\]
where at \(s=0,m=1\) the value is interpreted continuously. Thus
\[
0\le B_{N,K}(s)\le4\sum_{m\ge1}\frac{\Phi_N(m/K)}m.
\]
Set \(g_N(x)=\Phi_N(x)/x\). This positive function is increasing up to \((N-1)/(N+1)\), decreasing thereafter, and
\[
\sup_{x>0}g_N(x)\le\frac{N+1}{N-1}\le3\qquad(N\ge2).
\]
The right-endpoint mesh sum of any nonnegative unimodal integrable function is bounded by its integral plus one mesh width times its maximum (split at the mode). Applying this elementary comparison with mesh \(1/K\) gives
\[
\sum_{m\ge1}\frac{\Phi_N(m/K)}m
=\frac1K\sum_{m\ge1}g_N(m/K)
\le\int_0^\infty g_N(x)\,dx+\frac3K.
\]
The beta integral equals
\[
I_N:=\int_0^\infty g_N(x)\,dx
=4^N\mathrm{B}(N,N)
=\frac{4^N((N-1)!)^2}{(2N-1)!}.
\]
Since \(I_1=4\) and \(I_{N+1}/I_N=2N/(2N+1)\le\sqrt{N/(N+1)}\), induction gives \(I_N\le4/\sqrt N\). We conclude the uniform estimate
\[
\boxed{\ \sup_{0\le s<1}B_{N,K}(s)\le\frac{16}{\sqrt N}+\frac{12}{K}.\ }
\]

**4. Vanishing of the full Berezin transform.** For fixed integers \(N,K\), the diagonal sequence \(\Phi_N((n+1)/K)\to0\) as \(n\to\infty\); hence \(T_{f_{N,K}}\) is compact. Its Berezin transform \(B_{N,K}(s)\to0\) as \(s\uparrow1\), since the normalized kernels converge weakly to zero. The previous estimate and \(\sqrt{N_j}=(j+1)^2\) imply
\[
\sum_{j\ge1}\sup_{0\le s<1}B_{N_j,K_j}(s)
\le16\sum_{j\ge1}(j+1)^{-2}+12\sum_{j\ge1}K_j^{-1}<\infty.
\]
Therefore dominated convergence for series gives
\[
\sum_{j\ge1}B_{N_j,K_j}(s)\longrightarrow0
\quad\text{as }s\uparrow1.
\]
Because \(f=\sum_j f_{N_j,K_j}\) in \(L^1\), and \(|k_w|^2\) is bounded on the disk for each fixed \(w\), one may integrate the sum termwise. Thus \(\widetilde{T_f}(w)=\sum_j B_{N_j,K_j}(|w|^2)\), proving the claimed boundary vanishing. The finite building-block Toeplitz operators are compact, but **their series is not asserted to converge in operator norm**; the strong/form limit can be noncompact.

## Verification

The accompanying standalone `check_formulas.py` executes 333 exact rational assertions. They check the finite binomial/Laplace identity, the beta-integral estimate, the peak normalization, positivity bounds, and finite partial Berezin sums across multiple indices and rational radii. Run it with `python3 check_formulas.py` from the directory containing this document. The infinite summations, operator extension, compactness claims, and limit statements are established by the analytic argument above rather than inferred from the finite checks. The displayed sum of \(L^1\) norms, the scale ratio, and the analytic constant estimates can also be reproduced directly from the definitions.

## Relationship to prior work

Looi (2026, arXiv:2608.09131, first posted August 10) constructs \(L^1\)-symbol Toeplitz operators with boundary-vanishing Berezin transforms that are noncompact, including a real-symbol positive-operator example on the disk. This **general noncompactness phenomenon and positivity are prior work**, not claimed as new here. Looi explicitly states in the introduction that the block arrangements in that work are nonradial and that the radial \(L^1\) problem is not addressed. The present contribution is an explicit **radial** \(L^1\) symbol, diagonal positive operator, and arbitrary small symbol-norm realization, based on an exact inverse-Laplace construction rather than transported nonradial blocks.

Zorboska (2002) studies radial operators and proves a compactness/Berezin equivalence for radial integrable Toeplitz symbols under an additional oscillation condition, while noting the unrestricted unbounded radial case as unresolved. Korenblum and Zhu (1995) prove radial compactness characterization under bounded-symbol hypotheses; our symbol lies outside that regime. Suárez (2007) concerns norm limits of Toeplitz operators with bounded symbols. Li and Wang (2026, arXiv:2608.23733) treat bounded symbols on radial-weight spaces, not arbitrary signed radial \(L^1\) symbols. An earlier broad 2007 preprint by Agbor contains a claimed compactness criterion for \(L^1\) symbols that is incompatible with the later counterexamples; it does not supply an explicit radial construction or a logically valid implication covering the present negative example.

## Limitations

This is a specific constructive counterexample in the unweighted one-variable Bergman space. It neither classifies all radial \(L^1\) symbols with vanishing Berezin transform nor establishes sharp estimates for the essential norm. The symbol is real and radial but not required to be nonnegative; positivity pertains to its Toeplitz operator. The formula is a convergent \(L^1\) series, not a pointwise-uniform or operator-norm convergent series. Literature-priority uncertainty remains for equivalently phrased radial-moment counterexamples, despite the inspected nearest sources. The result has not undergone independent mathematical audit.

## References

1. S. Looi, *When the Berezin transform fails to detect compactness: Toeplitz operators with \(L^1\) symbols on weighted Bergman spaces*, arXiv:2608.09131 (first posted 2026-08-10), https://arxiv.org/abs/2608.09131.
2. N. Zorboska, *The Berezin transform and radial operators*, Proceedings of the American Mathematical Society 131 (2003), 793–800, DOI:10.1090/S0002-9939-02-06691-1, https://doi.org/10.1090/S0002-9939-02-06691-1.
3. B. Korenblum and K. Zhu, *An application of Tauberian theorems to Toeplitz operators*, Journal of Operator Theory 33 (1995), 353–361, https://jot.theta.ro/jot/archive/1995-033-002/1995-033-002-010.html.
4. D. Suárez, *The eigenvalues of limits of radial Toeplitz operators*, arXiv:0710.0797 (2007), https://arxiv.org/abs/0710.0797.
5. Y. Li and Z. Wang, *Compact Toeplitz operators on radial weighted Bergman spaces*, arXiv:2608.23733 (first posted 2026-08-24), https://arxiv.org/abs/2608.23733.
6. A. Agbor, *Boundedness and Compactness of Toeplitz operators with \(L^1\) symbols on the Bergman space*, arXiv:0708.2611 (2007), https://arxiv.org/abs/0708.2611.
7. Z.-H. Zhou, W.-L. Chen, and X.-T. Dong, *The Berezin transform and radial operators on the Bergman space of the unit ball*, Complex Analysis and Operator Theory 7 (2013), 313–329, DOI:10.1007/s11785-011-0145-2, https://doi.org/10.1007/s11785-011-0145-2.
8. S. Looi, *The Berezin liminf criterion fails for radial Toeplitz operators*, arXiv:2603.10879 (first posted 2026-03-11), https://arxiv.org/abs/2603.10879.
