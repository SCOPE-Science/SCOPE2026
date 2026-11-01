# Sharp inverse-square regularization penalty for two-moment annihilator projections

## Finding

The natural codimension-two annihilator of the mass and first-moment functionals in a real continuous-function space admits arbitrarily near-minimal projections, but never a minimal projection. Imposing a Lipschitz bound on the canonical first-moment coefficient introduces a sharp, explicitly computable inverse-square penalty.

Write \(X=C([-1,1];\mathbb R)\) with the supremum norm, and let \(d\mu(t)=dt/2\). Put
\[
Y=\left\{f\in X:\int f\,d\mu=0,\quad\int tf(t)\,d\mu=0\right\}.
\]
Every bounded projection \(P:X\to Y\) has a unique representation
\[
Pf=f-\left(\int f\,d\mu\right)g_0-\left(\int tf(t)\,d\mu\right)g_1
\]
for continuous real functions \(g_0,g_1\), with the four normalization conditions
\[
\int g_0\,d\mu=1,\qquad \int tg_0(t)\,d\mu=0,\qquad
\int g_1\,d\mu=0,\qquad \int tg_1(t)\,d\mu=1.
\]
Define the usual global Lipschitz seminorm \(\operatorname{Lip}(g_1)=\sup_{s\ne t}|g_1(s)-g_1(t)|/|s-t|\). For real \(K>0\), put
\[
\Lambda(K)=\inf\{\|P\|:P^2=P,\ \operatorname{ran}P=Y,\ \operatorname{Lip}(g_1)\le K\}.
\]
For \(K\ge3\) this family is nonempty; if needed an empty infimum is understood as \(+\infty\).

For \(r>0\), define
\[
A(r)=r\operatorname{arsinh}(1/r),\qquad
B(r)=\frac{1+\sqrt{1+r^2}-r^2\operatorname{arsinh}(1/r)}2.
\]
The equation \(A(r_*)=B(r_*)\) has exactly one positive solution. Let \(L=1/A(r_*)\). Then
\[
\boxed{\lambda(Y,X)=1+L,\qquad
\lim_{K\to\infty}K^2[\Lambda(K)-(1+L)]
=\frac{L^4}{6(1+r_*)}.}
\]
Numerically, \(r_*=0.7349935892425393\ldots\), \(1+L=2.2204049171163608\ldots\), and the displayed sharp coefficient is \(0.2130917668352374\ldots\). No projection onto \(Y\) attains \(\lambda(Y,X)\).

The inverse-square asymptotic, rather than an unrestricted minimal-projection formula alone, is the quantitative contribution. The parameter \(K\) regularizes exactly the first-moment coordinate selected by the normalized moment basis \(\mu,t\mu\).

## Assumptions and scope

All spaces and coefficients are **real**. Integrals are with respect to uniform probability measure on the closed interval; in particular \(\int t^2\,d\mu=1/3\). No differentiability beyond global Lipschitz continuity of \(g_1\) is assumed. The estimate concerns the limit \(K\to\infty\) and does not assert a closed form for \(\Lambda(K)\) at every finite value. The projection norm is the norm as an operator on \(C([-1,1];\mathbb R)\), not a norm on an \(L^p\) domain.

## Proof

**1. Exact dual reduction.** Put \(R=I-P\). The four moments imply \(R^2=R\), \(\ker R=Y\), and \(R\) has rank two. Since the compact interval has no isolated points, the finite-rank Daugavet identity gives \(\|P\|=\|I-R\|=1+\|R\|\). Its adjoint is
\[
R^*\nu=\langle\nu,g_0\rangle\mu+\langle\nu,g_1\rangle(t\mu).
\]
Consequently
\[
\|R\|=\|R^*\|=\max_{x\in[-1,1]}\Phi(g_0(x),g_1(x)),\qquad
\Phi(a,b)=\frac12\int_{-1}^1|a+bt|\,dt.
\]
The elementary formula
\[
\Phi(a,b)=\begin{cases}|a|,&|a|\ge|b|,\\(a^2+b^2)/(2|b|),&|a|<|b|\end{cases}
\]
is valid also at zero by continuity. Reflection and convex averaging replace \(g_0(x)\) by its even part and \(g_1(x)\) by its odd part, preserving all four moments, not increasing \(\|R\|\), and not increasing \(\operatorname{Lip}(g_1)\). We henceforth restrict to these symmetrized functions, writing \(a(t)=g_0(t)\) and \(b(t)=g_1(t)\) for \(t\in[0,1]\). The normalization becomes \(\int_0^1a(t)\,dt=\int_0^1t b(t)\,dt=1\).

