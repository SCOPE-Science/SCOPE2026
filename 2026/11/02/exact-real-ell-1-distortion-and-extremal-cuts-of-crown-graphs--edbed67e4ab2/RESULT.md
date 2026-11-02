# Exact real \(\ell_1\) distortion and extremal cuts of crown graphs

## Finding

For an integer \(n\geq3\), let \(\operatorname{Cr}_n=K_{n,n}-M\) denote the simple unweighted crown graph, where \(M\) is a fixed perfect matching. Give its \(2n\) vertices their shortest-path metric \(d_n\). Let \(c_{\ell_1}(\operatorname{Cr}_n)\) be the smallest bilipschitz distortion of an embedding of this finite metric into a real \(\ell_1\) space of unrestricted dimension. With \(h=\lceil n/2\rceil\),

\[
\boxed{c_{\ell_1}(\operatorname{Cr}_n)=\frac{2(h-1)}h=2-\frac{2}{\lceil n/2\rceil}.}
\]

Thus the first two cases \(n=3,4\) are isometric, the values are constant in pairs \((2j-1,2j)\), and the values tend to \(2\). Every optimal embedding, after normalization to be noncontracting, has the following forced metric profile: all distinct vertices in either bipartition class have embedded distance \(2\), and every pair of opposite-class vertices not in the deleted matching has embedded distance \(2(h-1)/h\). All nonconstant positive-weight cuts in a cut decomposition of such an optimum attain equality in the sharp cut inequality in the proof.

## Assumptions and scope

Write the vertex classes as \(A=\{a_i:i\in[n]\}\) and \(B=\{b_i:i\in[n]\}\), where \(a_i b_j\) is an edge exactly when \(i\ne j\). All edges have weight \(1\); \(n\ge3\) ensures connectivity. For a map \(f\) into a real \(\ell_1\) space, its distortion is the product of its largest expansion ratio and largest contraction ratio, or equivalently the least \(D\ge1\) for which a positive rescaling satisfies \(d_n(u,v)\le\|f(u)-f(v)\|_1\le Dd_n(u,v)\) for all distinct vertices. The target dimension is not prescribed. A cut metric \(\delta_C\) is \(1\) across a cut and \(0\) within each shore. Every finite restriction of a real \(\ell_1\) metric is a finite nonnegative combination of cut metrics, by coordinate threshold decomposition; this elementary fact is used only on the \(2n\) vertices.

For \(i\ne j\), \(d_n(a_i,a_j)=d_n(b_i,b_j)=2\); for \(i\ne j\), \(d_n(a_i,b_j)=1\); and \(d_n(a_i,b_i)=3\). In particular, a missing matched edge has a three-step route via two other indices, and bipartiteness excludes any even-length route joining its endpoints.

## Proof

**Sharp inequality for an arbitrary cut.** For any cut, let \(x_i\in\{0,1\}\) and \(y_i\in\{0,1\}\) indicate the shore memberships of \(a_i\) and \(b_i\). Define \(k=\sum_i x_i\), \(\ell=\sum_i y_i\), and \(t=\sum_i x_i y_i\). Let \(S\) be the mean value of the cut metric on all \(n(n-1)\) unordered within-class vertex pairs in both classes, and \(U\) its mean on all \(n(n-1)\) *unmatched* cross-class pairs. Directly counting separated pairs gives

\[
S=\frac{k(n-k)+\ell(n-\ell)}{n(n-1)},\qquad
U=\frac{(n-1)(k+\ell)-2k\ell+2t}{n(n-1)}.
\]

Set \(v=k+\ell\), \(z=k-\ell\), and \(h=\lceil n/2\rceil\). Substitution and \(4k\ell=v^2-z^2\) yield the exact identity

\[
hn(n-1)\left(U-\frac{h-1}{h}S\right)
=(n-h)v-\frac{v^2}{2}+\left(h-\frac12\right)z^2+2ht.
\tag{1}
\]

Complementing a cut does not change its metric; hence assume \(0\le v\le n\). For \(n=2h\), the right side of (1) is

\[
\frac{v(n-v)+(n-1)z^2}{2}+2ht\ge0.
\]

For \(n=2h-1\), it becomes

\[
\frac{v(n-1-v)+nz^2}{2}+2ht.
\]

This is nonnegative if \(v\le n-1\). If \(v=n\), then \(z=k-\ell\) is an odd integer, so \(z^2\ge1\), and the expression remains nonnegative. Consequently, for every cut,

\[
\boxed{U\ge\frac{h-1}{h}S.}\tag{2}
\]

The equality cuts can also be classified directly from (1). Apart from constant zero cuts, for even \(n\) they satisfy \(v=n\), \(z=0\), and \(t=0\) after complementation. For odd \(n\), they satisfy either \(v=n\), \(|z|=1\), \(t=0\), or \(v=n-1\), \(z=0\), \(t=0\), after complementation. These alternatives give the exact support restriction asserted in the finding.

**Global lower bound.** If \(m\) is any \(\ell_1\) metric on the vertices, a nonnegative cut decomposition extends (2) linearly to its averaged distances. Rescale an arbitrary bilipschitz embedding so that \(d_n\le m\le Dd_n\). The within-class original distance is always \(2\), so \(S_m\ge2\). Every unmatched cross-class original distance is \(1\), so \(U_m\le D\). Inequality (2) therefore implies \(D\ge2(h-1)/h\).

