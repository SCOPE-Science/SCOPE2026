# Independence polynomials as one-line extension polynomials of finite \(K_{m,n}\)-free incidence structures
## Finding
Fix integers \(m,n\ge 2\). For a finite \(K_{m,n}\)-free incidence structure \(A\), let \(P(A)\) be its point set and define the \(m\)-uniform saturation hypergraph \(H_A\) on \(P(A)\) by
\[
E(H_A)=\{M\in \binom{P(A)}m: M\text{ is simultaneously incident with exactly }n-1\text{ lines of }A\}.
\]
For \(S\subseteq P(A)\), let \(A+\ell_S\) be obtained by adjoining one new line \(\ell_S\) incident exactly with the points of \(S\). Define the one-line extension polynomial
\[
E_A(z)=\sum_{S\subseteq P(A):\ A+\ell_S\text{ is }K_{m,n}\text{-free}} z^{|S|}.
\]
Then
\[
E_A(z)=I_{H_A}(z),
\]
where \(I_H(z)=\sum_{S\subseteq V(H):\ S\text{ independent in }H}z^{|S|}\) is the independence polynomial.

Conversely, every finite simple \(m\)-uniform hypergraph \(H\) occurs as \(H_A\) for some finite \(K_{m,n}\)-free incidence structure \(A\). Hence the one-line extension polynomials of finite models of the universal theory \(T^p_{m,n}\) are exactly the independence polynomials of finite \(m\)-uniform hypergraphs.

As a complexity consequence, for every fixed \(m,n\ge2\), computing \(E_A(1)\) from a finite \(K_{m,n}\)-free incidence structure \(A\) is \(\#P\)-complete under polynomial-time metric reductions.

## Assumptions and scope
An incidence structure has unary point and line sorts and a binary incidence relation. It is \(K_{m,n}\)-free when no \(m\) points are all incident with the same \(n\) lines. Conant and Kruckman denote the universal theory of such structures by \(T^p_{m,n}\), and construct its model companion \(T_{m,n}\). The claim here concerns finite models of the universal base theory and a single new-line extension; it is not a claim about complete \(1\)-types in the model companion.

The parameters \(m,n\) are fixed constants at least two. The input to the counting problem is a finite incidence structure already known to be \(K_{m,n}\)-free.

## Proof
Let \(S\subseteq P(A)\). Since \(A\) is already \(K_{m,n}\)-free, any new copy of \(K_{m,n}\) in \(A+\ell_S\) must use the new line \(\ell_S\). Such a copy exists exactly when there is an \(m\)-set \(M\subseteq S\) that was already incident with \(n-1\) lines of \(A\). By definition, those \(M\) are precisely the hyperedges of \(H_A\). Therefore
\[
A+\ell_S\text{ is }K_{m,n}\text{-free}
\quad\Longleftrightarrow\quad
S\text{ contains no edge of }H_A.
\]
Thus the admissible neighborhoods \(S\) are exactly the independent sets of \(H_A\), proving \(E_A(z)=I_{H_A}(z)\).

For the converse, let \(H=(V,E)\) be any finite simple \(m\)-uniform hypergraph. Construct \(A_H\) with point set \(V\). For every hyperedge \(e\in E\), add \(n-1\) distinct lines, each incident exactly with the \(m\) points of \(e\). Any \(m\)-set of points is incident with \(n-1\) lines exactly when it is an edge of \(H\); distinct \(m\)-edges cannot be contained in one another. Hence \(A_H\) is \(K_{m,n}\)-free and \(H_{A_H}=H\).

For complexity, membership in \(\#P\) is immediate for fixed \(m,n\): nondeterministically choose \(S\subseteq P(A)\) and check in polynomial time that no \(m\)-subset of \(S\) already has \(n-1\) common lines in \(A\).

For hardness, start with a graph \(G=(V,E)\), whose number \(i(G)\) of independent sets is a classical \(\#P\)-complete quantity. Let \(C\) be a new set of \(m-2\) vertices and form the \(m\)-uniform hypergraph
\[
H_m(G)=\{C\cup e:e\in E\}
\]
on \(V\cup C\). An independent set of \(H_m(G)\) either omits at least one point of \(C\), in which case its intersection with \(V\) is arbitrary, or contains all of \(C\), in which case its intersection with \(V\) must be independent in \(G\). Therefore
\[
i(H_m(G))=(2^{m-2}-1)2^{|V|}+i(G).
\]
Build \(A_{H_m(G)}\) by the preceding incidence construction. Since \(E_{A_{H_m(G)}}(1)=i(H_m(G))\), one oracle value for the extension count recovers \(i(G)\) by subtracting the explicit offset. This is a polynomial-time metric reduction.

## Verification
The accompanying verifier independently constructs incidence structures from all small \(m\)-uniform hypergraphs in the ranges \(m=2\), up to four vertices, and \(m=3\), up to five vertices, for \(n=2,3,4\). For every subset of points it checks directly that adjoining one line preserves \(K_{m,n}\)-freeness exactly when that subset is independent in the saturation hypergraph. It also checks the graph-to-\(m\)-uniform hardness identity for every graph through five vertices and \(2\le m\le5\).

The recorded replay output is:

`checked_extension_instances=3348`

`checked_hardness_instances=4400`

`VERIFY_OK`

These finite checks support the implementation and edge cases; the theorem itself is proved uniformly above.

## Relationship to prior work
Conant and Kruckman define \(T^p_{m,n}\) as the universal theory of \(K_{m,n}\)-free incidence structures and use the same saturation threshold \(n-1\) in their free-completion construction. Their Proposition 2.3 adds separate new lines to deficient \(m\)-sets, and Theorem 2.8 identifies the model companion. The inspected paper does not state the polynomial \(E_A(z)\), identify arbitrary one-line neighborhoods with hypergraph independent sets, realize every \(m\)-uniform independence polynomial in this way, or derive the exact counting-complexity consequence.

Vadhan proves that counting graph independent sets remains \(\#P\)-complete even under strong graph restrictions. The reduction above is specific to the incidence-extension problem and is explicit for every fixed \(m,n\ge2\).

## Limitations
The result is about finite one-line extensions of models of the universal theory \(T^p_{m,n}\), not about complete types over parameter sets in existentially closed models of \(T_{m,n}\). It makes no approximation-complexity claim and no claim about the complexity when \(m\) or \(n\) is part of the input rather than fixed.

The originality search found no direct statement of this exact extension-polynomial identification, but short structural observations can exist as unindexed folklore. The literature comparison therefore supports, but cannot logically prove, novelty.

## References
1. Gabriel Conant and Alex Kruckman, *Independence in generic incidence structures*, arXiv:1709.09626; Journal of Symbolic Logic 84 (2019), 750–780, DOI 10.1017/jsl.2019.8.
2. Salil P. Vadhan, *The Complexity of Counting in Sparse, Regular, and Planar Graphs*, SIAM Journal on Computing 31 (2001), 398–427, DOI 10.1137/S0097539797321602.
