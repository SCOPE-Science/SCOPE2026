# Sharp almost-sure phase-opposition threshold for analytic sinusoidal torus updates

## Finding

**Theorem (closed critical threshold and measure-theoretic reversal).** Let \(d\geq1\), let \(K\in\mathbb R^{d\times d}\) be symmetric positive definite, and let \(A=\operatorname{diag}(a_1,\ldots,a_d)\), with every \(a_i>0\). Write
\[
\Lambda=\lambda_{\max}(A^{1/2}KA^{1/2}),\qquad
F_h(z)=z+hKA\sin z\pmod{2\pi},\qquad
p_*=(\pi,\ldots,\pi).
\]
Sine acts coordinatewise, and \(h>0\). For every \(0<h\leq 2/\Lambda\), every trajectory of \(F_h\) converges to one of the \(2^d\) binary-phase equilibria \(\{0,\pi\}^d\); the potential \(V(z)=\sum_i a_i\cos z_i\) strictly decreases at every other point, and the basin of \(p_*\) has full normalized Haar measure. The equilibrium \(p_*\) is Lyapunov stable, there are no nontrivial periodic orbits, the nonwandering set is exactly \(\{0,\pi\}^d\), and the topological entropy is zero.

For every \(h>2/\Lambda\), the basin of the **same specified phase-opposition equilibrium** \(p_*\) has Haar measure zero. Thus the full-measure basin property for \(p_*\) holds exactly for \(0<h\leq2/\Lambda\). The supercritical statement does not assert that other, potentially winding, attractors are absent.

## Assumptions and scope

The phase space is \(\mathbb T^d=(\mathbb R/2\pi\mathbb Z)^d\), with normalized Haar (Lebesgue) measure. Matrices are fixed; \(K\) is symmetric positive definite, not necessarily diagonally dominant, and \(A\) is a fixed positive diagonal matrix. The map is real analytic for every \(h>0\). In particular, for a positive-weight finite tree with oriented incidence matrix \(B\), choosing \(K=B^TB\) and \(A\) its edge-weight diagonal satisfies the hypotheses, without imposing any concavity on the weights. All claims concern the reduced edge-coordinate dynamics rather than the unreduced common-phase direction.

A basin is \(\mathcal B_h(p)=\{z:\lim_{n\to\infty}F_h^n(z)=p\}\). All limit statements refer to discrete forward iteration on the torus. No invertibility of \(F_h\) is assumed or claimed at or above \(1/\Lambda\).

## Proof

**Step 1: an exact positive remainder at the critical step.** Set \(u=A\sin z\), \(w=Ku\), and \(q=u^TKu\). The derivative of \(V\) is \(\nabla V=-u\) and its Hessian is \(-A\operatorname{diag}(\cos z_i)\). Taylor's formula along the straight lifted segment from \(z\) to \(z+hw\), using periodicity of \(V\), gives the **identity**
\[
\begin{aligned}
V(z)-V(F_hz)
={}&h\left(1-\frac{h\Lambda}{2}\right)q
+\frac{h^2}{2}\left(\Lambda q-w^TAw\right)\\
&+h^2\sum_{i=1}^d a_i w_i^2
\int_0^1(1-t)\bigl(1+\cos(z_i+t h w_i)\bigr)\,dt.
\end{aligned}
\tag{1}
\]
Because \(A^{1/2}KA^{1/2}\) is positive definite, \(q>0\) whenever \(u\ne0\), and
\[
w^TAw=u^TKAKu\leq\Lambda u^TKu=\Lambda q.
\]
For \(0<h\leq2/\Lambda\), the first two terms on the right of (1) are nonnegative. If \(u\ne0\), invertibility of \(K\) implies \(w_i\ne0\) for at least one index. For that index, \(t\mapsto z_i+t h w_i\) is nonconstant; consequently \(1+\cos(z_i+t h w_i)\) is not identically zero and its integral against \(1-t\) is strictly positive. Hence
\[
V(F_hz)<V(z)\quad\Longleftrightarrow\quad\sin z\ne0,
\qquad 0<h\leq2/\Lambda.
\tag{2}
\]
This uses the genuine curvature variation of the cosine along the step, unlike a constant-Hessian upper bound, whose coefficient vanishes at equality.

