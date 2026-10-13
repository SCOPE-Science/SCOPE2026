# Asymptotic independence of crossing and nesting counts in uniform chord diagrams

## Finding
For every integer \(n\geq 2\), choose uniformly one of the \((2n-1)!!\) perfect matchings on the ordered points \(1,\ldots,2n\). Let \(C_n\) count unordered pairs of matching edges with interlacing endpoints (crossings), and let \(N_n\) count unordered pairs in which one edge lies inside the other (nestings). Then
\[
\mathbb E C_n=\mathbb E N_n=\frac{n(n-1)}6,\quad
\operatorname{Var}(C_n)=\operatorname{Var}(N_n)=\frac{n(n-1)(n+3)}{45},
\]
\[
\operatorname{Cov}(C_n,N_n)=-\frac{n(n-1)}{18},\qquad
\operatorname{Corr}(C_n,N_n)=-\frac5{2(n+3)}.
\]
Despite this strictly negative covariance at every finite order, the *joint* fluctuation limit is
\[
\left(\frac{C_n-\binom n2/3}{n^{3/2}},
\frac{N_n-\binom n2/3}{n^{3/2}}\right)
\xrightarrow{\mathrm d}(G_C,G_N),
\qquad G_C,G_N\text{ independent }\mathcal N(0,1/45).
\]
Thus the first-order fluctuation channels are exactly orthogonal, although the finite-sample statistics are not independent. The principal assertion is their **joint Gaussian limit with independence**, supported by the exact covariance and projection identities; the pre-existing bivariate enumerator already determines the finite joint distribution.

## Assumptions and scope
The matchings are uniform on labeled *ordered* endpoints. For edges \((a,b)\), \((c,d)\) with left endpoints smaller than right endpoints, a crossing occurs when the four endpoints alternate, and a nesting when one interval strictly contains the other. An edge pair cannot be both. The theorem concerns *counts of pairs* of crossings and nestings, not the maximum number of mutually crossing or nested edges. There are no other parameters and no assumptions on endpoint spacings beyond their strict order.

## Proof
**A uniform independent-chord representation.** Sample \(2n\) independent continuous uniform points in \((0,1)\), group points in consecutive labeled pairs, and then rank the \(2n\) values. The induced matching of ranks is uniform: each matching has exactly \(2^n n!\) realizing permutations of the underlying labels. Let \(Z_i=(A_i,B_i)\), where \(0<A_i<B_i<1\) are the sorted endpoints of pair \(i\). These \(n\) chord variables are independent, each with density \(2\) on the unit upper triangle. Write \(h_C(Z_i,Z_j)\) and \(h_N(Z_i,Z_j)\) for the crossing and nesting indicators. Consequently \(C_n=\sum_{i<j}h_C(Z_i,Z_j)\) and \(N_n=\sum_{i<j}h_N(Z_i,Z_j)\): two bounded order-two U-statistics of independent chords.

**Conditional projections.** For a fixed chord with endpoints \(0<a<b<1\) and length \(\ell=b-a\), direct enumeration of the positions of two independent endpoints gives
\[
q_C(a,b):=\mathbb E[h_C(Z_1,Z_2)\mid Z_1=(a,b)]=2\ell(1-\ell),
\]
\[
q_N(a,b):=\mathbb E[h_N(Z_1,Z_2)\mid Z_1=(a,b)]=\ell^2+2a(1-b).
\]
Crossing means exactly one of the second chord's endpoints is in \((a,b)\). Nesting means both are inside or one is to the left and the other to the right. In particular \(\mathbb E q_C=\mathbb E q_N=1/3\). Integrating against density \(2\) on \(0<a<b<1\) yields
\[
\mathbb E[q_C^2]=\mathbb E[q_N^2]=\frac{2}{15},\qquad
\mathbb E[q_Cq_N]=\frac19.
\]
These integrations can be checked without numerical approximation: write \(h=1-\ell\), integrate \(a\) over \([0,h]\), and use
\[
\int_0^{h}(\ell^2+2a(h-a))\,da=\ell^2h+\frac{h^3}{3},
\]
\[
\int_0^{h}(\ell^2+2a(h-a))^2\,da
=\ell^4h+\frac23\ell^2h^3+\frac2{15}h^5.
\]
The remaining integrals of monomials in \(\ell\) and \(1-\ell\) give the stated rational values. Hence the first-projection covariance matrix is exactly
\[
\operatorname{Cov}\left((q_C(Z_1),q_N(Z_1))\right)
=\begin{pmatrix}1/45&0\\0&1/45\end{pmatrix}.
\]
This zero is the critical nontrivial cancellation.

