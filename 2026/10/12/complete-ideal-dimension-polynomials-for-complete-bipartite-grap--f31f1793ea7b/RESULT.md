# Complete ideal-dimension polynomials for complete-bipartite graph Lie algebras

## Finding
Let \(a,b\ge1\) and \(q\) be any prime power. Every ideal of the \((a+b+ab)\)-dimensional complete-bipartite graph Lie algebra over \(\mathbf F_q\) is counted, by its \(\mathbf F_q\)-dimension, by

\[
\mathcal I_{a,b,q}(T)=\sum_{r=0}^{a}\sum_{s=0}^{b}\sum_{k=0}^{\min(r,s)}\sum_{t=0}^{(a-r)(b-s)}
{a\brack r}_q{b\brack s}_q{r\brack k}_q{s\brack k}_q\,|\mathrm{GL}_k(\mathbf F_q)|
{(a-r)(b-s)\brack t}_q\,q^{(r+s-k)((a-r)(b-s)-t)}
T^{ab-(a-r)(b-s)+t+r+s-k}.
\]

Here \({n\brack j}_q\) is the Gaussian binomial coefficient (zero for \(j<0\) or \(j>n\)) and \(|\mathrm{GL}_k(\mathbf F_q)|=\prod_{i=0}^{k-1}(q^k-q^i)\), with the empty product equal to \(1\). This is an exact formula for the entire ideal-dimension distribution, not merely for ideals arising from vertex-induced subgraphs. It works without characteristic restrictions and is symmetric in \(a,b\).

