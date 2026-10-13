# A sharp transverse-stability barrier and ordered-polar equilibrium census for cubic opinion amplification

## Finding

**Theorem (full two-dimensional ordered-polar classification).** In the equal-group two-community bounded-confidence model of Bakim (2026), with the cubic amplification law, let \(\alpha,\beta>0\) and \(0<\varepsilon\leq1\). An *interacting ordered-polar equilibrium* means \(0<x<y<1\), \(0<y-x<\varepsilon\), and both time derivatives zero. Such an equilibrium is locally asymptotically stable in the full two-dimensional system **if and only if**
\[
\varepsilon>\frac1{\sqrt3},\qquad
\alpha>3\beta,\qquad
1-\frac{2\beta}{\alpha}<\varepsilon^2.
\]
For \(0<\varepsilon<1\), the latter two inequalities are exactly
\[
3\beta<\alpha<\frac{2\beta}{1-\varepsilon^2}.
\]
When \(\varepsilon=1\), the upper endpoint is absent. In that parameter region, there is **exactly one** stable interacting ordered-polar equilibrium, namely
\[
(x_*,y_*)=\left(\frac{1-\delta_*}{2},\frac{1+\delta_*}{2}\right),\qquad
\delta_* =\sqrt{1-\frac{2\beta}{\alpha}}.
\]
Its full-system eigenvalues (in original time) are \(3\beta-\alpha\) and \(2\beta-\alpha\). For \(2\beta<\alpha<3\beta\), when this equilibrium lies strictly within the confidence region, it is instead a **saddle**, despite being attracting along the invariant midpoint line. At \(\alpha=3\beta\), when the branch is within the confidence region, it is nonlinearly unstable.

For completeness, **all** interacting ordered-polar equilibria with strictly positive gap belong to the symmetric family above, or to one of two asymmetric families. The latter occur precisely if \(\alpha>3\beta\) and their gap \(\tfrac12\sqrt{1+\beta/\alpha}\) lies strictly below \(\varepsilon\). Writing \(k=\beta/\alpha\), the two asymmetric equilibria are
\[
(x,y)=\left(\frac{1+s-d}{2},\frac{1+s+d}{2}\right),\qquad
s=\pm\frac12\sqrt{1-3k},\quad d=\frac12\sqrt{1+k}.
\]
Each is a saddle. Equality \(\alpha=3\beta\) merges both with the symmetric branch, rather than adding distinct equilibria. Reversing the group labels gives the reverse-ordered equivalents.

In particular, for the published illustrative confidence threshold \(\varepsilon=0.3\), **no asymptotically stable interacting partial-polarization equilibrium exists for any** \(\alpha,\beta>0\). At \(\beta=1\), \(\alpha=2.1\), the reported partial-polarization branch has gap \(1/\sqrt{21}<0.3\), yet its full-system eigenvalues are \(0.9\) and \(-0.1\): it is a saddle, not an attractor.

## Assumptions and scope

The two opinion means \(x(t),y(t)\) range over \([0,1]\) and obey the model's published equations (4)--(6) for equal group shares \(p=1/2\):
\[
\dot x=\tfrac12\gamma(x,y)(y-x)+\alpha A(x),\qquad
\dot y=\tfrac12\gamma(x,y)(x-y)+\alpha A(y),
\]
where \(A(z)=z(1-z)(2z-1)\), and \(\gamma(x,y)=\beta\) when \(|y-x|\leq\varepsilon\), and \(\gamma(x,y)=0\) otherwise. The strict inequality \(0<y-x<\varepsilon\) guarantees a smooth neighborhood, so ordinary local asymptotic stability has an unambiguous classical meaning. For an interacting fixed point *on* the switching surface \(y-x=\varepsilon\), the one-sided noninteracting gap derivative equals \(\beta\varepsilon>0\), excluding Lyapunov stability from the noninteracting side. We adopt the published convention that the interaction is on at equality, and make no Filippov-sliding claims.

Here *polarized* means two different group means, not necessarily that an arbitrary initial condition converges to that fixed point. This is a two-dimensional mean-field result, not a theorem for arbitrary agent networks, unequal group shares, or arbitrary amplification functions.

## Proof

**1. Exact polynomial reduction.** Put \(k=\beta/\alpha\), define shifted midpoint \(s=x+y-1\) and opinion gap \(d=y-x>0\), and rescale time by \(\tau=\alpha t/2\). In the interacting region, the exact equations (without Taylor approximation) are
\[
\frac{ds}{d\tau}=s(1-s^2-3d^2),\qquad
\frac{dd}{d\tau}=d(1-2k-3s^2-d^2).\tag{1}
\]
The open ordered-opinion triangle is \(d>0\), \(|s|+d<1\). This change of variables is invertible and uses positive time scaling.

**2. Exhaustive equilibrium classification.** For \(d>0\), equation (1) says either \(s=0\) or \(s^2+3d^2=1\); the second equation requires \(3s^2+d^2=1-2k\). In the first case, \(d^2=1-2k\), yielding exactly the symmetric polar branch if \(0<k<1/2\). In the other case, solving the two linear equations in the squares gives
\[
s^2=\frac{1-3k}{4},\qquad d^2=\frac{1+k}{4}.
\]
For positive \(k\), distinct asymmetric branches exist iff \(0<k<1/3\). They lie in the open opinion triangle because
\[
(|s|+d)^2=\frac{1-k+\sqrt{(1-3k)(1+k)}}2<1.
\]
Every branch also must meet the independent strict confidence condition \(d<\varepsilon\). No further interacting ordered-polar equilibria exist because the polynomial equations have been exhausted.

