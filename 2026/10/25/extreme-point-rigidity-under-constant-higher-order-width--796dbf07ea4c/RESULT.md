# Extreme-point rigidity under constant higher-order width

## Finding

Let \(k\geq3\) be an integer and \(c>0\). For a planar convex body \(K\), let \(h_K(\theta)\) be its support function and impose the constant \(k\)-order width condition of Ou and Pan:

\[
\sum_{j=0}^{k-1}h_K\!\left(\theta+\frac{2\pi j}{k}\right)=c
\quad\text{for all }\theta.
\]

All such bodies have the same perimeter \(2\pi c/k\), and the collection is convex under Minkowski interpolation after identifying translations. The following is a complete extreme-point characterization **without any smoothness or genericity hypothesis**:

**Theorem.** A body in this class is Minkowski-extreme modulo translations if and only if its generalized curvature-radius density

\[
\rho_K(\theta)=h_K(\theta)+h_K''(\theta)
\]

is almost everywhere either \(0\) or \(c\). Every body in this class automatically has an essentially bounded density, with

\[
0\leq\rho_K(\theta)\leq c,
\qquad
\sum_{j=0}^{k-1}\rho_K\!\left(\theta+\frac{2\pi j}{k}\right)=c
\quad\text{a.e.}
\]

In particular, for almost every fundamental angle \(t\in[0,2\pi/k)\), the \(k\)-tuple of curvature-radius values is an extreme simplex vertex: exactly one of its entries is \(c\) and the remaining entries are zero.

**Corollary.** A global least-area body of prescribed constant \(k\)-order width exists. Every such minimizer is Minkowski-extreme and therefore has the foregoing two-valued curvature radius. This is a structural necessary condition for the generalized Blaschke–Lebesgue problem; it does **not** identify all minimizers or their minimum area.

For \(k=3\), the centrally symmetric lens bounded by two circular arcs of radius \(c\), each turning through \(\pi/3\), belongs to the class. Its area is exactly

\[
A_{\mathrm{lens}}=c^2\left(\frac\pi3-\frac{\sqrt3}{2}\right),
\]

which provides an explicit admissible upper bound on the global minimum, strictly below the equal-perimeter disk area \(\pi c^2/9\).

## Assumptions and scope

A **body** means a compact convex subset of the Euclidean plane with nonempty interior. Its support function is \(h_K(\theta)=\max_{x\in K}x\cdot(\cos\theta,\sin\theta)\), defined modulo the addition of a first harmonic (translation). The distribution \(h_K+h_K''\) is the nonnegative curvature-radius measure indexed by outer normal angle. When absolutely continuous it is denoted \(\rho_K(\theta)\,d\theta\). All equality and two-valued conditions on \(\rho_K\) are Lebesgue-almost-everywhere statements. Minkowski extremality means that \(K=(K_++K_-)/2\), with both \(K_\pm\) satisfying the same constant \(k\)-order width, forces \(K_+\) and \(K_-\) to be translates; any nontrivial convex combination can be reduced to the midpoint criterion by adjusting interpolation coefficients.

The result applies to all integers \(k\geq3\) and all \(c>0\). The proof actually also specializes to the known two-rotation, ordinary constant-width case \(k=2\); that classical case is not part of the claimed contribution. No restriction to finite Fourier degree, polygonal bodies, or smooth boundaries is made.

## Proof

### 1. The curvature simplex and the closure condition

Write \(S_k f(\theta)=\sum_{j=0}^{k-1}f(\theta+2\pi j/k)\). Rotation commutes with differentiation in distributions, hence

\[
S_k(h+h'')=(1+\partial_\theta^2)S_kh=c\,d\theta.
\]

For every convex body the curvature-radius measure \(\mu=h+h''\) is nonnegative. The previous identity is \(\sum_jR_{2\pi j/k}\mu=c\,d\theta\). Since all summands are nonnegative measures, \(0\leq\mu\leq c\,d\theta\), so \(\mu=\rho\,d\theta\) with \(0\leq\rho\leq c\) a.e., and the displayed orbit-sum identity holds. Integrating the sum over one fundamental interval gives \(\int_0^{2\pi}\rho\,d\theta=2\pi c/k\), the common perimeter. Translation invariance follows from \(\sum_{j=0}^{k-1}e^{2\pi ij/k}=0\).

Conversely, an essentially bounded nonnegative \(2\pi\)-periodic function \(\rho\) with \(S_k\rho=c\) and vanishing first Fourier moments \(\int_0^{2\pi}\rho(\theta)e^{i\theta}\,d\theta=0\) determines a periodic solution of \(h+h''=\rho\), unique modulo first harmonics. Its positively homogeneous extension is convex, so \(h\) is the support function of a convex body; \(S_kh=c\) because \(S_k\rho=c\) and the first-harmonic ambiguity is annihilated by \(S_k\). Thus the permissible densities are precisely the nonnegative simplex fields with the two real first-moment constraints. The body is full-dimensional: a segment has atomic curvature-radius measure, whereas \(\rho\in L^\infty\) has none.

