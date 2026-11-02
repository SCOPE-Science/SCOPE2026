# Sharp first-overlap law for random widths of regular simplices

## Finding
Let \(\Delta_d\subset\mathbb R^d\) be a regular simplex of unit edge length, with integer \(d\ge2\). For \(U\) uniformly distributed on the unit sphere, let \(W_d\) be the width of \(\Delta_d\) in direction \(U\), i.e. the distance between its two supporting hyperplanes orthogonal to \(U\). Define
\[
c=\frac{\sqrt3}{2},\qquad t_0=\sqrt{\frac23},\qquad N_d=d(d+1),\qquad H_d=d(d+1)(d-1).
\]
Let \(Q_d(t)\) be the relative spherical area of one cap \(\{u:u\cdot a\ge t\}\) for a fixed unit vector \(a\). Let \(J_d(t)\) be the relative area of the intersection of two such caps whose centers make angle \(\pi/3\). Then the **exact upper-width law through the first two overlap regimes** is
\[
\mathbb P(W_d\ge t)=\begin{cases}
N_dQ_d(t),&c\le t\le1,\\
N_dQ_d(t)-H_dJ_d(t),&t_0\le t\le c.
\end{cases}
\]
The terms are explicit one-dimensional integrals: with \(I_x(\alpha,\beta)\) the regularized incomplete beta function,
\[
Q_d(t)=\frac12 I_{1-t^2}\!\left(\frac{d-1}{2},\frac12\right).
\]
For \(d\ge3\), putting \(s=1/2\),
\[
J_d(t)=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}
\int_{t/c}^{1}(1-z^2)^{(d-3)/2}
I_{\min\{1,\,((cz-t)/(s\sqrt{1-z^2}))^2\}}
\!\left(\frac12,\frac{d-2}{2}\right)\,dz.
\]
The integrand at \(z=1\) is understood by its limit. For \(d=2\) and \(t_0\le t\le c\),
\[
J_2(t)=\frac{2\arccos(t)-\pi/3}{2\pi}.
\]
The correction is nonzero at every \(t<c\) sufficiently close to \(c\). More precisely, as \(\delta\downarrow0\), for each fixed \(d\ge2\),
\[
\boxed{N_dQ_d(c-\delta)-\mathbb P(W_d\ge c-\delta)
=\frac{4(d^2-1)}{\pi}\left(\frac4{\sqrt3}\right)^{(d-2)/2}
\delta^{d/2}+o(\delta^{d/2}).}
\]
Thus the first departure from a disjoint-cap approximation has the sharp dimension-dependent fractional power \(d/2\), with an explicit nonzero coefficient. For \(d\ge3\), \(t_0\) is the next sharp combinatorial boundary: three cap interiors begin to intersect immediately below it, and therefore the displayed pairwise inclusion-exclusion formula no longer applies unchanged.

In dimension \(3\), the cap terms have an elementary form. For \(t_0\le t\le c\), set
\[
\phi(t)=\arccos\!\left(\frac{t}{\sqrt{3(1-t^2)}}\right),\qquad
\gamma(t)=\arccos\!\left(\frac{1/2-t^2}{1-t^2}\right).
\]
Then
\[
Q_3(t)=\frac{1-t}{2},\qquad
J_3(t)=\frac{2\pi-2\gamma(t)-4t\phi(t)}{4\pi},
\]
so the entire law on \([t_0,1]\) is elementary. This does not assert a complete law below \(t_0\) in dimension \(3\) or higher.

## Assumptions and scope
The result concerns all integers \(d\ge2\), a nondegenerate regular simplex with **unit Euclidean edge length**, and normalized Haar surface measure on \(S^{d-1}\). Boundary directions for which two supporting vertices tie have measure zero. The probability uses the inclusive event \(W_d\ge t\), which is continuous in \(t\); all displayed threshold endpoints are included. The exact two-regime formula concerns only \(t\in[t_0,1]\), not the unexamined lower-width region for \(d\ge3\).

