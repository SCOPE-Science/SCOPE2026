# A nine-vertex counterexample to KC-monotonicity of random greedy independent sets

## Finding

Let \(G\) be a finite simple graph. Process its vertices in a uniformly random order, accepting a vertex exactly when no previously accepted vertex is adjacent to it. Write \(M(G)\) for the expected size of the resulting maximal independent set.

**Theorem (sharp first KC reversal).** On vertices \(\{0,1,\ldots,8\}\), let \(T\) and \(U\) be the trees with the following edge sets:

\[
\begin{aligned}
E(T)&=\{01,05,12,23,24,56,67,68\},\\
E(U)&=\{01,05,12,16,23,24,67,68\}.
\end{aligned}
\]

Here \(ij\) denotes the undirected edge \(\{i,j\}\). The tree \(U\) is obtained from \(T\) by a **proper KC-transformation**: take the bare path \(1-0-5\) and move the off-path edge \(56\) from endpoint \(5\) to endpoint \(1\). Nevertheless,

\[
M(T)=\frac{73}{15},\qquad M(U)=\frac{34}{7},\qquad
M(U)-M(T)=-\frac{1}{105}<0.
\]

No tree on at most eight vertices has a proper KC-transformation that decreases \(M\). Thus nine is the smallest order at which monotonicity of expected random greedy independent-set size under proper KC-transformations fails.

## Assumptions and scope

A KC-transformation is defined on a tree \(G\) by choosing distinct vertices \(x,y\) joined by a *bare path*: all internal vertices of the path have degree two. If \(z\) is the neighbor of \(y\) on that path, replace each edge \(yw\), where \(w\in N_G(y)\setminus\{z\}\), by \(xw\). The transformation is proper when both endpoints have degree at least two, so the transformed tree has exactly one more leaf. For unordered bare paths the transformations in the two directions are isomorphic (as in the cited definition).

The vertex order is uniform over all \(|V(G)|!\) permutations; no edges are weighted. The statistic is the **expected cardinality** of the first random greedy independent set, not the number of maximal independent sets, the independence number, or the expected number of vertices in the first two greedy coloring classes.

## Proof

**1. Exact first-arrival identity.** For every \(S\subseteq V(G)\), define \(m_G(S)\) as the expected random greedy independent-set size in the induced graph \(G[S]\), with \(m_G(\varnothing)=0\). Conditioning on the first vertex \(v\) of the uniform order gives

\[
m_G(S)=1+\frac{1}{|S|}\sum_{v\in S}m_G\bigl(S\setminus N_{G[S]}[v]\bigr)
\qquad(S\ne\varnothing).
\]

Indeed, the first vertex is accepted, all its neighbors can never be accepted, and the restriction of the original uniform permutation to the remaining vertices is again uniform. This recursively determines exact rational expectations for every induced subgraph; no random sampling is involved.

**2. The explicit proper shift.** In \(T\), the vertices on \(1-0-5\) have degrees \(2,2,2\); its only internal vertex \(0\) has degree two. The only neighbor of \(5\) off that path is \(6\). Replacing \(56\) by \(16\) therefore gives precisely \(U\), increasing the number of leaves from four to five.

**3. Exact expectations.** For \(v=0,\ldots,8\) in order, the nine contributions \(1+m_T(V(T)\setminus N_T[v])\) in the first-arrival identity are

\[
\left(\frac{13}{3},\frac{11}{2},\frac{56}{15},\frac{21}{4},
\frac{21}{4},\frac{11}{2},\frac{56}{15},\frac{21}{4},\frac{21}{4}\right),
\]

whose sum is \(219/5\). The corresponding contributions for \(U\) are

\[
\left(\frac{13}{3},6,\frac{11}{3},\frac{21}{4},\frac{21}{4},
\frac{106}{21},\frac{11}{3},\frac{21}{4},\frac{21}{4}\right),
\]

whose sum is \(306/7\). Dividing each sum by nine yields \(M(T)=73/15\) and \(M(U)=34/7\), hence the stated strict reversal.

As a separate direct check, exhaustive evaluation of all \(9!=362880\) vertex orders gives the following numbers of orders by selected-set cardinality:

