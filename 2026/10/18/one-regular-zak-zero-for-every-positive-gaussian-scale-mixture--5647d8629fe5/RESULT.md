# One regular Zak zero for every positive Gaussian scale mixture

## Finding
Let \(\mu\) be any nonzero finite positive Borel measure on \((0,\infty)\) satisfying
\[
\int_{(0,1)}a^{-1/2}\,d\mu(a)<\infty,
\qquad
g_\mu(x)=\int_{(0,\infty)}e^{-ax^2}\,d\mu(a).
\]
For every \(h>0\), define
\[
Z_hg_\mu(t,\xi)=\sqrt h\sum_{k\in\mathbb Z}
     g_\mu(h(t-k))e^{2\pi i k\xi}.
\]
Then the *entire* zero set in \([0,1)^2\) is exactly
\[
\bigl\{(t,\xi):Z_hg_\mu(t,\xi)=0\bigr\}
   =\bigl\{(\tfrac12,\tfrac12)\bigr\}.
\]
The central zero is nondegenerate: the real Jacobian of \((\Re Z_hg_\mu,\Im Z_hg_\mu)\) with respect to \((t,\xi)\) has positive determinant there. More precisely, \(\partial_t\Re Z_hg_\mu<0\), \(\partial_\xi\Im Z_hg_\mu<0\), and both off-diagonal entries vanish at that point. Furthermore, \(\Im Z_hg_\mu(t,\xi)>0\) for \(0<t<1\) and \(0<\xi<1/2\), with the opposite sign for \(1/2<\xi<1\).

A consequence is that, for every integer \(q\ge2\) and every \(h>0\), the rectangular Gabor system
\[
\left\{e^{2\pi i n x/h}g_\mu(x-mh/q):m,n\in\mathbb Z\right\}
\]
is a frame of \(L^2(\mathbb R)\).

## Assumptions and scope
The measure need not have a density, compact support, finite moments, or a finite number of atoms. Positivity is essential to the argument; signed and complex mixtures are not covered. The stated integral condition ensures \(g_\mu\in L^1(\mathbb R)\cap L^\infty(\mathbb R)\), because
\[
\int_\mathbb R g_\mu(x)\,dx
 =\sqrt\pi\int_{(0,\infty)}a^{-1/2}\,d\mu(a)<\infty.
\]
Thus the Zak series converges absolutely and uniformly on the fundamental square and defines a continuous quasiperiodic function. Near its center the series may be differentiated termwise, including for measures unbounded at large precisions. The conclusion concerns the exact zero geometry and integer-oversampled Gabor lattices, not all nonintegral lattice densities or the maximal frame set.

## Proof
**1. Heat-kernel sector positivity.** Put \(K_s(y)=(4\pi s)^{-1/2}e^{-y^2/(4s)}\) and
\[
Q_s(t,\theta)=\sum_{k\in\mathbb Z}K_s(t-k)e^{ik\theta},
\qquad s>0.
\]
The series is a classical heat solution in \(t\): \(\partial_sQ_s=\partial_t^2Q_s\), with quasiperiodicity \(Q_s(t+1,\theta)=e^{i\theta}Q_s(t,\theta)\) and evenness of \(K_s\). Poisson summation gives the strictly positive boundary value
\[
Q_s(0,\theta)=\sum_{\ell\in\mathbb Z}e^{-s(\theta+2\pi\ell)^2}>0.
\]
For \(0<\theta<\pi\), the real-valued function \(u(s,t)=\Im Q_s(t,\theta)\), on \(0<t<1\), has zero initial trace as \(s\downarrow0\), left Dirichlet value zero, and right Dirichlet value \(\sin\theta\,Q_s(0,\theta)>0\). The strict parabolic maximum principle (or the strictly positive Dirichlet heat Poisson kernel) therefore gives \(u(s,t)>0\) for every \(s>0\) and \(0<t<1\). Conjugation yields the opposite sign for \(\pi<\theta<2\pi\).

