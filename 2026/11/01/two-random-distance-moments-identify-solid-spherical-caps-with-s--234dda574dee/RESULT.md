# Two random-distance moments identify solid spherical caps with sharp cubic stability

## Finding
For a three-dimensional **solid** Euclidean spherical cap, two even moments of the distance between two independent volume-uniform points determine the radius of its parent sphere and its height. Precisely, let \(R>0\), \(0<t\le2\), and
\[
K_{R,t}=\{(x,y,z)\in\mathbb R^3:x^2+y^2+z^2\le R^2,\ z\ge R(1-t)\}.
\]
The cap height is \(H=Rt\); \(t=2\) is the full ball (included as the endpoint of this family). Let \(M_1=\mathbb E\|X-Y\|^2\) and \(M_2=\mathbb E\|X-Y\|^4\) for independent uniform-volume points \(X,Y\in K_{R,t}\). Define \(u=2-t\) and
\[
A(u)=7u^3+14u^2+20u+8,\qquad
B(u)=41u^4+82u^3+99u^2+108u+36.
\]
Then the **exact forward moments** are
\[
M_1=R^2\frac{3(2-u)A(u)}{40(1+u)^2},\qquad
M_2=R^4\frac{(2-u)^2B(u)}{70(1+u)^2}.
\]
The scale-free observation \(Q=M_2/M_1^2\) obeys
\[
\boxed{Q=\frac{160(1+u)^2B(u)}{63A(u)^2}.}
\]
It is a strictly increasing bijection from \(u\in[0,2)\) onto \(Q\in[10/7,7/4)\). Thus \(Q\) uniquely gives \(u\), and then the positive value \(M_1\) uniquely determines \(R\) and \(H=R(2-u)\). Every \(M_1>0\) with \(Q\in[10/7,7/4)\) is realized by exactly one such cap. The first moment alone never identifies both parameters.

A **sharp inverse stability boundary** occurs at the full ball. On each shape range \(t\in[\varepsilon,2]\), \(\varepsilon>0\), the inverse \(Q\mapsto u\) satisfies a uniform Hölder bound of exponent \(1/3\). This exponent cannot be improved: as \(u\downarrow0\),
\[
Q-\frac{10}{7}=\frac{25}{63}u^3+O(u^4).
\]
On compact subintervals excluding \(t=2\), the inverse is locally Lipschitz. In particular, the full sphere is distinguishable from a proper cap by the exact moment ratio, but near-sphere inference is cubically ill-conditioned.

## Assumptions and scope
Distance is Euclidean ambient distance, not intrinsic boundary distance or spherical angular distance. Both points are sampled independently from normalized three-dimensional Lebesgue measure on the **volume** of the cap. The radius \(R\) and height \(H\) are initially unknown. The assertion covers all \(0<H\le2R\), including caps larger than hemispheres, with the full ball as an endpoint. Moments are population expectations without measurement noise. Rotation and translation are irrelevant to identification up to congruence.

## Proof
Scale to \(R=1\) and write \(z\) for the coordinate along the cap axis. Its normalized density is \((1-z^2)/v_t\) for \(1-t\le z\le1\), where
\[
v_t=\int_{1-t}^1(1-z^2)\,dz=\frac{t^2(3-t)}3.
\]
Given \(z\), the two remaining coordinates are uniform in the disk of radius \(\sqrt{1-z^2}\). Therefore their conditional squared radial mean is \((1-z^2)/2\) and conditional fourth radial mean is \((1-z^2)^2/3\). Define \(Z_j=v_t^{-1}\int_{1-t}^1 z^j(1-z^2)\,dz\). Axial symmetry gives the first vector moment \(\mu=(0,0,Z_1)\), the second raw-moment matrix \(T=\operatorname{diag}((1-Z_2)/4,(1-Z_2)/4,Z_2)\), and
\[
\mathbb E\|X\|^2=\frac{1+Z_2}2,\quad
\mathbb E\|X\|^4=\frac{1+Z_2+Z_4}3,\quad
\mathbb E(\|X\|^2 X)=\left(0,0,\frac{Z_1+Z_3}{2}\right).
\]
Independence, expansion of \(\|X-Y\|^2\), and expansion of its square yield
\[
\begin{aligned}
\mathbb E\|X-Y\|^2&=2\bigl(\mathbb E\|X\|^2-\|\mu\|^2\bigr),\\
\mathbb E\|X-Y\|^4&=2\mathbb E\|X\|^4+2(\mathbb E\|X\|^2)^2+4\operatorname{tr}(T^2)
-8\mu\cdot\mathbb E(\|X\|^2X).
\end{aligned}
\]
Each \(Z_j\) is an integral of a polynomial. Direct integration and simplification give, with \(u=2-t\),
\[
\mathbb E\|X-Y\|^2=\frac{3(2-u)A(u)}{40(1+u)^2},\qquad
\mathbb E\|X-Y\|^4=\frac{(2-u)^2B(u)}{70(1+u)^2}.
\]
Rescaling distances by \(R\) proves the forward formulas. Set \(C(u)=66u^3+117u^2+56u+12\). Exact differentiation gives
\[
\boxed{\frac{dQ}{du}=\frac{3200(1+u)u^2C(u)}{63A(u)^3}.}
\]
Every coefficient of \(A\) and \(C\) is positive; hence the derivative is strictly positive for \(0<u<2\). Direct substitution gives \(Q(0)=10/7\) and the continuous limiting value \(Q(2^-)=7/4\), proving the exact range and injectivity. Recover \(R\) from \(R^2=M_1\,40(1+u)^2/[3(2-u)A(u)]\). Conversely this positive \(R\) realizes any admissible pair, establishing surjectivity. Holding \(M_1\) fixed and varying \(u\) shows one moment cannot identify the cap.

