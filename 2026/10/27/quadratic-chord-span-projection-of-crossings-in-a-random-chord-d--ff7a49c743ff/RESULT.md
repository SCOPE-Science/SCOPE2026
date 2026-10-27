# Quadratic chord-span projection of crossings in a random chord diagram

## Finding
For every integer \(n\ge2\), let a perfect matching of \(2n\) cyclically ordered labeled points be chosen uniformly. Let \(I_e\) indicate that a potential chord \(e\) is present, \(X\) be the number of crossing pairs of present chords, and \(d(e)\in\{1,\ldots,n\}\) the shorter cyclic endpoint distance. Define the additive quadratic span statistic
\[
Q=\sum_e (n-d(e))^2 I_e.
\]
Then the orthogonal projection of \(X\) in \(L^2\) onto the entire affine space of additive chord statistics \(c+\sum_e a_eI_e\) is
\[
\widehat X=\frac{n(n-1)}6-\frac{Q-n^2(n-1)/3}{2(n-1)}.
\]
Writing \(R=X-\widehat X\), **every individual potential-chord indicator** satisfies \(\operatorname{Cov}(R,I_e)=0\). The variance decomposition is exact:
\[
\operatorname{Var}(\widehat X)=\frac{n^2(2n+1)}{90},\qquad
\operatorname{Var}(R)=\frac{n(n-2)}{30},\qquad
\operatorname{Var}(X)=\frac{n(n-1)(n+3)}{45}.
\]
Consequently, among all predictors linear in arbitrary chord-presence indicators, the squared population correlation with \(X\) is maximized by \(Q\), and its optimal explained-variance fraction is
\[
\mathcal R_n^2=\frac{n(2n+1)}{2(n-1)(n+3)}\ge\frac67.
\]
Equality holds exactly at \(n=4\); moreover \(\mathcal R_n^2\to1\). Thus all but \(O(n^2)\) of the \(\Theta(n^3)\) crossing variance is captured by one additive quadratic span statistic, even though \(X\) itself is a pair-interaction statistic.

For each \(1\le d\le n\), let \(L_d\) count present chords of cyclic endpoint distance \(d\). With \(m_d=2n\) for \(d<n\) and \(m_n=n\), the **entire crossing/length-count covariance vector** is
\[
\operatorname{Cov}(X,L_d)=
\frac{m_d\bigl(n(n-1)-3(n-d)^2\bigr)}{3(2n-1)(2n-3)}.
\]
Its signs change exactly at the span threshold \(d=n-\sqrt{n(n-1)/3}\). Exact zero covariance occurs at precisely the positive Pell solutions \((2n-1)^2-12(n-d)^2=1\), giving infinitely many pairs starting with \((n,d)=(4,2),(49,21),(676,286)\).

## Assumptions and scope
The sample space is the \((2n-1)!!\) perfect matchings of the fixed cyclic order \(0,1,\ldots,2n-1\), all equally likely; chords cross when their four endpoints alternate around the circle. Distances are measured in *number of cyclic boundary steps*, rather than Euclidean chord length or the number of intermediate vertices. Every sum over \(e\) includes each unordered potential endpoint pair once. All assertions hold for every integer \(n\ge2\), including the degenerate exact-prediction case \(n=2\).

An additive chord statistic is any random variable \(c+\sum_e a_eI_e\) with fixed real coefficients. Optimality means least population mean-square error within that finite-dimensional affine class, not an assertion about nonlinear conditional expectation given \(Q\), and not finite-sample estimation from data.

