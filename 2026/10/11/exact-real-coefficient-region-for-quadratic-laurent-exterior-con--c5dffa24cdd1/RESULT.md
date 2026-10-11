# Exact real-coefficient region for quadratic Laurent exterior convexity

## Finding
For real \(a,b\), set
\[
f_{a,b}(z)=z+\frac{a}{z}+\frac{b}{z^2},\qquad |z|>1.
\]
The bounded complement of its image is convex, and the map is injective on the exterior unit disk, **if and only if**
\[
-1\le a\le1,\qquad |b|\le B(a),\qquad
B(a)=\begin{cases}(1+a)/4,&-1\le a\le0,\\
(1-a)\sqrt{1+a}/4,&0\le a\le1.
\end{cases}
\]
The sharp coefficient body \(\{(a,b): -1\le a\le1,\ |b|\le B(a)\}\) is convex. Therefore convex linear combinations of **any** two exterior-convex members of this entire real-coefficient two-term Laurent family are again exterior convex. At \(a=0\) the minimizing boundary angle changes from an endpoint to an interior critical angle. All inequalities are non-strict at the coefficient boundary; the image-complement convexity and exterior analyticity remain valid there.

## Assumptions and scope
The coefficients \(a,b\) are real. The normalization is that the leading coefficient at infinity is one and the constant Laurent coefficient is zero. Convexity means that \(f\) is univalent on \(\{|z|>1\}\) and the compact omitted set \(\mathbb C\setminus f(\{|z|>1\})\) is convex. The established criterion is \(\operatorname{Re}(1+zf''(z)/f'(z))>0\) for every \(|z|>1\). There is no claim concerning arbitrary complex pairs \((a,b)\) or higher Laurent coefficients.

## Proof
Put \(w=1/z\). Direct differentiation yields the exterior-convexity quantity
\[
Q(w)=1+\frac{zf''(z)}{f'(z)}
=\frac{1+aw^2+4bw^3}{1-aw^2-2bw^3},
\qquad
\Phi(w)=\frac{Q(w)-1}{Q(w)+1}
=w^2\frac{a+3bw}{1+bw^3}.
\]
Whenever the exterior map is convex, \(Q\) has positive real part and \(\Phi\) is a Schur function with a double zero at the origin. Twice applying Schwarz's lemma shows that \(S(w)=\Phi(w)/w^2\) is Schur. Its constant and linear Taylor coefficients are \(a\) and \(3b\), so the Cauchy coefficient bounds imply \(|a|\le1\) and \(|b|\le1/3\). In particular \(1+bw^3\ne0\) on \(|w|\le1\). By the maximum-modulus principle, \(|S(w)|\le1\) in the disk is equivalent to the boundary condition
\[
|a+3bw|\le|1+bw^3|\quad (|w|=1).
\]
Conversely, whenever \(|a|\le1\), \(|b|<1\), and this boundary condition holds, the maximum-modulus principle gives \(|S(w)|\le1\); hence \(|\Phi(w)|\le |w|^2<1\) inside. The inverse Cayley map makes \(\operatorname{Re}Q>0\), proving exterior convexity by the stated criterion. Thus it suffices to solve the exact boundary inequality.

Replacing \(w\) by \(-w\) changes \(b\) to \(-b\), so put \(t=|b|\). For \(w=e^{i\theta}\), with \(x=\cos\theta\in[-1,1]\), the squared-modulus difference is
\[
\begin{aligned}
|1+te^{3i\theta}|^2-|a+3te^{i\theta}|^2
&=1-a^2-8t^2+2t\{\cos3\theta-3a\cos\theta\}\\
&=1-a^2-8t^2+2t\{4x^3-3(1+a)x\}.
\end{aligned}
\]
The cubic \(g_a(x)=4x^3-3(1+a)x\) has candidate global minima \(g_a(-1)=3a-1\) and, when \(-1\le a\le1\), \(g_a(\sqrt{1+a}/2)=-(1+a)^{3/2}\). The other endpoint and interior critical point give maxima or larger values. For \(-1\le a\le0\), \(1-3a\ge(1+a)^{3/2}\), whereas for \(0\le a\le1\) the inequality reverses. Therefore
\[
\min_{x\in[-1,1]}g_a(x)=
\begin{cases}3a-1,&-1\le a\le0,\\ -(1+a)^{3/2},&0\le a\le1.\end{cases}
\]
The boundary Schur condition is now exactly
\[
1-a^2-8t^2-2tH(a)\ge0,
\qquad
H(a)=\begin{cases}1-3a,&a\le0,\\(1+a)^{3/2},&a\ge0.\end{cases}
\]
This expression strictly decreases in \(t\ge0\) (apart from its initial derivative when \(H=0\), which does not occur here). Substitution and factorization give its unique nonnegative root
\[
t=B(a)=\begin{cases}(1+a)/4,&a\le0,\\(1-a)\sqrt{1+a}/4,&a\ge0.\end{cases}
\]
In either branch \(0\le B(a)\le1/4\), so the \(|b|<1\) needed for the converse follows automatically. Hence the classification is necessary and sufficient, including all coefficient endpoints.

Finally \(B\) is continuous at zero, affine on \([-1,0]\), and for \(a>0\),
\[
B'(a)=-\frac{1+3a}{8\sqrt{1+a}},\qquad
B''(a)=-\frac{5+3a}{16(1+a)^{3/2}}<0.
\]
The right derivative at zero is \(-1/8\), below the left derivative \(1/4\). Therefore \(B\) is concave on \([-1,1]\), and its symmetric hypograph \(|b|\le B(a)\) is convex, giving the interpolation assertion.

## Verification
The Cayley rational-function identity follows by expanding the displayed numerator and denominator. The minimizer of \(g_a\) follows by differentiating \(g_a'(x)=12x^2-3(1+a)\) and comparing the exact candidate values. The sharp roots satisfy \(1-a^2-8B(a)^2-2B(a)H(a)=0\) identically on each branch. A standalone standard-library script `check_region.py` verifies these formulas on representative rational and irrational parameter values, checks boundary angles numerically as a sanity test, and checks sample coefficient-body convex combinations. The proof does not depend on finite sampling.

## Relationship to prior work
Guo and Hu (2026, arXiv:2609.04279) recently disproved Pommerenke's universal convex-interpolation assertion for the full exterior-univalent class \(\Sigma\) by mixing distinct infinite-series examples with complex parameters. Their work establishes the exterior curvature criterion used here and identifies the natural contrasting question of what finite coefficient subfamilies remain closed under mixing. Its explicit proof does not state an exact real two-coefficient Laurent body or the present all-parameter rigidity. The classical criterion itself is not the solved coefficient classification: here the sharp boundary, phase transition and parameter-space convexity are derived by a separate global cubic minimization.

## Limitations
Only real coefficients with no Laurent terms below \(z^{-2}\) are classified. There is no conclusion that all complex-coefficient quadratic Laurent maps, nor all exterior convex mappings, are closed under convex interpolation. A complete literature search cannot rule out an unindexed prior equivalent coefficient-region calculation; this remains a residual originality risk. The auxiliary finite-parameter script is not a proof of the universal assertions.

## References
Yuankai Guo and Xiaozhe Hu, *A Counterexample to a Problem of Pommerenke on Convex Functions in the Class \(\Sigma\)*, arXiv:2609.04279, first submitted 2026-09-03, Section 1 (exterior-convexity criterion), Sections 2–3 (counterexample).

Ch. Pommerenke, 1962 results on convex exterior functions and their convex combinations, as cited in Guo–Hu, arXiv:2609.04279. The cited classical theorem is used only for comparison; the new classification follows directly from the curvature criterion.
