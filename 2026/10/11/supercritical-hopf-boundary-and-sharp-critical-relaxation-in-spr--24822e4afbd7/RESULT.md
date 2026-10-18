# Supercritical Hopf boundary and sharp critical relaxation in Sprott case F

## Finding
For every fixed \(b>0\), Sprott's quadratic case-F flow
\[
\dot x=y+z,\qquad \dot y=-x+ay,\qquad \dot z=x^2-bz
\]
has a **nondegenerate supercritical Hopf bifurcation at \(a=0\)**. With the convention \(q=(1,i,0)\) for the critical right eigenvector and the standard Hopf formula, its first Lyapunov coefficient is
\[
\ell_1(b)=-\frac{2b}{(b^2+1)(b^2+4)}<0.
\]
There is consequently no generalized-Hopf degeneracy anywhere on the positive-damping Hopf boundary. For sufficiently small \(a>0\) there is a unique small periodic orbit, orbitally asymptotically stable, satisfying
\[
\max_t \sqrt{x(t)^2+y(t)^2}
=\sqrt{\frac{(b^2+1)(b^2+4)}{b}\,a}+O_b(a),
\qquad P=2\pi+O_b(a).
\]
At the boundary \(a=0\), the origin is locally asymptotically stable although its linearization has the imaginary pair \(\pm i\). For every sufficiently small nonstationary forward trajectory not belonging to the one-dimensional strong-stable manifold, the **sharp asymptotic** is
\[
\lim_{t\to\infty}t\bigl(x(t)^2+y(t)^2\bigr)=\frac{(b^2+1)(b^2+4)}b.
\]
The remaining sufficiently small trajectories on the strong-stable manifold decay exponentially.

## Assumptions and scope
The state lies in \(\mathbb R^3\), time is continuous, \(b>0\) is fixed, and \(a\) varies in a sufficiently small interval around zero depending on \(b\). A 'small orbit' lies in a sufficiently small neighborhood of the origin, not the full global phase portrait. The maximum in the amplitude formula is over one period. The strong-stable manifold is the invariant one-dimensional manifold tangent at the origin to the stable eigenline for eigenvalue \(-b\) at \(a=0\). All limits are for \(t\to+\infty\) and solutions initially in a suitably small forward-invariant neighborhood. Constants implicit in \(O_b\) may depend on fixed \(b\). For \(a<0\) sufficiently small, the origin is locally exponentially attracting; for \(a>0\) sufficiently small, it is unstable and the bifurcating stable cycle surrounds it locally.

## Proof
**1. Linear Hopf crossing.** At the origin the Jacobian and characteristic polynomial are
\[
J(a,b)=\begin{pmatrix}0&1&1\\-1&a&0\\0&0&-b\end{pmatrix},
\qquad \det(\lambda I-J)=(\lambda+b)(\lambda^2-a\lambda+1).
\]
For \(|a|<2\), the critical pair is \(a/2\pm i\sqrt{1-a^2/4}\), and the third eigenvalue is \(-b\). Therefore the real-part crossing derivative at \(a=0\) is exactly \(1/2\), and the remaining direction stays strongly stable.

**2. Reconstruct the cubic coefficient.** Put \(A=J(0,b)\), \(q=(1,i,0)^T\), and \(p=(1/2,i/2,1/[2(b-i)])^T\). They satisfy \(Aq=iq\), \(A^Tp=-ip\), and \(\bar p^Tq=1\). The symmetric quadratic term in the Taylor expansion \(F(u)=Au+B(u,u)/2\) is \(B(u,v)=(0,0,2u_xv_x)^T\); the cubic tensor vanishes. The standard complex Hopf-coefficient expression is
\[
G_{21}=\bar p^T\left[B\left(\bar q,(2iI-A)^{-1}B(q,q)\right)-2B\left(q,A^{-1}B(q,\bar q)\right)\right].
\]
Both resolvents exist since \(b>0\). Explicitly,
\[
A^{-1}B(q,\bar q)=(0,2/b,-2/b)^T,
\]
\[
(2iI-A)^{-1}B(q,q)=\left(-\frac{4i}{3(b+2i)},\frac{2}{3(b+2i)},\frac{2}{b+2i}\right)^T,
\]
and substitution simplifies exactly to
\[
G_{21}=-\frac{4i}{3(b+i)(b+2i)},\quad
\operatorname{Re}G_{21}=-\frac{4b}{(b^2+1)(b^2+4)},\quad
\operatorname{Im}G_{21}=-\frac{4(b^2-2)}{3(b^2+1)(b^2+4)}.
\]
With critical frequency one and the stated eigenvector convention, \(\ell_1=\operatorname{Re}G_{21}/2\), yielding the asserted strictly negative expression. As an independent second-order check, the local center-manifold graph at criticality begins
\[
z=\frac{(b^2+2)x^2-2bxy+2y^2}{b(b^2+4)}+O(\lVert(x,y)\rVert^3),
\]
and substitution into its quadratic invariance equation gives exact equality.