## Proof
**1. Crossing covariance for a prescribed chord.** Fix a potential chord \(e\) of cyclic distance \(d\). Its presence has probability \(p=(2n-1)^{-1}\). Once this chord is fixed, the other \(2n-2\) endpoints form an independent uniform matching. Among the \(n-1\) remaining chords, the expected number of crossing pairs is \((n-1)(n-2)/6\), because any two distinct chords in a uniform matching cross with probability \(1/3\). The prescribed chord separates \(d-1\) endpoints from the remaining \(2n-d-1\); each endpoint in the first group is paired across the separation with probability \((2n-d-1)/(2n-3)\). Therefore
\[
\mathbb E[X\mid I_e=1]
=\frac{(n-1)(n-2)}6+
\frac{(d-1)(2n-d-1)}{2n-3}.
\]
Since \(\mathbb E X=n(n-1)/6\), subtraction gives
\[
\operatorname{Cov}(X,I_e)
=\frac{n(n-1)-3(n-d)^2}{3(2n-1)(2n-3)}.\tag{1}
\]

**2. Covariance of an additive matching statistic with one edge.** Put \(N=2n\), \(w_e=(n-d(e))^2\), and \(\overline w=n(n-1)/3\). Each vertex is incident to exactly two potential chords of each distance below \(n\), and to one of distance \(n\). Hence every vertex has the same total incident weight, \(T=2\sum_{j=1}^{n-1}j^2\), while the full edge-weight sum is \(NT/2\); in particular its mean over all \(\binom N2\) potential edges is \(\overline w\), and \(\mathbb E Q=n\overline w=n^2(n-1)/3\).

For two different potential edges, their matching indicators have joint probability \(0\) if they share a vertex, and \(q=((N-1)(N-3))^{-1}\) if disjoint. The joint probability for the same edge is \(p=(N-1)^{-1}\). Separating the edge itself, the edges incident to either endpoint, and the disjoint edges yields
\[
\operatorname{Cov}(Q,I_e)
=(p+q)w_e+(q-p^2)\frac{NT}{2}-2qT
=\frac{N-2}{(N-1)(N-3)}(w_e-\overline w).\tag{2}
\]
Equation (1) becomes
\[
\operatorname{Cov}(X,I_e)=
-\frac{w_e-\overline w}{(N-1)(N-3)}
=-\frac{\operatorname{Cov}(Q,I_e)}{N-2}.\tag{3}
\]
Thus \(R=X-\mathbb E X+(Q-\mathbb E Q)/(N-2)\) is centered and orthogonal to every \(I_e\). Since \(\widehat X\) belongs to their affine span, it is the orthogonal projection of \(X\) onto that span, even when the coefficients in an additive predictor depend arbitrarily on the endpoint labels.

**3. Exact variances.** Multiply (2) by \(w_e\) and sum over all potential edges. The first weighted-deviation moment vanishes, so
\[
\operatorname{Var}(Q)=\frac{N-2}{(N-1)(N-3)}
\sum_e(w_e-\overline w)^2.
\]
There are \(2n\) potential chords at distance \(d<n\), and \(n\) at distance \(n\). Consequently
\[
\sum_e w_e=2n\sum_{j=1}^{n-1}j^2,
\qquad\sum_e w_e^2=2n\sum_{j=1}^{n-1}j^4.
\]
The standard square- and fourth-power sums now give
\[
\operatorname{Var}(Q)=\frac{2n^2(n-1)^2(2n+1)}{45},\qquad
\operatorname{Cov}(X,Q)=-\frac{n^2(n-1)(2n+1)}{45}.\tag{4}
\]
The established crossing variance for uniform chord diagrams is \(\operatorname{Var}(X)=n(n-1)(n+3)/45\), stated in Paguyo (2021), Lemma 2.2, attributing it to Flajolet and Noy; it can also be proved by enumerating overlaps among pairs of crossing quadruples. Combining this identity with (4), the Pythagorean theorem for orthogonal projections gives
\[
\operatorname{Var}(\widehat X)=\frac{\operatorname{Var}(Q)}{4(n-1)^2}=\frac{n^2(2n+1)}{90},
\quad\operatorname{Var}(R)=\operatorname{Var}(X)-\operatorname{Var}(\widehat X)=\frac{n(n-2)}{30}.
\]
The explained fraction follows by division. Moreover,
\[
\mathcal R_n^2-\frac67=
\frac{(2n-9)(n-4)}{14(n-1)(n+3)}\ge0
\]
for integral \(n\ge2\), with equality only at \(n=4\); its limit is \(1\).

