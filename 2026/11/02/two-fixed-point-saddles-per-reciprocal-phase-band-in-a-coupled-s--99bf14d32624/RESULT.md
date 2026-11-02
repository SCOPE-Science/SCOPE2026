# Two fixed-point saddles per reciprocal phase band in a coupled sine-square map

## Finding

For every fixed \(a,b>0\), the Zhu–Deng–Zhang–Zhu map
\[
 F_{a,b}(x,y)=\bigl(\sin^2(a\pi/x+b y),\;\sin^2(b\pi y+a x)\bigr),\qquad x>0,
\]
has a complete, explicitly asymptotic local fixed-point spectrum near the excluded corner \((0,0)\). The second fixed-point equation has a unique analytic small-state solution \(y=Y(x)\), and for every sufficiently large positive integer \(n\), **exactly two** fixed points on that branch lie in the reciprocal phase band
\[
 (n-\tfrac12)\pi<a\pi/x+bY(x)<(n+\tfrac12)\pi.
\]
Writing the two points as \((x_{n,\sigma},y_{n,\sigma})\), with \(\sigma\in\{-1,+1\}\), their exact defining equations are
\[
 y_{n,\sigma}=Y(x_{n,\sigma}),\qquad
 a\pi/x_{n,\sigma}+bY(x_{n,\sigma})
 =n\pi+\sigma\arcsin\sqrt{x_{n,\sigma}}.
\]
Their asymptotics as \(n\to\infty\), with fixed \(a,b\), are
\[
 \boxed{\displaystyle
 x_{n,\sigma}=\frac{a}{n}-\sigma\frac{a^{3/2}}{\pi n^{5/2}}+O_{a,b}(n^{-7/2}),
 \qquad y_{n,\sigma}=\frac{a^4}{n^2}+O_{a,b}(n^{-3}).}
\]
In particular, the two branch positions split by
\[
 x_{n,-1}-x_{n,+1}=\frac{2a^{3/2}}{\pi n^{5/2}}+O_{a,b}(n^{-7/2}).
\]
Each point is a hyperbolic saddle. Its real multipliers can be labeled so that
\[
 \boxed{\displaystyle
 \lambda_{u,n,\sigma}=-\sigma\frac{2\pi}{\sqrt a}n^{3/2}
       +O_{a,b}(n^{1/2}),\qquad
 \lambda_{s,n,\sigma}=\frac{2a^2b\pi}{n}+O_{a,b}(n^{-2}).}
\]
Consequently, the two saddles in each band have opposite Jacobian orientation for all sufficiently large \(n\). For sufficiently small fixed \(\delta,\eta>0\), every fixed point in \(0<x<\delta\), \(0\le y<\eta\) is among these two-per-band points, apart from a finite initial number of bands. The number with \(\varepsilon\le x<\delta\), \(0\le y<\eta\), obeys
\[
 \boxed{\displaystyle N(\varepsilon)=\frac{2a}{\varepsilon}+O_{a,b,\delta,\eta}(1)}
 \quad\text{as }\varepsilon\downarrow0.
\]

## Assumptions and scope

The parameters \(a,b\) are **arbitrary but fixed positive real numbers**, and the map is evaluated only where \(x>0\). The output is in \([0,1]^2\), but no global extension of the map at \(x=0\) is assumed. All asymptotic constants and the threshold beyond which the classification holds may depend on \(a,b\). The local rectangle is chosen small enough that the implicit branch \(y=Y(x)\) exhausts its second fixed-point equation; the statement does not enumerate fixed points with \(y\) bounded away from zero. Here a hyperbolic saddle means one real multiplier of modulus greater than one and the other of modulus less than one; it need not be area-preserving.

## Proof

**1. The unique small branch.** Put
\[
 G(x,y)=y-\sin^2(b\pi y+a x).
\]
At \((0,0)\), \(G=0\) and \(G_y=1\). By the real-analytic implicit-function theorem there exist \(\delta_0,\eta>0\) and a unique real-analytic \(Y\) with \(G(x,Y(x))=0\), \(Y(0)=0\), such that every solution of \(G(x,y)=0\) with \(|x|<\delta_0\), \(|y|<\eta\) lies on this graph. Differentiating at the origin, or comparing Taylor coefficients, gives
\[
 Y(x)=a^2x^2+2a^3b\pi x^3+O_{a,b}(x^4),\qquad Y'(x)=O_{a,b}(x).
\]
For positive sufficiently small \(x\), this branch has \(Y(x)>0\) and \(0< b\pi Y(x)+a x<\pi/4\).

