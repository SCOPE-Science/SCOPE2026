# Sharp antagonistic symmetry breaking in a three-colour two-urn logistic model

## Finding

Consider the logistic three-colour interacting-urn model of Pires and Rosales on the complete graph with two vertices. Let its interaction coefficient be \(\alpha=-2a\), where \(a>0\). Write \(p_i\) for the proportion of colour \(i\) in the first urn and \(z_i=2p_i-1\) for \(i=1,2,3\). The fixed-point equations are
\[
 z_i=\tanh\!\left(-a\sum_{j\ne i}z_j\right),\qquad i=1,2,3.
\]

**Theorem.** If \(0<a\le1\), the origin is the only fixed point in \((-1,1)^3\). If \(a>1\), at least thirteen distinct fixed points exist: the origin; six permutations of \((r,0,-r)\), where \(r\in(0,1)\) is the unique solution of \(\operatorname{artanh}r=ar\); and six permutations of \((-b,-b,v)\) and \((b,b,-v)\), where \(b\in(0,1)\) uniquely solves
\[
 \tanh(2ab)-b-\frac{\operatorname{artanh}b}{a}=0,
 \qquad v=\tanh(2ab)>b.
\]
Each of the six \((r,0,-r)\) equilibria is linearly asymptotically stable for the stochastic-approximation ordinary differential equation
\[
 \dot z_i=-z_i+\tanh\!\left(-a\sum_{j\ne i}z_j\right).
\]
The origin is linearly asymptotically stable for \(0<a<1\) and linearly unstable for \(a>1\). At \(a=1\), the origin is the unique fixed point and has two zero linearization eigenvalues. These statements concern the ODE, not stability of iteration of the fixed-point map.

## Assumptions and scope

There are exactly two urn vertices connected by one edge and three colours, each colour having unit addition per time step and the same total initial count, as in the cited model. The response is \(\varphi(t)=(1+e^{-t})^{-1}\) with common antagonistic coupling \(\alpha=-2a<0\). Positive initial urn masses ensure proportions belong to the interior. Fixed points of the limiting drift, not individual random trajectories, are analyzed. All parameter statements quantify over every real \(a>0\), with no large-coupling cutoff.

For two urns, the probability assigned to the first urn for colour \(i\) is \(\varphi(\alpha\sum_{j\ne i}(p_j-(1-p_j)))\). Consequently \(2\varphi(t)-1=\tanh(t/2)\) gives exactly the displayed equations. This normalization fixes the transition at \(\alpha=-2\).

## Proof

