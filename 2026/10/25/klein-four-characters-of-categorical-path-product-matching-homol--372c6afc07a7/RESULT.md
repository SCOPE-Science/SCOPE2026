# Klein-four characters of categorical path-product matching homology

## Finding
For every integer \(\ell\ge2\), let \(G_\ell=P_\ell\times P_3\) be the **categorical/direct** product of simple paths, not their Cartesian product. Thus its vertices are \((i,j)\), with \(1\le i\le\ell\), \(1\le j\le3\), and two vertices are adjacent precisely if both coordinates differ by one. Let \(X_\ell=\mathsf M(G_\ell)\) be the ordinary matching simplicial complex. Two commuting automorphisms are horizontal reversal \(h(i,j)=(\ell+1-i,j)\) and vertical reversal \(v(i,j)=(i,4-j)\). Their subgroup is \(V=\langle h,v\rangle\cong C_2\times C_2\).

The entire reduced rational homology is concentrated in one **odd** degree: \(d_\ell=\ell-1\) for even \(\ell\) and \(d_\ell=\ell-2\) for odd \(\ell\). Its complete character \(\chi_\ell\) on \((1,h,v,hv)\) is as follows:

\[
\boxed{
\begin{array}{c|rrrr}
\ell&\chi_\ell(1)&\chi_\ell(h)&\chi_\ell(v)&\chi_\ell(hv)\\\hline
2r\ (r\ge1)&1&(-1)^r&1&(-1)^r\\
4s+1\ (s\ge1)&2^{2s+1}-1&1&1&2^{s+1}-1\\
4s+3\ (s\ge0)&2^{2s+2}-1&2^{s+1}-1&1&-(2^{s+1}-1)
\end{array}}
\]

There is no other reduced homology, even integrally. For the four rational one-dimensional characters \(\varepsilon_{a,b}\) defined by \(\varepsilon_{a,b}(h)=a\), \(\varepsilon_{a,b}(v)=b\), \(a,b\in\{-1,1\}\), their exact multiplicities are
\[
\boxed{m_{a,b}=\frac{\chi_\ell(1)+a\chi_\ell(h)+b\chi_\ell(v)+ab\chi_\ell(hv)}4.}
\]
Consequently the only positive reduced rational Betti number of the geometric quotient \(|X_\ell|/V\) is in degree \(d_\ell\), and equals \(m_{1,1}\): it is \(1\) for \(\ell\equiv0\pmod4\), \(0\) for \(\ell\equiv2\pmod4\), \(2^{2s-1}+2^{s-1}\) for \(\ell=4s+1\), and \(2^{2s}\) for \(\ell=4s+3\). These formulas classify only the specified natural Klein-four subgroup; additional graph automorphisms in small or exceptional widths are outside the claim.

## Assumptions and scope
The path \(P_t\) has exactly \(t\) vertices, and \(\mathsf M\) is the ordinary simplicial matching complex, not the complex of perfect matchings. Graphs are finite and simple. The representation is over \(\mathbb Q\), not a claim about a particular integral module splitting; the nonequivariant integral groups are free because of the known sphere-wedge theorem [1]. All formulas hold for every integer \(\ell\ge2\), including the boundaries \(\ell=2,3\). The quotient means the geometric realization followed by the indicated finite-group quotient.

## Proof
**1. Homology concentration and signed Lefschetz.** Theorem 3.5 in the corrected second version of Gupta--Sarkar--Sawant--Shukla [1] establishes
\[
X_{2r}\simeq S^{2r-1},\qquad
X_{2r+1}\simeq\bigvee^{2^{r+1}-1}S^{2r-1}\quad(r\ge1),
\]
with the first formula also valid for \(r=1\). In particular the unique nonzero reduced homology degree is odd. For an automorphism \(g\) of \(G_\ell\), write \(\mathcal E\) for its edge set. The alternating **augmented** simplicial-chain trace gives
\[
\operatorname{tr}(g\mid\widetilde H_{d_\ell}(X_\ell;\mathbb Q))
=\sum_{\substack{M\subseteq\mathcal E\text{ matching}\\gM=M}}
(-1)^{|M|}\operatorname{sgn}(g\mid M).
\tag{1}
\]
The empty matching contributes \(1\). Indeed a matching with \(p\) edges is an oriented \((p-1)\)-simplex, the augmented empty chain has degree \(-1\), and the unique homology degree is odd. For an involution, decompose invariant matchings into edge orbits of lengths one and two. A length-one orbit contributes a factor \(-1\) and a length-two orbit contributes \((-1)^2(-1)=-1\) to the summand in (1). Thus the trace is the weighted matching count \((-1)^{\text{number of selected edge orbits}}\), where eligible orbits must be internally vertex-disjoint and pairwise compatible.

