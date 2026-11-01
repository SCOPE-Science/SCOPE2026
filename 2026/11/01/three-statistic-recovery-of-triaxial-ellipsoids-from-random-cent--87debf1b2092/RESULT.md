# Three-statistic recovery of triaxial ellipsoids from random central-section diameters

## Finding

The probability law of the half-diameter of a Haar-random central plane section determines the three semiaxes of any strictly triaxial Euclidean ellipsoid in dimension three, up to rigid rotation. More strongly, **just its two support endpoints and its upper-end square-root tail coefficient determine the semiaxes uniquely**. A one-dimensional integral gives the exact law and a complete-elliptic-integral formula gives the sharp tail coefficient. This is an inverse-identification result; the general joint eigenvalue distribution of random compressions is classical and is not claimed as new.

Let \(a>b>c>0\), \(\alpha=a^{-2}\), \(\beta=b^{-2}\), \(\gamma=c^{-2}\). Define
\[
E_{a,b,c}=\left\{x\in\mathbb R^3:\frac{x_1^2}{a^2}+\frac{x_2^2}{b^2}+\frac{x_3^2}{c^2}\le 1\right\}.
\]
For a Haar-uniform unit vector \(N\in S^2\), let \(R=\max\{\|x\|_2:x\in E_{a,b,c}\cap N^\perp\}\). Its support is exactly \([b,a]\); there are no endpoint atoms.

For any \(b<r<a\), write \(t=r^{-2}\), \(A=t-\alpha\), \(B=\beta-t\), \(C=\gamma-t\), and
\[
q_r(\varphi)=A\left(\frac{\cos^2\varphi}{B}+\frac{\sin^2\varphi}{C}\right).
\]
Then the exact distribution function is
\[
\Pr(R\le r)=1-\frac2\pi\int_0^{\pi/2}\sqrt{\frac{q_r(\varphi)}{1+q_r(\varphi)}}\,d\varphi.
\]
The distribution is continuous and strictly increasing for \(b<r<a\), and is zero below \(b\) and one above \(a\).

Define the **observed upper-end coefficient**
\[
T=\lim_{r\uparrow a}\frac{\Pr(R>r)}{\sqrt{a-r}}.
\]
Let the complete elliptic integral with parameter convention be
\[
\mathcal E(m)=\int_0^{\pi/2}\sqrt{1-m\sin^2u}\,du\quad(0\le m\le1).
\]
The limit exists and equals
\[
T=\frac2\pi\sqrt{\frac{2}{a^3(\beta-\alpha)}}\,\mathcal E\!\left(1-\frac{\beta-\alpha}{\gamma-\alpha}\right).
\]
The inverse reconstruction is explicit up to the inverse of a strictly monotone scalar function. Read \(a\) and \(b\) from the right and left endpoints of the support. Set
\[
K=\frac2\pi\sqrt{\frac{2}{a^3(\beta-\alpha)}}.
\]
There is a unique \(m\in(0,1)\) with \(\mathcal E(m)=T/K\), and then
\[
\boxed{\ c=\left(\alpha+\frac{\beta-\alpha}{1-m}\right)^{-1/2}.\ }
\]
In particular, three scalar distributional statistics (left endpoint, right endpoint, and sharp upper-tail coefficient) uniquely identify the unordered axis triple. Alternatively, once \(a,b\) are fixed, **any one interior CDF value** \(\Pr(R\le r_0)\) with \(b<r_0<a\) strictly decreases with \(c\) and therefore identifies \(c\).

## Assumptions and scope

All three semiaxes are strictly positive and pairwise distinct, ordered \(a>b>c\). The section plane passes through the ellipsoid center, and its unoriented normal is Haar-uniform. Euclidean radius means the maximum Euclidean norm in the section, equivalently half the section's Euclidean diameter because the body is centrally symmetric. Observing full section diameter instead of \(R\) simply multiplies the observed variable by two. No random displacement of the cutting plane is allowed. The endpoint limits are one-sided. The elliptic integral uses its **parameter** \(m\), not its modulus.

