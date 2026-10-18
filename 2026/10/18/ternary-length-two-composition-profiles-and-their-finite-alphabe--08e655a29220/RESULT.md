# Ternary length-two composition profiles and their finite-alphabet growth law

## Finding
Fix an alphabet of \(q\ge2\) distinct labeled symbols. For a word of length \(n\), observe the multiset of compositions of **all contiguous factors of lengths one and two**. An unordered composition specifies the multiplicity of each symbol in its factor, so the length-two factors \(ij\) and \(ji\) have identical observations. Let \(P_q(n)\) be the number of distinct observations among length-\(n\) words, equivalently the maximum size of a zero-error code distinguishable from these observations.

For the first nonbinary alphabet, \(q=3\), the complete generating function is
\[
\sum_{n\ge1}P_3(n)z^{n-1}=
\frac{3(1-2z+2z^2+3z^3-2z^4+z^6-z^7)}{(1-z)^6(1+z)^2}.
\]
In particular \(P_3(1),\ldots,P_3(12)\) are
\[
3,6,18,45,108,228,447,807,1377,2226,3456,5169,
\]
and \(P_3(28)=282873\). All coefficients are exact. The resulting quasi-polynomial has period dividing two and satisfies
\[
P_3(n)=\frac{n^5}{80}+O(n^4).
\]
More generally, for every fixed integer \(q\ge2\), put \(E=\binom{q+1}{2}\). Then
\[
\boxed{P_q(n)=\frac{E}{2^{q-1}(E-1)!}\,n^{E-1}+O_q(n^{E-2}).}
\]
The general coefficient follows from a complete graph-theoretic characterization, given below, rather than an extrapolation of finite data.

## Assumptions and scope
The word is linear (not cyclic); the alphabet is labeled; the observation has multiplicities and includes lengths **one and two only**. No symbol ordering within a length-two factor is retained. Define the number of singleton factors of symbol \(i\) as \(v_i\). Define \(e_{ij}=e_{ji}\), for \(i\le j\), as the number of length-two factors containing \(i\) and \(j\). The \(E\) numbers \(e_{ij}\) sum to \(m=n-1\).

Construct an undirected multigraph \(G\) with vertex set the alphabet, \(e_{ii}\) loops at vertex \(i\), and \(e_{ij}\) undirected edges between distinct vertices. Loops contribute two to the degree. The **edge support** \(S\) consists of positive-degree vertices, and its connectivity ignores isolated unused letters. When \(n\ge2\), \(S\) is nonempty.

## Proof
**Graph/profile equivalence.** Reading a word from left to right traverses precisely its \(m\) adjacent-pair edges; it is an Euler trail of \(G\). Thus its positive-degree support is connected, and the number of odd-degree vertices is zero or two. Conversely, the Euler-trail criterion for undirected multigraphs gives a word traversing every edge once whenever that support is connected and the number of odd-degree vertices is zero or two. Loops cause no exception.

Let \(d_i\) be the degree and \(t_i\) the number of endpoints of the traversal equal to symbol \(i\); the initial and final symbols are counted separately, including twice when they coincide. Counting symbol occurrences before and after each traversed edge gives the identity
\[
2v_i=d_i+t_i.
\]
If precisely two vertices have odd degree, the trail endpoints are the two odd vertices and hence their \(t_i\), and the profile \(v_i\), are forced. If all degrees are even, an Euler circuit may start and end at **any** vertex in \(S\), giving exactly \(|S|\) different symbol-count profiles. These profiles are distinct because their endpoint vectors differ. Consequently, for \(n\ge2\), the exact count is
\[
P_q(n)=\sum_{\substack{(e_{ij})_{i\le j}\ge0\\\sum e_{ij}=n-1\\G[S]\ \mathrm{connected}}}
\begin{cases}
|S|,&\text{every degree is even},\\
1,&\text{exactly two degrees are odd},\\
0,&\text{otherwise}.
\end{cases}
\]
At \(n=1\), the \(q\) singleton words yield \(P_q(1)=q\). Every distinct observation gives one equivalence class of words, so a distinguishable code has at most one word per class; selecting one from every class attains \(P_q(n)\).

**Ternary generating function.** Set \(z\) to mark each adjacency edge, and partition connected multigraphs by the cardinality of their positive-degree support. Single-vertex graphs contribute \(3/(1-z)\): their edges are loops and each graph carries one profile. For a fixed pair of vertices, the cross-edge multiplicity \(c\) is positive. If \(c\) is odd there is one endpoint profile; if \(c\) is even there are two. The two loop multiplicities are free. Summing over the three pairs gives
\[
F_2(z)=\frac{3(z+2z^2)}{(1-z^2)(1-z)^2}.
\]
For all three vertices to occur, let \(a,b,c\) be the multiplicities on the three different cross-edges. Their positive-edge graph is connected precisely when at least two of \(a,b,c\) are positive. Therefore the unweighted cross-edge series is
\[
\frac{3z^2-2z^3}{(1-z)^3}.
\]
Every such graph has either two odd vertices (one profile) or no odd vertices (three profiles). All three vertex degrees are even precisely when \(a,b,c\) have a common parity. With at least two positive, the all-even cross-edge series is
\[
\frac{z^3+3z^4-2z^6}{(1-z^2)^3}.
\]
There are three free loop variables. The three-vertex contribution is therefore
\[
F_3(z)=\frac{3z^2-2z^3}{(1-z)^6}
+\frac{2(z^3+3z^4-2z^6)}{(1-z)^3(1-z^2)^3}.
\]
Here the factor two adds the two **extra** profiles for an all-even graph. The sum \(3/(1-z)+F_2(z)+F_3(z)\) simplifies by ordinary rational algebra to the claimed expression. All possible words and profiles are counted once by their literal multiplicity vectors.