### 2. Two-valued density implies extremality

Suppose \(\rho(\theta)\in\{0,c\}\) almost everywhere and \(K=(K_++K_-)/2\). The feasible measures of \(K_\pm\) have densities \(0\leq\rho_\pm\leq c\), with \(\rho=(\rho_++\rho_-)/2\). At a point where \(\rho=0\), nonnegativity forces both densities to vanish. At a point where \(\rho=c\), the upper bound forces both to equal \(c\). Hence \(\rho_+=\rho_-=\rho\) almost everywhere. Therefore \(h_+-h_-\) solves \(u''+u=0\), so it is a first harmonic and the two bodies differ only by translation. This proves extremality.

### 3. Interior simplex mass implies a genuine midpoint decomposition

Suppose instead that the density is not two-valued on a positive-measure set. Write on \(t\in[0,2\pi/k)\)

\[
r_j(t)=\rho\!\left(t+\frac{2\pi j}{k}\right),
\qquad r_j(t)\geq0,\qquad \sum_jr_j(t)=c.
\]

A simplex vector that is not a vertex has at least two strictly positive coordinates. Because there are finitely many pairs and the union of threshold sets exhausts this event, there exist distinct indices \(p,q\), a number \(\delta>0\), and a measurable set \(E\subset[0,2\pi/k)\) of positive measure on which \(r_p,r_q\geq\delta\).

Choose three disjoint positive-measure subsets of \(E\). The two real linear equations

\[
\int_E\phi(t)\cos t\,dt=0,
\qquad
\int_E\phi(t)\sin t\,dt=0
\]

have a nonzero bounded solution \(\phi\) constant on those three subsets, by the nontrivial kernel of a two-by-three real matrix. Scale it so \(|\phi|\leq\delta\). Define the perturbation \(g\) on one full turn by

\[
g\!\left(t+\frac{2\pi j}{k}\right)=
\begin{cases}
\phi(t),&j=p,\\
-\phi(t),&j=q,\\
0,&\text{otherwise},
\end{cases}\qquad t\in[0,2\pi/k).
\]

Then \(S_kg=0\), and the two moment equations ensure \(\int_0^{2\pi}g(\theta)e^{i\theta}\,d\theta=0\), since the first harmonic is multiplied by the nonzero constant \(e^{2\pi ip/k}-e^{2\pi iq/k}\). Both \(\rho_+=\rho+g\) and \(\rho_-=\rho-g\) are nonnegative, satisfy the same orbit sum and closure moments, and are distinct. By Step 1 they define feasible convex bodies \(K_+,K_-\), and their average has the original curvature measure. Consequently \(K=(K_++K_-)/2\) up to translation, with nontranslates \(K_\pm\). Thus \(K\) is not extreme. This proves the reverse implication.

### 4. Strict concavity and area minimizers

Fix translations, for instance by requiring the first harmonics of \(h\) to vanish. Write \(\widehat\rho_n=(2\pi)^{-1}\int_0^{2\pi}\rho(\theta)e^{-in\theta}\,d\theta\). Since \(\widehat\rho_0=c/k\) and \(\widehat\rho_{\pm1}=0\), the usual support-function area formula gives the absolutely convergent series

\[
A(K)=\frac12\int_0^{2\pi}h\rho\,d\theta
=\pi\left(\frac ck\right)^2
-2\pi\sum_{n=2}^{\infty}\frac{|\widehat\rho_n|^2}{n^2-1}.
\]

For two distinct feasible densities \(\rho_1,\rho_2\) and \(0<t<1\), subtracting the affine interpolation of their areas yields

\[
A(t\rho_1+(1-t)\rho_2)-tA(\rho_1)-(1-t)A(\rho_2)
=2\pi t(1-t)\sum_{n=2}^{\infty}
\frac{|\widehat\rho_{1,n}-\widehat\rho_{2,n}|^2}{n^2-1}>0.
\]

The inequality is strict: all constant and first harmonics already agree, so some higher harmonic differs whenever the densities differ. Therefore area is strictly concave on the translation-quotiented feasible set. An area minimizer cannot be a nontrivial midpoint: one of the two endpoints would have strictly smaller area.

Existence follows from compactness. Every feasible body has fixed perimeter \(2\pi c/k\); after fixing the Steiner point, all lie in a uniformly bounded disk. Blaschke selection gives Hausdorff convergence of a subsequence of any minimizing sequence. The constant-width support identity is closed under uniform support-function convergence, and area is Hausdorff-continuous. Any limiting feasible compact convex set is a body rather than a segment, since its curvature measure remains dominated by \(c\,d\theta\) but a nontrivial segment has nonzero atomic curvature measure; a point cannot have the prescribed positive perimeter. Thus the least-area body exists. Strict concavity forces its extremality, and the characterization proves the two-valued necessary condition.

### 5. A concrete three-rotation lens