For calculations identify \(\mathbb R^d\) with \(H=\{x\in\mathbb R^{d+1}:\sum_i x_i=0\}\), and use vertices \(v_i=(e_i-\mathbf1/(d+1))/\sqrt2\). The oriented unit edge directions are \(r_{ij}=(e_i-e_j)/\sqrt2\), for \(i\ne j\). Hence
\[
W_d(u)=\max_{i\ne j}\langle u,r_{ij}\rangle.
\]

## Proof
**1. Spherical-cap representation.** There are \(N_d=d(d+1)\) distinct oriented roots \(r_{ij}\). The event \(W_d\ge t\) is exactly the union of the equal spherical caps \(C_{ij}(t)=\{u\in S^{d-1}:\langle u,r_{ij}\rangle\ge t\}\). Standard integration of one sphere coordinate, whose square has the beta distribution with parameters \((1/2,(d-1)/2)\), yields \(Q_d\).

**2. Root angles and overlap counts.** For distinct oriented roots, the inner product is one of \(-1,-1/2,0,1/2\), and each root has exactly \(2(d-1)\) other roots at inner product \(1/2\). Therefore the number of unordered \(\pi/3\)-separated pairs is \(H_d=N_d(d-1)\). Two equal caps centered at angle \(\theta\) overlap with positive surface measure precisely if \(2\arccos t>\theta\). For \(t>t_0>1/\sqrt2\), only the pairs with \(\theta=\pi/3\) can overlap, and none overlap for \(t\ge c\).

**3. No triple overlaps above \(t_0\).** For any three distinct oriented roots \(a,b,f\), pairwise inner products are at most \(1/2\), so \(\|a+b+f\|^2\le6\). Any point in their three caps satisfies
\[
3t\le\langle u,a+b+f\rangle\le\sqrt6,
\]
which requires \(t\le t_0\). At equality there are at most isolated maximizing directions, hence their spherical measure is zero. This proves that inclusion-exclusion stops after pairs on \([t_0,c]\). When \(d\ge3\), three roots \(r_{ij},r_{ik},r_{i\ell}\) with distinct \(j,k,\ell\) have all mutual inner products \(1/2\). At the unit vector proportional to their sum, all three projections equal \(t_0\), giving positive triple intersections for every \(t<t_0\) close enough. This proves the sharp next boundary.

**4. Exact pair-lens integral.** For a pair \(a,b\) at angle \(\pi/3\), write \(a=cp+se\), \(b=cp-se\) for orthogonal unit vectors \(p,e\), with \(c=\sqrt3/2\) and \(s=1/2\). Set \(z=u\cdot p\), \(x=u\cdot e\). Both cap inequalities are equivalent to \(cz-s|x|\ge t\). The density of \(z\) is
\[
\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}(1-z^2)^{(d-3)/2},\qquad -1<z<1.
\]
Conditional on \(z\), the normalized variable \(x/\sqrt{1-z^2}\) is a first coordinate of a uniform point on \(S^{d-2}\). Its squared absolute value has beta parameters \((1/2,(d-2)/2)\) for \(d\ge3\). Conditioning proves the stated integral. On \(S^1\), the lens is an interval intersection of angular length \(2\arccos t-\pi/3\), proving the \(d=2\) expression. In \(d=3\), spherical-lens Gauss–Bonnet gives area \(2\pi-2\gamma-4t\phi\), proving the elementary specialization.

