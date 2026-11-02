# Parity-kernel codes of cyclic prisms and their Reed–Muller support hierarchy

## Finding
Let \(n\ge3\), let \(G_n=C_n\square K_2\), and let \(\mathcal E_n\) be the family of vertex subsets having even intersection with **every closed neighborhood**. Writing \(g=\gcd(n,4)\), the binary incidence vectors form a length-\(2n\), dimension-\(g\) code with complete Hamming-weight enumerator
\[
W_n(z)=1+(2^g-2)z^n+z^{2n}.
\]
The full code, not only its cardinality, has a canonical classification up to coordinate permutation:

* \(g=1\): the length-\(2n\) binary repetition code;
* \(g=2\): the \(n\)-fold coordinate repetition of \(\operatorname{RM}(1,1)\), the full binary code on two points;
* \(g=4\): the \(n/4\)-fold coordinate repetition of \(\operatorname{RM}(1,3)\), the first-order binary Reed–Muller \([8,4,4]\) code.

The generalized Hamming weights \(d_r\), defined as the smallest union-of-support cardinality of any dimension-\(r\) subcode, are respectively
\[
(d_r)=\begin{cases}
(2n),&g=1,\\
(n,2n),&g=2,\\
(n,3n/2,7n/4,2n),&g=4.
\end{cases}
\]
In the closed-neighborhood binary Lights-Out game, there are exactly \(2^g\) quiet button-press patterns, and exactly the fraction \(2^{-g}\) of all target states can be reached from the zero state.

## Assumptions and scope
The cycle \(C_n\) is the **simple** graph with vertices \(i\in\mathbb Z/n\mathbb Z\) and edges between distinct consecutive residues. The two layers are \(a_i\) and \(b_i\), joined by rungs. Every closed neighborhood has four different vertices for \(n\ge3\). Arithmetic on incidence bits and the neighborhood matrix is over \(\mathbb F_2\). An even closed-neighborhood set may be empty; excluding the empty set simply subtracts the constant term of the enumerator. The code-repetition terminology means replicating each coordinate in an identical block of length \(n\) or \(n/4\), not taking a direct sum of independent codes.

## Proof
Write the selected-vertex indicators in the upper and lower layers as \(a_i,b_i\in\mathbb F_2\). The condition at upper vertex \(i\) is
\[
a_{i-1}+a_i+a_{i+1}+b_i=0,\]
so necessarily
\[
b_i=a_{i-1}+a_i+a_{i+1}.\tag{1}\]
The condition at the corresponding lower vertex is
\[
b_{i-1}+b_i+b_{i+1}+a_i=0.\]
Substituting (1), all repeated terms cancel, leaving \(a_{i-2}+a_{i+2}=0\), or
\[
a_{i+4}=a_i\qquad\text{for every }i\pmod n.\tag{2}\]
Conversely (2), together with (1), satisfies all upper and lower equations, so these equations are necessary and sufficient. A binary \(n\)-periodic sequence obeying period four is precisely a free \(g=\gcd(n,4)\)-periodic sequence. This proves \(\dim\mathcal E_n=g\) and gives an explicit bijection between \(\mathbb F_2^g\) and all valid sets.

If \(g=1\), the upper sequence is constant and (1) makes the lower sequence the same constant. Thus only the zero word and all-ones word occur.

If \(g=2\), the sequence alternates between two arbitrary bits, and (1) again gives \(b_i=a_i\). Each of the two free bits occurs in precisely \(n\) vertex positions, so the code is the \(n\)-fold coordinate repetition of the full length-two binary space \(\operatorname{RM}(1,1)\). Its two nonfull nonzero words have weight \(n\).

If \(g=4\), one four-column prism block contains exactly eight binary coordinate linear forms in the independent variables \((a_0,a_1,a_2,a_3)\). Four are the four coordinate forms and the others are the four forms obtained by omitting one coordinate from their sum. Their coefficient vectors are exactly the eight vectors of **odd Hamming weight** in \(\mathbb F_2^4\). Since the odd-weight vectors constitute an affine three-dimensional hyperplane, an affine reindexing of the eight positions identifies every linear combination of these forms with evaluation of an arbitrary affine Boolean function on \(\mathbb F_2^3\). This is precisely \(\operatorname{RM}(1,3)\). There are fourteen nonconstant nonzero affine Boolean functions, each balanced with four ones; the remaining nonzero word is the constant-one function with eight ones. Repeating the block \(n/4\) times gives fourteen words of weight \(n\) and one of weight \(2n\). This proves the weight enumerator in all cases.

