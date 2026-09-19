# Unit-normalized weak Gauss–Newton can amplify energy error without bound

## Result

Consider the weak elliptic Gauss–Newton construction of Schwencke and Maier (arXiv:2609.20641v1). For test functions \(z_i\in H_0^1(\Omega)\), its weak residual and Jacobian components are
\[
b_i=a(v_\theta,z_i)-\langle f,z_i\rangle,
\qquad
J_{ij}=a(\partial_jv_\theta,z_i),
\]
and the parameter correction is obtained from the ordinary Euclidean least-squares problem
\[
\min_\xi \frac12\|b-J\xi\|_2^2.
\]
The numerical experiments normalize fixed test functions in the corresponding energy norm.

Energy normalization of the individual tests does **not** control the metric induced by this least-squares problem. Even with a fixed two-dimensional test space, two unit-energy tests can become nearly parallel, and the resulting Gauss–Newton step can increase the true energy error by an arbitrarily large factor.

More generally, the Euclidean weak-residual metric is determined by the frame operator of the chosen test family, not only by its span. It is proportional to the energy norm on the test span if and only if the test family is a tight frame on that span.

## Frame identity and the invariant metric

Let \((H,a)\) be a real Hilbert space, let \(Z=(z_i)_{i=1}^N\subset H\), and define the analysis map
\[
T_Zw=(a(w,z_i))_{i=1}^N.
\]
Let
\[
S_Z=T_Z^*T_Z,
\qquad
S_Zw=\sum_{i=1}^N a(w,z_i)z_i,
\]
be the frame operator, let \(W=\operatorname{span}Z\), and let \(G=T_ZT_Z^*\) be the Gram matrix, \(G_{ij}=a(z_j,z_i)\). Then
\[
\boxed{\|T_Zw\|_2^2=a(S_Zw,w).}
\]
Thus ordinary Euclidean least squares in the weak measurements minimizes the quadratic form induced by \(S_Z\).

By contrast,
\[
\boxed{(T_Zw)^TG^\dagger(T_Zw)=\|P_W^aw\|_a^2,}
\]
where \(P_W^a\) is the energy-orthogonal projector onto \(W\). This identity follows from the singular-value decomposition of \(T_Z\), equivalently from
\[
T_Z^*G^\dagger T_Z=P_W^a.
\]
Hence the Gram-weighted residual is invariant under a change of coordinates spanning the same test space.

For \(w\in W\),
\[
\|T_Zw\|_2^2=c\|w\|_a^2\quad\text{for every }w\in W
\]
holds if and only if
\[
\boxed{S_Z|_W=cI_W,}
\]
i.e. if and only if \(Z\) is a tight frame on \(W\). Unit normalization \(\|z_i\|_a=1\) fixes the trace of \(S_Z\) but does not control its smallest eigenvalue or condition number.

## Explicit fixed-span counterexample

Choose any energy-orthonormal pair \(\phi_1,\phi_2\in H_0^1(\Omega)\):
\[
a(\phi_i,\phi_j)=\delta_{ij}.
\]
Take the exact solution and one-parameter approximation model
\[
u=-\phi_2,
\qquad
v_\theta=\theta\phi_1,
\]
with current parameter \(\theta=0\). Then the current solution error is
\[
e=v_0-u=\phi_2,
\qquad
\|e\|_a=1,
\]
and the tangent correction is \(\xi\phi_1\).

For any \(\varepsilon>0\), choose
\[
z_1=\phi_2,
\qquad
z_2=\frac{\varepsilon\phi_1+\phi_2}{\sqrt{1+\varepsilon^2}}.
\]
Both tests have unit energy norm, and for every \(\varepsilon>0\)
\[
\operatorname{span}\{z_1,z_2\}=\operatorname{span}\{\phi_1,\phi_2\}.
\]
Thus neither the test span nor the individual test norms change as \(\varepsilon\to0\); only the frame geometry degenerates.

The weak residual and one-column Jacobian are
\[
b=
\begin{bmatrix}
1\\
(1+\varepsilon^2)^{-1/2}
\end{bmatrix},
\qquad
J=
\begin{bmatrix}
0\\
\varepsilon(1+\varepsilon^2)^{-1/2}
\end{bmatrix}.
\]
Ordinary Euclidean Gauss–Newton therefore gives
\[
\boxed{\xi_\varepsilon=\frac{J^Tb}{J^TJ}=\frac1\varepsilon.}
\]
Because the model is linear, this is not merely a linearization artifact. After the source update \(\theta\leftarrow\theta-\xi_\varepsilon\), the true energy error is
\[
\boxed{
\|v_{-\xi_\varepsilon}-u\|_a
=\sqrt{1+\varepsilon^{-2}}.
}
\]
The amplification factor diverges as \(\varepsilon\downarrow0\), despite fixed test span and unit-normalized test functions.