## Proof

**1. Compression and support endpoints.** Write \(D=\operatorname{diag}(\alpha,\beta,\gamma)\). For any plane \(H\),
\[
R(H)^{-2}=\min\{x^{\mathsf T}Dx:x\in H,\ \|x\|_2=1\}.
\]
By the two-dimensional Courant–Fischer min-max principle, \(\alpha\le R(H)^{-2}\le\beta\), hence \(b\le R(H)\le a\). Planes containing the first coordinate axis realize \(a\); the plane orthogonal to it realizes \(b\). Every neighborhood of these normals has positive Haar measure and the continuous section-radius map takes values nearby, so the support is exactly \([b,a]\).

**2. Exact cone criterion.** Fix \(b<r<a\). The condition \(R(N^\perp)\le r\) is equivalent to the quadratic form \(D-tI=\operatorname{diag}(-A,B,C)\) being nonnegative on \(N^\perp\). If \(N_1\ne0\), substitute \(x_1=-(N_2x_2+N_3x_3)/N_1\). Weighted Cauchy–Schwarz shows that nonnegativity for every pair \((x_2,x_3)\) holds **if and only if**
\[
N_1^2\ge A\left(\frac{N_2^2}{B}+\frac{N_3^2}{C}\right).
\]
The exceptional event \(N_1=0\) has Haar probability zero; there the form fails to be nonnegative since the first coordinate axis belongs to the plane. Parametrize \(N=(u,\sqrt{1-u^2}\cos\varphi,\sqrt{1-u^2}\sin\varphi)\). For Haar-uniform \(N\in S^2\), \(u\) is uniform on \([-1,1]\), independently of the uniform azimuth \(\varphi\in[0,2\pi)\). The cone criterion becomes \(|u|\ge\sqrt{q_r(\varphi)/(1+q_r(\varphi))}\). Integrating the conditional probability and using quadrant symmetry proves the displayed CDF formula.

As \(r\uparrow a\), both \(A\to0\) and \(q_r\to0\) uniformly, so the CDF tends to one. As \(r\downarrow b\), the first summand in \(q_r\) diverges for almost every azimuth, so dominated convergence gives CDF tending to zero. The CDF is strictly increasing in the open support because, as \(r\) increases, \(A\) decreases while \(B,C\) increase, and the integrand is strictly increasing in \(q_r\). Hence it has no atoms anywhere.

**3. Sharp upper-end coefficient.** Define \(B_0=\beta-\alpha>0\), \(C_0=\gamma-\alpha>B_0\). As \(r\uparrow a\),
\[
A=r^{-2}-a^{-2}\sim\frac{2(a-r)}{a^3},\qquad
\frac{q_r(\varphi)}A\longrightarrow\frac{\cos^2\varphi}{B_0}+\frac{\sin^2\varphi}{C_0},
\]
uniformly in azimuth. Therefore dominated convergence, with a uniform strictly positive denominator near \(r=a\), gives
\[
T=\frac2\pi\sqrt{\frac2{a^3}}\int_0^{\pi/2}
\sqrt{\frac{\cos^2\varphi}{B_0}+\frac{\sin^2\varphi}{C_0}}\,d\varphi.
\]
Factor out \(B_0^{-1/2}\) and set \(m=1-B_0/C_0\in(0,1)\). The integral is \(B_0^{-1/2}\mathcal E(m)\), proving the sharp tail formula and its strictly positive finite coefficient.

**4. Inverse rigidity.** The endpoints determine \(a,b\), hence \(\alpha,\beta\) and \(K\). For \(m\in(0,1)\), \(\mathcal E\) is strictly decreasing because
\[
\mathcal E'(m)=-\frac12\int_0^{\pi/2}\frac{\sin^2u}{\sqrt{1-m\sin^2u}}\,du<0.
\]
Its endpoint values are \(\mathcal E(0)=\pi/2\) and \(\mathcal E(1)=1\). The observed ratio \(T/K\) consequently determines exactly one \(m\in(0,1)\). Solving the defining equation for \(m\) yields \(\gamma=\alpha+(\beta-\alpha)/(1-m)\), hence the asserted unique \(c\).

