# Exact derivative-order asymptotics and an error-function transition for one-diagonal Bergman traces

## Finding
Consider the finite-interval derivative energy introduced by Hartmann and Orsoni, with each derivative order retained rather than summed immediately. Its response to a boundary pole has two distinct sharp power laws, and the circle–line junction has an explicit, uniform complementary-error-function transition.

For \(\sigma>0\), \(0<a<1\), and either sign, put \(\zeta=a\pm i h(a)\), where
\[
h(a)=\begin{cases}
a,&0<a\le1/4,\\
\sqrt{1/8-(a-1/2)^2},&1/4\le a\le3/4,\\
1-a,&3/4\le a<1.
\end{cases}
\]
Let \(f(z)=(\zeta-z)^{-\sigma}\), with an analytic branch on the domain defined below, and set
\[
E_n(\sigma,\zeta)=\frac{2^n}{(2n+1)!}\int_0^{1/2}x^{2n+1}\left(\lvert f^{(n)}(x)\rvert^2+\lvert f^{(n)}(1-x)\rvert^2\right)\,dx.
\]
As \(n\to\infty\), the following **exact asymptotic equivalents** hold.

For \(1/4<a<3/4\) (open circular cap),
\[
E_n(\sigma,\zeta)\sim\frac{\sqrt\pi\,8^\sigma}{4\Gamma(\sigma)^2}
\left(\frac1{16a-4}+\frac1{12-16a}\right)n^{2\sigma-7/2}.
\]
For \(0<a<1/4\) or \(3/4<a<1\) (straight sides), with \(r=\min(a,1-a)\),
\[
E_n(\sigma,\zeta)\sim\frac{\pi\,2^{1-\sigma}r^{2-2\sigma}}{\Gamma(\sigma)^2}
n^{2\sigma-3}.
\]
For the two junctions \(a\in\{1/4,3/4\}\),
\[
E_n(\sigma,\zeta)\sim\frac{\pi\,8^\sigma}{16\Gamma(\sigma)^2}n^{2\sigma-3}.
\]
These formulas hold on either upper or lower boundary by conjugation.

**Junction window.** Fix \(\eta\in\mathbb R\), put \(a_n=1/4+\eta/\sqrt n\), and choose \(\zeta_n=a_n+i h(a_n)\). Then
\[
\lim_{n\to\infty}n^{3-2\sigma}E_n(\sigma,\zeta_n)
=\frac{\pi\,8^\sigma}{16\Gamma(\sigma)^2}
 e^{16(\max\{\eta,0\})^2}\operatorname{erfc}(4\eta),
\]
uniformly for \(\eta\) in each fixed compact interval. The corresponding assertion at the right junction is obtained by replacing \(a_n\) with \(3/4-\eta/\sqrt n\), and the lower boundary gives the same constants.

Consequently the one-diagonal energy sum \(\sum_{n\ge0}E_n\) converges exactly for \(\sigma<5/4\) at open cap points, and exactly for \(\sigma<1\) at straight-side points or junctions. In contrast, \(f\in A^2(\Omega)\) holds exactly for \(\sigma<1\) at **every** nonvertex boundary point. Thus the cap supports the sharp interval \(1\le\sigma<5/4\) in which all one-diagonal derivative energy is finite despite an infinite Bergman norm. The previously published simple-pole example is a special instance of the last phenomenon, not a novelty assertion here.

## Assumptions and scope
Let \(D(c,r)=\{z\in\mathbb C:\lvert z-c\rvert<r\}\), and let
\[
\Omega=\bigcup_{0<t\le1/2}D(t,t/\sqrt2)
\;\cup\;\bigcup_{0<t<1/2}D(1-t,t/\sqrt2).
\]
A direct maximization over \(t\) gives \(\Omega=\{a+ib:0<a<1,\lvert b\rvert<h(a)\}\), with the boundary height specified above. This simply connected domain admits an analytic branch of \((\zeta-z)^{-\sigma}\) for \(\zeta\in\partial\Omega\) and \(\sigma>0\). The branch phase does not affect the energy. All displayed limits concern \(n\to\infty\), with \(\sigma>0\) fixed; compact uniformity is asserted only for the moving-junction parameter \(\eta\). The vertices \(0,1\) are excluded, and the theorem makes no statement about arbitrary holomorphic functions.