For the generalized Hamming weights, in the full two-coordinate code every dimension-one space can be supported on one position, while a dimension-two space uses both. In \(\operatorname{RM}(1,3)\), the common zero set of a dimension-\(r\) subcode of affine functions has at most \(2^{3-r}\) points for \(1\le r\le3\), since \(r\) independent affine equations (when compatible) impose codimension \(r\). All these maxima are attained by independent coordinate functions. Dimension four leaves no common zero. Hence the generalized support sizes in one block are \((4,6,7,8)\). Replication multiplies all support sizes by the replication factor, proving the displayed hierarchy.

Finally, a vector of button presses is quiet exactly if it is in the kernel of the closed-neighborhood matrix \(M=I+A(G_n)\). Symmetry and rank-nullity give rank \(2n-g\), so the image has \(2^{2n-g}\) vectors out of the \(2^{2n}\) possible targets. This is the asserted reachability fraction. No probabilistic independence assumption is used.

## Verification
The companion standalone program `verify.py` constructs the actual \(2n\times2n\) closed-neighborhood matrix and independently computes its binary kernel by full row reduction for all \(3\le n\le64\). It checks the explicit parametrization and all codeword weights. A separate brute-force path enumerates **every** subset of \(V(G_n)\) for \(3\le n\le9\), evaluating the graph-theoretic neighborhood condition directly. It confirms that the eight code coordinates at \(n=4\) are precisely the eight odd-weight four-bit forms. Independent subspace enumeration reproduces each generalized Hamming weight for \(3\le n\le24\). These finite tests corroborate, but do not replace, the displayed proof for every integer \(n\ge3\).

## Relationship to prior work
Klostermeyer's *Prime Nullspace Matrices and Even Dominating Sets* (first public version 22 October 2026) studies analogous binary nullspace matrices arising from **open rectangular grid** graphs. Goldwasser, Klostermeyer and Ware's earlier work develops Fibonacci-polynomial criteria for parity domination on grids. Neither supplies the cyclic-prism three-regime weight distribution or its repeated Reed–Muller description in the material inspected. General linear-algebraic results for parity domination and Lights-Out give the kernel interpretation, not the present explicit code equivalence and generalized support hierarchy. A separate body of work on ordinary dominating polynomials of cylinders counts sets satisfying a different, nonparity condition. The novelty claim is specifically the complete closed-neighborhood parity **code** and generalized-weight classification on cyclic prisms, not the definition of even domination, the general nullspace correspondence, or the standard Reed–Muller code weight facts.

## Limitations
This result assumes two layers, uniform ordinary closed neighborhoods, and a simple cyclic prism. It does not establish corresponding classifications on open ladders, wider cylinders, arbitrary generalized Petersen graphs, or nonbinary parity variants. The Reed–Muller identification uses coordinate permutation, not preservation of graph adjacency. Historical priority remains qualified by inaccessible older full texts and alternative Lights-Out terminology. Independent mathematical validation has not been performed.

## References
1. W. F. Klostermeyer, *Prime Nullspace Matrices and Even Dominating Sets*, arXiv:2610.31475v1, posted 2026-10-22, https://arxiv.org/html/2610.31475v1.
2. J. Goldwasser, W. Klostermeyer, and H. Ware, *Fibonacci Polynomials and Parity Domination in Grid Graphs*, Graphs and Combinatorics **18** (2002), 271–283, DOI 10.1007/s003730200020.
3. A. Batal, *Parity of an odd dominating set*, Communications Faculty of Sciences University of Ankara, Series A1 Mathematics and Statistics **71** (2022), https://dergipark.org.tr/en/pub/cfsuasmas/article/1051208.
4. S. Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, arXiv:2408.08053 (2024); ordinary rather than parity domination.