**4. Length-class signs and Pell boundary.** Sum (1) over the \(m_d\) potential chords at distance \(d\). This proves the displayed covariance vector. Because its denominator and \(m_d\) are positive, its sign is exactly that of \(n(n-1)-3(n-d)^2\). Writing \(x=2n-1\), \(y=n-d\), equality reduces to \(x^2-12y^2=1\). Every positive solution is generated from
\[
 x_j+y_j\sqrt{12}=(7+2\sqrt{12})^j,\qquad j=1,2,\ldots,
\]
with \(n=(x_j+1)/2\) and \(d=n-y_j\). Here \(x_j\) is odd and \(1\le d\le n\), so all such Pell solutions are admissible. The standard positive Pell solution classification excludes other equality cases, proving infinitude and exhaustiveness.

## Verification
Run the standard-library-only program `python verify.py`. It enumerates *every* perfect matching for \(2\le n\le7\), recomputes crossings and squared span deficits independently from their definitions, and checks exact means, variances, individual-edge covariances, length-count covariances, the projection coefficient, residual variance, and explained-variance fraction using rational arithmetic. It also checks the first three Pell-zero pairs through \(n=1999\). Its successful output is `VERIFY_OK 1106 exact assertions; 3 Pell-zero pairs through n=1999`. The infinite-domain proof is analytic and does not depend on the finite tests.

## Relationship to prior work
Acan (2015), Sections 2–3, provides conditional chord-crossing degree information and results on the number of chords of specified lengths. Paguyo (2021), Lemma 2.2 and Section 4.1, gives established moments of the crossing count, limit theory for short chords, and discusses length-class counts; Féray (2016), Section 6, gives another crossing central limit theorem via weighted dependency graphs. Cameron and Killpatrick (2019) study linear rather than cyclic chord lengths, especially the short-chord statistic. These results supply important ingredients and motivation. None of the material inspected states the exact projection onto **all** additive chord indicators, its residual \(n(n-2)/30\), the sharp \(6/7\) variance bound, or the Pell-classified length-covariance zeros. The contribution is the joint structural projection and variance decomposition, not previously established crossing moments, single-chord conditional expectations, or Poisson limits.

## Limitations
Optimality is within the affine span of edge-presence indicators: nonlinear functions of the entire matching or its length histogram may yield lower prediction error. Orthogonality of \(R\) and the indicators is not independence. The result is exact for uniform perfect matchings on a fixed cyclic order, not weighted matchings, arbitrarily distributed geometric endpoints, or random chord geometries with a different probability law. The crossing variance is a cited established premise; finite enumeration checks it only for \(2\le n\le7\). Historical priority for the particular decomposition is not independently certified, and an implicit derivation in broader matching projection literature remains possible.

## References
- H. Acan, *On a uniformly random chord diagram and its intersection graph*, first public arXiv posting 2015-01-07, arXiv:1501.01489; Sections 2–3. https://arxiv.org/abs/1501.01489
- J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, first public arXiv posting 2021-04-02, arXiv:2104.01134; Lemma 2.2 and Section 4.1, primary MSC2020 60C05. https://arxiv.org/abs/2104.01134
- V. Féray, *Weighted dependency graphs*, first public arXiv posting 2016-05-12, arXiv:1605.03836; Section 6. https://arxiv.org/abs/1605.03836
- N. T. Cameron and K. Killpatrick, *Statistics on Linear Chord Diagrams*, first public arXiv posting 2019-02-24, arXiv:1902.09021. https://arxiv.org/abs/1902.09021
- P. Flajolet and M. Noy, *Analytic combinatorics of chord diagrams*, 2000; crossing-moment results as cited in Paguyo's Lemma 2.2.
