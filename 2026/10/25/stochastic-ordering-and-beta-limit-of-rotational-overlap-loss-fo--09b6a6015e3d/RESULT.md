# Stochastic ordering and beta limit of rotational overlap loss for regular polygons

## Finding
For each integer \(n\ge3\), let \(P_n\) be a centered regular \(n\)-gon of circumradius \(R>0\), and rotate an independent congruent copy through an angle \(\Phi\) uniformly distributed on \([0,2\pi)\). Define the overlap area loss \(\Delta_n=\operatorname{Area}(P_n)-\operatorname{Area}(P_n\cap R_\Phi P_n)\), its sharp positive maximum \(M_n\), and the normalized loss \(Q_n=\Delta_n/M_n\).

Put \(k_n=\pi/n\) and \(c_n=\cos k_n\). Then
\[
M_n=\operatorname{Area}(P_n)\tan^2(k_n/2),\qquad \operatorname{Area}(P_n)=nR^2\sin k_n\cos k_n.
\]
For every \(q\in[0,1]\), the complete distribution is
\[
\boxed{\mathbb P(Q_n\le q)=1-\frac{1}{k_n}\arccos\!\left(\frac{c_n(1+\eta_n(q))}{1-\eta_n(q)}\right),\qquad
\eta_n(q)=q\frac{1-c_n}{1+c_n}.}
\]
It is zero for \(q<0\), and one for \(q>1\). The arccosine input lies in \([c_n,1]\).

**Main new conclusion: a strict side-count stochastic hierarchy.** There is a simultaneous coupling of all \(Q_n\), \(n\ge3\), on a single uniform \(U\sim\operatorname{Unif}[0,1]\), under which
\[
\boxed{Q_3>Q_4>Q_5>\cdots>1-U^2\quad\text{almost surely}.}
\]
In particular \(Q_n\) strictly stochastically dominates \(Q_{n+1}\), and converges to the beta-distributed variable \(Q_\infty=1-U^2\), whose CDF is \(F_\infty(q)=1-\sqrt{1-q}\) on \([0,1]\). The finite-size correction is uniform in \(0\le U\le1\):
\[
Q_n=1-U^2+\frac{\pi^2}{6n^2}U^2(1-U^2)+O(n^{-4}).
\]
Consequently,
\[
\mathbb EQ_n=\frac23+\frac{\pi^2}{45n^2}+O(n^{-4}),\qquad
\operatorname{Var}(Q_n)\longrightarrow\frac4{45},
\]
and the *unscaled* geometric loss obeys
\[
\frac{n^2\Delta_n}{R^2}\ \xrightarrow{\ d\ }\ \frac{\pi^3}{4}(1-U^2).
\]
An exact finite-size mean, useful independently of the CDF, is
\[
\mathbb EQ_n=\frac{\tan k_n-(2/k_n)\log(\sec k_n)}{\tan k_n\tan^2(k_n/2)}.
\]

## Assumptions and scope
The two convex regular polygons have the same center, radius \(R>0\), and integer side count \(n\ge3\). The rotation is uniform modulo \(2\pi\), with translation forbidden; equality of angle distributions modulo polygonal symmetries suffices. Area denotes ordinary Euclidean planar area. Stochastic dominance means \(\mathbb P(Q_n>q)>\mathbb P(Q_{n+1}>q)\) for every \(0<q<1\); the common coupling supplies an almost-surely strict comparison. All limits take \(n\) through **all** integers, not a parity subsequence.