| Cardinality | For \(T\) | For \(U\) |
|---:|---:|---:|
| 3 | 25984 | 35200 |
| 4 | 139776 | 127680 |
| 5 | 53760 | 53760 |
| 6 | 143360 | 146240 |

Each column sums to \(362880\), and its weighted mean independently gives the claimed fraction.

**4. Minimality.** Every labeled tree on \(n\ge2\) vertices is represented by a unique Prüfer sequence of length \(n-2\). For each \(1\le n\le8\), enumerate these sequences, retain one representative of each unrooted isomorphism type using the lexicographically smallest recursively sorted rooted-tree encoding, and examine every bare path with nonleaf endpoints. Apply the exact first-arrival identity to both trees of every proper KC-transform pair. The exhaustive counts are:

| Order | Unlabeled trees | Proper KC paths checked | Smallest increase |
|---:|---:|---:|---:|
| 1 | 1 | 0 | — |
| 2 | 1 | 0 | — |
| 3 | 1 | 0 | — |
| 4 | 2 | 1 | \(1/2\) |
| 5 | 3 | 4 | \(4/15\) |
| 6 | 6 | 13 | \(1/9\) |
| 7 | 11 | 35 | \(2/105\) |
| 8 | 23 | 93 | \(1/480\) |

All tested increases are strictly positive. The Prüfer bijection establishes exhaustiveness of tree inputs; the rooted encoding is an isomorphism invariant complete for trees, and every possible nonleaf-endpoint bare path is tested. Reversing a KC path gives an isomorphic output, so one orientation per unordered pair suffices. The complete, standard-library-only verification is in `verify.py`, which also checks the independent direct permutation counts above. This proves the sharp lower order boundary. \(\square\)

## Verification

Run `python3 verify.py` with Python 3.10 or newer. The script uses only the standard library (`fractions`, `functools`, `itertools`, and `collections`). It prints `VERIFY_OK` after recomputing the first-arrival fractions, all proper KC comparisons through eight vertices, and direct permutation histograms of both nine-vertex witnesses. It does not use numerical tolerances, Monte Carlo simulation, a precomputed tree list, or unlisted external files.

## Relationship to prior work

Krivelevich, Mészáros, Michaeli, and Shikhelman prove that paths minimize the expected random greedy independent-set size among trees. In Section 8.1 they define KC-transformations, and Section 9 explicitly suggests that the expected greedy independence ratio may increase strictly under every proper such transformation. Their Theorem 8.3 instead proves monotonicity of an auxiliary quantity \(\nu\); it does **not** prove this conjectured monotonicity of \(M\). The nine-vertex pair above refutes only that stronger, conjectural local monotonicity. It does **not** refute their proved path-minimization theorem or the monotonicity of \(\nu\). The first public version of the motivating paper appeared on July 16, 2019; the inspected full journal text appeared online December 18, 2023.

The source's separate open question about the *first two* greedy color classes concerns a different random variable; a failure of the two-class assertion would not imply the present nine-vertex first-class KC reversal. Searches for the exact nine-vertex shift, expected-set-size implications, tree shifts, and the alternate KC/Kelmans terminology did not identify this particular obstruction; absence from searches does not establish complete historical priority.

## Limitations

The result proves a sharp **finite minimal counterexample** for uniform random-order greedy maximal independent sets on finite unweighted trees. It does not determine the full set of exceptional KC transformations at larger orders, provide an infinite counterfamily, disprove global path minimality, or address other random greedy coloring statistics. Historical novelty is based on accessible full text, indexed mathematical records, and targeted literature queries, not an independent priority certification.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli, and C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216 (first submitted July 16, 2019); *Random Structures & Algorithms* 64 (2024), 986–1015, DOI: 10.1002/rsa.21200. Sections 8.1 and 9.
2. P. Csikvári, *On a poset of trees*, *Combinatorica* 30 (2010), 125–137. Cited for the original tree-shift construction, not for a greedy-probability inequality.
3. B. Bollobás and M. Tyomkyn, *Walks and paths in trees*, *Journal of Graph Theory* 70 (2012), 54–66. Related KC-transform context; concerns walk/path counts, not the statistic proved here.