**3. Exact linear stability.** The Jacobian in \((s,d)\) and scaled time is
\[
J=\begin{pmatrix}
1-3s^2-3d^2&-6sd\\
-6sd&1-2k-3s^2-3d^2
\end{pmatrix}.
\]
At the symmetric polar branch, the eigenvalues in scaled time are \(6k-2\) and \(4k-2\), hence \(3\beta-\alpha\) and \(2\beta-\alpha\) in physical time. Since the branch exists for \(\alpha>2\beta\), its gap eigenvalue is always negative; its midpoint eigenvalue is positive for \(2\beta<\alpha<3\beta\) and negative for \(\alpha>3\beta\). At either asymmetric equilibrium, the scaled-time Jacobian has
\[
\operatorname{tr}J=k-1<0,\qquad
\det J=2(1+k)(3k-1)<0,
\]
so both asymmetric equilibria are saddles.

**4. Nonhyperbolic threshold.** At \(k=1/3\), the symmetric branch has \(s=0\), \(d_0=1/\sqrt3\), one zero eigenvalue, and one strictly negative eigenvalue. The local center manifold is
\[
d=d_0-\frac{3\sqrt3}{2}s^2+O(s^4),
\]
which follows by matching the quadratic coefficients in its invariance equation. Substitution in the exact first equation gives
\[
\frac{ds}{d\tau}=8s^3+O(s^5).
\]
Thus \(s=0\) repels along the center manifold and is not locally asymptotically stable. This applies when \(\varepsilon>1/\sqrt3\); at equality with the switching gap the outward one-sided argument below applies.

**5. Strict confidence boundary and sharp feasibility.** At any equilibrium with \(d=\varepsilon>0\), the interacting gap derivative is zero by definition; immediately on the noninteracting side the difference of the two right-hand sides is \(\beta d>0\), so arbitrarily close trajectories on that side move away and the switching point cannot be locally asymptotically stable. Hence stable partial polarization requires \(d<\varepsilon\). The only possible stable branch is symmetric, and its two negative eigenvalues require \(\alpha>3\beta\). Since \(d^2=1-2\beta/\alpha>1/3\) in that regime, there is some such branch inside the confidence region iff \(\varepsilon>1/\sqrt3\). The displayed parameter inequalities are equivalent to these conditions; if satisfied, smooth hyperbolicity proves local exponential asymptotic stability. This proves the claimed necessary and sufficient classification.

## Verification

The included `verify.py` is a stand-alone SymPy program that symbolically reconstructs (1), the symmetric-branch eigenvalues, the asymmetric-branch equilibrium and Jacobian identities, and the cubic center-manifold coefficient. It also checks both contrasting rational parameter choices: the saddle with \((\alpha/\beta,\varepsilon)=(21/10,3/10)\) and the stable interacting branch with \((\alpha/\beta,\varepsilon)=(4,4/5)\). The checker returns `VERIFY_OK` with SymPy. These finite checks support but do not substitute for the all-parameter algebraic proof above.

## Relationship to prior work

Bakim (2026), equations (4)--(8), correctly supplies the cubic mean-field equations and the invariant midpoint restriction. Its Theorems 2 and 3 and Fig. 2 label the polarization branch stable upon its appearance at \(\alpha=2\beta\), using a scalar gap equation. The present result differs by assessing **both** independent perturbation directions, proving the sharp additional threshold \(\alpha=3\beta\), deriving the confidence feasibility barrier \(\varepsilon>1/\sqrt3\), and finding two previously unlisted asymmetric saddle branches. The source's scalar pitchfork formula on the invariant midpoint line is not disputed.

Earlier network models by Baumann and collaborators (2020) use unbounded opinions, nonlinear influence, and network homophily; their polarized states can be metastable, but their governing field is not Bakim's two-community bounded-confidence cubic. Lim and Bentley (2022) study discrete-time social opinion amplification on networks, a distinct update law. Sîrbu et al. (2019) use a pair-selection bias in a mean-field Deffuant model rather than the cubic self-amplification drift. None of these works implies the specific full-system stability criterion or exact algebraic branch census above. The generic principle that invariant-subspace stability does not imply full-dimensional stability is standard and is not asserted to be new.

## Limitations

The theorem addresses local behavior of *ordinary equilibria* for equal group sizes. It does not establish global basins, compare relative prevalence of competing attractors, determine sliding states under an alternative Filippov interpretation, or extend the result to unequal group fractions or stochastic agent-based dynamics. The discontinuity at confidence equality makes global trajectory assertions especially sensitive to solution conventions. Broader abstract classifications of exchange-symmetric coupled cubic systems may contain related statements, so a complete novelty guarantee beyond the compared literature is not asserted.

## References

1. S. Bakim, "Mathematical Modeling of Opinion Dynamics under Algorithmic Amplification: A Bifurcation Analysis," *Black Sea Journal of Engineering and Science* **9** (2026), 1230--1242, published 2026-05-15, doi:10.34248/bsengineering.1882307. Open full text: https://dergipark.org.tr/en/download/article-file/5686662.
2. F. Baumann, P. Lorenz-Spreen, I. M. Sokolov, M. Starnini, "Modeling Echo Chambers and Polarization Dynamics in Social Networks," *Physical Review Letters* **124** (2020), 048301; preprint arXiv:1906.12325.
3. S. L. Lim and P. J. Bentley, "Opinion amplification causes extreme polarization in social networks," *Scientific Reports* **12** (2022), 18131, doi:10.1038/s41598-022-22856-z.
4. A. Sîrbu, D. Pedreschi, F. Giannotti, J. Kertész, "Algorithmic bias amplifies opinion fragmentation and polarization: A bounded confidence model," *PLOS ONE* **14** (2019), e0213246, doi:10.1371/journal.pone.0213246.
