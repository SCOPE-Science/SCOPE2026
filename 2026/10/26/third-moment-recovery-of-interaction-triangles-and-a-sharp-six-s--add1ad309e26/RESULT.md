# Third-moment recovery of interaction triangles and a sharp six-species risk reversal

## Finding

The retained interaction count in a partially surviving ecological network has the following identifiability property. Let \(G\) be a finite simple undirected graph on \(n\ge6\) species, and retain exactly \(k\) species uniformly without replacement. Let \(Y_k\) count retained edges. For two graphs with the **same degree multiset**, the entire first- and second-moment rarefaction curves agree. Their third moments satisfy
\[
\mathbb E Y_k^3(G)-\mathbb E Y_k^3(H)
=6\Delta T\,\frac{(k)_3(n-k)_3}{(n)_6}
+6\Delta K\,\frac{(k)_4(n-k)_2}{(n)_6},
\]
where \(T\) is triangle count, \(K=\sum_{uv\in E}(d_u-1)(d_v-1)\), \(\Delta\) means the difference between the two graphs, and \((a)_r\) denotes a falling factorial (zero if \(a<r\)). Thus third moments at just \(k=3,4\), together with the degree multiset, determine both \(T\) and \(K\). Conversely, equal \(T\) and \(K\) exactly characterize equality of the complete first-three-moment curves among degree-matched graphs.

For regular graphs \(K\) is already fixed by the degree sequence. In particular, for the triangular prism \(P=C_3\square K_2\) and the complete bipartite graph \(B=K_{3,3}\), both connected cubic six-species interaction networks, the probability generating functions satisfy
\[
\mathbb E[z^{Y_k(P)}]-\mathbb E[z^{Y_k(B)}]
=\begin{cases}(z-1)^3/10,&k=3,\\0,&k\ne3.\end{cases}
\]
Under independent species survival with common probability \(p\in(0,1)\), letting \(Y_p\) be the surviving-link count, the difference is exactly
\[
\mathbb E[z^{Y_p(P)}]-\mathbb E[z^{Y_p(B)}]
=2p^3(1-p)^3(z-1)^3.
\]
Consequently the prism has a larger chance of at least one link and at least three links, but a smaller chance of at least two links. The differences in the three upper-tail probabilities are respectively \(2a,-4a,2a\), with \(a=p^3(1-p)^3\). The graphs have equal means and variances throughout. Six is the smallest possible number of vertices for such a pair of nonisomorphic connected regular simple graphs.

## Assumptions and scope

A species interaction is represented by an unweighted undirected simple edge, without adaptive rewiring, trophic direction, or compensatory extinction. Only the induced edges among surviving species are counted. Sampling is either uniformly conditional on exactly \(k\) species surviving or independent common-probability species survival. The result concerns structural distinguishability and distributional risks, not statistical sampling-error bounds or dynamical food-web persistence.

Write \(m=|E(G)|\), \(d_v\) for vertex degrees, \(W=\sum_v\binom{d_v}{2}\), \(S=\sum_v\binom{d_v}{3}\), and \(T\) for the number of triangles. Define \(K=\sum_{uv\in E(G)}(d_u-1)(d_v-1)\). Set \(\alpha_j(k)=\binom{n-j}{k-j}/\binom nk\), with out-of-range binomial coefficients interpreted as zero. In the third-moment identity all dimensions are exact and \(3\le k\le n\) is permitted; the formula also applies to all \(0\le k\le n\) under the zero convention.

## Proof

**First two moments.** For each edge \(e\), let \(I_e\) indicate retention of both endpoints. Then \(Y_k=\sum_e I_e\). A specified \(j\)-vertex set is retained with probability \(\alpha_j\). Edge pairs share a vertex in exactly \(W\) cases; the other \(\binom m2-W\) pairs have four distinct endpoints. Thus
\[
\mathbb E Y_k=m\alpha_2,\qquad
\mathbb E Y_k^2=m\alpha_2+2W\alpha_3+2(\tbinom m2-W)\alpha_4.
\]
Both depend only on the degree multiset.

**Three-edge configurations.** Every unordered triple of distinct edges falls into exactly one of five classes: triangles (three occupied vertices), three-stars, three-edge paths (both four vertices), a wedge plus a disjoint edge (five), or three disjoint edges (six). Let their counts be \(T,S,P,U,V\), respectively. Counting an ordered pair of adjacent edges completed to a third edge gives
\[
P=K-3T,\quad U=W(m-2)-3T-3S-2P,
\quad V=\tbinom m3-T-S-P-U.
\]
Indeed \(K\) counts each triangle three times and each three-edge path once, while \(W(m-2)\) counts the wedge multiplicity three for triangles/stars, two for paths, and one for the five-vertex type. Substituting simplifies the latter two counts to
\[
U=W(m-2)-3S-2K+3T,\qquad
V=\tbinom m3-W(m-2)+2S+K-T.
\]
Expanding \((\sum I_e)^3\) and grouping ordered triples gives the exact identity
\[
\begin{aligned}
\mathbb E Y_k^3={}&m\alpha_2+6W\alpha_3+6(\tbinom m2-W)\alpha_4\\
&+6\bigl[T\alpha_3+(S+K-3T)\alpha_4\\
&\qquad+(W(m-2)-3S-2K+3T)\alpha_5\\
&\qquad+(\tbinom m3-W(m-2)+2S+K-T)\alpha_6\bigr].
\end{aligned}
\]
For degree-matched graphs all quantities other than \(T,K\) cancel. The two remaining coefficients are
\[
\alpha_3-3\alpha_4+3\alpha_5-\alpha_6
=\frac{(k)_3(n-k)_3}{(n)_6},\qquad
\alpha_4-2\alpha_5+\alpha_6
=\frac{(k)_4(n-k)_2}{(n)_6}.
\]
These follow by the inclusion-exclusion interpretation: probability that three specified vertices are present and three other specified vertices absent, and probability that four are present and two absent. This proves the central identity. At \(k=3\), the second coefficient is zero and the first strictly positive; at \(k=4\), the second is strictly positive for \(n\ge6\). Hence \(\Delta T\) and then \(\Delta K\) are uniquely recovered, establishing both directions of moment-curve identifiability. For \(d\)-regular graphs, \(K=m(d-1)^2\).

