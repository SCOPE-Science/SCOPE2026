# Negative component–coverage covariance for uniformly paired intervals

## Finding

Fix an integer \(n\ge2\). Take any \(2n\) strictly increasing real locations \(y_1<\cdots<y_{2n}\), and choose a perfect matching of their labels uniformly among all \((2n-1)!!\) matchings. Replace each matched pair by the closed interval between its locations. Let \(K_n\) be the number of connected components of the union and let \(V_n\) be its Lebesgue length. **For every such fixed configuration of locations,**

\[
\operatorname{Cov}(K_n,V_n\mid y_1,\ldots,y_{2n})<0.
\]

More precisely, for \(1\le j<n\), let \(Z_j\) indicate that the first \(2j\) labels are all matched amongst themselves. Put

\[
q_{a,b}=\frac{\binom{a}{b}}{\binom{2a}{2b}}\qquad(1\le b<a),
\]

and define

\[
d_{n,j}=q_{n,j}(1-q_{n,j})+\sum_{\substack{1\le i<n\\i\ne j}}q_{n,\max(i,j)}\bigl(q_{\max(i,j),\min(i,j)}-q_{n,\min(i,j)}\bigr).
\]

Every term is strictly positive and the exact conditional covariance is

\[
\boxed{\operatorname{Cov}(K_n,V_n\mid y_1,\ldots,y_{2n})=-\sum_{j=1}^{n-1}(y_{2j+1}-y_{2j})d_{n,j}<0.}
\]

The same strict sign holds **unconditionally** when the ordered location vector is random and independent of the uniform matching, provided its total range is integrable. In particular this covers order statistics of independent observations from **any atomless law with finite first absolute moment**, without a density, symmetry, or uniformity assumption.

For independent uniform locations on a nondegenerate interval \([a,b]\), a further exact relation holds:

\[
\boxed{\operatorname{Cov}(K_n,V_n)=-\frac{b-a}{2n+1}\operatorname{Var}(K_n).}
\]

For \(n=2\), this is \(-2(b-a)/45\). The boundary case \(n=1\) has deterministic component count and covariance zero, and is excluded from the strict assertion.

## Assumptions and scope

The geometric locations are real and pairwise distinct in increasing order. The matching is exactly uniform among all perfect matchings and independent of the locations if the latter are random. The set covered by the matching is the union of its **line intervals**, not an intersection graph of chords drawn on a circle. Both the component count and the union length are computed in the real line. If the locations are random, the finite expectation of their range guarantees the existence of the covariance. No assertion is made for nonuniform or location-dependent matchings, repeated endpoints, or nonintegrable ranges.

## Proof

**Step 1 (cut representation).** Write \(g_k=y_{k+1}-y_k>0\). The open gap between the \(k\)-th and \((k+1)\)-st locations is outside every matched interval exactly when no matched pair straddles this gap. If \(k\) is odd, this is impossible by parity: an odd number of labels cannot all be paired internally. If \(k=2j\) is even, precisely the event \(Z_j=1\) leaves the gap uncovered. Hence, deterministically for every matching,

\[
K_n=1+\sum_{j=1}^{n-1}Z_j,\qquad
V_n=y_{2n}-y_1-\sum_{j=1}^{n-1}g_{2j}Z_j.
\]

All intervals are nonempty and the first and last locations are covered, so these missing gaps account for all components and all missing length.

**Step 2 (exact matching probabilities).** Internal matching of the first \(2j\) labels and of the remaining \(2n-2j\) labels can be chosen in \((2j-1)!!(2n-2j-1)!!\) ways. Consequently,

\[
\Pr(Z_j=1)=\frac{(2j-1)!!(2n-2j-1)!!}{(2n-1)!!}=q_{n,j},
\]

where the conventional empty double factorial is \((-1)!!=1\). If \(1\le i<j<n\), conditional on \(Z_j=1\), the matching inside the first \(2j\) labels is uniform, giving

\[
\Pr(Z_i=Z_j=1)=q_{n,j}q_{j,i}.
\]

**Step 3 (strict positive cut correlations).** For integers \(a>b\ge1\), direct cancellation of binomial coefficients yields

\[
\frac{q_{a+1,b}}{q_{a,b}}=\frac{2a+1-2b}{2a+1}<1.
\]

Thus \(q_{j,i}>q_{n,i}\) whenever \(i<j<n\), and therefore

