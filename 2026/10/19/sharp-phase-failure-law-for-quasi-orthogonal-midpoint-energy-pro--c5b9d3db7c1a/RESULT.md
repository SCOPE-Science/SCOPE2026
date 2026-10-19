# Sharp phase-failure law for quasi-orthogonal midpoint energy projection

## Finding

A convex quadratic first integral does **not** guarantee solvability of the energy-restoring quasi-orthogonal Runge--Kutta projection at arbitrary fixed steps. For the planar anisotropic linear oscillator and explicit midpoint rule below, the exact all-initial-data solvability threshold is
\[
 h_{\mathrm c}(\kappa)=\frac{2}{\sqrt{\kappa(\kappa^2-1)}}.
\]
For a uniformly sampled energy phase, the probability of *no real projection parameter* is zero at or below this threshold, has the explicit arcsine formula in the theorem, turns on with a square-root singularity above the threshold, and tends to one with a sharp inverse-square success tail for large steps. The probability and boundary laws describe solvability of the prescribed one-dimensional correction, not preservation of the invariant by any other correction direction.

**Theorem.** Fix \(\kappa>1\), set \(r=\kappa^2\), and define
\[
 D=1+\frac{\kappa^4h^4}{4},\qquad D_{\mathrm c}=\left(\frac{r+1}{r-1}\right)^2,\qquad H=D(r-1)^2.
\]
For every nonzero initial vector, the quasi-orthogonal energy projection defined below admits a real correction parameter if and only if
\[
 D\,\frac{(r-1)^2s(1-s)}{1+(r^2-1)s}\le1,
\]
where \(s=\kappa^2y_2^2/E(y)\in[0,1]\) is determined by the midpoint predictor \(y\). A correction exists for **every** nonzero initial vector if and only if \(0<h\le h_{\mathrm c}(\kappa)\). At equality there are four initial phases (modulo \(2\pi\)) producing a double real correction root; all other phases have two distinct roots. Above the threshold an open nonempty set of phases has no real root, while some phases remain solvable.

Sample the initial vector as \(q_0=R(\cos\theta,\kappa^{-1}\sin\theta)\), where \(R>0\) is arbitrary and \(\theta\) is uniform on \([0,2\pi)\). Let \(p_{\mathrm{fail}}(\kappa,h)\) denote the probability of an unsolvable projection equation. If \(h>h_{\mathrm c}(\kappa)\), put
\[
 s_\pm=\frac{H-r^2+1\ \pm\ \sqrt{[H-(r+1)^2][H-(r-1)^2]}}{2H}.
\]
Then \(0<s_-<s_+<1\), and exactly
\[
 \boxed{p_{\mathrm{fail}}(\kappa,h)=\frac{2}{\pi}\left(\arcsin\sqrt{s_+}-\arcsin\sqrt{s_-}\right).}
\]
At and below the threshold \(p_{\mathrm{fail}}=0\). For each fixed \(\kappa>1\), as \(D\downarrow D_{\mathrm c}\) from above,
\[
 p_{\mathrm{fail}}(\kappa,h)\sim
 \frac{2(r-1)}{\pi(r+1)}\sqrt{D-D_{\mathrm c}},
\]
and as \(h\to\infty\),
\[
 \boxed{1-p_{\mathrm{fail}}(\kappa,h)\sim
 \frac{4(r+1)}{\pi r(r-1)h^2}.}
\]
The threshold scales as \(h_{\mathrm c}(\kappa)\sim2\kappa^{-3/2}\) for large anisotropy. In the isotropic limiting case \(\kappa=1\), every nonzero initial vector admits a correction at every positive step.

## Assumptions and scope

Work in exact real arithmetic with the positive-definite energy
\[
 E(q)=q^{\mathsf T}Qq,\qquad Q=\operatorname{diag}(1,\kappa^2),
\]
and the smooth nonstationary conservative ODE
\[
 \dot q=Aq,\qquad A=\begin{pmatrix}0&\kappa^2\\-1&0\end{pmatrix}.
\]
Indeed \(A^{\mathsf T}Q+QA=0\), hence \(E(q(t))\) is constant. Start from any \(q_0\ne0\) and use the standard explicit two-stage midpoint formula
\[
 k_1=Aq_0,\qquad k_2=A(q_0+\tfrac h2 k_1),\qquad y=q_0+hk_2,
\]
with \(h>0\). The stage-derivative subspace is \(\mathcal S=\operatorname{span}\{k_1,k_2\}\). The quasi-orthogonal correction uses the line through \(y\) in the direction of the projection of \(\nabla E(y)\) onto \(\mathcal S\), as in the construction of Najafian--Vermeire. Solvability means existence of some **real** parameter on that line producing \(E(q_0)\). The normalizing length of the search direction does not affect existence. No projection-root selection policy or subsequent time step is assumed.