For \(k=3\), define \(\rho=c\) on the disjoint normal-angle intervals \([0,\pi/3)\) and \([\pi,4\pi/3)\), and \(\rho=0\) elsewhere, all angles modulo \(2\pi\). Each orbit \(\{t,t+2\pi/3,t+4\pi/3\}\) meets the occupied set once (up to endpoints), so \(S_3\rho=c\). The occupied set is invariant under rotation by \(\pi\), hence both first Fourier moments vanish. By Step 1 this density generates a centrally symmetric feasible body.

The normal-angle set has two active intervals of length \(\pi/3\); its boundary comprises two circular arcs of radius \(c\), each subtending \(\pi/3\), joined at their two endpoints. Equivalently this is the intersection of two radius-\(c\) disks with center separation \(\sqrt3\,c\). The exact two-segment circular area is

\[
A=2\left[\frac{c^2}{2}\left(\frac\pi3-\sin\frac\pi3\right)\right]
=c^2\left(\frac\pi3-\frac{\sqrt3}{2}\right).
\]

Its curvature radius takes only \(0,c\), so the lens is an extreme member, but this alone does not establish that it globally minimizes area.

## Verification

The analytical proof uses only positivity of planar curvature-radius measures, solvability of the periodic equation \(h''+h=\rho\) with first-moment closure, a finite-dimensional moment-annihilation construction, Fourier orthogonality, and compactness of fixed-perimeter convex bodies. All essential implications hold for arbitrary nonsmooth convex bodies. The accompanying script `verify_k3_example.py` independently checks the three-rotation curvature orbit sum, the first Fourier moment and numerical Fourier area for the explicitly described lens at a fine discrete resolution. It is a consistency check, **not** a proof of the general extreme-point theorem; the proof above is analytic.

For \(c=1\), the exact lens area is approximately \(0.181172147412159\), whereas the equal-perimeter disk area is approximately \(0.349065850398866\). Numeric agreement of the Fourier approximation with the exact circular-segment value can be reproduced with Python and NumPy.

## Relationship to prior work

Ou and Pan (2010) introduced the constant \(k\)-order width constraint, proved its fixed-perimeter law and support-Fourier characterization, and explicitly posed the associated minimum-area question. Their paper does not provide a complete extreme-point classification or the curvature-radius minimizer reduction. The ordinary \(k=2\) case belongs to the classical theory of constant-width bodies: Kallay's two-valued curvature criterion, as quoted by Hynd (2025), is an important antecedent. The theorem here concerns the distinct constraints for all \(k\geq3\), where the curvature values form a \(k\)-simplex coupled by two global closure moments; the two-rotation statement does not imply it.

Gao, Martini and Zhang (2024) analyze smooth curvature flows converging to constant \(k\)-order width; the flow theorem has neither the global Minkowski extreme-point conclusion nor a least-area structural condition. Pan, Zhang and Chao (2016) optimize a different notion called biwidth, not the Ou–Pan \(k\)-order support sum. Zhang (2015/2016) studies geometric characterizations of constant higher-order width, and is a particularly relevant bibliographic risk because its complete manuscript could not be inspected.

## Limitations

The exact least area and a full classification of least-area bodies remain unproved. The two-valued condition is necessary but generally not sufficient for least area; an extreme body need not minimize a strictly concave functional. The lens is an explicit admissible example, not an asserted optimizer. The curvature-radius quantity is indexed by outer normal angle and is defined as a density of a measure, not as pointwise reciprocal curvature at every boundary point. The originality comparison remains contingent on a full reading of Zhang's specialist article (DOI below), which was inaccessible through the available lawful full-text routes. Independent expert audit has not been performed.

## References

1. Ke Ou and Shengliang Pan, *Some Remarks about Closed Convex Curves*, Pacific Journal of Mathematics 248 (2010), 393–401. DOI: 10.2140/pjm.2010.248.393. Complete publicly accessible paper: https://msp.org/pjm/2010/248-2/pjm-v248-n2-p08-p.pdf.
2. Deyan Zhang, *A Generalization of Domains of Constant Width*, Beiträge zur Algebra und Geometrie 57 (2016), 259–270. DOI: 10.1007/s13366-015-0252-8. Full-text access unresolved.
3. Shengliang Pan, Deyan Zhang and Zhongjun Chao, *A Generalization of the Blaschke–Lebesgue Problem to a Kind of Convex Domains*, Discrete and Continuous Dynamical Systems B 21 (2016), 1587–1601. DOI: 10.3934/dcdsb.2016012.
4. Laiyuan Gao, Horst Martini and Deyan Zhang, *Deforming Locally Convex Curves into Curves of Constant \(k\)-order Width* (2024), arXiv:2404.05267.
5. Ryan Hynd, *On Extreme Constant Width Bodies in \(\mathbb R^3\)*, arXiv:2501.16940 (2025), especially the discussion of Kallay's planar extreme-point characterization.
6. Rolf Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, Cambridge University Press, 1993, for curvature measures and support functions.
