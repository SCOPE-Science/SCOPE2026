# A sharp Airy-edge law for four-periodic geometric weighted shifts

## Finding

Fix real parameters \(s,t>0\). Let \(T_{q,s,t}\) be the unilateral weighted shift on \(\ell^2(\mathbb N_0)\) given by
\[
T_{q,s,t}e_n=\sigma_n q^n e_{n+1},\qquad
(\sigma_0,\sigma_1,\sigma_2,\sigma_3)=(1,s,1,t),\quad
\sigma_{n+4}=\sigma_n,\quad 0<q<1.
\]
Write \(w(T)=\sup_{\|u\|=1}|\langle Tu,u\rangle|\) for the numerical radius, and set
\[
D=\sqrt{4+(s-t)^2},\qquad
L=\frac{s+t+D}{4},\qquad
\kappa=\frac{2stL}{(s+t)D}.
\]
Let \(a_{\mathrm{Ai}}>0\) denote the absolute value of the largest negative zero of the classical Airy function, uniquely characterized by \(\operatorname{Ai}(-a_{\mathrm{Ai}})=0\) and \(a_{\mathrm{Ai}}\approx2.338107410\). Then
\[
\boxed{\lim_{q\uparrow1}\frac{L-w(T_{q,s,t})}{(-\log q)^{2/3}}
 =a_{\mathrm{Ai}}\,\kappa^{1/3}.}
\]
Equivalently,
\[
w(T_{q,s,t})=L-a_{\mathrm{Ai}}\,\kappa^{1/3}(1-q)^{2/3}
+o_{s,t}((1-q)^{2/3}).
\]
Both the fractional exponent and the leading constant are sharp for every fixed pair \(s,t>0\). In the geometrically weighted unmodulated case, \(s=t=1\), the statement specializes to
\[
w(T_{q,1,1})=1-2^{-1/3}a_{\mathrm{Ai}}(1-q)^{2/3}
+o((1-q)^{2/3}).
\]

## Assumptions and scope

The Hilbert space is complex \(\ell^2(\mathbb N_0)\); the periodic weights \(1,s,1,t\) are strictly positive and remain **fixed** as \(q\uparrow1\). The theorem concerns the **infinite** compact operator at each \(0<q<1\), not just its finite sections. The period-four pattern and its indexing begin with the weight \(1\) between \(e_0\) and \(e_1\). The numerical radius is a scalar invariant, not the spectral radius of the nonnormal shift (which is zero for \(q<1\)). No claim is made about estimates uniform as \(s\) or \(t\) approaches zero.

## Proof

**1. Self-adjoint reduction and periodic upper edge.** Put \(\varepsilon=-\log q>0\) and
\[
J_\varepsilon=\tfrac12(T_{e^{-\varepsilon},s,t}+T_{e^{-\varepsilon},s,t}^*).
\]
Its only nonzero Jacobi entries are \((J_\varepsilon)_{n,n+1}=\sigma_n e^{-\varepsilon n}/2\). Rotation of the basis makes \(T\) unitarily equivalent to every \(e^{i\theta}T\), so the support-function formula for numerical radius gives \(w(T)=\lambda_{\max}(J_\varepsilon)\). The Jacobi matrix is compact for \(\varepsilon>0\), and its largest eigenvalue is positive; the Rayleigh maximum may be restricted to real nonnegative vectors because its off-diagonal entries are nonnegative.

Define
\[
r=\frac{s-t+D}{2}>0,\qquad r^2-(s-t)r=1,\qquad
\phi=(1,r,r,1)\text{ extended four-periodically}.
\]
For the two-sided undamped periodic Jacobi operator, direct substitution gives
\[
\frac{\sigma_n\phi_{n+1}+\sigma_{n-1}\phi_{n-1}}2=L\phi_n
\quad(n\in\mathbb Z),\qquad L=\frac{r+t}{2}.
\]
Positivity of the periodic \(\phi\), together with a square-completion and long periodic cutoffs, identifies \(L\) as the upper band edge of the undamped periodic operator. No Floquet asymptotic theorem is needed in the argument below.