## Proof
**1. Exact Laplace reduction and normalization.** The positive derivative magnitude is
\[
\lvert f^{(n)}(x)\rvert^2=\frac{\Gamma(n+\sigma)^2}{\Gamma(\sigma)^2}
\lvert x-\zeta\rvert^{-2(n+\sigma)}.
\]
Write \(b=h(a)\), and for \(t\in\{a,1-a\}\) put
\[
R_t(x)=\frac{x^2}{2((x-t)^2+b^2)},\qquad
G_t(x)=x((x-t)^2+b^2)^{-\sigma},
\quad 0\le x\le\frac12.
\]
Then, **exactly**,
\[
E_n=P_n\sum_{t\in\{a,1-a\}}\int_0^{1/2}G_t(x)R_t(x)^n\,dx,
\qquad P_n=\frac{4^n\Gamma(n+\sigma)^2}{\Gamma(\sigma)^2\Gamma(2n+2)}.
\]
The two indexed terms are retained separately even when \(a=1/2\). The gamma duplication/Stirling formula gives
\[
P_n=\frac{\sqrt\pi}{2\Gamma(\sigma)^2}
 n^{2\sigma-5/2}\left(1+O_\sigma(n^{-1})\right).
\]
Geometrically, \(R_t(x)\le1\), since every disk \(D(x,x/\sqrt2)\), \(0<x\le1/2\), stays inside \(\Omega\) and \(\zeta\) is a boundary point. Equality in \(R_t\) occurs precisely at the disk-center parameters whose circles touch \(\zeta\).

**2. Interior cap.** For \(1/4<a<3/4\), \(R_a(1/2)=R_{1-a}(1/2)=1\), and both have their unique maximum at the right integration endpoint. Direct differentiation gives
\[
\left.\frac{d}{dx}\log R_t(x)\right|_{x=1/2}=16t-4>0,
\qquad G_t(1/2)=8^\sigma/2.
\]
Endpoint Laplace asymptotics yields
\[
\int_0^{1/2}G_t(x)R_t(x)^n\,dx\sim
\frac{8^\sigma}{2n(16t-4)}.
\]
Summing \(t=a,1-a\) and multiplying by \(P_n\) proves the cap formula.

**3. Open straight sides.** By reflection it suffices to take \(0<a<1/4\). In the term \(t=a\), \(R_a\) reaches its unique maximum \(1\) at the *interior* point \(x=2a\). A direct calculation yields
\[
\left.\frac{d^2}{dx^2}\log R_a(x)\right|_{x=2a}=-\frac{1}{2a^2},\qquad
G_a(2a)=2^{1-\sigma}a^{1-2\sigma}.
\]
The interior Laplace formula therefore gives
\[
\int_0^{1/2}G_a(x)R_a(x)^n\,dx
\sim 2^{2-\sigma}a^{2-2\sigma}\sqrt\pi\,n^{-1/2}.
\]
For \(t=1-a\) the continuous ratio \(R_{1-a}\) is uniformly strictly below \(1\) on the integration interval, so its contribution is exponentially small. Multiplying by the Stirling prefactor proves the straight-side constant. Reflection gives the right side.

**4. Fixed junctions.** At \(a=1/4\), the left interior maximizer has just reached \(x=1/2\). With \(v=1/2-x\),
\[
R_{1/4}(1/2-v)=1-4v^2+O(v^3),\qquad
G_{1/4}(1/2)=8^\sigma/2.
\]
Thus the leading integral is the *half* Gaussian
\[
\int_0^{1/2}G_{1/4}(x)R_{1/4}(x)^n\,dx
\sim\frac{8^\sigma}{2}\frac{\sqrt\pi}{4\sqrt n}.
\]
The other term, \(t=3/4\), has a nondegenerate endpoint slope and contributes \(O(n^{-1})\). Multiplication by \(P_n\) gives the junction coefficient. Reflection treats \(a=3/4\).

