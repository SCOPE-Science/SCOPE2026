# Opposite directional kurtosis signs in chiral four-heading transport

## Finding

Let \(\mathbf X_T=(X_T,Y_T)\) be the displacement of a four-heading velocity-jump particle. Its heading takes values \(j\in\{0,1,2,3\}\), with velocity \(v(\cos(\pi j/2),\sin(\pi j/2))\), speed \(v>0\), and independent clockwise/counterclockwise turn clocks of rates \(a>0\), \(b>0\). Every turn changes heading by exactly a quarter revolution. Put \(s=a+b\), \(d=a-b\), \(R=s^2+d^2\), and \(\chi=d/s\in(-1,1)\). For \(Z_T(\theta)=X_T\cos\theta+Y_T\sin\theta\), the stationary-heading long-time cumulant rates are

\[
\lim_{T\to\infty}\frac{\kappa_2(Z_T(\theta))}{T}=\frac{v^2s}{R},\qquad
\lim_{T\to\infty}\frac{\kappa_4(Z_T(\theta))}{T}=3v^4\left(\frac{s(3d^2-s^2)}{R^3}-\frac{\sin^2(2\theta)}{sR}\right).
\]

The effective diffusion coefficient is isotropic, \(D_{\mathrm{eff}}=v^2s/(2R)\), yet all diagonal directions have strictly negative fourth-cumulant rate. The cardinal axes have positive fourth-cumulant rate precisely when \(|\chi|>1/\sqrt3\), or equivalently \(a/b>2+\sqrt3\) or \(a/b<2-\sqrt3\). In this regime the precise positive angular sectors are

\[
\sin^2(2\theta)<\frac{3\chi^2-1}{(1+\chi^2)^2}.
\]

At sector boundaries the rate is zero, and elsewhere it is negative. For weaker chirality, the rate is strictly negative for every angle except at the critical chirality and exact cardinal axes, where it vanishes. The radial Gaussian fourth-moment deficit is nevertheless always negative:

\[
\lim_{T\to\infty}\frac{\mathbb E|\mathbf X_T|^4-2(\mathbb E|\mathbf X_T|^2)^2}{T}
=-\frac{4v^4(1-\chi^2)(3-\chi^2)}{s^3(1+\chi^2)^3}<0.
\]

Thus the same process can have positive asymptotic excess kurtosis along fixed axes, negative along diagonals, and a negative rotationally aggregated excess-kurtosis numerator. For any fixed noncritical direction, the finite-time excess-kurtosis sign agrees with the stated rate for all sufficiently large \(T\).

## Assumptions and scope

The particle moves freely in the whole Euclidean plane, with no translational Brownian noise, walls, position resets, or initial displacement. The independent turn clocks operate in every heading. Headings form the irreducible four-state continuous-time chain with generator

\[
(Qf)(j)=a[f(j+1)-f(j)]+b[f(j-1)-f(j)],
\]

where indices are modulo four. The initial heading is chosen uniformly, the unique invariant distribution. All limits hold for each fixed \(v,a,b>0\), direction \(\theta\in\mathbb R\), and \(T\to\infty\). For finite \(T\), the distribution is fourfold rotation-invariant but not fully isotropic. The radial deficit is not itself a normalized kurtosis; its sign remains negative after division by the positive squared radial second moment.

## Proof

**Principal spectral branch.** For the projected displacement, Feynman–Kac applies to the finite tilted generator

\[
M_\theta(k)=Q+kv\,\operatorname{diag}(\cos\theta,\sin\theta,-\cos\theta,-\sin\theta).
\]

Direct exact evaluation, using \(z\) for the spectral variable, gives

\[
\det(zI-M_\theta(k))=
 z(z+2s)[(z+s)^2+d^2]-(kv)^2(z+s)^2
 +(kv)^4\cos^2\theta\sin^2\theta.
\]

At \(k=0\) the four eigenvalues are \(0\), \(-2s\), and \(-s\pm id\). Hence the eigenvalue zero is simple and strictly separated in real part from all others. The analytic eigenvalue \(\lambda_\theta(k)\) with \(\lambda_\theta(0)=0\) is the long-time logarithmic moment-generating-function rate near \(k=0\). Analytic perturbation of this finite matrix, or direct substitution in the determinant, yields

\[
\lambda_\theta(k)=\frac{v^2s}{2R}k^2+
\frac{v^4}{8}\left(\frac{s(3d^2-s^2)}{R^3}-\frac{\sin^2(2\theta)}{sR}\right)k^4+O(k^6).
\]

The odd powers vanish because a two-step heading rotation changes the sign of the projected speed while preserving the rate law. Smooth spectral perturbation and its uniform exponentially decaying remainder justify differentiating the long-time scaled logarithmic moment generating function through fourth order. Multiplying its quadratic and quartic Taylor coefficients by \(2!\) and \(4!\) proves the projected cumulant assertions.

