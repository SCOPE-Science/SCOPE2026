# Parity collapse of least-squares capacity bounds on two distant disks

## Finding
Let \(a>R>0\), and let
\[
K_{a,R}=\overline D(-a,R)\cup\overline D(a,R).
\]
Here \(dA=dx\,dy\) is unnormalized planar Lebesgue measure. For each integer \(m\ge0\), define the squared monic Bergman minimum
\[
\lambda_m(a,R)=\min_{q(z)=z^m+\cdots}\int_{K_{a,R}}|q(z)|^2\,dA(z).
\]
For \(n\ge1\), let
\[
L_n(a,R)=\left(\frac n\pi\lambda_{n-1}(a,R)\right)^{1/(2n)}.
\]
Ransford's capacity inequality guarantees \(L_n(a,R)\le\operatorname{cap}(K_{a,R})\) for every \(n\).

**Theorem.** For each *fixed* integer \(k\ge0\) and each \(\sigma\in\{0,1\}\), as \(a/R\to\infty\),
\[
\lambda_{2k+\sigma}(a,R)=\frac{2\pi4^k}{k+1}\,a^{2k+2\sigma}R^{2k+2}\left(1+O_k((R/a)^2)\right).
\]
Consequently,
\[
\operatorname{cap}(K_{a,R})\sim\sqrt{2aR},\qquad
\lim_{a/R\to\infty}\frac{L_{2k+2}(a,R)}{\operatorname{cap}(K_{a,R})}=1,\qquad
\lim_{a/R\to\infty}\frac{L_{2k+1}(a,R)}{\operatorname{cap}(K_{a,R})}=0.
\]
Thus **every fixed even degree** of the least-squares capacity bound is asymptotically sharp as the disks separate, while **every fixed odd degree** loses an asymptotically full proportion of the capacity.

The first three bounds are exactly
\[
L_1=\sqrt2\,R,\qquad
L_2=(4a^2R^2+2R^4)^{1/4},\qquad
L_3=(12a^2R^4+2R^6)^{1/6}.
\]
For every \(a\ge R>0\), \(L_2>\max\{L_1,L_3\}\); the lower-bound sequence is therefore not generally nondecreasing even for the union of two congruent disks.

## Assumptions and scope
The two closed disks are disjoint when \(a>R\); at \(a=R\), tangency occurs at one point, and the exact first-three-degree formulas and their strict comparisons remain valid. The asymptotics use \(k\) fixed and \(a/R\to\infty\), without assuming a simultaneous limit in polynomial degree. No comparison is asserted uniformly in unbounded \(k\). All capacities are logarithmic capacities of plane compact sets.

## Proof
**1. Ransford normalization.** For monic \(p\) of degree \(n\), its derivative divided by \(n\) runs over all monic polynomials of degree \(n-1\). The inequality
\[
\operatorname{cap}(K)^n\ge(\pi n)^{-1/2}\inf_{p\text{ monic},\deg p=n}\|p'\|_{L^2(K)}
\]
therefore gives \(L_n\le\operatorname{cap}(K)\) with precisely the stated normalization.

**2. Symmetry and exact disk reduction.** Positive-area support makes the monic minimizer unique. Reflection \(z\mapsto-z\) preserves the domain and norm, so the minimizing monic polynomial of degree \(m=2k+\sigma\) has parity \(\sigma\). It is uniquely of the form \(q(z)=z^\sigma P(z^2-a^2)\), with \(P\) monic of degree \(k\).

Put \(\varepsilon=R/a\) and write \(P(t)=(2aR)^kQ(t/(2aR))\) with \(Q\) monic of degree \(k\). On the disk \(z=a+Rw\), where \(|w|<1\), one has
\[
\frac{z^2-a^2}{2aR}=w+\frac\varepsilon2w^2,
\qquad z^\sigma=a^\sigma(1+\varepsilon w)^\sigma.
\]
By reflection, the integral over the negative disk equals the positive-disk integral. Hence **exactly**, for every \(a>R\),
\[
\lambda_{2k+\sigma}=2R^2a^{2\sigma}(2aR)^{2k}
\min_{Q\ \mathrm{monic},\deg Q=k}\int_{|w|<1}
\left|(1+\varepsilon w)^\sigma Q\left(w+\frac\varepsilon2w^2\right)\right|^2dA(w).
\tag{1}
\]
This is a finite-dimensional Hilbert-space minimization, not a numerical approximation.