**5. Uniform moving-junction crossover.** Let \(a=1/4+\delta\), \(\delta=\eta/\sqrt n\), and \(v=1/2-x\). On the cap side \(\delta\ge0\), the exact identity is
\[
R_a(1/2-v)=1-\frac{v^2+4\delta v}{1/4-v+4\delta v+2v^2}.
\]
On the straight side \(\delta\le0\), the exact identity is
\[
R_a(1/2-v)=1-\frac{(v+2\delta)^2}{1/4+4\delta^2-v+4\delta v+2v^2}.
\]
Substitute \(v=y/\sqrt n\). On every bounded \(y\)-interval the powers tend uniformly for bounded \(\eta\) to
\[
R_a(1/2-y/\sqrt n)^n
\longrightarrow\exp\bigl(-4(y+2\eta)^2+16(\max\{\eta,0\})^2\bigr).
\]
The derivative factor tends to \(8^\sigma/2\). To justify integration over the growing interval, fix a sufficiently small \(v_0>0\): the exact denominators above stay bounded between two positive constants for \(0\le v\le v_0\) and bounded \(\eta\), so \(R_a^n\le C\exp(-c y^2)\) after absorbing a uniform linear term; for \(v\ge v_0\), compactness and the unique maximum at \(v=0\) for \(\delta=0\) give \(R_a^n=O(e^{-c'n})\), uniformly over bounded \(\eta\). These estimates justify compact-uniform dominated convergence. The mirrored term \(t=1-a\) has an ordinary endpoint maximum near \(\delta=0\), contributing \(O(n^{-1})\), uniformly over bounded \(\eta\), and is negligible after \(n^{-1/2}\) scaling. Finally,
\[
\int_0^\infty e^{-4(y+2\eta)^2}\,dy
=\frac{\sqrt\pi}{4}\operatorname{erfc}(4\eta),
\]
which, combined with the prefactor from step 1, proves the stated profile, including its exponential factor for \(\eta>0\).

**6. Summability and Bergman threshold.** Every leading constant is positive. The series \(\sum_{n\ge1}n^{2\sigma-7/2}\) converges iff \(\sigma<5/4\); the series \(\sum_{n\ge1}n^{2\sigma-3}\) converges iff \(\sigma<1\). The \(n=0\) term is finite because \(\zeta\) is not on the real interval. At every listed boundary point, the domain has a nonzero interior cone and fits locally inside a half-disk about \(\zeta\); polar comparison of \(\int |z-\zeta|^{-2\sigma}\,dA\) with \(\int_0^\varepsilon r^{1-2\sigma}dr\) proves the Bergman criterion. No finite computation is invoked in this implication.

## Verification
The accompanying Python 3 script `verify_trace.py` directly quadratures the **original exact derivative-order expression** in its stable Laplace form (Simpson integration, gamma normalization via `lgamma`) and compares against all three fixed-location coefficient formulas at five boundary points and against the junction profile at three moving values. Its observed output is:

`CHECK_OK: five fixed-boundary asymptotics and three junction crossover profiles; finite quadrature only`

This is a finite numerical sanity check. All infinite-domain claims follow from the six analytic proof steps above. Reproduce with `python3 verify_trace.py` using only the standard library.

## Relationship to prior work
Hartmann and Orsoni, *Identifying Bergman space functions from intervals* (arXiv:2602.14801, first public version 2026-02-16, revised 2026-10-03), introduce exactly this one-diagonal series, domain, and an explicit pole at the midpoint of the upper circular arc for which a finite one-diagonal sum fails to detect infinite Bergman area. That basic obstruction and the full two-diagonal norm identity are **established prior work**, not claimed as new. Their Section 3 bounds the entire sum but does not provide the all-location sharp asymptotics of its individual derivative orders or the moving circle–line junction window. Aikawa, Hayashi and Saitoh's 1991 infinite-sector identity is also prior work; it does not analyze this finite-domain boundary transition. The present added statement resolves the derivative-order energy localization and the sharp coefficient across the natural geometric junction. This comparison was made against their accessible primary full texts; undiscovered equivalent asymptotic computations in older literature remain possible.

## Limitations
The result is specific to pole powers with real positive exponent on the nonvertex boundary of the stated disk-union domain. It is not a general norm equivalence or reconstruction theorem; the simple-pole non-detectability itself is prior art. Uniformity holds on compact sets of the moving parameter, not over all boundary points simultaneously. The source literature may imply weaker convergence thresholds by alternative global arguments, but it does not explicitly give these sharp derivative-order coefficients or the error-function crossover in the inspected material. Independent priority assessment and independent proof validation have not been performed.

## References
Hartmann, Andreas, and Marcu-Antone Orsoni. *Identifying Bergman space functions from intervals*. arXiv:2602.14801v1 (2026-02-16) and v2 (2026-10-03). https://arxiv.org/html/2602.14801v2 ; https://arxiv.org/abs/2602.14801 .

Aikawa, Hiroaki, Wataru Hayashi, and Saburou Saitoh. *Isometrical identities for the Bergman and the Szegö spaces on a sector*. Journal of the Mathematical Society of Japan **43** (1991), 195–201. https://doi.org/10.2969/jmsj/04310195 .
