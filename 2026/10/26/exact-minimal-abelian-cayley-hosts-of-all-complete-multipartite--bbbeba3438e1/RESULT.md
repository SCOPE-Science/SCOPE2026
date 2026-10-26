# Exact minimal abelian Cayley hosts of all complete multipartite graphs
## Finding
Let \(t\ge2\) and \(m_1,\ldots,m_t\ge1\) be integers, and set \(M=\max_i m_i\). For the complete multipartite graph \(G=K_{m_1,\ldots,m_t}\),
\[
\boxed{\eta(G)=tM.}
\]
Every optimal host is moreover *forced to be balanced complete multipartite*: if an induced embedding exists in \(\operatorname{Cay}(\Gamma,S)\) with \(|\Gamma|=tM\), then a subgroup \(H\le\Gamma\) of order \(M\) satisfies \(S=\Gamma\setminus H\). The \(t\) graph parts occupy pairwise distinct cosets of \(H\); any part of size \(M\) fills its coset. Conversely this coset construction realizes every admissible tuple in a cyclic group of order \(tM\).

## Assumptions and scope
All graphs are finite, simple, undirected. An abelian Cayley graph has a finite abelian group \(\Gamma\), written additively, and a symmetric connection set \(S=-S\subseteq\Gamma\setminus\{0\}\). An induced embedding is an injection of graph vertices into \(\Gamma\) preserving edges *and* nonedges. The invariant \(\eta(G)\) minimizes \(|\Gamma|\) over all finite abelian groups and all such connection sets, not only cyclic groups or connection sets of units. All \(t\) part sizes are positive. The one-part edgeless case is excluded.

## Proof
**Lower bound.** Consider any induced labeling in a finite abelian group \(\Gamma\). Choose a largest part and denote its set of labels by \(A\), so \(|A|=M\). Choose one label \(z_i\) from each of the other \(t-1\) parts. Define
\[
X_0=A-A,\qquad X_i=z_i-A\quad(1\le i<t).
\]
A translate \(A-a\) for any \(a\in A\) lies in \(X_0\), so \(|X_0|\ge M\); each \(X_i\) has exactly \(M\) elements. We prove these \(t\) sets are pairwise disjoint.

If \(z_i-a\in X_0\), then it is a difference across an edge between different parts, whereas the same difference in \(A-A\), if nonzero, arises from a nonedge between two distinct vertices of the large part. This is impossible for an induced labeling. Here \(z_i-a\ne0\) because labels of distinct vertices are distinct, so the zero difference in \(X_0\) causes no exception. If \(z_i-a=z_j-b\) for distinct \(i,j\), then \(z_i-z_j=a-b\). The left side corresponds to an edge between representatives of distinct parts and is nonzero. The right side corresponds to a nonedge inside \(A\) (necessarily \(a\ne b\)), again impossible. Hence
\[
|\Gamma|\ge\left|\bigcup_{i=0}^{t-1}X_i\right|=\sum_{i=0}^{t-1}|X_i|\ge tM.
\]

**Upper bound.** Take \(\Gamma=\mathbb Z/(tM)\mathbb Z\) and its subgroup \(H=t\mathbb Z/(tM)\mathbb Z\), which has \(M\) elements and index \(t\). Set \(S=\Gamma\setminus H\). Its Cayley graph joins exactly the pairs in different \(H\)-cosets, so it is \(K_{M,\ldots,M}\). Place the \(i\)-th part in any \(m_i\) elements of the \(i\)-th coset. This yields an induced copy of \(G\) and an upper bound \(tM\).

**Rigidity at equality.** Now suppose \(|\Gamma|=tM\). Equality in the disjoint packing implies \(|A-A|=M\). Fix \(a_0\in A\) and let \(H=A-A\). Because \(A-a\subseteq H\) has \(M\) elements for every \(a\in A\), in fact \(A-a=H\) for every \(a\in A\). Thus \(A=a_0+H\). For each \(h=a-a_0\in H\), we have \(H-h=A-a=H\), proving that \(H\) is a subgroup: it contains zero and is invariant under subtraction of each of its elements. Also \(|H|=M\).

