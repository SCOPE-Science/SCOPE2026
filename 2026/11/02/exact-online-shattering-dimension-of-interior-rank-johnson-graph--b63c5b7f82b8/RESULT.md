# Exact online shattering dimension of interior-rank Johnson graphs

## Finding
Let \(n,k\) be integers with \(3\le k\le n-3\). The Johnson graph \(J(n,k)\) has as vertices the \(k\)-subsets of \([n]\); two vertices are adjacent when their intersection has size \(k-1\). Let \(\mathcal N_{n,k}\) be the binary concept class whose possible centers are all vertices of \(J(n,k)\), and where the answer to the vertex query \(Q\) for center \(C\) is \(1\) if and only if \(|C\cap Q|=k-1\). Thus the concepts are open neighborhoods, not closed neighborhoods.

The exact Littlestone (complete adaptive-shattering tree) dimension is
\[
\operatorname{Ldim}(\mathcal N_{n,k})=
\begin{cases}
5,&\min(k,n-k)\ge4\ \text{and}\ \max(k,n-k)\ge6,\\
4,&\text{otherwise}.
\end{cases}
\]
In particular, the first interior-rank dimension-five instance up to rank-complement symmetry is \(J(10,4)\). Every induced subgraph of an arbitrary Johnson graph has open-neighborhood Littlestone dimension at most \(5\), and this global constant is sharp.

The previously established static VC dimension equals \(4\) throughout \(3\le k\le n-3\) [1]. Thus the theorem also gives the exact zero-or-one adaptive-minus-static gap throughout these ranks.

## Assumptions and scope
A complete binary Littlestone tree of depth \(d\) has a vertex query at each internal node, and for each binary path of length \(d\) at least one center realizes every answer on that path. The queries may depend on previous answers; repeating a query cannot allow both children to be nonempty. The dimension is the maximum such depth. Only finite simple Johnson graphs with the adjacency and the open-neighborhood convention above are considered. A graph induced by a subset of the vertices inherits adjacency, and its neighborhood class uses only its remaining centers and queries.

For \(3\le k\le n-3\), rank-complementation \(C\mapsto[n]\setminus C\) gives an isomorphism \(J(n,k)\cong J(n,n-k)\). The formula includes the boundary cases \(n=6\) and \((n,k)=(10,5)\); neither is inferred merely from nearby numerics.

## Proof
**1. Two positive queries.** Let \(U,V\) be distinct \(k\)-subsets queried positively along a branch. Possible centers lie in \(F=N(U)\cap N(V)\). Put \(r=k-|U\cap V|\). Since Johnson distance obeys the triangle inequality, \(F=\varnothing\) when \(r\ge3\). When \(r=2\), writing \(U=T\cup\{a,b\}\) and \(V=T\cup\{c,d\}\) with all four displayed elements distinct gives exactly the four centers \(T\cup\{a,c\},T\cup\{a,d\},T\cup\{b,c\},T\cup\{b,d\}\). Therefore \(\operatorname{Ldim}(F)\le2\) by its cardinality.

When \(r=1\), write \(U=S\cup\{a\}\), \(V=S\cup\{b\}\) with \(|S|=k-1\). The common centers form the disjoint union \(F=A\sqcup B\), where
\[
A=\{S\cup\{c\}:c\notin S\cup\{a,b\}\},\qquad
B=\{(S\setminus\{s\})\cup\{a,b\}:s\in S\}.
\]
Their sizes are \(|A|=n-k-1\), \(|B|=k-1\), so \(|F|=n-2\).

**2. The trace lemma.** For every possible query \(Q\), its positive trace on \(F\) is exactly one of the following: all of \(F\), \(A\setminus\{x\}\) for an \(x\in A\), \(B\setminus\{y\}\) for a \(y\in B\), or a set of at most two centers. Specifically, the first three cases occur when \(Q\in\{U,V\}\), \(Q\in A\), and \(Q\in B\), respectively.

To verify the remaining bound directly, put \(t=|Q\cap S|\) and \(h=|Q\cap\{a,b\}|\). Adjacency to an \(A\)-center \(S\cup\{c\}\) means \(t+\mathbf1_{c\in Q}=k-1\); adjacency to a \(B\)-center indexed by \(s\in S\) means \(t-\mathbf1_{s\in Q}+h=k-1\). If \(t=k-1\), the query is \(U\), \(V\), or a member of \(A\). If \(t=k-2\) and \(h=2\), the query is in \(B\); if \(h=0\) it neighbors at most two centers of \(A\) and none of \(B\); if \(h=1\) it neighbors at most one center of each. If \(t=k-3\), only \(h=2\) can yield neighbors, and then at most two belong to \(B\). If \(t<k-3\), it has no neighbors in \(F\). This proves the trace classification without using computation.

The query traces restricted to \(A\) alone (or to \(B\) alone) are therefore either the entire block, a co-singleton, or a subset of size at most two. No query in such a block can have both answer branches of Littlestone dimension at least \(2\): a co-singleton has a singleton negative branch, while a trace of size at most two has a small positive branch. Hence \(\operatorname{Ldim}(A)\le2\) and \(\operatorname{Ldim}(B)\le2\). On \(F\), every nontrivial query has a positive branch of size at most two or contained in \(A\) or \(B\). It follows that \(\operatorname{Ldim}(F)\le3\).

