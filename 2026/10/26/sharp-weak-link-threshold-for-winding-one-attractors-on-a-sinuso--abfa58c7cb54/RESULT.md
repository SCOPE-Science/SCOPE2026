# Sharp weak-link threshold for winding-one attractors on a sinusoidal cycle

## Finding
Consider an attractive sinusoidal phase network on a cycle with \(n\ge5\) vertices, with \(n-1\) edge strengths equal to \(1\), one exceptional edge strength \(0<w\le1\), and a fixed discrete step \(0<h<1/4\). Among stationary configurations whose principal oriented edge increments have winding \(+1\), **there is exactly one linearly attracting phase class if and only if \(w>w_c(n)\)**; the reflected winding \(-1\) has the same classification. Here \(m=n-1\), and the unique number \(t_m\in(\pi/(m-1),\pi/2)\) solving
\[
\tan t_m=m\tan\!\left(\frac{\pi+t_m}{m}\right)
\]
determines the sharp threshold
\[
w_c(n)=\frac{\sin((\pi+t_m)/m)}{\sin t_m},\qquad 0<w_c(n)<1.
\]
At \(w=w_c(n)\) the winding-one attracting branch and an index-one saddle branch collide in a nondegenerate saddle-node (and likewise for winding \(-1\)); at smaller positive weights no **linearly attracting** winding-one or winding-minus-one phase class exists. For \(w_c(n)<w\le1\), each of these two winding sectors contains exactly one linearly attracting configuration and one associated index-one saddle of the specified equal-strong-edge form.

Let \(t_*\in(0,\pi/2)\) be the unique solution of \(\tan t_*=\pi+t_*\). As \(m=n-1\to\infty\),
\[
w_c(n)=\frac{\sec t_*}{m}-\frac{\sec t_*(\pi+t_*)^2}{6m^3}+O(m^{-5}),
\qquad \sec t_*\approx 4.6033388488.
\]
The edge-defect threshold is therefore of order \(1/n\) with an explicit two-term correction. The classification concerns hyperbolic **stationary phase classes** in winding \(\pm1\), not every attractor or every winding sector.

## Assumptions and scope
Label vertices \(0,1,\ldots,n-1\) cyclically. The edge from \(j\) to \(j+1\pmod n\) has strength \(a_j=1\) for \(0\le j<n-1\), and \(a_{n-1}=w\). For phases \(\theta\in(\mathbb R/2\pi\mathbb Z)^n\), the dynamics is
\[
\theta_j^+=\theta_j+h\sum_{k:\{j,k\}\in E}a_{jk}\sin(\theta_k-\theta_j)\pmod{2\pi}.
\]
Quotient by simultaneous phase rotation. Define oriented principal increments \(d_j=\operatorname{Arg}(e^{i(\theta_{j+1}-\theta_j)})\in(-\pi,\pi)\) when no edge is antipodal. Their winding is \(q=(2\pi)^{-1}\sum_{j=0}^{n-1}d_j\in\mathbb Z\). Linearly attracting means all eigenvalues of the derivative restricted to the common-phase quotient have modulus strictly less than one. Saddle index means the number of derivative eigenvalues outside the closed unit disk, counted with multiplicity. The distinguished family described below lies strictly inside the principal-increment domain. We exclude configurations with antipodal principal-edge ambiguity from the winding assertion; none can be a linearly attracting stationary class for this model.

## Proof
**1. Stationarity and an exact Hessian test.** Let \(B\) be the cyclic incidence matrix and \(d=B^T\theta\) modulo \(2\pi\). The smooth potential is
\[
V(\theta)=-\sum_{j=0}^{n-1}a_j\cos d_j.
\]
Its gradient is \(\nabla V=B(a_j\sin d_j)_j\), and the stated dynamics is \(\theta^+=\theta-h\nabla V(\theta)\) modulo \(2\pi\). Each component of \(h\nabla V\) has modulus at most \(2h<1/2\), so a fixed point modulo \(2\pi\) is precisely a zero of \(\nabla V\). The kernel of the incidence matrix is the constant-edge-current line. Hence every stationary configuration satisfies
\[
a_j\sin d_j=J \quad(0\le j<n)
\]
for some real current \(J\). The Hessian quadratic form at a stationary point is
\[
\langle\xi,D^2V\,\xi\rangle=\sum_{j=0}^{n-1}a_j\cos d_j\,(\xi_{j+1}-\xi_j)^2.
\]
The vector of edge differences \(\Delta_j=\xi_{j+1}-\xi_j\) ranges over exactly the codimension-one space \(\sum_j\Delta_j=0\). The graph Laplacian bound gives \(\|D^2V\|\le4\); therefore, for \(0<h<1/4\), the derivative \(I-hD^2V\) is strictly contracting on the rotation quotient exactly when the Hessian is positive definite there. A negative Hessian eigenvalue gives an unstable derivative eigenvalue above \(1\), while a zero Hessian eigenvalue gives a neutral multiplier \(1\).

