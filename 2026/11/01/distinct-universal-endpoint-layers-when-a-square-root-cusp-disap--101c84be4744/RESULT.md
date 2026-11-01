# Distinct universal endpoint layers when a square-root cusp disappears

## Finding

For the full-branch expanding interval maps
\[
f_\theta(\tfrac12\pm t)=1-\theta t-2K_\theta\sqrt t,\qquad
K_\theta=\frac{1-\theta/2}{\sqrt2},\qquad 1<\theta<2,
\]
let \(h_\theta\) be the unique normalized absolutely continuous invariant density, known to belong to \(W^{2,1}(0,1)\). Put \(\varepsilon=2-\theta\). As \(\varepsilon\downarrow0\), the maps converge uniformly to the full tent map and \(h_\theta\to1\) in \(L^1(0,1)\), indeed uniformly on compact subsets of \((0,1)\). Nevertheless the invariant densities have two **different** universal endpoint profiles on the common quadratic scale:
\[
\begin{aligned}
h_{2-\varepsilon}(1-\varepsilon^2 z)&\longrightarrow R(z):=1-\frac{1}{\sqrt{1+16z}},\\
h_{2-\varepsilon}(\varepsilon^2 z)&\longrightarrow L(z):=\sum_{j=1}^{\infty}2^{-j}\left(1-\frac{1}{\sqrt{1+16z/2^j}}\right).
\end{aligned}
\]
Both convergences are uniform for \(z\) in any compact subinterval of \([0,\infty)\). Moreover, \(0<L(z)<R(z)<1\) for every \(z>0\), despite the symmetry of the maps: the left endpoint inherits a diluted copy of the right endpoint layer along its inverse-branch return. The left profile is the unique bounded solution of \(L(z)=\frac12[L(z/2)+R(z/2)]\) with \(L(0)=0\). In particular, \(R'(0)=8\) and \(L'(0)=8/3\).

The following fixed-parameter endpoint identities (also available in related mixture analysis) are used as inputs to the new limiting law:
\[
h_\theta'(1)=-\frac{h_\theta(1/2)}{K_\theta^2},\qquad
h_\theta'(0)=\frac{h_\theta(1/2)}{K_\theta^2[(1+\theta/2)^2-1]}.
\]
Consequently,
\[
\varepsilon^2h_{2-\varepsilon}'(1)\to-8,\qquad
\varepsilon^2h_{2-\varepsilon}'(0)\to\frac83,\qquad
\liminf_{\varepsilon\downarrow0}\varepsilon^2\|h_{2-\varepsilon}''\|_{L^1}\ge\frac{32}{3}.
\]
Thus \(L^1\) stability of invariant densities coexists with an order-\(\varepsilon^{-2}\) second-derivative obstruction. In fact \(h_\theta\not\to1\) in \(W^{1,1}\), since \(h_\theta(0)=h_\theta(1)=0\) while the limiting density has trace \(1\) at both endpoints.

## Assumptions and scope

The parameter varies through the real interval \(1<\theta<2\); only the deterministic map above, with Lebesgue reference measure and invariant *probability* normalization, is considered. The established \(W^{2,1}\) existence and uniqueness theorem for each fixed parameter is used as an input [1]. The parameter endpoint \(\theta=2\) is excluded from the cusp regularity assertion: its limiting tent map has invariant density \(1\). All endpoint values and first derivatives refer to continuous Sobolev traces. The profile variables \(z\) are nonnegative, fixed or ranging over a fixed compact set as \(\varepsilon\downarrow0\).

## Proof

