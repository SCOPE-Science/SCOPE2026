# Exact finite-population spectrum and slow relaxation of reactive Stuart–Landau polygons

## Finding
Consider \(M\geq3\) identical Stuart–Landau oscillators with purely reactive all-to-all diffusive coupling:
\[
\dot z_j=(\beta+i\omega-k|z_j|^2)z_j+i\gamma\sum_{\ell\ne j}(z_\ell-z_j),\qquad
\beta,k>0,\quad \gamma\in\mathbb R\setminus\{0\}.
\]
For any \(u_1,\dots,u_M\in\mathbb C\), \(|u_j|=1\), with \(\sum_j u_j=0\), the rotating polygon \(z_j(t)=\sqrt{\beta/k}\,u_j\exp(i(\omega-M\gamma)t)\) is an exact solution. Set
\[
Q=M^{-1}\sum_{j=1}^M u_j^2,\qquad q=|Q|,\qquad h=M\gamma.
\]
For a **noncollinear polygon**, equivalently \(q<1\), its full \(2M\)-dimensional real co-rotating characteristic polynomial is exactly
\[
\boxed{\chi(\lambda)=[\lambda(\lambda+2\beta)]^{M-2}
\bigl([\lambda(\lambda+2\beta)]^2+h^2[(\lambda+\beta)^2-\beta^2q^2]\bigr).}
\]
Both \(0\) and \(-2\beta\) are semisimple eigenvalues, each of multiplicity \(M-2\); the four remaining eigenvalues lie strictly in the open left half-plane for **every** \(\gamma\ne0\) and every noncollinear polygon. The \((M-2)\)-dimensional smooth local polygon equilibrium manifold is normally attracting. Trajectories starting sufficiently close to a given noncollinear polygon converge exponentially, in its rotating frame, to some (possibly different) polygonal equilibrium.

There is a sharp universal weak-decay law as the polygon approaches collinearity. The unique collective eigenvalue tending to zero as \(q\uparrow1\) satisfies
\[
\boxed{\lambda_{\mathrm{slow}}(q)=-\tfrac{\beta}{2}(1-q^2)+O((1-q^2)^2).}
\]
Its leading coefficient is independent of population size and coupling strength. For every even \(M\ge4\), noncollinear balanced antipodal-pair configurations realize \(q\uparrow1\).

## Assumptions and scope
All oscillators share exactly the same positive growth \(\beta\), cubic saturation \(k\), and natural frequency \(\omega\). The real part of coupling and the nonlinear frequency shift both vanish; the imaginary coupling \(\gamma\) is nonzero and can have either sign. The polygon has all \(M\) amplitudes nonzero, obeys complex closure, and is noncollinear (the \(u_j\) are not all contained in one real line through the origin). The exact spectrum concerns the full real Jacobian, not a phase-only reduction or an infinite-population limit. When \(\omega-M\gamma\ne0\) the co-rotating eigenvalues are Floquet exponents of the physical periodic orbit, whose period is \(2\pi/|\omega-M\gamma|\); at zero rotating frequency the same spectrum describes an equilibrium.

## Proof
**1. Exact polygon and regularity.** The coupling is \(i\gamma(MZ-z_j M)\), where \(Z=M^{-1}\sum_jz_j\). On the rotating polygon the mean field vanishes, the amplitude is \(\sqrt{\beta/k}\), and its frequency is \(\omega-M\gamma\). Rotating by that frequency gives the autonomous equation
\[
\dot w_j=(\beta-k|w_j|^2)w_j+i\gamma\sum_\ell w_\ell.
\]
Its equilibria include \(w_j^*=\sqrt{\beta/k}\,u_j\), with \(\sum_j u_j=0\). The two real polygon closure equations have rank two in angular variables exactly when the unit vectors do not all lie on one real line. Indeed, their derivative columns are \(iu_j\). Also, equality in the triangle inequality \(|M^{-1}\sum_j u_j^2|\le1\) holds if and only if all \(u_j^2\) are equal, precisely the collinear case. The implicit function theorem gives a smooth equilibrium manifold of dimension \(M-2\) when \(q<1\).

**2. Jacobian and finite-rank reduction.** Denote perturbations by \(v_j\) and \(S=\sum_jv_j\). The *exact* linearization at the polygon is
\[
\dot v_j=-\beta(v_j+u_j^2\overline{v_j})+i\gamma S.
\]
Its real-linear complexification acts on independent variables \((v_j,\overline v_j)\). Deleting the collective coupling produces \(M\) identical characteristic factors \(d(\lambda)=\lambda(\lambda+2\beta)\). For \(d(\lambda)\ne0\), inversion of each two-dimensional local block and summation give the collective compatibility equations
\[
\begin{pmatrix}
 d(\lambda)-ih(\lambda+\beta)&-ih\beta Q\\
 ih\beta\overline Q&d(\lambda)+ih(\lambda+\beta)
\end{pmatrix}
\begin{pmatrix}S\\\overline S\end{pmatrix}=0.
\]
Their determinant is \(P(\lambda)=d(\lambda)^2+h^2[(\lambda+\beta)^2-\beta^2|Q|^2]\). The matrix determinant lemma for this rank-two coupling therefore yields \(\det(\lambda I-J)=d(\lambda)^{M-2}P(\lambda)\). Both sides are polynomials, so the formula also holds at the excluded values \(d(\lambda)=0\).

