# An exact global reset-benefit threshold for a partially reactive interval

## Finding
Consider a diffusion of diffusivity \(D>0\) on \([0,L]\), with a reflecting right endpoint, a partially reactive left endpoint of radiation rate \(\kappa>0\), and an initial/reset location \(x_0\in(0,L)\). Independent Poisson position resets to \(x_0\) occur at rate \(r\ge0\) and do not reset accumulated reaction history beyond renewal of surviving paths. Set
\[
\beta=1-x_0/L,\qquad \eta=D/(\kappa L),\qquad u=\beta^2,\qquad y=L\sqrt{r/D}.
\]
The mean absorption time \(T(r)\) obeys, for \(r>0\),
\[
\frac{D T(r)}{L^2}=\frac{\cosh y+\eta y\sinh y-\cosh(\beta y)}{y^2\cosh(\beta y)},\qquad
\frac{D T(0)}{L^2}=\eta+\frac{1-u}{2}.
\]
**Sharp global classification:** define
\[
F(u,\eta)=(1-u)(1-5u)+4\eta(1-3u).
\]
If \(F(u,\eta)\ge0\), then \(T(r)>T(0)\) for **every** \(r>0\); no resetting is the unique globally optimal strategy. If \(F(u,\eta)<0\), then some \(r>0\) strictly reduces the absorption time and a finite positive global minimizer exists. This last assertion does not require or claim uniqueness among positive minimizers. In particular, the critical initial position is given explicitly by
\[
u_c(\eta)=\frac{3+6\eta-2\sqrt{1+4\eta+9\eta^2}}{5},\qquad
x_{0,c}/L=1-\sqrt{u_c(\eta)}.
\]
Resetting is beneficial precisely when \(x_0/L<x_{0,c}/L\), and not beneficial at equality. The threshold moves continuously from \(1-1/\sqrt5\) in the perfectly reactive limit \(\eta\downarrow0\) to \(1-1/\sqrt3\) as \(\eta\to\infty\). Both limiting values are limits of the theorem, not assertions at zero reactivity.

## Assumptions and scope
The diffusion has generator \(D\partial_x^2\) on \((0,L)\). Its no-reset absorption-time Laplace transform \(\phi(s,x)=\mathbb E_x[e^{-s\mathcal T}]\) solves \(D\phi_{xx}=s\phi\), with boundary conditions \(D\phi_x(0)=\kappa(\phi(0)-1)\) and \(\phi_x(L)=0\). Thus \(\phi(0)\ne1\) at finite reactivity. All claims quantify over \(D,L,\kappa>0\), \(x_0\in(0,L)\) and \(r\ge0\). Reaction is Markovian and reset times are exponential, independent of diffusion.

## Proof
**Laplace transform and renewal.** The unique bounded solution to the second-order boundary-value problem is
\[
\phi(s,x)=\frac{\cosh((L-x)\sqrt{s/D})}{\cosh(L\sqrt{s/D})+(\sqrt{Ds}/\kappa)\sinh(L\sqrt{s/D})}.
\]
Indeed its spatial derivative at \(L\) is zero, and its derivative at zero is \(-\sqrt{s/D}\sinh(L\sqrt{s/D})\) times the normalization; multiplying by \(D\) gives \(\kappa(\phi(0)-1)\). The ordinary renewal decomposition at Poisson reset time gives \(T(r)=[1-\phi(r,x_0)]/[r\phi(r,x_0)]\), from which the displayed mean-time formula and its \(r=0\) limit follow.

**A global sign criterion.** Put \(t_0=\eta+(1-u)/2\). Multiplication by the positive \(y^2\cosh(\beta y)\) shows that the sign of \(T(r)-T(0)\) is exactly the sign of
\[
Q(y)=\cosh y+\eta y\sinh y-(1+t_0y^2)\cosh(\beta y).
\]
Its absolutely convergent even Taylor series is
\[
Q(y)=\sum_{n=2}^{\infty}\frac{B_n y^{2n}}{(2n)!},\quad
B_n=(1-u)\left[\sum_{j=0}^{n-1}u^j-n(2n-1)u^{n-1}\right]+2n\eta\left[1-(2n-1)u^{n-1}\right].
\]
In particular \(B_2=F(u,\eta)\). Write \(B_n=A_n+\eta C_n\), where \(A_n\) and \(C_n\) are the two displayed summands. For \(0<u<1/3\), all \(C_n>0\): this follows from \((2n-1)u^{n-1}<1\) for \(n\ge2\), since at \(n=2\) it is \(3u<1\) and subsequent ratios are at most \(5/9<1\). For \(n\ge4\), all \(A_n>0\): at \(n=4\), \(\sum_{j=0}^3u^j>1+u>28u^3\) for \(u<1/3\) (at the upper bound, \(1+u=4/3>28/27\)); for \(n\ge5\), \(n(2n-1)u^{n-1}\le n(2n-1)/3^{n-1}<1\) (the \(n=5\) bound is \(45/81<1\), and the expression decreases thereafter). Thus \(B_n>0\) for every \(n\ge4\) when \(u<1/3\).