**2. Three boundary matching sums.** For \(t\ge1\), let \(F_t\) be the signed number \(\sum_M(-1)^{|M|}\) of matchings of \(P_t\times P_3\). Let \(B_t\) be the same sum after deleting the **middle** vertex of its final column, and \(C_t\) after deleting the **top and middle** vertices of the final column. Then
\[
\begin{array}{c|ccc}
 t&F_t&B_t&C_t\\\hline
2s+1\ (s\ge0)&2^{s+1}-1&2^{s+1}-1&2^s\\
2s\ (s\ge1)&1&1-2^s&0.
\end{array}\tag{2}
\]
For completeness, this is an exact finite-width transfer calculation rather than a numerical extrapolation. Index boundary occupancy states by the three-bit masks \(0,\ldots,7\) (top, middle, bottom bits of weights \(1,2,4\)). The only four possible edges across a column boundary have endpoint indices \((0,1),(1,0),(1,2),(2,1)\). Define the integer transition matrix \(T_{ab}\) by summing \((-1)^{|E|}\) over subsets of those four edges with pairwise-disjoint endpoints, no left endpoint belonging to state \(a\), and right endpoint mask exactly \(b\). In state order \(0,\ldots,7\), direct four-edge enumeration gives
\[
T=\begin{pmatrix}
1&-1&-2&2&-1&0&2&0\\
1&-1&-1&1&-1&0&1&0\\
1&0&-2&0&0&0&0&0\\
1&0&-1&0&0&0&0&0\\
1&-1&-1&1&-1&0&1&0\\
1&-1&0&0&-1&0&0&0\\
1&0&-1&0&0&0&0&0\\
1&0&0&0&0&0&0&0
\end{pmatrix}.
\]
Let \(e_0\) be the row vector selecting state zero, \(u=(1,1,1,1,1,1,1,1)^\mathsf T\), and let \(b\) and \(c\) be terminal indicator vectors \(b_j=1\) iff \(j\mathbin{\&}2=0\), and \(c_j=1\) iff \(j\mathbin{\&}3=0\). Then \(F_t=e_0T^{t-1}u\), \(B_t=e_0T^{t-1}b\), \(C_t=e_0T^{t-1}c\). The characteristic polynomial is \(z^4(z+1)(z+2)(z^2-2)\). The initial terms for \(t=1,\ldots,8\) are respectively \((1,1,3,1,7,1,15,1)\), \((1,-1,3,-3,7,-7,15,-15)\), and \((1,0,2,0,4,0,8,0)\). The expressions (2) satisfy the characteristic recurrence (indeed its \((z+1)(z^2-2)\) factor). The eight initial terms and Cayley--Hamilton therefore prove (2) for all \(t\).

**3. Edge-orbit geometry.** In the following, a 'half graph' is the induced categorical product on the first \(r\) long-path columns, with the same four diagonal edge types as above.

For \(v\), every edge lies in a swapped pair sharing its endpoint in the middle row. Thus no nonempty edge orbit is eligible. Formula (1) gives \(\chi_\ell(v)=1\) for all \(\ell\).

For odd \(\ell=2r+1\), the central column is fixed by \(h\). Every edge orbit touching this column has two edges sharing a vertex there, so none is eligible. All other edge orbits correspond exactly to matchings of the left half graph: \(\chi_\ell(h)=F_r\). Under \(hv\), the orbits touching the central column consist of exactly two eligible but mutually incompatible double-edge orbits; either occupies the middle vertex of the left half's final column. Hence \(\chi_\ell(hv)=F_r-2B_r\).

