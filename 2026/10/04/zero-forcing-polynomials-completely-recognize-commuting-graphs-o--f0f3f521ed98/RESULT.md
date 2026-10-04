# Zero forcing polynomials completely recognize commuting graphs of finite AC-groups

## Finding

Let \(G\) be a finite nonabelian AC-group, meaning that \(C_G(g)\) is abelian for every \(g\notin Z(G)\), and let \(\Gamma_c(G)\) be its commuting graph on \(G\setminus Z(G)\). Let \(X_1,\ldots,X_t\) be the distinct sets \(C_G(g)\setminus Z(G)\) and put \(m_i=|X_i|\). If \(J=\{i:m_i\ge2\}\) and \(N=\sum_i m_i\), then \[\mathcal Z(\Gamma_c(G);x)=x^{N-|J|}\prod_{i\in J}(x+m_i),\qquad Z(\Gamma_c(G))=M(\Gamma_c(G))=N-|J|,\qquad \operatorname{mr}(\Gamma_c(G))=|J|.\] Every minimum zero forcing set contains every singleton centralizer component and omits exactly one vertex from each nontrivial centralizer component, so their number is \(\prod_{i\in J}m_i\). Moreover the zero forcing polynomial determines the entire multiset \(\{m_1,\ldots,m_t\}\); consequently, for finite nonabelian AC-groups \(G,H\), \[\mathcal Z(\Gamma_c(G);x)=\mathcal Z(\Gamma_c(H);x)\iff \Gamma_c(G)\cong\Gamma_c(H).\]

Thus a graph polynomial that is not a complete invariant on arbitrary graphs becomes a complete isomorphism invariant on the commuting graphs of finite nonabelian AC-groups. The same factorization also gives exact real symmetric minimum rank and maximum nullity.

## Assumptions and scope

Let \(G\) be a finite nonabelian group. Its commuting graph \(\Gamma_c(G)\) has vertex set
\[
G\setminus Z(G),
\]
and distinct vertices are adjacent exactly when they commute.

An AC-group is a group in which
\[
C_G(g)
\]
is abelian for every noncentral element \(g\).

For the zero forcing polynomial, write
\[
\mathcal Z(\Gamma;x)=\sum_{k=0}^{|V(\Gamma)|}z(\Gamma;k)x^k,
\]
where \(z(\Gamma;k)\) counts the zero forcing sets of size \(k\).

For real symmetric graph minimum rank, let \(\mathcal S(\Gamma)\) be the set of real symmetric matrices whose off-diagonal nonzero pattern is exactly \(\Gamma\), and define
\[
\operatorname{mr}(\Gamma)=\min_{A\in\mathcal S(\Gamma)}\operatorname{rank}A,
\qquad
M(\Gamma)=|V(\Gamma)|-\operatorname{mr}(\Gamma).
\]

## Proof

Das and Nongsiang prove that if \(G\) is a finite nonabelian AC-group, then the sets
\[
X=C_G(u)\setminus Z(G),
\qquad
u\in G\setminus Z(G),
\]
form the clique-block decomposition of the commuting graph. In particular, after removing duplicate centralizers,
\[
\Gamma_c(G)\cong \bigsqcup_{i=1}^{t}K_{m_i},
\qquad
m_i=|X_i|.
\tag{1}
\]

We derive all claimed consequences directly from (1).

For a singleton component,
\[
\mathcal Z(K_1;x)=x,
\]
because its unique isolated vertex must be initially blue. For \(m\ge2\),
\[
\mathcal Z(K_m;x)=m x^{m-1}+x^m
=
x^{m-1}(m+x).
\tag{2}
\]
Indeed, a set in \(K_m\) is zero forcing exactly when it omits at most one vertex.

A set zero-forces a disjoint union exactly when its intersection with every connected component zero-forces that component. Hence the zero forcing polynomial is multiplicative over the components in (1). Let
\[
J=\{i:m_i\ge2\},
\qquad
N=\sum_{i=1}^{t}m_i.
\]
Multiplying (2) and the singleton factors gives
\[
\mathcal Z(\Gamma_c(G);x)
=
x^{N-|J|}
\prod_{i\in J}(m_i+x).
\tag{3}
\]

The least exponent in (3) is therefore
\[
Z(\Gamma_c(G))=N-|J|.
\]
Moreover, a minimum zero forcing set is forced componentwise: every singleton component must be included, while in every nontrivial clique exactly one vertex is omitted. Thus the minimum zero forcing sets are exactly those described in the finding, and their number is
\[
\prod_{i\in J}m_i.
\]