## Proof
**Tangency geometry.** Set \(k=\pi/n\) and \(r=R\cos k\). Each side of \(P_n\) is tangent to the disk of radius \(r\). Reduce the relative rotation modulo \(2k\) and fold by reflection to an angle \(\alpha\in[0,k]\). Because the original rotation is uniform, \(\alpha\) is uniform on \([0,k]\). Except at endpoints, the supporting-line normals of the two polygons interlace into \(2n\) cyclic angles with successive gaps alternating \(\alpha\) and \(2k-\alpha\). Every one of these tangent inequalities supports a genuine edge of the intersection: its point of tangency lies strictly inside all other supporting half-planes. For any polygon circumscribed about a circle of radius \(r\), if successive outward tangent normals have angular gaps \(\gamma_j\in(0,\pi)\), each corner contributes \(r\tan(\gamma_j/2)\) to each adjacent tangent length. Since area equals radius times semiperimeter,
\[
A_n(\alpha):=\operatorname{Area}(P_n\cap R_\alpha P_n)
=nr^2\bigl[\tan(\alpha/2)+\tan(k-\alpha/2)\bigr]. \tag{1}
\]
The endpoint formulas, by continuity, are \(A_n(0)=nr^2\tan k=\operatorname{Area}(P_n)\) and \(A_n(k)=2nr^2\tan(k/2)\). Equation (1) is symmetric about \(\alpha=k\), decreases strictly for \(0<\alpha<k\), and has no other extremum on the folded interval: differentiate to obtain \((nr^2/2)[\sec^2(\alpha/2)-\sec^2(k-\alpha/2)]<0\). Therefore the maximal loss is
\[
M_n=nr^2[\tan k-2\tan(k/2)]
=nr^2\tan k\tan^2(k/2)=\operatorname{Area}(P_n)\tan^2(k/2)>0. \tag{2}
\]

**Exact loss quantile and distribution.** Set \(U=1-\alpha/k\), which is uniform on \([0,1]\). Using \(\tan x+\tan y=\sin(x+y)/(\cos x\cos y)\), followed by \(2\cos a\cos b=\cos(a+b)+\cos(a-b)\), equation (1) gives
\[
A_n(\alpha)=\frac{2nr^2\sin k}{\cos k+\cos(kU)}.
\]
Subtract from \(A_n(0)=nr^2\sin k/\cos k\) and divide by (2):
\[
\boxed{Q_n=q_k(U)=\frac{\cos(kU)-\cos k}{\cos(kU)+\cos k}\,
\frac{1+\cos k}{1-\cos k}
=\frac{\tan((1+U)k/2)\tan((1-U)k/2)}{\tan^2(k/2)}.} \tag{3}
\]
Here \(q_k(U)\) is continuous, equals 1 at \(U=0\), equals 0 at \(U=1\), and is strictly decreasing in \(U\) in between. Given a threshold \(q\in[0,1]\), write \(c=\cos k\) and \(\eta=q(1-c)/(1+c)\). Solving (3) for its unique threshold gives \(\cos(kU)=c(1+\eta)/(1-\eta)\). Consequently \(\mathbb P(Q_n\le q)=\mathbb P(U\ge k^{-1}\arccos(c(1+\eta)/(1-\eta)))\), which is precisely the displayed CDF.

**Strict ordering across side counts.** Fix \(0<U<1\) and put \(a=1+U\), \(b=1-U\), so \(a+b=2\). Logarithmically differentiate the last product in (3) with respect to \(k\):
\[
\frac{\partial}{\partial k}\log q_k(U)
=\frac{a}{\sin(ak)}+\frac{b}{\sin(bk)}-\frac2{\sin k}
=\frac{f(ak)+f(bk)-2f(k)}{k},\quad f(z)=\frac z{\sin z}. \tag{4}
\]
The function \(f\) is strictly convex on \((0,\pi)\). Direct differentiation gives
\[
f''(z)=\frac{z(1+\cos^2z)-\sin(2z)}{\sin^3z}>0.
\]
Indeed the numerator vanishes at zero and its derivative is \(\sin z[3\sin z-2z\cos z]>0\) on \((0,\pi)\): for \(z<\pi/2\), use \(\tan z>z\); for \(z\ge\pi/2\), the cosine is nonpositive. Since \(0<bk<k<ak\le2\pi/3<\pi\) for every \(n\ge3\), strict Jensen convexity in (4) yields \(\partial_k\log q_k(U)>0\). As \(k_n=\pi/n\) strictly decreases, equation (3), with the same \(U\), proves \(Q_n>Q_{n+1}\) almost surely. Because all \(q_k\) are strictly monotone continuous transforms of a nonatomic uniform variable with common support \([0,1]\), this also gives a strict inequality between their survival probabilities for every interior threshold.

**Sharp asymptotics and mean.** The Taylor expansion \(\tan z=z+z^3/3+2z^5/15+O(z^7)\), used uniformly for \(0\le(1\pm U)k/2\le k\) as \(k\to0\), gives from (3)
\[
q_k(U)=1-U^2+\frac{k^2}{6}U^2(1-U^2)+O(k^4),
\]
with the remainder uniform over \([0,1]\). Thus the beta CDF follows from the uniform coupling, while expectation of \(U^2(1-U^2)\) is \(1/3-1/5=2/15\), proving the mean correction \(k^2/45\). Bounded convergence gives \(\operatorname{Var}(Q_n)\to\operatorname{Var}(1-U^2)=4/45\). Also, \(M_n=nR^2\sin k\cos k\tan^2(k/2)=\pi R^2k^2/4+O(R^2k^4)\), proving the geometric scaling limit.

