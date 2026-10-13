# An exact coupled period-two orbit for fixed-step simplified Muon
## Finding
Consider the mixed-spiked matrix-sensing model with \(n=3r\) and the source invariant factor manifold
\[
X=[aU\;bV\;cW],
\]
where the column spaces of \(U,V,W\) are mutually orthogonal. For any
\[
0<\eta<1,\qquad 0<\chi<\frac13,
\]
choose the interaction matrix
\[
\widehat K_{\chi}=
\begin{pmatrix}
1&\chi&0\\
\chi&1&0\\
0&0&1
\end{pmatrix}.
\]
This interaction is genuinely coupled because \(\chi>0\). It is also realizable by the source model: since \(n=3r\),
\[
\widehat K_{\chi}=\frac23 I_3+r^2\Sigma,
\qquad
\Sigma=\frac1{r^2}
\begin{pmatrix}
\frac13&\chi&0\\
\chi&\frac13&0\\
0&0&\frac13
\end{pmatrix}\succ0,
\]
where positive definiteness follows from \(0<\chi<1/3\).

Put
\[
\delta=\frac{\eta^2}{4},
\qquad
t=\frac{\eta}{4}\sqrt{8-\eta^2},
\qquad
q=2\delta-\delta^2=t^2.
\]
Then the two factor states
\[
X^+=\left[(1+\eta-\delta)U\;\; (\eta-t)V\;\; \frac\eta2 W\right]
\]
and
\[
X^-=\left[(1-\delta)U\;\; -tV\;\; -\frac\eta2 W\right]
\]
form an exact period-two orbit of the actual fixed-step simplified Muon iteration:
\[
X^+\longmapsto X^-\longmapsto X^+.
\]
Every block of the gradient is nonzero at both states, so the matrix polar factor used in the update is single-valued there.

At \(X^-\), the reduced coordinate vector is
\[
z^-=
\begin{bmatrix}
(1-\delta)^2-1\\
t^2\\
\eta^2/4
\end{bmatrix}
=
\begin{bmatrix}
-q\\q\\\eta^2/4
\end{bmatrix},
\]
and therefore its reduced loss is exactly
\[
f(X^-)=(1-\chi)q^2+\frac{\eta^4}{32}>0.
\]
Hence the coupled fixed-step iteration does not converge to the ground truth.

## Assumptions and scope
The statement uses simplified Muon without momentum and with a constant exact polar-factor step \(\eta\). It applies to the population mixed-spiked matrix-sensing objective introduced in arXiv:2606.21514v1, restricted to the source invariant manifold \(X=[aU\;bV\;cW]\). The interaction matrix is a positive-definite member of the source family and has a nonzero signal--nuisance coupling.

The result concerns the actual factor-level Muon update. The source also visualizes reduced coefficient trajectories obtained by discretizing continuous reduced dynamics; those coefficient plots are not used as proof here.

The constraints \(0<\eta<1\) and \(0<\chi<1/3\) ensure, respectively, that the displayed factors stay away from the sign singularities and that the covariance realizing \(\widehat K_{\chi}\) is positive definite. No stochastic noise, momentum, Newton--Schulz approximation, or learning-rate decay is included.

## Proof
For the source reduced objective
\[
f(\alpha,\beta,\gamma)
=\frac12
\begin{bmatrix}\alpha-1&\beta&\gamma\end{bmatrix}
\widehat K_{\chi}
\begin{bmatrix}\alpha-1\\\beta\\\gamma\end{bmatrix},
\]
write
\[
z=\begin{bmatrix}a^2-1\\b^2\\c^2\end{bmatrix}.
\]
The source's factor-manifold computation shows that the gradient has three mutually orthogonal blocks whose scalar force signs are the signs of the coordinates of \(\widehat K_{\chi}z\), with an additional factor sign from \(a,b,c\). Positive scalar prefactors do not affect the polar factor. Thus, whenever all three gradient blocks are nonzero, one fixed simplified-Muon step is
\[
a^+=a-\eta\,\operatorname{sign}\!\big(a(\widehat K_{\chi}z)_1\big),
\]
\[
b^+=b-\eta\,\operatorname{sign}\!\big(b(\widehat K_{\chi}z)_2\big),
\qquad
c^+=c-\eta\,\operatorname{sign}\!\big(c(\widehat K_{\chi}z)_3\big).
\]

