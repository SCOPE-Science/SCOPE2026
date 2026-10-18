# Critical fifth-moment failure of local dual Brunn–Minkowski concavity near the disk

## Finding
For an origin-symmetric planar convex body \(K\) containing the origin, define the normalized radial-power functional
\[
\mathcal F_q(K)=\left(\frac{1}{2\pi}\int_0^{2\pi}\rho_K(\theta)^q\,d\theta\right)^{1/q},\qquad q>0.
\]
Here \(\rho_K(\theta)\) is the Euclidean radial function. For every fixed \(0<q<5\), there exists a \(C^2\) neighborhood of the Euclidean unit disk, among origin-symmetric positively curved \(C^2\) bodies, on which \(\mathcal F_q\) is concave along **every** Minkowski segment. The threshold is optimal, with its endpoint excluded: for **every** \(q\ge5\) and every such neighborhood, two smooth, strictly convex, origin-symmetric members violate midpoint concavity.

The critical \(q=5\) failure is invisible at the disk's quadratic Hessian. Put \(h_b(\phi)=1+b\cos(4\phi)\), \(f(\phi)=\cos(2\phi)\). For \(b<0\) of sufficiently small magnitude, \(h_b\) is a support function with strictly positive curvature radius and
\[
\left.\frac{d^2}{dt^2}\mathcal F_5(h_b+t f)\right|_{t=0}=-6b+O(b^2)>0.
\]
Thus the endpoint failure comes from coupling the second and fourth even Fourier harmonics, rather than from a positive quadratic variation at the circle.

## Assumptions and scope
Support functions are written \(h(\phi)\), with outer-unit-normal angle \(\phi\), and are \(2\pi\)-periodic, \(C^2\), positive, satisfy \(h+h''>0\), and are origin-symmetric \(h(\phi+\pi)=h(\phi)\). The \(C^2\)-distance is that of support functions on the unit normal circle; the disk has \(h\equiv1\). Addition and nonnegative scalar multiplication of supports coincide with Minkowski addition and dilation of their bodies. Concavity means
\[
\mathcal F_q((1-t)K+tL)\ge(1-t)\mathcal F_q(K)+t\mathcal F_q(L)
\]
for every pair within a specified neighborhood and each \(0\le t\le1\). No inequality outside that local neighborhood is claimed for \(4<q<5\). The boundary \(q=5\) is excluded even locally.

