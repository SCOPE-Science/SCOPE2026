# Sharp Gaussian fluctuations of the intrinsic-volume index of a simplex vertex cone

## Finding
For the simplicial cone \(D_m=\operatorname{pos}\{e_0-e_i:1\le i\le m\}\subset\mathbb R^{m+1}\), let \(J_m\) be its conic intrinsic-volume index: \(\Pr(J_m=k)=v_k(D_m)\). As the integer \(m\to\infty\),
\[
\boxed{\frac{J_m-2\log m}{2\sqrt{\log m}}\Longrightarrow N(0,1)},\quad
\boxed{\mathbb E J_m\sim2\log m},\quad
\boxed{\operatorname{Var}(J_m)\sim4\log m}.
\]
In particular, \(\operatorname{Var}(J_m)/(2\mathbb E J_m)\to1\), making this natural cone sequence an asymptotic saturator of McCoy–Tropp's universal conic variance bound. The theorem concerns conic intrinsic volumes, not the ordinary Euclidean intrinsic volumes of a simplex.

## Assumptions and scope
The vectors \(e_0,\ldots,e_m\) form the standard orthonormal basis of \(\mathbb R^{m+1}\). The cone \(D_m\) is the tangent cone at a vertex of a regular \(m\)-simplex (up to reflection). It has \(m\) linearly independent generating rays; the ambient one-dimensional orthogonal complement does not alter intrinsic volumes. Denote the standard normal density and upper tail by \(\phi(t)=(2\pi)^{-1/2}\exp(-t^2/2)\) and \(\overline\Phi(t)=\int_t^\infty\phi(u)\,du\). For each \(m\), the equation
\[
 m[\phi(t_m)-t_m\overline\Phi(t_m)]=t_m
\]
has exactly one positive solution \(t_m\). Put \(\lambda_m=m\overline\Phi(t_m)\). In addition to the boxed formulas, the proof establishes
\[
 \frac{J_m-\lambda_m}{t_m}\Longrightarrow N(0,2),\qquad
 \frac{\mathbb E J_m-\lambda_m}{t_m}\longrightarrow0.
\]
There are no finite-dimensional Gaussian approximations or uniform convergence rates asserted here.

## Proof
**1. Exact Gaussian face-count representation.** Let \(G_0,\ldots,G_m\) be independent standard normal variables and let \(Z_i=-G_i\) for \(1\le i\le m\). Projection of \(G=(G_0,\ldots,G_m)\) onto \(D_m\) has the unique form \(\sum_{i=1}^m a_i(e_0-e_i)\), with \(a_i=(Z_i-S_m)_+\). The scalar \(S_m\) is the unique real solution of
\[
 H_m(S_m)=G_0+S_m,\qquad H_m(s)=\sum_{i=1}^m(Z_i-s)_+.
\]
Indeed, this is exactly the complementary-slackness system for minimizing the strictly convex projection objective, and \(H_m(s)-s-G_0\) decreases continuously from positive infinity to negative infinity. Because the rays are linearly independent and Gaussian ties have probability zero, the dimension of the face containing the projection is \(N_m(S_m)=\sum_{i=1}^m\mathbf1_{\{Z_i>S_m\}}\). The standard Gaussian projection characterization of conic intrinsic volumes therefore gives
\[
 J_m\stackrel{d}=N_m(S_m).
\]
This identity is for all integers \(m\ge1\), including the zero-dimensional face.