**Leading coefficient for arbitrary alphabets.** There are \(E=q(q+1)/2\) possible unordered edge types, including loops. The number of nonnegative edge-multiplicity vectors summing to \(m\) is \(\binom{m+E-1}{E-1}\). Vectors having any prescribed edge type absent number only \(O_q(m^{E-2})\). In particular, except for that lower-order contribution, every type occurs and the graph has full support and is connected.

The parity of a degree depends solely on the cross-edge multiplicities modulo two. The attainable parity vectors are exactly the \(2^{q-1}\) binary vectors of even total parity. For each such parity vector, the number of nonnegative edge-multiplicity vectors of weight \(m\) is
\[
\frac{1}{2^{q-1}}\binom{m+E-1}{E-1}+O_q(m^{E-2}).
\]
To justify uniformity, fix a nonempty character of the even-parity space, represented by signs on a nontrivial vertex cut. The multivariate generating function of the signed multiplicities, after recording total edge count by \(z\), is a product of factors \((1-z)^{-1}\) for the loop edges and same-side cross-edges and \((1+z)^{-1}\) for crossing edges. A nontrivial cut has at least one crossing edge and at least one noncrossing edge (all \(q\) loops are noncrossing). Thus the poles at both \(z=1\) and \(z=-1\) have orders at most \(E-1\), so its coefficients are \(O_q(m^{E-2})\). Fourier inversion over the degree-parity group proves the displayed equidistribution, including possible period-two fluctuations in the error term.

For full support, an all-even degree vector has weight \(q\); a vector with exactly two odd degrees has weight one, and all other parity vectors have weight zero. The sum of weights across parity vectors is \(q+\binom q2=E\). Multiplying this weight sum by the asymptotic number per parity class, and absorbing disconnected or non-full-support cases into the error term, yields
\[
P_q(n)=\frac{E}{2^{q-1}}\binom{n+E-2}{E-1}+O_q(n^{E-2})
=\frac{E}{2^{q-1}(E-1)!}n^{E-1}+O_q(n^{E-2}).
\]
For \(q=3\), the leading coefficient is \(6/(4\cdot120)=1/80\), agreeing with the pole of the exact generating function.

## Verification
The accompanying standalone `verify.py` uses three mathematically distinct finite checks. First it enumerates ternary words literally for every \(1\le n\le11\), derives their observations by counting singleton and adjacent-pair factor compositions, and compares the distinct count with the rational-series coefficients. Second it enumerates all ternary edge-multiplicity vectors independently, determines graph connectivity and degree parity, and checks the exact graph/profile count against the rational series for every \(1\le n\le28\). Third it compares literal word enumeration against graph enumeration for \(q=4\) and \(1\le n\le7\). Each assertion passed. The code also regenerates all displayed coefficients and the \(n=28\) value using integer arithmetic.

These are finite reproducibility checks, not substitutes for the all-length proofs above.

## Relationship to prior work
Ye and Elishco defined the length-limited substring-composition model and developed reconstruction constructions for general alphabets and varying length limits; their length-two ternary profile count is not given there. The existing exact **binary** length-two composition-profile result gives a quadratic count and an ambiguity classification; restricting to binary words does not imply the ternary generating function or the all-alphabet leading coefficient. Gabrys and Milenkovic study ordered substring multispectra, which distinguish \(ij\) from \(ji\), unlike the present observations. Jacquet, Knessl, and Szpankowski count balanced **directed cyclic** Markov types, not undirected adjacent-composition spectra of linear words with endpoint-sensitive singleton counts. Their asymptotic exponent for three symbols differs from the exponent here.

## Limitations
The exact rational function is for \(q=3\), length limit two. The all-alphabet theorem identifies only the dominant term, not a general closed rational function or ambiguity-class multiplicities for \(q\ge4\). Neither theorem handles longer observed factors, noisy counts, unlabeled alphabets, or cyclic reads. Targeted searches and full-text comparisons did not show an existing equivalent formula, but an unindexed treatment under undirected Markov types or Euler-trail enumerators is a residual originality risk. Independent mathematical verification has not been performed.

## References
1. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963v1 (first posted 2022-08-31); IEEE Transactions on Information Theory **70** (2024), 3922–3940.
2. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548 (2018); IEEE Transactions on Information Theory **65** (2019), 7682–7696.
3. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), 387–400; DOI:10.46298/dmtcs.2768.
4. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *String Reconstruction from Substring Compositions*, SIAM Journal on Discrete Mathematics **29** (2015), 1340–1371.
