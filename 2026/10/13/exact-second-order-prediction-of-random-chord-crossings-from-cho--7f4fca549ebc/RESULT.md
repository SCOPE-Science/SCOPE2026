# Exact second-order prediction of random chord crossings from chord lengths

## Finding

Let \(n\ge 2\) and choose \(2n\) independent points uniformly on the circumference of a unit circle. Pair the points in their sampling order into \(n\) independent chords. Let \(L_i\) be the Euclidean length of chord \(i\), and \(X_n\) the number of unordered pairs of distinct chords crossing strictly inside the circle. Define the *short-arc fractions*
\[
r_i=\frac{\arcsin(L_i/2)}{\pi}\in(0,1/2),\qquad 1\le i\le n.
\]
Conditional on the entire length vector, the crossing count obeys the **exact second-order conditional law**
\[
\boxed{\mathbb E[X_n\mid L_1,\ldots,L_n]=\sum_{i<j}2\min(r_i,r_j)},
\]
\[
\boxed{\operatorname{Var}(X_n\mid L_1,\ldots,L_n)=\sum_{i<j}2\min(r_i,r_j)\bigl(1-2\min(r_i,r_j)\bigr)}.
\]
The first boxed expression is the unique mean-square-optimal predictor from the lengths. Exactly,
\[
\operatorname{Var}(X_n)=\frac{n(n-1)(n+3)}{45},\qquad
\mathbb E\!\left[(X_n-\mathbb E[X_n\mid L_1,\ldots,L_n])^2\right]=\frac{n(n-1)}{12}.
\]
Hence the proportion of crossing-count variance explained by all chord lengths equals
\[
\boxed{\frac{\operatorname{Var}(\mathbb E[X_n\mid L_1,\ldots,L_n])}{\operatorname{Var}(X_n)}=\frac{4n-3}{4n+12}=1-\frac{15}{4(n+3)}}.
\]
This fraction tends to one as \(n\to\infty\), while the irreducible mean-square error remains of order \(n^2\), compared with the total variance of order \(n^3\).

## Assumptions and scope

Each chord is constructed by joining two independent points chosen uniformly by arc length on the same circle. The chords are independent. Equivalently, independent uniform circular endpoints may be paired by an independent uniformly random perfect matching; the resulting unlabeled configuration has the same law. The circle has radius one, \(n\ge2\), and events of endpoint coincidences or triple intersections have probability zero. The short-arc fraction is the length of the shorter of the two circular arcs between a chord's endpoints, divided by the full circumference. It is uniquely determined by the Euclidean chord length. The theorem does *not* concern chords sampled by uniform midpoint or invariant-line measure, two different random-chord models.

## Proof

**1. Conditional geometry.** For one independently sampled chord let \(U\in(0,1)\) denote the clockwise fractional separation of its two labeled endpoints. Then \(U\) is uniform, \(R=\min(U,1-U)\in(0,1/2)\) has density \(2\), and its Euclidean length is \(2\sin(\pi R)\). Conditional on \(R=r\), the chord can be represented by the endpoints of an arc \([\Theta,\Theta+r]\) modulo one, where \(\Theta\) is uniform on the circle. These rotations remain mutually independent for different chords when all lengths are fixed.

Fix two short-arc fractions \(r,s\in(0,1/2)\), rotate the first arc to \([0,r]\), and uniformly rotate the second arc of length \(s\). The underlying chords cross if and only if exactly one second endpoint lies in \([0,r]\). The set of second-arc starting points producing a crossing is the symmetric difference between \([0,r]\) and its translate by \(-s\). Because both arc lengths are at most one half, that symmetric difference has normalized length \(2\min(r,s)\). Therefore
\[
\Pr\bigl(\text{chords }i,j\text{ cross}\mid r_i,r_j\bigr)=g(r_i,r_j),\qquad g(r,s)=2\min(r,s).
\]

**2. Pairwise conditional decorrelation.** Let \(H_{ij}\) be the indicator that chords \(i\) and \(j\) cross. Conditional on the full length vector, disjoint-edge indicators are independent, since they use different random rotations. If \(H_{ij}\) and \(H_{ik}\) share chord \(i\), condition additionally on that chord's rotation. The remaining two chord rotations are independent, and by rotational symmetry each conditional crossing probability is the constant \(g(r_i,r_j)\) or \(g(r_i,r_k)\), independent of the shared rotation. Thus such indicators are also **pairwise independent conditional on all lengths**. This does not assert joint independence of the entire crossing-indicator family. Summing the Bernoulli means and variances of the pairwise-independent indicators gives both boxed conditional identities.