**2. Positive-definiteness forces equal strong-edge increments.** If two edges have negative cosine, choose an edge-difference perturbation supported on those two edges with values \(+1,-1\); its quadratic form is negative. If a strong edge has negative cosine and another strong edge has positive cosine, their sine values agree and their cosine magnitudes agree, so this two-edge perturbation has quadratic form zero. If any strong edge has zero cosine then \(|J|=1\); since \(w\le1\), necessarily \(w=1\), and every edge has zero cosine, again excluding positive definiteness. Consequently every linearly attracting stationary class has positive cosine on all \(m=n-1\) strong edges, and hence their oriented principal increments all equal one value \(\alpha\in(-\pi/2,\pi/2)\). For winding \(+1\), the common current must be positive (otherwise every principal increment is negative), so \(\alpha\in(0,\pi/2)\) and the exceptional increment is \(\beta\in(0,\pi)\). The winding condition and equal-current condition become
\[
m\alpha+\beta=2\pi,\qquad \sin\alpha=w\sin\beta.
\]
Thus \(\alpha=(2\pi-\beta)/m\) and \(w=f_m(\beta):=\sin((2\pi-\beta)/m)/\sin\beta\). For \(m\ge4\), this parametrizes \(0<\beta<\pi\) with \(0<\alpha<\pi/2\). Any such pair reconstructs a stationary phase class uniquely up to rotation.

