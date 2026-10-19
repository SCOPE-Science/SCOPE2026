# Exact half-turn locking tongue for normalized affine circle maps

## Finding

For a real parameter \(0<\alpha<1\), the normalized affine circle homeomorphism
\[
F_{\alpha,\theta}(z)=\frac{\alpha+e^{i\theta}z}{|\alpha+e^{i\theta}z|},\qquad z\in\mathbb S^1\subset\mathbb C,
\]
has a primitive two-cycle if and only if
\[
\operatorname{dist}_{\mathbb R/2\pi\mathbb Z}(\theta,\pi)
\le \delta_\alpha:=\arcsin\left(\frac{1-\sqrt{1-\alpha^2}}{2}\right).
\]
At a strict inequality there are **exactly two primitive two-cycles**, one attracting and one repelling; every orbit outside the repelling two-cycle approaches the attracting two-cycle. At either equality there is **exactly one primitive two-cycle**, with return multiplier one, and all circle orbits approach that (nonhyperbolic) cycle. Outside the closed locking interval no primitive two-cycles exist. In particular this is a complete half-rotation locking interval, not merely a sufficient parameter neighborhood.

For \(0<s:=|\sin\theta|<s_\alpha:=(1-\sqrt{1-\alpha^2})/2\) within the locking interval, put \(c=-\cos\theta>0\), \(r=e^{i\theta}\), and
\[
q_\pm=\frac{\alpha^2+4s^2\pm\sqrt{(\alpha^2+4s^2)^2-16s^2}}2.
\]
For either sign, set \(p=1-q_\pm\), \(u=c+\sqrt{q_\pm-s^2}\), \(v=c-\sqrt{q_\pm-s^2}\). A representative of the corresponding two-cycle is
\[
z=\frac{\alpha(u+r)}{p-r^2},\qquad w=\frac{\alpha(v+r)}{p-r^2};\qquad F_{\alpha,\theta}(z)=w,\quad F_{\alpha,\theta}(w)=z.
\]
The lower branch \(q_-\) is attracting; the upper branch \(q_+\) is repelling. Their exact return multipliers are
\[
\Lambda(q)=\frac{(u^2+1-\alpha^2)(v^2+1-\alpha^2)}{4u^2v^2},\qquad
\Lambda(q)-1=\frac{(q^2-4s^2)(q-s^2)}{(1-q)q^2}.
\]
At either locking endpoint the roots coalesce at \(q=2s_\alpha\). The branch gap obeys the sharp square-root law
\[
q_+-q_-\sim \sqrt{32s_\alpha\sqrt{1-\alpha^2}}\sqrt{s_\alpha-s}
\quad (s\uparrow s_\alpha).
\]
For weak forcing the tongue half-width satisfies \(\delta_\alpha=\alpha^2/4+O(\alpha^4)\).

## Assumptions and scope

The domain is the **entire unit circle** with Euclidean complex modulus. The parameters obey \(\alpha\in(0,1)\), \(\theta\in\mathbb R/(2\pi\mathbb Z)\); exact real arithmetic and Euclidean radial normalization are part of the definition. Every primitive two-cycle comprises two distinct points interchanged by \(F_{\alpha,\theta}\). Return multiplier means the derivative of \(F_{\alpha,\theta}^2\) in the positively oriented angular coordinate. At the central angle \(\theta=\pi\), some algebraic formulas have removable singularities and the two cycles are treated separately. No assertion is made about other rational rotation-number tongues.

## Proof

**1. Circle orientation and exclusions.** As \(0<\alpha<1\), \(\alpha+r z\ne0\) for \(|z|=1\), and radial projection induces a smooth orientation-preserving diffeomorphism. Its angular derivative is
\[
D_{\angle}F_{\alpha,\theta}(z)=
\frac{1+\alpha\operatorname{Re}(r z)}{|\alpha+r z|^2}>0.
\]
If a circle orientation-preserving homeomorphism has a fixed point, it has no distinct prime-two point: a lift of a fixed-point circle homeomorphism restricts to a strictly increasing map between consecutive fixed lifts and cannot possess a nontrivial two-cycle. At \(\theta=0\) fixed points exist, hence no primitive two-cycle. We now handle \(\theta\not\equiv0,\pi\) modulo \(2\pi\).

