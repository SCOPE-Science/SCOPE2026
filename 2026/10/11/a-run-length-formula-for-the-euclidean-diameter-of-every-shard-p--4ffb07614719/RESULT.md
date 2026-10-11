# A run-length formula for the Euclidean diameter of every shard polytope
## Finding
Let
\[
\alpha=(a,b,A,B)
\]
be an arc in the sense of Padrol--Pilaud--Ritter. Encode each position in
\[
[a,b]
\]
by
\[
U
\quad\text{if it lies in }\{a\}\cup A,
\qquad
D
\quad\text{if it lies in }B\cup\{b\}.
\]
Because \(a\) is a \(U\)-position and \(b\) is a \(D\)-position, the word has a unique run decomposition
\[
U^{p_1}D^{q_1}\cdots U^{p_f}D^{q_f},
\qquad
p_i,q_i\ge1.
\tag{1}
\]
Thus \(f\) is exactly the number of \(\alpha\)-falls.

From the alternating run word
\[
U_1D_1\cdots U_fD_f
\]
form the **spare-run word**
\[
\sigma_\alpha
\]
by retaining \(U_i\) exactly when
\[
p_i\ge2,
\]
and retaining \(D_i\) exactly when
\[
q_i\ge2.
\]
Let \(g(\alpha)\) be the largest \(g\) for which \(\sigma_\alpha\) has a subsequence
\[
U<D<U<D<\cdots<U<D
\]
of length \(2g\). Equivalently, scan \(\sigma_\alpha\) from left to right: retain the first available \(U\), match it to the next available \(D\), and repeat. The number of completed pairs is \(g(\alpha)\).

Then the Euclidean diameter of the shard polytope is
\[
\boxed{
\operatorname{diam}\bigl(\mathrm{SP}(\alpha)\bigr)
=
\sqrt{2\bigl(f+g(\alpha)\bigr)}.
}
\tag{2}
\]

The distinguished zero vertex has eccentricity
\[
\boxed{
\max_{v\in\operatorname{vert}\mathrm{SP}(\alpha)}
\|v\|_2
=
\sqrt{2f}.
}
\tag{3}
\]
Exactly
\[
\boxed{
\prod_{i=1}^f p_iq_i
}
\tag{4}
\]
vertices attain the distance in (3).

In particular,
\[
\boxed{
\sqrt{2f}
\le
\operatorname{diam}\bigl(\mathrm{SP}(\alpha)\bigr)
\le
2\sqrt f.
}
\tag{5}
\]
The upper equality holds if and only if
\[
p_i\ge2
\quad\text{and}\quad
q_i\ge2
\qquad
(1\le i\le f).
\tag{6}
\]
The lower equality holds if and only if
\[
g(\alpha)=0,
\]
equivalently no spare \(U_i\) occurs weakly before a spare \(D_j\).

A notable consequence of (2) is that, once the number of runs is fixed, the diameter depends on each run length only through the dichotomy
\[
1
\quad\text{versus}\quad
\ge2.
\]

## Assumptions and scope
The shard polytope is the standard type-\(A\) shard polytope
\[
\mathrm{SP}(\alpha)
=
\operatorname{conv}
\{\chi(M):M\text{ is an }\alpha\text{-alternating matching}\}
\]
in the standard coordinate realization of the cited source. The metric is ordinary Euclidean distance restricted to its affine span.

An \(\alpha\)-alternating matching is allowed to be empty. Its characteristic vector has a \(+1\) at each selected \(U\)-position, a \(-1\) at each selected \(D\)-position, and zero elsewhere.

The result concerns the ordinary Euclidean diameter, not the graph diameter of the one-skeleton.

## Proof
By the published vertex description, every vertex is
\[
\chi(M)
\]
for an \(\alpha\)-alternating matching
\[
M=\{a_1,b_1,\ldots,a_k,b_k\},
\qquad
a_1<b_1<\cdots<a_k<b_k.
\tag{7}
\]
A matching can use at most one coordinate from any maximal \(U\)-run or \(D\)-run.

