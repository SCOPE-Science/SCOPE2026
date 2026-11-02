# Complete binary additive-colouring spectrum of labelled cycles

## Finding
For each integer \(n\ge3\), let \(C_n\) be the simple cycle with labelled vertices \(0,\ldots,n-1\). An *additive two-colouring* assigns \(f_i\in\{1,2\}\) to each vertex, with the sums of the labels on the two neighbours unequal at the ends of every edge. Define
\[
P_n(z)=\sum_{f\text{ additive}}z^{|\{i:f_i=2\}|}.
\]
The complete bivariate enumeration is
\[
\boxed{\displaystyle\sum_{n\ge3}P_n(z)u^n=
\frac{2zu^2+4(z+z^3)u^4-8z^4u^8}
{1-zu^2-(z+z^3)u^4+z^4u^8}-2zu^2.}
\]
In particular \(P_n(z)=0\) for every odd \(n\). For every even \(n\ge4\), the least exponent and greatest exponent in \(P_n(z)\) are respectively \(\lceil n/4\rceil\) and \(n-\lceil n/4\rceil\), and
\[
\boxed{[z^{\lceil n/4\rceil}]P_n(z)=
\begin{cases}4,&n\equiv0\pmod4,\\n,&n\equiv2\pmod4.\end{cases}}
\]
Moreover \(P_n(z)=z^nP_n(1/z)\) for even \(n\). Thus the same multiplicities occur at the largest exponent. For even \(n\), these enumerate the additive colourings with the minimum possible palette size of two (the known additive chromatic number); for odd \(n\), two labels are impossible.

## Assumptions and scope
All cycles are simple, finite and **labelled**. Indices in this document are read modulo \(n\). The neighbour-sum condition is open-neighbourhood additive colouring: for adjacent vertices \(i\) and \(i+1\), require \(f_{i-1}+f_{i+1}\ne f_i+f_{i+2}\). No properness condition is imposed on the labels \(f_i\) themselves. Distinct functions on the fixed labelled vertices count separately. The weight variable records occurrences of label \(2\), not total numerical label sum.

## Proof
Put \(b_i=f_i-1\in\{0,1\}\). The edge condition becomes
\[
b_{i-1}+b_{i+1}\ne b_i+b_{i+2}.
\]
Build a directed weighted graph with eight states \((a,b,c)\in\{0,1\}^3\). For each \(d\in\{0,1\}\), there is an arc from \((a,b,c)\) to \((b,c,d)\) with weight \(z^d\) if and only if \(a+c\ne b+d\). Its adjacency matrix \(M(z)\) is indexed lexicographically by states. For \(n\ge3\), a closed walk of length \(n\), with its starting position distinguished, corresponds bijectively to a labelled cyclic binary word satisfying all edge conditions. Because successive triple coordinates overlap, the walk determines precisely the bits at vertices \(0,\ldots,n-1\). Its weight is \(z\) to the number of ones, so \(P_n(z)=\operatorname{tr}(M(z)^n)\).

There are exactly three directed simple cycles in the state digraph, written here as lists of three-bit states:
\[
\begin{array}{ll}
000\to001\to010\to100\to000,&\text{length }4,\ \text{weight }z,\\
010\to101\to010,&\text{length }2,\ \text{weight }z,\\
101\to011\to111\to110\to101,&\text{length }4,\ \text{weight }z^3.
\end{array}
\]
The first and third simple cycles are vertex-disjoint; the two-step cycle intersects each of the other two. Direct enumeration of the outgoing arcs (and independently the standalone exact checker) verifies that the list is exhaustive. The directed-cycle expansion of the determinant therefore gives
\[
\Delta(u,z)=\det(I-uM(z))=1-zu^2-(z+z^3)u^4+z^4u^8.
\]
For a matrix of formal polynomials, the standard trace–determinant identity gives
\[
\sum_{n\ge1}\operatorname{tr}(M(z)^n)u^n
=-u\frac{\partial}{\partial u}\log\Delta(u,z).
\]
The first two trace coefficients are \(0\) and \(2z\), respectively, and the graph cycles begin at order three. Removing those two formal coefficients produces the claimed generating function, with no unproved extrapolation.

All directed simple cycles above have even lengths, hence the state digraph is bipartite; every closed walk has even length. Thus \(P_n=0\) for odd \(n\). Replacing each \(b_i\) by \(1-b_i\) preserves the inequalities and sends its number of ones to \(n\) minus that number; this proves the palindromic identity.