**Matching explicit upper bound.** Put \(r=\lfloor n/2\rfloor\), \(N=\binom nr\), and \(W=2(2h-1)/h\). Index \(N\) real coordinates by the \(r\)-element subsets \(I\subset[n]\), and define

\[
f(a_i)_I=\frac WN\,\mathbf1_{\{i\in I\}},\qquad
f(b_i)_I=\frac WN\,\mathbf1_{\{i\notin I\}}.
\]

Each coordinate is a positively weighted cut metric. For two distinct indices, the proportion of subsets separating their two membership indicators is

\[
s=\frac{2r(n-r)}{n(n-1)}=\frac h{2h-1}.
\]

Thus the induced \(\ell_1\) metric is exactly

\[
\|f(a_i)-f(a_j)\|_1=\|f(b_i)-f(b_j)\|_1=Ws=2\quad(i\ne j),
\]
\[
\|f(a_i)-f(b_j)\|_1=W(1-s)=\frac{2(h-1)}h\quad(i\ne j),
\]
\[
\|f(a_i)-f(b_i)\|_1=W=\frac{2(2h-1)}h.
\]

For all \(h\ge2\), \(3\le W\le3\cdot2(h-1)/h\). Hence the embedding is noncontracting and never expands any original distance by more than \(2(h-1)/h\). Combined with the lower bound, this proves the exact formula for every integer \(n\ge3\).

**Rigidity for optimum metrics.** If the distortion equals the lower bound, then the chain \(D\ge U_m\ge(h-1)S_m/h\ge2(h-1)/h\) consists entirely of equalities. Every within-class embedded distance is at least \(2\), and their average equals \(2\); thus each equals \(2\). Every unmatched cross-class embedded distance is at most \(D\), and their average equals \(D\); thus each equals \(D\). Finally, the cut inequality is a nonnegative linear inequality; equality for a positive combination requires equality for every positive-weight constituent cut. The equality classification follows from (1). No rigidity is asserted for the matched cross-class embedded distances or for the coordinate dimension.

## Verification

The standalone Python 3 standard-library script `VERIFY.py` checks graph distances by breadth-first search for \(3\le n\le12\); enumerates every cut for \(3\le n\le8\) and checks inequality (2) and its stated equality cases by exact integers; and enumerates all balanced subsets for \(3\le n\le13\), verifying every induced pair distance and both bilipschitz bounds using exact rational arithmetic. Execute `python3 VERIFY.py` in the directory containing this file. A replay yielded `CHECK_OK 180380 exact integer/rational assertions for distances, cuts, equality cases, and embeddings, n<=13`. The infinite-parameter statement is proved by identity (1) and the explicit construction, not by extrapolating these finite tests.

## Relationship to prior work

The standard graph-metric \(\ell_1\) embedding and cut-cone setting appears in Gupta, Newman, Rabinovich and Sinclair, *Cuts, Trees and \(\ell_1\)-Embeddings of Graphs* (2004), and the 2017 preprint by Abraham, Filtser, Gupta and Neiman develops general shortest-path-decomposition embedding bounds. Their general bounds do not immediately imply the sharp fixed unweighted crown-graph staircase and equality-supported cut construction derived here.

Johnston, Kayll and Palmer (2022) explicitly study \(K_{n,n}\) with a matching removed, but their object is the *number of deranged perfect matchings*, not metric distortion. A separate result on the supremal negative-type exponent of crown-graph metrics concerns a different invariant: its qualitative non-isometry conclusion for larger crowns does not determine the sharp distortion values or cut profiles here. Exact cut-cone calculations for unrelated cubic-symmetric graphs likewise involve distinct finite objects.

Matoušek's 1996 paper discusses embeddings of finite metric spaces into normed spaces and is relevant to dimension-sensitive embeddings of crown graphs. Its full text was not available for the present comparison; the precise overlap risk under alternative notation remains unresolved and is not represented as excluded.

## Limitations

The theorem concerns only the unweighted shortest-path metric of \(K_{n,n}\) with a *full* perfect matching removed; it does not address other edge lengths, partial matching removal, arbitrary bipartite graphs, smallest target dimension, or the possible range of matched-pair distances among all optimal embeddings. Originality has received a qualified same mathematical model literature comparison rather than a complete historical-priority certification. No independent mathematical audit has been performed.

## References

1. I. Abraham, A. Filtser, A. Gupta and O. Neiman, *Metric Embedding via Shortest Path Decompositions*, arXiv:1708.04073v1, public August 14, 2017. https://arxiv.org/abs/1708.04073
2. A. Gupta, I. Newman, Y. Rabinovich and A. Sinclair, *Cuts, Trees and \(\ell_1\)-Embeddings of Graphs*, Combinatorica **24** (2004), 233–269. DOI:10.1007/s00493-004-0015-x. https://people.eecs.berkeley.edu/~sinclair/cuts.pdf
3. D. Johnston, P. M. Kayll and C. Palmer, *Deranged Matchings: Proofs and Conjectures*, arXiv:2209.11319v1, public September 22, 2022. https://arxiv.org/abs/2209.11319
4. J. Matoušek, *On the Distortion Required for Embedding Finite Metric Spaces into Normed Spaces*, Israel J. Math. **93** (1996), 333–344. DOI:10.1007/BF02761110 (full-text comparison unresolved).
