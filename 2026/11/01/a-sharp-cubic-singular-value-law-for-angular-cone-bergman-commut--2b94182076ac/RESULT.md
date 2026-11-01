# A sharp cubic singular-value law for angular-cone Bergman commutators

## Finding

For a weighted analytic Bergman space on the unit ball of \(\mathbb C^2\), an angular-cone Toeplitz operator has a compact commutator with coordinate multiplication whose complete singular spectrum is explicit. More precisely, for every fixed \(\alpha>-1\) and \(0<t<1\), the singular-value count of the commutator \(C_{\alpha,t}=[T_t,M_{z_1}]\) obeys
\[
\lim_{\varepsilon\downarrow0}\varepsilon^3\#\{j:s_j(C_{\alpha,t})>\varepsilon\}
=\mathcal C(t):=\frac{\sqrt t(1-t)^2}{3\pi\sqrt3}.
\]
Thus \(s_j(C_{\alpha,t})\sim (\mathcal C(t)/j)^{1/3}\), and \(C_{\alpha,t}\) belongs to the Schatten class \(S_p\) exactly when \(p>3\). The coefficient is independent of the Bergman weight \(\alpha\) and is uniquely maximized over the opening parameter at \(t=1/5\). The critical rearranged spectral power sum satisfies \(\sum_{j=1}^J s_j(C_{\alpha,t})^3\sim\mathcal C(t)\log J\).

## Assumptions and scope