**2. Exact ground-state energy.** Define four-periodic coefficients
\[
(m_0,m_1,m_2,m_3)=(1,r^2,r^2,1),\qquad
(c_0,c_1,c_2,c_3)=(r,sr^2,r,t),
\]
with \(m_n=\phi_n^2\), \(c_n=\sigma_n\phi_n\phi_{n+1}\), and \(c_{-1}=t\). The periodic eigenvector identity is precisely
\[
2Lm_n=c_{n-1}+c_n\qquad(n\ge0).
\]
For every real finitely supported vector \(u\), write \(u_n=\phi_n v_n\), extending \(v\) by zero beyond its support. An exact expansion of the quadratic forms yields
\[
\begin{split}
L\sum_{n\ge0}m_n v_n^2-\langle u,J_\varepsilon u\rangle
={}&\frac12\sum_{n\ge0}c_n e^{-\varepsilon n}(v_{n+1}-v_n)^2
+\frac t2v_0^2\\
&+\frac12\sum_{n\ge1}
\left[c_n(1-e^{-\varepsilon n})
+c_{n-1}(1-e^{-\varepsilon(n-1)})\right]v_n^2.
\end{split}
\tag{1}
\]
All terms on the right are nonnegative. By form continuity the identity extends to \(\ell^2\), and, in particular, \(0<w(T_{q,s,t})<L\). Define \(\mathcal Q_\varepsilon(v)\) to be the right side of (1), with mass \(\|v\|_m^2=\sum m_n|v_n|^2\). Consequently
\[
L-w(T_{e^{-\varepsilon},s,t})
=\inf_{v\ne0}\frac{\mathcal Q_\varepsilon(v)}{\|v\|_m^2}.
\tag{2}
\]

**3. The effective stiffness and the proper edge scale.** The resistance of one period and the mean mass are
\[
S=\frac2r+\frac1{sr^2}+\frac1t,
\qquad \bar m=\frac{1+r^2}{2}.
\]
For any five endpoint values, Cauchy--Schwarz gives the sharp cell inequality
\[
\sum_{k=0}^{3}c_k(v_{4j+k+1}-v_{4j+k})^2
\ge \frac{(v_{4j+4}-v_{4j})^2}{S},
\tag{3}
\]
with equality precisely when the four increments are proportional to \(1/c_k\). Therefore the effective continuum kinetic coefficient, *after mass normalization*, is
\[
\alpha=\frac{2}{S\bar m}=\frac4{(1+r^2)S}
=\frac{2st}{L(s+t)D}>0.
\tag{4}
\]
The last equality follows algebraically from \(r^2-(s-t)r=1\) and \(D=r+1/r\). Write \(h=\varepsilon^{1/3}\); then \(\varepsilon=h^3\). A vector spread across indices of order \(h^{-1}\) has discrete-gradient energy of order \(h^2\), whereas the first-order loss of Jacobi coupling, \(\varepsilon n\), is also of order \(h^2\). This balancing determines the noninteger exponent.

