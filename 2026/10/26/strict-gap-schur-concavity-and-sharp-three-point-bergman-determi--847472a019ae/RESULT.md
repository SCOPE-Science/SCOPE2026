# Strict gap Schur concavity and sharp three-point Bergman determinant on a circle

## Finding
For the analytic Bergman space of the unit disk with normalized area, use the reproducing kernel \(K(z,w)=(1-z\overline w)^{-2}\). Fix \(0<r<1\), write \(t=r^2\), and take any three (possibly coincident) sites \(z_j=r e^{i\theta_j}\). Their normalized evaluation-kernel Gram matrix is
\[
B_{jk}=\frac{K(z_j,z_k)}{\sqrt{K(z_j,z_j)K(z_k,z_k)}}=\frac{(1-t)^2}{(1-z_j\overline {z_k})^2}.
\]
Then the following bound is sharp for every radius:
\[
0\le \det B\le \frac{81t^3(t^3+2)(2t^3+1)}{(1+t+t^2)^6}.
\]
Equality on the right holds if and only if the sites are an equally spaced three-point orbit on the circle, up to relabeling and common rotation. More strongly, for pairwise distinct sites, let \(\alpha,\beta,\gamma>0\) be their counterclockwise successive angular gaps, so \(\alpha+\beta+\gamma=2\pi\). The function \(\log\det B\) is **strictly Schur concave** in these gaps: replacing any two unequal gaps by a strictly more equal pair, keeping their sum fixed and both positive, strictly increases the determinant. Hence its unique gap maximizer is \((2\pi/3,2\pi/3,2\pi/3)\).

The maximal determinant has the limiting laws \(\max\det B\sim162r^6\) as \(r\downarrow0\) and \(1-\max\det B\sim (1-r^2)^4/3\) as \(r\uparrow1\).

## Assumptions and scope
The result concerns exactly three *normalized* Bergman point-evaluation kernels at a *common fixed Euclidean radius* in the open disk. The Bergman area convention is \(dA/\pi\). The determinant is real and nonnegative because \(B\) is a Gram matrix; sites may coincide, in which case it vanishes. Strict gap Schur concavity is asserted on the open simplex of distinct sites, not at coincident angles or for points with unequal radii.

For \(\alpha\in(0,2\pi)\), put
\[
u(\alpha)=\frac{2t(1-\cos\alpha)}{(1-t)^2+2t(1-\cos\alpha)}=\frac{4t\sin^2(\alpha/2)}{(1-t)^2+4t\sin^2(\alpha/2)}.
\]
This is the squared pseudohyperbolic distance of two sites separated by \(\alpha\). Write \(u=u(\alpha),\ v=u(\beta),\ w=u(\gamma)\), and \(P=6-2(u+v+w)+uvw\).

## Proof
**1. Exact determinant identity.** Let \(S\) be the normalized Hardy/Szegő Gram matrix for the same sites, so \(S_{jk}=(1-t)/(1-z_j\overline {z_k})\) and \(B_{jk}=S_{jk}^{\,2}\) (ordinary entrywise complex square). The Cauchy determinant identity for a normalized Szegő Gram matrix of three distinct disk sites gives
\[
\det S=\prod_{1\le i<j\le3}\left|\frac{z_i-z_j}{1-z_i\overline {z_j}}\right|^2=uvw.
\]
Let \(q=S_{12}S_{23}S_{31}\) and \(a=|S_{12}|^2=1-u\), \(b=|S_{23}|^2=1-v\), \(c=|S_{31}|^2=1-w\). Expansion of a Hermitian three-by-three determinant gives
\[
2\operatorname{Re}q=\det S-1+a+b+c=uvw+2-u-v-w,
\quad |q|^2=abc.
\]
Consequently
\[
\begin{aligned}
\det B&=1-(a^2+b^2+c^2)+2\operatorname{Re}(q^2)\\
&=1-(a^2+b^2+c^2)+(2\operatorname{Re}q)^2-2abc\\
&=uvw\bigl(6-2(u+v+w)+uvw\bigr)=uvwP. \tag{1}
\end{aligned}
\]
The last equality is a polynomial identity, independently checked with exact arithmetic. Since \(0<u,v,w<1\), \(P>0\) (indeed \(P\ge 6-6+0=0\), with strictness inside the cube); thus \(\log\det B\) is well defined for distinct sites.

