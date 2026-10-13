# All \(k\)-metric generators of path-barbell graphs
## Finding
For integers \(p,q\ge3\) and \(\ell\ge1\), form \(B_{p,q}^{(\ell)}\) from disjoint cliques \(K_p\) and \(K_q\). Choose \(a\in V(K_p)\) and \(b\in V(K_q)\), and join \(a\) to \(b\) by a path of length \(\ell\), with all internal path vertices new. Write
\[
X=V(K_p)\setminus\{a\},\qquad Y=V(K_q)\setminus\{b\},
\]
and write the path vertices in order as \(c_0=a,c_1,\ldots,c_\ell=b\).

For an integer \(k\ge1\), a set \(S\subseteq V(B_{p,q}^{(\ell)})\) is a \(k\)-metric generator when every two distinct vertices are distinguished by at least \(k\) vertices of \(S\), where a landmark \(s\) distinguishes \(u,v\) when \(d(s,u)\ne d(s,v)\). Then:

1. \(S\) is a 1-metric generator if and only if \(|X\setminus S|\le1\) and \(|Y\setminus S|\le1\).
2. \(S\) is a 2-metric generator if and only if \(X\cup Y\subseteq S\).
3. No \(k\)-metric generator exists for any \(k\ge3\).

Define the all-set enumerator
\[
\mathcal R_k(G;x)=\sum_{S\text{ a }k\text{-metric generator}}x^{|S|}.
\]
Then
\[
\mathcal R_1(B_{p,q}^{(\ell)};x)
=x^{p+q-4}(x+p-1)(x+q-1)(1+x)^{\ell+1},
\]
\[
\mathcal R_2(B_{p,q}^{(\ell)};x)
=x^{p+q-2}(1+x)^{\ell+1},
\]
and \(\mathcal R_k(B_{p,q}^{(\ell)};x)=0\) for \(k\ge3\). Hence
\[
\dim_1(B_{p,q}^{(\ell)})=p+q-4,
\qquad
\dim_2(B_{p,q}^{(\ell)})=p+q-2.
\]
There are exactly \((p-1)(q-1)\) metric bases and exactly one 2-metric basis, namely \(X\cup Y\).

## Assumptions and scope
Graphs are finite, simple, connected, and unweighted. The parameters satisfy \(p,q\ge3\) and \(\ell\ge1\). The path of length \(\ell\) includes its two clique attachment vertices, so the graph has \(p+q+\ell-1\) vertices. The endpoint cases \(p=2\) or \(q=2\) are excluded because the multiplicity arguments using at least two landmarks in each non-attachment clique class change there.

The term “path-barbell” is descriptive: the graph is defined explicitly above, independently of naming conventions. The one-edge symmetric specialization \(p=q=n\), \(\ell=1\) is the usual barbell consisting of two \(K_n\)'s joined by a bridge.

## Proof
For \(x,x'\in X\) with \(x\ne x'\), every vertex outside \(\{x,x'\}\) has equal distance to \(x\) and \(x'\). Thus the complete set of vertices distinguishing \(x\) from \(x'\) is exactly \(\{x,x'\}\). The same statement holds for every distinct pair in \(Y\). It follows immediately that no \(k\)-metric generator can exist for \(k\ge3\).

For ordinary resolving sets, the same twin-pair observation proves necessity: if two vertices of \(X\) are omitted from \(S\), that omitted pair has no landmark that distinguishes it. Thus \(|X\setminus S|\le1\), and symmetrically \(|Y\setminus S|\le1\).

Assume conversely that these two inequalities hold. Since \(p,q\ge3\), both \(S\cap X\) and \(S\cap Y\) are nonempty. Distinct vertices in the same one of \(X,Y\) are distinguished by whichever one of the pair belongs to \(S\). If \(i\ne j\), every vertex \(x\in X\) satisfies
\[
d(x,c_i)=i+1,
\]
so any landmark in \(S\cap X\) distinguishes \(c_i\) and \(c_j\). For \(x\in X\), the pair \(x,c_0\) is distinguished by every landmark in \(S\cap Y\); for \(i\ge1\), the pair \(x,c_i\) is distinguished by every landmark in \(S\cap X\), because such a landmark is at distance at most \(1\) from \(x\) and at distance \(i+1\ge2\) from \(c_i\). The right-hand cases with \(Y\) are symmetric. Finally, any \(x\in X\) and \(y\in Y\) are distinguished by every landmark in \(S\cap X\): its distance to \(x\) is at most \(1\), while its distance to \(y\) is \(\ell+2\). Hence the two omission inequalities are sufficient for a 1-metric generator.

