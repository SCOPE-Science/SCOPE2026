# Inverse-distance braid-wall law for tree associahedra

## Finding

Let \(T\) be any labelled tree on \(V=[n]\), where \(n\geq2\). For every nonempty vertex set \(S\subseteq V\) inducing a connected subtree, let \(\Delta_S=\operatorname{conv}\{e_v:v\in S\}\). Fix strictly positive real coefficients \(\lambda_S>0\) and set
\[
P(T,\lambda)=\sum_{\varnothing\neq S\subseteq V:\,T[S]\text{ connected}}\lambda_S\Delta_S.
\]
The standard graph associahedron is the case \(\lambda_S=1\). For each permutation \(\pi=(\pi_1,\ldots,\pi_n)\), in *decreasing objective-coordinate order*, let \(v_T(\pi)\) be the unique vertex exposed by a generic linear objective with that ordering. If \(\pi'\) is obtained by interchanging two consecutive entries \(u,v\) of \(\pi\), call that braid-wall edge **surviving** when \(v_T(\pi)\neq v_T(\pi')\).

**Inverse-distance theorem.** For every unordered pair of distinct labels \(\{u,v\}\), exactly
\[
N_T(u,v)=\frac{(n-1)!}{\operatorname{dist}_T(u,v)}
\]
undirected edges of the \(n\)-label permutohedron exchanging \(u,v\) survive the coarsening to the normal fan of \(P(T,\lambda)\). There are \((n-1)!\) such permutohedron edges before coarsening, hence the conditional survival fraction is exactly \(1/\operatorname{dist}_T(u,v)\). This statement holds **simultaneously for all strictly positive coefficients** \(\lambda_S\).

It follows that the complete labelled survival table reconstructs the tree metric by
\[
\operatorname{dist}_T(u,v)=\frac{(n-1)!}{N_T(u,v)},
\]
and therefore reconstructs \(T\) (its edges are precisely the pairs having survival fraction one). In particular, if \(H(T)=\sum_{u<v}\operatorname{dist}_T(u,v)^{-1}\) is the Harary index, the number of surviving permutohedron edges is exactly
\[
E_{\mathrm{surv}}(T)=(n-1)!\,H(T),
\]
and their fraction among all \(n!(n-1)/2\) permutohedron edges is
\[
Q(T)=\frac{2H(T)}{n(n-1)}.
\]

For the path \(P_n\) and the star \(S_n\), respectively,
\[
Q(P_n)=\frac{2[nH_{n-1}-(n-1)]}{n(n-1)}\sim\frac{2\log n}{n},
\qquad
Q(S_n)=\frac{n+2}{2n}\longrightarrow\frac12,
\]
where \(H_k=\sum_{j=1}^k1/j\) denotes the harmonic number. Thus the average local braid-chamber sensitivity vanishes on long paths but stays macroscopically positive for stars.

## Assumptions and scope

The graph \(T\) is a finite *simple, connected, acyclic, labelled* graph on at least two vertices. Every connected-set simplex occurs with a strictly positive weight; these weights need not be equal or rational. Ambient coordinate labels and the braid fan are fixed. A generic objective has strictly ordered coordinates. Edges of the permutohedron are indexed by **adjacent entries in the objective-order list**, not by arbitrary swaps of labels. Only the criterion of whether two adjacent chambers expose different vertices is counted: no claim is made that distinct surviving braid edges yield distinct edges of the quotient polytope.

## Proof