## Proof

Since \(A^2=-\kappa^2I\), the predictor has the form
\[
 y=\left(1-\frac{\kappa^2h^2}{2}\right)q_0+hAq_0=\alpha q_0+hAq_0.
\]
For \(h>0\), the vectors \(Aq_0\) and \(q_0\) are linearly independent: a real eigenvalue of \(A\) would contradict \(A^2=-\kappa^2I\). As \(k_2=Aq_0-\frac{h\kappa^2}{2}q_0\), this proves \(\mathcal S=\mathbb R^2\). Consequently the prescribed line is exactly \(y+\lambda Qy\), with \(\lambda\in\mathbb R\), because \(\nabla E(y)=2Qy\).

The matrix \(M=\alpha I+hA\) obeys \(M^{\mathsf T}QM=DQ\), with
\[
 D=\alpha^2+\kappa^2h^2=1+\frac{\kappa^4h^4}{4}>0.
\]
In particular \(E(y)=D E(q_0)\), and \(M\) is invertible. Let \(a=y_1^2\) and \(b=\kappa^2y_2^2\), so \(a+b=D E(q_0)\). The energy along the proposed correction line is the scalar quadratic
\[
 F(\lambda)=a(1+\lambda)^2+b(1+r\lambda)^2,
 \qquad r=\kappa^2.
\]
Completing the square gives the exact minimum
\[
 \min_{\lambda\in\mathbb R}F(\lambda)
 =a+b-\frac{(a+rb)^2}{a+r^2b}
 =\frac{ab(r-1)^2}{a+r^2b}.
\]
Because \(F\) is strictly convex and tends to infinity at both ends, the equation \(F(\lambda)=E(q_0)\) has two, one, or no real roots according as this minimum is less than, equal to, or greater than \(E(q_0)\). Setting \(s=b/(a+b)\) proves the pointwise criterion in the theorem.

The function
\[
 g_r(s)=\frac{(r-1)^2s(1-s)}{1+(r^2-1)s}
\]
on \([0,1]\) has unique maximum \((r-1)^2/(r+1)^2\), attained at \(s=1/(r+1)\). This follows by differentiating its positive denominator: the only interior critical point solves \(1-2s-(r^2-1)s^2=0\). The map \(M\) is invertible, so every predictor phase and in particular the unique maximizing value of \(s\) is realized by an initial vector. Universal solvability is thus equivalent to
\[
 D\frac{(r-1)^2}{(r+1)^2}\le1.
\]
Solving this inequality using \(D=1+r^2h^4/4\) gives exactly \(h\le2/\sqrt{\kappa(\kappa^2-1)}\). At equality the worst phase has a double root; there are four signed angle representatives on the energy circle.

For the phase distribution, use transformed coordinates \(w=Q^{1/2}q\). The midpoint matrix is conjugate to
\[
 Q^{1/2}MQ^{-1/2}=\begin{pmatrix}\alpha&\kappa h\\-\kappa h&\alpha\end{pmatrix},
\]
which is \(\sqrt D\) times an orthogonal rotation. A uniformly distributed initial energy angle therefore yields a uniformly distributed predictor angle. For that angle \(s=\sin^2\theta\) has density \(1/(\pi\sqrt{s(1-s)})\) on \((0,1)\). Failure means
\[
 Hs^2-(H-r^2+1)s+1<0,
\]
which, precisely when \(H>(r+1)^2\), defines the interval \((s_-,s_+)\) with the displayed roots. Integrating the arcsine density across this interval gives the exact probability.

