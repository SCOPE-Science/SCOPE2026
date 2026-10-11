# Sharp finite-jet pre-Schwarzian distortion for an exponential-sine derivative class

## Finding

Put \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(\Phi(w)=e^w(1+\sin w)\). For an integer \(m\ge1\), let \(\mathcal D_m\) consist of normalized holomorphic functions \(f\) on \(\mathbb D\) satisfying \(f(0)=0\) and \(f'(z)=\Phi(\omega(z))\) for a Schwarz function \(\omega:\mathbb D\to\mathbb D\) with \(\omega(z)=O(z^m)\) at the origin. These functions are locally univalent, because \(\Phi\) has no zeros on \(\mathbb D\). Write \(T_f=f''/f'\).

For every \(m\ge1\) and every \(0<r<1\), the exact radial envelope is
\[
\sup_{f\in\mathcal D_m}\sup_{|z|=r}(1-r^2)|T_f(z)|
=\max_{0\le s\le r^m}
\left(\frac{m(1-r^2)s}{r}+r^m-\frac{s^2}{r^m}\right)(1+\sec s+\tan s).
\]
Every maximizing \(s\) on the right is realized by an explicit disk automorphism in the construction below (or by a constant Schwarz factor at the endpoint). The displayed equality is exact, not an approximation or a non-sharp upper estimate.

In particular, the sharp full-disk pre-Schwarzian norm is *independent of the prescribed finite order of vanishing*:
\[
\boxed{\displaystyle\sup_{f\in\mathcal D_m}\|T_f\|
=(1-r_*^2)(1+\sec r_*+\tan r_*)=2.14565700788682\ldots}
\]
for every integer \(m\ge1\), where \(\|T_f\|=\sup_{z\in\mathbb D}(1-|z|^2)|T_f(z)|\) and \(r_*\) is the unique solution in \((0,1)\) of
\[
(1-r^2)\sec r(\sec r+\tan r)=2r(1+\sec r+\tan r).
\]
The root satisfies \(0.27327758<r_*<0.27327760\). For \(m=1\), \(\omega(z)=-z\) attains this bound at \(z=r_*\). For \(m\ge2\), no interior point of any function in \(\mathcal D_m\) attains the upper bound, although the class supremum remains exactly the same.

## Assumptions and scope

Subordination here is defined by the explicit Schwarz-function representation; *global univalence is not assumed*. The source paper's univalent class is a subclass of \(\mathcal D_1\), but the claim concerns the locally univalent ambient derivative-subordination class, with arbitrary finite Taylor-jet vanishing. In fact \(f(z)=z+O(z^{m+1})\). No assertions about global univalence of the constructed finite Blaschke examples are required or made.

The relevant denominator \(1+\sin w\) is nonzero when \(|w|<1\), since its nearest zero to the origin has modulus \(\pi/2\). Thus \(\Phi(w)\ne0\) and all logarithmic derivatives used below are well-defined. At radius \(r=0\), the radial envelope is \(2\) for \(m=1\) and \(0\) for \(m\ge2\).

## Proof