**3. Zero and radial eigenspaces.** At a noncollinear polygon, \(P(0)=P(-2\beta)=h^2\beta^2(1-q^2)>0\). Angular vectors \(v_j=iu_jt_j\) with real \(\sum_j u_jt_j=0\) give \(M-2\) independent eigenvectors for eigenvalue zero. Radial vectors \(v_j=u_js_j\) with real \(\sum_j u_js_j=0\) give \(M-2\) independent eigenvectors for eigenvalue \(-2\beta\). Algebraic and geometric multiplicities agree, so these eigenvalues are semisimple.

**4. Strict transverse decay.** Expanding the remaining factor gives
\[
P(\lambda)=\lambda^4+4\beta\lambda^3+(4\beta^2+h^2)\lambda^2
+2\beta h^2\lambda+\beta^2h^2(1-q^2).
\]
The nontrivial Routh–Hurwitz determinants are
\[
4\beta(4\beta^2+h^2)-2\beta h^2=16\beta^3+2\beta h^2>0
\]
and
\[
4\beta(4\beta^2+h^2)(2\beta h^2)
-(2\beta h^2)^2-(4\beta)^2\beta^2h^2(1-q^2)
=16\beta^4h^2(1+q^2)+4\beta^2h^4>0.
\]
All four quartic coefficients are strictly positive when \(q<1\). Thus all four roots have negative real parts. The standard local stable-foliation theorem for a smooth manifold of equilibria with semisimple tangential zeros and strictly stable normal spectrum proves exponential convergence to some nearby polygon in the co-rotating frame. No claim is made of attraction to a predetermined polygon.

**5. Sharp collinear slowdown.** Put \(\varepsilon=1-q^2\). At \((\lambda,\varepsilon)=(0,0)\), \(P=0\), \(\partial_\lambda P=2\beta h^2\ne0\), and \(\partial_\varepsilon P=\beta^2h^2\). The implicit function theorem produces a unique simple eigenvalue branch with \(\mathrm d\lambda/\mathrm d\varepsilon=-\beta/2\), proving the stated asymptotic. Its three companion roots remain strictly stable at \(q=1\), by the cubic Routh test. For even \(M\ge4\), take \(M/2\) unit vectors in a narrow angular sector and include their negatives. Closure holds, the polygon is noncollinear if two directions differ, and \(q\to1\) as the sector shrinks. The coefficient \(-\beta/2\) is therefore attained as a genuine shape-degeneration limit.

## Verification
The standalone `verify_spectrum.py` uses exact rational arithmetic to reconstruct an eight-by-eight real Jacobian for a four-oscillator polygon with \(q=3/5\) and verify its entire characteristic polynomial; checks both quartic Hurwitz determinants and the weak-decay derivative; and independently compares direct Jacobian spectra for closed configurations with \(M=3,4,5,6,8\). Run `python verify_spectrum.py` with SymPy, NumPy and SciPy. Exact matrix identities are finite verifications, while the all-population theorem and nonlinear convergence follow from the analytical proof above.

## Relationship to prior work
Zhao and Uchida, arXiv:2610.08239v1 (first public 2026-10-06), identify polygonal zero-order-parameter motions, their dimension, and the full Jacobian as the appropriate stability object; they use numerical polygon sampling for transverse stability. Existence and manifold dimension are *not* claimed as new here. León and Pazó, arXiv:2006.02159 (2020), derive quadrupolar-order-parameter-dependent stability boundaries for incoherent states, substantially anticipating the relevance of \(q\). Their treatment studies the thermodynamic limit and quasi-phase reduction and does not state this exact full finite-\(M\) characteristic factorization, its semisimple eigenvalue counts, or the coupling-independent collinearity slowdown. Ku, Girvan and Ott, arXiv:1412.3803 (2014), study globally coupled identical oscillators and clump/chaos transitions with other coefficients. The present contribution is the exact finite-dimensional characteristic identity plus its sharp near-collinear decay consequence, **not** a first discovery of incoherent-state stability or second-harmonic dependence.

## Limitations
The theorem assumes homogeneous growth, purely reactive coupling, no amplitude-dependent frequency, and \(q<1\). No uniform rate is asserted as \(q\to1\), and the nonlinear behavior *at* collinearity is not classified. The result establishes local, not global, attraction. A historical-priority risk remains from the earlier quadrupolar stability literature, including Chabanol–Hakim–Rappel (1997), whose full-text comparison was not completed because retrieval failed; independent mathematical and historical validation has not been performed.

## References
1. L. Zhao and N. Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators*, arXiv:2610.08239v1, 2026-10-06, https://arxiv.org/abs/2610.08239 (especially Section 5).
2. I. León and D. Pazó, *Quasi phase reduction of all-to-all strongly coupled λ–ω oscillators near incoherent states*, arXiv:2006.02159, 2020, https://arxiv.org/abs/2006.02159 (especially Sections IV.3.2 and V.1.3).
3. W. L. Ku, M. Girvan and E. Ott, *Dynamical transitions in large systems of mean field-coupled Landau–Stuart oscillators*, arXiv:1412.3803, 2014, https://arxiv.org/abs/1412.3803.
4. M.-L. Chabanol, V. Hakim and W.-J. Rappel, *Collective chaos and noise in the globally coupled complex Ginzburg–Landau equation*, Physica D 103 (1997), 273–293. Full text not materially inspected in this review.
