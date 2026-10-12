# Complete abelian-subalgebra census for biclique graph Lie algebras

## Finding

Let \(K\) be any field, let \(a,b\geq1\), and let \(U\), \(W\) be vector spaces over \(K\) of dimensions \(a\), \(b\). Put \(Z=U\otimes_K W\) and form the two-step nilpotent Lie algebra
\[
 L_{a,b}(K)=U\oplus W\oplus Z,\qquad
 [(u,w,z),(u',w',z')]=(0,0,u\otimes w'-u'\otimes w).
\]
This is the edge-distinct graph Lie algebra of the complete bipartite graph \(K_{a,b}\). Here “abelian subalgebra” means a linear subspace with identically zero bracket, including the zero subalgebra.

**Classification.** Every abelian subalgebra \(H\) is specified uniquely by a triple \((T,C,f)\): \(T\) is a bracket-vanishing linear subspace of \(U\oplus W\); \(C\leq Z\); and \(f:T\to Z/C\) is linear. The subalgebra is the inverse image, inside \(T\oplus Z\), of the graph of \(f\) in \(T\oplus(Z/C)\). Moreover, the complete list of possible \(T\) is:

- an arbitrary linear subspace of \(U\), including zero;
- a nonzero linear subspace of \(W\); or
- a line \(K(u,w)\) with both \(u\ne0\) and \(w\ne0\).

The zero subspace appears just once, and the last type is disjoint from the first two. These statements hold in all characteristics, including characteristic two.

For every prime power \(q\), let \(\mathcal A_{a,b,q}(X)=\sum_{H}X^{\dim H}\), summing over all embedded abelian Lie subalgebras of \(L_{a,b}(\mathbf F_q)\). Write \({n\brack k}_q\) for the Gaussian binomial coefficient, defined as zero when \(k<0\) or \(k>n\), put \(h=ab\), and set
\[
 B_t(X)=\sum_{j=0}^{h}{h\brack j}_q q^{t(h-j)}X^{t+j},
 \qquad M_{a,b}(q)=\frac{(q^a-1)(q^b-1)}{q-1}.
\]
Then the **complete dimension enumerator**, without restrictions on \(a,b,q\), is
\[
 \boxed{\mathcal A_{a,b,q}(X)=B_0(X)
  +\sum_{t=1}^{a}{a\brack t}_q B_t(X)
  +\sum_{t=1}^{b}{b\brack t}_q B_t(X)
  +M_{a,b}(q)B_1(X).}
\]

The maximal abelian subalgebras **by inclusion** are precisely \(Z\oplus U\), \(Z\oplus W\), and \(Z\oplus K(u,w)\) for every line \(K(u,w)\) with nonzero \(U\)- and \(W\)-components. They number
\[
 \boxed{2+\frac{(q^a-1)(q^b-1)}{q-1}},
\]
and their respective dimensions are \(h+a\), \(h+b\), and \(h+1\). In contrast, the maximum possible abelian dimension is \(h+\max(a,b)\). For \(a,b\ge2\), there are many inclusion-maximal abelian subalgebras strictly smaller than those of maximum dimension; the gap is unbounded as \(\max(a,b)\) grows. All inclusion-maximal abelian subalgebras happen to be Lie ideals because they contain \(Z=[L_{a,b},L_{a,b}]\).

## Assumptions and scope

Only \(a,b\ge1\), finite dimensionality, and the displayed bracket are assumed. Over arbitrary fields the classification and dimension statements hold. The numerical polynomial and cardinalities require \(K=\mathbf F_q\) for a prime power \(q\). The central summand \(Z\) has dimension \(ab\); the entire algebra has dimension \(a+b+ab\). Subalgebras are counted as distinct embedded linear subspaces, not modulo automorphisms. “Maximal” always means inclusion-maximal unless explicitly stated as maximum-dimensional. The bracket is alternating also in characteristic two, and the Jacobi identity is automatic because its image is central.

## Proof

**1. Centralizer rigidity.** Let \(x=(u,w)\in U\oplus W\) have both components nonzero. If \(y=(u',w')\) commutes with \(x\), then \(u\otimes w'=u'\otimes w\). Choose a functional \(\lambda\in U^*\) satisfying \(\lambda(u)=1\). Applying \(\lambda\otimes\operatorname{id}_W\) gives \(w'=\lambda(u')w\). Inserting this in the tensor equality gives \((u'-\lambda(u')u)\otimes w=0\); since \(w\ne0\), we conclude \(u'=\lambda(u')u\). Thus the centralizer of \(x\) **inside \(U\oplus W\)** is exactly \(Kx\). No characteristic or algebraic-closure assumption was used.

**2. Classification of horizontal bracket-vanishing spaces.** If \(T\le U\oplus W\) is bracket-vanishing and contains a mixed vector \(x\) as above, centralizer rigidity forces \(T\le Kx\), so \(T=Kx\). If no such mixed vector occurs, every vector of \(T\) belongs to \(U\cup W\). Since no nonzero element of \(U\) commutes with a nonzero element of \(W\), the entire \(T\) lies in one summand. Conversely, any subspace of \(U\), any subspace of \(W\), and every mixed line has zero internal bracket. This is exhaustive, without counting a zero subspace twice.

**3. Lifts across the center.** For any abelian subalgebra \(H\le L\), let \(T\) be its image in \(L/Z=U\oplus W\) and \(C=H\cap Z\). The quotient \(H/C\) projects isomorphically to \(T\), so it is uniquely a graph of a linear map \(f:T\to Z/C\). Conversely, the inverse image of that graph inside \(T\oplus Z\) has dimension \(\dim T+\dim C\) and is abelian because \([T,T]=0\). If \(\dim T=t\), \(\dim C=j\), there are exactly \(q^{t(h-j)}\) such maps. This proves the stated one-to-one parametrization.