For the near-threshold asymptotic, let \(\varepsilon=H-(r+1)^2\downarrow0\). Its quadratic discriminant factors as
\[
 [H-(r+1)^2][H-(r-1)^2]=\varepsilon(4r+\varepsilon).
\]
Hence \(s_+-s_-\sim2\sqrt{r\varepsilon}/(r+1)^2\), with both roots tending to \(1/(r+1)\). The arcsine density there is \((r+1)/(\pi\sqrt r)\), yielding
\[
 p_{\mathrm{fail}}\sim\frac{2\sqrt\varepsilon}{\pi(r+1)}
 =\frac{2(r-1)}{\pi(r+1)}\sqrt{D-D_{\mathrm c}}.
\]
For \(h\to\infty\), the roots satisfy \(s_-\sim H^{-1}\) and \(1-s_+\sim r^2H^{-1}\). Therefore the successful phase fraction is asymptotic to \(2(1+r)/(\pi\sqrt H)\). Since \(\sqrt H\sim r(r-1)h^2/2\), the stated inverse-square law follows. Finally, for \(\kappa=1\) the correction is radial and its line passes through the origin, so it always meets the original energy circle.

## Verification

An explicit rational witness uses \(\kappa=2\), \(h=2\), \(q_0=(1,1/2)\). The explicit midpoint prediction is \(y=(-3,-11/2)\), and its entire quasi-orthogonal correction line has energy
\[
 F(\lambda)=9(1+\lambda)^2+121(1+4\lambda)^2
 \ge\frac{9801}{1945}>2=E(q_0).
\]
Thus no real correction exists even though the invariant is strictly convex, the vector field is smooth, and the stage subspace is all of \(\mathbb R^2\).

Run `python verify.py` with Python 3.9 or later and no third-party dependencies. It checks the rational witness, independent matrix and minimization identities, sharp witness angles on both sides of the threshold, numerical phase integration, and both asymptotics. Its recorded output is in `verification_output.txt`; these numerical checks supplement, rather than replace, the exact proof.

## Relationship to prior work

Najafian and Vermeire (2024) define the quasi-orthogonal correction by projecting the invariant gradient onto the span of Runge--Kutta stage derivatives. Their Theorem 3 gives local solvability and order preservation for convex invariants **when the step is sufficiently small**; their Remark 4 identifies the full-stage-space case with ordinary orthogonal projection. Neither statement implies global solvability at arbitrary steps. The present theorem quantifies the phase fraction of global failure for a natural convex quadratic invariant in precisely that full-stage-space case.

The optimization identity behind the worst-phase threshold is the classical sharp two-eigenvalue steepest-descent (Kantorovich) contraction bound; it is not independently claimed as a novel inequality. The additional result is the complete phase-resolved *nonexistence distribution* for the fixed-step Runge--Kutta projection equation and its two sharp asymptotic regimes. Earlier Runge--Kutta invariant-projection constructions, including Calvo and coauthors (2006), provide relevant methodological context but use different search directions.

## Limitations

This is a one-step solvability theorem for explicit midpoint on a two-dimensional linear oscillator with strictly convex anisotropic quadratic invariant. It does not characterize other Runge--Kutta schemes, other correction directions, a safeguarded alternative that chooses any vector in the stage span, global multi-step solution accuracy, or finite precision. The uniform-phase law presumes uniform *energy angle*, not uniform Euclidean arclength on the ellipse. The sharp worst-case threshold is related to classical exact-line-search bounds, and an equivalent probability-law formulation in older line-search literature remains a literature-priority risk. The original method's published small-step theorem is respected, not contradicted.

## References

1. M. R. Najafian and B. C. Vermeire, *Quasi-Orthogonal Runge-Kutta Projection Methods*, arXiv:2409.18328v1, first publicly submitted 2024-09-26. https://arxiv.org/abs/2409.18328 ; accessible method text at https://arxiv.org/html/2409.18328 .
2. M. Calvo, D. Hernández-Abreu, J. I. Montijano, and L. Rández, *On the Preservation of Invariants by Explicit Runge--Kutta Methods*, SIAM Journal on Scientific Computing 28 (2006), 868–885, DOI 10.1137/04061979X.
3. E. de Klerk, F. Glineur, and A. Taylor, *On the worst-case complexity of the gradient method with exact line search for smooth strongly convex functions*, Optimization Letters 11 (2017), 1185–1199, DOI 10.1007/s11590-016-1087-4.