At the same time, the measured squared residual decreases from
\[
\|b\|_2^2=1+\frac1{1+\varepsilon^2}
\]
to
\[
\|b-J\xi_\varepsilon\|_2^2=1.
\]
Thus the discrete objective reports improvement while the energy error becomes arbitrarily worse.

## Exact dependence on frame conditioning

The Gram matrix of the two unit tests is
\[
G_\varepsilon=
\begin{bmatrix}
1&c_\varepsilon\\
c_\varepsilon&1
\end{bmatrix},
\qquad
c_\varepsilon=(1+\varepsilon^2)^{-1/2}.
\]
Its condition number is
\[
\kappa_\varepsilon=\frac{1+c_\varepsilon}{1-c_\varepsilon}.
\]
Solving this relation for \(\varepsilon\) yields the exact identities
\[
\boxed{
|\xi_\varepsilon|
=\frac12\left(\sqrt{\kappa_\varepsilon}-\frac1{\sqrt{\kappa_\varepsilon}}\right),
}
\]
and
\[
\boxed{
\frac{\|v_{-\xi_\varepsilon}-u\|_a}{\|v_0-u\|_a}
=\frac12\left(\sqrt{\kappa_\varepsilon}+\frac1{\sqrt{\kappa_\varepsilon}}\right).
}
\]
Hence the bad step grows asymptotically like one half of the square root of the test-frame condition number.

## Gram weighting on the same example

For the same residual components and Jacobian, consider the discrete dual-norm objective
\[
(b-J\xi)^TG_\varepsilon^{-1}(b-J\xi).
\]
Because the two tests span \(\operatorname{span}\{\phi_1,\phi_2\}\), this is exactly
\[
\|\phi_2-\xi\phi_1\|_a^2=1+\xi^2.
\]
Its minimizer is \(\xi=0\), so the spurious \(1/\varepsilon\) correction disappears.

This Gram-inverse remedy is **not** claimed as new. Robust Variational Physics-Informed Neural Networks (RVPINNs) already establish that classical weak residual losses depend on the selected test basis and replace them with a discrete dual norm involving the inverse test Gram matrix. The contribution here is the source-specific Gauss–Newton obstruction: individual energy normalization, as used in arXiv:2609.20641v1, does not prevent a fixed-span family from producing an arbitrarily harmful Gauss–Newton step, and the failure admits the exact frame-conditioning law above.

## Relation to prior work

Rojas, Maczuga, Muñoz-Matute, Pardo, and Paszyński (CMAME 425, 2024, Article 116904; arXiv:2308.16910) explicitly show that the classical VPINN loss depends on the basis of a fixed test space and formulate a basis-independent discrete dual-norm loss using the inverse Gram matrix. Their work therefore covers the broad basis-dependence mechanism and the robust Gram-weighted remedy.

The 2026 Gauss–Newton/Petrov–Galerkin paper cites that work, but its general weak-test construction nevertheless applies ordinary Euclidean Gauss–Newton to the weak residual components, and its fixed experimental test functions are individually energy-normalized. The present result isolates what that normalization does not control: near-linear dependence of the test frame can make the Gauss–Newton correction itself arbitrarily destructive in the physical energy norm.

## Limitations

The counterexample is deliberately minimal: a symmetric coercive elliptic energy space, a linear one-parameter model, and two tests. It proves a worst-case instability mechanism, not that the reported numerical experiments exhibit it or that the overall solver necessarily diverges. Damping, trust regions, regularization, adaptive test selection, or well-conditioned/tight test families can suppress the phenomenon.

The tight-frame and Gram identities are standard frame/minimum-residual facts and are not presented as general new mathematics. The originality claim is restricted to their explicit implication for the 2026 weak Gauss–Newton construction: a fixed-span, individually unit-normalized family with unbounded one-step energy-error amplification and the exact dependence on frame conditioning.

## Reproducibility

`artifacts/verify_frame_obstruction.py` evaluates the two-dimensional formulas directly in an energy-orthonormal coordinate system. `artifacts/verification_output.txt` records the output for several values of \(\varepsilon\).

## References

1. N. Schwencke and R. Maier, *Beyond PINNs: A Unified Gauss–Newton and Petrov–Galerkin Framework for Neural and Hybrid PDE Solvers*, arXiv:2609.20641v1, 2026. https://arxiv.org/abs/2609.20641
2. S. Rojas, P. Maczuga, J. Muñoz-Matute, D. Pardo, and M. Paszyński, *Robust Variational Physics-Informed Neural Networks*, Computer Methods in Applied Mechanics and Engineering 425 (2024), 116904. https://doi.org/10.1016/j.cma.2024.116904 ; arXiv:2308.16910.
