# Structural zero mode and quadratic center drift in a memristor hyperchaotic oscillator
## Finding
For the four-dimensional system printed as System (7) by Fu, Xu, and Xiao,
\[
\dot x=(\alpha+3\beta w^2)y+pxz+x,\qquad
\dot y=xy-xz-10x+z,
\]
\[
\dot z=x^2+qxy+w,\qquad \dot w=y,
\]
the equilibrium at the origin is not hyperbolic. Its exact characteristic polynomial is
\[
\chi_0(\lambda)=\lambda(\lambda^3+10\alpha\lambda-1).
\]
For every \(\alpha>0\), the zero eigenvalue is simple; the cubic factor has exactly one positive real root and one conjugate pair with negative real part. Thus the origin has one unstable direction, two stable directions, and one center direction.

The zero mode is nonlinear rather than accidentally neutral. With the center coordinate normalized by right and left zero eigenvectors, the reduced equation is
\[
\dot\xi=10p\,\xi^2+O(\xi^3).
\]
At the article's parameters \(\alpha=1/7\), \(\beta=2/7\), \(p=1/5\), and \(q=20\), this becomes
\[
\dot\xi=2\xi^2+O(\xi^3).
\]
Accordingly, on the local center branch approaching the origin from \(\xi<0\),
\[
\xi(t)\sim-\frac{1}{2t}.
\]
This exact local structure is incompatible with the source's reported spectrum of two nonzero complex-conjugate pairs at the origin.

## Assumptions and scope
The calculation uses the vector field and Jacobian printed in the cited article. The spectral statement assumes \(\alpha>0\). The nonzero quadratic center coefficient requires \(p\ne0\); the displayed numerical consequence uses the article's value \(p=1/5\). No conclusion is made here about trajectories far from the origin, the existence of the numerically displayed hyperchaotic attractor, circuit simulation, or the performance of the synchronization controller.

## Proof
At \(S_0=(0,0,0,0)\), the printed Jacobian specializes to
\[
J_0=\begin{pmatrix}
0&\alpha&0&0\\
-10&0&1&0\\
0&0&0&1\\
0&1&0&0
\end{pmatrix}.
\]
Direct determinant expansion gives
\[
\det(\lambda I-J_0)=\lambda(\lambda^3+10\alpha\lambda-1).
\]
The derivative of \(g(\lambda)=\lambda^3+10\alpha\lambda-1\) is \(3\lambda^2+10\alpha>0\), so \(g\) is strictly increasing. Since \(g(0)=-1\) and \(g(1)=10\alpha>0\), it has exactly one real zero \(r\in(0,1)\), and that zero is positive. Vieta's relation gives real part \(-r/2<0\) for the remaining conjugate pair. Because \(g(0)=-1\), the factor \(\lambda\) is simple.

A right zero eigenvector and a normalized left zero eigenvector are
\[
v=(1,0,10,0)^T,\qquad \ell=(1,0,0,-\alpha)^T,
\]
with \(J_0v=0\), \(\ell^TJ_0=0\), and \(\ell^Tv=1\). Let \(B=D^2f(0)\) denote the symmetric quadratic tensor of the vector field. Evaluation on the center direction gives
\[
B(v,v)=(20p,-20,2,0)^T.
\]
For a simple zero eigenvalue, projection of the quadratic center-manifold equation by \(\ell^T\) removes the range term and yields the normalized scalar coefficient
\[
\frac12\ell^TB(v,v)=10p.
\]
Hence \(\dot\xi=10p\xi^2+O(\xi^3)\). At \(p=1/5\), the coefficient is \(2\). Along the center branch with \(\xi<0\) that converges to the origin, \((-1/\xi)'=2+O(\xi)\), which gives \(\xi(t)\sim-1/(2t)\).

## Verification
The bundled verifier reconstructs \(\det(\lambda I-J_0)\) over exact rational arithmetic at \(\alpha=1/7\), checks both zero eigenvectors, evaluates the Hessian contraction exactly, and confirms the quadratic coefficient \(2\). As an independent algebraic consistency check on the same printed model, it also reconstructs the other equilibrium's characteristic polynomial
\[
\chi_1(\lambda)=\lambda^4+2\lambda^3+\frac{228}{5}\lambda^2+\frac{308}{5}\lambda-3
\]
at \(S_1=(-1,0,-5,-1)\).

## Relationship to prior work
The primary article prints the vector field, the Jacobian, and the equilibrium spectra. It reports at \(S_0\) two nonzero conjugate pairs, whereas the determinant of its displayed Jacobian vanishes identically at that equilibrium. Source-specific searches by title, DOI, exact equation fragments, equilibrium language, zero-eigenvalue terminology, and center-manifold terminology did not locate a published correction or a prior statement of the factorization and quadratic center coefficient. The closest published records found concern zero modes and center dynamics in different differential systems and do not imply this source-specific result.

## Limitations
This is a local theorem for the printed autonomous vector field. A nonhyperbolic equilibrium can coexist with remote chaotic or hyperchaotic invariant sets, so the result does not by itself invalidate the article's global numerical attractor plots. It also does not audit the controller equations or hardware model. The center coordinate is normalized by \(\ell^Tv=1\); under a different scalar coordinate the numerical coefficient changes covariantly, while its nonvanishing and the one-sided quadratic character remain invariant.

## References
Fu, Q.; Xu, X.; Xiao, C. *LQR Chaos Synchronization for a Novel Memristor-Based Hyperchaotic Oscillator*. Mathematics 2023, 11(1), 11. DOI: 10.3390/math11010011. First public version of record: 2022-12-20.
