# A half-Courant overlap barrier for additive two-corner fluxes

## Finding

For a natural two-component symmetrizable hyperbolic conservation law, an exact face flux assembled as a central contribution plus two *isolated* endpoint corrections acquires a missing nonlinear interaction term as soon as the two inward-moving contact waves overlap. The critical tangential Courant number is exactly \(1/2\), despite the ability to keep the maximum full characteristic Courant number below one.

Let \(L,v,\varepsilon>0\), let \(p_0,q_0,\alpha,\beta>0\), and let \(\Phi\) be a \(C^2\) scalar function on a rectangle containing the four states \((p_0+i\alpha,q_0+j\beta)\), \(i,j\in\{0,1\}\). Consider
\[
\partial_t\begin{pmatrix}p\\q\end{pmatrix}
+\partial_x\left[\varepsilon\Phi(p,q)\begin{pmatrix}1\\1\end{pmatrix}\right]
+\partial_y\begin{pmatrix}vp\\-vq\end{pmatrix}=0,
\]
with initial data independent of \(x\), given by
\[
p(y,0)=p_0+\alpha\mathbf 1_{\{y<0\}},\qquad
q(y,0)=q_0+\beta\mathbf 1_{\{y>L\}}.
\]
For \(0\le H\le L/v\), denote by \(I(H)\) either component of the exact space-time normal flux through the finite face \(x=0,\ 0\le y\le L\), integrated from \(t=0\) to \(H\). Write \(\Phi_{ij}=\Phi(p_0+i\alpha,q_0+j\beta)\), and define the mixed finite difference
\[
\Delta_\Phi=\Phi_{11}-\Phi_{10}-\Phi_{01}+\Phi_{00}.
\]
Then
\[
\boxed{I(H)=\varepsilon\left[LH\Phi_{00}+\frac{vH^2}{2}
(\Phi_{10}+\Phi_{01}-2\Phi_{00})
+v\left(H-\frac{L}{2v}\right)_+^2\Delta_\Phi\right].}
\]
The first two terms are exactly the central flux plus the two individual isolated-corner corrections; the final term is an exact corner-overlap defect. Additivity holds for every \(H\le L/(2v)\), and for \(H>L/(2v)\) it holds if and only if \(\Delta_\Phi=0\). For every nonzero mixed finite difference the critical value \(vH/L=1/2\) is sharp, and \(I(H)\) is \(C^1\) but not \(C^2\) there. On a connected open rectangular state domain, the isolated-corner rule is exact for all positive rectangles and all permitted times if and only if \(\Phi(p,q)=f(p)+g(q)\) for one-variable functions \(f,g\).

In particular, take \(\Phi(p,q)=pq\), \(p_0=q_0=\alpha=\beta=L=v=1\), \(\varepsilon=1/10\), and \(H=9/10\). The additive prediction is exactly \(171/1000\), while the true flux per component is \(187/1000\), a missing \(16/1000\). Every state has \(1\le p,q\le2\), the system is strictly hyperbolic in every spatial direction, and a common full characteristic-speed bound is \(\lambda=\sqrt{29}/5\). Its full Courant number obeys
\[
\lambda H/L=\frac{9\sqrt{29}}{50}<1.
\]
Thus the failure is not caused by exceeding the standard full-speed Courant-one bound.

## Assumptions and scope

The interface-normal flux refers to the physical flux of the displayed conservation law, not a particular reconstruction, limiter, machine-learned correction, or fully specified finite-volume time step. The comparison is to the mathematically defined *additive isolated-corner formula* using the same central constant state and two separate half-line vertex problems. The observed discrepancy does not by itself establish instability or incorrectness of a particular fully discrete solver. Initial data and the solution are constant in \(x\); the waves propagate in opposite tangential directions. For the strict-hyperbolicity assertion, the exhibited choice \(\Phi(p,q)=pq\) and positive states are essential. Exact flux formulas apply to all real-valued \(C^2\) functions \(\Phi\) and the specified contact-wave solution, even without strict hyperbolicity.

## Proof

**Exact solution.** Since the initial data do not depend on \(x\), the normal-flux derivative vanishes identically. The remaining equations are two scalar transport equations. Hence their exact weak solution is
\[
p(y,t)=p_0+\alpha\mathbf 1_{\{y<vt\}},\qquad
q(y,t)=q_0+\beta\mathbf 1_{\{y>L-vt\}}.
\]
It is obtained as the limit of smooth transported initial profiles and satisfies the conservation law distributionally. For \(0\le vt\le L\), the two excited subintervals within the face each have length \(vt\), and their overlap length is \((2vt-L)_+\). At each point the flux has the exact inclusion-exclusion expansion
\[
\Phi(p,q)=\Phi_{00}
 +(\Phi_{10}-\Phi_{00})\mathbf1_{\{y<vt\}}
 +(\Phi_{01}-\Phi_{00})\mathbf1_{\{y>L-vt\}}
 +\Delta_\Phi\mathbf1_{\{y<vt\}}\mathbf1_{\{y>L-vt\}}.
\]
Integrating over \(0\le y\le L\) gives the instantaneous scalar flux
\[
\varepsilon\left[L\Phi_{00}+vt(\Phi_{10}+\Phi_{01}-2\Phi_{00})
 +(2vt-L)_+\Delta_\Phi\right].
\]
The final term first becomes nonzero at \(T=L/(2v)\). Its time integral over \([0,H]\) is \(\varepsilon v(H-T)_+^2\Delta_\Phi\). This proves the claimed identity, sharp transition, and the jump \(2\varepsilon v\Delta_\Phi\) in the one-sided second derivatives at \(H=T\).