## Proof
**1. Exact support-function integral.** Let \(Q=h+h''>0\), \(R=(h^2+(h')^2)^{1/2}\). The boundary point with outer normal \(n(\phi)\) is \(x=h n+h'\tau\), hence its radial distance is \(R\). If \(\theta\) is its radial angle, then
\[
\frac{d\theta}{d\phi}=\frac{hQ}{R^2}>0.
\]
Consequently, with \(J_q(h)=\int_0^{2\pi}\rho_h(\theta)^q\,d\theta\),
\[
J_q(h)=\int_0^{2\pi}hQ R^{q-2}\,d\phi,\qquad \mathcal F_q(h)=\bigl(J_q(h)/(2\pi)\bigr)^{1/q}.
\]
For periodic \(C^2\) variations \(f\), differentiation and integration by parts give
\[
J'_q(h)[f]=q\int_0^{2\pi} f R^{q-2}Q\,d\phi
\]
and the exact Hessian
\[
J''_q(h)[f,f]=q\int_0^{2\pi}\left\{R^{q-2}\bigl(f^2-(f')^2\bigr)+(q-2)R^{q-4}hQ f^2\right\}\,d\phi.
\]
To check the cancellation, differentiate the first-variation expression. Its cross term \((q-2)R^{q-4}h'Qff'\) cancels the corresponding term in \(\int R^{q-2}ff''\) after integration by parts, because \(R' =h'Q/R\). Differentiating the positive power then gives
\[
\frac{\mathcal F_q''(h)[f,f]}{\mathcal F_q(h)}=\frac{J_q''(h)[f,f]}{qJ_q(h)}-\frac{q-1}{q^2}\left(\frac{J_q'(h)[f]}{J_q(h)}\right)^2.
\]
The bilinear Hessian follows by polarization. These formulas are valid for every real \(q>0\) under the stated strict curvature hypotheses.

**2. Concavity in a neighborhood for \(0<q<5\).** Write the mean as \(\bar f=(2\pi)^{-1}\int f\). Substitution of \(h\equiv1\) yields
\[
\mathcal F_q''(1)[f,f]=(q-1)\overline{(f-\bar f)^2}-\overline{(f')^2}.
\]
By the Fourier expansion of every \(\pi\)-periodic \(f\), the first nonconstant allowed frequencies are \(\pm2\); therefore
\[
\overline{(f')^2}\ge4\overline{(f-\bar f)^2}.
\]
For each fixed \(q<5\), the disk Hessian is strictly negative on all nonconstant directions, with a uniform negative coercivity estimate on mean-zero directions in \(H^1\). Indeed, the Fourier coefficients have weights \(k^2-(q-1)\), and for even \(k\ne0\), their ratio to \(1+k^2\) has a strictly positive minimum.

The exact Hessian from part 1 depends continuously on \(h\) in the \(C^2\) norm as a bilinear form on \(H^1\): the weights \(R^{q-2}\), \(R^{q-4}hQ\), and the coefficients of the squared first variation are uniformly bounded and converge uniformly as \(h\to1\). Hence for all \(h\) sufficiently close to \(1\), the Hessian is still strictly negative on mean-zero directions. Because \(\mathcal F_q\) is positively homogeneous of degree one, differentiating \(\mathcal F_q(sh)=s\mathcal F_q(h)\) gives \(\mathcal F_q''(h)[h,f]=0\) for every \(f\). Decompose any \(f\) as \(f=c h+g\) where \(\bar g=0\); its Hessian equals the Hessian on \(g\), and is nonpositive. Along a Minkowski segment of two sufficiently close supports, all intermediate supports remain close to \(1\) and strictly convex. Twice integration of the nonpositive second derivative proves concavity for the entire segment.

**3. Beyond the critical order.** For \(h=1\), \(f=\cos2\phi\), the disk formula gives
\[
\mathcal F_q''(1)[f,f]=(q-5)/2.
\]
For every \(q>5\), this is positive. For small \(t>0\), the supports \(1\pm tf\) remain positive and have positive curvature radii \(1\mp3t\cos2\phi\). Their midpoint is the disk, and the positive Hessian forces a strict reverse midpoint inequality.

**4. The critical endpoint \(q=5\).** Fix \(f=\cos2\phi\) and \(h_b=1+b\cos4\phi\). For \(|b|<1/15\), \(h_b+h_b''=1-15b\cos4\phi>0\). Quarter-turn symmetry of \(h_b\) and sign reversal of \(f\) give \(J_5'(h_b)[f]=0\) identically. Write \(c=\cos4\phi\). Uniformly as \(b\to0\),
\[
R=1+bc+O(b^2),\quad Q=1-15bc,\quad h_bQ=1-14bc+O(b^2),
\]
so the exact Hessian formula becomes
\[
\frac{J_5''(h_b)[f,f]}5=\int_0^{2\pi}\left[4f^2-(f')^2+bc\{-36f^2-3(f')^2\}\right]d\phi+O(b^2).
\]
The constant-term integral vanishes. Fourier orthogonality gives
\[
\overline{cf^2}=\tfrac14,\qquad \overline{c(f')^2}=-1,
\]
so \(J_5''(h_b)[f,f]/(2\pi\cdot5)=-6b+O(b^2)\). Since \(J_5(h_b)/(2\pi)=1+O(b^2)\) (its linear term integrates to zero),
\[
\mathcal F_5''(h_b)[f,f]=-6b+O(b^2).
\]
For negative \(b\) sufficiently near zero this is positive. The supports \(h_b\pm t f\) are positive, strictly convex, and arbitrarily \(C^2\)-close to \(1\) by choosing \(b,t\) sufficiently small. Their midpoint is \(h_b\). Taylor's theorem shows their mean functional strictly exceeds the midpoint functional, proving failure of concavity in every neighborhood at \(q=5\).

## Verification
The standalone `CHECKER.py` reconstructs the exact Fourier constant terms \(\overline{f^2}=1/2\), \(\overline{(f')^2}=2\), \(\overline{cf^2}=1/4\), \(\overline{c(f')^2}=-1\), thus independently certifying the leading endpoint coefficient \(-6\). It evaluates the untruncated integral Hessian at a range of positive and negative \(b\) values using uniformly spaced trapezoidal quadrature, finding the correct signs and slopes. It also tests the disk spectral coefficients at sample \(q\). The infinite-dimensional local concavity and arbitrarily small counterexamples follow from the analytical Fourier coercivity and asymptotic proof, not from finite tests.

## Relationship to prior work
The 2026 work of Li, Wan, and Zhang (arXiv:2608.03949) proves global origin-symmetric dual Brunn–Minkowski concavity at \(q=4\) in the plane, constructs global failures for \(q>4\), and records the **previously known** ball-point spectral stability bound \(q\le5\), attributed there to Xu and Yang. Tao (arXiv:2610.09636) determines the planar global \(L_p\) ranges, in particular the \(p=1\) global range \(q\le4\). Those results differ logically from a uniform neighborhood statement for \(4<q<5\), and a failure within **every** neighborhood at \(q=5\) despite neutral ball Hessian. The disk Fourier spectral formula alone does not imply the resonant endpoint failure. The earlier 2026 Xu–Yang article treats local behavior at the ball and is relevant to priority; its complete text was not accessible for full comparison, so earlier coverage of the neighborhood aspect cannot be excluded decisively.

## Limitations
The result concerns only dimension two, origin-symmetric \(C^2\) bodies of positive curvature, ordinary Minkowski addition, and one fixed \(q>0\) at a time. It supplies no explicit optimal neighborhood radius or global positive result for \(4<q<5\); indeed the known global bound ends at \(q=4\). The complete earlier Xu–Yang source and Tao preprint were unavailable for full-text comparison, leaving a historical-priority risk despite statement-level and accessible full-text checks. No independent mathematical audit has been conducted.

## References
1. H. Li, Y. Wan, Y. Zhang, *On the Brunn–Minkowski inequality for \(q\)-th dual quermassintegrals with \(q>n\)*, arXiv:2608.03949 (first publicly available August 4, 2026), especially §§1, 3–5 and Remark 3.1.
2. J. Tao, *On the \(L_p\) Brunn–Minkowski inequality for planar dual quermassintegrals*, arXiv:2610.09636 (October 7, 2026); abstract and publication metadata.
3. H. Xu, K. Yang, *A note on the Brunn–Minkowski inequality for dual quermassintegrals*, Proceedings of the American Mathematical Society 154 (2026), 3133–3141, doi:10.1090/proc/17647; accessed metadata and indirect mathematical attribution only.
4. S. Sadovsky, G. Zhang, *Brunn–Minkowski and reverse isoperimetric inequalities for dual quermassintegrals*, arXiv:2505.23748 (May 29, 2025), introductory inequality and motivating question.
