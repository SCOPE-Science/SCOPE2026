# Exact acute-triangle probability for independent uniform perimeter points of an equilateral triangle

## Finding
Let \(P,Q,R\) be three independent points distributed uniformly by arclength on the entire boundary of a nondegenerate equilateral Euclidean triangle. Points on the same side are allowed; collinear triples are not acute triangles. Then
\[
\Pr(\triangle PQR\text{ is acute})
=\frac{17}{3}\log\frac43-\frac43
=0.2968650772267586\ldots .
\]
More precisely, conditional on the samples occupying exactly two distinct sides (two points on one side, the third on a different side),
\[
\Pr(\text{acute}\mid\text{exactly two sides})
=4\log\frac43-\frac56
=0.3173949564737904\ldots .
\]
Together with the previously tabulated one-point-per-side probability \(\frac{27}{2}\log\frac43-\frac72\), this evaluates the full perimeter-sampling problem in closed form, including its degenerate one-side cases.

## Assumptions and scope
The reference triangle has side length \(1\), which loses no generality by similarity, and vertices \(A=(0,0)\), \(B=(1,0)\), \(C=(1/2,\sqrt3/2)\). Each sample independently selects one of the three sides with probability \(1/3\) and then a uniform arclength parameter in \([0,1]\). A triangle is acute exactly when all three of its interior angles are strictly below \(\pi/2\). Vertex and right-angle equality events have measure zero; the all-on-one-side event is collinear with probability \(1/9\).

## Proof
The probabilities of exactly one, two, or three occupied sides are respectively \(1/9\), \(2/3\), and \(2/9\). This follows by counting the \(3^3=27\) equally likely ordered side-label triples: \(3\) use one side, \(18\) use two, and \(6\) use three.

**Exactly two sides.** By symmetry and relabeling, condition on two points on \(AB\) at \(X=(x,0)\), \(Y=(y,0)\), with \(0<x<y<1\), and a third point on \(AC\) at \(Z=(t/2,\sqrt3t/2)\), \(0<t<1\). The ordered pair \((x,y)\) has density \(2\) over \(0<x<y<1\). Put \(a=t/2\). The angles at \(X\) and \(Y\) are acute exactly when \(x<a<y\); the angle at \(Z\) is acute exactly when
\[
(a-x)(y-a)<\frac{3t^2}{4}=3a^2.
\]
At fixed \(t\), write \(u=a-x\) and \(v=y-a\). Thus the favorable conditional area is
\[
f(t)=2\int_0^{t/2}\int_0^{1-t/2}
\mathbf1_{\{uv<3t^2/4\}}\,dv\,du.
\]
The product restriction first becomes active at \(t=1/2\). Direct one-variable integration, using the breakpoint \(u=(3t^2/4)/(1-t/2)\), gives the exact continuous profile
\[
f(t)=\begin{cases}
\displaystyle \frac{3t^2}{2}\left(1+\log\frac{2-t}{3t}\right),&0<t\le\frac12,\\[3pt]
\displaystyle t\left(1-\frac t2\right),&\frac12\le t<1.
\end{cases}
\]
Consequently
\[
\int_0^1 f(t)\,dt=\log\frac{256}{81}-\frac56
=4\log\frac43-\frac56.
\]
All orientations of the two occupied sides have the same conditional probability.

