# Sharp two-data weighted-variation modulus of maximal averaging on stars

## Finding

**Theorem.** Let \(S_m\) be the unit-edge star with center \(o\), leaves \(v_1,\ldots,v_m\), and \(m\ge1\). Let \(w_1,\ldots,w_m>0\), \(W=\sum_{i=1}^m w_i\), and \(w_*=\min_i w_i\). On nonnegative real vertex data, let \(M\) be the centered Hardy–Littlewood maximal operator formed from uniform counting-measure averages over graph-distance balls. Set
\[
 V_w(f)=\sum_{i=1}^{m}w_i|f(v_i)-f(o)|.
\]
The exact two-input seminorm Lipschitz constant is
\[
 K_m(w)=\sup_{\substack{f,h\ge0\\ V_w(f-h)>0}}
 \frac{V_w(Mf-Mh)}{V_w(f-h)}
 =\begin{cases}
 \frac12,&m=1,\\[3pt]
 1+\dfrac{W-w_*}{(m+1)w_*},&m\ge2.
 \end{cases}
\]
The supremum is attained by two strictly positive signals. In particular, for \(m\ge2\) and uniform variation weights, \(K_m=2m/(m+1)\); every choice of positive weights is expansive. Among weights with any fixed total \(W\), equal weights are the unique minimizers of \(K_m(w)\). For fixed \(m\ge2\), the constant diverges when one weight tends to zero and all other weights stay bounded below.

**Domain boundary.** The nonnegativity restriction is essential for the conventional maximal operator defined using averages of absolute values. On unrestricted signed data, no finite constant in this *seminorm* inequality exists even on a three-vertex star.

## Assumptions and scope

The unit-edge graph-distance balls around the center are its singleton and all \(m+1\) vertices. Around leaf \(v_i\), they are its singleton, the pair \(\{o,v_i\}\), and all vertices (duplicates cause no difficulty). Input values are real and nonnegative, while the variation weights \(w_i\) are arbitrary positive reals and do not change averaging weights. The stated quotient ranges over *all pairs* of nonnegative vertex signals whose difference has positive variation, with no normalization on their common baseline. When their difference has zero variation, translation covariance on the nonnegative cone makes the output difference have zero variation as well.

For the interval between two positive inputs, every ball average remains positive and is affine. Piecewise affine breakpoints therefore suffice for the global operator estimate.

## Proof

Write \(c=f(o)\), \(g_i=f(v_i)-c\), \(N=m+1\), and \(\mu=N^{-1}\sum_{j=1}^m g_j\). The exact balls give
\[
 (Mf)(o)=c+\max\{0,\mu\},\qquad
 (Mf)(v_i)=c+\max\{g_i,g_i/2,\mu\}.
\]
Consequently, the output edge-gradient vector is the globally defined continuous piecewise-affine map
\[
 F_i(g)=\max\{g_i,g_i/2,\mu\}-\max\{0,\mu\}.
\]
Every real \(g\in\mathbb R^m\) is realized by a *strictly positive* signal after choosing a sufficiently large common baseline \(c\). Moreover, \(V_w(f-h)=\|g(f)-g(h)\|_{1,w}\) and \(V_w(Mf-Mh)=\|F(g(f))-F(g(h))\|_{1,w}\), where \(\|z\|_{1,w}=\sum_iw_i|z_i|\). It suffices to determine the weighted \(\ell^1\) Lipschitz constant of \(F\).

Fix a full-dimensional affine cell and a column index \(j\). The derivative of a leaf's selected term with respect to \(g_j\) belongs to \(\{1,1/2,1/N\}\) for its own leaf and to \(\{0,1/N\}\) for any other leaf. If the center selects zero, the absolute weighted column sum is at most
\[
 w_j+\frac{1}{N}\sum_{i\ne j}w_i.
\]
If instead the center selects \(\mu\), the derivative of each output-gradient coordinate subtracts \(1/N\). Because \(N\ge2\), the absolute value of the own-coordinate derivative is at most \(1-1/N\), while each other-coordinate derivative has magnitude at most \(1/N\). Its weighted column sum is therefore at most
\[
 w_j\left(1-\frac1N\right)+\frac1N\sum_{i\ne j}w_i,
\]
which is smaller. The induced operator norm on weighted \(\ell^1\) is the largest weighted column sum divided by \(w_j\). Hence every affine cell has norm at most
\[
 1+\max_j\frac{W-w_j}{Nw_j}=1+\frac{W-w_*}{Nw_*}.
\]
A segment crosses only finitely many cells (or can be handled by a limiting parallel segment if it lies on a boundary). Integrating affine derivatives along the segment gives this bound globally.