For 2-metric generation, the twin-pair observation is stronger. Since the only two vertices that distinguish a pair \(x,x'\in X\) are \(x\) and \(x'\), every 2-metric generator must contain all of \(X\); similarly it must contain all of \(Y\). Conversely, take \(S\supseteq X\cup Y\). A same-side twin pair is distinguished by its two members. Any two distinct path vertices are distinguished by every vertex of \(X\), and \(|X|=p-1\ge2\). A pair \(x,c_0\) with \(x\in X\) is distinguished by every vertex of \(Y\), while \(x,c_i\) for \(i\ge1\) is distinguished by every vertex of \(X\). The symmetric statements hold on the right, and a pair \(x\in X,y\in Y\) is distinguished by every vertex of \(X\). Thus every pair has at least two distinguishing landmarks, proving the 2-metric criterion.

The enumerators now factor. On \(X\), a 1-metric generator may choose all \(p-1\) vertices or omit exactly one, contributing
\[
x^{p-1}+(p-1)x^{p-2}=x^{p-2}(x+p-1).
\]
The analogous factor for \(Y\) is \(x^{q-2}(x+q-1)\). Membership of the \(\ell+1\) path vertices is completely free, giving \((1+x)^{\ell+1}\). This proves the formula for \(\mathcal R_1\). For \(k=2\), every vertex of \(X\cup Y\) is forced into the set and every path vertex is optional, giving the stated \(\mathcal R_2\). The minimum degrees and minimum coefficients give the dimension and basis-count statements.

## Verification
A standalone exhaustive checker, `verify.py`, constructs the graphs and computes all-pairs shortest-path distances directly. For every \(3\le p,q\le5\), every \(1\le\ell\le3\), every \(k\in\{1,2,3\}\), and every vertex subset \(S\), it compares the literal definition of \(k\)-metric generation against the structural characterization above. It also compares the complete cardinality histograms against the coefficients of the stated polynomials and checks the predicted minima and basis counts.

Replay result:

`VERIFY_OK parameter_triples=27 k_values=3 subset_checks=65856 max_order=12`

The finite replay is supplementary evidence only. The theorem for all admissible parameters is established by the analytic distance argument above.

## Relationship to prior work
Estrada-Moreno, Rodríguez-Velázquez, and Yero introduced the \(k\)-metric-dimension framework and proved that the maximum feasible \(k\) is the minimum, over vertex pairs, of the number of vertices distinguishing that pair. They also prove a general lower bound obtained from non-singleton twin classes. In the present family, that framework explains why \(k\le2\) and yields the lower bound \(\dim_2\ge p+q-2\), but it does not give the all-generator characterizations or either enumerator.

Setyawan and Kusmayadi studied the symmetric one-edge barbell \(B_{n,n}\) and proved the scalar equality \(\dim_2(B_{n,n})=2n-2\). That scalar specialization is therefore not claimed as new. Their paper exhibits a 2-metric basis for the bridge barbell; the result here identifies every 1- and 2-metric generator, allows unequal clique sizes and arbitrary positive handle length, proves uniqueness of the minimum 2-generator, and gives both all-set polynomials.

## Limitations
The theorem excludes clique sizes below \(3\). It concerns vertex-distance \(k\)-metric generators, not edge, strong, local, adjacency, multiset, or doubly resolving variants. The literature comparison found no source that states the full asymmetric arbitrary-handle all-generator classification or its polynomials, but an obscure or poorly indexed source could contain an overlapping special case. No claim of independent validation is made.

## References
1. A. Estrada-Moreno, J. A. Rodríguez-Velázquez, and I. G. Yero, “The k-metric dimension of a graph,” arXiv:1312.6840, first public version 2013-12-24.
2. A. A. Setyawan and T. A. Kusmayadi, “On the k-Metric Dimension of a Barbell Graph and a t-fold Wheel Graph,” DOI:10.2991/assehr.k.200827.111, 2020.