**Step 1: exact adjacent-chamber comparison.** For a permutation \(\pi\), each simplex \(\Delta_S\) uniquely exposes \(e_{a(S,\pi)}\), where \(a(S,\pi)\) is the first element of \(S\) in the order \(\pi\). Consequently,
\[
v_T(\pi)=\sum_{S\text{ connected}}\lambda_S e_{a(S,\pi)}.
\]
Suppose \(u=\pi_k\), \(v=\pi_{k+1}\), and \(A=\{\pi_1,\ldots,\pi_{k-1}\}\). The only summands affected by swapping \(u,v\) are connected sets \(S\) that contain both of them and avoid \(A\). Every such summand shifts from \(\lambda_Se_u\) to \(\lambda_Se_v\); all other summands remain fixed. With the orientation chosen from \(\pi\) to \(\pi'\),
\[
v_T(\pi)-v_T(\pi')=\left(\sum_{\substack{S\text{ connected}:\\\{u,v\}\subseteq S,\;S\cap A=\varnothing}}\lambda_S\right)(e_u-e_v).
\]
Because each \(\lambda_S>0\), cancellation cannot occur. The two exposed vertices differ if and only if at least one such set exists.

**Step 2: specialize to a tree.** Let \(R_T(u,v)\) denote the unique vertex set of the simple path between \(u\) and \(v\). Every connected vertex set containing both endpoints includes all of \(R_T(u,v)\); the path vertex set itself is connected. Hence the condition in Step 1 is equivalent to
\[
A\cap\bigl(R_T(u,v)\setminus\{u,v\}\bigr)=\varnothing.
\]
If \(d=\operatorname{dist}_T(u,v)\), precisely \(d-1\) internal path vertices must follow the adjacent \(u,v\) block in the objective order.

**Step 3: exact edge count.** Fix distinct labels \(u,v\). Regard adjacent \(u,v\) as a single block, which may be internally oriented in two ways. After contracting this block, the order is a uniformly varying permutation of \(n-1\) objects. There are \((n-1)!\) undirected permutohedron edges exchanging \(u,v\), because the two orientations represent the two endpoints of each edge. Among these \(n-1\) objects, exactly \(d\) distinguished objects consist of the block and the \(d-1\) internal path vertices. In precisely a fraction \(1/d\) of all block permutations the block precedes the other \(d-1\) distinguished objects. By Step 2 these and only these edges survive. Thus \(N_T(u,v)=(n-1)!/d\) for every pair and every choice of positive weights.

**Step 4: recovery, totals and examples.** All counts are positive; knowledge of the labelled integer \(N_T(u,v)\) recovers the positive integer distance \(d\). Distance-one pairs recover all tree edges. Summing Step 3 over unordered label pairs gives \((n-1)!H(T)\); division by \(n!(n-1)/2\) gives \(Q(T)\). A path has \(n-d\) unordered vertex pairs at distance \(d\), so its Harary index is \(\sum_{d=1}^{n-1}(n-d)/d=nH_{n-1}-(n-1)\). A star has \(n-1\) pairs at distance one and \(\binom{n-1}{2}\) at distance two, so its Harary index is \((n-1)(n+2)/4\). The displayed formulas follow; the path asymptotic uses \(H_{n-1}=\log n+O(1)\).

## Verification

The accompanying standalone `checker.py` enumerates **actual exposed vertices of the connected-subset Minkowski sum**, rather than substituting the path-survival criterion into the code. It independently enumerates connected vertex subsets, the full objective-order permutation set, and undirected adjacent-swap edges; compares the exposed vertices; and computes all graph distances by breadth-first search. Exact integer counts are compared with the rational inverse-distance formula for all \(145\) labelled trees of orders \(2\) through \(5\), together with six selected labelled trees of orders \(6\) and \(7\). All \(151\) tests pass. The checker uses no external packages. Its finite coverage corroborates, but does not replace, the proof for arbitrary \(n\).

Reproduce using `python3 checker.py` from the directory containing the files. This is a proof by a finite symmetry argument for every tree order, not an inference from experiments.

## Relationship to prior work

The generalized-permutahedron realization by connected-subset simplex sums, the normal-fan coarsening, and the map from permutations to maximal tubings are established. Pilaud, Santos and Ziegler's 2023 survey presents the connected-tube Minkowski sum explicitly; Barnard and McConville study the canonical permutation-to-tubing projection; Cardinal, Merino and Mütze study permutation orders and elimination trees; Albertin, Pilaud and Ritter analyze weak-order quotient fans and braid wall crossings. These sources supply geometry and projection context, **not an identified formula** for the number of surviving walls classified by a swapped label pair or the tree-distance reconstruction formula. The Harary index is an established graph invariant; its appearance here as a fan-wall survival sum is the asserted connection. No claim is made that these background constructions or the Harary index themselves are new.

## Limitations

The inverse-distance law depends essentially on the uniqueness of paths in trees; it does not assert the same formula for graphs containing cycles. The weights must be strictly positive: removing a tube can collapse additional walls. Metric recovery requires the fixed coordinate labels and the distribution of counts across label pairs; the unlabelled total alone need not reconstruct a tree. Surviving braid edges are not identified with distinct graph-associahedron edges. Searches of accessible mathematical records and primary literature found no covering theorem, but terminology variations and unindexed prior publications remain a bibliographic risk. Independent mathematical audit has not been performed.

## References

- E. Barnard and T. McConville, *Lattices from graph associahedra and subalgebras of the Malvenuto–Reutenauer algebra*, first public arXiv posting 2018-08-16, arXiv:1808.05670, https://arxiv.org/abs/1808.05670 .
- V. Pilaud, F. Santos and G. M. Ziegler, *Celebrating Loday's Associahedron*, first public arXiv posting 2023-05-15, arXiv:2305.08471, https://arxiv.org/abs/2305.08471 , especially Section 4.1.
- J. Cardinal, A. Merino and T. Mütze, *Combinatorial generation via permutation languages. IV. Elimination trees*, first public arXiv posting 2021-06-30, arXiv:2106.16204, https://arxiv.org/abs/2106.16204 .
- D. Albertin, V. Pilaud and J. Ritter, *Removahedral congruences versus permutree congruences*, first public arXiv posting 2020-05-30, arXiv:2006.00264, https://arxiv.org/abs/2006.00264 .