**2. The half-frequency fiber.** For \(\theta=\pi\), the function \(v(s,t)=Q_s(t,\pi)\) is real, and symmetry pairing the terms indexed by \(k\) and \(1-k\) gives \(v(s,1/2)=0\) and \(v(s,1-t)=-v(s,t)\). On \(0<t<1/2\) it solves the heat equation with zero initial trace, positive boundary value \(v(s,0)=Q_s(0,\pi)>0\), and zero boundary value at \(1/2\). Strict positivity gives
\[
v(s,t)>0\quad(0\le t<1/2),\qquad
v(s,t)<0\quad(1/2<t\le1).
\]
At \(\theta=0\) the series is everywhere strictly positive. At \(t=0\), Poisson summation gives \(Q_s(0,\theta)>0\) for every \(\theta\). These cases exhaust the fundamental square and show that \(Q_s\) has only its central zero.

**3. Nondegeneracy.** The parabolic Hopf boundary lemma applied to the strictly positive solution \(v\) on \(0<t<1/2\) gives \(\partial_t Q_s(1/2,\pi)<0\). For an individual Gaussian \(H_b(t,\theta)=\sum_ke^{-b(t-k)^2}e^{ik\theta}\), differentiating its absolutely convergent series at the central zero gives
\[
\partial_tH_b(1/2,\pi)
 =-2ib\,\partial_\theta H_b(1/2,\pi),\qquad b>0.
\]
Both \(\partial_tH_b\) and \(\partial_\theta H_b/i\) are real there, hence \(\partial_\theta\Im H_b(1/2,\pi)=\partial_t\Re H_b(1/2,\pi)/(2b)<0\). The remaining two Jacobian entries vanish: \(H_b(t,\pi)\) is real for every \(t\), while \(\Re H_b(t,\theta)\) is even in \(\theta-\pi\) at the central point. Thus the two diagonal entries of the real Jacobian are strictly negative and its determinant is strictly positive.

**4. Passage to arbitrary positive mixtures.** For each \(a>0\), set \(b=ah^2\). The scaled Gaussian Zak term is \(\sqrt h H_b(t,2\pi\xi)=\sqrt h(4\pi s)^{1/2}Q_s(t,2\pi\xi)\), where \(s=1/(4b)\). Every strict sign statement in steps 1--3 has the *same orientation* for every \(a\); integration against nonzero positive \(\mu\) preserves it. Absolute convergence and Fubini follow from the integral condition. For the two central derivatives, small-\(a\) estimates follow from the Poisson series, with exponential decay in \(1/a\) at half-frequency; large-\(a\) estimates follow from the Gaussian series on a neighborhood of \(t=1/2\). This justifies differentiation under the integral and preserves both strictly negative diagonal derivatives. The asserted unique regular zero and strict sector signs follow.

**5. Integer oversampling.** Zak diagonalization of the Gabor system with time step \(h/q\) and frequency step \(1/h\) gives the continuous nonnegative fiber weight, up to a harmless fixed normalization,
\[
W(t,\xi)=\sum_{j=0}^{q-1}|Z_hg_\mu(t-j/q,\xi)|^2.
\]
Its terms cannot vanish simultaneously: each one has its only zero when its spatial argument is \(1/2\) modulo one, and two distinct shifts \(j/q\) cannot have that same argument. Thus \(W\) has positive minimum and finite maximum on the compact torus, proving the frame assertion by the standard Zak criterion.