**Finite covariance.** For either indicator \(h\), \(\mathbb Eh=1/3\) and \(\operatorname{Var}(h)=2/9\). For two distinct pairs of chord labels sharing exactly one label, conditional independence given that common chord shows that the covariance of two crossing indicators equals \(\operatorname{Var}(q_C)=1/45\); the same holds for nestings. The covariance of a crossing indicator and a nesting indicator on two distinct pairs sharing one label is \(\operatorname{Cov}(q_C,q_N)=0\). For the *same* pair of labels, crossing and nesting are mutually exclusive, so their covariance is \(-1/9\). Disjoint label pairs are independent. Counting \(\binom n2\) individual pairs and \(6\binom n3=n(n-1)(n-2)\) ordered overlapping pair-pair incidences in a variance sum gives
\[
\operatorname{Var}(C_n)=\binom n2\frac29+6\binom n3\frac1{45}
=\frac{n(n-1)(n+3)}{45},
\]
and the same for \(N_n\). Mixed pair-pair terms with different underlying label pairs vanish, giving \(\operatorname{Cov}(C_n,N_n)=-\binom n2/9\). Division by the positive variances yields the correlation formula. The formulas include the boundary \(n=2\).

**Independent bivariate limit.** For \(T=C,N\) define \(\xi_T(Z_i)=q_T(Z_i)-1/3\). The order-two Hoeffding decomposition gives
\[
T_n-\mathbb ET_n=(n-1)\sum_{i=1}^n\xi_T(Z_i)+R_{T,n},
\]
where \(R_{T,n}\) is a degenerate order-two U-statistic: conditional expectation of any summand given either argument is zero. Its variance is \(O(n^2)\) because its bounded pair summands are orthogonal whenever their index sets differ. Therefore \(R_{T,n}/n^{3/2}\to0\) in \(L^2\). The independent vectors \((\xi_C(Z_i),\xi_N(Z_i))\) are centered and bounded with covariance matrix \(\operatorname{diag}(1/45,1/45)\). The ordinary two-dimensional independent-summand central limit theorem, followed by Slutsky's theorem, proves the displayed joint weak limit. A centered Gaussian vector with diagonal covariance has independent coordinates. This last conclusion concerns weak limiting independence; it does not assert independence at any finite \(n\).

## Verification
The standalone \(\texttt{verify.py}\) implements independent recursive enumeration of perfect matchings through seven chords, comprising \(146599\) instances; it tests exact means and every entry of the three-by-three crossing/nesting/alignment covariance matrix using rational arithmetic (\(84\) exact checks). It separately enumerates the \(90\) interleavings of three labeled chords and symbolically verifies the first-projection integrals. Run with Python 3 and SymPy installed: \(\texttt{python verify.py}\); success prints \(\texttt{VERIFY_OK 146599 84}\). This finite check supports but does not replace the all-order U-statistic proof or the CLT.

## Relationship to prior work
Kasraoui and Zeng (2006), Proposition 3.8, give a joint crossing/nesting generating function for every finite matching size. Thus the present exact finite covariance formulas **are not represented as novel enumerations**; they can in principle be recovered by differentiating that earlier bivariate enumerator. Flajolet and Noy (2000) establish a **marginal** Gaussian limit for crossing counts and its variance, but not the independent two-dimensional crossing/nesting limit. Khare, Lorentz, and Yan develop exact moments of matching statistics and the marginal second moments for crossing and nesting classes, not the joint Gaussian independence proved here. Acan's random chord-diagram results concern, among other things, crossing-based intersection graphs and **maximal** crossing/nesting configurations, which are distinct from the pair counts here. The substantive distinction is the explicit zero covariance of the two first-order projections and the resulting joint limit, not a claim that marginal crossing normality or finite pairwise enumeration was unknown.

## Limitations
The conclusion is for uniform complete matchings on \(2n\) ordered endpoints only; it says nothing about nonuniform matchings, other pattern lengths, rates of multivariate normal approximation, or higher-order joint cumulants. The independence is asymptotic under \(n^{3/2}\) scaling and coexists with strictly negative finite correlation. Historical priority is provisional: an unpublished, unindexed, or implicit multivariate asymptotic analysis of the established bivariate generating function could have obtained this weak limit. No independent scientific audit has been performed.

## References
1. A. Kasraoui and J. Zeng, *Distribution of crossings, nestings and alignments of two edges in matchings and partitions*, arXiv:math/0601081v1 (first public version 2006-01-04), Proposition 3.8. https://arxiv.org/abs/math/0601081
2. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, Formal Power Series and Algebraic Combinatorics (2000), pp. 191–201. Author-hosted full text: https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
3. N. Khare, R. Lorentz, and C. H. Yan, *Moments of Matching Statistics*, author-hosted full text: https://people.tamu.edu/~huafei-yan/Files/final_joc158.pdf
4. H. Acan, *On a uniformly random chord diagram and its intersection graph*, Discrete Mathematics, DOI 10.1016/j.disc.2016.11.004 (source considered only as coverage comparison).