**Step 2: all forward trajectories converge below and at equality.** Since \(V\) is bounded below, \(V(F_h^nz)\) is convergent and its consecutive differences tend to zero. By (2), compactness, and continuity of the difference, every accumulation point lies in \(S=\{0,\pi\}^d\). In particular, the distance of the trajectory to \(S\) tends to zero. Also \(F_h(z)-z=hKA\sin z\) on a periodic lift, so the torus step distance tends to zero. Select disjoint small closed neighborhoods of the finitely many points of \(S\), separated by a positive gap. Eventually all iterates lie in their union and every step is smaller than the gap, so no transitions between neighborhoods remain possible. The trajectory therefore converges to one point of \(S\). Each point of \(S\) is fixed; conversely (2) makes every fixed point belong to \(S\) in this parameter range. Strict decrease excludes a cycle of length greater than one.

Any point not in \(S\) has a neighborhood on which the first-step loss in \(V\) exceeds the entire neighborhood's variation in \(V\), making it wandering. Thus the nonwandering set is precisely \(S\), and the standard localization of topological entropy to the nonwandering set yields zero entropy.

**Step 3: every nonsink binary equilibrium has an expanding direction.** For \(p\in S\), put \(D_p=\operatorname{diag}(\cos p_1,\ldots,\cos p_d)\). The derivative is \(DF_h(p)=I+hKAD_p\). The real matrix \(KAD_p\) is similar to the real symmetric matrix \(K^{1/2}AD_pK^{1/2}\). Sylvester's inertia law gives the same numbers of positive and negative eigenvalues as \(AD_p\). If \(p\ne p_*\), some coordinate of \(p\) equals zero, so \(KAD_p\) has a positive eigenvalue \(\mu\). Hence \(DF_h(p)\) has an eigenvalue \(1+h\mu>1\), for every \(h>0\). This remains valid when some **other** eigenvalue of \(DF_h(p)\) is zero or has modulus one.

**Step 4: analytic null preimages and the full-measure basin.** The Jacobian determinant \(\det DF_h(z)\) is a real-analytic function of \(z\). At the all-zero binary point \(p_0\), it equals \(\det(I+hKA)>0\): indeed \(KA\) is similar to the positive-definite symmetric matrix \(A^{1/2}KA^{1/2}\). Thus \(\det DF_h\) is not identically zero. Its zero locus has Haar measure zero. Off that locus the inverse function theorem supplies countably many local inverse charts; consequently the inverse image under \(F_h\) of every Haar-null Borel set is Haar-null (the Luzin \(N^{-1}\) property).

For a \(C^1\) map whose derivative at a fixed point has at least one eigenvalue of modulus greater than one, the **endomorphism version of the local center-stable theorem** gives a neighborhood and a null local center-stable set containing every point whose entire future remains in that neighborhood. Crucially, this theorem does not require that the full derivative be invertible. An orbit converging to the fixed point eventually remains in that neighborhood, so its initial point belongs to a countable union of preimages of the local null set. These preimages are null by the previous paragraph; therefore the fixed point's complete basin is null. This general theorem and the \(N^{-1}\) globalization are stated explicitly in Muşat--Boumal (2026 revision), Theorems 4--6.

Apply this to every \(p\in S\setminus\{p_*\}\). Step 2 proves that all orbits converge to \(S\); Step 3 shows all competing basins are null. Since \(S\) is finite, the complement of \(\mathcal B_h(p_*)\) is null for \(0<h\le2/\Lambda\). The strict global minimum of \(V\) at \(p_*\), together with monotonicity and the positive potential gap outside each sufficiently small neighborhood, also proves Lyapunov stability.

