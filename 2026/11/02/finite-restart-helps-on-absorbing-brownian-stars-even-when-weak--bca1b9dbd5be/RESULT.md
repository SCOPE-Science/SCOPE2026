# Finite restart helps on absorbing Brownian stars even when weak restart hurts

## Finding
For every integer \(q\ge4\), diffusivity \(D>0\), and scale \(\ell>0\), form a compact metric star with one edge of length \(\ell\) and \(q\) edges of length \(q\ell\). All outer leaves absorb, the central vertex obeys the Kirchhoff condition, and a Brownian particle starts at the center. Let \(T_r\) be its mean absorption time when independent Poisson resets to the center occur at rate \(r\ge0\). Then
\[
T_0=\frac{\ell^2(1+q^2)}{4D},\qquad
\left.\frac{dT_r}{dr}\right|_{r=0}=\frac{\ell^4q^2}{24D^2}>0.
\]
Nevertheless, at the fixed, explicit positive reset rate
\[
r_*=\frac{D(\log4)^2}{\ell^2},\qquad T_{r_*}<T_0
\quad\text{for every integer }q\ge4.
\]
The improvement becomes unbounded as the number of long arms grows:
\[
\frac{T_{r_*}}{T_0}\sim\frac{15}{2(\log4)^2q}\longrightarrow0
\qquad(q\to\infty).
\]
Consequently, a beneficial positive global minimizer exists even though every sufficiently small positive reset rate is harmful. Uniqueness of that positive minimizer is not asserted.

## Assumptions and scope
Distances along each edge are measured outward from the central vertex; the generator is \(D\,d^2/dx^2\). Functions are continuous at the center and satisfy \(\sum_j\partial_x f_j(0)=0\). The \(q+1\) terminal boundaries are absorbing (Dirichlet). Resetting is instantaneous, has no overhead, is independent of diffusion and absorption, and returns the particle exactly to the center. These assumptions define Kirchhoff Brownian motion on a finite metric star. The theorem concerns its mean time until *any* leaf is reached, rather than hitting a specified target leaf. Set \(\tau\) equal to the absorption time without resetting, \(F(s)=\mathbb E[e^{-s\tau}]\), and \(T_r=\mathbb E[\tau_r]\). The limiting values at \(r=0\) are understood by continuity.

## Proof
**1. Exit transform.** For general edge lengths \(L_i>0\), put \(k=\sqrt{s/D}\). By the backward equation, the exit transform \(u_i(x)=\mathbb E_{i,x}[e^{-s\tau}]\) solves \(D u_i''=su_i\), with \(u_i(L_i)=1\). If its common vertex value is \(F(s)\), the unique edge solution is
\[
u_i(x)=F(s)\cosh(kx)+\frac{1-F(s)\cosh(kL_i)}{\sinh(kL_i)}\sinh(kx).
\]
Summing its outward derivatives at the vertex gives the exact identity
\[
F(s)=\frac{\sum_i\operatorname{csch}(kL_i)}{\sum_i\operatorname{coth}(kL_i)}.
\]
For the stated star, with \(z=\ell\sqrt{s/D}\), this becomes
\[
F(s)=\frac{\operatorname{csch}z+q\operatorname{csch}(qz)}{\operatorname{coth}z+q\operatorname{coth}(qz)}.\tag{1}
\]
The finite compact graph with absorbing leaves has an almost surely finite absorption time and finite moments. At zero, the transform extends analytically.

**2. Moments and adverse weak-reset response.** Expand \(\operatorname{csch}z=z^{-1}-z/6+7z^3/360+O(z^5)\) and \(\operatorname{coth}z=z^{-1}+z/3-z^3/45+O(z^5)\) in (1):
\[
F(s)=1-\frac{\ell^2(1+q^2)}{4D}s
+\frac{\ell^4}{D^2}\left(\frac{1+q^4}{48}+\frac{(1+q^2)^2}{24}\right)s^2+O(s^3).
\]
Since \(F(s)=1-\mathbb E[\tau]s+\mathbb E[\tau^2]s^2/2+O(s^3)\),
\[
\mathbb E[\tau]=\frac{\ell^2(1+q^2)}{4D},\quad
\operatorname{Var}(\tau)=\frac{\ell^4(3+2q^2+3q^4)}{48D^2},\quad
\frac{\operatorname{Var}(\tau)}{(\mathbb E\tau)^2}
=1-\frac{4q^2}{3(1+q^2)^2}<1.
\]
The renewal decomposition at the first reset gives, for \(r>0\),
\[
T_r=\frac{1-F(r)}{rF(r)}.
\tag{2}
\]
Differentiating its Taylor expansion yields
\[
T_r=T_0+\frac{\ell^4q^2}{24D^2}r+O(r^2).
\]
Thus resetting initially **increases** mean exit time for every positive integer \(q\).