For the minimum exponent, a valid binary word cannot contain the consecutive pattern \(0000\), because that would violate the four-term inequality. Consequently every cyclic gap between consecutive ones has length at most four, yielding at least \(\lceil n/4\rceil\) ones. The word \((1000)^{n/4}\) attains the bound when \(n\equiv0\pmod4\). When \(n=4k+2\), the word \((1000)^k10\) has \(k+1=\lceil n/4\rceil\) ones and also satisfies the condition. Both constructions follow by inspection of their cyclic length-four subwords, which are drawn from \(1000,0001,0010,0100,1010,0101\), each satisfying the displayed inequality.

For completeness, classify *all* extremizers. Let the cyclic distances between successive ones be \(d_1,\ldots,d_j\). They are positive integers at most four and sum to \(n\). When \(n=4k\) and \(j=k\), every distance equals four, giving precisely the four labelled rotations of the four-periodic word. When \(n=4k+2\) and \(j=k+1\), the sum of the deficits \(4-d_i\) equals two. Thus either precisely one distance is two and all others four, or two distances are three and all others four. A distance three creates the forbidden local pattern \(1001\), which violates the same four-term inequality. So precisely one distance two must occur. Choosing the vertex immediately before that unique short gap determines the configuration bijectively, giving exactly \(n\) labelled configurations. Their validity follows from the construction above. Complementation proves the statement for the maximal exponent.

Finally, all these calculations also imply a total-count growth statement: the dominant positive real zero of \(x^4-x^3-1\) is \(\rho\approx1.380277569\), and for even \(n\), \(P_n(1)=2\rho^n(1+o(1))\). Indeed, the characteristic polynomial at \(z=1\) factors as \((x^4-x^3-1)(x^4+x^3-1)\), the state digraph is strongly connected and has period exactly two, and the two peripheral eigenvalues are \(\pm\rho\). This asymptotic is a consequence, not an assumption, of the finite-state proof.

## Verification
Run \(\texttt{python3 verify.py}\) in a directory containing the supplied standalone file. It independently enumerates all \(131064\) bit assignments across labelled cycle lengths \(3\) through \(16\), comparing each exact weight coefficient to the transfer trace. It enumerates all simple directed cycles and computes the determinant from compatible cycle collections, verifies the derived polynomial recurrence to length \(84\), compares direct transfer traces through length \(36\), and checks the extremal coefficient formula and coefficient reversal to length \(84\). Expected final line begins \(\texttt{VERIFY_OK}\). Finite tests corroborate the proof; the transfer bijection, determinant argument, and extremal-gap classification prove the universal statements.

For illustration,
\[
P_4(z)=4z+2z^2+4z^3,\qquad
P_6(z)=6z^2+2z^3+6z^4,
\]
\[
P_8(z)=4z^2+8z^3+2z^4+8z^5+4z^6.
\]

## Relationship to prior work
The general additive chromatic number and a sharp degree-based upper bound are studied by A. Koutsoutis and J. Koutsoutis (2026). Their argument concerns existence and bounds, not a complete weighted count on cycles. D. Severín (2016; journal version 2020) already obtains the additive chromatic numbers of cycles: two for even lengths and three for odd lengths. Those minimum palette sizes are not claimed here. The present contribution is the all-coefficient weighted enumeration for the two-label palette, the sharp extremal multiplicities, and the underlying three-simple-cycle transfer graph. Neighbour-sum-distinguishing labelings are also called lucky labelings or additive vertex colourings; changing names does not create a new problem. A broader pre-existing enumeration theorem for local constrained cyclic words might imply the formula without expressly mentioning this graph parameter; this remains a historical-priority risk.

## Limitations
No complete formula is supplied for the three-label optimal assignments on odd cycles, for graph families other than simple cycles, or for labelings modulo dihedral symmetry. The result counts functions over an ordered palette \(\{1,2\}\), not colourings modulo label permutations. Independent mathematical and comprehensive historical-priority audits have not been performed. The observed lack of a covering literature match is not a proof of global originality.

## References
1. A. Koutsoutis and J. Koutsoutis, *An elementary proof of a tight \(\Delta+1\) bound for the additive chromatic number*, arXiv:2610.30174v1, publicly posted 2026-10-19. https://arxiv.org/abs/2610.30174
2. D. Severín, *On the additive chromatic number of several families of graphs*, arXiv:1602.07675, publicly posted 2016-02-24. https://arxiv.org/abs/1602.07675
3. S. Czerwiński, J. Grytczuk and W. Żelazny, *Lucky labelings of graphs*, Information Processing Letters 109 (2009), 1078–1081. https://doi.org/10.1016/j.ipl.2009.05.011