**Step 5: the sharp supercritical reversal.** At \(p_*\), \(D_{p_*}=-I\), so
\[
DF_h(p_*)=I-hKA.
\]
The matrix \(KA\) has positive real eigenvalues and largest eigenvalue \(\Lambda\). For \(h>2/\Lambda\), one eigenvalue of the derivative is \(1-h\Lambda<-1\). Reapply Step 4's local endomorphism center-stable theorem and the analytic \(N^{-1}\) property. It follows that \(\mathcal B_h(p_*)\) is null for every such \(h\). Combining both sides proves the claimed sharp inclusive threshold.

## Verification

Identity (1) is an exact integral Taylor identity, not a numerical approximation. The crucial strictness depends on \(K\) being nonsingular and on the analytic cosine curvature having no nonconstant interval on which it equals \(-1\). The spectral comparison follows from the Rayleigh quotient of \(A^{1/2}KA^{1/2}\); the inertia statement follows from congruence by \(K^{1/2}\). At the nonlinear and noninvertible parameter values, the null-basin step uses the **non-diffeomorphism** center-stable result and the independently verified analytic regular-point property, not a stable-manifold theorem requiring an invertible map.

The standalone Python script `CHECK.py` evaluates (1) with a direct cosine integral quadrature on a two-dimensional weighted path example, tests strict loss at the endpoint on noncritical points, and checks derivative multipliers. Its finite checks are corroboration only; the all-dimensional statements are proved above.

## Relationship to prior work

Buescu, D'Aniello, and Oliveira, *Morse--Smale dynamics in discrete Huygens networks* (arXiv:2610.10993v1, publicly posted 2026-10-07), construct the separated cosine potential. Their Theorem 3.2 proves strict descent for the **open** interval \(0<h<2/\Lambda\), their Proposition 3.4 proves convergence there, and their Theorem 3.7/Corollary 5.2 give a full-measure sink basin under the smaller invertibility condition \(0<h<1/\Lambda\). Their Corollary 5.3 shows that the phase-opposition point ceases to be a sink above \(2/\Lambda\), without a measure-zero basin conclusion. The present exact remainder closes the endpoint and the analytic null-preimage argument establishes basin behavior across the noninvertible regime; it does **not** claim the source's Morse--Smale transversality conclusion there.

Schaeffer and McCalla, *Extending the step-size restriction for gradient descent to avoid strict saddle points* (arXiv:1908.01753v1), provide a null-basin approach for \(\alpha L\in(0,2)\), excluding the endpoint. Muşat and Boumal, *Gradient descent avoids strict saddles with a simple line-search method too* (arXiv:2507.13804v3, 2026 revision), provide general endomorphism center-stable and null-preimage theorems, and prove saddle avoidance for almost all constant step sizes. These techniques are **used**, not claimed as new; their statements alone do not imply the present critical-step Lyapunov identity or full-measure convergence at the specific exceptional endpoint. Accessible similar work on discrete phase-network critical rates and analytic torus-map injectivity addresses different properties rather than this exact basin threshold.

## Limitations

This result concerns the explicit analytic cosine family with \(K\) symmetric positive definite and \(A\) positive diagonal. It does not prove structural stability or Morse--Smale transversality at noninvertible parameter values. The supercritical assertion is only that the prescribed equilibrium \(p_*\) has a null basin: other fixed points resulting from nonzero torus winding, cycles, or attractors can exist at large \(h\), and their global dynamics is not classified. At the critical step no uniform exponential convergence rate is claimed. The proof requires the general local center-stable theorem and the fact that a nontrivial real-analytic zero set is null. Independent mathematical or priority validation has not been performed.

## References

1. J. Buescu, E. D'Aniello, and H. M. Oliveira, *Morse--Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, 2026-10-07. https://arxiv.org/html/2610.10993
2. H. Schaeffer and S. G. McCalla, *Extending the step-size restriction for gradient descent to avoid strict saddle points*, arXiv:1908.01753v1, 2019-08-05. https://arxiv.org/abs/1908.01753
3. A.-A. Muşat and N. Boumal, *Gradient descent avoids strict saddles with a simple line-search method too*, arXiv:2507.13804v3, 2026-09-22, especially Theorems 4--7. https://arxiv.org/html/2507.13804v3
