# Exact echo-attenuation bias and the nonuniform-grid positivity frontier for Lie splitting

## Finding
Consider the free-diffusion Bloch–Torrey equation on the line,
\[
\partial_t m=D\partial_{xx}m-i g(t)x m,\qquad m(0,x)=1,\quad D>0,
\]
where the real gradient \(g\) is constant with value \(g_j\) on each of \(N\ge2\) intervals of arbitrary durations \(h_j>0\). Let \(q_0=0\), \(q_j=\sum_{k=1}^j h_k g_k\), and impose the echo condition \(q_N=0\). Compare the exact phase-then-diffusion and diffusion-then-phase Lie products, using exact subflows and the same integrated gradient on each interval. Their respective final amplitudes are \(S_R=e^{-D R}\) and \(S_L=e^{-D L}\), while the true signal is \(S_*=e^{-D I}\), with
\[
I=\frac13\sum_{j=1}^N h_j(q_{j-1}^2+q_{j-1}q_j+q_j^2),\quad
R=\sum_{j=1}^N h_jq_j^2,\quad L=\sum_{j=1}^N h_jq_{j-1}^2.
\]
Set \(E=\frac16\sum_{j=1}^Nh_j(q_j-q_{j-1})^2\) and \(J=\frac12\sum_{i=1}^{N-1}(h_i-h_{i+1})q_i^2\). The **exact log-attenuation errors** satisfy
\[
R-I=E+J,\qquad L-I=E-J.
\]
The two Lie orders have equal final echo amplitudes for **every** piecewise-constant echo gradient if and only if all durations are equal. On this unique class of grids, both overattenuate by the same strictly positive logarithmic amount (unless the gradient is zero):
\[
R-I=L-I=\frac{h^2}{6}\int_0^T g(t)^2\,dt.
\]
For arbitrary durations, there is a complete linear-time criterion for **universal nonunderattenuation** of each Lie order. Put \(n=N-1\), and define real symmetric tridiagonal matrices \(T_R,T_L\) of size \(n\), whose nonzero entries are
\[
(T_R)_{ii}=2h_i-h_{i+1},\qquad (T_L)_{ii}=2h_{i+1}-h_i,\qquad
(T_R)_{i,i+1}=(T_L)_{i,i+1}=-\frac{h_{i+1}}2.
\]
The right, respectively left, order overattenuates or reproduces the exact signal **for every echo gradient** precisely when \(T_R\), respectively \(T_L\), is positive semidefinite. Each can be tested using the leading-minor recurrence \(\Delta_0=1\), \(\Delta_1=a_1\),
\[
\Delta_k=a_k\Delta_{k-1}-\frac{h_k^2}{4}\Delta_{k-2}\qquad(2\le k\le n),
\]
with \(a_i\) the corresponding diagonal. The exact criterion is \(\Delta_i>0\) for \(1\le i<n\) and \(\Delta_n\ge0\); for \(n=1\), simply \(\Delta_1\ge0\). For two steps, simultaneous nonunderattenuation holds if and only if
\[
\frac12\le\frac{h_1}{h_2}\le2.
\]
This neighboring-ratio test is **not sufficient** once three steps are allowed: with \((h_1,h_2,h_3)=(1,2,1)\) and echo knots \((q_0,q_1,q_2,q_3)=(0,2,1,0)\), \(I=19/3\) but \(R=6\), so the right-order product underattenuates; reversing the two interior knots gives the same strict underattenuation for the left-order product.

## Assumptions and scope
All assertions hold for every integer \(N\ge2\), every positive duration vector, every real piecewise-constant gradient, and \(D>0\). Signals are final scalar spatially uniform echoes (\(q_N=0\)) on the whole line; the initial constant magnetization is bounded, although not square-integrable. There are no boundaries, radiofrequency pulses, advection, relaxation, or spatially varying coefficients. The numerical products use exact analytic phase and diffusion subflows rather than approximate spatial discretizations. The sign convention \(R-I>0\) denotes excess attenuation because \(S_R<S_*\).

## Proof
**Exact and split solutions.** For \(m(t,x)=e^{-iG(t)x-DH(t)}\), the Bloch–Torrey equation reduces to \(G'(t)=g(t)\), \(H'(t)=G(t)^2\), with zero initial values. Consequently \(G(t_j)=q_j\), \(H(T)=I\), and the exact echo is \(e^{-DI}\). On a phase substep, multiplication by \(e^{-i h_j g_jx}\) sends a plane wave with spatial frequency \(-q_{j-1}\) to one with frequency \(-q_j\). On a diffusion substep, a plane wave of frequency \(-q\) is multiplied by \(e^{-Dh_jq^2}\). Composing phase before diffusion therefore yields \(R\); composing diffusion before phase yields \(L\). These identities hold at every finite grid size, without approximation.

