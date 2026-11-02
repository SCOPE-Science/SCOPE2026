# Critical group of the 48-line intersection graph on the complex Fermat quartic

## Finding
Let \(X\subset\mathbb P^3_{\mathbb C}\) be the smooth Fermat quartic
\[
X:\quad x_0^4+x_1^4+x_2^4+x_3^4=0.
\]
Let \(G_X\) be the graph on its \(48\) geometric lines, with two distinct lines adjacent precisely when they intersect on \(X\). Then \(G_X\) is connected and \(14\)-regular. Its reduced Laplacian has the Smith normal form
\[
\operatorname{diag}\bigl(1^{18},4^2,12^{10},24^5,192^6,960^2,1920^3,5760\bigr).
\]
Consequently its critical group (sandpile group, or graph Jacobian) is
\[
K(G_X)\cong (\mathbb Z/4\mathbb Z)^2\oplus(\mathbb Z/12\mathbb Z)^{10}
\oplus(\mathbb Z/24\mathbb Z)^5\oplus(\mathbb Z/192\mathbb Z)^6
\oplus(\mathbb Z/960\mathbb Z)^2\oplus(\mathbb Z/1920\mathbb Z)^3
\oplus\mathbb Z/5760\mathbb Z.
\]
In particular,
\[
|K(G_X)|=2^{115}3^{28}5^6,\qquad \exp K(G_X)=5760.
\]
The unit Smith factors are included in the displayed normal form but omitted from the group decomposition.

## Assumptions and scope
The base field is \(\mathbb C\), and intersection means geometric intersection of two distinct embedded projective lines on this fixed quartic model. The graph is not the intersection lattice of \(\operatorname{NS}(X)\); its critical group is the torsion cokernel of its integral graph Laplacian. We use the classical theorem that the \(48\) lines are exactly the three coordinate-pairing families of \(16\) lines each (Shimada–Shioda, Section 3, as well as Schütt–Shioda–van Luijk).

For \(p\in\{0,1,2\}\) label the coordinate pairings by
\[
P_0=((0,1),(2,3)),\quad P_1=((0,2),(1,3)),\quad P_2=((0,3),(1,2)).
\]
Let \(\zeta=\exp(\pi i/4)\), so \(\zeta^4=-1\). For each pairing \(P_p=((i,j),(k,l))\) and \(a,b\in\{0,1,2,3\}\), define the line \(\ell_{p,a,b}\) by
\[
x_i=\zeta^{2a+1}x_j,\qquad x_k=\zeta^{2b+1}x_l.
\]
These are all distinct and lie on \(X\). The standalone verifier uses precisely this ordering of the \(48\) lines.

## Proof
**1. Exact adjacency.** Two lines meet if and only if their four defining linear equations have a nonzero common solution, equivalently their \(4\times4\) coefficient determinant vanishes in \(\mathbb Z[\zeta]\). For lines in the same pairing, the criterion is that their first or second exponents agree. For \(p<q\) from different pairings, the complete criteria are
\[
\begin{array}{c|l}
(p,q)&\ell_{p,a,b}\cap\ell_{q,c,d}\ne\varnothing\\\hline
(0,1)&a+d-c-b\equiv0\pmod4\\
(0,2)&a+b+d+1-c\equiv0\pmod4\\
(1,2)&a+b-c-d\equiv0\pmod4.
\end{array}
\]
Each line has six neighbors in its own pairing and four neighbors in each of the other two pairings. Thus \(G_X\) is \(14\)-regular with \(144+192=336\) edges. Connectivity follows by direct breadth-first search of the finite adjacency matrix. The exact determinant procedure in `verify.py` works over the integral basis \(1,\zeta,\zeta^2,\zeta^3\), using \(\zeta^4=-1\), and independently agrees with every one of the above criteria.