**Uniqueness up to the threshold.** Every fixed point is interior because \(|\tanh t|<1\) for finite \(t\). Put \(S=z_1+z_2+z_3\). Applying \(\operatorname{artanh}\) gives
\[
 g_a(z_i):=\operatorname{artanh}(z_i)-az_i=-aS.
\]
For \(0<a\le1\), \(g_a'(z)=(1-z^2)^{-1}-a\ge0\), with strict increase of \(g_a\) on \((-1,1)\) even at \(a=1\). Therefore all coordinates are equal. A common value \(w\) must satisfy \(w=\tanh(-2aw)\), whose sides have opposite signs unless \(w=0\). Thus the origin is unique.

**Six polarized fixed points.** For \(a>1\), the map \(r\mapsto\operatorname{artanh}(r)/r\) increases strictly from \(1\) to \(+\infty\) on \((0,1)\). Indeed its derivative has the sign of \(r/(1-r^2)-\operatorname{artanh}(r)\), which vanishes at zero and has strictly positive derivative \(2r^2/(1-r^2)^2\). Let its unique value-\(a\) solution be \(r\). Substituting any permutation of \((r,0,-r)\) into the fixed equations verifies it, yielding six distinct points.

**Six additional fixed points.** Define \(H_a(b)=\tanh(2ab)-b-\operatorname{artanh}(b)/a\) for \(0\le b<1\). It has \(H_a(0)=0\), \(H_a'(0)=2a-1-a^{-1}>0\) when \(a>1\), and \(H_a(b)\to-\infty\) as \(b\uparrow1\). Moreover, for \(0<b<1\),
\[
 H_a''(b)=-8a^2\tanh(2ab)\operatorname{sech}^2(2ab)
 -\frac{2b}{a(1-b^2)^2}<0.
\]
Strict concavity gives exactly one positive zero \(b\). With \(v=\tanh(2ab)\), the defining equation yields \(v=b+\operatorname{artanh}(b)/a>b\). Directly, the equations for \((-b,-b,v)\) become \(v=\tanh(2ab)\) and \(\operatorname{artanh}(b)=a(v-b)\), so this vector and its negative solve the system. They each have three distinct coordinate placements, for six solutions. Their two equal nonzero coordinates distinguish them from the polarized permutations and from zero. Hence at least thirteen equilibria exist.

**ODE stability.** The Jacobian of the drift is \(J_{ij}=-\delta_{ij}-a(1-z_i^2)(1-\delta_{ij})\). At zero its eigenvalues are \(-1-2a\) and \(a-1\), the latter twice, proving the stated linear behavior. At \((r,0,-r)\), put \(s=1-r^2\). The antisymmetric outer-coordinate mode has eigenvalue \(as-1\). The remaining two-dimensional invariant mode has trace \(-2-as\) and determinant \(1+as-2a^2s\).

Set \(u=\operatorname{artanh}(r)>0\), so \(r=\tanh u\), \(a=u\coth u\), and \(s=\operatorname{sech}^2u\). Then \(as=2u/\sinh(2u)<1\). Furthermore
\[
 (1+as-2a^2s)\sinh^2u
 =\sinh^2u+u\tanh u-2u^2>0.
\]
For strict positivity use \(\sinh^2u>u^2+u^4/3\) and \(\tanh u\ge u-u^3/3\), both for \(u>0\). The second inequality follows by differentiating \(\tanh u-u+u^3/3\), whose derivative is \(u^2-\tanh^2u\ge0\), and the first follows from the positive-coefficient power series of \(\sinh^2u\). Thus the antisymmetric eigenvalue is negative and the remaining block has negative trace and positive determinant, so all eigenvalues have strictly negative real part. Symmetry gives the same conclusion for all six polarized points.

## Verification

Run `python3 check_equilibria.py` with a standard Python 3 installation. It checks the model drift at thirteen explicitly constructed equilibria for each of ten positive interaction magnitudes above the transition, compares analytic and finite-difference Jacobians, and checks the strict stability inequalities. The numerical bisection and finite-difference checks are finite diagnostic tests only; the theorem's all-parameter claims follow from the preceding analytic inequalities.

## Relationship to prior work

Pires and Rosales, *Multiple colour interacting urns on complete graphs*, arXiv:2212.09397 (first public version 2022-12-19), define the urn and its fixed-point flow. Their Theorem 1 gives stochastic convergence conditional on finitely many fixed points and their corollary gives a small-interaction uniqueness regime. Their worked multistable example uses three vertices, two colours and positive interaction, rather than the present two vertices, three colours and negative interaction. Here the new conclusions concern a sharp antagonistic uniqueness boundary, explicit thirteen-solution lower bound and six ODE-stable polarized equilibria for every supercritical magnitude. The classical Hopfield energy analogy in the source is not a claim of novelty.

## Limitations

The theorem proves **at least** thirteen solutions, not exactly thirteen; other solutions are not excluded. It does not prove all fixed points are finite in number, almost-sure selection of a particular equilibrium, probabilities of attraction basins, or stochastic convergence without the hypotheses of an applicable external theorem. It does not claim stability of direct iteration of the reinforcement map, and the critical point's nonlinear stability is not determined. The result is for three colours, two vertices and the stated logistic response only. Historical novelty has been assessed against accessible primary sources and research records but is not independently certified.

## References

1. B. Pires and R. A. Rosales, *Multiple colour interacting urns on complete graphs*, arXiv:2212.09397, first version posted 2022-12-19. https://arxiv.org/abs/2212.09397 . Full text: https://arxiv.org/html/2212.09397v3 .
2. M. Benaïm, I. Benjamini, J. Chen and Y. Lima, *A generalized Pólya's urn with graph based interactions*, Random Structures & Algorithms 46 (2015), 614–634; preprint https://arxiv.org/abs/1211.1247 .
3. B. Costa and J. Jordan, *Phase transitions in non-linear urns with interacting types*, arXiv:2006.02685. https://arxiv.org/abs/2006.02685 .
