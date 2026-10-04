# The Morse complex of \(K_{2,n}\) is a wedge of \(n^2-1\) \(n\)-spheres
## Finding
For every integer \(n\ge 1\), let \(K_{2,n}\) have bipartition \(\{u,v}\sqcup\{w_0,\ldots,w_{n-1}\}\). Then
\[
\mathcal M(K_{2,n})\simeq \bigvee^{n^2-1} S^n.
\]
For \(n=1\), the empty wedge means a point. Thus the first non-star complete-bipartite slice has a uniform exact homotopy type, not merely a connectivity bound.

## Assumptions and scope
The ordinary Morse complex \(\mathcal M(G)\) is the simplicial complex whose vertices are primitive discrete vector-field pairs \((x,e)\), with \(x\) a vertex incident to an edge \(e\), and whose simplices are collections of such pairs that use every cell at most once and contain no closed \(V\)-path.

Write
\[
A_i=(u,uw_i),\qquad B_i=(v,vw_i),\qquad X_i=(w_i,uw_i),\qquad Y_i=(w_i,vw_i).
\]
Equivalently, orient a selected matched edge away from its paired vertex. A face contains at most one \(A_i\), at most one \(B_j\), and at most one of \(X_k,Y_k\) for each \(k\). It cannot contain \(A_i,X_i\) or \(B_i,Y_i\). Because every simple cycle of \(K_{2,n}\) is a four-cycle, the only additional obstruction is
\[
\{A_i,Y_i,B_j,X_j}\qquad (i\ne j).
\]
These conditions are therefore necessary and sufficient for a face of \(\mathcal M(K_{2,n})\).

## Proof
Apply sequential element matchings to the augmented face poset, including the empty face, in the order
\[
X_0,A_0,Y_0,B_0,\ X_1,A_1,Y_1,B_1,\ \ldots,\ X_{n-1},A_{n-1},Y_{n-1},B_{n-1}.
\]
At a symbol \(q\), pair every still-unmatched face \(\sigma\) not containing \(q\) with \(\sigma\cup\{q}\) whenever both are still present. A sequence of element matchings is acyclic: each stage is an element matching on the remaining face poset after earlier stages, and the standard sequential-element-matching (cluster/patchwork) lemma makes the union acyclic.

It remains to identify the survivors. The following finite-state invariant gives an induction on the completed block index \(r\). Let \(a\) denote the index of the unique \(A\)-symbol when one is present and \(b\) the analogous \(B\)-index. Call an index past when it is at most \(r\), and future when it is larger than \(r\). On processed coordinates \(0,\ldots,r\), every surviving face has exactly one of the following patterns; unprocessed coordinates remain arbitrary subject to the face conditions above.

- If \(a\) is future and \(b\) is future or absent, every processed right state is \(Y\). If \(a\) is future and \(b=j\) is past, every processed state is \(Y\) except state \(j\), which is empty.
- If \(A\) is absent and \(b\) is future, every processed state is \(Y\). If \(A\) is absent and \(b=j\ge1\) is past, state \(j\) is \(X\) and all other processed states are \(Y\); no survivor has \(b=0\) in this case.
- If \(a=i\) is past and \(b\) is future, every processed state is \(Y\) except state \(i\), which is empty. If \(i\ge1\) and \(b=0\), every processed state is \(Y\) except state \(0\), which is empty.
- If \(a=i\ge1\) and \(b=j\ge1\) are past, then for \(j\le i\) every processed state is \(Y\) except state \(j\), which is empty; for \(j>i\), state \(j\) is \(X\), state \(i\) is empty, and every other processed state is \(Y\).
- If \(a=0\) is past, the only surviving possibility has \(b\) future, with state \(0\) empty and all other processed states equal to \(Y\). No survivor has a past \(A\)-index and absent \(B\).