If \(0<u\le1/5\), both \(A_2\ge0\) and \(A_3>0\), so every \(B_n>0\). Suppose now \(1/5<u<1/3\) and \(B_2\ge0\). Since \(C_2>0\), this means \(\eta\ge -A_2/C_2\). Because \(C_3>0\), it suffices to test \(B_3\) at that threshold. Direct polynomial factorization gives
\[
A_3 C_2-A_2 C_3=-2(u-1)^3(9u-1)>0
\]
for \(1/5<u<1/3\); hence \(B_3>0\). Combining these cases proves \(Q(y)>0\) for every \(y>0\) whenever \(B_2\ge0\). Conversely, if \(B_2<0\), the expansion \(Q(y)=B_2y^4/24+O(y^6)\) is negative for all sufficiently small \(y>0\). Moreover \(T(r)\to\infty\) as \(r\to\infty\), because \(x_0>0\), so a finite strictly positive global minimizer exists.

Finally \(F(u,\eta)\) is strictly decreasing on \(u\in(0,1/3)\) and changes sign between \(u=1/5\) and \(u=1/3\); for \(u\ge1/3\) it is negative. Solving its quadratic yields the stated \(u_c(\eta)\). The endpoint limits follow directly. This proves every strict/equality case.

## Verification
Run `python3 verify.py` with SymPy. The checker independently differentiates the Taylor expression through order twelve, checks the factored polynomial identity controlling the threshold, and tests 600 numerical parameter choices and multiple rates. These finite tests are diagnostics only; the all-parameter result rests on the complete positive-coefficient argument in the proof.

## Relationship to prior work
Evans and Majumdar (2011) introduced diffusion with Poisson resetting and the standard first-passage optimization principle. Whitehouse, Evans and Majumdar (2013) treat partially reactive targets, principally in unbounded geometry. Christou and Schadschneider (2015) study resetting with an *interior absorbing point* between reflecting walls and exhibit an optimal-rate transition. Its complete 18-page text was not accessible in this comparison, so potential reductions from its interior-trap formula remain a material priority risk. Benkhadaj and Grebenkov (2022), particularly their original full-text Sec. III.1 and Eq. (83), analyze bounded intervals with **reactive endpoints at both ends**; they derive first-reaction-time expressions and explore position resetting, but do not state the one-reactive/one-reflecting global threshold established here. The exact global if-and-only-if condition for finite \(\kappa\), including nonattainment of any positive-rate improvement on the boundary, is the assessed contribution; neither the renewal identity nor the Laplace solution alone is claimed novel.

## Limitations
No uniqueness or closed form of the positive optimal rate is asserted. The result excludes reset-location endpoints, nonexponential resetting, non-Markovian surface reactions, varying diffusivity, and more than one reactive boundary. Historical originality remains provisional, most materially because the complete 2015 interior-sink paper was not accessible. Independent review has not occurred.

## References
- M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting* (2011), arXiv:1102.2704.
- J. Whitehouse, M. R. Evans and S. N. Majumdar, *Effect of Partial Absorption on Diffusion with Resetting* (2013), Phys. Rev. E 87, 022118.
- C. Christou and A. Schadschneider, *Diffusion with Resetting in Bounded Domains* (first publicly verified 2015-06-23), J. Phys. A 48, 285003, DOI:10.1088/1751-8113/48/28/285003.
- Z. Benkhadaj and D. S. Grebenkov, *Encounter-based Approach to Diffusion with Resetting* (2022), arXiv:2209.00947, especially Sec. III.1.