**2. Necessary algebraic reduction.** Let \(z\ne w\), \(|z|=|w|=1\), and \(F(z)=w\), \(F(w)=z\). The two positive normalization factors \(u=|\alpha+r z|\), \(v=|\alpha+r w|\) satisfy
\[
u w=\alpha+r z,\qquad v z=\alpha+r w.
\]
Writing \(p=uv\), eliminating \(w\) gives
\[
(p-r^2)z=\alpha(u+r),\qquad(p-r^2)w=\alpha(v+r).
\]
Because \(p>0\) and \(r^2\) is not positive real for \(\theta\not\equiv0,\pi\), the denominator is nonzero. Equality of \(|z|^2\) and \(|w|^2\) now implies
\[
(u-v)(u+v+2\cos\theta)=0.
\]
The alternative \(u=v\) implies \(z=w\), so \(u+v=-2\cos\theta=2c>0\), requiring \(\cos\theta<0\). Let \(s=|\sin\theta|\), \(q=1-p\). Since \(uv=p\in(0,c^2]\), necessarily \(q\in[s^2,1)\). The identity \(u+v=2c\) gives \(|u+r|^2=1-p=q\), while \(|p-r^2|^2=q^2+4s^2(1-q)\). Taking the modulus of the displayed expression for \(z\) yields precisely
\[
Q(q):=q^2-(\alpha^2+4s^2)q+4s^2=0.
\]
Thus every primitive two-cycle at a noncentral angle determines an admissible root of \(Q\). Exchanging the cycle's two points exchanges \(u,v\) but not \(q\), so one root can represent at most one cycle.

**3. Sharp root existence and converse.** Write
\[
s_\alpha=\frac{1-\sqrt{1-\alpha^2}}2,
\qquad S_\alpha=\frac{1+\sqrt{1-\alpha^2}}2.
\]
For \(s\in(0,1)\), the discriminant factors as
\[
\Delta(s)=(\alpha^2-4s(1-s))(\alpha^2+4s(1+s)).
\]
For \(0<s<s_\alpha\) one has \(s^2<2s<1\), \(Q(s^2)=s^2(4-\alpha^2-3s^2)>0\), \(Q(1)=1-\alpha^2>0\), and \(Q(2s)=2s(4s(1-s)-\alpha^2)<0\). Therefore **exactly two** roots lie in \((s^2,1)\), straddling \(2s\). At \(s=s_\alpha\) there is one double admissible root \(q=2s_\alpha\). For \(s_\alpha<s<S_\alpha\) the discriminant is negative. For \(s\ge S_\alpha\) the quadratic vertex \((\alpha^2+4s^2)/2\ge2S_\alpha>1\), so \(Q\) is decreasing throughout \([s^2,1]\); since \(Q(1)>0\), there is no admissible root. If \(\cos\theta\ge0\), the prior sum condition independently excludes a primitive two-cycle.

Conversely, for any admissible root \(q\) under \(\cos\theta<0\), define \(p,u,v,z,w\) by the formulas in the finding, choosing the nonnegative square root. They obey \(u,v>0\), \(uv=p\), \(|u+r|^2=q\), and \(\alpha^2q=|p-r^2|^2\). Therefore \(|z|=|w|=1\); substituting in the linear equations proves \(u w=\alpha+r z\) and \(v z=\alpha+r w\). Positivity of \(u,v\) proves \(F(z)=w\), \(F(w)=z\). In fact \(u\ne v\) even at the coalescence because \(q\ge 2s_\alpha>s^2\) at the endpoint. Thus every reconstructed pair is genuinely primitive. Every admissible root thus gives exactly one primitive two-cycle, with no omitted solutions.

The three inequalities above imply the exact locking region \(d(\theta,\pi)\le\arcsin s_\alpha\). The central case \(\theta=\pi\) is addressed in Step 5.

