# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

For the homogeneous system
\[
\dot x=G(x)-x+F\mathbf e,
\]
the hypotheses on the quadratic advection imply both \(G(\lambda\mathbf e)=0\) and energy preservation \(x^TG(x)=0\). After translating the constant equilibrium, the exact identity
\[
\frac12\frac{d}{dt}\|y\|^2=-y^T(I-FS)y,
\qquad S=(A+A^T)/2,
\]
is immediate. Cyclic equivariance makes \(A=DG(\mathbf e)\) circulant, so the eigenvalues of \(S\) are the real parts of the Fourier eigenvalues of \(A\). This proves global exponential convergence whenever all \(F\Re\lambda_k(A)<1\).

The marginal case was checked separately rather than inferred from the strict case. Expanding energy preservation at \(\mathbf e+\varepsilon z\) gives
\[
\mathbf e^TA=0,
\qquad
\mathbf e^TG(z)=-z^TAz.
\]
On the kernel of \(H=I-FS\), one has \(\mathbf e^Ty=0\) and, for nonzero \(y\),
\[
\frac{d}{dt}\mathbf e^Ty=-\frac{\|y\|^2}{F}\ne0.
\]
Thus no nonzero trajectory can remain in the zero-dissipation set. The largest invariant subset is the origin, and LaSalle's invariance principle gives global convergence. Lyapunov stability follows from the nonincreasing Euclidean energy. Conversely, a mode with \(F\Re\lambda_k(A)>1\) is a genuine unstable linear mode. This establishes the claimed equivalence.

For the standard Lorenz-96 advection the Fourier symbol was independently recomputed as \(e^{i\theta}-e^{-2i\theta}\), with real part \(\cos\theta-\cos2\theta\). The stated formulas for the finite-dimensional maximum and minimum were checked for dimensions 4 through 64, together with the two polynomial identities used in the proof. These computational checks support, but are not needed for, the analytic proof.

## Originality — PASS, narrowly scoped

The strict-interior stability statement is not new. Kerin and Engler, *On the Lorenz '96 Model and Some Generalizations* (DCDS-B 27 (2022), 769--797; arXiv:2005.07767), prove global asymptotic stability for the homogeneous G-map under strict spectral inequalities. Their treatment also develops the cyclic quadratic framework and Fourier linearization. That prior result is explicitly separated from the present contribution.

The inspected Lorenz-96 literature on the constant equilibrium, energy estimates, travelling waves, and the first Hopf/Hopf--Hopf bifurcations did not state the equality-case result proved here: when the centered energy derivative is only negative semidefinite and the linearization has neutral modes, the quadratic advection necessarily transfers a nonzero marginal state into the damped mean direction, so the equilibrium is nevertheless globally asymptotically stable. Consequently the strict sufficient condition closes to an exact if-and-only-if global criterion.

Van Kekem and Sterk's bifurcation analyses locate and classify the first instabilities and the travelling waves born after them; they are consistent with the endpoint theorem but do not supply this global nonhyperbolic closure. Lorenz's original predictability paper and Lorenz--Emanuel provide model context rather than the endpoint stability statement.

Originality is asserted only to the best of our knowledge. The main residual risk is that this short endpoint argument may have appeared implicitly in an older, poorly indexed stability treatment or as an unstated consequence of a more general invariance-principle argument. No inspected source supplied that statement or the mean-transfer obstruction in this Lorenz-96-like setting.

## Value — PASS

The contribution closes a mathematically meaningful gap exactly where the standard energy estimate loses coercivity. It shows that neutral linear modes at the energy boundary do not support a hidden compact recurrent set: nonlinear advection forces departure from the zero-dissipation Fourier subspace. This upgrades a strict sufficient condition to an exact global stability criterion for a whole homogeneous energy-preserving cyclic quadratic class.

For standard finite-dimensional Lorenz-96, the result identifies the exact closed forcing interval on which the homogeneous equilibrium is globally asymptotically stable, with explicit Fourier formulas for both endpoints. In particular, the critical endpoint itself remains globally attracting; recurrent waves or other compact nontrivial dynamics can only occur after the spectral boundary is crossed.

## Scientific limitations

The theorem requires homogeneous forcing and unit homogeneous damping, exact quadratic energy preservation, and cyclic equivariance. It gives no quantitative decay rate at a marginal endpoint and does not classify the dynamics after instability. The uniform interval \([-1/2,8/9]\) is a convenient dimension-independent subset of the exact finite-dimensional interval, not generally the exact interval itself. The novelty claim excludes the strict-interior stability theorem, which is prior work.