**2. Exactly two fixed points in each sufficiently high band.** Let
\[
 \theta(x)=a\pi/x+bY(x),\qquad
 \alpha(x)=\arcsin\sqrt{x},\quad 0<x<\min(\delta_0,1/2).
\]
Then \(\theta(x)\to+\infty\),
\[
 \theta'(x)=-a\pi/x^2+bY'(x),\qquad
 \alpha'(x)=\frac1{2\sqrt{x(1-x)}}.
\]
Shrinking \(\delta_0\), ensure \(\theta'(x)<-\alpha'(x)<0\) on \((0,\delta_0)\). Thus \(\theta\) traverses each sufficiently high phase band exactly once as \(x\) decreases. Within a band \((n-\frac12)\pi<\theta<(n+\frac12)\pi\), the equation \(\sin^2\theta=x\) is equivalent to precisely one of
\[
 H_{n,\sigma}(x):=\theta(x)-n\pi-\sigma\alpha(x)=0,
 \qquad \sigma\in\{-1,+1\}.
\]
Both derivatives \(H'_{n,\sigma}=\theta'-\sigma\alpha'\) are negative. In the positive half-band, \(H_{n,+1}\) changes sign between the central zero of \(\sin^2\theta\) and the neighboring maximum; in the negative half-band the same holds for \(H_{n,-1}\). Hence there is exactly one root on each side, with no additional roots. The label \(\sigma=+1\) has the smaller \(x\)-coordinate. The implicit-function uniqueness from step 1 shows these are **all** fixed points in the chosen local rectangle whose phases belong to such bands.

**3. Positions and counting law.** At either root,
\[
 x_{n,\sigma}=\frac{a}{n+[\sigma\alpha(x_{n,\sigma})-bY(x_{n,\sigma})]/\pi}.
\]
First \(x_{n,\sigma}=a/n+O_{a,b}(n^{-5/2})\). Substituting
\(\alpha(x)=\sqrt{x}+O(x^{3/2})\) and \(Y(x)=a^2x^2+O(x^3)\) into this identity yields
\[
 x_{n,\sigma}=a/n-\sigma a^{3/2}/(\pi n^{5/2})+O_{a,b}(n^{-7/2}).
\]
The corresponding expansion of \(Y\) yields \(y_{n,\sigma}=a^4/n^2+O_{a,b}(n^{-3})\). All but a bounded number of phase bands in the interval \(\varepsilon\le x<\delta\) contribute two roots; the number of these bands is
\(\theta(\varepsilon)/\pi+O_{a,b,\delta}(1)=a/\varepsilon+O_{a,b,\delta}(1)\).
This proves the local counting law, including the endpoint error bounded independently of \(\varepsilon\).

**4. Saddle spectrum and orientation.** Set \(\phi=b\pi y+a x\). The Jacobian is exactly
\[
 DF_{a,b}(x,y)=
 \begin{pmatrix}
 -a\pi x^{-2}\sin(2\theta)&b\sin(2\theta)\\
 a\sin(2\phi)&b\pi\sin(2\phi)
 \end{pmatrix}.
\]
At a fixed point on the small branch,
\[
 \sin(2\theta)=\sigma 2\sqrt{x(1-x)},\qquad
 \sin(2\phi)=2a x+O_{a,b}(x^2)>0.
\]
Therefore the diagonal terms are
\[
 A=-\sigma 2a\pi x^{-3/2}(1+O(x)),\qquad
 D=2ab\pi x+O_{a,b}(x^2),
\]
and the off-diagonal product \(BC=O_{a,b}(x^{3/2})\). Since \(|A|\to\infty\), the discriminant \((A-D)^2+4BC\) is positive and the two eigenvalues are
\[
 \lambda_u=A+O_{a,b}(x^3),\qquad
 \lambda_s=D+O_{a,b}(x^3).
\]
Substituting the position asymptotics proves the claimed spectral formulas. In particular, \(|\lambda_u|>1>\lambda_s>0\) eventually. Their product, equivalently the exact identity
\[
 \det DF=-ab(1+\pi^2/x^2)\sin(2\theta)\sin(2\phi),
\]
has sign \(-\sigma\); this proves the orientation contrast between paired saddles. No finite-precision trajectory experiment is used for any universal or asymptotic conclusion.

## Verification

The standalone `checks/verify_singular_fixed_points.py` requires Python with `sympy` and `mpmath`. Run `python checks/verify_singular_fixed_points.py`. It checks the exact Jacobian and determinant identities and the implicit branch's cubic Taylor jet symbolically, then independently solves the local small-state equation and the two fixed-point phase equations at high precision for nine reciprocal bands across three positive parameter pairs. It checks each fixed-point residual, both real multipliers, the orientation signs, the leading position law and the pair-splitting coefficient. The recorded run passed 186 assertions. These finitely many checks are not an exhaustive proof of the infinitely many fixed points; that is provided by the monotonicity argument above.

## Relationship to prior work

The map was introduced by Zhu, Deng, Zhang and Zhu (2023), who studied chaotic indicators and image-encryption applications; its exact model equation is their Equation (1). The present theorem instead addresses a local fixed-point census near the singular boundary \(x=0\), the two-sided position splitting, orientation signs and spectral scaling. Standard oscillatory-root techniques explain why reciprocal sine phases produce many roots; they do not by themselves determine the coupled small-state branch or the two-dimensional saddle multipliers. Liu, Ning and Zhu (2024) study a related but different trigonometric map, with its reciprocal singularity in the second coordinate and a cosine-square second equation; its fixed-point equations are not equivalent to this family. A comparison with earlier unindexed work could alter publication priority; this analysis does not certify novelty independently.

## Limitations

The result is **local** to the fixed points approaching \((0,0)\); it does not classify fixed points whose second coordinate stays away from zero, describe nonstationary orbits, invariant basins, statistical chaos or cryptographic security. The source paper's full publisher text was not available for complete page-by-page comparison; the verified equation, published abstract and accessible section descriptions were inspected, and the limitation remains an originality risk. Saddle eigenvalues characterize local linear dynamics only. All asymptotics hold for fixed positive \(a,b\), with no claimed uniformity as these parameters diverge or approach zero.

## References

1. S. Zhu, X. Deng, W. Zhang, C. Zhu, *Construction of a New 2D Hyperchaotic Map with Application in Efficient Pseudo-Random Number Generator Design and Color Image Encryption*, Mathematics **11** (2023), article 3171, published July 19, 2023. DOI: 10.3390/math11143171. Model: Equation (1).
2. M. Liu, C. Ning, C. Zhu, *A Secure Image Encryption Scheme Based on a New Hyperchaotic System and 2D Compressed Sensing*, Entropy **26** (2024), article 603, published July 16, 2024. DOI: 10.3390/e26070603. Different comparison map: Section 2.1.