For two vertices
\[
x=\chi(M),
\qquad
y=\chi(N),
\]
a coordinate has a fixed sign whenever it is nonzero: \(U\)-coordinates are in \(\{0,1\}\) and \(D\)-coordinates are in \(\{0,-1\}\). Therefore
\[
\|x-y\|_2^2
=
|\operatorname{supp}(x)\mathbin{\triangle}\operatorname{supp}(y)|.
\tag{8}
\]
Thus Euclidean squared distance is exactly the Hamming distance between the two selected coordinate sets.

It remains to maximize (8). Process the run word from left to right and record how many of the two matchings are currently **open**, meaning that they have selected a \(U\) since their most recent selected \(D\). There are only three symmetric states:
\[
0,\quad1,\quad2.
\]
For each run, the two matchings may either skip it or select one coordinate there, subject to their alternating condition.

For a singleton \(U\)-run, the max-plus transition table is
\[
T_U^{(1)}
=
\begin{pmatrix}
0&1&0\\
-\infty&0&1\\
-\infty&-\infty&0
\end{pmatrix},
\tag{9}
\]
where rows are incoming states \(0,1,2\), columns are outgoing states, and entries are the Hamming rewards. The \(0\to2\) reward is \(0\), because both matchings must use the same unique coordinate.

For a \(U\)-run of length at least two,
\[
T_U^{(2)}
=
\begin{pmatrix}
0&1&2\\
-\infty&0&1\\
-\infty&-\infty&0
\end{pmatrix}.
\tag{10}
\]
Now two newly opened matchings can use distinct coordinates and contribute reward \(2\).

The \(D\)-run tables are the reverse analogues:
\[
T_D^{(1)}
=
\begin{pmatrix}
0&-\infty&-\infty\\
1&0&-\infty\\
0&1&0
\end{pmatrix},
\qquad
T_D^{(2)}
=
\begin{pmatrix}
0&-\infty&-\infty\\
1&0&-\infty\\
2&1&0
\end{pmatrix}.
\tag{11}
\]
The diameter squared is the maximum reward of a path beginning in state \(0\) before the first run and ending in state \(0\) after the last run.

The tables show immediately why only the conditions
\[
p_i=1\text{ or }p_i\ge2,
\qquad
q_i=1\text{ or }q_i\ge2
\]
matter.

To solve the three-state dynamic program, scan the spare-run word greedily. After the first \(i\) pairs of runs, let
\[
g_i
\]
be the number of completed spare \(U\)-\(D\) pairs, and let
\[
h_i\in\{0,1\}
\]
record whether one unmatched spare \(U\) is pending. Thus a spare \(U_i\) creates a pending symbol when none is present, and a spare \(D_i\) closes a pending symbol and increases \(g_i\) by one.

Let
\[
(A_i,B_i,C_i)
\]
be the maximum rewards after the \(i\)-th \(D\)-run in states \(0,1,2\). Direct max-plus multiplication of (9)--(11) gives, for every \(i\ge1\),
\[
A_i=2i+2g_i,
\tag{12}
\]
\[
B_i=A_i+2h_i-1,
\tag{13}
\]
and
\[
C_i=A_i+2h_i-2.
\tag{14}
\]
For \(i=1\), these identities are checked from the four possibilities
\[
(p_1=1\text{ or }\ge2)
\times
(q_1=1\text{ or }\ge2).
\]
For the induction step, substitute (12)--(14) into the corresponding \(U\)-table and then the \(D\)-table. The four singleton/spare choices update \(g_i,h_i\) exactly by the greedy rule above, and the displayed forms are preserved.

At the end, both matchings must be closed, so the required maximum is
\[
A_f=2f+2g_f.
\]
Since
\[
g_f=g(\alpha),
\]
equation (8) proves (2).