**4. Multipliers and global basins.** The angular derivative in Step 1 is equal to \((u^2+1-\alpha^2)/(2u^2)\) along an orbit with normalization factor \(u\), since \(u^2=1+\alpha^2+2\alpha\operatorname{Re}(rz)\). Multiplication at \(z,w\), reduction using \(Q(q)=0\), and \(uv=1-q\) yield the exact displayed identity for \(\Lambda(q)-1\). Because \(q>s^2\), its sign is the sign of \(q-2s\). The smaller root is hyperbolically attracting and the larger hyperbolically repelling; the double root is neutral. Each two-cycle gives exactly two fixed points of the orientation-preserving map \(F^2\). In the strict interior, these are the **only four** fixed points of \(F^2\), and its monotone motion between consecutive fixed points forces every forward orbit except the repelling two-cycle to converge to the attracting cycle. At an endpoint there are exactly two fixed points of \(F^2\), forming one neutral two-cycle; interval monotonicity similarly forces every forward orbit to approach that cycle. This convergence is a topological statement, not exponential attraction at the neutral endpoint.

**5. Central angle and endpoint asymptotics.** When \(\theta=\pi\), the two known primitive two-cycles are \(\{1,-1\}\) and the unordered pair of points on \(\mathbb S^1\) with real part \(\alpha/2\) and opposite imaginary parts. Their return multipliers are, respectively, \((1-\alpha^2)^{-1}>1\) and \((1-\alpha^2/2)^2<1\). Direct substitution establishes the identities and shows the two-cycle count continues across the central angle; this central classification was already established in the cited source and is not a separate novelty claim.

At fixed \(\alpha\), the factorization of \(\Delta\) gives \(\Delta(s)=32s_\alpha\sqrt{1-\alpha^2}(s_\alpha-s)+O((s_\alpha-s)^2)\) as \(s\uparrow s_\alpha\); the radical formula yields the stated square-root separation. The Taylor expansions \(s_\alpha=\alpha^2/4+O(\alpha^4)\) and \(\arcsin(s_\alpha)=s_\alpha+O(s_\alpha^3)\) yield the weak-forcing law.

## Verification

The standalone `checks/circle_tongue_check.py` reproduces four symbolic identities: discriminant factorization, \(Q(2s)\), \(Q(s^2)\), and the multiplier formula after imposing \(Q(q)=0\). It also performs 90 independent double-precision substitution tests for the orbit equations and multiplier signs at both angular sides of the tongue and at the central angle, for five distinct positive forcing strengths. All passed when executed. This code does not replace the global polynomial-root or circle-monotonicity arguments; numerical checks are finite tests only.

## Relationship to prior work

Shah and Yadav (arXiv:1606.08797), Section 3 and Remark 9, established existence of four period-two points for sufficiently small unspecified angular perturbations of half-turn rotation and classified the exact half-turn qualitatively. Choudhuri, Faraco, and Yadav (arXiv:2209.05236), Proposition 8(ii), likewise show existence in some unspecified neighborhood, while Proposition 10 identifies the attracting and repelling central cycles. Both are acknowledged prior results. The present statement adds the **optimal, necessary-and-sufficient angular threshold for every \(0<\alpha<1\)**, exact cycles and return multipliers off the central angle, a global basin classification, and the square-root tongue-edge law. The rotation-order argument is standard, not proposed as original. Published searches revealed related but materially different circle-map smoothing and driven Möbius-map results, neither supplying this parameter threshold for the normalized affine family. Priority cannot be proved from a search; an unindexed equivalent proof is possible.

## Limitations

The theorem concerns only primitive period-two dynamics, its adjacent basin geometry, and the specified square-root boundary; it does not classify other periodic rotation numbers or invariant measures outside the half-turn tongue. It assumes \(0<\alpha<1\) and exact arithmetic. Global convergence at a critical endpoint has no asserted rate. Source priority is not independently certified. Numerical tests neither establish the infinite-angle classification nor rule out prior work.

## References

1. R. Shah and A. K. Yadav, *Dynamics of Certain Distal Actions on Spheres*, arXiv:1606.08797, Section 3, Remark 9. https://arxiv.org/pdf/1606.08797
2. M. Choudhuri, G. Faraco and A. K. Yadav, *On the Distality and Expansivity of Certain Maps on Spheres*, arXiv:2209.05236, Proposition 7, Proposition 8(ii), Proposition 10. First posted September 12, 2022. https://arxiv.org/pdf/2209.05236