For the alternative one-point test, keeping \(a,b,r_0\) fixed, an increase in \(c\in(0,b)\) decreases \(\gamma\) and \(C\), so increases \(q_{r_0}(\varphi)\) for almost all \(\varphi\). The integral strictly increases and the CDF strictly decreases. Thus one interior scalar CDF value also determines \(c\).

## Verification

The standalone `verify.py` uses NumPy and SciPy. It independently constructs an orthonormal basis of each sampled plane, diagonalizes the restricted quadratic form, and compares its smallest eigenvalue with the derived cone criterion. The checked formula also agrees with direct Haar sampling, limiting prolate-spheroid formulas, the monotonicity prediction, and the upper-tail coefficient. Running `python verify.py` with dependencies in `requirements.txt` passed 60,449 deterministic/check assertions. A numerical test is not an all-parameters theorem: the preceding analysis proves the continuous distribution, exact coefficients and injectivity.

For the illustrative axis triple \((a,b,c)=(3,2,1)\), direct quadrature gives \(\Pr(R\le 2.5)\approx0.5501112037522726\) and \(T\approx0.53370587242544\).

## Relationship to prior work

The **Dixon–Anderson law** determines the *joint eigenvalue distribution* for a real Haar compression of a fixed symmetric matrix, so its dimension-three case already covers the existence and determination of the distribution of the two restricted eigenvalues; the present CDF formula is an auxiliary evaluated marginal and is **not** claimed independently new. The specific inverse statement is different: it proves that only the **single smallest restricted eigenvalue** (equivalently the largest section radius), or even its two support endpoints and a single sharp tail coefficient, determine every source semiaxis. This inverse implication and sharp geometric tail reconstruction are not stated in the inspected source.

Guedon–Litvak–Tatarko–Vritsiou (2026) and Hinrichs–Krieg–Novak–Prochno–Ullrich (2019/2021) analyze random section radii and bounds, primarily in broad or high-dimensional settings; the inspected relevant theorems do not establish this three-dimensional inverse characterization. Makarenko–Fletcher–Shukurov (2014) examine **randomly positioned** ellipsoid cuts and a **scale-invariant filamentarity statistic**, rather than centered radius laws. Prior work for axially symmetric one-spike ellipsoids covers a coincident-axes limiting case, not the strictly triaxial inverse statement.

## Limitations

The result is confined to centered ellipsoids with three distinct axes in Euclidean dimension three and Haar-uniform **central** planar cuts. It proves identifiability from the mathematical distribution, not a finite-sample statistical accuracy bound: upper-tail estimation may be difficult near rare events or degeneracy. The upper-tail coefficient need not distinguish any nonellipsoidal convex bodies. Historical priority with respect to older spectral and stereological literature remains provisional, and the mathematical proof has not undergone independent external review.

## References

1. O. Guedon, A. E. Litvak, K. Tatarko and B.-H. Vritsiou, *On random diameters of convex bodies*, first posted September 21, 2026, arXiv:2609.24131, https://arxiv.org/abs/2609.24131.
2. A. Hinrichs, D. Krieg, E. Novak, J. Prochno and M. Ullrich, *Random sections of ellipsoids and the power of random information*, arXiv:1901.06639, https://arxiv.org/abs/1901.06639.
3. T. Assiotis and J. Najnudel, *The boundary of the orbital beta process*, arXiv:1905.08684, especially Definition 1.1 and Proposition 1.2 (Dixon–Anderson kernel), https://arxiv.org/abs/1905.08684.
4. I. Makarenko, A. Fletcher and A. Shukurov, *3D morphology of a random field from its 2D cross-section*, arXiv:1407.4048, https://arxiv.org/abs/1407.4048.
