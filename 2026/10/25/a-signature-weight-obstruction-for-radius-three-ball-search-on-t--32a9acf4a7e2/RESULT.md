# A Signature-Weight Obstruction for Radius-Three Ball Search on the Eight-Cube

## Finding

Let \(Q_8=\{0,1\}^8\) with Hamming distance, and let \(M(Q_8,3)\) be the minimum number of nonadaptive queries of the form “is the unknown vertex in the radius-three ball centered at \(c\)?” needed to identify every vertex. Then

\[
M(Q_8,3)\ge 10.
\]

Thus neither eight nor nine radius-three balls can separate all 256 vertices of \(Q_8\). This is a lower bound only; it does not determine the exact value of \(M(Q_8,3)\).

## Assumptions and scope

A query center \(c\in Q_8\) returns the bit \(1\) exactly when \(d_H(x,c)\le 3\), where \(x\) is the unknown vertex. For a family of \(m\) centers \(c_1,\ldots,c_m\), its signature map is

\[
\sigma(x)=\bigl(\mathbf 1[d_H(x,c_j)\le 3]\bigr)_{j=1}^m.
\]

The family identifies every vertex if and only if \(\sigma\) is injective. Queries are nonadaptive and all have radius exactly three; variable-radius queries are outside this claim.

## Proof

Every radius-three ball in \(Q_8\) has size

\[
|B(c,3)|=\binom80+\binom81+\binom82+\binom83=1+8+28+56=93.
\]

If \(m\le 7\), injectivity is impossible because \(2^m<256\). If \(m=8\), an injective map from 256 vertices to \(\{0,1\}^8\) would be a bijection, so every signature coordinate would equal 1 on exactly 128 vertices. Each query coordinate is 1 on only 93 vertices, a contradiction.

Suppose \(m=9\) and \(\sigma\) is injective. Its image consists of 256 distinct nine-bit strings. Summing their Hamming weights by query coordinate gives

\[
\sum_{x\in Q_8}|\sigma(x)|=9\cdot93=837.
\]

There are exactly

\[
\sum_{k=0}^4\binom9k=1+9+36+84+126=256
\]

nine-bit strings of weight at most four, and their total weight is

\[
\sum_{k=0}^4 k\binom9k=9\sum_{k=0}^3\binom8k=9\cdot93=837.
\]

Among all sets of 256 distinct nine-bit strings, this is the unique minimum possible total weight: the 256 lowest-weight strings are precisely those of weight at most four. Equality therefore forces \(\sigma(Q_8)\) to be exactly that set.

Consequently, for any two distinct query coordinates \(i,j\), the number of signatures with both coordinates equal to 1 must be

\[
\sum_{k=0}^2\binom7k=1+7+21=29.
\]

Equivalently, every pair of query balls would have to intersect in exactly 29 vertices.

This is impossible. If two centers are at Hamming distance \(d\), their radius-three ball intersection has size

\[
I(d)=\sum_{a=0}^{d}\sum_{b=0}^{8-d}
\mathbf 1[a+b\le3\ \text{and}\ d-a+b\le3]
\binom da\binom{8-d}b.
\]

Splitting coordinates into the \(d\) positions where the centers differ and the \(8-d\) positions where they agree gives the following exact values:

| Center distance \(d\) | \(I(d)\) |
|---:|---:|
| 0 | 93 |
| 1 | 58 |
| 2 | 58 |
| 3 | 38 |
| 4 | 38 |
| 5 | 20 |
| 6 | 20 |
| 7 | 0 |
| 8 | 0 |

None equals 29, including the case of duplicate centers. This contradicts the forced pairwise intersection count. Therefore nine queries are impossible, and \(M(Q_8,3)\ge10\).

## Verification

The included standalone script recomputes the ball size, the signature weight counts, and every intersection value \(I(d)\) using integer binomial coefficients. Its assertions passed. The proof uses exact finite arithmetic, not a heuristic search. No construction with ten queries is established here, so the exact minimum remains unresolved by this result.

## Relationship to prior work

Kim, Kumbhat, Nagy, Patkós, Pokrovskiy, and Vizer define the nonadaptive ball-search parameter \(M(G,r)\) and give a seven-query radius-three construction for \(Q_7\), matching the information-theoretic lower bound in that dimension. The present statement concerns the adjacent dimension \(Q_8\) and a distinct lower-bound obstruction: an assumed nine-query identification would force all query-ball pair intersections to equal 29, which is incompatible with the Hamming-distance intersection profile above.

The broader identifying-code literature studies separating families in binary Hamming spaces, but coverage requirements and fixed-radius ball-query separation must not be conflated. This result asserts only a lower bound for the latter parameter.

## Limitations

The argument excludes query counts at most nine. It neither constructs a ten-query family nor proves that ten queries are impossible; therefore it does not determine \(M(Q_8,3)\). The literature review found no exact statement of this lower bound in the accessible material, but one related Hamming-space article was not inspected end-to-end, so an overlooked prior derivation remains a residual risk.

## References

1. Y. Kim, M. Kumbhat, Z. L. Nagy, B. Patkós, A. Pokrovskiy, and M. Vizer, “Identifying codes and searching with balls in graphs,” arXiv:1405.7508, first submitted 2014-05-29; published in *Discrete Applied Mathematics* 193 (2015), 39–47, DOI 10.1016/j.dam.2015.03.018.
2. “New identifying codes in the binary Hamming space,” arXiv:0804.3029, first submitted 2008-04-18; published in *European Journal of Combinatorics* 31 (2010), 491–501, DOI 10.1016/j.ejc.2009.03.032.