First consider \(X^+\). Since \(0<\eta<1\), one has
\[
0<\delta<\eta,
\qquad
0<t<\eta.
\]
Therefore each factor in \(X^+\) is positive, while its signal factor exceeds \(1\). Consequently all three entries of the corresponding \(z^+\) are strictly positive. Because \(\widehat K_{\chi}\) has nonnegative entries and positive diagonal, all three force coordinates are strictly positive. One Muon step subtracts \(\eta\) from each factor, giving exactly
\[
X^+\mapsto X^-.
\]

At \(X^-\), the signal factor remains positive because \(1-\delta>0\). By the definition of \(t\),
\[
t^2=\frac{\eta^2}{16}(8-\eta^2)
=\frac{\eta^2}{2}-\frac{\eta^4}{16}
=2\delta-\delta^2=q.
\]
Hence
\[
z^-=egin{bmatrix}-q\\q\\\eta^2/4\end{bmatrix},
\qquad
\widehat K_{\chi}z^-=
\begin{bmatrix}-(1-\chi)q\\(1-\chi)q\\\eta^2/4\end{bmatrix}.
\]
All three forces are nonzero. The signal factor is positive while its force is negative; the second and third factors are negative while their forces are positive. Thus all three gradient blocks have negative sign, and the next Muon step adds \(\eta\) to each factor. This yields
\[
X^-\mapsto X^+.
\]
The orbit is therefore exactly period two.

Finally,
\[
f(X^-)=\frac12(z^-)^{\!\top}\widehat K_{\chi}z^-
=(1-\chi)q^2+\frac{\eta^4}{32},
\]
which is strictly positive. The orbit cannot converge to the ground-truth minimizer.

## Verification
The bundled script `artifacts/verify_coupled_muon_cycle.py` reconstructs the two states, the realizable covariance, the force signs, and the exact step-to-step toggling on a grid of \(\eta\) and \(\chi\) values. It also checks the closed formula for the reduced loss at \(X^-\).

These finite computations are consistency checks only. The quantified result for every \(0<\eta<1\) and \(0<\chi<1/3\) follows from the algebraic sign calculation above.

## Relationship to prior work
The motivating 2026 river-valley paper introduces the mixed-spiked matrix-sensing model, derives the invariant factor manifold, and proves the block-sign form of simplified Muon. It explicitly emphasizes that a fixed step can overshoot and produce persistent late-stage oscillations. Its diagonal example is fully decoupled, while its coupled positive-semidefinite example is numerical and its general theorem establishes local river-energy behavior rather than an exact periodic orbit. Searches of the full text found no period or two-cycle theorem.

Ma, Huang, Chi, and Chen analyze simplified Muon on matrix factorization and derive exact decoupled scalar spectral recurrences. Their convergence theorem uses geometrically decaying learning rates, and they explain that Muon's fixed movement length motivates decay. Their scalar recurrence makes constant-step oscillation in a decoupled coordinate unsurprising, but it does not imply the present off-diagonal signal--nuisance cycle because their spectral modes are independent.

Shen, Huang, Huang, Shen, and Zhang provide broad convergence theory for Muon under several smoothness regimes. Their results concern convergence rates and structural Hessian advantages rather than the coupled mixed-spiked dynamics or the exact period-two construction above.

Targeted published-result searches for coupled Muon cycles, mixed-spiked period-two behavior, fixed-step river--hill periodicity, and equivalent orthogonalized-gradient formulations did not return a statement implying this exact family.

## Limitations
The theorem is an explicit family of coupled counterexamples, not a classification of all fixed-step trajectories for every positive-semidefinite interaction matrix. It uses exact spectral orthogonalization and no momentum. The coupling family has only one nonzero off-diagonal signal--nuisance pair; the third coordinate is decoupled so that the full polar factor stays nonsingular while the coupled mechanism remains transparent.

The theorem establishes existence of an exact persistent cycle for every fixed \(0<\eta<1\) within a continuum of feasible coupled covariances. It does not claim that generic initializations are attracted to this cycle, nor that the same orbit survives stochastic gradients, approximate Newton--Schulz orthogonalization, or momentum.

## References
1. T. Shen, J. Yang, R. Shi, J. Ma, J. Teng, and Z. Ma, *Towards Understanding the Power and Limits of the Muon Optimizer: A River-Valley Perspective*, arXiv:2606.21514v1, first public 2026-06-19.
2. J. Ma, Y. Huang, Y. Chi, and Y. Chen, *Preconditioning Benefits of Spectral Orthogonalization in Muon*, arXiv:2601.13474v1, 2026.
3. W. Shen, R. Huang, M. Huang, C. Shen, and J. Zhang, *On the Convergence Analysis of Muon*, arXiv:2505.23737v3; first public 2025-05-29.
