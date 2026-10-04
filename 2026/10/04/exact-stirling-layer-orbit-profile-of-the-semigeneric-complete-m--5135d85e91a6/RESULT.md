# Exact Stirling-layer orbit profile of the semigeneric complete multipartite digraph

## Finding

Let \(M\) be the countable semigeneric complete multipartite digraph: non-adjacency is an equivalence relation, every pair of vertices in distinct classes is joined by exactly one directed edge, and between any two equivalence classes every \(2\times2\) rectangle has even orientation parity. Let \(a_n\) be the number of \(\operatorname{Aut}(M)\)-orbits on injective ordered \(n\)-tuples. Then
\[
\boxed{a_0=1,\qquad a_n=\sum_{k=1}^n {n\brace k}\,2^{(k-1)n-\binom{k}{2}}\quad(n\ge1),}
\]
where \({n\brace k}\) is a Stirling number of the second kind. Equivalently,
\[
\boxed{a_n=2^{\binom n2}\sum_{j=0}^{n-1}{n\brace n-j}\,2^{-\binom{j+1}{2}}.}
\]
The first values are
\[
1,1,3,21,313,9585,591841,72906689,17809866625,\ldots
\]
for \(n=0,1,\ldots\).

For arbitrary ordered tuples, allowing repeated coordinates, the orbit profile is the Stirling transform
\[
\boxed{b_n=\sum_{r=0}^n {n\brace r}a_r,}
\]
beginning
\[
1,1,4,31,461,13286,757945,86793311,20019300954,\ldots.
\]

The exact formula also gives the entropy refinement
\[
\boxed{\log_2 a_n=\binom n2+2(\log_2 n)^2+O(\log n\,\log\log n).}
\]
Thus the parity condition changes the profile from a bare tournament term \(2^{\binom n2}\) by a superpolynomial but subexponential factor
\[
2^{2(\log_2 n)^2+O(\log n\log\log n)}.
\]

## Assumptions and scope

The semigeneric digraph is a standard countable ultrahomogeneous digraph. Kurilić and Kuzeljević explicitly include it among the countable ultrahomogeneous digraphs with strong amalgamation, describing it as a semigeneric variant of the countable complete multipartite digraph with the parity constraint that, for two pairs chosen from distinct non-adjacency classes, the number of directed edges from one pair to the other is even. Their article is classified primarily under \(03\mathrm{C}15\).

The claim concerns the exact labeled finite-age count, interpreted by ultrahomogeneity as an injective tuple-orbit count. It does not claim that the semigeneric digraph, its parity characterization, or the two-part structural lemma are new.

## Proof

Fix an injective ordered \(n\)-tuple and identify its coordinates with \([n]\). Its non-adjacency classes form a set partition \(\pi\) of \([n]\). Suppose \(\pi\) has \(k\) blocks \(B_1,\ldots,B_k\), with sizes \(s_1,\ldots,s_k\).

Consider two distinct blocks \(B_i,B_j\) of sizes \(r,s\). Encode the direction of every cross-edge by an \(r\times s\) binary matrix \(X\), where \(X_{uv}=1\) means that the edge is directed from the vertex in \(B_i\) to the vertex in \(B_j\). The semigeneric parity axiom says exactly that every \(2\times2\) submatrix has even binary sum:
\[
X_{uv}+X_{u'v}+X_{uv'}+X_{u'v'}=0\pmod2.
\]
Equivalently,
\[
X_{uv}=\rho_u+\gamma_v\pmod2
\]
for row bits \(\rho_u\) and column bits \(\gamma_v\). There are \(2^{r+s}\) choices of these bits, and the simultaneous replacement
\[
(\rho,\gamma)\mapsto(\rho+1,\gamma+1)
\]
leaves \(X\) unchanged. Hence the number of admissible orientations between these two blocks is exactly
\[
2^{r+s-1}.
\]
This also covers \(r=1\) or \(s=1\), where the rectangle condition is vacuous.

Choices for distinct unordered pairs of blocks are independent. Therefore, for the fixed partition \(\pi\), the number of admissible digraphs is
\[
\prod_{1\le i<j\le k}2^{s_i+s_j-1}
=2^{\sum_{i<j}(s_i+s_j-1)}.
\]
Each block size \(s_i\) occurs in exactly \(k-1\) pairs, so
\[
\sum_{i<j}(s_i+s_j-1)=(k-1)n-\binom{k}{2}.
\]
Crucially, this depends only on \(n\) and the number \(k\) of non-adjacency classes, not on their sizes. Since there are \({n\brace k}\) set partitions of \([n]\) into \(k\) blocks, summing over \(k\) proves
\[
a_n=\sum_{k=1}^n {n\brace k}2^{(k-1)n-\binom{k}{2}}.
\]
Because \(M\) is universal for its finite age and ultrahomogeneous, two injective ordered tuples are in the same automorphism orbit exactly when the induced labeled digraphs on their positions are identical. Thus the labeled age count is the orbit count.