**3. Cycle and its physical amplitude.** Nonzero transversal crossing and \(\ell_1<0\) give a standard nondegenerate supercritical Hopf bifurcation. In a smooth complex center coordinate \(w=\rho e^{i\theta}\), the local radial equation takes the form
\[
\dot\rho=\tfrac a2\rho-\frac{2b}{(b^2+1)(b^2+4)}\rho^3+O_b(|a|\rho^3+\rho^4),
\]
so the nonzero small-cycle radius satisfies
\[
\rho^2=\frac{(b^2+1)(b^2+4)}{4b}\,a+O_b(a^{3/2}).
\]
The physical coordinate relation \((x,y)=(w+\bar w,i(w-\bar w))+O_b(|w|^2)\) gives \(x^2+y^2=4\rho^2+O_b(\rho^3)\), establishing the stated leading amplitude. Its period tends to \(2\pi\), and its two transverse exponents have negative real part for sufficiently small \(a>0\) (one is associated with the radial Hopf direction and the other with the persisting \(-b\) direction).

**4. Critical algebraic relaxation.** At \(a=0\), on a local center manifold
\[
\dot\rho=-c_b\rho^3+O_b(\rho^4),\qquad
c_b=\frac{2b}{(b^2+1)(b^2+4)}>0.
\]
For every nonzero sufficiently small center solution, \(\rho\downarrow0\), and differentiation of \(\rho^{-2}\) yields
\[
\frac{d}{dt}\rho^{-2}=2c_b+O_b(\rho),
\qquad \lim_{t\to\infty}\frac{\rho(t)^{-2}}{t}=2c_b.
\]
Thus \(t\rho(t)^2\to1/(2c_b)=(b^2+1)(b^2+4)/(4b)\). The stable-foliation theorem for a semisimple imaginary pair separated from the eigenvalue \(-b\) gives exponential tracking of center-manifold motion by all sufficiently small solutions. Exactly the solutions on the one-dimensional strong-stable leaf through the equilibrium have zero center asymptotic and instead decay exponentially. The physical projection \(x^2+y^2=4\rho^2+O_b(\rho^3)\), together with exponential tracking, yields the claimed time-weighted limit \(4/(2c_b)\). This also proves local asymptotic stability at the nonhyperbolic boundary.

## Verification
Run `python check_sprott_f.py` with Python 3 and SymPy installed. The standalone checker constructs the Jacobian, complex eigenvectors, bilinear tensor and Hopf resolvents, checks the normalization identities, verifies the real and imaginary parts of \(G_{21}\) as exact rational functions for symbolic \(b>0\), verifies the quadratic center-manifold invariance equation, and confirms the full characteristic polynomial. A successful run prints `PASS`. Independent numerical integration at \(b=1\) was used only as a sanity check of the local amplitude and critical-limit scale; it is not used to prove the infinite-time statements.

## Relationship to prior work
J. C. Sprott's 1994 article introduced and numerically investigated case F among simple quadratic chaotic systems, and the author's 2013 technical note displayed its two-parameter regions and the exact equations above. The 1994 source establishes the benchmark flow and numerical chaotic regimes, while the 2013 note supplies qualitative numerical parameter regions, not an exact symbolic all-positive-\(b\) Hopf coefficient or the critical decay constant. General Hopf and center-manifold theorems supply the method but do not themselves furnish the computed coefficient or the physical-coordinate asymptotic for this particular system. Other publicly indexed results checked for focus and Hopf behavior concern non-equivalent vector fields; titles alone do not establish novelty. Remaining coverage risk is that an unindexed analysis or a differently normalized account of case F may already state an equivalent calculation.

## Limitations
The theorem is **local in phase space and in \(a\)** and assumes fixed \(b>0\); it does not classify far-away cycles, hidden attractors, chaotic windows, basin boundaries, or behavior as \(b\to0\). The critical asymptotic does not hold on the exceptional strong-stable manifold, which has exponential decay. Numerical trajectories are not substitutes for the analytic center-manifold argument. This is a mathematical proof and self-review, **not independent validation**.

## References
1. J. C. Sprott, *Some simple chaotic flows*, Physical Review E 50 (1994), R647–R650, DOI `10.1103/PhysRevE.50.R647` (public issue date 1994-08-01); author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper212.pdf.
2. J. C. Sprott, *Dynamic Regions in Simple Chaotic Flows* (2013 technical note, modified 2014), https://sprott.physics.wisc.edu/technote/regions.htm.
3. *Andronov–Hopf Bifurcation*, Scholarpedia, https://www.scholarpedia.org/article/Hopf_bifurcation (standard coefficient convention and theorem).