**2. A two-dimensional polar certificate.** For every \(r>0\) and \(t>0\),
\[
\sup_{\Phi(u,v)\le1}\{ru+tv\}=t+\sqrt{r^2+t^2}.
\]
Indeed the maximizing coordinates may be taken nonnegative. In the region \(0\le v\le u\), the supremum is at most \(r+t\). In the region \(0\le u<v\), the unit constraint is \(u^2+(v-1)^2\le1\), and Euclidean support gives \(t+\sqrt{r^2+t^2}\). The unique maximizer for \(r,t>0\) is
\[
(u,v)=\left(\frac r{\sqrt{r^2+t^2}},\ 1+\frac t{\sqrt{r^2+t^2}}\right).
\]
Define
\[
H(r)=\int_0^1(t+\sqrt{r^2+t^2})\,dt=rA(r)+B(r).
\]
If \(M=\|R\|\), integration of the polar inequality yields
\[
r+1=\int_0^1(ra+tb)\,dt\le M H(r),
\quad\text{hence}\quad
M\ge \sup_{r>0}\frac{1+r}{H(r)}.
\]
Moreover \(A'(r)=\operatorname{arsinh}(1/r)-1/\sqrt{1+r^2}>0\) and \(B'(r)=-rA'(r)<0\). Since \(A(0+)=0\), \(B(0+)=1\), \(A(\infty)=1\), and \(B(\infty)=1/2\), there is a unique \(r_*>0\) with \(A(r_*)=B(r_*)\). At that root \(H(r_*)=(1+r_*)A(r_*)\). Hence \(M\ge L=1/A(r_*)\).

**3. Sharpness without attainment.** For \(t>0\), define
\[
a_*(t)=L\frac{r_*}{\sqrt{r_*^2+t^2}},\qquad
b_*(t)=L\left(1+\frac t{\sqrt{r_*^2+t^2}}\right).
\]
Extend \(a_*\) evenly and \(b_*\) oddly. These bounded measurable functions satisfy the four moments and have \(\Phi(a_*(t),b_*(t))=L\) almost everywhere. Truncating the odd jump around \(t=0\) and adjusting the root as in part 5 produces continuous admissible pairs whose norms tend to \(L\), showing \(\lambda(Y,X)=1+L\).

If a continuous pair attained \(M=L\), nonnegativity of the pointwise polar deficit and equality of its integral would force equality in the unique polar maximizer at almost every \(t>0\), hence by continuity at every \(t>0\). Thus \(b(t)\to L\) as \(t\downarrow0\). But odd continuity requires \(b(0)=0\). This contradiction rules out a minimal projection. The argument also precludes attainment by a nonsymmetric original pair because its symmetrization is continuous.

**4. Sharp lower bound under a Lipschitz constraint.** Fix \(K>0\), choose a symmetric admissible pair with \(M=\|R\|\le K\), and set \(r=r_*\) in the polar certificate. Since \(b(0)=0\), \(|b(t)|\le Kt\); since \(\Phi(a,b)\ge|a|\), one has \(a(t)\le M\). For \(0\le t\le M/K\),
\[
\begin{aligned}
&M\left(t+\sqrt{r_*^2+t^2}\right)-r_*a(t)-tb(t)\\
&\qquad\ge Mt-Kt^2,
\end{aligned}
\]
while the full integrand is nonnegative on \([0,1]\). Integration gives the **finite-parameter certificate**
\[
H(r_*)[M-L]\ge\int_0^{M/K}(Mt-Kt^2)\,dt
=\frac{M^3}{6K^2}.
\]
It follows that \(\liminf_{K\to\infty}K^2[\Lambda(K)-(1+L)]\ge L^3/[6H(r_*)]=L^4/[6(1+r_*)]\), provided a matching bounded-norm family is available. That family is constructed next. For approximate infimizers, the same bound applies; no existence of a minimizer for \(\Lambda(K)\) is assumed.

**5. Explicit continuous near-optimal projections.** For a parameter \(r\) near \(r_*\) put \(M(r)=1/A(r)\) and define, for \(t\ge0\),
\[
\begin{aligned}
a_r(t)&=M(r)\frac r{\sqrt{r^2+t^2}},\\
b_{r,K}(t)&=\min\left\{Kt,\ M(r)\left(1+\frac t{\sqrt{r^2+t^2}}\right)\right\}.
\end{aligned}
\]
Extend \(a_r\) evenly and \(b_{r,K}\) oddly. For all sufficiently large \(K\), the two branches defining \(b_{r,K}\) are \(K\)-Lipschitz; their minimum and odd extension are also \(K\)-Lipschitz. Since \(b_{r,K}\) is between zero and the polar optimizer's second coordinate, and \(\Phi\) is nondecreasing in \(|b|\) for fixed \(|a|\), one has \(\Phi(a_r(t),b_{r,K}(t))\le M(r)\) everywhere. Also \(\int_0^1 a_r(t)dt=1\).

The missing first moment is \(M(r)D(r,K)\), where
\[
D(r,K)=\int_0^1 t\left[1+\frac t{\sqrt{r^2+t^2}}-\frac K{M(r)}t\right]_+dt.
\]
The function \(D(r,K)\) is continuous in \(r\), nonnegative and, uniformly for \(r\) near \(r_*\), satisfies
\[
D(r,K)=\frac{M(r)^2}{6K^2}+O(K^{-3}).
\]
For this estimate, the positive part is supported on \([0,t_0]\), where the unique crossing obeys \(t_0=M(r)/K+O(K^{-2})\). Expanding \(1+t/\sqrt{r^2+t^2}=1+O(t)\) and integrating \(t-(K/M(r))t^2\) from zero to \(M(r)/K\) gives the stated leading coefficient, with uniform remainder.

The scalar equation \(B(r)-A(r)=D(r,K)\) has a solution \(r_K\to r_*\) by the strict decrease of \(B-A\) and the intermediate value theorem. At \(r=r_K\), \(\int_0^1t b_{r,K}(t)dt=M(r_K)[B(r_K)-D(r_K,K)]=1\). Evenness and oddness give the two remaining zero moments, so \((a_{r_K},b_{r_K,K})\) represents a genuine projection with \(\|P\|\le1+M(r_K)\).

**6. Matching the coefficient.** Since \((B-A)'(r_*)=-(1+r_*)A'(r_*)\), the equation in part 5 gives
\[
r_K-r_*=-\frac{L^2}{6(1+r_*)A'(r_*)}\frac1{K^2}+O(K^{-3}).
\]
Because \(M'(r_*)=-L^2A'(r_*)\),
\[
M(r_K)=L+\frac{L^4}{6(1+r_*)}\frac1{K^2}+O(K^{-3}).
\]
This is the matching upper bound; combined with part 4 it proves the displayed limit and the sharp coefficient.

## Verification

The accompanying `check_projection_regularization.py` is self-contained and runs with standard Python 3. It numerically reconstructs \(r_*\), \(L\), and the coefficient, checks the polar maximizers, solves the scalar equations for six values of \(K\), verifies the moment equations and sampled norm and Lipschitz inequalities, and checks the inverse-square trend. Its execution yielded **31,047 passing numerical assertions**. These finite checks do **not** prove the uniform remainder, the infinite-dimensional operator identity, or uniqueness of the polar maximizer; those are proved analytically above.

## Relationship to prior work

Kania and Lewicki (2026) prove the Daugavet-space duality for finite-codimensional projection constants and construct nonattaining examples through piecewise-constant dual spaces. The reduction in part 1 is an application of their theorem, **not** an original theorem. Their inspected preprint treats neither the mass/first-moment annihilator nor a Lipschitz-constrained sharp asymptotic.

The Chalmers–Metcalf literature establishes classical minimal \(L^1\) projection and extension techniques, including polynomial subspaces. The unrestricted two-dimensional optimization is treated as background supporting the new result, not as independent evidence of originality. The contribution asserted here is **specifically the sharp \(K^{-2}\) asymptotic and its coefficient for the canonical first-moment regularization**, along with its direct boundary-layer proof. Earlier polynomial-projection work may imply related unconstrained facts under other formulations.

## Limitations

The result is for the real, uniformly weighted interval and for the particular, basis-normalized first-moment Lipschitz seminorm. It does not give a universal rate for general finite-codimensional subspaces, arbitrary moment weights, other regularity moduli, or all \(K\). Related 1992 and 1997 Chalmers–Metcalf primary texts were not fully accessible during comparison; their known abstracts do not establish the stated regularization asymptotic, but definitive historical priority requires additional primary-text review.

## References

1. T. Kania and G. Lewicki, *Finite-codimensional subspaces of Daugavet spaces: projection constants and minimal projections*, arXiv:2604.10771v1, publicly submitted 2026-04-12, especially Theorem 3.1 and Sections 4–5. https://arxiv.org/pdf/2604.10771
2. B. L. Chalmers and F. T. Metcalf, *The determination of minimal projections and extensions in L1*, Transactions of the American Mathematical Society **329** (1992), 289–305. DOI:10.1090/S0002-9947-1992-1034660-1.
3. B. L. Chalmers and F. T. Metcalf, *The minimal projection from L1 onto πn*, in *Stochastic Processes and Functional Analysis* (1997), 61–69. DOI:10.1201/9781003067597-5.
4. G. Lewicki and M. P. Prophet, *Simultaneous minimal extensions with applications*, Real Analysis Exchange **50** (2025), 159–177. DOI:10.14321/realanalexch.1721734662.
5. P. Hájek and T. Russo, *Projecting Lipschitz functions onto spaces of polynomials*, Mediterranean Journal of Mathematics **19** (2022), 190. arXiv:2102.02778 (a different Lipschitz-space complementability problem).