## Assumptions and scope
Put \(U=\mathbf F_q^a\), \(W=\mathbf F_q^b\), \(Z=U\otimes_{\mathbf F_q}W\), and \(L=U\oplus W\oplus Z\). Define
\[
[(u,w,z),(u',w',z')]=(0,0,u\otimes w'-u'\otimes w).
\]
This is an alternating two-step nilpotent Lie bracket in all characteristics; \(Z\) is central. Choosing bases of \(U,W\) identifies this Lie algebra with the usual edge-distinctly-labeled Lie algebra of the complete bipartite graph \(K_{a,b}\), with one central basis element per edge. An ideal means an \(\mathbf F_q\)-linear subspace stable under brackets with every element of \(L\). The polynomial uses the dimension of the ideal, rather than codimension; the standard finite-field ideal zeta polynomial follows by reversing exponents.

## Proof
Let \(V=U\oplus W\) and \(\pi:L\to V\) be the quotient projection. For any Lie ideal \(I\), set \(X=\pi(I)\le V\) and \(C=I\cap Z\le Z\). The ideal property is equivalent to \([X,V]\subseteq C\), because all brackets land in the central space \(Z\). Conversely, for every such pair \((X,C)\), the ideals with those projections and intersections are exactly the inverse images in \(V\oplus Z\) of graphs of linear maps \(\varphi:X\to Z/C\); there are \(q^{\dim X(\dim Z-\dim C)}\) distinct graphs. Thus it suffices to count the subspaces \(X\) according to their projections and the possible choices of \(C\).

Write \(A=\pi_U(X)\le U\), \(B=\pi_W(X)\le W\), with \(\dim A=r\) and \(\dim B=s\). Varying the second argument independently through \(U\) and \(W\) shows
\[
[X,V]=A\otimes W+U\otimes B\subseteq Z.
\]
The quotient of \(Z\) by this space is naturally \((U/A)\otimes(W/B)\), of dimension \(c=(a-r)(b-s)\); in particular \(\dim[X,V]=ab-c\). Every allowed \(C\) is the inverse image of a subspace of this quotient. If that subspace has dimension \(t\), then \(\dim C=ab-c+t\) and the number of such \(C\) is \({c\brack t}_q\). The possible graph maps number \(q^{\dim X(c-t)}\). The resulting ideal has dimension \(\dim X+ab-c+t\).

It remains to count \(X\le A\oplus B\) projecting surjectively onto both factors. Define \(A_0=\{u\in A:(u,0)\in X\}\) and \(B_0=\{w\in B:(0,w)\in X\}\). The standard subspace correspondence gives an isomorphism \(A/A_0\xrightarrow{\sim}B/B_0\) whose graph has inverse image \(X\). Consequently \(\dim(A/A_0)=\dim(B/B_0)=k\), with \(0\le k\le\min(r,s)\), and
\[
\dim X=r+s-k=:d.
\]
For fixed \((r,s,k)\), first choose \(A\) and \(B\), in \({a\brack r}_q{b\brack s}_q\) ways. Then choose their codimension-\(k\) subspaces \(A_0,B_0\), in \({r\brack k}_q{s\brack k}_q\) ways, and finally an isomorphism of the two \(k\)-dimensional quotients, in \(|\mathrm{GL}_k(\mathbf F_q)|\) ways. This classification is bijective, so no multiplicity is introduced.

Multiplying these independent choices by the \({c\brack t}_q\) central-subspace choices and \(q^{d(c-t)}\) graph maps, and inserting the ideal dimension \(ab-c+t+d\), gives exactly the fourfold sum stated in the finding. All arguments hold in every finite characteristic, including characteristic two. This completes the proof.

## Verification
Run the standalone script `verify.py` with Python 3 and no third-party dependencies. Its `predicted(a,b,q)` implements the theorem independently of the brute-force `brute(a,b,p)` routine, which enumerates row-reduced echelon subspaces of the ambient vector space and tests the ideal condition against every vertex-basis generator. Exhaustive finite-prime-field comparisons passed for \((a,b,q)=(1,1,2),(1,1,3),(1,2,2),(1,2,3),(2,2,2)\), with respective ideal totals \(6,7,26,45,247\). Additional evaluations check symmetry under exchanging \(a\) and \(b\). The output ends with `VERIFY_OK`. These finite checks corroborate, but do not replace, the proof for arbitrary \(a,b,q\).

## Relationship to prior work
Godoy Molina and Lagos, arXiv:2308.00272 (first public version, 2023-08-01), describe Lie algebras of labeled graphs, graph-derived ideals, and the graded derivation Lie algebra for two labelings of \(K_{a,b}\). Their Section 3 explicitly studies only special ideals detected by subgraphs; Section 5 concerns derivations, not counting all ideals. The present theorem counts all \(\mathbf F_q\)-linear Lie ideals, including those determined by noncoordinate subspaces and central graph lifts.

Lee, arXiv:2010.02268, develops the finite-field ideal zeta-polynomial framework and provides explicit examples such as free nilpotent Lie algebras. The special case \(a=b=1\) is the familiar three-dimensional Heisenberg algebra and is not claimed as new. The result here is the uniform arbitrary-\((a,b)\) formula for the complete-bipartite family. Lee, arXiv:2602.07254, computes explicit zeta functions of solvable Lie algebras of dimension at most four, which does not yield the family in dimensions five and above. General algorithms in the literature do not by themselves state this specialized closed polynomial.

## Limitations
This is a theorem about \(\mathbf F_q\)-linear Lie ideals of the stated finite-dimensional Lie algebras. It does not compute subgroup-counting functions for all characteristics, integral or \(p\)-adic ideal zeta functions, the subalgebra zeta polynomial, or automorphism-orbits of ideals. The formula is complete for ideals regardless of the field characteristic. The claimed literature novelty concerns the uniform closed ideal polynomial for the two-parameter bipartite family, not general subspace or quotient correspondences, nor the three-dimensional Heisenberg special case.

## References
1. M. Godoy Molina and D. Lagos, *Lie algebras associated with labeled directed graphs*, arXiv:2308.00272v2 (first public 2023-08-01), https://arxiv.org/abs/2308.00272 .
2. S. Lee, *Zeta functions of \(\mathbf F_p\)-Lie algebras and finite \(p\)-groups*, arXiv:2010.02268v3 (first public 2020-10-05), https://arxiv.org/abs/2010.02268 .
3. S. Lee, *Zeta functions of solvable Lie algebras over finite fields—with calculations in detail*, arXiv:2602.07254v1 (2026-02-06), https://arxiv.org/abs/2602.07254 .