For \(r=0\), this list follows immediately by applying the four toggles \(X_0,A_0,Y_0,B_0\) and the three face obstructions above. For the induction step, expose coordinate \(r+1\). The toggle \(X_{r+1}\) eliminates the two choices that differ only by \(X_{r+1}\) unless insertion is blocked by \(A_{r+1}\) or by the unique four-cycle obstruction; the subsequent \(A_{r+1}\), \(Y_{r+1}\), and \(B_{r+1}\) toggles do the same for their symbols. Splitting only according to whether \(a\) and \(b\) are past, future, or absent yields exactly the five rows above with \(r\) replaced by \(r+1\). Thus the invariant holds for all \(r\).

At \(r=n-1\) there are no future indices. The surviving augmented faces are therefore exactly the following.

First, for each \(1\le j\le n-1\),
\[
\{B_j,X_j}\cup\{Y_k:k\ne j}.
\]
Second, for each \(1\le i\le n-1\) and \(0\le j\le n-1\), there is one survivor:
\[
\begin{cases}
\{A_i,B_0}\cup\{Y_k:1\le k\le n-1},&j=0,\\
\{A_i,B_j}\cup\{Y_k:k\ne j},&1\le j\le i,\\
\{A_i,B_j,X_j}\cup\{Y_k:k\ne i,j},&i<j\le n-1.
\end{cases}
\]
There are \((n-1)+n(n-1)=n^2-1\) such faces, and each contains \(n+1\) vertices of the Morse complex, so each is an \(n\)-simplex.

The augmented matching also pairs the empty face once, with the vertex \(X_0\). Remove only that pair. Acyclicity is preserved, and on the ordinary nonempty face poset \(X_0\) becomes the unique critical \(0\)-simplex while the \(n^2-1\) survivors above are the only other critical cells. Discrete Morse theory therefore gives a CW complex with one \(0\)-cell and \(n^2-1\) cells of dimension \(n\), hence
\[
\mathcal M(K_{2,n})\simeq\bigvee^{n^2-1}S^n.
\]

## Verification
The included `verify_k2n_morse.py` independently enumerates all faces from the defining vector-field constraints, performs the stated element matching, compares the exact survivor set with the formulas above for \(1\le n\le7\), checks the Euler characteristic identity
\[
\chi(\mathcal M(K_{2,n}))=1+(-1)^n(n^2-1),
\]
and explicitly checks acyclicity of the resulting directed Hasse diagram for \(1\le n\le6\). It prints `VERIFY_OK`. These finite computations test the implementation and boundary cases; the theorem for all \(n\) rests on the induction above, not on extrapolation from the finite range.

## Relationship to prior work
Scoville and Zaremsky study Morse-complex connectivity and explicitly single out complete bipartite graphs \(K_{p,q}\) as examples whose Morse-complex homotopy type was, to their knowledge, not known; their complete-bipartite result supplies connectivity bounds rather than an exact homotopy type. Donovan and Scoville later compute exact Morse-complex homotopy types for paths and extended stars, including the star case \(K_{1,n}\), but not the two-left-vertex family treated here. The present result resolves the first non-star complete-bipartite slice \(K_{2,n}\) and gives both the sphere dimension and exact multiplicity.

## Limitations
The theorem concerns the ordinary Morse complex of \(K_{2,n}\). It does not determine \(\mathcal M(K_{p,q})\) for \(p\ge3\), generalized Morse complexes, pure Morse complexes, or attaching maps in unrelated graph families. The originality comparison is strongest against the named complete-bipartite discussion and later exact-family computations; an obscure equivalent computation under substantially different directed-tree terminology remains a residual bibliographic risk.

## References
1. N. A. Scoville and M. C. B. Zaremsky, “Higher connectivity of the Morse complex,” arXiv:2004.10481, first submitted 2020-04-22; later published in *Proceedings of the American Mathematical Society, Series B* 9 (2022), 135–149, DOI 10.1090/bproc/115.
2. C. Donovan and N. A. Scoville, “Star clusters in the Matching, Morse, and Generalized Morse complex,” arXiv:2207.13780, first submitted 2022-07-27; later published in *New York Journal of Mathematics* 29 (2023), 1393–1412.
3. D. N. Kozlov, “Complexes of directed trees,” *Journal of Combinatorial Theory, Series A* 88 (1999), 112–122.
