# An exact edge–triangle correlation gap in random chord intersection graphs

## Finding
Take a uniformly random perfect matching of \(2n\) distinct, cyclically ordered points, where \(n\ge3\) is an integer. Draw each matched pair as a chord. Its intersection graph has one vertex per chord and one edge for each crossing pair. Write \(X_n\) for its edge count and \(T_n\) for its number of (unordered) three-vertex cliques, that is, triples of mutually crossing chords. Then
\[
\mathbb E X_n=\frac{n(n-1)}6,\qquad
\mathbb E T_n=\frac{1}{15}\binom n3,
\]
\[
\operatorname{Var}(X_n)=\frac{n(n-1)(n+3)}{45},\qquad
\operatorname{Var}(T_n)=\binom n3\left(\frac{14}{225}+\frac{6(n-3)}{175}+\frac{(n-3)(n-4)}{350}\right),
\]
and
\[
\boxed{\operatorname{Cov}(X_n,T_n)=\frac{n(n-1)(n-2)(n+4)}{315}>0.}
\]
In particular,
\[
\boxed{\lim_{n\to\infty}\operatorname{Corr}(X_n,T_n)^2=\frac{20}{21}.}
\]
Thus the mean-square-optimal *linear* prediction of \(T_n\) from \(X_n\), with an intercept, leaves an asymptotically nonzero residual variance fraction \(1/21\). This is a statement about linear prediction, not a claim about arbitrary nonlinear prediction or joint asymptotic normality.

## Assumptions and scope
The endpoint locations are fixed, distinct and strictly ordered around a circle; only their cyclic order matters. Every perfect matching of those \(2n\) labeled endpoints has probability \(1/(2n-1)!!\). Chords are undirected, are drawn as straight segments, and cross when their interiors intersect. Clique triangles require all three chord pairs to cross. The correlation is defined for all integers \(n\ge3\), because both variances are positive. No independence of crossing indicators is assumed.

## Proof
**Step 1: restriction to finitely many chord labels.** Independently assign labels to the \(n\) chords in a uniform random ordering. Equivalently, read the endpoints cyclically as a uniform word containing each of the \(n\) labels exactly twice. For any chosen \(r\) labels, their induced relative word is uniformly distributed over the \((2r)!/2^r\) words with those letters each repeated twice. Relative words on disjoint label sets are independent (uniform shuffling of two independently uniform relative orders). Therefore indicators of events supported on disjoint chord-label sets are independent. This reduction applies to all \(n\).

**Step 2: exact local joint probabilities.** Let \(E_{ab}\) be the indicator that chords \(a,b\) cross, and \(Q_{abc}\) the indicator that \(a,b,c\) cross pairwise. The following table concerns **all** relative words for the indicated number of labeled chords; it is a complete finite count, not an asymptotic or Monte Carlo estimate.

| Event | Chord labels | Favourable words / all words | Probability |
| --- | ---: | ---: | ---: |
| \(E_{ab}\) | 2 | 2 / 6 | \(1/3\) |
| \(E_{ab}E_{ac}\) | 3 | 12 / 90 | \(2/15\) |
| \(Q_{abc}\) | 3 | 6 / 90 | \(1/15\) |
| \(Q_{abc}E_{ad}\) | 4 | 72 / 2520 | \(1/35\) |
| \(Q_{abc}Q_{abd}\) | 4 | 40 / 2520 | \(1/63\) |
| \(Q_{abc}Q_{ade}\) | 5 | 720 / 113400 | \(2/315\) |

For completeness, each entry may be reconstructed without a stochastic simulation: choose the two endpoint positions for the first label, then two of the remaining positions for the next, continuing until the last label is forced; at each complete word, test alternation of the two occurrences of each candidate crossing pair. The included `verify.py` enumerates these finite possibilities exactly as integers. The table thus specifies a terminating, explicit counting proof of the only nonstandard finite coefficients used below.