The sets \(X_i=z_i-A\) for \(i\ge1\) are distinct \(H\)-cosets and, with \(X_0=H\), partition all of \(\Gamma\). Every nonzero element of \(H=A-A\) is forbidden from the connection set because it is a nonedge difference; every element in \(X_i\) with \(i\ge1\) is an edge difference and belongs to \(S\). Hence \(S=\Gamma\setminus H\). Every vertex \(b\) in the same graph part as a representative \(z_i\) satisfies \(b-z_i\notin S\); therefore \(b-z_i\in H\), so that part lies wholly in \(z_i+H\). The large part is \(A=a_0+H\); the other parts lie in the other distinct cosets. This proves all rigidity assertions.

## Verification
A standalone Python 3 verifier `verify.py` exactly checks the cyclic construction and the \(t\)-set packing for all 456 nondecreasing part-size tuples with \(2\le t\le6\) and \(1\le m_i\le5\). It checks 55,420 unordered vertex pairs in these constructions. It additionally enumerates all normalized candidate induced labelings in every finite abelian group type of order below the predicted minimum in three small test families, totaling 19 group-type cases and 55,944 candidate labelings; no counterexample exists. Run `python3 verify.py`, with no third-party dependencies, to reproduce `verify_output.txt`. These finite checks are corroborative only; the proof above establishes the unrestricted statement.

## Relationship to prior work
Fokam Souop and Bitjoka, *Induced Embeddings of Graphs into Abelian Cayley Graphs* (2026), Definition 1 and Remark 12, introduce the invariant in the per-graph minimum-host form, prove \(\eta(K_{a,b})=2\max\{a,b\}\) and give only \(\eta(K_{m_1,\ldots,m_t})\le tM\) for general complete multipartite graphs. They explicitly identify the unbalanced case as open, with \(K_{1,1,5}\) singled out; the present disjoint-difference packing turns their construction into an equality for *all* positive part tuples. A separately published result, *Exact abelian Cayley host order for the unbalanced family \(K_{1,1,n}\)*, already proves the subfamily \(\eta(K_{1,1,n})=3n\) using three disjoint sets. That subfamily is **not** claimed as new; the full arbitrary-number-of-parts, arbitrary-part-size formula and optimal-host rigidity are the contributions here.

The older representation-number work of Akhtar, Evans and Pritikin addresses induced embeddings only in cyclic Cayley graphs with the connection set fixed to the unit residues. That is a strictly constrained invariant and does not imply a minimal order or rigidity for arbitrary abelian Cayley hosts. Babai and Sós provide the classical induced-difference criterion and general embeddings, not this exact multipartite minimal-host statement.

## Limitations
The result concerns complete multipartite graphs with at least two nonempty parts, **induced** embeddings, and finite **abelian** Cayley hosts. It does not give a formula for arbitrary graphs, isometric embedding orders, or minimum Cayley hosts subject to an externally fixed connection set. The optimal-host classification is graph-theoretic and does not classify the abstract abelian group structures or all injections into optimal hosts beyond the forced coset condition. The closely related one-family result is prior work, and searches cannot establish absolute publication priority; unindexed equivalent results remain a risk. Independent validation has not been performed.

## References
1. Rigobert Fokam Souop and Laurent Bitjoka, “Induced Embeddings of Graphs into Abelian Cayley Graphs,” arXiv:2609.01486, first publicly posted 2026-09-01, especially Definition 1, Theorem 11 and Remark 12; https://arxiv.org/abs/2609.01486.
2. “Exact abelian Cayley host order for the unbalanced family \(K_{1,1,n}\),” publicly indexed mathematical research record, 2026-10-04; https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-abelian-cayley-host-order-for-the-unbalanced-family-k-1-1--ef2188721b72.
3. Reza Akhtar, Anthony B. Evans and Dan Pritikin, “Representation numbers of complete multipartite graphs,” Discrete Mathematics 312 (2012), 1158–1165, doi:10.1016/j.disc.2011.12.003.
4. László Babai and Vera T. Sós, “Sidon sets in groups and induced subgraphs of Cayley graphs,” European Journal of Combinatorics 6 (1985), 101–114.