**4. Finite-field enumeration.** For each \(j\), the number of possible \(j\)-subspaces \(C\le Z\) is \({h\brack j}_q\). A prescribed horizontal subspace of dimension \(t\) therefore contributes \(B_t(X)\). The numbers of nonzero \(t\)-subspaces inside \(U\), resp. \(W\), are \({a\brack t}_q\), resp. \({b\brack t}_q\). Mixed one-dimensional subspaces correspond to simultaneous scalar orbits on \((U\setminus0)\times(W\setminus0)\); each orbit has \(q-1\) elements, giving \(M_{a,b}(q)\) mixed lines. Summing the disjoint cases proves the entire polynomial coefficient by coefficient.

**5. Inclusion-maximality.** Adding all of \(Z\) to any abelian subalgebra preserves abelianity, so every maximal one contains \(Z\). An abelian subspace \(T\le U\oplus W\) is maximal by inclusion exactly when it is \(U\), \(W\), or a mixed line, by step 2 and centralizer rigidity. Their lifts containing \(Z\) are unique. This proves the classification, cardinalities, dimensions, and the difference between inclusion-maximal and maximum-dimensional examples. Since \([L,L]=Z\), any subspace containing \(Z\) is automatically an ideal.

## Verification

The standalone script `verify.py` independently enumerates **every** row-reduced echelon subspace of the full \(\mathbf F_q\)-Lie algebra and checks that every pair of its basis vectors commutes. It compares dimension-by-dimension totals against the closed formula for \((a,b,q)=(1,1,2),(1,1,3),(1,1,5),(1,2,2),(1,2,3),(2,2,2)\). It separately enumerates horizontal abelian subspaces and tests pairwise containment to identify inclusion-maximal ones, reproducing the stated number and dimension distribution. Row-reduced enumeration totals were also checked against Gaussian coefficients, including all dimensions of \(\mathbf F_2^8\).

Observed counts by dimension: for \((a,b,q)=(1,2,2)\), \([1,31,59,19,1,0]\) with maximal-abelian dimensions \(3\) (four subalgebras) and \(4\) (one subalgebra); for \((2,2,2)\), \([1,255,2347,4035,1571,135,2,0,0]\) with nine inclusion-maximal abelian subalgebras of dimension \(5\) and two of dimension \(6\). The checker terminates with `VERIFY_OK`. These finite enumerations test the formulas but are **not** a substitute for the proof for arbitrary \(a,b,q\).

## Relationship to prior work

Godoy Molina and Lagos, arXiv:2308.00272, introduce graph-induced ideals and subalgebras for labeled graph Lie algebras and analyze graded derivations of the complete-bipartite family with distinct edge labels. Their identified graph-ideal constructions are not an enumeration of every linear abelian subalgebra, including arbitrary lifts across central subspaces. DeCoste, DeMeyer, Mainkar, and Ray, arXiv:2208.09541, study *abelian factors*, i.e., central direct-summand phenomena, a different notion from embedded abelian subalgebras. Rossmann's graphical-group enumeration concerns conjugacy-class sizes rather than the present Grassmannian incidence counts.

The 2025 work of Aldi, Gabrielsen, Grandini, Harris, and Kelley, arXiv:2504.19836, supplies general bounds and a connection between independence numbers and the **maximum dimension** of abelian subalgebras. For \(K_{a,b}\), the maximum-dimensional statement is therefore not claimed as new in isolation. Its independence polynomial counts vertex subsets, not the noncoordinate linear subspaces and their central lifts counted here. The broader 2024 study of Fernández Ouaridi, Navarro, and Towers, arXiv:2405.05859, addresses general maximum dimensions but not this distribution. Related exact counts of ideals, or of commutator images, do not imply the count of nonideal abelian subalgebras without extra structural classification.

## Limitations

The theorem concerns the edge-distinct complete-bipartite graph Lie algebra; repeated edge labels, arbitrary graphs, and nonabelian subalgebras are not classified. An equivalently formulated finite-field abelian-subspace census might exist under geometric or group-theoretic terminology not captured by the checked literature. The result does not prove a classification of graph Lie algebras up to isomorphism, nor does the finite checker verify infinite families. Inclusion-maximal and maximum-dimensional are distinct here and are not interchangeable.

## References

1. M. Godoy Molina and D. Lagos, *Lie algebras associated with labeled directed graphs*, arXiv:2308.00272v1 (first public version 1 August 2023), especially Sections 3 and 5; https://arxiv.org/abs/2308.00272.
2. R. DeCoste, L. DeMeyer, M. Mainkar and A. Ray, *Abelian Factor in 2-step Nilpotent Lie Algebras Constructed from Graphs*, arXiv:2208.09541v1 (19 August 2022); https://arxiv.org/abs/2208.09541.
3. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, *Bulletin of the London Mathematical Society* (2022), DOI:10.1112/blms.12665; https://doi.org/10.1112/blms.12665.
4. M. Aldi, T. Gabrielsen, D. Grandini, J. Harris and K. Kelley, *Independence Polynomials of 2-step Nilpotent Lie Algebras*, arXiv:2504.19836v1 (28 April 2025); https://arxiv.org/abs/2504.19836.
5. A. Fernández Ouaridi, R. M. Navarro and D. A. Towers, *Abelian Subalgebras and Ideals of Maximal Dimension in Poisson algebras*, arXiv:2405.05859v1 (9 May 2024); https://arxiv.org/abs/2405.05859.
6. Niranjan and S. Rani, *Image of Lie polynomial of degree 2 evaluated on Nilpotent Lie algebra*, arXiv:2204.13050v1 (27 April 2022); https://arxiv.org/abs/2204.13050.