**3. Exact unconditional moments.** For iid short-arc fractions \(R,S\) of density \(2\) on \((0,1/2)\), direct integrations give
\[
\mathbb E g(R,S)=\frac13,\quad \mathbb E g(R,S)^2=\frac16,\quad
q(r):=\mathbb E_S g(r,S)=2r(1-r),\quad
\operatorname{Var}(q(R))=\frac1{45}.
\]
Write \(M_n=\mathbb E[X_n\mid L_1,\ldots,L_n]=\sum_{i<j}g(R_i,R_j)\). The kernel variance is \(1/6-1/9=1/18\). Terms with disjoint index pairs are independent, and two distinct terms sharing exactly one index have covariance \(\operatorname{Var}(q(R))=1/45\). Counting the three shared-edge pairs per triple gives
\[
\operatorname{Var}(M_n)=\binom n2\frac1{18}+6\binom n3\frac1{45}
=\frac{n(n-1)(4n-3)}{180}.
\]
The conditional Bernoulli variance formula from step 2 yields
\[
\mathbb E\operatorname{Var}(X_n\mid L_1,\ldots,L_n)
=\binom n2\mathbb E\bigl[g(R,S)(1-g(R,S))\bigr]
=\binom n2\left(\frac13-\frac16\right)
=\frac{n(n-1)}{12}.
\]
By the law of total variance,
\[
\operatorname{Var}(X_n)=\operatorname{Var}(M_n)+\mathbb E\operatorname{Var}(X_n\mid L_1,\ldots,L_n)
=\frac{n(n-1)(n+3)}{45}.
\]
The conditional mean is the orthogonal projection of \(X_n\) onto square-integrable functions of all lengths; its residual mean-square risk is the displayed expectation of conditional variance. Dividing the two variance components proves the exact explained fraction and its limit. All integrals are bounded and all formulas hold for each finite integer \(n\ge2\).

## Verification

The standalone `verify.py` checks the exact crossing-kernel moments by symbolic integration and confirms, symbolically for an arbitrary integer parameter, the variance-component formulas and the explained fraction. Its separate continuous-rotation experiment tests conditional mean and variance at three fixed chord-length profiles, using 140,000 configurations per profile. Two further simulations, with 90,000 configurations each at three and six independent chords, compare the actual geometric crossing count and length-based predictor to the exact unconditional moments. Run `python verify.py` with Python 3, SymPy, and NumPy. The deterministic output ends with `VERIFY_OK symbolic=8 conditional_samples=3 unconditional_samples=2`. Sampling verifies illustrative cases but does not establish the infinite statements; the analytic proof above does.

## Relationship to prior work

Flajolet and Noy (2000), *Analytic Combinatorics of Chord Diagrams*, Section 2, already give the exact marginal mean \(n(n-1)/6\), marginal variance \(n(n-1)(n+3)/45\), and asymptotic Gaussian law of crossing count. None of those marginal identities entails the conditional prediction variance without a joint geometric model. Acan (arXiv:1501.01489v1, publicly submitted January 7, 2015) analyzes random chord diagrams and crossing degrees; its notion of chord “length” is an integer number of intervening *endpoint labels*, not Euclidean chord length. Bortolotto and Souza (arXiv:2504.12866v1) analyze the positions of intersections of random chord pairs, and Bortolotto and Ramos (2025, DOI 10.1112/mtk.70024) analyze extremal pairwise intersection probabilities. The present conditional second-order law concerns the full \(n\)-chord crossing count given all Euclidean chord lengths. No novelty is claimed for the marginal crossing-count moments, the fact that two random chords intersect with probability \(1/3\), or the standard law-of-total-variance principle.

## Limitations

The result uses independent endpoints that are uniform on the circumference and a common known unit-circle radius. It does not extend as stated to other Bertrand chord constructions, nonuniform endpoint laws, or dependent chords. Pairwise conditional independence of crossing indicators does **not** imply their mutual conditional independence or determine the complete conditional distribution of the crossing count. The proof determines second moments, not an error tail bound, central limit theorem conditional on lengths, or a novel joint distribution. A broader historical integral-geometric identity or an unpublished calculation might imply the conditional kernel; external independent scientific audit has not been performed. The numerical checks are finite corroboration only.

## References

1. P. Flajolet and M. Noy, “Analytic Combinatorics of Chord Diagrams,” INRIA Research Report RR-3914 (March 2000), Section 2. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
2. H. Acan, “On a uniformly random chord diagram and its intersection graph,” arXiv:1501.01489v1 (first posted 2015-01-07), Sections 1, 2, 4, and 6. https://arxiv.org/html/1501.01489v1
3. C. Bortolotto and V. Souza, “Intersections of random chords of a circle,” arXiv:2504.12866v1 (first posted 2025-04-17). https://arxiv.org/pdf/2504.12866
4. C. Bortolotto and J. P. G. Ramos, “On extremal problems associated with random chords on a circle,” *Mathematika* 71 (2025), e70024. https://doi.org/10.1112/mtk.70024