**4. Variational lower limit.** Consider a sequence \(h\downarrow0\) and normalized nonnegative vectors with \(\|v\|_m=1\) and \(\mathcal Q_{h^3}(v)\le Ch^2\). Such sequences exist by the recovery functions below; to take an actual minimizer, use the positive top eigenvector of compact \(J_{h^3}\). Equation (1) implies \(v_0^2=O(h^2)\) and, for every fixed \(R>0\),
\[
\sum_{0\le n\le R/h}|v_{n+1}-v_n|^2=O_R(h^2).
\tag{5}
\]
The potential coefficient in (1) is bounded below by a positive multiple of \(1-e^{-h^3(n-1)}\) for \(n\ge1\), uniformly over its four phases. Thus for fixed \(R>0\), after division by \(h^2\), its value is at least a positive multiple of \(R\) for all \(n\ge R/h\) when \(h\) is sufficiently small. Hence
\[
\limsup_{h\downarrow0}\sum_{n\ge R/h}m_n v_n^2\le\frac{C'}R,
\tag{6}
\]
which ensures tightness as \(R\to\infty\). Constants here depend only on the fixed parameters and the energy bound.

Define the continuous piecewise-linear interpolation \(f_h\) by
\[
f_h(4jh)=h^{-1/2}v_{4j},\qquad j=0,1,2,\ldots.
\]
Equations (3) and (5) give a uniform \(H^1\) bound on each compact interval; the boundary penalty gives \(f_h(0)\to0\). Along a subsequence, \(f_h\to f\) strongly in \(L^2_{\mathrm{loc}}\), uniformly on compact intervals, and weakly in \(H^1_{\mathrm{loc}}\). Within each four-site cell, differences from the interpolated endpoint are negligible in the normalized mass because their squared sum is \(O_R(h^2)\). Period averaging and (6) then give
\[
\bar m\int_0^\infty f(x)^2\,dx=1,\qquad f\in H_0^1(0,\infty).
\tag{7}
\]

On a bounded macroscopic interval \(0\le hn\le R\), the factors \(e^{-h^3 n}=1+O_R(h^2)\). Using (3) cellwise, then weak lower semicontinuity, yields
\[
\liminf_{h\downarrow0}\frac{1}{2h^2}
\sum_{n\ge0}c_ne^{-h^3n}(v_{n+1}-v_n)^2
\ge\frac2S\int_0^\infty|f'(x)|^2\,dx.
\tag{8}
\]
For the potential, the exact relation \(c_{n-1}+c_n=2Lm_n\) gives, uniformly on \(0\le hn\le R\),
\[
\frac{c_n(1-e^{-h^3 n})+c_{n-1}(1-e^{-h^3(n-1)})}{2h^2}
=Lm_n(hn)+O_R(h).
\tag{9}
\]
Strong local convergence and four-periodic averaging, followed by monotone passage \(R\to\infty\), show that the liminf of the potential divided by \(h^2\) is at least \(L\bar m\int_0^\infty x f(x)^2\,dx\). Combining (7)--(9) proves the lower bound
\[
\liminf_{\varepsilon\downarrow0}
\frac{L-w(T_{e^{-\varepsilon},s,t})}{\varepsilon^{2/3}}
\ge \inf_{\substack{f\in H_0^1(0,\infty)\\ f\ne0}}
\frac{\alpha\int|f'|^2+L\int x|f|^2}{\int|f|^2}.
\tag{10}
\]
Functions with infinite first moment are assigned infinite quotient.

**5. Matching recovery.** Take a nonnegative smooth compactly supported \(f\) on \([0,\infty)\) with \(f(0)=0\). Set \(v_{4j}=\sqrt h f(4jh)\). For each cell distribute the total increment between \(v_{4j}\) and \(v_{4j+4}\) according to the equality case of (3):
\[
v_{4j+k+1}-v_{4j+k}
=\frac{v_{4j+4}-v_{4j}}{S c_k},\qquad k=0,1,2,3.
\]
These cell values are nonnegative convex combinations of adjacent endpoints, and the resulting sequence is finitely supported. Standard Riemann sums, uniform Taylor bounds on its compact support, and the exact equality in (3) imply
\[
\begin{split}
\|v\|_m^2&\longrightarrow\bar m\int f^2,\\
\frac{\mathcal Q_{h^3}(v)}{h^2}
&\longrightarrow\frac2S\int|f'|^2+L\bar m\int x f^2.
\end{split}
\tag{11}
\]
Smooth nonnegative compactly supported Dirichlet functions are a form core for the limiting half-line operator with confining linear potential. Taking their infimum in (11) gives the reverse inequality in (10).

**6. Airy eigenvalue and constant.** The limit in (10)--(11) is the lowest eigenvalue of the half-line Sturm--Liouville operator
\[
-\alpha\frac{d^2}{dx^2}+Lx,
\qquad f(0)=0.
\]
After rescaling, its square-integrable ground state is proportional to
\[
\operatorname{Ai}\!\left((L/\alpha)^{1/3}x-a_{\mathrm{Ai}}\right),
\]
with eigenvalue \(a_{\mathrm{Ai}}\alpha^{1/3}L^{2/3}\). Substituting (4) gives \(a_{\mathrm{Ai}}\kappa^{1/3}\). Finally, \((-\log q)/(1-q)\to1\) as \(q\uparrow1\). This proves both asserted asymptotics.

## Verification

The standalone file `VERIFY.py` uses only Python's standard library. It checks, with exact rational arithmetic, the periodic eigenvector identity, the equality \(\alpha=2st/[L(s+t)D]\), the complete ground-state quadratic-form identity (1), and the sharp cellwise Cauchy equality (3) for rational parameter triples and finite trial vectors. Execute `python3 VERIFY.py`; expected output is `GEOMETRIC_FOUR_PERIODIC_AIRY_EDGE_EXACT_IDENTITIES_OK`. These finite identities corroborate the algebraic infrastructure; the infinite-dimensional asymptotic comes from the analytical compactness, lower-bound, and recovery arguments in the proof, not from numerical extrapolation.

## Relationship to prior work

Ghosh, Birbonshi and Ojha (2026) introduced the precise four-periodically modulated geometric weighted shift used here. Their Theorem 2.2 gives two-sided bounds; Theorems 2.5 and 2.12 address the degree-eight stationarity polynomial for a lower bound; and their Section 3 gives coupled entire-determinant recurrences and finite-section computations for the exact radius. Their full original arXiv HTML text does **not** give the \(q\uparrow1\) asymptotic, the Airy constant, or the periodic homogenized effective stiffness. The stronger determinant characterization at each fixed \(q\) is acknowledged but does not itself evaluate the singular limit.

The geometric unmodulated model and a determinant/bounds framework were developed by Chien and Nakazato (2009). Chakraborty and Ojha (2024/2025) considered the two-periodic specialization. Chakraborty, Ojha and Birbonshi (2022) and Undrakh and colleagues (2015) treat different periodic-tail or finite-prefix weighted shifts using exact polynomials. General discrete turning-point/Airy methods, including Fedotov and Klopp (2019), motivate the analytic context, but the present explicit coefficient is derived directly from the operator's ground-state form and four-edge cell resistance.

## Limitations

This is an exact first-order *asymptotic* statement, not a closed formula at a fixed \(q\), and it supplies neither a quantitative remainder bound nor uniformity as \(s,t\) vary toward degenerate parameter values. The source's lower-bound polynomial uniqueness questions and behavior of individual zeros of the entire function are not resolved. A broader general theorem on periodic Jacobi homogenization might independently imply the Airy limit after additional identification of the boundary condition and effective coefficient; no such prior coverage was established in the inspected sources. Independent assessment of originality and proof is outstanding.

## References

1. A. Ghosh, R. Birbonshi, S. Ojha, *On the numerical radius of a class of weighted shift operators* (first publicly posted 18 August 2026), arXiv:2608.17486, https://arxiv.org/html/2608.17486v1.
2. M.-T. Chien and H. Nakazato, *The numerical radius of a weighted shift operator with geometric weights*, Electronic Journal of Linear Algebra **18** (2009), DOI:10.13001/1081-3810.1293, https://journals.uwyo.edu/index.php/ela/article/download/587/587/587.
3. B. Chakraborty and S. Ojha, *On the numerical radius of weighted shift operators with generalized geometric weights*, Journal of Mathematical Analysis and Applications **543** (2025), article 129021, DOI:10.1016/j.jmaa.2024.129021.
4. B. Chakraborty, S. Ojha, R. Birbonshi, *Numerical radii of weighted shift operators using determinantal polynomials*, Operators and Matrices **16** (2022), 1155–1174, DOI:10.7153/oam-2022-16-75, https://files.ele-math.com/articles/oam-16-75.pdf.
5. H. Undrakh, H. Nakazato, O. Vandanjav, M.-T. Chien, *The numerical radius of a weighted shift operator*, Electronic Journal of Linear Algebra (2015), https://journals.uwyo.edu/index.php/ela/article/download/1617/1617/1617.
6. A. Fedotov and F. Klopp, *The complex WKB method for difference equations and Airy functions*, SIAM Journal on Mathematical Analysis (2019), DOI:10.1137/18M1228694.