**Six-species pair and whole generating function.** Both \(P\) and \(B\) have six vertices and nine edges, each degree three, but \(T(P)=2\), \(T(B)=0\). Direct classification of their \(\binom63=20\) three-vertex subsets gives respective retained-edge count multiplicities (for counts \(0,1,2,3\)) of \((0,6,12,2)\) and \((2,0,18,0)\). The difference is \((-2,6,-6,2)\), proving the displayed generating-function difference at \(k=3\). Direct classification of each \(\binom6k\) set for \(k\ne3\) gives identical distributions (and is independently checked by the executable enumeration in the verification package). It can also be established without enumeration: for \(k\ge4\), replacing a retained set by its complement and using regularity gives \(Y_k=m-d(6-k)+Y_{6-k}\); for \(k\le2\) the two graphs have equal vertex and edge counts, hence identical \(Y_k\) distributions. Therefore all other fixed-\(k\) generating-function differences vanish. Binomially mixing conditional distributions over \(k\) proves the independent-survival formula with coefficient \(\binom63p^3(1-p)^3\cdot 1/10=2p^3(1-p)^3\). Expanding \((z-1)^3\) and summing probabilities above each threshold gives the three upper-tail differences. Equal first-two-moment curves imply equal Bernoulli-mixture means and variances.

**Minimality.** For connected simple regular graphs with fewer than six vertices the degree determines the unlabelled graph up to isomorphism: degrees zero or one force trivial connected graphs; degree two forces a cycle; on at most five vertices every other realizable connected regular degree is complete or complementary to the unique matching. On six vertices, the connected cubic case has precisely the prism and \(K_{3,3}\) as its two nonisomorphic graphs: complementing produces a two-regular graph on six vertices, necessarily one six-cycle or two triangles. Therefore six is the first order permitting the claimed degree-controlled disparity.

## Verification

Run the dependency-free `verify.py` in the same directory as `CERTIFICATE.json`. It enumerates all \(2^{15}=32{,}768\) labeled simple six-vertex graphs and their 64 retained-vertex subsets, checking 688,128 exact moment formula comparisons; it also confirms the generating-function differences and the classification of connected regular graph types through six vertices. Arithmetic is integer or rational. The enumerator provides finite exhaustive checks at six vertices; the identities and identifiability for arbitrary \(n\) follow from the proof above rather than extrapolation.

## Relationship to prior work

Dunne, Williams, and Martinez (2002) studied species losses in ecological food webs and motivates interaction survival as an informative observable, but the accessible source material is about robustness/connectance, not the exact retained-edge moment inverse problem. Jha, Seshadhri, and Pinar (2014) developed path sampling for four-vertex subgraph counts, a different sampling target. Bhattacharya, Das, and Mukherjee (2020) analyzed motif estimation from independently sampled vertices, including fourth-moment asymptotics; their general framework is closest in sampling mechanism, but the inspected parts do not give this exact finite-sample first-three-moment identification, six-vertex generating-function contrast, or two-threshold risk reversal. Generic motif-moment expansions could conceivably imply parts of the algebra; originality is claimed for the combined precise theorem subject to that bibliographic limitation.

## Limitations

The theorem does not assert empirical causal dominance between particular food webs, global network identifiability from three moments, or a persistence result. Recovering \(T,K\) presupposes the known degree multiset and exact population moments at two sampling sizes; sampling variance and nonuniform survival are outside scope. The strict upper-tail reversal concerns thresholds one, two, and three in one six-vertex witness, not arbitrary ecological objectives. Published results under other terminology may subsume some aspects; no independent review has been performed.

## References

1. Dunne, J. A., Williams, R. J., and Martinez, N. D. (2002), Network structure and biodiversity loss in food webs: robustness increases with connectance, Ecology Letters 5, 558–567, https://doi.org/10.1046/j.1461-0248.2002.00354.x (publicly dated 2002-07-10).
2. Jha, M., Seshadhri, C., and Pinar, A. (2014), Path Sampling: A Fast and Provable Method for Estimating 4-Vertex Subgraph Counts, https://arxiv.org/abs/1411.4942 (first posted 2014-11-18).
3. Bhattacharya, B. B., Das, S., and Mukherjee, S. (2020), Motif Estimation via Subgraph Sampling: The Fourth Moment Phenomenon, https://arxiv.org/abs/2011.03026 (first posted 2020-11-05).
