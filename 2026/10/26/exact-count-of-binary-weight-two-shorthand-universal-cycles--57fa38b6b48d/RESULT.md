# Exact count of binary weight-two shorthand universal cycles

## Finding
For every integer \(n\ge 3\), let \(\mathcal L_n\) be the set of binary words of length \(n-1\) containing exactly one or exactly two ones. Let \(U_2(n)\) be the number of binary circular words of length \(\binom n2\), identified **only under cyclic rotation**, whose length-\(n-1\) circular factors are precisely the members of \(\mathcal L_n\), each occurring once. Then
\[
\boxed{U_2(n)=2^{\lfloor(n-2)/2\rfloor}.}
\]
In particular, the counts for \(n=3,4,\ldots,12\) are \(1,2,2,4,4,8,8,16,16,32\), respectively. These are universal cycles for the shorthand binary representations of the two-subsets of an \(n\)-element set, not universal cycles for the unreduced weight-two words of length \(n\).

## Assumptions and scope
The alphabet \(\{0,1\}\) is labeled. A circular word is compared only modulo positional rotations; reversal and complementation are **not** imposed as equivalences. The circular factors wrap around the endpoint. The weight \(|w|_1\) is the number of ones in \(w\). Since \(|\mathcal L_n|=\binom{n-1}{1}+\binom{n-1}{2}=\binom n2\), the specified circumference is forced.

The statement covers every integer \(n\ge3\); the proof does not extrapolate from small enumerations. Different occurrences of the same circular factor are forbidden by the definition.

## Proof
**1. Universal cycles as Eulerian tours.** Put \(m=n-2\ge1\). Form a directed edge-labeled graph \(G_m\) with one vertex for every binary word of length \(m\) of weight \(0,1,\) or \(2\), and one edge for each word \(a_0\cdots a_m\in\mathcal L_n\), from \(a_0\cdots a_{m-1}\) to \(a_1\cdots a_m\). The edge retains its full word as its label. A closed Eulerian tour uses each member of \(\mathcal L_n\) exactly once and hence gives precisely one desired circular word, and conversely. Because the labels are distinct and every label occurs once, Eulerian tours modulo cyclic edge shift correspond bijectively to the desired circles.

At every vertex of weight one, indegree and outdegree equal two. At every vertex of weight zero or two, both equal one. Thus every visit to a degree-one vertex is forced. Contracting all maximal directed paths whose internal vertices have degree one preserves cyclic Eulerian tours and distinguishes parallel edges by their original paths.

**2. The contracted digraph.** For \(0\le i<m\), denote by \(v_i=0^i10^{m-1-i}\) the weight-one vertex with its one at position \(i\), counted from zero at the left. From \(v_i\), the first outgoing symbol may be zero or one:

* Appending zero, and following the unique continuation through the all-zero vertex if needed, first reaches \(v_{i-1\pmod m}\).
* Appending one, and following the forced zero appends until the older one leaves (or directly if \(i=0\)), first reaches \(v_{m-1-i}\).

Consequently the contracted labeled directed multigraph \(H_m\) has vertices \(0,\ldots,m-1\) and exactly two outgoing arcs from \(i\):
\[
i\longrightarrow i-1\pmod m,\qquad i\longrightarrow m-1-i.
\]
Parallel arcs and loops are retained with multiplicity. The decrement arcs themselves form a Hamiltonian directed cycle, so \(H_m\) is strongly connected. The reflected arcs are also a permutation, hence the graph has indegree and outdegree two at every vertex.

**3. The Euler-tour count reduces to an arborescence count.** The BEST theorem for a directed Eulerian multigraph says that the number of cyclic Euler tours with distinguishable arcs equals \(\tau_r(H_m)\prod_i(2-1)!\), where \(\tau_r\) counts in-arborescences rooted at any fixed vertex \(r\). The anchoring of an Euler tour may be made canonical by fixing the unique arc corresponding to the contracted path containing the allowed word \(0^{n-2}1\); thus no extra circumference or rotational factor occurs. The factorial product equals one, so \(U_2(n)=\tau_r(H_m)\).

