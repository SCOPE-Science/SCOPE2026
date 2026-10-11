# Pitchfork phase diagram of the excluded sliding pseudo-equilibria
## Finding
For the symmetric zero-divergence three-dimensional piecewise-linear Filippov family introduced in arXiv:2609.33034, fix \(\mu>0\) and \(0<H<1\). On strict attractive sliding use
\[
s=x-y>0,\qquad d=x+y,\qquad |d|<s.
\]
The sliding field is
\[
\dot s=H-1-2\mu\frac{d^2}{s}+\frac{\kappa}{2s}(s^2-d^2),\qquad
\dot d=d\left(\frac{1+H}{s}-2\mu\right).
\]
Define
\[
\kappa_c=\frac{4\mu(1-H)}{1+H}.
\]
Then the complete interior pseudo-equilibrium diagram is:

- for \(\kappa\le0\), no pseudo-equilibrium;
- for \(0<\kappa<\kappa_c\), exactly one pseudo-equilibrium \(P_0=(2(1-H)/\kappa,0)\), a hyperbolic saddle;
- for \(\kappa=\kappa_c\), the same point is nonhyperbolic with eigenvalues \(\kappa_c/2\) and \(0\);
- for \(\kappa>\kappa_c\), \(P_0\) is a hyperbolic source and there are exactly two additional pseudo-equilibria
\[
s=\frac{1+H}{2\mu},\qquad
d=\pm\frac{1+H}{2\mu}\sqrt{\frac{\kappa-\kappa_c}{\kappa+4\mu}},
\]
both hyperbolic saddles.

At \(\kappa=\kappa_c\) the sliding field undergoes a nondegenerate supercritical \(d\mapsto-d\) pitchfork. With \(a=1-H\), \(b=1+H\), \(\varepsilon=\kappa-\kappa_c\), and \(u=s-2a/\kappa\), the reduced center equation is
\[
\dot d=\frac{b}{2a}\varepsilon d-\frac{16\mu^3}{ab^2}d^3+O(\varepsilon^2|d|+|\varepsilon|d^3+d^5).
\]

## Assumptions and scope
The statement concerns the source's Filippov-preserving zero-divergence normal form, with \(\mu>0\), \(0<H<1\), and the strict attractive-sliding region \(s>0\), \(|d|<s\). It classifies zeros and their local type for every real \(\kappa\). It does not alter the source's crossing-cycle classification and makes no assertion about escaping motion or continuation through the two-fold.

## Proof
For \(\kappa\le0\), the strict inequality \(s^2-d^2>0\) gives directly
\[
\dot s=-(1-H)-2\mu\frac{d^2}{s}+\frac{\kappa}{2s}(s^2-d^2)<0,
\]
so no interior zero exists.

Now let \(\kappa>0\). If \(d=0\), the first equation is \(\dot s=-(1-H)+\kappa s/2\), hence the unique zero is
\[
P_0:\qquad s_0=\frac{2(1-H)}{\kappa},\qquad d_0=0.
\]
If \(d\ne0\), the second equation forces
\[
s_*=\frac{1+H}{2\mu}.
\]
Substituting this value into the first equation and putting \(r=d^2/s_*^2\) gives
\[
r=\frac{\kappa-\kappa_c}{\kappa+4\mu}.
\]
Thus such zeros exist exactly when \(\kappa>\kappa_c\). Then \(0<r<1\), so both signs of \(d\) lie strictly inside the sliding cone and give exactly the displayed pair.

For \(\kappa>0\), set \(Q=2\mu+\kappa/2\). The Jacobian in \((s,d)\) is
\[
J=\begin{pmatrix}
\kappa/2+Qd^2/s^2&-2Qd/s\\
-(1+H)d/s^2&(1+H)/s-2\mu
\end{pmatrix}.
\]
At \(P_0\), its eigenvalues are
\[
\lambda_1=\frac{\kappa}{2},\qquad
\lambda_2=\frac{1+H}{2(1-H)}(\kappa-\kappa_c).
\]
This yields the saddle, nonhyperbolic, and source alternatives. At either off-axis zero the lower-right entry vanishes and
\[
\det J=-\frac{2Q(1+H)d^2}{s^3}<0,
\]
so each is a hyperbolic saddle.

It remains to identify the threshold bifurcation. Let \(a=1-H\), \(b=1+H\), \(\varepsilon=\kappa-\kappa_c\), and translate along the central branch by \(u=s-2a/\kappa\). At \(\varepsilon=0\) the nonzero eigenvalue is \(\kappa_c/2>0\). The center manifold has
\[
u=\frac{4\mu}{ab}d^2+O(d^4).
\]
Substitution in the \(d\)-equation yields
\[
\dot d=\frac{b}{2a}\varepsilon d-\frac{16\mu^3}{ab^2}d^3+O(\varepsilon^2|d|+|\varepsilon|d^3+d^5).
\]
Both leading coefficients have the signs required for a nondegenerate supercritical pitchfork. The exact off-axis branch found above agrees with the resulting square-root onset.

## Verification
Every equilibrium is obtained by the exact factorization of the second sliding equation into \(d=0\) or \(s=(1+H)/(2\mu)\). The strict-cone condition is checked explicitly by \((\kappa-\kappa_c)/(\kappa+4\mu)<1\). Stability follows from the exact Jacobian, and the pitchfork coefficient follows from a direct quadratic center-manifold substitution. No numerical sampling, partial enumeration, or computer-assisted certificate is used as proof.

## Relationship to prior work
The motivating paper derives the displayed sliding system and proves that the strict attractive-sliding region has no interior pseudo-equilibria exactly when \(\kappa\le0\). For \(\kappa>0\) it exhibits the diagonal zero \(P_0\) only to show that the no-pseudo-equilibrium hypothesis fails; its global theorem then assumes the positive-\(\kappa\) obstruction away. The complete number, location, stability type, exact threshold, and pitchfork normal form in that excluded sector are not stated there.

Generic literature on Filippov boundary-equilibrium and sliding bifurcations supplies broad local frameworks and model-specific examples, but the checked sources do not imply this exact phase diagram for the symmetric zero-divergence visible-visible two-fold family. In particular, the threshold depends simultaneously on the source parameters \(\mu\) and \(H\) through the specific two-dimensional sliding field above.

## Limitations
This is a complete local phase diagram for interior pseudo-equilibria of the stated sliding field, not a global classification of trajectories when \(\kappa>0\). The two off-axis saddles need not determine all global separatrix connections, and no claim is made about how their invariant manifolds interact with folds or the two-fold. The originality comparison cannot exclude an equivalent calculation hidden in unindexed notes or under different terminology.

## References
1. S. C. S. Ferreira, *Global classification of oscillatory dynamics in symmetric zero-divergence 3D piecewise-linear Filippov systems with a visible-visible two-fold*, arXiv:2609.33034, first public 2026-09-27. See the Filippov-preserving normal form, equation (12), and Lemma 1.
2. D. J. W. Simpson, *A general framework for boundary equilibrium bifurcations of Filippov systems*, arXiv:1804.11036.
3. R. Cristiano, T. Carvalho, D. J. Tonon, D. J. Pagano, *Hopf and Homoclinic Loop Bifurcations on a DC-DC Boost Converter under a SMC Strategy*, arXiv:1510.06611.
