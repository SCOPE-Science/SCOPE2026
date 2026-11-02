# Conserved convex energy and invariant ovals at the reflection endpoint of two-by-two Sinkhorn overrelaxation

## Finding
For every \(c>0\), the fixed-parameter overrelaxed Sinkhorn iteration at relaxation \(\omega=2\), applied to the strictly positive kernel
\[
K_c=\begin{pmatrix}1&c\\c&1\end{pmatrix}
\]
with uniform row and column marginals \((1/2,1/2)\), preserves the nonconstant function
\[
\mathcal H(X,Y)=2\cosh((X+Y)/2)+2c\cosh((X-Y)/2),
\]
where \(X=\log(u_1/u_2)\) and \(Y=\log(v_1/v_2)\) are the two projective logarithmic scaling coordinates. The map is a globally defined, orientation-preserving area-preserving diffeomorphism of \(\mathbb R^2\). It has precisely one fixed point, \((0,0)\). Every other trajectory stays on a compact smooth strictly convex oval, is bounded and recurrent, and **does not converge** to the desired projective scaling. Each oval supports dynamics conjugate to a rigid circle rotation: each trajectory is periodic or dense in its oval. Thus the open restriction \(\omega<2\) in the usual overrelaxation stability analysis has a global, explicitly integrable boundary phenomenon even for the smallest positive transport kernel.

## Assumptions and scope
Let \(u,v\in\mathbb R^2_{>0}\) and let \(a=b=(1/2,1/2)\). Use exactly the standard multiplicative overrelaxed Sinkhorn update
\[
u^+=u^{1-\omega}\circ(a/(K_cv))^{\omega},\qquad
v^+=v^{1-\omega}\circ(b/(K_c^\mathsf{T}u^+))^{\omega}
\]
(componentwise products, quotients and powers), at the **fixed** parameter \(\omega=2\). This is not an adaptive or descent-safeguarded overrelaxation rule. Scaling equivalences \((u,v)\sim(tu,t^{-1}v)\) are factored out by the two positive odds \(U=u_1/u_2\), \(V=v_1/v_2\). The theorem concerns exact arithmetic, \(c\in(0,\infty)\), all positive starting scalings, and convergence of these odds; no assertion is made about the otherwise redundant overall scaling gauge.

## Proof
**1. Reduction and two reflections.** Put \(U=e^X\), \(V=e^Y\) and
\[
g_c(t)=\frac{ct+1}{t+c},\qquad \phi_c(y)=\log\frac{e^y+c}{ce^y+1}.
\]
Taking coordinate ratios of the two overrelaxed scaling updates yields
\[
U^+=\frac{g_c(V)^2}{U},\qquad V^+=\frac{g_c(U^+)^2}{V}.
\]
Equivalently, the map \(T_c\) is the composition of
\[
R_X(X,Y)=(-X-2\phi_c(Y),Y),\qquad
R_Y(X,Y)=(X,-Y-2\phi_c(X)),
\]
with \(T_c=R_Y\circ R_X\). Each reflection is a smooth global involution with Jacobian determinant \(-1\), so \(T_c\) is a smooth global diffeomorphism with constant Jacobian determinant \(1\).

**2. Exact conserved quantity.** In odds coordinates define
\[
J_c(U,V)=\frac{UV+c(U+V)+1}{\sqrt{UV}}.
\]
For fixed \(V\), write this as
\[
J_c(U,V)=\frac{(V+c)\sqrt U+(cV+1)/\sqrt U}{\sqrt V}.
\]
The first reflection replaces \(\sqrt U\) by \(g_c(V)/\sqrt U\), interchanging the two displayed numerator summands. Thus \(J_c(g_c(V)^2/U,V)=J_c(U,V)\). The identical argument in the other coordinate proves invariance under the second reflection. Substituting \(U=e^X,V=e^Y\) gives exactly \(J_c(e^X,e^Y)=\mathcal H(X,Y)\); hence \(\mathcal H\circ T_c=\mathcal H\) for every \(c>0\).