**1. Inverse branches and fixed-point identities.** Write
\[
u_\theta(x)=\frac{\sqrt{K_\theta^2+\theta(1-x)}-K_\theta}{\theta},\quad
g_0(x)=\tfrac12-u_\theta(x)^2,\quad g_1(x)=\tfrac12+u_\theta(x)^2.
\]
The two inverse branches cover the two monotonicity intervals. Their common inverse-Jacobian weight is
\[
w_\theta(x)=\frac1\theta\left(1-\frac{K_\theta}{\sqrt{K_\theta^2+\theta(1-x)}}\right)
=\frac{u_\theta(x)}{K_\theta+\theta u_\theta(x)}.
\]
Writing \(\Lambda_\theta=1+\theta/2\), we have \(0\le w_\theta\le\Lambda_\theta^{-1}\), \(w_\theta(0)=\Lambda_\theta^{-1}\), \(w_\theta(1)=0\), and \(w_\theta'(1)=-1/(2K_\theta^2)\). Hence the invariant density obeys
\[
h_\theta(x)=w_\theta(x)[h_\theta(g_0(x))+h_\theta(g_1(x))].\tag{1}
\]
The endpoint relations \(g_0(0)=0\), \(g_1(0)=1\), \(g_0(1)=g_1(1)=1/2\) imply \(h_\theta(1)=h_\theta(0)=0\). Differentiating (1) at \(1\), the inverse-branch derivatives vanish and gives \(h_\theta'(1)=-h_\theta(1/2)/K_\theta^2\). At \(0\), the two branch derivatives are \(\pm1/\Lambda_\theta\) and both endpoint density values vanish, yielding \(h_\theta'(0)=[h_\theta'(0)-h_\theta'(1)]/\Lambda_\theta^2\). This establishes the two exact derivative identities.

**2. Uniform bounded variation near the tent endpoint.** Restrict temporarily to \(\theta\in[9/5,2)\); then \(\Lambda_\theta\ge19/10\). The four inverse branches of \(f_\theta^2\) map \([0,1]\) onto four consecutive subintervals \(J_\sigma\) that partition \([0,1]\). Because these intervals vary continuously and nondegenerately through \(\theta=2\), their lengths have a uniform lower bound \(m>0\). Each corresponding inverse-Jacobian product \(W_\sigma\) satisfies \(\|W_\sigma\|_\infty\le\Lambda_\theta^{-2}\) and \(\operatorname{Var}W_\sigma\le2\Lambda_\theta^{-2}\): the individual factors are monotone, bounded by \(\Lambda_\theta^{-1}\), and have variation no larger than this bound. The product-variation inequality, followed by \(\sup_J|\phi|\le\operatorname{Var}_J\phi+|J|^{-1}\int_J|\phi|\), therefore gives, for every \(\phi\in BV\),
\[
\operatorname{Var}(\mathcal L_\theta^2\phi)
\le\frac{3}{\Lambda_\theta^2}\operatorname{Var}\phi
+\frac{2}{m\Lambda_\theta^2}\|\phi\|_1
\le \rho\operatorname{Var}\phi+C\|\phi\|_1,\tag{2}
\]
with \(\rho=3/(19/10)^2<1\) and \(C=2/[m(19/10)^2]\). Applying (2) to \(h_\theta=\mathcal L_\theta^2h_\theta\), and using \(\|h_\theta\|_1=1\), establishes a uniform variation bound \(B=C/(1-\rho)\). Thus \(\|h_\theta\|_\infty\le1+B\).

By compactness of bounded subsets of \(BV\) in \(L^1\), every sequence \(\theta\uparrow2\) has a subsequence with an \(L^1\)-limit \(h\). Uniform convergence \(f_\theta\to f_2\), where \(f_2\) is the full tent map, passes invariance to the limit against continuous tests. The tent transfer operator contracts variation by \(1/2\), so its unique \(L^1\) invariant probability density is the constant \(1\). Hence every subsequence has the same limit and \(h_\theta\to1\) in \(L^1\).

To upgrade to *interior uniform convergence*, apply (2) iteratively to \(\phi_\theta=h_\theta-1\), with \(\|\phi_\theta\|_1\to0\) and \(\operatorname{Var}\phi_\theta\le B\). As transfer operators contract \(L^1\),
\[
\operatorname{Var}(\mathcal L_\theta^{2n}\phi_\theta)
\le \rho^n B+\frac{C}{1-\rho}\|\phi_\theta\|_1.
\]
The elementary \(BV\) estimate \(\|v\|_\infty\le\operatorname{Var}v+\|v\|_1\) gives the analogous uniform bound. For fixed \(n\), \(\mathcal L_\theta^{2n}1\to\mathcal L_2^{2n}1=1\) uniformly on each compact subset of \((0,1)\), because the finite inverse-orbit tree stays away from \(1\), the sole discontinuous-weight limiting point. Finally \(h_\theta-\mathcal L_\theta^{2n}1=\mathcal L_\theta^{2n}\phi_\theta\). Send \(\theta\uparrow2\), then \(n\to\infty\). This proves local uniform convergence, in particular \(h_\theta(1/2)\to1\).

**3. Right endpoint layer.** Since \(K_{2-\varepsilon}=\varepsilon/(2\sqrt2)\), for fixed \(z\ge0\),
\[
w_{2-\varepsilon}(1-\varepsilon^2z)=\frac1{2-\varepsilon}
\left(1-\frac1{\sqrt{1+8(2-\varepsilon)z}}\right).
\]
Both inverse branches of \(1-\varepsilon^2z\) tend uniformly to \(1/2\) for \(z\) in any compact set. Substituting into (1), the interior uniform convergence yields \(R(z)\), uniformly on compacts.

**4. Propagation to the left endpoint.** For each \(x\in[0,1]\), define \(x_0=x\) and \(x_{j+1}=g_0(x_j)\). Iterating (1) along this inverse branch yields
\[
h_\theta(x)=\sum_{j=0}^{\infty}\left[\prod_{k=0}^{j}w_\theta(x_k)\right]h_\theta(1-x_{j+1}).\tag{3}
\]
The omitted tail after index \(j\) is bounded by \((1+B)\Lambda_\theta^{-(j+1)}\), which tends uniformly to zero as \(j\to\infty\) for \(\theta\ge9/5\). For \(x=\varepsilon^2z\), fixed \(j\), and \(z\) in a compact interval, repeated use of \(g_0'(0)=\Lambda_\theta^{-1}\) proves \(x_j/\varepsilon^2\to z/2^j\) uniformly; also \(w_\theta(x_j)\to1/2\). Apply the right-layer limit to each \(h_\theta(1-x_{j+1})\), and use the geometric tail bound to exchange the limit and sum in (3). This gives exactly \(L(z)\). Grouping the series by its first term proves the displayed renewal equation. The series also gives \(L'(0)=8\sum_{j\ge1}4^{-j}=8/3\), while \(R'(0)=8\).

**5. Sobolev obstruction.** The derivative identities from step 1 and \(h_\theta(1/2)\to1\) yield the two scaled derivative limits. Since \(h_\theta'\) is absolutely continuous, \(\|h_\theta''\|_1\ge|h_\theta'(1)-h_\theta'(0)|\), proving the lower bound \(32/3\). Also the boundary traces of \(h_\theta-1\) are \(-1\), forbidding its convergence to zero in \(W^{1,1}\).

## Verification

The accompanying `verify.py` runs finite-grid Perron–Frobenius iterations at two positive cusp strengths, confirms probability normalization and endpoint vanishing to grid tolerance, compares both rescaled endpoint profiles at three scaled locations, and checks the exact dyadic renewal identity numerically. Reproduce with `python verify.py` and NumPy installed. This is a numerical consistency check, not an infinite-parameter proof. The universal assertions are established by steps 1–5.

## Relationship to prior work

Oltiboev and Vafoyev [1] establish fixed-parameter \(W^{2,1}\) existence, a spectral gap, and analytic response to Bernoulli mixing *between two fixed cusp maps*. Their Section 3 defines the family used here; the source does not classify the singular deterministic limit \(\theta\uparrow2\), the two rescaled invariant-density layers, or the derivative blow-up. Their fixed-parameter endpoint regularity is used, not claimed as new. Fixed-parameter endpoint derivative identities have also been established for random mixtures containing these maps; their deterministic special case is reproduced as an input, not a novelty assertion. Oltiboev, Rakhimov, and Ruziboev [2] consider random cusp systems and response under probability perturbation; Bahsoun and Galatolo [3] consider singularity-driven response in a different parameter regime. Neither inspected statement implies these explicit endpoint profiles. Standard Lasota–Yorke and \(BV\) compactness techniques are used as tools rather than new theorems. Specialized unindexed or inaccessible boundary-layer literature remains a historical-priority risk.

## Limitations

Only the displayed one-parameter deterministic cusp family and its limit to the full tent map are covered. The lower bound on \(\|h_\theta''\|_1\) is not asserted to be a sharp asymptotic equality; no upper asymptotic for that norm is proved. Local uniform convergence does not include endpoints. The results neither give uniform mixing bounds as \(\theta\uparrow2\) nor classify general cusp perturbations or random mixtures.

## References

[1] D. Oltiboev and F. Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, ACTA NUUz (Exact Sciences), 2(2.3), 178–183 (issue published 2026-10-06), https://journals.nuu.uz/index.php/actanuuz/article/view/15305 ; arXiv:2610.23180v1 (2026-10-16), https://arxiv.org/abs/2610.23180 .

[2] D. Oltiboev, K. Rakhimov and M. Ruziboev, *Linear response for random systems with a cusp*, arXiv:2608.26969v1 (2026-08-27), https://arxiv.org/abs/2608.26969 .

[3] W. Bahsoun and S. Galatolo, *Linear response due to singularities*, Nonlinearity 37 (2024), 075010, https://arxiv.org/abs/2301.02301 .

[4] A. Lasota and J. Yorke, *On the existence of invariant measures for piecewise monotonic transformations*, Trans. Amer. Math. Soc. 186 (1973), 481–488.
