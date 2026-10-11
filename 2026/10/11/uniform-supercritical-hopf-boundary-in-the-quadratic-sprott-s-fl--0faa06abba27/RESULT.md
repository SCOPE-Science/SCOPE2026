# Uniform supercritical Hopf boundary in the quadratic Sprott-S flow

## Finding
For every fixed \(a>0\), the upper equilibrium of the quadratic Sprott-S family
\[
\dot x=-x-ay,\qquad \dot y=x+z^2,\qquad \dot z=b+x
\]
undergoes a **nondegenerate supercritical Hopf bifurcation exactly at \(b=1/4\)**. Its first Lyapunov coefficient in the eigenvector normalization defined below is
\[
\boxed{\displaystyle l_1(a)=-\frac{\sqrt a(8a+1)}{(a+1)(4a+1)}<0.}
\]
The equilibrium is asymptotically stable for \(0<b<1/4\); it has a two-dimensional unstable subspace for \(b>1/4\). For each fixed \(a>0\), sufficiently close to but above \(b=1/4\), a locally unique, nonconstant, orbitally asymptotically stable periodic orbit bifurcates from this equilibrium. Its least period converges to \(2\pi/\sqrt a\) as \(b\downarrow1/4\). These conclusions hold for the entire positive \(a\)-axis, not just at selected numerical parameter values.

## Assumptions and scope
States \((x,y,z)\) and parameters \((a,b)\) are real. The theorem assumes \(a>0\), \(b>0\), and concerns the branch with **positive** equilibrium \(z\)-coordinate. The two equilibria are
\[
E_\pm(b)=(-b,b/a,\pm\sqrt b).
\]
"Locally unique" means unique modulo time translation among sufficiently small periodic orbits near the upper equilibrium at the Hopf point. The existence neighborhood in \(b\) is allowed to depend on \(a\). The first Lyapunov coefficient uses the standard multilinear Hopf formula and the explicit normalization below; its sign (and thus criticality) is intrinsic.

## Proof
**1. Exact stability boundary.** At \(E_+(b)\), the Jacobian and characteristic polynomial are
\[
A_b=\begin{pmatrix}-1&-a&0\\1&0&2\sqrt b\\1&0&0\end{pmatrix},\qquad
p_b(\lambda)=\lambda^3+\lambda^2+a\lambda+2a\sqrt b.
\]
The cubic Routh-Hurwitz conditions for all three eigenvalues to have negative real parts are \(a>0\), \(2a\sqrt b>0\), and \(a>2a\sqrt b\), equivalent to \(0<b<1/4\). At \(b_0=1/4\),
\[
p_{b_0}(\lambda)=(\lambda+1)(\lambda^2+a),
\]
so the spectrum is \(\{-1,i\sqrt a,-i\sqrt a\}\). When \(b>1/4\), the Routh table has two sign changes; there is one stable eigenvalue and one unstable complex-conjugate pair. Writing \(\omega=\sqrt a\), implicit differentiation of \(p_b(\lambda)=0\) along the eigenvalue branch through \(i\omega\) gives
\[
\left.\frac{d}{db}\operatorname{Re}\lambda(b)\right|_{b=b_0}=\frac{a}{a+1}>0.
\]
Thus the eigenvalue crossing is transversal for every \(a>0\).

**2. Exact cubic Hopf coefficient.** Translate by \(E_+(b_0)\). At the critical point the vector field is \(\dot u=Au+\tfrac12B(u,u)\), with
\[
A=\begin{pmatrix}-1&-\omega^2&0\\1&0&1\\1&0&0\end{pmatrix},\qquad
B(u,v)=(0,2u_3v_3,0)^\top.
\]
There are no cubic or higher terms. Choose the complex right eigenvector and normalized left eigen-row
\[
q=(i\omega,1-i/\omega,1)^\top,\qquad
\ell=\frac{(1,i\omega,1)}{2+2i\omega}.
\]
Direct calculation verifies \(Aq=i\omega q\), \(\ell A=i\omega\ell\), and \(\ell q=1\). Put
\[
G_{21}=\ell\left[B\!\left(\bar q,(2i\omega I-A)^{-1}B(q,q)\right)-2B\!\left(q,A^{-1}B(q,\bar q)\right)\right].
\]
The standard Hopf coefficient for this convention is \(l_1=\operatorname{Re}G_{21}/(2\omega)\). Evaluating the displayed rational matrix expression gives
\[
G_{21}=-\frac{2\omega(12\omega-5i)}{3(\omega-i)(2\omega-i)},\qquad
l_1=-\frac{\omega(8\omega^2+1)}{(\omega^2+1)(4\omega^2+1)}.
\]
Every numerator and denominator needed for this formula is nonzero at \(\omega>0\). The numerator of \(l_1\) is strictly negative and its denominator strictly positive.

**3. Periodic-orbit existence and stability.** The analytic vector field, simple imaginary pair, hyperbolic third eigenvalue, positive crossing derivative, and negative nonzero first Lyapunov coefficient satisfy the nondegenerate Hopf bifurcation theorem. Its supercritical branch exists on \(b>b_0\), is stable within the two-dimensional center dynamics, and is transversely stable because the third eigenvalue stays near \(-1\). Hence these cycles are orbitally asymptotically stable in the full three-dimensional flow. The frequency tends to \(\omega\), so their least periods tend to \(2\pi/\omega\). The local Hopf branch is unique up to phase in a sufficiently small neighborhood.

## Verification
The standalone `verify_hopf.py` uses exact SymPy algebra to verify the characteristic polynomials, three eigenvector relations, transversality, and the formula for \(l_1\) for symbolic positive \(\omega\). It also checks \(l_1(1)=-9/10\) as a specialization. To replay, install SymPy and execute `python verify_hopf.py` alongside this document. The proof of existence invokes the standard nondegenerate Hopf theorem; the checker is not itself a proof of that theorem.

## Relationship to prior work
Sprott (1994) introduced the quadratic flow and documented equilibria and numerical chaotic behavior. Sprott's 2013–2014 two-parameter atlas depicts regions of equilibrium, periodic and chaotic behavior numerically. Mendes, Lainscsek and Letellier (2021) discuss the jerk-equivalence and topological relationships of the original Sprott families, including case S, but not the displayed uniform Hopf coefficient. The present claim supplies an exact, all-positive-\(a\) bifurcation surface, direction, and local stable-cycle existence theorem. Its existence conclusion is not inferred merely from numerical parameter maps or stationary moment constraints.

## Limitations
The theorem is **local** to the positive-\(z\) equilibrium and to \(b=1/4\); it does not classify global attractors, prove chaotic dynamics, guarantee global continuation of the stable cycles, or assert uniqueness of periodic orbits away from a small Hopf neighborhood. It does not give a uniform positive parameter-neighborhood width for all \(a>0\). The coefficient depends on the displayed eigenvector normalization, though the sign does not. Historical priority remains subject to older or unindexed analyses of an equivalent jerk equation.

## References
1. J. C. Sprott, “Some simple chaotic flows,” *Physical Review E* **50** (1994), R647–R650, https://doi.org/10.1103/PhysRevE.50.R647 (published 1994-08-01).
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” 2013, revised 2014, https://sprott.physics.wisc.edu/technote/regions.htm.
3. E. M. A. M. Mendes, C. Lainscsek and C. Letellier, “Diffeomorphical equivalence vs topological equivalence among Sprott systems,” *Chaos* **31** (2021), 083126, https://doi.org/10.1063/5.0058330.
4. Standard nondegenerate Hopf bifurcation theorem and multilinear first-Lyapunov-coefficient formula (the formula used is displayed explicitly in the proof).