Now consider minimum rank. Because the graph is a disjoint union, every matrix in
\[
\mathcal S(\Gamma_c(G))
\]
is block diagonal with one block for each clique component. A singleton \(K_1\) has minimum rank \(0\), since its \(1\times1\) block may be zero. A clique \(K_m\) with \(m\ge2\) has minimum rank \(1\): rank \(0\) is impossible because its off-diagonal entries must be nonzero, while the all-ones matrix has rank \(1\) and the correct pattern. Hence
\[
\operatorname{mr}(\Gamma_c(G))=|J|.
\]
Consequently
\[
M(\Gamma_c(G))
=
N-|J|
=
Z(\Gamma_c(G)).
\]

Finally, the polynomial determines the clique-size multiset. After factoring out its largest power of \(x\), all remaining roots are negative integers, and their absolute values, with multiplicity, are precisely the values
\[
m_i\ge2.
\]
The total degree gives \(N\), so the number of singleton components is
\[
N-\sum_{i\in J}m_i.
\]
Thus \(\mathcal Z(\Gamma_c(G);x)\) recovers the full multiset
\[
\{m_1,\ldots,m_t\}.
\]
A disjoint union of cliques is determined up to graph isomorphism by that multiset, proving
\[
\mathcal Z(\Gamma_c(G);x)
=
\mathcal Z(\Gamma_c(H);x)
\quad\Longleftrightarrow\quad
\Gamma_c(G)\cong\Gamma_c(H)
\]
for finite nonabelian AC-groups \(G,H\).

## Verification

The accompanying `verify.py` constructs five groups directly from their multiplication laws:
\[
S_3,\quad D_8,\quad D_{10},\quad D_{12},\quad Q_8.
\]
For every noncentral element it computes the full centralizer and checks the AC condition. It then verifies that the distinct sets \(C_G(g)\setminus Z(G)\) partition the noncentral elements into clique components.

For each resulting commuting graph, every vertex subset is exhaustively tested for the zero forcing property. The exact polynomial is compared with (3), including the minimum-set count. The verifier also builds the block all-ones minimum-rank witness and computes its rank exactly over rational arithmetic.

Exact replay output:

```text
S3: profile=[1, 1, 1, 2], |V|=5, Z=M=4, mr=1, min_sets=2, polynomial={4: 2, 5: 1}
D8: profile=[2, 2, 2], |V|=6, Z=M=3, mr=3, min_sets=8, polynomial={3: 8, 4: 12, 5: 6, 6: 1}
D10: profile=[1, 1, 1, 1, 1, 4], |V|=9, Z=M=8, mr=1, min_sets=4, polynomial={8: 4, 9: 1}
D12: profile=[2, 2, 2, 4], |V|=10, Z=M=6, mr=4, min_sets=32, polynomial={6: 32, 7: 56, 8: 36, 9: 10, 10: 1}
Q8: profile=[2, 2, 2], |V|=6, Z=M=3, mr=3, min_sets=8, polynomial={3: 8, 4: 12, 5: 6, 6: 1}
VERIFY_OK
```

The computations are finite corroboration only. The general theorem is proved by the AC centralizer decomposition and the componentwise arguments above.

## Relationship to prior work

Das and Nongsiang give the key algebraic structure: for a finite nonabelian AC-group, the commuting graph decomposes into cliques indexed by distinct noncentral centralizers. Their paper uses this decomposition to compute graph genus and then specializes it to dihedral, generalized quaternion, semidihedral, order-\(pq\), order-\(p^3\), \(PSL(2,2^k)\), and \(GL(2,q)\) families. It does not discuss zero forcing, maximum nullity, or graph minimum rank.

Boyer and collaborators introduced the zero forcing polynomial and explicitly study multiplicativity, uniqueness, and closed forms for graph families. That generic multiplicativity is prior coverage and is not claimed here. The new algebraic statement is that, on the AC-group commuting-graph class, the polynomial factors by noncentral centralizer sizes and becomes a complete commuting-graph isomorphism invariant.

The standard minimum-rank framework for zero forcing predates both papers. Here the equality \(M=Z\) is proved directly from the clique-block decomposition rather than inferred only from the general zero forcing bound.

## Limitations

The theorem requires the AC condition. General commuting graphs need not be disjoint unions of cliques, so neither the factorization nor polynomial recognizability extends automatically.

The polynomial determines the multiset
\[
|C_G(g)|-|Z(G)|
\]
for distinct noncentral centralizers. It does not, in general, determine the group itself, the center size separately, or the individual centralizer orders without additional group information.

The complete-invariant assertion is only for the commuting graphs within this AC-group class; the zero forcing polynomial is not a complete invariant for arbitrary graphs.

The minimum rank is over real symmetric matrices.

## References

1. A. K. Das and D. Nongsiang, “On the genus of the commuting graphs of finite non-abelian groups,” arXiv:1311.6342, first posted 25 November 2013; later published in *International Electronic Journal of Algebra* 19 (2016), 91–109.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910, first posted 26 January 2018; *Discrete Applied Mathematics* 258 (2019), 35–48. DOI: 10.1016/j.dam.2018.11.033.
3. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