For (3), if \(M\) has \(k\) pairs then
\[
\|\chi(M)\|_2^2=2k.
\tag{15}
\]
An alternating matching uses at most one coordinate from each of the \(f\) \(U\)-runs and each of the \(f\) \(D\)-runs, so
\[
k\le f.
\]
Choosing one coordinate from every run gives the valid alternating matching
\[
U_1,D_1,\ldots,U_f,D_f,
\]
so equality is attainable. This proves (3).

A matching has \(f\) pairs if and only if it chooses exactly one coordinate from every run. There are independently
\[
p_i
\]
choices in \(U_i\) and
\[
q_i
\]
choices in \(D_i\), proving (4).

Finally,
\[
0\le g(\alpha)\le f
\]
gives (5). Equality
\[
g(\alpha)=f
\]
requires and is implied by retaining every one of the \(2f\) run symbols in \(\sigma_\alpha\), which is exactly condition (6).

Because a Euclidean diameter of a polytope can be attained at a pair of vertices, the vertex calculation above is the diameter of the full polytope, not merely of its vertex set.

## Verification
The proof is arbitrary-dimensional and does not infer an infinite statement from finite enumeration.

The source-dependent premise was checked directly in the full text: shard-polytope vertices are exactly the characteristic vectors of possibly empty alternating matchings, with \(+1\) entries on \(\{a\}\cup A\) and \(-1\) entries on \(B\cup\{b\}\).

The accompanying `verify.py` exhaustively checks every \(U/D\) arc word of length \(2\) through \(10\) that begins in \(U\) and ends in \(D\). It enumerates every alternating matching, computes every pairwise Euclidean squared distance directly from the characteristic vectors, and compares the resulting diameter with (2). It also checks the zero-vertex eccentricity and the farthest-vertex count (4). These finite checks are corroborative only.

## Relationship to prior work
Padrol, Pilaud, and Ritter introduce shard polytopes as elementary Minkowski summands for quotientopes. Their Definition 39 gives alternating matchings, including the empty matching, and their Proposition 40 identifies the shard polytope with the convex hull of the corresponding characteristic vectors. The same section develops facet descriptions, dimensions, faces, symmetries, normal fans, matroid interpretations, and Minkowski geometry.

The inspected full text contains no occurrence of “diameter”, “circumradius”, or “inradius”. Targeted searches for Euclidean diameter, Hamming distance between shard vertices, alternating-matching maximum distance, and series-parallel-matroid diameter did not locate a statement implying (2).

Ferroni, Morales, and Panova later prove Ehrhart positivity for all shard polytopes through their relation with fence-poset order polynomials. Their inspected full text is enumerative and contains no occurrence of “diameter”, “distance”, or “Euclidean”.

The present theorem uses the original vertex model in a different direction: it turns the alternating-matching encoding into an exact Euclidean metric invariant. The result is not a graph-distance statement and is not implied by the source's face or normal-fan descriptions.

## Limitations
The formula is specific to the standard coordinate realization of type-\(A\) shard polytopes. It does not claim an affine-invariant diameter, a type-\(B\) formula, or a diameter formula for arbitrary Minkowski sums of shard polytopes.

The spare statistic \(g(\alpha)\) has a linear-time greedy computation, but no claim is made that it is the only useful metric statistic of an arc.

A residual originality risk remains that the same metric observation appears under the series-parallel matroid translation or another terminology not surfaced by the searches. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Arnau Padrol, Vincent Pilaud, and Julian Ritter, *Shard Polytopes*, arXiv:2007.01008, first public version 2020-07-02; International Mathematics Research Notices 2023(9), 7686--7796, DOI 10.1093/imrn/rnac042.
2. Luis Ferroni, Alejandro H. Morales, and Greta Panova, *Skew Shapes, Ehrhart Positivity and Beyond*, arXiv:2503.16403.
