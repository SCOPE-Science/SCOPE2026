# Sharp Mahler-product monotonicity of symmetric planar circular lenses

## Finding
For \(0\le a<1\), let \(B_2^2(c,1)\) denote the closed unit Euclidean disk centered at \(c\in\mathbb R^2\), and define the centrally symmetric lens
\[
K_a=B_2^2(ae_1,1)\cap B_2^2(-ae_1,1),\qquad e_1=(1,0).
\]
Write \(K_a^\circ=\{u\in\mathbb R^2:\langle u,x\rangle\le1\text{ for all }x\in K_a\}\) and \(\mathcal P(a)=\operatorname{area}(K_a)\operatorname{area}(K_a^\circ)\). The areas and their product are exactly
\[
\operatorname{area}(K_a)=2\bigl(\arccos a-a\sqrt{1-a^2}\bigr),\qquad
\operatorname{area}(K_a^\circ)=\frac{\pi+4a}{(1-a^2)^{3/2}},
\]
\[
\boxed{\mathcal P(a)=\frac{2(\pi+4a)(\arccos a-a\sqrt{1-a^2})}{(1-a^2)^{3/2}}.}
\]
The product is **strictly decreasing on \((0,1)\)**, with the sharp family-specific inequalities
\[
\boxed{\frac{4(\pi+4)}3<\mathcal P(a)\le\pi^2\quad(0\le a<1).}
\]
Equality on the right holds precisely for the unit disk at \(a=0\); the left endpoint is an unattained limit as \(a\to1^-\). In that limit, a linear rescaling of \(K_a\) converges to the full-dimensional parabolic lens
\[
C=\{(X,Y)\in\mathbb R^2:|X|+Y^2\le1\},\qquad
\operatorname{area}(C)\operatorname{area}(C^\circ)=\frac{4(\pi+4)}3.
\]
Thus the lower constant has an affine-geometric model and is not just a formal asymptotic number.

## Assumptions and scope
All areas are planar Euclidean Lebesgue areas. The polar is taken about the origin, which is the center of symmetry and hence a Santaló point of \(K_a\). For \(a<1\), the lens has nonempty interior and contains the origin. The limiting case \(a=1\) is excluded because the actual intersection is a singleton and has no finite planar polar area. The result applies to two disks of any common radius by similarity invariance of the Mahler product, but not to arbitrary unequal-radius intersections or arbitrary higher dimensions.

## Proof
**1. The lens area.** Membership in both disks is equivalent to
\[
(|x|+a)^2+y^2\le1,
\]
so for \(|x|\le1-a\) the vertical section has length \(2\sqrt{1-(|x|+a)^2}\). Hence, setting \(b=\sqrt{1-a^2}\) and \(\alpha=\arccos a\),
\[
\operatorname{area}(K_a)=4\int_a^1\sqrt{1-z^2}\,dz
=2(\alpha-ab).
\]

**2. The polar area.** For \(u=(\cos\theta,\sin\theta)\) in the first quadrant the support function is
\[
h_{K_a}(u)=
\begin{cases}
1-a\cos\theta,&0\le\theta\le\alpha,\\
b\sin\theta,&\alpha\le\theta\le\pi/2.
\end{cases}
\]
Indeed, optimizing \(x\cos\theta+y\sin\theta\) over the upper-right section reduces to maximizing \((z-a)\cos\theta+\sqrt{1-z^2}\sin\theta\) over \(a\le z\le1\); the unconstrained maximizer \(z=\cos\theta\) lies in the interval exactly when \(\theta\le\alpha\). The other branch occurs when the maximum is attained at \(x=0\). Reflection symmetry gives the remaining quadrants. The radial function of \(K_a^\circ\) is \(1/h_{K_a}\), so radial integration gives
\[
\operatorname{area}(K_a^\circ)=2\left[
\int_0^\alpha\frac{d\theta}{(1-a\cos\theta)^2}
+\frac1{b^2}\int_\alpha^{\pi/2}\!\csc^2\theta\,d\theta\right].
\]
The tangent half-angle substitution, using \(\tan(\alpha/2)=b/(1+a)\), shows
\[
\int_0^\alpha\frac{d\theta}{1-a\cos\theta}=\frac\pi{2b}.
\]
For the squared denominator, the identity
\[
\frac1{(1-a\cos\theta)^2}=\frac1{b^2(1-a\cos\theta)}
+\frac a{b^2}\frac{d}{d\theta}\left(\frac{\sin\theta}{1-a\cos\theta}\right)
\]
gives
\[
\int_0^\alpha\frac{d\theta}{(1-a\cos\theta)^2}
=\frac\pi{2b^3}+\frac a{b^3}.
\]
Since \(\cot\alpha=a/b\), the other integral equals \(a/b^3\). Thus \(\operatorname{area}(K_a^\circ)=(\pi+4a)/b^3\), and multiplying by the lens area proves the closed product formula.