Putting \(k=n-j\) gives
\[
(k-1)n-\binom{k}{2}=\binom n2-\binom{j+1}{2},
\]
which yields the second displayed form.

For tuples with repetitions, first choose the equality partition of the \(n\) coordinate positions into \(r\) realized points, then choose an injective \(r\)-tuple orbit. This gives
\[
b_n=\sum_{r=0}^n {n\brace r}a_r.
\]

For the asymptotic estimate, write \(N=\binom n2\), \(L=\log_2 n\), and
\[
R_n=\frac{a_n}{2^N}=\sum_{j=0}^{n-1}{n\brace n-j}2^{-\binom{j+1}{2}}.
\]
Every partition of \([n]\) into \(n-j\) blocks has a canonical spanning forest with \(j\) edges, so
\[
{n\brace n-j}\le \binom Nj\le N^j.
\]
Hence
\[
R_n\le \sum_{j\ge0}2^{j\log_2N-j(j+1)/2},
\]
and completing the square shows
\[
\log_2R_n\le2L^2+O(L).
\]
For the reverse inequality, choose \(j=\lfloor2L\rfloor\) and count only partitions consisting of \(j\) disjoint pairs and \(n-2j\) singletons. Their number is
\[
\frac{n!}{(n-2j)!2^j j!}.
\]
Since \(j=O(\log n)\), its logarithm is \(2jL-O(j\log j)\). Multiplying by \(2^{-\binom{j+1}{2}}\) gives
\[
\log_2R_n\ge2L^2-O(L\log L).
\]
Together the bounds prove
\[
\log_2a_n=\binom n2+2L^2+O(L\log L).
\]

## Verification

The bundled checker uses restricted-growth strings to enumerate every set partition through six labeled vertices. For each partition it brute-forces every orientation of the cross-block pairs and tests the defining parity condition on every \(2\times2\) rectangle. It compares the resulting count, partition by partition, with
\[
2^{(k-1)n-\binom{k}{2}}.
\]
It then checks the Stirling formula, the \(j\)-layer rewrite, and the repetition Stirling transform. The direct brute-force totals through six vertices are
\[
1,3,21,313,9585,591841,
\]
and the script returns `VERIFY_OK`.

## Relationship to prior work

Kurilić--Kuzeljević supply a recent model-theoretic source in the assigned scope: they explicitly list the semigeneric parity digraph among countable ultrahomogeneous structures satisfying strong amalgamation. Earlier work of Coskey--Ellis gives a two-part structural lemma: between two maximal antichains, the orientation is determined by two subsets, which is equivalent to the row-plus-column binary-matrix form used above. That local structure is therefore prior.

The retained contribution is the global exact enumeration over all non-adjacency partitions, the simplification of the exponent to a function of the number of blocks alone, its interpretation as the exact ordered-tuple orbit profile, and the resulting profile asymptotic. Targeted web searches and published-finding corpus searches for semigeneric digraph enumeration, Stirling formulas, tuple orbits, parity matrices, and finite-age counts did not locate these statements.

The closest semantic-index result found concerns side-preserving reducts of the random bipartite graph, where orbit counts also reduce to binary matrices modulo row/column flips. It is structurally adjacent but concerns different groups and a different quotient problem.

## Limitations

The novelty claim is deliberately not attached to the local two-block factorization, which is already implicit in the literature. A specialized enumeration paper could contain the same global formula under Cherlin's older notation; targeted searches did not find one, so residual folklore risk remains.

The asymptotic estimate records the leading correction on the logarithmic scale, not a full saddle-point expansion. The verifier checks finite cases only; the all-\(n\) formulas are proved deductively above.

## References

1. Miloš S. Kurilić and Boriša Kuzeljević, “Positive families and Boolean chains of copies of ultrahomogeneous structures,” *Comptes Rendus Mathématique* 358 (2020), no. 7, 791–796. DOI: 10.5802/crmath.82. Published online 16 November 2020. 2020 MSC: 03C15, 03C50, 20M20, 06A06, 06A05.
2. Samuel Coskey and Paul Ellis, “The conjugacy problem for automorphism groups of homogeneous digraphs,” *Contributions to Discrete Mathematics* 12 (2017), no. 1, 62–73. DOI: 10.55016/ojs/cdm.v12i1.62551. Section 4 gives the semigeneric parity condition and its two-antichain structural lemma.