**2. Deterministic threshold and tail moments.** Write \(h(t)=\mathbb E(Z-t)_+=\phi(t)-t\overline\Phi(t)\), for standard normal \(Z\). Since \(h\) decreases continuously, \(m h(t)=t\) has one positive root \(t_m\). The classical normal-tail expansions yield, as \(t\to\infty\),
\[
 h(t)=\frac{\phi(t)}{t^2}\bigl(1+O(t^{-2})\bigr),\qquad
 \overline\Phi(t)=\frac{\phi(t)}t\bigl(1+O(t^{-2})\bigr),
\]
\[
 \mathbb E(Z-t)_+^2=\frac{2\overline\Phi(t)}{t^2}(1+o(1)),\qquad
 \mathbb E(Z-t)_+^3=O(\overline\Phi(t)t^{-3}).
\]
The equation \(m h(t_m)=t_m\) implies
\[
 t_m^2=2\log m+O(\log\log m),\quad
 \lambda_m=m\overline\Phi(t_m)\sim t_m^2,\quad
 m\phi(t_m)/t_m^3\to1.
\]
In fact \(\lambda_m-2\log m=O(\log\log m)=o(t_m)\). All these statements concern the limit \(m\to\infty\); finite small \(m\) need not have large \(t_m\).

**3. A two-dimensional rare-event central limit theorem.** Abbreviate \(t=t_m\), \(\lambda=\lambda_m\), and define
\[
 X_m=\frac{N_m(t)-\lambda}{t},\qquad Y_m=H_m(t)-t.
\]
Here \(\mathbb E Y_m=0\) exactly. Independence over \(i\), the formulas in step 2, and \(m h(t)=t\) give
\[
 \operatorname{Var}X_m\to1,\quad \operatorname{Var}Y_m\to2,\quad
 \operatorname{Cov}(X_m,Y_m)=\frac{m h(t)(1-\overline\Phi(t))}{t}\to1.
\]
For each fixed linear combination of the two coordinates, the sum of the centered absolute third moments of its independent summands is \(O(t^{-1})\). This follows from \(m\overline\Phi(t)\asymp t^2\) and the third tail moment above. Lyapunov's theorem and Cramér–Wold yield
\[
 (X_m,Y_m)\Longrightarrow (X,Y),\qquad
 \operatorname{Cov}(X,Y)=\begin{pmatrix}1&1\\1&2\end{pmatrix}.
\]
The independent \(G_0\) remains independent of this Gaussian vector.

**4. Expansion of the random threshold and count.** Since \(N_m(t)/t^2\to1\) in probability and \(Y_m-G_0=O_{\Pr}(1)\), monotonicity of \(H_m(s)-s-G_0\) first brackets its root within \(t\pm K/t^2\), with arbitrarily high probability for sufficiently large fixed \(K\). On this interval the number of \(Z_i\) lies in a window of width \(2K/t^2\) has expectation \(O(Kt)\), so the derivative of \(H_m\) differs from \(-N_m(t)\) by at most \(O_{\Pr}(t)=o_{\Pr}(t^2)\). Substitution into the root equation gives the precise expansion
\[
 t^2(S_m-t)=Y_m-G_0+o_{\Pr}(1).
\]
For every fixed \(K\), the centered empirical counts on the window \([t-K/t^2,t+K/t^2]\) are uniformly \(o_{\Pr}(t)\): partition it into finitely many intervals of mesh \(\varepsilon/t^2\), use binomial variances \(O(t)\) at the grid points, and sandwich intermediate points by monotonicity; then let \(\varepsilon\downarrow0\). A Taylor expansion of the normal tail now shows
\[
 \frac{N_m(S_m)-N_m(t)}{t}
 =-\frac{m\phi(t)}{t^3}\,t^2(S_m-t)+o_{\Pr}(1)
 =-Y_m+G_0+o_{\Pr}(1).
\]
Therefore \((J_m-\lambda_m)/t_m\Longrightarrow X-Y+G_0\), a centered normal of variance \(1+2+1-2=2\). Since \(t_m\sim\sqrt{2\log m}\) and \(\lambda_m-2\log m=o(t_m)\), the claimed explicitly centered and scaled central limit theorem follows.