**3. A fixed finite-rate improvement.** In (1) and (2), use
\(\operatorname{coth}x-\operatorname{csch}x=\tanh(x/2)\). This yields
\[
T_r=\frac{\ell^2}{Dz^2}
\frac{\tanh(z/2)+q\tanh(qz/2)}{\operatorname{csch}z+q\operatorname{csch}(qz)}.
\tag{3}
\]
Choose \(z=\log4\), so that \(r=r_*\). Now
\[
\tanh(z/2)=\frac35,\quad \operatorname{csch}z=\frac8{15},\quad
\tanh(qz/2)=\frac{4^q-1}{4^q+1},\quad
\operatorname{csch}(qz)=\frac{2\cdot4^q}{4^{2q}-1}.
\]
For \(q=4\), exact rational arithmetic in (3) gives
\[
T_{r_*}=\frac{\ell^2}{D}\frac{299421}{37000(\log4)^2},
\qquad T_0=\frac{17\ell^2}{4D}.
\]
The strict improvement is equivalent to \((\log4)^2>17613/9250\). Indeed the positive-term inverse-hyperbolic-tangent series gives
\[
\log2=2\sum_{j\ge0}\frac{3^{-2j-1}}{2j+1}
>\frac{56}{81}>\frac{69}{100},
\]
and hence \((\log4)^2>(69/50)^2=4761/2500>17613/9250\).

For every integer \(q\ge5\), the numerator of the fraction in (3) is strictly smaller than \(q+3/5\), while its denominator is strictly larger than \(8/15\). Using \((\log4)^2>19/10\),
\[
T_{r_*}<\frac{\ell^2}{D}\frac{15(q+3/5)}{8(\log4)^2}
<\frac{\ell^2}{D}\frac{75(q+3/5)}{76}
<\frac{\ell^2}{D}\frac{1+q^2}{4}=T_0.
\]
The last strict inequality is equivalent to \(19q^2-75q-26>0\), true at \(q=5\) (value \(74\)) and strictly increasing thereafter. This proves improvement for all claimed integers.

**4. Large-star limit and existence of a nonzero optimum.** In (3) with \(z=\log4\) fixed, \(q\operatorname{csch}(qz)=O(q4^{-q})\) and \(q\tanh(qz/2)=q+O(q4^{-q})\). Therefore \(T_{r_*}=\ell^2D^{-1}\,[15q/(8(\log4)^2)+O(1)]\), and division by the exact \(T_0\) establishes the stated asymptotic. Further, as \(r\to\infty\), \(F(r)\sim2e^{-z}/(q+1)\), so \(T_r\sim(q+1)e^z/(2r)\to\infty\). By continuity and \(T_{r_*}<T_0\), a global minimum is attained at a strictly positive finite rate. The proof does not count or uniquely determine its minimizers.

## Verification
The standalone `verify_star_restart.py` checks the exact rational \(q=4\) coefficient, the rational logarithm bounds, the all-integer comparison reduced to \(19q^2-75q-26>0\), the first two moments, and sample large-\(q\) asymptotics. It independently solves finite-state resolvent systems for subdivided star random walks whose generators converge to the Kirchhoff diffusion, confirming the continuum Laplace transform. Run `python verify_star_restart.py`; it requires Python 3, NumPy, and SciPy. These finite numerical checks are supplementary; the proof above covers every integer \(q\ge4\) and positive \(D,\ell\).

## Relationship to prior work
Evans and Majumdar (2011) established the Poisson-resetting first-passage renewal method for Brownian search. Kostrykin, Potthoff, and Schrader (2011) provided the rigorous metric-graph Brownian framework. Reuveni (2015) developed universal optimal-restart fluctuation identities. Chen and Huang (2021) demonstrated discontinuous restart transitions in two- and three-dimensional spherical shells, including the general warning that a coefficient of variation below one does not exclude beneficial finite resetting. Riascos and coauthors (2019/2020) gave spectral resetting formulas for *discrete-time network walks*, including Cayley trees. None of those inspected statements supplies the present finite metric-star length/multiplicity family, its positive initial derivative for every member, and its unbounded finite-rate improvement. The general renewal formula is borrowed mathematical machinery, not claimed as original. Other exact resetting solutions for branched or nearly one-dimensional geometries could affect historical priority.

## Limitations
This is an exact statement about a specifically scaled but infinite family of stars, not a sharp characterization of all length profiles or all reset rates. The theorem does not claim uniqueness of the globally optimal positive reset rate, nor a universal restart transition for arbitrary graphs. Kirchhoff transmission, equal diffusivity, absorbing leaves, instantaneous hub resetting, and zero reset overhead are essential. The gain becomes unbounded because the overall geometry grows with \(q\); it is not a fixed-total-length resource theorem. No independent validation has been performed.

## References
1. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704v1 (first public 2011-02-14), https://arxiv.org/abs/1102.2704 .
2. V. Kostrykin, J. Potthoff, and R. Schrader, *Brownian Motions on Metric Graphs*, arXiv:1102.4937 (first public 2011-02-24), https://arxiv.org/abs/1102.4937 .
3. S. Reuveni, *Optimal stochastic restart renders fluctuations in first passage times universal*, arXiv:1512.01600v1 (first public 2015-12-05), https://arxiv.org/abs/1512.01600 .
4. A. P. Riascos, D. Boyer, P. Herringer, and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568, https://arxiv.org/abs/1910.13568 .
5. H. Chen and F. Huang, *First passage of a diffusing particle under stochastic resetting in bounded domains with spherical symmetry*, arXiv:2109.11101, https://arxiv.org/abs/2109.11101 .