**1. A positive-coefficient reduction.** Set \(U(w)=\sec w+\tan w\). On \(|w|<1\),
\[
U'(w)=\frac{1+U(w)^2}{2},\qquad U(0)=1.
\]
Writing \(U(w)=\sum_{n\ge0}u_nw^n\), coefficient comparison gives \(u_0=1\), \(u_1=1\), and, for \(n\ge1\),
\[
(n+1)u_{n+1}=\frac12\sum_{j=0}^n u_ju_{n-j}>0.
\]
Hence every \(u_n\) is positive. Moreover,
\[
\frac{\Phi'(w)}{\Phi(w)}
=1+\frac{\cos w}{1+\sin w}=1+U(-w).
\]
The triangle inequality therefore yields, for \(s=|w|<1\),
\[
\left|\frac{\Phi'(w)}{\Phi(w)}\right|\le1+U(s)=1+\sec s+\tan s.
\]
For \(s>0\), equality requires \(w=-s\), because the constant and strictly positive first-order terms of \(1+U(-w)\) must have the same argument. Equality holds at \(w=-s\).

**2. Exact radial optimization.** The order-\(m\) Schwarz lemma gives \(\omega(z)=z^m\eta(z)\) with a Schur function \(\eta:\mathbb D\to\overline{\mathbb D}\). At \(|z|=r>0\), put \(s=|\omega(z)|\le r^m\), so \(|\eta(z)|=s/r^m\). The Schwarz--Pick inequality applied to \(\eta\) gives
\[
\begin{aligned}
(1-r^2)|\omega'(z)|
&\le m(1-r^2)r^{m-1}|\eta(z)|+r^m(1-r^2)|\eta'(z)|\\
&\le\frac{m(1-r^2)s}{r}+r^m-\frac{s^2}{r^m}.
\end{aligned}
\]
Combining this with Step 1 and \(T_f=(\Phi'/\Phi)(\omega)\omega'\) gives the asserted upper envelope.

The bound is attained for each \(s\in[0,r^m)\): put \(v=-s/r^m\), \(c=(r+v)/(1+rv)\in(-1,1)\), and
\[
\eta(z)=\frac{c-z}{1-cz},\qquad \omega(z)=z^m\eta(z).
\]
Then \(\eta(r)=v\), \(\eta'(r)=-(1-v^2)/(1-r^2)<0\), \(\omega(r)=-s\), and both terms in \(\omega'(r)\) are nonpositive real numbers. Thus equality holds in every preceding inequality. If \(s=r^m\), choose the constant \(\eta\equiv-1\). Integrating \(f'(z)=\Phi(\omega(z))\) with \(f(0)=0\) produces the required member of \(\mathcal D_m\). Compactness of \([0,r^m]\) proves existence of a maximizing \(s\).

**3. Unique global constant.** Applying Schwarz--Pick directly to \(\omega\) yields
\[
(1-|z|^2)|T_f(z)|\le G(|\omega(z)|),\qquad
G(s)=(1-s^2)(1+U(s)).
\]
Let \(R(s)=2s(1+U(s))/((1-s^2)\sec s\,U(s))\) for \(0<s<1\). Since \(U'=\sec s\,U\),
\[
\frac{R'(s)}{R(s)}=
\frac1s+\frac{2s}{1-s^2}-\tan s-\frac{\sec s}{1+U(s)}>0.
\]
Indeed \(\sec s/(1+U(s))<1<1/s\), and \(\tan s\le s/(1-s^2/2)<2s/(1-s^2)\) for \(0<s<1\). As \(R(s)\) increases from \(0\) to \(+\infty\), it crosses \(1\) exactly once, at \(s=r_*\). Differentiating \(G\) shows \(G'(s)\) has the sign of \(1-R(s)\); hence \(r_*\) is its unique global maximizer and \(G(r_*)\) is the universal bound.

For \(m=1\), choose \(\omega(z)=-z\) and evaluate at \(z=r_*\). For every fixed \(m\ge2\), set \(s=r_*\), choose \(R\in(s^{1/m},1)\), and let
\[
c_R=\frac{R-s/R^m}{1-sR^{1-m}},\qquad
\omega_R(z)=z^m\frac{c_R-z}{1-c_Rz}.
\]
Here \(c_R\in(-1,1)\), \(\omega_R(R)=-s\), and direct differentiation gives
\[
(1-R^2)|\omega_R'(R)|
=\frac{ms(1-R^2)}R+R^m-\frac{s^2}{R^m}
\longrightarrow1-s^2.
\]
Consequently the corresponding normalized primitives satisfy \((1-R^2)|T_{f_R}(R)|\to G(r_*)\), proving sharpness for every \(m\). Finally, for \(m\ge2\), equality at an interior point would force equality in Schwarz--Pick for \(\omega\), hence \(\omega\) would be a disk automorphism. This contradicts \(\omega'(0)=0\), proving the interior nonattainment assertion.

## Verification

The standalone standard-library script `verify_pre_schwarzian.py` checks a rational bracket for the unique critical radius using alternating Taylor bounds for \(\sin\) and \(\cos\), reproduces the displayed numerical constant, and verifies the disk-automorphism identities by exact rational arithmetic on representative parameters. These finite checks support numerical localization and algebraic reproducibility; the analytic positivity, sharpness, all-orders quantifier, and uniqueness proofs are in Steps 1--3 and do not rest on experiments.

## Relationship to prior work

Das and Sarkar (arXiv:2607.25280v1, v2) study initial logarithmic/inverse coefficients and Hankel/Toeplitz determinants for the *globally univalent* class defined by \(f'\prec e^z(1+\sin z)\). They do not state the radial pre-Schwarzian envelope or the finite-jet invariance proved here. The pre-Schwarzian norm and Schwarz--Pick/Dieudonné methods are classical; Kim and Sugawa and subsequent work develop norm bounds for other close-to-convex or Ma--Minda families. The reduction to a Schwarz function is therefore not claimed as new in isolation. The assessed object-specific conclusions are the sharp simultaneous radial formula for every vanishing order, its explicit Blaschke equality construction, and the exact common global constant.

## Limitations

No assertion is made that all primitives in \(\mathcal D_m\) are globally univalent. The radial maximization remains a one-real-variable maximum, not a closed-form algebraic optimizer for each separate \((m,r)\). The full-disk constant is characterized by a transcendental equation rather than elementary closed form. Prior generic pre-Schwarzian distortion theory may offer alternative routes to the upper envelope; complete absence of equivalent unpublished or poorly indexed work is not established. Only the stated analytic and locally univalent class is proved.

## References

1. P. Das and N. Sarkar, *Coefficient Problems and Sharp Determinant Estimates for the Class* \(\mathcal P^*\), arXiv:2607.25280v1 (first public July 28, 2026), revised v2 August 30, 2026. https://arxiv.org/abs/2607.25280
2. Y. C. Kim and T. Sugawa, *Norm estimates of the pre-Schwarzian derivatives for certain classes of univalent functions*, Proc. Edinburgh Math. Soc. 49 (2006), 131--143, DOI:10.1017/S0013091504000306.
3. M. F. Ali, M. Nurezzaman and S. Pal, *Pre-Schwarzian norm estimate for certain Ma-Minda Class of functions*, arXiv:2409.20216.
4. R. Biswas, *Pre-Schwarzian norm estimation for functions in the Ma-Minda-type starlike and convex classes*, arXiv:2505.01910.