**Bias decomposition.** On the \(j\)-th interval, \(G\) interpolates affinely from \(q_{j-1}\) to \(q_j\), so its exact squared integral is \(h_j(q_{j-1}^2+q_{j-1}q_j+q_j^2)/3\). The trapezoidal value exceeds this integral by \(h_j(q_j-q_{j-1})^2/6\). The right and left endpoint sums lie, respectively, \(\frac12\sum_jh_j(q_j^2-q_{j-1}^2)\) above and below that trapezoidal sum. Summation by parts, using \(q_0=q_N=0\), proves the formulas \(R-I=E+J\) and \(L-I=E-J\).

**Uniqueness and uniform-grid superconvergence.** The difference \(R-L=2J=\sum_{i=1}^{N-1}(h_i-h_{i+1})q_i^2\). The echo knots \(q_1,\ldots,q_{N-1}\) are arbitrary: each knot vector determines gradients \(g_j=(q_j-q_{j-1})/h_j\). Requiring \(R=L\) for every echo therefore forces each coefficient \(h_i-h_{i+1}=0\), and uniformity clearly suffices. On a uniform grid, \(J=0\) and \(E=h^2\int_0^Tg^2/6\). Hence both orders have exact second-order error in the log echo signal even though generic Lie product errors are first-order.

**Complete arbitrary-mesh classification.** Directly expanding the two exact errors shows
\[
3(R-I)=v^\top T_Rv,\qquad3(L-I)=v^\top T_Lv,\qquad
v=(q_1,\ldots,q_{N-1})^\top.
\]
Since all vectors \(v\) occur as echo knot vectors, universal nonunderattenuation is equivalent to the corresponding positive-semidefinite condition. Both tridiagonal matrices are irreducible because every off-diagonal entry is nonzero. If such a symmetric matrix is positive semidefinite, every *proper leading principal block* is positive definite: otherwise a null vector of a singular leading block, with nonzero final component due to irreducibility, coupled to the next coordinate would produce a negative quadratic form. Conversely, positive definiteness of the proper leading blocks and nonnegativity of the full determinant imply positive semidefiniteness by a Schur complement. The standard tridiagonal determinant expansion gives precisely the stated recurrence and strict/nonstrict sign test. For \(N=2\), the matrices are the scalars \(2h_1-h_2\) and \(2h_2-h_1\), establishing the sharp ratio interval. For \(N=3\), the stated explicit echo knots give the strict violations of the two quadratic forms; both adjacent ratios lie within the two-step interval, disproving a purely adjacent-ratio extension.

## Verification
The standalone Python 3 standard-library script `verify.py` evaluates both attenuation formulas, the bias decomposition, and the tridiagonal forms with exact rational arithmetic for many positive grids and echo knot vectors. It separately checks uniform-grid equality and the sharp two-step ratio and three-step counterexamples. The script reports 17,464 successful supplementary exact-rational checks. These finite tests are not used as proof of the universal statement; the analytical arguments above establish that.

## Relationship to prior work
Kaltenbacher, Muñoz, and Thalhammer (2026, arXiv:2610.04355) study general three-part Lie–Trotter splitting for non-autonomous Bloch–Torrey equations, including the longitudinal applied gradient and first-order solution convergence. In their original full text, the central Theorem 1 and experiments address general solution errors; the special echo observable, equal-order cancellation criterion, and arbitrary-grid tridiagonal attenuation-sign classification are not stated. The use of diffusion phase accumulation and gradient impulses predates this work, including the 1997 analysis of generalized NMR spin echoes (PMID 9405218). Standard trapezoidal quadrature identities are used as ingredients, not claimed as new. The result here combines them into a complete, sharp, arbitrary-grid, two-order echo-splitting design criterion.

## Limitations
This is an exact free-diffusion homogeneous-coefficient benchmark, not a convergence or stability theorem for a three-dimensional bounded-domain MRI discretization. Arbitrary radiofrequency rotation, imposed relaxation, boundaries, spatially varying diffusion, or temporal approximation of a non-piecewise-constant gradient are not covered. Echo amplitudes are not general magnetization norms. The split-order bias can change sign on nonuniform grids; the classification does not prescribe an optimal grid for all other error sources. An earlier equivalent exact-specialization result might exist in specialized NMR gradient-pulse literature not accessible in full text.

## References
- B. Kaltenbacher, P. Muñoz, and M. Thalhammer, *Operator splitting methods for non-autonomous evolution equations comprising three parts, with application to the Bloch-Torrey equation of MRI*, arXiv:2610.04355v1, publicly submitted 2026-10-03. https://arxiv.org/abs/2610.04355
- *A simple matrix formalism for spin echo analysis of restricted diffusion under generalized gradient waveforms*, *Journal of Magnetic Resonance* (1997), PubMed PMID 9405218. https://pubmed.ncbi.nlm.nih.gov/9405218/
- B. Fornberg, *Improving the Accuracy of the Trapezoidal Rule*, SIAM Review (2020), https://doi.org/10.1137/18M1229353 (quadrature context only; not a claim that the special mesh criterion is therein).