**Three distinct sides.** To independently recover the tabulated component, let \(X=(x,0)\in AB\), \(Y=(1-y/2,\sqrt3y/2)\in BC\), and \(Z=(z/2,\sqrt3z/2)\in AC\), where \(x,y,z\) are independent uniform parameters in \([0,1]\). The angle at \(X\) is obtuse precisely when
\[
(X-Y)\cdot(X-Z)=x^2-x+\frac{xy}{2}+\frac{z(1+y-x)}{2}<0.
\]
For fixed \(x,y\), its \(z\)-probability therefore equals
\[
\min\left\{1,\max\left\{0,\frac{x(2-2x-y)}{1+y-x}\right\}\right\}.
\]
Integrating over \(y\in[0,1]\) yields
\[
q(x)=\begin{cases}
\displaystyle x\left[3(1-x)\log\frac{2-x}{1-x}-1\right],&0<x\le1/2,\\[3pt]
\displaystyle(1-x)\left[3x\log\frac{1+x}{x}-1\right],&1/2\le x<1.
\end{cases}
\]
For the second branch, the clipping transition is \(y=(2x-1)(1-x)/(1+x)\), and the positivity endpoint is \(y=2(1-x)\). Since \(q(x)=q(1-x)\), the probability that angle \(X\) is obtuse is
\[
q=2\int_0^{1/2}x\left[3(1-x)\log\frac{2-x}{1-x}-1\right]dx
=\frac32-\frac92\log\frac43.
\]
At most one angle of a nondegenerate triangle can be obtuse, and the three sampled sides are symmetric. Thus the conditional probability of an acute triangle is
\[
1-3q=\frac{27}{2}\log\frac43-\frac72.
\]
Right-angle equalities have three-dimensional Lebesgue measure zero.

**Mixture.** Combining the two nondegenerate occupancy patterns gives
\[
\Pr(\text{acute})
=\frac23\left(4\log\frac43-\frac56\right)
+\frac29\left(\frac{27}{2}\log\frac43-\frac72\right)
=\frac{17}{3}\log\frac43-\frac43.
\]
The omitted one-side probability \(1/9\) is exactly the degenerate mass.

## Verification
All of the displayed one-dimensional definite integrals were recomputed symbolically, including each branch endpoint and the mixture identity. The accompanying self-contained `verify_boundary.py` recomputes the conditional integrals by numerical quadrature, checks the exact expressions, and carries out a deterministic pseudo-random three-point simulation as a supplementary independent normalization check. These finite checks support the analytic proof; they are not a substitute for its all-parameter integral identities.

## Relationship to prior work
A question posted September 17, 2024 asks exactly for the probability under independent uniform sampling on the perimeter and provides a triple-integral representation with an approximate numerical value of \(0.27\); it does not evaluate the integral in closed form. The result here supplies a closed evaluation, an explicit exact two-side conditional probability, and a separate derivation of the three-side contribution.

The three-distinct-side conditional probability \(\frac{27}{2}\log(4/3)-\frac72\) is already tabulated in the Online Encyclopedia of Integer Sequences, entry A394836 (published 2026), which attributes an associated three-side problem to Enoch Beery Seitz (1878). That **known component is not claimed as new**. The other known models of random triangles examined in the comparisons—including Finch's triangles made from random tangents to a circle and exact pairwise boundary-distance moments—have different sampling constructions or events and do not provide the evaluated unconditional perimeter law.

## Limitations
This theorem treats only equilateral Euclidean triangles with the normalized arclength sampling law and acute/nonacute classification. It does not cover general triangle shapes, other polygon boundaries, or the full distribution of the triangle angles. The full problem's 2024 triple-integral representation was already available, so novelty is claimed only for the explicit elementary evaluation and the two-edge decomposition; unindexed earlier closed evaluations remain a bibliographic risk. The date of the nineteenth-century source is established at year resolution only and is not assigned an invented calendar day.

## References
1. Jerry Leung, “Three points on the sides of an equilateral triangle,” September 17, 2024 (edited September 28, 2024), https://puzzling.stackexchange.com/questions/128400/three-points-on-the-sides-of-an-equilateral-triangle .
2. Online Encyclopedia of Integer Sequences, A394836, “Decimal expansion of the probability that three points selected uniformly and independently at random one on each of the three sides of an equilateral triangle form an acute triangle,” https://oeis.org/A394836 .
3. Enoch Beery Seitz, Problem 20, *The Mathematical Visitor*, vol. 1 no. 2 (1878), pp. 40–41; cited in OEIS A394836.
4. Steven R. Finch, *Three Random Tangents to a Circle*, arXiv:1101.3931v1, first posted January 20, 2011, https://arxiv.org/abs/1101.3931 .