**3. Global geometry and unique fixed point.** Direct differentiation yields
\[
\nabla^2\mathcal H
=\frac12\cosh((X+Y)/2)
\begin{pmatrix}1&1\\1&1\end{pmatrix}
+\frac c2\cosh((X-Y)/2)
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
For \(c>0\) this Hessian is positive definite everywhere. Also \(\mathcal H(X,Y)\to\infty\) whenever \(\|(X,Y)\|\to\infty\), and its unique minimum \(2(1+c)\) occurs at the origin. Every higher regular level is therefore a compact, smooth, strictly convex simple closed curve. Since \(T_c\) preserves each level, all trajectories remain bounded. To see that the only fixed point is the origin, note that \(\phi_c(0)=0\) and
\[
|\phi_c'(y)|=\frac{|1-c^2|e^y}{(e^y+c)(ce^y+1)}\le\frac{|1-c|}{1+c}<1.
\]
At a fixed point the reflections imply \(X=-\phi_c(Y)\), \(Y=-\phi_c(X)\); their composition is a strict contraction, with the sole solution \((0,0)\). In particular, an orbit of positive energy excess cannot converge to the unique fixed point because its conserved energy exceeds \(2(1+c)\).

**4. Rotation dynamics on each level.** Let \(E>2(1+c)\). On the invariant oval \(\Gamma_E=\{\mathcal H=E\}\), the Hamiltonian vector field \(J\nabla\mathcal H\), with the standard constant symplectic matrix \(J\), is nonvanishing and has a periodic flow. Since \(T_c\) preserves both the area two-form and \(\mathcal H\), it preserves this vector field, commutes with its flow and hence acts on the entire oval by a fixed shift of Hamiltonian time. Reparametrizing the oval by the normalized flow time conjugates \(T_c|_{\Gamma_E}\) to a rigid circle rotation. Rational rotation numbers give periodic trajectories; irrational ones give trajectories dense in their oval. In either case every nonfixed trajectory is recurrent and never converges to \((0,0)\).

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic to evaluate 125 positive parameter/initial-odds triples. It checks preservation of the squared conserved quantity separately through both reflections, the determinant-one Jacobian identity, and energy preservation across 875 further full iterations. The analytical calculations above establish the conclusions for the entire continuum \(c>0\) and all positive initial scalings; the finite tests are only reproducibility checks.

## Relationship to prior work
Thibault, Chizat, Dossal and Papadakis introduced multiplicative overrelaxed Sinkhorn and studied adaptive Lyapunov safeguards [1]. Lehmann, von Renesse, Sambale and Uschmajew established local convergence for \(0<\omega<2\) and a smaller globally guaranteed parameter range [2]; their theory does not cover the endpoint \(\omega=2\). Soma and Uschmajew extended overrelaxation analysis to operator scaling and likewise emphasize local and limited-range global results [3]. The broad QRT theory includes symplectic rational maps with rational first integrals [4]; after the odds reduction, the recurrence here is of a multiplicative QRT type. That general mechanism is prior work, not claimed as newly invented. The present result specializes that mechanism to a named matrix-scaling iteration and establishes the **entire positive-plane** energy geometry, global bounded nonconvergence and rotation classification at its excluded parameter endpoint.

## Limitations
The exact conserved energy and global oval classification are proved only for the displayed symmetric two-by-two positive kernel, equal marginal vectors, fixed parameter \(\omega=2\), and exact arithmetic. Neither global nonconvergence for all positive kernels nor a corresponding integral for unequal marginals follows. The rotation number as a function of energy is not explicitly evaluated, and the theorem does not assert that a particular nonfixed orbit is periodic. The connection to general QRT invariants creates a genuine priority risk for the algebraic first-integral component; independently established priority for this precise algorithmic boundary claim remains outstanding.

## References
[1] A. Thibault, L. Chizat, C. Dossal, N. Papadakis, *Overrelaxed Sinkhorn-Knopp Algorithm for Regularized Optimal Transport*, arXiv:1711.01851, first public 2017-11-06; Algorithms 14 (2021), 143.

[2] T. Lehmann, M.-K. von Renesse, A. Sambale, A. Uschmajew, *A note on overrelaxation in the Sinkhorn algorithm*, arXiv:2012.12562, first public 2020-12-23; Optimization Letters 16 (2022), 2209–2220.

[3] T. Soma, A. Uschmajew, *Accelerating operator Sinkhorn iteration with overrelaxation*, arXiv:2410.14104, first public 2024-10-18.

[4] K. Hamad, A. N. W. Hone, P. H. van der Kamp, G. R. W. Quispel, *QRT maps and related Laurent systems*, arXiv:1702.07047, first public 2017-02-22; Advances in Applied Mathematics 96 (2018), 216–248.