For stability, \(Q'(u)/u^2\) extends continuously to a strictly positive function on every \([0,2-\varepsilon]\). If \(u_1<u_2\) in such an interval, then for some \(c_\varepsilon>0\),
\[
Q(u_2)-Q(u_1)\ge c_\varepsilon\int_{u_1}^{u_2}s^2\,ds\ge \frac{c_\varepsilon}{3}(u_2-u_1)^3.
\]
This is the asserted uniform \(1/3\)-Hölder inverse bound. Direct expansion at \(u=0\) gives \(Q(u)-10/7=25u^3/63+O(u^4)\), so no larger Hölder exponent can hold at the full ball. Away from that endpoint the derivative is positive, implying local Lipschitz inversion.

## Verification
The supplied `cap_verify.py` checks the raw axial integrals and moment identities with exact symbolic arithmetic; separately evaluates the raw axial integrals by numerical quadrature; verifies the factored monotonicity and cubic endpoint coefficient; and independently generates volume-uniform pairs for several cap shapes to compare empirical moments. Run `python cap_verify.py` after installing the packages in `requirements.txt`. The checker reports `ALL_CHECKS_PASSED` in the recorded execution. Symbolic identities and the preceding analytic proof, not finite simulation, justify universal claims.

## Relationship to prior work
Moseeva, Tarasov and Zaporozhets (2020) derive random-distance distributions on **spherical surfaces** with angular metric, including surface spherical caps; their measured object differs from volume-uniform Euclidean distances in a solid ball cap. Bonnet, Gusakova, Thäle and Zaporozhets (2020) prove sharp inequalities for the **first ordinary distance moment** over general convex bodies, but no two-even-moment cap inverse theorem or cubic endpoint exponent. Tu and Fischbach (2002) provide general random-distance formulas for balls with arbitrary density, offering a general forward-integral framework; it does not, in the inspected material, establish a sharp cap-shape inversion. General polynomial formulas for even distance moments, as described by García-Pelayo (2011), can facilitate forward calculations but do not by themselves imply strict monotonicity of this cap's normalized moment ratio or its sharp inverse exponent. An earlier sphere-cap inertia formula determines low-order coordinate moments but not the inverse theorem. These comparisons concern the mathematical statements, not a claim that a literature search proves novelty.

## Limitations
This is a geometric population-identifiability theorem, not a finite-sample estimator or a noisy-data guarantee. Its stability assertion is about the exact normalized moment ratio, on cap-height ranges bounded away from zero; it does not state global conditioning for unnormalized radius recovery as the cap collapses. The uniqueness theorem is restricted to uniformly sampled three-dimensional **solid spherical caps** and does not cover arbitrary ball intersections, spherical surface sampling or higher-dimensional caps. Historical priority is provisional: relevant generic moment formulas, particularly García-Pelayo (2011), were not available in complete inspectable form, and unlocated equivalent treatments remain possible.

## References
1. T. Moseeva, A. Tarasov, D. Zaporozhets, *Random sections of spherical convex bodies*, arXiv:2007.07297 (first submitted 2020-07-14), https://arxiv.org/abs/2007.07297.
2. G. Bonnet, A. Gusakova, C. Thäle, D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, arXiv:2010.03351 (first submitted 2020-10-07), https://arxiv.org/abs/2010.03351.
3. S.-J. Tu, E. Fischbach, *Random Distance Distribution for Spherical Objects*, arXiv:math-ph/0201046 (2002), https://arxiv.org/abs/math-ph/0201046.
4. R. García-Pelayo, *Moments of the distribution of distance*, Journal of Mathematical Physics 52 (2011), 033505, DOI:10.1063/1.3559719.
5. T. Moseeva, *Random sections of convex bodies*, Zap. Nauchn. Sem. POMI 486 (2019), 190–199; DOI:10.1007/s10958-021-05585-y for the English publication.