Let \(\mathbb B^2=\{z\in\mathbb C^2:|z_1|^2+|z_2|^2<1\}\). Equip \(A^2_\alpha(\mathbb B^2)\), \(\alpha>-1\), with the probability-normalized measure
\[
d\mu_\alpha(z)=\frac{\Gamma(\alpha+3)}{\pi^2\Gamma(\alpha+1)}(1-|z|^2)^\alpha\,dV(z).
\]
Let \(P_\alpha\) denote its orthogonal Bergman projection. For fixed \(t\in(0,1)\), set
\[
\Omega_t=\left\{z\in\mathbb B^2:|z_1|^2>t(|z_1|^2+|z_2|^2)\right\},
\quad T_t=P_\alpha\mathbf1_{\Omega_t}|_{A^2_\alpha}.
\]
Coordinate multiplication \(M_{z_1}f=z_1f\) is bounded on this space. The commutator convention is \(C_{\alpha,t}=T_tM_{z_1}-M_{z_1}T_t\). For any compact operator, \(s_j\) denotes its positive singular values in nonincreasing order with multiplicity, and \(\#\{j:s_j>\varepsilon\}\) is the strict counting function. All limits hold with \(t\) and \(\alpha\) fixed; no uniform statement at \(t=0\) or \(t=1\) is asserted.

## Proof

**1. Exact diagonalization.** For \(k,\ell\ge0\), put \(n=k+\ell\) and define the normalized monomial
\[
e_{k,\ell}(z)=\sqrt{\frac{\Gamma(n+\alpha+3)}{\Gamma(\alpha+3)k!\ell!}}\,z_1^kz_2^\ell.
\]
These vectors form an orthonormal basis. The radial Dirichlet integral separates the total radius from the angular variable \(u=|z_1|^2/(|z_1|^2+|z_2|^2)\); relative to the squared monomial weight, \(u\) has the beta distribution with parameters \((k+1,\ell+1)\). The angular-invariant Toeplitz operator is therefore diagonal:
\[
T_te_{k,\ell}=\lambda_{k,\ell}(t)e_{k,\ell},\quad
\lambda_{k,\ell}(t)=\frac{(n+1)!}{k!\ell!}\int_t^1u^k(1-u)^\ell\,du
=\Pr\{\operatorname{Bin}(n+1,t)\le k\}.
\]
The beta-binomial identity in the last equality follows by differentiating both sides in \(t\) and checking their common value at \(t=1\). Also
\[
M_{z_1}e_{k,\ell}=\sqrt{\frac{k+1}{n+\alpha+3}}\,e_{k+1,\ell}.
\]
Writing \(m=k+1\), the binomial recurrence gives
\[
\lambda_{k+1,\ell}-\lambda_{k,\ell}
=(1-t)\binom{n+1}{m}t^m(1-t)^{n+1-m}.
\]
Consequently
\[
C_{\alpha,t}e_{k,\ell}=c_{n,m}e_{k+1,\ell},\quad
c_{n,m}=\sqrt{\frac{m}{n+\alpha+3}}(1-t)\binom{n+1}{m}t^m(1-t)^{n+1-m},
\quad 1\le m\le n+1.
\]
These images are pairwise orthogonal. Thus the complete singular-value multiset is exactly \(\{c_{n,m}:n\ge0,1\le m\le n+1\}\), with multiplicity; all listed values are positive.

**2. Local Gaussian profile and global bounds.** Put \(\sigma^2=t(1-t)\) and \(A_t=\sqrt{1-t}/\sqrt{2\pi}\). The fixed-parameter binomial local central limit theorem, obtained by uniform Stirling expansion, implies that for every \(R>0\), uniformly on \(|u_{n,m}|\le R\), where \(u_{n,m}=(m-(n+1)t)/\sqrt n\),
\[
\sqrt n\,c_{n,m}=A_t\exp\left(-\frac{u_{n,m}^2}{2\sigma^2}\right)+o(1).
\]
For every fixed \(t\in(0,1)\), the binomial point masses \(p_{N,m}\) satisfy the explicit interior second-difference identity \[\Delta^2\log p_{N,m}=\log\frac{m(N-m)}{(m+1)(N-m+1)}\le-\frac4{N+2}.\] Its mode lies within one integer of \(Nt\), and Stirling gives \(p_{N,\mathrm{mode}}=O_t(N^{-1/2})\). Summing these negative second differences on either side of the mode produces Gaussian tail control. Hence there exist constants \(B_t,b_t>0\) such that
\[
0<c_{n,m}\le B_tn^{-1/2}\exp(-b_tu_{n,m}^2),\qquad n\ge1.
\]
The factor \(\sqrt{m/(n+\alpha+3)}\) is at most one for \(\alpha>-1\); the constants may be chosen independently of \(\alpha\). In particular, \(\sup_m c_{n,m}=O_t(n^{-1/2})\), proving compactness by the exact orthogonal-shift representation. The same local limit and dominating Gaussian yield, for every fixed \(p>0\),
\[
\sum_{m=1}^{n+1}c_{n,m}^{p}\sim
A_t^p\sqrt{\frac{2\pi\sigma^2}{p}}\ n^{(1-p)/2}.
\]
Summing in \(n\) proves \(\sum_{n,m}c_{n,m}^p<\infty\) precisely for \(p>3\). At \(p=3\), the sum over degrees \(n\le N\) equals \(\frac32\mathcal C(t)\log N+o(\log N)\).

**3. Counting-law constant.** Let \(N(\varepsilon)=\#\{(n,m):c_{n,m}>\varepsilon\}\). On degree ranges \(\delta\varepsilon^{-2}\le n\le R\varepsilon^{-2}\), with \(0<\delta<R<\infty\), introduce \(r=\varepsilon^2n\) and \(u=u_{n,m}\). By the local limit, the limiting inequality is
\[
A_t e^{-u^2/(2\sigma^2)}>\sqrt r.
\]
The lattice-cell density in \((r,u)\) is \(\varepsilon^{-3}\sqrt r\,dr\,du\). The Gaussian bound makes the relevant \(u\)-range uniformly bounded on compact positive \(r\)-intervals, so ordinary Riemann summation applies outside the null boundary of the inequality. For the omitted small degrees, using \(\sum_m c_{n,m}^2=O_t(n^{-1/2})\) gives
\[
\varepsilon^3\sum_{n<\delta\varepsilon^{-2}}\#\{m:c_{n,m}>\varepsilon\}
\le O_t(\sqrt\delta)+o(1).
\]
For the omitted large degrees, \(\sup_m c_{n,m}\le B_t/\sqrt n\) makes the count zero once \(n>R\varepsilon^{-2}\) and \(R>B_t^2\). Hence sending \(\delta\downarrow0\) and \(R\uparrow\infty\) gives
\[
\begin{aligned}
\lim_{\varepsilon\downarrow0}\varepsilon^3N(\varepsilon)
&=\int_{\mathbb R}\int_0^{A_t^2e^{-u^2/\sigma^2}}\sqrt r\,dr\,du\\
&=\frac23A_t^3\int_{\mathbb R}e^{-3u^2/(2\sigma^2)}\,du
=\frac{\sqrt t(1-t)^2}{3\pi\sqrt3}.
\end{aligned}
\]
Monotone inversion of this counting asymptotic gives the stated singular-value equivalent, and consequently \(\sum_{j\le J}s_j^3\sim\mathcal C(t)\log J\). Finally, the logarithmic derivative of \(\sqrt t(1-t)^2\) is \((1-5t)/(2t(1-t))\), proving the unique global maximum at \(t=1/5\). Every step uses the actual weight-dependent finite-degree formula; independence of \(\alpha\) is a limit conclusion rather than an assumption.

## Verification

A standalone standard-library script, `verify_spectrum.py`, independently checks the exact beta-binomial integral, eigenvalue recurrence and normalized monomial-shift factor for small integer weights and several rational apertures. It also evaluates finite local central-limit moments and truncated counting functions for three values of \(t\). The script executed with 1,640 successful finite assertions. Those finite checks are supplementary; the analytical proof above, not numerical extrapolation, establishes the count for all degrees and all permitted fixed parameters.

## Relationship to prior work

Quiroga-Barranco and Sánchez-Nungaray (2020) supply weighted-ball torus-invariant Toeplitz spectral integral representations. Quiroga-Barranco (2021) provides general unit-ball monomial formulas for torus-invariant and quasi-homogeneous Toeplitz operators. García and Vasilevski (2015) give an earlier two-dimensional weighted-ball operator-algebra treatment. These are prior input for the diagonal representation, not evidence of novelty of that representation. Engliš, Guo and Zhang (2007) obtain commutator weak-ideal and Dixmier-trace laws for smooth boundary symbols, whereas the present characteristic symbol has a jump along a codimension-one angular interface. The claim here is limited to the exact singular sequence and sharp \(\varepsilon^{-3}\) Weyl law with its aperture-optimizing constant. A previously published general jump-symbol theorem implying this coefficient is a remaining priority risk.

## Limitations

The geometric parameter \(t\) is fixed strictly between zero and one, and \(\alpha>-1\) is fixed; no endpoint-uniform limit is proved. The theorem concerns the two-complex-dimensional unit ball and the specific coordinate commutator with a conical characteristic symbol. It does not claim a general discontinuous-symbol commutator law. Explicit finite experiments do not independently certify infinite statements, and no independent mathematical review is represented.

## References

1. R. Quiroga-Barranco and A. Sánchez-Nungaray, *Moment maps of Abelian groups and commuting Toeplitz operators acting on the unit ball* (2020), arXiv:2009.12448, https://arxiv.org/abs/2009.12448.
2. R. Quiroga-Barranco, *Toeplitz operators, \(\mathbb T^m\)-invariance and quasi-homogeneous symbols* (first posted 2021-06-03), arXiv:2106.01980, https://arxiv.org/abs/2106.01980.
3. A. García and N. Vasilevski, *Toeplitz Operators on the Weighted Bergman Space over the Two-Dimensional Unit Ball* (2015), https://doi.org/10.1155/2015/306168.
4. M. Engliš, K. Guo and G. Zhang, *Toeplitz and Hankel operators and Dixmier traces on the unit ball of \(\mathbb C^n\)* (2007), arXiv:0707.2025, https://arxiv.org/abs/0707.2025.
5. J. Isralowitz, *Schatten \(p\) class commutators on weighted Bergman spaces* (2011), arXiv:1109.0864, https://arxiv.org/abs/1109.0864.