**5. Mean and variance, with matching sharp constant.** The preceding convergence implies \(J_m/t_m^2\to1\) in probability. Let \(\delta_m=\mathbb E J_m\). McCoy–Tropp's universal bound \(\operatorname{Var}(J_m)\le2\delta_m\) is valid for every closed convex cone. If \(\delta_m\) stayed bounded on a subsequence, Markov's inequality would contradict \(J_m\to\infty\) in probability. Hence \(\delta_m\to\infty\); Chebyshev with that variance bound yields \(J_m/\delta_m\to1\), and thus \(\delta_m/t_m^2\to1\). In particular, both \((J_m-\lambda_m)/t_m\) and \((J_m-\delta_m)/t_m\) are tight, so the deterministic differences \((\delta_m-\lambda_m)/t_m\) are bounded.

McCoy–Tropp's exponential moment bound states, for real \(\eta\),
\[
 \mathbb E\exp\{\eta(J_m-\delta_m)\}\le
 \exp\left\{\frac{\delta_m}{2}(e^{2\eta}-2\eta-1)\right\}.
\]
Taking \(\eta=\pm c/t_m\) for any fixed \(c>0\), using \(\delta_m/t_m^2\to1\), proves uniform exponential integrability of \((J_m-\delta_m)/t_m\), hence uniform integrability of all its fixed powers. Along any subsequence on which \((\delta_m-\lambda_m)/t_m\to a\), step 4 implies \((J_m-\delta_m)/t_m\Longrightarrow N(-a,2)\). Uniform integrability and the exact zero mean force \(a=0\). It follows that \((\delta_m-\lambda_m)/t_m\to0\), and uniform integrability of squares gives
\[
 \frac{\operatorname{Var}(J_m)}{t_m^2}\longrightarrow2.
\]
With \(t_m^2\sim2\log m\) and \(\delta_m\sim2\log m\), this proves the other two boxed conclusions and \(\operatorname{Var}(J_m)/(2\delta_m)\to1\).

## Verification
The supplementary `verify.py` computes the unique deterministic threshold, independently reconstructs Gaussian projection face counts by sorting and by a scalar root, verifies the associated Karush–Kuhn–Tucker equations, and compares empirical sample moments with the predicted large-sample normalization at several dimensions. The finite computations are not substitutes for the Lyapunov theorem, empirical-process window argument, or uniform-integrability proof; the latter are analytic.

## Relationship to prior work
McCoy and Tropp (arXiv:1308.5265, Theorems 4.5 and 4.8) established the universal conic variance and exponential-moment bounds invoked in step 5. Goldstein, Nourdin and Peccati (arXiv:1411.6265) established a general CLT for conic intrinsic-volume indices centered by their **actual** means and scaled by their **actual** standard deviations; their worked examples do not include this vertex cone or its explicit logarithmic normalizations. Kabluchko and Seidel (arXiv:2006.09492, Theorem 2.4) gave exact finite-dimensional intrinsic volumes for related simplex-generated cones, but no explicit high-dimensional fluctuation law for this regular-simplex vertex cone in the inspected article. The present result identifies the deterministic centering, exact leading variance, and sharp saturation of the universal variance bound in this family; a generic CLT without evaluation of the mean and variance does not supply those parameters. An earlier equivalent asymptotic hidden in other literature remains possible.

## Limitations
The result is asymptotic for the specified regular-simplex vertex cones only. It does not supply finite-dimensional error rates, a local limit theorem, or universality over arbitrary simplex shapes. The prior-literature search is nonexhaustive, and equivalent unpublished or unlocated asymptotics cannot be ruled out. The probabilistic verifier samples finite instances and does not certify any asymptotic assertion. No independent external audit has been performed.

## References
1. M. B. McCoy and J. A. Tropp, *From Steiner Formulas for Cones to Concentration of Intrinsic Volumes*, arXiv:1308.5265, first public 24 August 2013, especially Theorems 4.5 and 4.8.
2. L. Goldstein, I. Nourdin, G. Peccati, *Gaussian Phase Transitions and Conic Intrinsic Volumes: Steining the Steiner Formula*, arXiv:1411.6265, first public 23 November 2014, especially Theorem 1.1 and Table 1.
3. Z. Kabluchko and H. Seidel, *Convex Cones Spanned by Regular Polytopes*, arXiv:2006.09492, first public 16 June 2020, especially Theorem 2.4.