**3. Universal upper bound.** If a complete depth-\(6\) tree existed for the neighborhood class, follow its first two positive edges. Its two queries must be distinct, and their joint-positive family \(F\) would have to carry a complete depth-\(4\) subtree, contradicting Step 2. Therefore \(\operatorname{Ldim}(\mathcal N_{n,k})\le5\). The same bound for induced subgraphs follows by restriction of both query and center sets. For rank \(1\) the concept class consists of complements of singletons and has depth at most \(1\); the empty/full ranks are trivial. Thus the induced-subgraph corollary covers all ranks.

**4. The sharp upper bound four below the threshold.** If \(n\le9\), a common-neighbor family for distinct queries has at most \(n-2\le7\) members, hence Littlestone dimension at most \(2\). If \(n=10\) and \(k=5\), the only potentially larger family is the distance-one family \(A\sqcup B\) with \(|A|=|B|=4\). By Step 2 every nontrivial query has at most three positive centers, so no root can support a complete depth-\(3\) tree on \(F\). Thus \(\operatorname{Ldim}(F)\le2\) in these cases. Two successive positive edges of a hypothetical depth-\(5\) tree would demand a depth-\(3\) subtree on \(F\), a contradiction. Hence the dimension is at most \(4\) whenever the theorem's dimension-five condition fails, because in the stated interior-rank domain this failure is exactly \(\min(k,n-k)=3\) or \(n\le9\) or \((n,k)=(10,5)\). For \(\min(k,n-k)=3\) and arbitrarily large \(n\), the stronger bound also holds: then one block of every distance-one \(F\) has size two, so a query with positive trace in that block cannot support depth three, while a trace in the other block has a negative branch of size at most three; all other traces have size at most two. Consequently \(\operatorname{Ldim}(F)\le2\) and the global dimension is at most \(4\).

**5. Explicit matching lower bounds and embeddings.** The standalone file `johnson_adaptive_trees.json` gives complete labeled adaptive trees of depths \(4\) for \(J(6,3)\) and \(5\) for \(J(10,4)\), with one actual center witnessing each leaf. The self-contained `verify_johnson_online.py` checks all \(16\) and \(32\) leaf paths directly from the definition, with no assumption about the claimed formula.

Every interior-rank \(J(n,k)\) contains an induced copy of \(J(6,3)\): fix \(k-3\) elements, allow three additional elements to vary over six new elements, and exclude all other elements. Thus every case has dimension at least \(4\). Whenever \(k\ge4\) and \(n-k\ge6\), an analogous fixed-set embedding gives \(J(10,4)\) inside \(J(n,k)\). When \(k\ge6\) and \(n-k\ge4\), apply rank complementation first. These are precisely the parameter ranges \(\min(k,n-k)\ge4\) and \(\max(k,n-k)\ge6\), giving dimension at least \(5\). The upper and lower bounds agree for every asserted parameter pair.

## Verification
With Python 3 and the two supplied standalone artifacts in one directory, run `python verify_johnson_online.py johnson_adaptive_trees.json`. The checker independently constructs every \(k\)-subset, recomputes adjacency using intersection sizes, recursively checks every node and leaf in both certificates, verifies the certificates have \(2^d\) distinct witnesses, and computes exact finite dimensions by a memoized full-query recurrence. It additionally checks the common-neighbor trace lemma in representative cases and recomputes the claimed dimensions for all \(20\) interior-rank pairs with \(6\le n\le13\), identifying ranks up to complementation. The output is recorded in `verification_output.txt`. The all-order upper bounds and all-order embeddings are mathematical arguments above, not extrapolations from this finite test.

## Relationship to prior work
Adler, Benediktsson and Macpherson [1], first publicly available July 31, 2020, proved that open-neighborhood VC dimension on Johnson graphs is at most four and characterized its attainment, including the four-dimensional static threshold in \(J(6,3)\). Their full-text Johnson-graph section also computes the common-neighborhood cardinalities for pairs at distances one and two; these known geometric inputs are acknowledged. The paper determines static VC dimension and VC density, not an adaptive Littlestone formula or the sharp five-dimensional threshold. The numerical lower bound \(\operatorname{Ldim}\ge\operatorname{VCdim}\) does not decide the dimension-five cases. Earlier analysis of the triangular graphs \(J(n,2)\) likewise addresses a smaller rank and does not prove this interior-rank classification. The new components here are the trace-based online upper bound, the exceptional four-dimensional boundary, and the explicitly certified depth-five example propagated to all larger ranks.

## Limitations
The exact formula is asserted only for \(3\le k\le n-3\); outside this range only the universal upper bound is asserted here. Neither the finite checker nor unsuccessful literature searches prove historical originality, and no independent mathematical audit is claimed. In particular, priority under alternative model-theoretic terms for adaptive shattering remains an open literature-check risk. The argument concerns open, not closed, neighborhoods.

## References
[1] I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (first public version, 2020-07-31); *Discrete Applied Mathematics* 312 (2022), 29–44, doi:10.1016/j.dam.2021.09.017. Full relevant Johnson-graph section and Theorem 3.7 inspected.