**5. Sharp first-overlap expansion.** Let \(t=c-\delta\) with \(\delta>0\). The caps touch at \(u=p\) when \(\delta=0\). Use local coordinates \(u=(\sqrt{1-x^2-\|y\|^2},x,y)\), with \(x\in\mathbb R\), \(y\in\mathbb R^{d-2}\), relative to the orthonormal decomposition \(p,e,p^\perp\cap e^\perp\). The lens condition is
\[
c\sqrt{1-x^2-\|y\|^2}-s|x|\ge c-\delta.
\]
Scale \(x=\delta X\), \(y=\sqrt\delta Y\). The spherical area density tends uniformly on the shrinking lens to Euclidean measure and the rescaled domains converge to \(s|X|+(c/2)\|Y\|^2\le1\). Dominated convergence then gives
\[
\operatorname{area}(C_a\cap C_b)=
\frac{8\kappa_{d-2}}{d}\left(\frac4{\sqrt3}\right)^{(d-2)/2}\delta^{d/2}+o(\delta^{d/2}),
\]
where \(\kappa_k\) is the volume of the unit \(k\)-ball and \(\kappa_0=1\). Dividing by \(\operatorname{area}(S^{d-1})=d\kappa_d\), multiplying by \(H_d\), and using \(\kappa_{d-2}/\kappa_d=d/(2\pi)\) yields precisely the coefficient in the theorem. The two-dimensional case follows from the same scaled interval calculation.

## Verification
An executable independent checker is supplied as `verify.py` (requires Python 3 with NumPy and SciPy). It generates every oriented type-\(A_d\) root for \(2\le d\le8\), checks all pairwise inner-product multiplicities, numerically integrates the lens by conditioning, checks the sharp coefficient near the transition, and compares the claimed distribution with independent Haar-direction Monte Carlo samples in dimensions \(2,3,4,5\). It also checks the three-dimensional Gauss–Bonnet expression against the independently integrated lens formula.

The verifier passed 66 grouped assertions and comparisons in the recorded execution, including 360,000 sample directions per tested dimension. These computations are checks, not substitutes for the dimension-uniform proof above.

## Relationship to prior work
Finch, *Width Distributions for Convex Regular Polyhedra* (first publicly posted 2011), analyzes the tetrahedral and cubic mean and mean-square widths and explicitly leaves the tetrahedral density unknown. Finch, *Mean Width of a Regular Simplex* (first publicly posted 2011), develops normal-order-statistic integral formulas for moments. Kabluchko, Litvak and Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables* (first publicly posted 2015), establish all-moment identities and high-dimensional limit laws. The result here is not the known Gaussian-range representation or a moment evaluation: it resolves a specific **finite-dimensional distribution interval** with exact geometric thresholds, root-cap multiplicities, and a sharp nonanalytic overlap coefficient.

The previously published first-multiple-overlap analysis for **simplex-centered** spherical caps concerns a different cap-center configuration; the centers here are the full oriented type-\(A_d\) root configuration. Related random-width calculations for cubes and cross-polytopes similarly do not imply the type-\(A_d\) pair multiplicity or its coefficient. Affentranger and Schneider's *Random Projections of Regular Simplices* (1992) treats asymptotic expected face counts of higher-dimensional projections, not this tail law.

## Limitations
This establishes no full random-width density below \(t_0\) for \(d\ge3\). The next transition involves triple cap overlaps and requires additional analysis. The exact coefficient concerns fixed dimension as \(\delta\downarrow0\), not an interchange of limits as \(d\to\infty\). A published but unindexed earlier calculation of the same cap overlap or tetrahedral width may exist; the novelty assessment is based on the inspected literature and research-record comparisons, not a universal priority certificate.

## References
- Steven R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, initial public submission 2011-10-04; https://arxiv.org/abs/1110.0671.
- Steven R. Finch, *Mean Width of a Regular Simplex*, arXiv:1111.4976, initial public submission 2011-11-21; https://arxiv.org/abs/1111.4976.
- Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479, initial public submission 2015-11-26; https://arxiv.org/abs/1511.08479.
- F. Affentranger and R. Schneider, *Random Projections of Regular Simplices*, Discrete & Computational Geometry 7 (1992), 219–226; DOI:10.1007/BF02187839. Abstract and bibliographic record consulted; full text not inspected.