\[
\operatorname{Cov}(Z_i,Z_j)=q_{n,j}(q_{j,i}-q_{n,i})>0
\]

for distinct cuts (exchange \(i,j\) if necessary). For a single cut, \(\operatorname{Var}(Z_j)=q_{n,j}(1-q_{n,j})>0\), since \(0<q_{n,j}<1\). It follows that

\[
d_{n,j}=\operatorname{Cov}(K_n,Z_j)=\sum_{i=1}^{n-1}\operatorname{Cov}(Z_i,Z_j)>0.
\]

**Step 4 (conditional and unconditional covariance).** With the locations fixed, the two identities in Step 1 and positivity in Step 3 imply

\[
\operatorname{Cov}(K_n,V_n\mid \boldsymbol y)=-\sum_{j=1}^{n-1}g_{2j}\,d_{n,j}<0.
\]

For random locations independent of the matching, \(\mathbb E(K_n\mid\boldsymbol Y)=1+\sum_jq_{n,j}\) is constant. The total-covariance identity therefore removes its between-location term and gives

\[
\operatorname{Cov}(K_n,V_n)=-\sum_{j=1}^{n-1}\mathbb E(Y_{2j+1}-Y_{2j})d_{n,j}<0.
\]

Integrability follows from \(0\le V_n\le Y_{2n}-Y_1\) and \(1\le K_n\le n\). Every expected even spacing is strictly positive because the locations are strictly increasing almost surely.

**Step 5 (uniform-spacing identity).** For \(2n\) independent uniform observations on \([a,b]\), each internal order-statistic spacing has mean \((b-a)/(2n+1)\). Also, because \(K_n=1+\sum_jZ_j\),

\[
\sum_{j=1}^{n-1}d_{n,j}=\operatorname{Var}(K_n).
\]

Substituting these equal expected spacings into Step 4 proves the stated uniform identity. At \(n=2\), \(\Pr(K_2=2)=1/3\), so \(\operatorname{Var}(K_2)=2/9\) and the displayed value follows.

## Verification

The accompanying standalone `verify_matching_intervals.py` uses only Python standard-library exact fractions. It exhaustively enumerates all perfect matchings for \(n=2,3,4,5,6,7\), constructs geometric intervals and merges them **independently** of the proposed cut formula, and compares first and second component moments and mixed covariance with the closed formulas. For each size it checks two distinct positive gap profiles, one equal-spaced and one highly unequal, thus giving twelve exact geometric comparisons. It also checks individual and joint cut probabilities and six uniform-spacing identities. Run `python verify_matching_intervals.py` to reproduce the verification. These finitely many checks are corroboration; the proof of the theorem for all \(n\) and all admissible location laws is the analytic argument above.

## Relationship to prior work

Uniform perfect matchings of ordered endpoints are linear versions of the standard random chord-diagram model. Flajolet and Noy analyze **components of the chord-intersection graph** and crossings; these are not components of the union of real intervals. For example, nested chords produce separate vertices in an intersection graph but overlapping line intervals. Acan studies the same chord-intersection graph, its degrees, cores, and component structure, without the joint union-length statistic. Young studies **connected groups of adjacent short chords** (his Definition 2), also distinct from components of the union of all matched intervals. None of those specifically inspected statements gives the present location-uniform, conditional mixed covariance or its exact uniform-spacing identity. The elementary matching counts used in the proof are standard combinatorial ingredients, not separately asserted to be new.

## Limitations

The strict sign concerns **covariance**, not stochastic dominance or full negative association. No claim is made for nonuniform or geometry-dependent pairings. The sharp factor in the uniform-spacing identity requires uniform locations; a general atomless distribution instead has location-dependent mean spacings. Finite enumeration is not an infinite certificate. Although relevant prior primary work has been compared at the level of its component definitions and stated results, older matching-factorization or interval-coverage literature could imply the mixed formula indirectly; historical priority is not exhaustively established. Independent validation has not been performed.

## References

1. H. Acan, *On a uniformly random chord diagram and its intersection graph*, first public arXiv version 7 January 2015, arXiv:1501.01489v1, https://arxiv.org/abs/1501.01489.
2. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report RR-3914 (2000), https://algo.inria.fr/flajolet/Publications/FlNo00.pdf.
3. D. Young, *Linear k-Chord Diagrams*, arXiv:2004.06921v3 (2020), https://arxiv.org/abs/2004.06921.