For sharpness when \(m\ge2\), choose a leaf \(v_j\) having \(w_j=w_*\). Take a strictly positive base signal with \(c=2\), with every other leaf at value \(1\), and with \(f(v_j)=2+m-3/2\). Its edge gradient satisfies \(g_j=m-3/2>0\), \(g_i=-1\) otherwise, and \(\mu=-1/(2N)\). Thus the center strictly selects \(0\), leaf \(v_j\) strictly selects \(g_j\), and all other leaves strictly select \(\mu\), because \(-1/2<\mu<0\). Increase only \(f(v_j)\) by any \(0<t<1/2\). These strict selections persist, the input edge-gradient difference is \(t\) at leaf \(j\) alone, and the output edge-gradient difference is \(t\) at leaf \(j\) and \(t/N\) at each other leaf. Therefore
\[
 \frac{V_w(Mh-Mf)}{V_w(h-f)}
 =\frac{w_jt+(W-w_j)t/N}{w_jt}
 =1+\frac{W-w_*}{Nw_*},
\]
proving attainment with strictly positive data.

If \(m=1\), the two possible ball averages show directly that \((Mf)(v_1)-(Mf)(o)=(f(v_1)-f(o))/2\) for every nonnegative \(f\); the sharp two-input factor is \(1/2\). For \(m\ge2\), the expression for \(K_m(w)\) strictly decreases as \(w_*\) increases with fixed \(W\), and \(w_*\le W/m\), with equality exactly for equal weights. This proves the minimization and rigidity statement. Taking \(w_*\downarrow0\) proves divergence.

For signed-data failure, take \(m\ge2\), \(f(o)=1\), \(f(v_i)=0\), and \(h=f-2\) at every vertex. Then \(f-h\) is constant and has zero variation, while the conventional absolute-value maximal outputs satisfy \((Mf)(o)=1\), \((Mf)(v_i)=1/2\), \((Mh)(o)=2-1/N\), and \((Mh)(v_i)=2\). Their difference has nonzero variation. Arbitrarily small perturbations of \(h\) produce strictly positive denominators tending to zero but numerators bounded away from zero. Thus unrestricted signed data have infinite seminorm Lipschitz constant.

## Verification

Run `python verify.py` using only the Python standard library. The standalone checker performs exact rational arithmetic on the maximal averages, verifies a formal derivative-column upper bound for every combination of active selections through seven leaves (including infeasible combinations, a stronger finite check), tests explicitly attaining pairs with unequal variation weights, checks thousands of arbitrary positive-input secants, and evaluates signed-data obstructions. In the checked execution it passed 127,926 exact selector-column tests, 20 attaining-pair tests, 5,000 exact-rational random-secant tests, and seven signed-input obstructions.

These finite checks are reproducibility diagnostics rather than an infinite proof. The global bound follows from the derivative estimates above, and sharpness follows from the explicit open affine cell and pair.

## Relationship to prior work

Soria and Tradacete introduced the finite-graph centered maximal operator and studied sharp one-input \(\ell^p\) mapping norms, including stars. González-Riquelme and Madrid subsequently determined the classical *one-input* \(1\)-variation sharp star constant \(m/(m+1)\). The present two-data equal-weight modulus is \(2m/(m+1)\) for \(m\ge2\): individual variation contraction therefore does not imply variation contraction of differences. Neither a bound for \(V_w(Mf)\) alone nor the pointwise sublinearity \(|Mf-Mh|\le M|f-h|\) controls the variation of \(Mf-Mh\) by the variation of \(f-h\). The independent weighted-edge geometry and explicit best-weight rigidity are additional features of the present result.

The later study of \(2\)-variation and maximal-function \(\ell^p\) norms on stars treats one-input optimization with a different denominator. No implication from its inspected mathematical statements yields this weighted two-data modulus. This originality comparison is limited to the inspected sources and available records; an equivalent formulation elsewhere is not ruled out.

## Limitations

The theorem uses finite unweighted *graph-distance* stars with counting-measure averages; arbitrary positive weights occur only in the variation seminorm. The cone of nonnegative vertex functions is indispensable. No bound is asserted for unrestricted signed functions, directed graphs, general trees, arbitrary vertex sampling masses, \(p\)-variation with \(p\ne1\), or maximal iterates. Novelty outside the literature checked remains subject to independent review.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1, first public 2014-10-22. https://arxiv.org/abs/1410.6204
2. C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146v1, first public 2020-05-06. https://arxiv.org/abs/2005.03146
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630v1, first public 2020-11-05. https://arxiv.org/abs/2011.02630
