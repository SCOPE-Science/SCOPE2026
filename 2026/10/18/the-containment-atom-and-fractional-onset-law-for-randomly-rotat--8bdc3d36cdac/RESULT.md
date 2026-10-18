# The containment atom and fractional onset law for randomly rotated scaled ellipses

## Finding
Fix a filled ellipse \(E=\{(x,y):x^2/a^2+y^2/b^2\le1\}\) with \(a>b>0\). For a scale \(k\ge1\) and angle \(\theta\), set \(E_{k,\theta}=kR_\theta E\) and \(Y_\theta=\operatorname{area}(E\cap E_{k,\theta})\). The area profile, including every containment and transverse-intersection orientation, has the following exact elementary formula.

Define \(q=(a^2-b^2)/(ab)\), and, for \(0\le\theta\le\pi/2\), let
\[
\lambda(\theta)=\frac{q\sin\theta+\sqrt{4+q^2\sin^2\theta}}2.
\]
If \(\lambda(\theta)\le k\), then \(Y_\theta=\pi ab\). Otherwise set
\[
\phi=\arctan\sqrt{\frac{k^2-\lambda^{-2}}{\lambda^2-k^2}}.
\]
Then
\[
\boxed{Y_\theta=2ab\left[\phi+k^2\left(\frac\pi2-\arctan(\lambda^2\tan\phi)\right)\right].}
\]
For arbitrary real \(\theta\), use \(|\sin\theta|\) in the definition of \(\lambda\). Every branch and equality boundary is included.

A sharp *containment phase transition* occurs at \(k=a/b\). If \(k\ge a/b\), then \(Y_\theta=\pi ab\) for every direction. If \(1<k<a/b\), set
\[
\theta_c=\arcsin\left(\frac{ab}{a^2-b^2}\left(k-k^{-1}\right)\right)\in(0,\pi/2).
\]
The overlap equals the full smaller-ellipse area precisely for \(\theta\in[0,\theta_c]\cup[\pi-\theta_c,\pi]\), modulo \(\pi\), and is strictly decreasing on \((\theta_c,\pi/2)\). Thus under uniform relative orientation \(\Theta\in[0,\pi)\), the random overlap \(Y=Y_\Theta\) has **exactly one atom**, of mass
\[
\boxed{\Pr(Y=\pi ab)=\frac{2\theta_c}{\pi}},
\]
and a strictly continuous component on \([y_-,\pi ab)\), where \(y_-=Y_{\pi/2}\) is evaluated by the preceding elementary formula. For \(y_-\le y<\pi ab\), there is a unique \(\theta(y)\in[\theta_c,\pi/2]\) satisfying \(Y_{\theta(y)}=y\), and the complete CDF is
\[
\boxed{F_Y(y)=1-\frac{2\theta(y)}\pi.}
\]
It is zero for \(y<y_-\) and one for \(y\ge\pi ab\); the latter jump has size \(2\theta_c/\pi\). For \(k=1\), the atom disappears, and the formula reduces to the equal-area rotation case. For \(k\ge a/b\), the law is purely atomic at \(\pi ab\).

The continuous mass approaches the atom with a universal **two-thirds power**. For \(1<k<a/b\), put \(L=qk^2\cos\theta_c/(1+k^2)\) and
\[
K=\frac{4ab}{3\sqrt{1-k^{-4}}}\left(\frac{2L}{k}\right)^{3/2}>0.
\]
Then
\[
\pi ab-Y_{\theta_c+t}=Kt^{3/2}+o(t^{3/2})\quad(t\downarrow0),\qquad
\boxed{\Pr(\pi ab-\varepsilon<Y<\pi ab)\sim\frac2\pi\left(\frac\varepsilon K\right)^{2/3}}.
\]
The inequality excludes the atom at the upper endpoint. Thus the onset exponent differs from the linear endpoint behavior when \(k=1\).

## Assumptions and scope
All ellipses are centered at the origin, have fixed axes \(a>b>0\), and the second is the uniformly magnified, randomly rotated copy \(kR_\theta E\). The scale obeys \(k\ge1\). For the probability claims, unoriented relative rotation is Haar-uniform on \([0,\pi)\). We use ordinary Euclidean area, and the formula is for filled ellipses.

## Proof
Normalize by \(x=\operatorname{diag}(a,b)z\), which multiplies area by \(ab\) and makes the original ellipse the unit disk. The second ellipse has shape matrix \(C=k^2\operatorname{diag}(a,b)^{-1}R_\theta\operatorname{diag}(a^2,b^2)R_\theta^{\mathsf T}\operatorname{diag}(a,b)^{-1}\). It is positive definite, \(\det C=k^4\), and its eigenvalues are \(k^2\lambda^2\) and \(k^2\lambda^{-2}\), since the trace divided by \(k^2\) is \(2+q^2\sin^2\theta\), so \(\lambda-\lambda^{-1}=q|\sin\theta|\). A rotation of the normalized coordinates does not alter the intersection area.