**3. Gram-matrix asymptotics with an error bound.** Set \(F_j^\varepsilon(w)=(1+\varepsilon w)^\sigma(w+\varepsilon w^2/2)^j\) for \(0\le j\le k\). The Gram matrix \(G_{ij}(\varepsilon)=\int_{|w|<1}F_i^\varepsilon\overline{F_j^\varepsilon}\,dA\) obeys
\[
G_{jj}(\varepsilon)=\frac\pi{j+1}+O_k(\varepsilon^2),\qquad
G_{ij}(\varepsilon)=O_k(\varepsilon)\quad(i\ne j).
\]
Indeed, \(F_j^\varepsilon=w^j+\sum_{h\ge1}c_{j,h}\varepsilon^hw^{j+h}\) with finitely many coefficients, and the disk moments satisfy \(\int_{|w|<1}w^u\overline{w}^v\,dA=\delta_{uv}\pi/(u+1)\). The coefficient of \(\varepsilon\) in each diagonal entry therefore vanishes. At \(\varepsilon=0\), \(G\) is positive diagonal, so its leading \(k\)-by-\(k\) block has a uniformly bounded inverse for sufficiently small \(\varepsilon\). Completing the square in the lower-degree coefficients of the monic \(Q\) shows that the minimum in (1) is the Schur complement
\[
G_{kk}-G_{k,<k}\,G_{<k,<k}^{-1}G_{<k,k}
=\frac\pi{k+1}+O_k(\varepsilon^2).
\]
For \(k=0\) there is no lower block, and the same conclusion follows directly. Substitution into (1) gives the claimed coefficient, including the relative \(O_k((R/a)^2)\) remainder.

**4. Capacity and parity.** For every \(z\in K_{a,R}\),
\[
|z^2-a^2|=|z-a||z+a|\le R(2a+R).
\]
Thus \(K_{a,R}\) lies in the closed lemniscate \(\{|z^2-a^2|\le R(2a+R)\}\), whose capacity, by the monic polynomial pullback law, is \(\sqrt{R(2a+R)}\). Therefore
\[
L_2=(4a^2R^2+2R^4)^{1/4}
\le\operatorname{cap}(K_{a,R})
\le\sqrt{R(2a+R)},
\]
and both endpoints are asymptotic to \(\sqrt{2aR}\). For \(n=2k+2\), the asymptotic norm gives
\[
L_{2k+2}^{4k+4}=4^{k+1}a^{2k+2}R^{2k+2}(1+O_k(\varepsilon^2)),
\]
so \(L_{2k+2}\sim\sqrt{2aR}\). For \(n=2k+1\),
\[
L_{2k+1}=\left(\frac{2(2k+1)4^k}{k+1}\right)^{1/(4k+2)}
 a^{k/(2k+1)}R^{(k+1)/(2k+1)}(1+O_k(\varepsilon^2)),
\]
whose ratio to \(\sqrt{2aR}\) tends to zero as \((R/a)^{1/(4k+2)}\).

**5. Exact first-three-degree bounds and nonmonotonicity.** The monic minimizers in degrees \(0,1,2\) are, respectively, \(1,z,z^2-a^2\): the average of \(z^2\) on either disk is \(a^2\), because all nonconstant analytic monomials have zero disk average. Direct disk moments yield
\[
\lambda_0=2\pi R^2,\quad
\lambda_1=2\pi R^2(a^2+R^2/2),\quad
\lambda_2=2\pi R^2(2a^2R^2+R^4/3).
\]
This yields \(L_3=(12a^2R^4+2R^6)^{1/6}\). The strict comparison follows by setting \(t=a/R\ge1\) and checking
\[
(4t^2+2)^3>(12t^2+2)^2
\]
for all \(t\ge1\), with \(L_2>L_1\) immediate.

## Verification
The accompanying self-contained Python program `verify.py` evaluates disk moment integrals and Schur complements with exact rational arithmetic; it checks the first-degree formulas, the strict low-degree comparison on exact sample parameters, the Gram reduction for degrees through a finite cutoff, and the approach to the large-separation constant. These finite computations are checks of algebra and normalization; the assertions for all fixed degrees follow from the proof above, not from enumeration.

## Relationship to prior work
Ransford, *A least-squares lower bound for capacity* (first publicly posted October 17, 2026), proves the general bound used here but does not evaluate its degree-by-degree behavior on widely separated unions of disks. Gustafsson–Putinar–Saff–Stylianopoulos (2009) study Bergman polynomials on general archipelagos and explicit polynomial lemniscates in the different regime of polynomial degree tending to infinity for fixed geometry. The exact polynomial-lemniscate pullback case is not the ordinary two-disk geometry. Kiro–Nishry (2025), Theorem 4.19 and Appendix B, bound two-disk Bergman polynomial norms with fixed geometry controls while polynomial degree tends to infinity; their constants depend on the separation cutoff and do not give the present fixed-degree large-separation parity law.

## Limitations
The asymptotic statements keep \(k\) fixed. The first-three-degree comparison permits tangency but not overlapping disks. Neither the limiting behavior as \(k\to\infty\) and \(a/R\to\infty\) simultaneously nor exact capacities at finite separation are determined. Earlier unindexed two-disk calculations may affect historical priority. Independent mathematical validation has not been performed.

## References
1. Thomas Ransford, *A least-squares lower bound for capacity*, first public version October 17, 2026. https://hub.valency.io/works/W_7er9kkad
2. B. Gustafsson, M. Putinar, E. B. Saff, and N. Stylianopoulos, *Bergman polynomials on an archipelago: Estimates, zeros and shape reconstruction*, Advances in Mathematics 222 (2009), 1405–1460. https://arxiv.org/abs/0811.1715
3. A. Kiro and A. Nishry, *Integer-valued polynomials satisfying growth constraints* (2025), Theorem 4.19 and Appendix B. https://arxiv.org/html/2508.17335v1