For the exact mean, integrate (1) against uniform \(\alpha\in[0,k]\):
\[
\mathbb EA_n(\alpha)=\frac{nr^2}{k}\int_0^k[\tan(\alpha/2)+\tan(k-\alpha/2)]\,d\alpha
=\frac{2nr^2}{k}\log\sec k.
\]
Subtract this from \(nr^2\tan k\) and divide by (2). No stochastic independence assumption other than uniformity of the relative angle is needed.

## Verification
The standalone `verify.py` implements polygon intersection by sequential clipping against each edge of an independently constructed rotated regular polygon, without using the tangent-normal area formula as the reference. It compares 868 resulting polygon areas across every order \(n=3,\ldots,30\) and 31 nonsymmetric angles per order with the analytic formula, all within absolute tolerance \(10^{-9}\). It also numerically compares the exact CDF and first moment against uniform-angle samples, checks coupling monotonicity for \(3\le n<150\) and 199 interior values of \(U\), and checks the uniform \(k^2\) expansion at four large polygon orders. The checker prints `ALL_ROTATED_POLYGON_OVERLAP_CHECKS_OK`. These finite checks corroborate, but do not replace, the all-integer proof.

## Relationship to prior work
Buck and Siddon (2012) investigate exact areas of polygons circumscribed about a circle from prescribed **side lengths**; their tangency-area context does not provide the law of a random relative rotation. O'Rourke and Zaimi (2015) determine the **number of sides** in rotating regular-polygon intersections, not area distributions. Brazitikos and Stavrakakis (2014) obtain general estimates for random rotations of symmetric convex bodies in arbitrary dimension; a plausible author-hosted copy timed out, so their complete special-case coverage remains an access risk, but the accessible abstract does not state the finite regular-polygon distribution or ordering. A previously recorded exact gap law for the rotational intersection of **two regular tangential polygons of distinct orders** already gives the full area CDF in that setting. Its tangent-gap formula extends immediately to the equal-order case, so the equal-order CDF and its fixed-order mean are **supporting identities, not independently claimed new**. A published published-finding corpus finding, *Sharp random-rotation area order and exponential shape memory for tangential polygons* (2026), gives expected areas under multiple rotations, but no all-order stochastic comparison. The substantive result here is instead the strict stochastic ordering under a **single coupling across every side count**, with its universal beta limit and sharp second-order correction. Neither the unequal-order area law nor the published expectation theorem implies this all-side-count comparison. The elementary tangent-length identity and fixed-size mean are not asserted to be new.

## Limitations
Only concentric congruent regular Euclidean polygons under uniform **relative rotation** are treated. Translations, nonuniform rotations, different side counts or shapes, and intersections of three or more copies are excluded. The distribution has compact support, so no Gaussian or large-deviation assertion is made. The equal-order finite-size CDF is an elementary extension of an earlier unequal-order polygon gap law; the novelty claim is confined to strict cross-order coupling and its quantified beta limit, not the tangent formula or fixed-order CDF. One relevant general paper's full text was not accessible, and unindexed earlier formulas remain an originality risk. Independent scientific validation has not been performed.

## References
1. Marshall W. Buck and Robert L. Siddon, *The Area of a Polygon with an Inscribed Circle*, arXiv:1203.3438v1, first posted March 15, 2012, https://arxiv.org/html/1203.3438v1.
2. Silouanos Brazitikos and Pantelis Stavrakakis, *On the intersection of random rotations of a symmetric convex body*, Mathematical Proceedings of the Cambridge Philosophical Society 157 (2014), 13–30, https://doi.org/10.1017/S0305004114000115.
3. Joseph O'Rourke and Gjergji Zaimi, *Intersection of rotating regular polygons*, MathOverflow question and answer, October 17, 2015, https://mathoverflow.net/questions/221120/intersection-of-rotating-regular-polygons.
4. *Sharp random-rotation area order and exponential shape memory for tangential polygons*, published published-finding corpus result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-random-rotation-area-order-and-exponential-shape-memory-fo--9cc93a56f053.