**3. Exactly one fold and its stability.** The function \(f_m\) tends to \(+\infty\) as \(\beta\to0^+\) or \(\beta\to\pi^-\). Differentiating,
\[
\frac{f_m'(\beta)}{f_m(\beta)}=-\frac{\cot\alpha}{m}-\cot\beta.
\]
Because \(\cot\alpha>0\), a critical point requires \(\beta>\pi/2\). Put \(t=\pi-\beta\). Its critical equation is \(\tan t=m\tan((\pi+t)/m)\). On \(0<t<\pi/2\), let \(G(t)=\tan t-m\tan((\pi+t)/m)\). We have \(G(0)<0\), \(G(t)\to+\infty\) at the right endpoint, and
\[
G'(t)=\sec^2t-\sec^2((\pi+t)/m).
\]
It is negative on \(t<\pi/(m-1)\), positive thereafter. Thus there is precisely one critical point \(t_m\in(\pi/(m-1),\pi/2)\), and it is the nondegenerate global minimum of \(f_m\). Since \(f_m(2\pi/(m+1))=1\) and this parameter is not the minimizer (its \(\beta<\pi/2\)), \(0<w_c(n)<1\).

For these configurations, writing \(c=\cos\alpha>0\), the constrained Hessian form is
\[
Q(\Delta_1,\ldots,\Delta_m)
=c\sum_{j=1}^m\Delta_j^2+w\cos\beta\left(\sum_{j=1}^m\Delta_j\right)^2.
\]
Its inertia has \(m-1\) positive directions and one direction with sign \(\operatorname{sgn}(c+mw\cos\beta)\). The identity
\[
\frac{f_m'(\beta)}{f_m(\beta)}=-\frac{c+mw\cos\beta}{m\sin\alpha}
\]
therefore shows that the lower-\(\beta\) root of \(f_m(\beta)=w\) is linearly attracting and the upper-\(\beta\) root has precisely one unstable direction. These exist exactly for \(w>w_c(n)\). At the minimum, the distinguished eigenvalue is zero. Differentiating the logarithmic derivative and using \(t_m>\alpha_m\) gives
\[
f_m''(\pi-t_m)=w_c(n)\left(\frac1{\sin^2t_m}-\frac1{m^2\sin^2\alpha_m}\right)>0,
\qquad \alpha_m=(\pi+t_m)/m.
\]
This proves the ordinary saddle-node: for \(w\downarrow w_c(n)\) the two branches separate in \(\beta\) by \(2\sqrt{2(w-w_c(n))/f_m''(\pi-t_m)}+O(w-w_c(n))\). Reflection \(\theta\mapsto-\theta\) proves the winding \(-1\) assertion. Since step size controls the derivative directly, the threshold is independent of \(h\) throughout the stated range.

**4. Large-cycle law.** The limiting equation \(\tan t=\pi+t\) has exactly one solution in \((0,\pi/2)\), since its left side minus its right side starts negative and increases strictly after \(0\). The implicit-function theorem, using the variable \(1/m^2\), yields
\[
t_m=t_*+\frac{\pi+t_*}{3m^2}+O(m^{-4}).
\]
Indeed, \(m\tan((\pi+t)/m)=(\pi+t)+(\pi+t)^3/(3m^2)+O(m^{-4})\), and \(\tan t_* - (\pi+t_*)=0\) implies \(\sec^2t_*-1=\tan^2t_*=(\pi+t_*)^2\). Finally,
\[
w_c(n)=\frac{\sin((\pi+t_m)/m)}{\sin t_m}
=\frac1m\frac{\pi+t_*}{\sin t_*}-\frac{(\pi+t_*)^3}{6m^3\sin t_*}+O(m^{-5}),
\]
because \((\pi+t)/\sin t\) has zero first derivative at \(t=t_*\). Since \((\pi+t_*)/\sin t_*=\sec t_*\), the stated expansion follows.

## Verification
Run `python checker.py` with Python 3 and NumPy. The checker numerically brackets the unique critical equation, tests both branches against equal-current equations, constructs physical weighted graph Hessians, checks their nonzero spectral signs for eight cycle sizes, and compares the two-term large-size expansion. It records only finite diagnostics; every universal quantifier and the \(O(m^{-5})\) statement follow from the analytic proof above. The generated `checker_output.txt` records the executed tests.

## Relationship to prior work
The reciprocal discrete phase map and quotient potential follow the general framework of Buescu, D'Aniello, and Oliveira (2026, Sections 2 and 5.5). Their later paper with Oliveira on rings studies equal edge weights and repulsive sine interactions and proves almost-global convergence, not the weak-link attractive winding-one threshold. Delabays, Coletta, and Jacquod (2016, Section IV) establish loop-current and one-obtuse-edge structural restrictions for cycles of common coupling strength with possibly nonzero frequency injections; these statements do not give a defect-weight critical value. Manik, Timme, and Witthaut (2017, Sections V–VII) study general weighted cycle flows and count normal-operation states, but their normal-operation theorem assumes all cosines positive and does not provide the explicit sharp defect threshold where the attracting family persists with one obtuse edge or its large-cycle asymptotic. In all cases the broad current-conservation and Hessian framework is prior knowledge; the claim here is the precise weighted-one-edge classification and the singular threshold law, not that general framework.

## Limitations
The result concerns identical frequencies, an attractive sinusoidal interaction on a single cycle with one exceptional edge, \(n\ge5\), and \(0<h<1/4\). It classifies linearly attracting stationary configurations only in the principal-increment winding sectors \(q=\pm1\), and identifies a corresponding saddle branch. It neither classifies all other winding sectors, all unstable states, nonstationary attractors, basin volumes, nor nonlinear behavior exactly at the neutral fold. The explicit weak-edge threshold can be derived within general weighted cycle-flow formalisms; priority over every possible uninspected specialization has not been established.

## References
1. J. Buescu, E. D'Aniello, H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks* (2026), arXiv:2610.10993v1, first public 2026-10-07, https://arxiv.org/html/2610.10993v1 .
2. J. Buescu, H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings* (2026), arXiv:2610.19953v1, first public 2026-10-14, https://arxiv.org/html/2610.19953v1 .
3. R. Delabays, T. Coletta, P. Jacquod, *Multistability of Phase-Locking and Topological Winding Numbers in Locally Coupled Kuramoto Models on Single-Loop Networks* (2016), arXiv:1512.04266v2, https://arxiv.org/html/1512.04266v2 .
4. D. Manik, M. Timme, D. Witthaut, *Cycle flows and multistability in oscillatory networks*, Chaos 27, 083123 (2017), https://grk2767.tu-dresden.de/files/user/chair_nd/CFND_Publications/Manik_Chaos_2017.pdf .