**Sharp directional signs.** The axial fourth rate has sign \(3d^2-s^2\). Solving \(3(a-b)^2>(a+b)^2\) in the positive ratio \(a/b\) gives the two disjoint intervals separated by \(2\pm\sqrt3\). For a diagonal, the negative of the relevant numerator is \(R^2-s^2(3d^2-s^2)=2s^4-s^2d^2+d^4>0\), because \(d^2<s^2\). In general, multiplying the projected fourth rate by a strictly positive factor gives the sign of \((3\chi^2-1)/(1+\chi^2)^2-\sin^2(2\theta)\); this proves the exact angular sectors and endpoints.

**Radial contraction.** The full two-variable spectral branch has homogeneous expansion

\[
\lambda(k_x,k_y)=\frac{v^2s}{2R}(k_x^2+k_y^2)+\frac{v^4}{8}\left[
\frac{s(3d^2-s^2)}{R^3}(k_x^2+k_y^2)^2-
\frac{4k_x^2k_y^2}{sR}\right]+O(\|(k_x,k_y)\|^6).
\]

At each \(T\), quarter-turn invariance gives \(\mathbb E X_T=\mathbb E Y_T=0\), \(\mathbb E X_TY_T=0\) and equal coordinate variances. Expanding centered fourth moments therefore gives the exact identity

\[
\mathbb E|\mathbf X_T|^4-2(\mathbb E|\mathbf X_T|^2)^2
=\kappa_{xxxx}(T)+\kappa_{yyyy}(T)+2\kappa_{xxyy}(T).
\]

Taking four derivatives of the homogeneous quartic yields

\[
\lim_{T\to\infty}\frac{\kappa_{xxxx}+\kappa_{yyyy}+2\kappa_{xxyy}}T
=\frac{4v^4(4s^2d^2-3s^4-d^4)}{sR^3}
=-\frac{4v^4(1-\chi^2)(3-\chi^2)}{s^3(1+\chi^2)^3}.
\]

Since \(|\chi|<1\), the last expression is strictly negative. Every claimed limit and sign follows.

## Verification

The accompanying standalone `CHECKER.py` symbolically reconstructs the full fourth-cumulant tensor and radial contraction and verifies the exact critical ratio. Separately from the characteristic determinant calculation, it solves the finite-state tilted Poisson recursions through fourth order for six different pairs of positive rational turning rates and three independent projection directions, with exact arithmetic. It also checks representative regions on both sides of the threshold. The recorded exact output is `PASS: 236 exact algebraic and independent Poisson-recursion checks`. These calculations cross-check, rather than replace, the analytic determinant and strict-inequality proof; no finite experimental sample is used to infer universal validity.

## Relationship to prior work

Loewe, Kozhukhov, and Shendruk studied four-cardinal-direction run-and-tumble-turn dynamics and hydrodynamic fourth-order anisotropy for symmetric clockwise/counterclockwise turns, with a distinct appendix on unequal horizontal/vertical relaxation. The present result changes the *handedness* of the quarter-turn clocks and gives explicit directional fourth-cumulant sectors and a negative radial deficit under the same parameters. Sevilla's continuum-orientation model allows asymmetric turning-angle distributions and develops angle-resolved transport methods, but its rotationally uniform initial headings do not fix a four-axis lattice orientation; the proposed result concerns laboratory-axis directional signs. Villa-Torrealba and coauthors treat partial-reorientation velocity-jump processes and non-Gaussian measures but do not state this finite-four-heading, handed-turn sign classification. The general spectral perturbation method is standard and is not claimed as new. A wider analysis of chiral discrete-state persistent walks could contain an equivalent unstated formula; see limitations.

## Limitations

The result is asymptotic for a fixed four-heading process and fixed positive rates; it does not classify all finite-time kurtosis signs, does not describe the singular unidirectional limits \(a=0\) or \(b=0\), and does not prove a thermodynamic phase transition. The angular fourth cumulant concerns displacement along a fixed lab-frame direction, not the rotationally averaged marginal. Scholarly originality is subject to independent priority assessment, particularly for general finite-state Markov additive-functional formulas and earlier chiral four-velocity models.

## References

1. B. Loewe, T. Kozhukhov, and T. N. Shendruk, *Anisotropic run-and-tumble-turn dynamics*, arXiv:2305.03663, first posted 2023-05-05; https://arxiv.org/abs/2305.03663. Open full text: https://www.pure.ed.ac.uk/ws/portalfiles/portal/403664786/anisotropic_run_tumble.pdf.
2. F. J. Sevilla, *Two-dimensional active motion*, arXiv:1905.07090, https://arxiv.org/pdf/1905.07090.
3. A. Villa-Torrealba et al., *Run-and-tumble bacteria slowly approaching the diffusive regime*, arXiv:2002.02872, https://arxiv.org/pdf/2002.02872.