**4. Spectral evaluation.** Let \(P\) act on column functions by \((Pf)(i)=f(i-1\pmod m)\), and \(R\) by \((Rf)(i)=f(m-1-i)\). The outgoing Laplacian is \(L_m=2I-P-R\). Both \(P\) and \(R\) are permutation matrices, so this balanced Laplacian has all principal cofactors equal. Since the decrement cycle makes its nullspace one-dimensional, the directed matrix-tree theorem gives
\[
\tau_r(H_m)=\frac1m\prod_{\lambda\ne0}\lambda,
\]
where nonzero eigenvalues are included with algebraic multiplicity.

Let \(\zeta=\exp(2\pi i/m)\) and \(e_k(i)=\zeta^{ki}\). The constant mode gives the unique zero eigenvalue. For each pair \(k\) and \(m-k\) with \(1\le k<m/2\), the span of \(e_k,e_{m-k}\) is invariant; its \(L_m\) matrix has determinant
\[
(2-\zeta^k)(2-\zeta^{-k})-1
=4\bigl(1-\cos(2\pi k/m)\bigr)
=2(1-\zeta^k)(1-\zeta^{-k}).
\]
For even \(m\), the remaining mode \(k=m/2\) contributes eigenvalue four. Applying the cyclotomic identity \(\prod_{k=1}^{m-1}(1-\zeta^k)=m\): if \(m=2r+1\), the product of nonzero eigenvalues is \(m2^r\); if \(m=2r\), the paired product is \(2^{r-1}(m/2)\) and the exceptional eigenvalue four makes the total \(m2^r\). For \(m=1\) the empty eigenvalue product equals one. Hence in every case
\[
\tau_r(H_m)=2^{\lfloor m/2\rfloor}
=2^{\lfloor(n-2)/2\rfloor}.
\]
This completes the proof.

## Verification
The standalone `verify.py` reconstructs the unrestricted weight-one/two edge-labeled de Bruijn graph, enumerates its Euler tours anchored at the unique edge \(0^{n-2}1\), reconstructs the contracted two-arc graph independently, and computes exact Laplacian cofactors by fraction-free integer elimination. These three calculations agree with the formula at each \(n=3,\ldots,12\). The code additionally verifies the circular factors for every enumerated tour. Small-length independent direct binary-word enumeration checks the same counts for \(n=3,4,5,6\). Run `python3 verify.py` with a standard Python 3 installation. These finite tests supplement, rather than replace, the all-length proof.

## Relationship to prior work
Ruskey, Sawada, and Williams (2012) developed the fixed-weight shorthand representation, proved existence and constructed universal cycles through constrained de Bruijn graphs and cool-lex necklace concatenation. Their graph framework is the starting point here; the new asserted contribution is the **closed population count at weight two**, via a contracted rotation-reflection digraph and a Fourier/matrix-tree evaluation, rather than an existence or construction statement.

Chen, Sima, and Milenkovic (2025) analyze orthogonal families of fixed-weight de Bruijn sequences; orthogonality is a packing constraint on several cycles and is not the population count for one shorthand universal cycle. Standard BEST and matrix-tree theorems are credited as background tools. The indicated searches did not establish that the displayed specialized closed formula appeared previously, but this is not a claim of independently certified historical priority.

## Limitations
The count is restricted to binary weight **exactly two in the original length-\(n\) subset representation**, equivalently weights one or two at length \(n-1\). It neither gives a formula for arbitrary subset size nor for pairwise orthogonal collections. It does not identify rotations with reflections or complementation. Earlier unindexed enumerations or an implicit formula in otherwise broader literature remain possible. No independent validation has been performed.

## References
1. F. Ruskey, J. Sawada, A. Williams, *De Bruijn Sequences for Fixed-Weight Binary Strings*, SIAM Journal on Discrete Mathematics 26(2), 605–617 (2012), DOI `10.1137/100808782`, publicly available May 8, 2012. Full relevant Sections 1–2, 6–7 consulted at https://www.researchgate.net/publication/265351686_De_Bruijn_Sequences_for_Fixed-Weight_Binary_Strings.
2. Y.-P. Chen, J. Sima, O. Milenkovic, *Generalized Orthogonal de Bruijn and Kautz Sequences*, Entropy 27(4), 366 (2025), DOI `10.3390/e27040366`. Relevant definitions and Section 5 consulted at https://www.mdpi.com/1099-4300/27/4/366.
3. Standard directed Euler-tour (BEST) theorem and directed matrix-tree theorem, used in their conventional multigraph forms.
