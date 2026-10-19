# Complete linearized inertia of balanced polygonal Stuart–Landau states under dissipative mean-field coupling

## Finding

Consider \(M\geq3\) Stuart–Landau oscillators with strictly positive real mean-field coupling and no reactive or nonlinear-frequency-shift term:
\[
\dot z_j=(\beta_j+i\omega-\kappa |z_j|^2)z_j
  +c\sum_{\ell\ne j}(z_\ell-z_j),\qquad
j=1,\ldots,M.
\]
Suppose \(c>0\), \(\kappa>0\), \(\omega\in\mathbb R\), and \(\beta_j>Mc\) for every \(j\). At any balanced phase-locked solution
\[
z_j(t)=e^{i\omega t}w_j,\qquad
\sum_j w_j=0,\qquad
|w_j|^2=\frac{\beta_j-Mc}{\kappa},
\]
write \((n_+,n_-,n_0)\) for the respective numbers of positive, negative and zero eigenvalues of the real \(2M\)-dimensional Jacobian in the frame rotating at frequency \(\omega\), including common-phase neutrality.

**The complete inertia classification is**
\[
(n_+,n_-,n_0)=
\begin{cases}
(2,M,M-2),&\text{if the vectors }w_j\text{ are not collinear},\\
(1,M,M-1),&\text{if collinear and }\tau<1,\\
(1,M-1,M),&\text{if collinear and }\tau=1,\\
(2,M-1,M-1),&\text{if collinear and }\tau>1,
\end{cases}
\qquad
\tau=\frac c2\sum_{j=1}^M\frac1{\beta_j-Mc}.
\]
Thus **all such balanced solutions are linearly unstable**, with precisely two expanding real directions at every noncollinear polygon, independent of its geometry and amplitude heterogeneity. At a noncollinear polygon the \(M-2\) zero eigenvalues are exactly tangent to the smooth manifold of balanced polygons, so it is a normally hyperbolic saddle manifold locally. The collinear strata have a sharp, explicit transition in unstable dimension at \(\tau=1\).

## Assumptions and scope

All \(M\) oscillators are active, since \(\beta_j>Mc\). A balanced solution is considered only when its positive lengths \(r_j=\sqrt{(\beta_j-Mc)/\kappa}\) admit a closed polygon. No existence assertion is made for length lists failing polygon closure. The vectors are collinear when all \(w_j\) lie on one real line through the origin in \(\mathbb C\); otherwise they span \(\mathbb R^2\). The angular frequency \(\omega\) is arbitrary and is removed by an exact co-rotating change of variables. The inertia counts eigenvalues with multiplicity; none are complex because the Jacobian is real symmetric.

## Proof

Write \(a_j=\beta_j-Mc>0\), \(w_j(t)=e^{-i\omega t}z_j(t)\), and \(S=\sum_j w_j\). The exact co-rotating vector field is
\[
\dot w_j=(a_j-\kappa|w_j|^2)w_j+cS.
\]
For a fixed balanced polygon the two equilibrium conditions are \(S=0\) and \(a_j=\kappa|w_j|^2\). Identifying each complex coordinate with a real two-vector, the derivative at this equilibrium is
\[
(Jv)_j=c\sum_{\ell=1}^M v_\ell
      -2\kappa(w_j\cdot v_j)w_j.
\]
Consequently its symmetric quadratic form is
\[
\langle v,Jv\rangle
=c\left|\sum_jv_j\right|^2
-2\kappa\sum_j(w_j\cdot v_j)^2.\tag{1}
\]
Introduce linear maps \(T:(\mathbb R^2)^M\to\mathbb R^2\), \(Tv=\sum_jv_j\), and \(U:(\mathbb R^2)^M\to\mathbb R^M\), \((Uv)_j=w_j\cdot v_j\). Equation (1) reads \(c\|Tv\|^2-2\kappa\|Uv\|^2\). It immediately bounds the positive index by \(2\) and negative index by \(M\), since \(\operatorname{rank}T=2\) and \(\operatorname{rank}U=M\) (all \(w_j\ne0\)).

First suppose the \(w_j\) are not collinear. Their ninety-degree rotations \(iw_j\), treated as real two-vectors, span \(\mathbb R^2\). The tangential subspace \(\ker U=\{(t_j iw_j)_j:t_j\in\mathbb R\}\) therefore maps **onto** \(\mathbb R^2\) under \(T\). Choose a two-dimensional subspace of \(\ker U\) on which \(T\) is injective. Equation (1) is strictly positive on every nonzero vector therein, so the positive index equals \(2\).

For the negative index, prescribe arbitrary real numbers \(b_1,\ldots,b_M\) and take \(v_j^{(0)}=b_j w_j/|w_j|^2\); thus \(Uv^{(0)}=b\). Surjectivity of \(T|_{\ker U}\) supplies \(t\in\ker U\) with \(Tt=-Tv^{(0)}\). The vector \(v=v^{(0)}+t\) then satisfies \(Tv=0\), \(Uv=b\). Choosing these vectors linearly in \(b\) yields an \(M\)-dimensional subspace where equation (1) equals \(-2\kappa\|b\|^2<0\) for \(b\ne0\). Hence the negative index equals \(M\), and the remaining \(2M-(M+2)=M-2\) eigenvalues vanish.