**2. Spectrum and spanning trees.** Let \(A\) be the \(48\times48\) adjacency matrix. Exact integer matrix multiplication gives
\[
\det(tI-A)=(t-14)(t-2)^{28}(t+2)^{12}(t+6)^6(t+10).
\]
For a short reproducible certificate, `verify.py` checks the annihilating polynomial with these five distinct roots and the first five power traces. Since \(A\) is real symmetric, those checks uniquely determine all eigenvalue multiplicities by the nonsingular Vandermonde system. The connected Laplacian \(L=14I-A\) has nonzero eigenvalues \(12\) (multiplicity \(28\)), \(16\) (multiplicity \(12\)), \(20\) (multiplicity \(6\)), and \(24\) (multiplicity \(1\)). By the matrix-tree theorem, the determinant of any reduced Laplacian is
\[
\frac{12^{28}16^{12}20^6\,24}{48}=2^{115}3^{28}5^6.
\]

**3. Integral Smith data.** Delete the last row and column of \(L\) to obtain the integral \(47\times47\) matrix \(R\). The verified local Smith valuations are

| Prime | Exponent and multiplicity |
| --- | --- |
| \(2\) | \(0:18,\ 2:12,\ 3:5,\ 6:8,\ 7:4\) |
| \(3\) | \(0:20,\ 1:26,\ 2:1\) |
| \(5\) | \(0:41,\ 1:6\) |

These are exact local unimodular diagonalizations, not floating-point estimates: the algorithm works modulo \(p^{e+1}\), where \(e\) is the already proved valuation of \(\det R\), performs unit-pivot row/column operations, and divides the remaining block by \(p\) only after certifying that all its entries are divisible by \(p\). This modulus determines every Smith valuation because none can exceed \(e\). The valuation sums are exactly \(115,28,6\), respectively. No other prime divides \(\det R\). Aligning the sorted local valuation lists yields the displayed \(47\) Smith factors, whose product equals the tree count. The standard reduced-Laplacian presentation identifies their nonunit factors with \(K(G_X)\).

## Verification
Execute `python3 verify.py` with Python's standard library. It generates the \(48\) line equations, evaluates all \(1128\) pair determinants exactly in \(\mathbb Z[\zeta]\), checks the graph and its connectedness, certifies the spectral polynomial and power traces, computes the local Smith valuations for every possible torsion prime, and recombines the invariant factors. The expected last line is `VERIFY_OK`. An additional exact Hermite-normal-form computation of the reduced Laplacian reproduced the spanning-tree determinant; it is not required to run the standalone verifier.

## Relationship to prior work
Schütt, Shioda and van Luijk establish integral generation of the Fermat quartic Néron–Severi group by lines, a claim about the divisor intersection lattice. Shimada and Shioda give explicit equations for the \(48\) lines and classify their intersecting-pair orbits (of sizes \(48,96,192\)); Bouyer likewise analyzes the Picard lattice and its discriminant \(64\). Those results specify the geometry underlying the present graph, but do not state its reduced Laplacian Smith normal form or critical-group decomposition. The graph's order can be recovered from its spectrum; its integral invariant factors require additional information. Closest accessible mathematical-record findings concern the different \(64\)-line Schur quartic graph or the \(85\)-line Yu–Zhu quintic graph, and neither implies these \(48\)-vertex factors.

## Limitations
The assertion is for the complex Fermat quartic's particular line-incidence graph and does not identify its critical group with Picard torsion, the Néron–Severi discriminant group, or a geometric Jacobian of a curve. This calculation does not claim a classification for all quartic K3 surfaces or reductions to positive characteristic. Earlier unindexed graph computations could contain an equivalent group; no independent historical-priority determination or external mathematical audit has been performed.

## References
1. M. Schütt, T. Shioda, R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377 (first public version December 12, 2008), especially Sections 1, 3 and 6.1. https://arxiv.org/abs/0812.2377
2. I. Shimada, T. Shioda, *On a smooth quartic surface containing 56 lines which is isomorphic as a K3 surface to the Fermat quartic*, arXiv:1604.06265 (first public version April 21, 2016), especially Section 3 and the intersecting-pair orbit table. https://arxiv.org/abs/1604.06265
3. F. Bouyer, *A study of quartic K3 surfaces with a (Z/2Z)4 action*, PhD thesis, University of Warwick (2016), Chapter 4. https://wrap.warwick.ac.uk/id/eprint/80893/