**Classification of exact additivity.** For \(H>T\), the prefactor multiplying \(\Delta_\Phi\) is positive, proving the fixed-rectangle necessity and sufficiency. For any \(C^2\) function on a connected open rectangle,
\[
\Delta_\Phi=\int_{p_0}^{p_0+\alpha}\int_{q_0}^{q_0+\beta}
\partial_{pq}\Phi(s,t)\,dt\,ds.
\]
If this vanishes for all sufficiently small rectangles, continuity forces \(\partial_{pq}\Phi=0\) throughout the domain. Integrating this equality shows \(\Phi(p,q)=f(p)+g(q)\); the converse is immediate. For a product flux, \(\Delta_\Phi=\alpha\beta>0\), so the overlap error is strictly positive at every \(H>T\).

**Hyperbolic example and Courant bound.** For \(\Phi=pq\), the directional flux Jacobian for unit normal \(n=(n_x,n_y)\) is
\[
A_n=\begin{pmatrix}\varepsilon n_xq+vn_y&\varepsilon n_xp\\
\varepsilon n_xq&\varepsilon n_xp-vn_y\end{pmatrix}.
\]
The symmetrizer \(S=\operatorname{diag}(q,p)\) is positive definite and makes \(SA_n\) symmetric. The characteristic discriminant equals
\[
\big(\varepsilon n_x(q-p)+2vn_y\big)^2+4\varepsilon^2n_x^2pq>0
\]
for every nonzero normal and \(p,q>0\), proving strict hyperbolicity. In the \(S\)-weighted inner product the symmetric normal Jacobian has spectral norm bounded by
\[
\varepsilon(p+q)|n_x|+v|n_y|
\le\sqrt{v^2+\varepsilon^2(p+q)^2}.
\]
For the stated positive data, \(p+q\le4\), so \(\lambda=\sqrt{29}/5\) is an admissible bound. At \(H=9/10\), its Courant square is \(2349/2500<1\). The exact rational flux values follow by substituting the four states into the established formula.

## Verification

Execute `python3 verify.py` using Python 3 and only the standard library. The checker independently partitions the face into constant-state intervals at each time, integrates the resulting piecewise-linear instantaneous flux exactly using rational arithmetic, and compares that direct computation with the closed formula for seven polynomial flux families over 10,500 parameter cases. It also checks the displayed rational counterexample and squared Courant inequality. These finite checks are independent algebraic corroboration, not a substitute for the proof for all parameters.

## Relationship to prior work

Gaburro, Ricchiuto and Dumbser (2025) study complete multidimensional Riemann solvers and schemes with vertex fluxes and genuinely multidimensional upwinding. Gallardo, Schneider and Castro (2018) give a one-dimensional-face-plus-two-vertex construction of incomplete multidimensional fluxes; their formulas concern approximate resolved fluxes and scheme stability, rather than the exact physical flux of two independently transported contacts on a complete finite face. The present theorem isolates when adding individually exact endpoint corrections equals that physical face flux, and quantifies a non-polynomial overlap barrier. It does not claim that general corner-coupled methods omit all such cross effects. The accessible 2025 primary PDF was examined in its sections on face-flux quadrature, Osher-type corner tensors, residual-distribution corner fluctuations, the N scheme, higher-order extension and conclusions; its formulas (7), (9), (23), (27), (39) and (46) define approximate numerical fluxes rather than an exact two-contact physical face-time integral. Earlier equivalent specializations cannot be excluded without further historical review.

## Limitations

The theorem is for two counterpropagating contact families, rectangular faces, finite horizons \(H\le L/v\), and a nonlinear normal physical flux. The strict-hyperbolic example uses positive states. It does not prove a stability threshold for general nonlinear systems or a numerical scheme; a solver with transverse evolution or explicit interaction corrections may capture the defect. The identity is analytically exact in the stated model, while the research-priority assessment remains provisional.

## References

1. E. Gaburro, M. Ricchiuto and M. Dumbser, *On general and complete multidimensional Riemann solvers for nonlinear systems of hyperbolic conservation laws*, arXiv:2506.00207, first version 2025-05-30. https://arxiv.org/abs/2506.00207
2. J. M. Gallardo, K. A. Schneider and M. J. Castro, *On a class of two-dimensional incomplete Riemann solvers*, arXiv:1811.05188, first version 2018-11-13. https://arxiv.org/abs/1811.05188