The balanced polygon family is locally the intersection of the \(M\) fixed-radius equations and the two real closure equations. The radius constraints are independent, and the derivative of closure on their tangential space is surjective precisely when the polygon is noncollinear. By the submersion theorem the family is a smooth manifold of dimension \(M-2\). Its tangent vectors differentiate a family of equilibria and therefore lie in \(\ker J\). Since the nullity has exactly this dimension, the nullspace is *only* the tangent space, proving the asserted normal hyperbolicity and Morse–Bott nondegeneracy of the equilibrium manifold.

Now suppose all \(w_j\) lie on a common real line. Rotate coordinates so \(w_j=(s_jr_j,0)\), with \(s_j\in\{-1,1\}\) and \(r_j>0\). Reorder coordinates into all longitudinal (real) and all transverse (imaginary) components. The Jacobian becomes the direct sum
\[
J_{\parallel}=-2\operatorname{diag}(a_1,\ldots,a_M)
                         +c\boldsymbol1\boldsymbol1^{\mathsf T},
\qquad
J_{\perp}=c\boldsymbol1\boldsymbol1^{\mathsf T}.
\]
The transverse block has one positive eigenvalue and \(M-1\) zeros. Let \(D=\operatorname{diag}(a_1,\ldots,a_M)\), and let \(u_j=1/\sqrt{a_j}\). A real congruence gives
\[
D^{-1/2}J_{\parallel}D^{-1/2}
=-2I_M+cuu^{\mathsf T}.
\]
This matrix has \(M-1\) strictly negative eigenvalues and one remaining eigenvalue
\[
-2+c\|u\|^2
=2(\tau-1),\qquad
\tau=\frac c2\sum_j a_j^{-1}.
\]
Sylvester's law of inertia then gives the three collinear cases after adding the transverse block. Every row of the classification has at least one strictly positive eigenvalue, proving instability.

For a concrete singular boundary, set \(M=4\), \(\beta_j=\beta>0\), and take the balanced collinear configuration with signs \((+,-,+,-)\). It exists for \(0<c<\beta/4\). Here \(\tau=2c/(\beta-4c)\), so its unstable dimension changes from one to two exactly at \(c=\beta/6\), with an extra zero eigenvalue at the boundary. In contrast, every noncollinear four-sided polygon with the same lengths has unstable dimension two throughout its existence interval.

## Verification

The accompanying `verify.py` uses only Python's standard library. It constructs the Jacobian directly from the defining co-rotating cubic vector field and determines its signature by **exact rational congruence elimination**, not floating-point eigenvalue thresholds. It also checks polynomial directional differences (including the explicit cubic truncation error), equilibrium closure, and every predicted inertia case for deterministic noncollinear and collinear examples.

Reproduce with `python3 verify.py`; the tested package reports `VERIFY_OK: exact rational polynomial/Jacobian/inertia/closure assertions = 3504`. These are finite consistency tests of the displayed algebra. They are not substituted for the all-\(M\) proof.

## Relationship to prior work

Zhao and Uchida (arXiv:2610.08239v1, first posted October 6, 2026) derive the same model, its gradient-flow reduction for real coupling (Sec. 3), and the manifold of closed-polygon zero-order-parameter states (Sec. 5). Their transverse stability treatment uses sampled Jacobians in a regime with generally nonzero reactive coupling; it does not give the complete inertia classification for the strictly dissipative, all-active regime proved here. Those established structural ingredients and the polygon dimension are prior work, not part of the new claim.

Kemeth and collaborators (arXiv:1807.11231v2) derive stability boundaries for synchronized and regular splay states and analyze two-cluster transverse modes in mean-field coupled systems, primarily with identical individual oscillators. Ku, Girvan, and Ott (arXiv:1412.3803v1) analyze incoherent and clustered regimes and their linearizations in related mean-field models. Their stated results do not determine the all-size, arbitrary-heterogeneity polygon inertia or the explicit collinear threshold. The congruence and rank arguments above supply that classification.

## Limitations

The theorem assumes strictly **positive** real coupling, strictly positive nonlinear saturation, and all-active oscillators. It says nothing about nonzero imaginary coupling or nonlinear frequency shifts, partly active polygons, or nonlinear/global dynamics outside the local equilibrium neighborhood. The collinear threshold describes linearized inertia; a zero eigenvalue at \(\tau=1\) does not alone prove any particular nonlinear bifurcation. Earlier equivalent results in specialized literature cannot be excluded by finite literature searches. Independent scientific validation has not been performed.

## References

1. L. Zhao and N. Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators*, arXiv:2610.08239v1 (first posted 2026-10-06), Sections 2, 3, and 5. https://arxiv.org/html/2610.08239v1
2. A. Kemeth et al., *Cluster singularity: the unfolding of clustering behavior in globally coupled Stuart-Landau oscillators*, arXiv:1807.11231v2, Sections II–III. https://arxiv.org/html/1807.11231v2
3. W. L. Ku, M. Girvan, and E. Ott, *Dynamical Transitions in Large Systems of Mean Field-Coupled Landau-Stuart Oscillators: Extensive Chaos and Clumped States*, arXiv:1412.3803v1, Sections II–IV. https://arxiv.org/html/1412.3803v1