**2. Coordinatewise derivatives.** Differentiate (1) with respect to \(u\):
\[
\frac{\partial\log(uvwP)}{\partial u}
=\frac1u C_u,\qquad C_u=\frac{P-2u+uvw}{P}.
\]
There is a positive decomposition
\[
P-2u+uvw=2\bigl[(1-u)(2-vw)+(1-v)(1-w)\bigr]>0.
\]
Cyclic permutation gives \(C_v,C_w>0\), and direct subtraction shows
\[
C_u-C_v=-\frac{2(u-v)}{P}.\tag{2}
\]
For \(0<\phi<\pi\), \(u(\phi)\) is strictly increasing and
\[
\frac{u'(\phi)}{u(\phi)}=
\frac{(1-t)^2\cot(\phi/2)}{(1-t)^2+2t(1-\cos\phi)}>0
\]
is strictly decreasing, because its numerator strictly decreases and its denominator strictly increases. For \(\pi\le\phi<2\pi\), \(u'(\phi)\le0\).

**3. Strict Schur concavity.** Fix two distinct gaps \(\alpha>\beta\) with \(\alpha+\beta<2\pi\). The gap derivatives are
\[
D_\alpha=\partial_\alpha\log\det B=(u'(\alpha)/u(\alpha))C_u,
\qquad D_\beta=(u'(\beta)/u(\beta))C_v.
\]
If \(\alpha<\pi\), then also \(\beta<\pi\). Thus \(u>v\), which by (2) implies \(0<C_u<C_v\); the positive logarithmic derivatives satisfy \(u'(\alpha)/u(\alpha)<u'(\beta)/u(\beta)\). Hence \(D_\alpha<D_\beta\). If \(\alpha\ge\pi\), then automatically \(\beta<\pi\); therefore \(D_\alpha\le0<D_\beta\). The symmetric argument covers every pair of gaps. We have proved
\[
(\alpha-\beta)(D_\alpha-D_\beta)<0\qquad (\alpha\ne\beta).
\]
The strict Schur--Ostrowski differential criterion proves strict Schur concavity on the positive fixed-sum simplex. One may alternatively integrate the strict derivative inequality directly along each two-coordinate averaging path. Every positive triple with sum \(2\pi\) majorizes the equilateral triple; repeated averaging therefore strictly raises the determinant unless all gaps already agree. If any sites coincide, \(\det B=0\), whereas the equilateral determinant is positive, completing global uniqueness.

**4. Evaluation and asymptotics.** At \(\alpha=\beta=\gamma=2\pi/3\), \(u=v=w=3t/(1+t+t^2)\). Substitution into (1) yields
\[
\det B=\frac{81t^3(t^3+2)(2t^3+1)}{(1+t+t^2)^6}.
\]
Expansion at \(t=0\) gives \(162t^3+O(t^4)\). Factorizing its deficit at \(t=1\) or taking four derivatives yields \(1-\max\det B=(1-t)^4/3+o((1-t)^4)\). This finishes the proof.

## Verification
The standalone Python 3 standard-library script `checks/check_gram.py` tests the algebraic determinant formula using exact rational arithmetic, rechecks the positivity decomposition, verifies the sharp equilateral expression on rational parameter grids, and compares complex three-by-three Gram determinants with the pseudohyperbolic formula for deterministic non-equilateral triples. Executing `python3 checks/check_gram.py` prints `CHECK_OK` if all tests pass. These finite checks corroborate identities and examples but do not replace the differential argument for all radii and angles.

## Relationship to prior work
Tian's finite-point Schwarz--Pick inequality [1] compares Bergman Gram matrices under holomorphic disk maps by Loewner order; its constants depend on the number of points and map degree. It does not assert an optimal fixed-radius determinant node configuration or strict gap Schur concavity. The general kernel-Fekete framework of Karvonen, Särkkä, and Tanaka [2] motivates maximizing Gram determinants but develops approximate designs for truncated real Gaussian kernels, not exact three-point Bergman geometry. Related exact Szegő-kernel orbit determinant results [3] optimize a different kernel, corresponding to exponent one; neither their determinant identities nor their optimality statement by themselves imply Schur concavity for the entrywise-squared exponent-two Bergman matrix. The present calculation uses the Szegő Cauchy determinant as an input and then handles the new polynomial coupling explicitly.

## Limitations
The argument makes no assertion for four or more points, unequal radial coordinates, other kernel powers, unnormalized arbitrary-diagonal Gram determinants, or unrestricted two-dimensional Fekete sites. Strict Schur concavity is in the three cyclic angular gaps, not in every parameterization of node positions. The computation provides mathematical evidence of an explicit theorem but not an independent priority audit. A pre-existing equivalent in classical reproducing-kernel/Fekete literature remains possible despite targeted searches.

## References
[1] James Tian, *A finite-Point Schwarz-Pick Inequality*, arXiv:2608.10443v1 (first public version 2026-08-11). https://arxiv.org/abs/2608.10443

[2] T. Karvonen, S. Särkkä, and K. Tanaka, *Kernel-based interpolation at approximate Fekete points*, arXiv:1912.07316 (first public 2019). https://arxiv.org/abs/1912.07316

[3] *Sharp determinant stability and conditioning of concentric Szegő orbit frames*, mathematical research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-determinant-stability-and-conditioning-of-concentric-szeg--44f30fce73fa