The two radial squares in the normalized first quadrant are \(1\) and
\[
\rho^2(\varphi)=\frac{k^2}{\lambda^{-2}\cos^2\varphi+\lambda^2\sin^2\varphi}.
\]
If \(k\ge\lambda\), the latter is at least one in every direction; thus the disk is contained and the area is \(\pi ab\). For \(1\le k<\lambda\), the curves meet at the unique angle \(\phi\in(0,\pi/2)\) for which \(\rho(\phi)=1\). Rearrangement gives \(\tan^2\phi=(k^2-\lambda^{-2})/(\lambda^2-k^2)\). The disk is the smaller radial constraint up to \(\phi\), and the second ellipse is smaller afterward. Fourfold quadrant symmetry and the polar area element imply
\[
Y=2ab\left[\phi+k^2\int_\phi^{\pi/2}\frac{d\varphi}{\lambda^{-2}\cos^2\varphi+\lambda^2\sin^2\varphi}\right].
\]
Setting \(t=\tan\varphi\) evaluates the integral as \(\pi/2-\arctan(\lambda^2\tan\phi)\), proving the stated formula, including the boundary by continuity.

On \([0,\pi/2]\), the parameter \(\lambda\) increases strictly from \(1\) to \(a/b\). Hence containment occurs precisely where \(\lambda\le k\), giving the critical \(\theta_c\). In the crossing regime, increasing \(\lambda\) strictly decreases the area: in the interval \(\varphi\ge\phi\), the derivative of \(\lambda^{-2}\cos^2\varphi+\lambda^2\sin^2\varphi\) with respect to \(\log\lambda\) is strictly positive, since \(\tan\phi>\lambda^{-2}\) when \(\lambda>k\ge1\). At the moving boundary \(\rho^2(\phi)=1\), so the boundary terms in differentiating the polar integral cancel. This proves strict monotonicity of \(Y_\theta\) on \((\theta_c,\pi/2)\).

For uniform \(\Theta\in[0,\pi)\), symmetry gives two containment intervals of total length \(2\theta_c\). Outside them the continuous area decreases strictly between the middle angle and a boundary angle. Therefore, for any area \(y\) in the nonconstant branch, the event \(Y\le y\) is exactly \(\Theta\in[\theta(y),\pi-\theta(y)]\), proving the CDF and its single atom.

For the fractional law let \(t=\theta-\theta_c\downarrow0\). The matrix singular-value parameter is \(\lambda=k+Lt+O(t^2)\), with \(L\) as stated. Write \(z=\pi/2-\varphi\). In the vanishing angular region where the larger ellipse ceases to contain the disk, one has uniformly on its shrinking support
\[
1-\rho^2(\pi/2-z)=\frac{2Lt}{k}-(1-k^{-4})z^2+o(t+z^2).
\]
This positive deficit is supported to leading order on \(0\le z\le\sqrt{2Lt/[k(1-k^{-4})]}\). The exact area deficit equals twice \(ab\) times the integral of its positive part, and elementary integration of this parabolic cap gives
\[
\pi ab-Y_{\theta_c+t}=\frac{4ab}{3\sqrt{1-k^{-4}}}\left(\frac{2L}{k}\right)^{3/2}t^{3/2}+o(t^{3/2}).
\]
The set of orientations with deficit between zero and \(\varepsilon\) consists of two intervals adjacent to \(\theta_c\) and \(\pi-\theta_c\), with total length asymptotic to \(2(\varepsilon/K)^{2/3}\), proving the probability law. At \(k=1\) the quadratic-cap derivation is inapplicable (the two ellipses coincide at alignment), explaining the different linear onset.

## Verification
`CHECK.py` separately evaluates both original ellipse quadratic forms by midpoint integration of the smaller radial square. A grid of shapes, scales and angles corroborates all analytic branches, including the full-containment regime. For \(1<k<a/b\) it also verifies the transition value, strict numerical ordering away from the boundary, and eight near-critical tests of the predicted three-halves deficit coefficient. Its finite checks are not the universal proof, which is given above.

## Relationship to prior work
Hughes and Chraibi (2011) provide a general computational algorithm for two arbitrary ellipse overlap areas based on conic intersections and sector formulas. A 2019 public discussion of concentric ellipses gives a partial radial method and an exact special-case formula for pairs of equal-area quarter-rotated ellipses. The latter, under affine normalization, also accounts for the **equal-area** case \(k=1\); no originality is claimed for that equal-area overlap identity. The present result instead treats the unequal-area regime \(1<k<a/b\), and identifies its sharp containment threshold, mixed atomic–continuous random-area distribution, and noninteger grazing exponent, which are not stated in those inspected sources. Generic numerical computability is prior work.

## Limitations
The result covers uniformly scaled copies, not arbitrary pairs of unequal-area ellipses, and requires a common center. The CDF's continuous branch is specified exactly using the inverse of an explicit strictly monotone elementary function rather than an elementary inverse expression. Computational tests are finite corroboration. Historical priority may be affected by unindexed stereological work or inaccessible documentation. Independent mathematical validation has not been performed.

## References
Hughes, G. B. and Chraibi, M., *Calculating Ellipse Overlap Areas*, arXiv:1106.3787v1, first posted 19 June 2011, https://arxiv.org/abs/1106.3787.

*Intersection area of concentric ellipses*, Mathematics Stack Exchange question 3312747, discussion dated 3–4 August 2019, https://math.stackexchange.com/questions/3312747/intersection-area-of-concentric-ellipses (partial general approach and a quarter-turn equal-area formula).

Eberly, D., *Intersection of Ellipses*, Geometric Tools documentation, https://www.geometrictools.com/Documentation/IntersectionOfEllipses.pdf (only search-indexed contents accessible during comparison).