**Step 3: count overlapping indicators.** Write \(X_n=\sum_{a<b}E_{ab}\), \(T_n=\sum_{a<b<c}Q_{abc}\). The mean formulas follow from the first and third rows. For the variance of \(X_n\), distinct edge indicators sharing one label have covariance \(2/15-1/9=1/45\); those sharing no labels are independent. Hence
\[
\operatorname{Var}(X_n)=\binom n2\left(\frac29+2(n-2)\frac1{45}\right)=\frac{n(n-1)(n+3)}{45}.
\]
For distinct triangle indicators sharing respectively two or one labels, their covariances are
\[
\frac1{63}-\frac1{225}=\frac2{175},\qquad
\frac2{315}-\frac1{225}=\frac1{525}.
\]
A fixed triangle has \(3(n-3)\) other triangles sharing two labels, and \(3\binom{n-3}{2}\) sharing exactly one; triangles with disjoint labels are independent. Counting both orders in variance gives
\[
\begin{aligned}
\operatorname{Var}(T_n)
&=\binom n3\left[\frac{14}{225}+3(n-3)\frac2{175}+3\binom{n-3}{2}\frac1{525}\right]\\
&=\binom n3\left[\frac{14}{225}+\frac{6(n-3)}{175}+\frac{(n-3)(n-4)}{350}\right].
\end{aligned}
\]
A triangle and one of its three own edges have covariance \(1/15-(1/15)(1/3)=2/45\). A triangle and an edge sharing exactly one label have covariance \(1/35-1/45=2/315\). For each triangle there are three edges of the first kind and \(3(n-3)\) of the second; disjoint edges contribute zero. Consequently
\[
\operatorname{Cov}(X_n,T_n)
=\binom n3\left[3\frac2{45}+3(n-3)\frac2{315}\right]
=\frac{n(n-1)(n-2)(n+4)}{315}.
\]
All identities hold for each integer \(n\ge3\), with the lower boundary cases covered by the same counts and the empty overlap sums interpreted as zero.

**Step 4: sharp linear-prediction limit.** Taking leading terms gives
\[
\operatorname{Var}(X_n)\sim\frac{n^3}{45},\quad
\operatorname{Var}(T_n)\sim\frac{n^5}{2100},\quad
\operatorname{Cov}(X_n,T_n)\sim\frac{n^4}{315}.
\]
Therefore the squared correlation tends to
\[
\frac{(1/315)^2}{(1/45)(1/2100)}=\frac{20}{21}.
\]
For a nondegenerate bivariate finite-variance law, least-squares affine prediction has explained fraction exactly squared correlation; hence its unexplained variance fraction tends to \(1/21\). Equivalently the residual variance has leading term \(n^5/44100\). These conclusions follow algebraically from the exact finite formulas, with no appeal to any limiting distribution.

## Verification
The standalone `verify.py` uses only the Python standard library. It exactly enumerates all repeated-label words for the six local events, obtaining numerators \((2,12,6,72,40,720)\) over denominators \((6,90,90,2520,2520,113400)\). Independently, it enumerates every perfect matching for \(n=3,4,5,6,7\), computes the intersection graph directly, and checks both means, both variances and the covariance as rational numbers. It also checks positivity and correlation bounds for a finite range. Run `python verify.py`. The unbounded theorem is justified by the overlap decomposition and the complete **five-label** local enumeration, not by the bounded global matching checks.

## Relationship to prior work
Flajolet and Noy (2000) establish marginal moments and a limit law for the total crossing count. Acan (arXiv:1501.01489v1, 2015) treats the same uniform-matching intersection graph and studies degrees, components, cliques and core structures; its primary classification is 60C05. Pilaud and Rué (arXiv:1307.6440v1, 2013) provide generating functions for diagrams with a *fixed total number* of crossings and discuss forbidden cliques, but not mixed moments for unrestricted random diagrams. Paguyo (arXiv:2104.01134, 2021) gives crossing-count normal approximation and simple-chord asymptotics; Stoimenow's 1999 thesis chapter on chord-diagram enumeration deals with isolated-chord and noncrossing counts. The crossing-count mean and variance are acknowledged as known; the finding assessed here is the simultaneous exact **triangle variance and edge–triangle covariance**, with the \(20/21\) explained-variance limit. These inspected sources did not state that joint result.

## Limitations
The model is a uniform **perfect matching of fixed cyclic endpoints**, not arbitrary independent continuous random chords or an Erdős–Rényi graph. The result identifies exact second moments and optimal *affine* prediction only; it does not prove a bivariate central limit theorem, nonlinear prediction optimality, or a statistical sampling application. General mixed-pattern/U-statistic frameworks might imply the same formulas without spelling them out, so exhaustive historical priority is not certified. Independent scientific review has not been performed.

## References
- P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, 2000; publicly available at https://algo.inria.fr/flajolet/Publications/FlNo00.pdf.
- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, first posted 2015-01-07, https://arxiv.org/pdf/1501.01489.
- V. Pilaud and J. Rué, *Analytic combinatorics of chord and hyperchord diagrams with k crossings*, arXiv:1307.6440v1, https://arxiv.org/pdf/1307.6440.
- J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, https://arxiv.org/pdf/2104.01134.
- A. Stoimenow, *On enumeration of chord diagrams and asymptotics of Vassiliev invariants*, dissertation, 1999, Chapter 3, https://webdoc.sub.gwdg.de/ebook/diss/2003/fu-berlin/1999/21/kap3.pdf.