For even \(\ell=2r\), the reflections \(h\) and \(hv\) interchange the two central columns. Each has exactly two eligible, mutually incompatible, double-edge orbits crossing the central gap. Either such orbit uses the middle vertex and one of the two outer vertices in the last column of the left half. By vertical symmetry the two restrictions have equal signed matching sum \(C_r\). All remaining orbits are freely represented by left-half matchings, so \(\chi_{2r}(h)=\chi_{2r}(hv)=F_r-2C_r\).

Substitute (2) to obtain the displayed four character values. Their identity value also agrees with the known Betti ranks of [1], providing an independent normalization check. Since \(V\) is the Klein four-group, orthogonality of its four rational characters gives the multiplicity formula; rational transfer for finite simplicial actions (using barycentric subdivision) gives \(\widetilde H_*(|X_\ell|/V;\mathbb Q)\cong\widetilde H_*(|X_\ell|;\mathbb Q)^V\), proving the quotient statement.

## Verification
The standalone Python 3 program `verify.py` has no external dependencies. Run `python verify.py` in the same directory. It generates the finite transfer matrix from the four cross-column edges, checks formula (2) for lengths \(1\) through \(27\), and independently enumerates valid edge orbits for all four group elements for widths \(2\) through \(9\), then the three nonidentity elements for widths \(10\) through \(14\). It also tests all four representation multiplicities for integrality and nonnegativity through width \(16\). The completed tests returned `TRANSFER_MATRIX_EXACT_27_OK` and `GROUP_ACTION_ORBIT_SUMS_VERIFIED 47 MAX_STATES 743476`. These are finite checks only; the proof of all widths is the transfer-matrix recurrence and the uniform orbit analysis above.

## Relationship to prior work
Gupta--Sarkar--Sawant--Shukla [1] proved the exact nonequivariant homotopy types in Theorem 3.5 of the second arXiv version (Theorem 5.5 in the first version), using disconnected line graphs, joins, and inductive independence-complex reductions. Those Betti numbers and homotopy types are **not claimed as new here**. The additional result is the complete two-reflection action on the unique reduced rational homology group, all four irreducible multiplicities, and the resulting quotient Betti numbers. The categorical/direct product is not the Cartesian rectangular grid. Related results on matching complexes of Cartesian \(3\times t\) grids [2] address distinct graph families; their reflection formulas do not specialize to this theorem. Work on the isolated \(P_6\times P_6\) categorical product [3] likewise does not cover the infinite \(P_\ell\times P_3\) family or its reflection action.

## Limitations
No integral lattice decomposition is claimed; the rational character determines the representation only over characteristic zero. The theorem concerns the indicated four-element symmetry subgroup, not every automorphism of \(G_\ell\). The pre-existing homotopy-type theorem is an essential input. Potential equivalent formulations dispersed through broader equivariant matching-complex literature cannot be excluded without independent bibliographic review. Finite computation corroborates but does not certify the infinite argument.

## References
[1] R. K. Gupta, S. Sarkar, S. S. Sawant, S. Shukla, *On the matching complexes of categorical product of path graphs*, arXiv:2403.15298, first posted 2024-03-22, v1 first posted 2024-03-22; revised v2 posted 2026-04-23, especially Theorem 3.5 and Section 3 of v2 (Theorem 5.5 of v1). https://arxiv.org/html/2403.15298v2 and https://arxiv.org/abs/2403.15298 .

[2] *Orthogonal-reflection Lefschetz formulas for 3×n grid matching complexes* and *Half-turn Lefschetz characters and full symmetry quotients of 3×n grid matching complexes*: public research records concerning the **Cartesian** grid family (not the direct graph product); bibliographic comparison based on their public summaries, not an asserted full-text exclusion.

[3] *The matching complex of P6 × P6 is a wedge of 169 eleven-spheres*: public research record concerning a single distinct **categorical** product (comparison based on its public summary).