**6. A class outside standard total-positivity arguments.** The two-scale mixture \(g(x)=e^{-x^2}+e^{-100x^2}\) belongs to the theorem but is not log-concave. At \(x=1/10\), writing \(u=e^{-1/100}\) and \(v=e^{-1}\), direct differentiation gives
\[
 gg''-(g')^2=-2u^2+\frac{4751}{25}uv-200v^2>0.
\]
Indeed, the elementary bounds \(0.99<u<1\) and \(1/3<v<2/5\) make the right-hand side strictly greater than \(-2-32+(4751/25)(0.99/3)>0\). Total positivity of order two would force log-concavity, so the earlier totally-positive unique-zero theorems do not directly cover this example. It is also not convex near the origin, as \(g''(0)=-202\).


The family also contains the inverse-multiquadric windows \(g(x)=(x^2+\rho^2)^{-\beta}\) for every \(\rho>0\) and \(\beta>1/2\), by the positive Laplace--Gamma representation
\[
(x^2+\rho^2)^{-\beta}=\frac1{\Gamma(\beta)}\int_0^\infty a^{\beta-1}e^{-\rho^2a}e^{-ax^2}\,da.
\]
The restriction \(\beta>1/2\) is exactly what makes the inverse-square-root integral finite near zero. These familiar rational/decay windows are examples of the broad mixture theorem, not claims of historical priority for their individual zero geometry.

## Verification
The accompanying standalone `verify.py` evaluates finitely many two- and three-scale mixtures over six choices of dilation, tests the strict signs on interior fibers and boundaries, checks the central zero and Jacobian, verifies the per-Gaussian derivative relation, and independently checks the explicit non-log-concavity witness. Run with `python verify.py`; it uses only the Python standard library. Its numerical comparisons do **not** prove the infinite-dimensional theorem; the proof above relies on heat-kernel positivity, the Hopf lemma, and justified positive integration.

## Relationship to prior work
Sun and Zhou establish unique simple Zak zeros and maximal frame sets for *individual* complex extended Gaussians (arXiv:2602.06641, first posted February 6, 2026). Janssen's earlier critical-density study includes individual Gaussians and a class of positive even windows with a convexity condition, which does not include the nonconvex mixture exhibited above. Kloos and Kloos--Stoeckler treat totally positive windows and exponential splines; the non-log-concave mixture cannot be covered by the total-positivity hypothesis. The new assertion is the stability of the **entire regular zero geometry** under arbitrary positive Gaussian scale mixing, including measures with continuous or unbounded support. The integer-oversampled frame implication itself is a classical Zak consequence, not asserted to be a new criterion.

## Limitations
No statement is made for signed mixtures, higher-dimensional Zak transforms, or general nonintegral Gabor densities. The literature search may have missed equivalent earlier results under heat-semigroup or completely-monotone nomenclature. The 2003 Janssen paper was compared directly with its published class assumptions; a 2017 paper on averaged totally positive functions was accessible by abstract but not in complete text, so historical priority remains a qualified assessment. No independent external validation has been performed.

## References
1. W. Sun and W. Zhou, *Frame Sets and Zeros of Zak Transforms of Extended Gaussians*, arXiv:2602.06641 (v1 February 6, 2026), https://arxiv.org/abs/2602.06641.
2. A. J. E. M. Janssen, *On Generating Tight Gabor Frames at Critical Density*, Journal of Fourier Analysis and Applications 9 (2003), 175--214, doi:10.1007/s00041-003-0011-3. Open text: https://pure.tue.nl/ws/files/3079889/Metis235352.pdf.
3. T. Kloos, *Zeros of the Zak Transform of Totally Positive Functions*, arXiv:1411.1539 (2014), https://arxiv.org/abs/1411.1539.
4. T. Kloos and J. Stoeckler, *Zak Transforms and Gabor Frames of Totally Positive Functions and Exponential B-Splines*, arXiv:1311.7359 (2013), https://arxiv.org/abs/1311.7359.
5. O. L. Vinogradov and A. Yu. Ulitskaya, *Zeros of the Zak Transform of Averaged Totally Positive Functions*, Journal of Approximation Theory (2017), doi:10.1016/j.jat.2017.06.001 (abstract inspected; full text not inspected).