**3. Strict monotonicity.** Put \(N(a)=\arccos a-ab\), so \(N'(a)=-2b\) and \(N(a)>0\) for \(0\le a<1\). Define
\[
H(a)=\bigl(4+8a^2+3\pi a\bigr)N(a)-2(\pi+4a)b^3.
\]
Direct differentiation, with \(b'=-a/b\), gives
\[
\mathcal P'(a)=\frac{2H(a)}{b^5},\qquad
H'(a)=(16a+3\pi)N(a)-16b^3,\qquad
H''(a)=16\arccos a-6\pi b.
\]
Set \(\theta=\arccos a\in(0,\pi/2)\). Since \(\theta/\sin\theta\) is strictly increasing in \(\theta\) (its derivative has numerator \(\sin\theta-\theta\cos\theta>0\)), the sign of
\[
H''(a)=2b\left(\frac{8\theta}{\sin\theta}-3\pi\right)
\]
changes **exactly once**, from positive to negative as \(a\) grows from \(0\) to \(1\). The needed endpoint data are
\[
H(0)=0,\quad \lim_{a\to1^-}H(a)=0,\quad
H'(0)=\frac{3\pi^2}{2}-16<0,
\]
\[
\lim_{a\to1^-}\frac{H'(a)}{b^3}=\frac{6\pi-16}{3}>0,
\quad\text{and}\quad \lim_{a\to1^-}H'(a)=0.
\]
These signs are strict, for example by the elementary bounds \(3<\pi<22/7\). Since \(H'\) first increases strictly and then decreases strictly to \(0\) from above, it crosses zero exactly once, going from negative to positive. Consequently \(H\), starting and ending at zero, first decreases and then increases, remaining strictly negative between endpoints. Hence \(\mathcal P'(a)<0\) for all \(0<a<1\). This proves the sharp monotonicity statement independently of any numerical plots.

**4. Limiting geometry and value.** As \(a\to1^-\), let \(\varepsilon=1-a\) and apply the invertible linear map
\[
(x,y)\mapsto\left(X=\frac{x}{\varepsilon},\;Y=\frac{y}{\sqrt{2\varepsilon}}\right).
\]
The transformed lens satisfies
\[
|X|\le1,\qquad
Y^2\le1-|X|-\frac\varepsilon2(1-|X|)^2.
\]
It therefore converges in Hausdorff distance to \(C=\{|X|+Y^2\le1\}\), which has interior. The volume product is invariant under invertible linear maps and continuous under Hausdorff convergence when the limit contains the origin in its interior. On the other hand,
\[
\lim_{a\to1^-}\frac{\arccos a-a\sqrt{1-a^2}}{(1-a^2)^{3/2}}=\frac23,
\]
obtained by writing \(a=\cos\theta\) and expanding \(\theta-\sin\theta\cos\theta\) at \(\theta=0\). Thus \(\mathcal P(C)=2(\pi+4)(2/3)=4(\pi+4)/3\). Directly, \(\operatorname{area}(C)=8/3\), so also \(\operatorname{area}(C^\circ)=(\pi+4)/2\).

## Verification
The included standalone `verify.py` uses only the Python standard library. It independently integrates the primal sections using a nonsingular change of variable, and the polar radial integral using Simpson quadrature. It also checks the support-branch junction, derivative sign, decreasing products on a deterministic grid, and both endpoints. Executing `python verify.py` produced `PASS: 2045 deterministic geometric/numerical assertions; analytic proof required for all parameters.` These finite diagnostics do not establish strict monotonicity for uncountably many values; the derivative-sign argument above does.

## Relationship to prior work
The Blaschke–Santaló upper bound gives \(\mathcal P(K)\le\pi^2\) for planar centrally symmetric convex bodies, and the planar Mahler bound gives \(\mathcal P(K)\ge8\). Both are global bounds, not the strict separation-dependent law or the sharp family-specific lower constant established here. Meyer and Reisner (2006) investigate polar volumes along general shadow systems; those general convexity statements do not supply the displayed lens product or its derivative signs.

Finch (2013) computes geometric quantities of the three-dimensional symmetric lens, not this planar Mahler-product law. An accessible published research record entitled *Mean width of a symmetric lens in every dimension* gives the same lens support-function branches, which are therefore prior work, and evaluates the angular **first power** of that support function to obtain mean width. In contrast, polar area here requires the angular **inverse square**; the exact product and global strict monotonicity are separate conclusions. The accessible record and the inspected primary literature do not state those conclusions. The novelty assessment is bounded by these searches and inspections, not an assertion of exhaustive historical priority.

## Limitations
The theorem is for the centrally symmetric intersection of exactly two congruent Euclidean disks in the plane and for the origin-based polar. It does not extend by this proof to unequal-radius lenses, intersections of three or more disks, or higher-dimensional volume products. The degenerating original lens at \(a=1\) itself has no finite planar polar area; the lower sharp value is for its full-dimensional affine blow-up limit. Historical literature on intrinsic volumes, polar areas and related symmetrizations is large; an equivalent formula in an older unindexed source remains an originality risk. Neither a general solution to Mahler's conjecture nor a new Blaschke–Santaló bound for arbitrary bodies is claimed.

## References
1. M. Meyer and S. Reisner, *Shadow systems and volume of polar convex bodies*, arXiv:math/0606305v1, posted 2006-06-13; https://arxiv.org/abs/math/0606305 .
2. S. R. Finch, *Mutually Equidistant Spheres that Intersect*, arXiv:1301.5515v1, posted 2013-01-23; https://arxiv.org/abs/1301.5515 .
3. K. J. Böröczky, E. Makai Jr., M. Meyer and S. Reisner, *Volume product of planar polar convex bodies — lower estimates with stability*, arXiv:1507.01481v1, posted 2015-07-06; https://arxiv.org/abs/1507.01481 .
4. *Mean width of a symmetric lens in every dimension*, publicly accessible mathematical research record; https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-mean-width-of-a-symmetric-lens-in-every-dimension--80ec085cfff6 .
