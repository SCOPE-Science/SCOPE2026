# Exact binary nullity for mixed-parity Cartesian products of cliques

## Finding
Let \(d\geq 2\) and \(q_1,\ldots,q_d\geq 2\) be integers, at least one even. On the Cartesian product \(G=K_{q_1}\square\cdots\square K_{q_d}\), let \(M=I+A(G)\) act on vertex configurations over \(\mathbb F_2\). Define \(E=\{i:q_i\text{ even}\}\), \(O=\{i:q_i\text{ odd}\}\), and
\[
P_E=\prod_{i\in E}q_i,\quad R_E=\prod_{i\in E}(q_i-2),\qquad P_O=\prod_{i\in O}q_i,\quad R_O=\prod_{i\in O}(q_i-2).
\]
An empty product is \(1\). Then the exact binary nullity is
\[
\boxed{\dim_{\mathbb F_2}\ker M=\frac{P_E+R_E}{2}\cdot\frac{P_O+(-1)^{d+1}R_O}{2}.}
\]
In particular, the all-on configuration has exactly \(2^{\dim\ker M}\) distinct binary press patterns that turn every light off. The Lights Out game is universally solvable (and the all-on press pattern unique) exactly when all \(q_i\) are even and \(d\) is even.

For every integer \(r\geq1\), the product \(K_{2r}\square K_3\) has nullity \(2r-1\), although the characteristic-polynomial gcd lower bound considered by Peters, Goldwasser and Young has degree only \(1\). Thus the excess over that lower bound is unbounded.

## Assumptions and scope
Every \(K_{q_i}\) is a loopless complete graph on \(q_i\) vertices; vertices of \(G\) are tuples and two vertices are adjacent if and only if exactly one coordinate differs. Pressing a vertex toggles its own light and its neighbors (closed-neighborhood switching). Press patterns are binary vectors, so pressing twice has no net effect. The theorem requires at least one even alphabet; it does not make an originality claim for the all-odd case.

## Proof
Over \(\mathbb F_2\), write \(J_i\) for the operator that sums coordinates in the \(i\)-th tensor factor and repeats that sum at every value of that coordinate. Since \(A(K_q)=J_q+I_q\) in characteristic two,
\[
M=(d+1)I+\sum_{i=1}^d J_i.
\]
For each odd \(q\), \(J_q^2=J_q\). Its \(1\)-eigenspace is the constant line and its \(0\)-eigenspace has dimension \(q-1\). Decompose the tensor product over all odd indices by choosing for each coordinate either its constant line or its zero-eigenspace. If exactly \(k\) odd indices use their constant line, the operator on the even-index tensor space is \(N+(d+1+k)I\), where \(N=\sum_{i\in E}J_i\). The total multiplicity of odd-index choices with \(d+1+k\) even is, by parity extraction,
\[
s=\frac{P_O+(-1)^{d+1}R_O}{2};
\]
here \(P_O=\prod_{i\in O}((q_i-1)+1)\) and \(R_O=\prod_{i\in O}((q_i-1)-1)\).

For even \(q\), \(J_q^2=0\) and \(\operatorname{rank}J_q=1\). Choose a two-dimensional invariant summand \(U_q=\langle e_1,\mathbf1\rangle\), with \(J_q e_1=\mathbf1\), \(J_q\mathbf1=0\), and a complementary trivial summand \(W_q\subset\ker J_q\) of dimension \(q-2\). Tensoring the choices of \(U_q\) or \(W_q\) over even indices decomposes their whole tensor space. On the all-trivial summand, of dimension \(R_E\), the operator \(N\) vanishes. On any summand containing a \(U_q\), define \(h\) on one chosen \(U_q\) by \(h(\mathbf1)=e_1\) and \(h(e_1)=0\), tensored with identities on other factors. Then \(Nh+hN=I\): the chosen coordinate contributes \(J_qh+hJ_q=I\), and each other coordinate contributes twice a commuting term, which is zero in characteristic two. Also \(N^2=0\), since every \(J_i^2=0\) and distinct terms commute. Consequently, \(\ker N=\operatorname{im}N\) on each such summand; its kernel has half the summand's dimension. Therefore
\[
\dim\ker N=R_E+\frac{P_E-R_E}{2}=\frac{P_E+R_E}{2}.
\]
Because \(N^2=0\), the operator \(I+N\) is its own inverse. Only odd-index summands with scalar term zero contribute to the kernel; there are \(s\) such weighted choices. Multiplication yields the displayed nullity formula.

Write \(e=|E|\). The degree of \(G\) has parity \(e\). If \(e\) is even, pressing all vertices gives \(M\mathbf1=\mathbf1\). If \(e\) is odd, choose an even coordinate \(i\) and one symbol \(a\) in its alphabet. Press exactly the vertices whose \(i\)-th coordinate equals \(a\). The indicator \(f\) obeys \(J_i f=\mathbf1\) and \(J_jf=(q_j\bmod 2)f\) for \(j\ne i\), so \(Mf=\mathbf1+(e+1\bmod 2)f=\mathbf1\). Thus all-on is solvable in both cases, and every solution is a translate of \(\ker M\).

Since \(P_E+R_E>0\), the nullity vanishes precisely when \(s=0\). If \(O\ne\varnothing\), then \(P_O>R_O\geq1\), so \(s>0\). If \(O=\varnothing\), then \(s=(1+(-1)^{d+1})/2\), which vanishes exactly when \(d\) is even. This proves the uniqueness assertion.

Finally, for \(G=K_{2r}\square K_3\), one has \(P_E=2r\), \(R_E=2r-2\), \(P_O=3\), \(R_O=1\), \(d=2\), hence \(\nu=2r-1\). In characteristic two, the characteristic polynomials of the factor adjacency matrices are \(p_{K_{2r}}(x)=(x+1)^{2r}\) and \(p_{K_3}(x)=x(x+1)^2\); therefore \(\deg\gcd(p_{K_{2r}}(x+1),p_{K_3}(x))=\deg x=1\). The excess \(2r-2\) grows without bound.

## Verification
A standalone exact-arithmetic program, \(\texttt{verify\_hamming\_lights.py}\), separately constructs the closed-neighborhood toggle matrix by enumerating all vertices and neighbors, calculates its rank using binary row elimination, and checks both a predicted kernel dimension and an explicit all-on press vector. It passed on 109 distinct admissible graphs with dimensions \(2\) through \(4\), coordinate sizes \(2\) through \(4\), and at most 180 vertices; this covered 6,230 exact toggle equations. Small examples include \(\nu(K_4\square K_3)=3\), \(\nu(K_2\square K_4)=0\), and \(\nu(K_2\square K_3\square K_4)=8\). The finite computations corroborate but do not replace the proof for all parameters.

## Relationship to prior work
Peters, Goldwasser and Young (2017) proved a general characteristic-polynomial test for universal solvability on Cartesian products and gave the two-factor even-clique criterion. Their two-factor criterion is prior work, not claimed here. Curtis, Earl, Livingston and Shader (2018) proved a general Sylvester-equation nullity formula in terms of Jordan blocks or invariant factors that applies in principle to *any* two-factor Cartesian product, hence to repeated products after further calculation. The new contribution asserted here is the uniform closed expression for arbitrary mixed-parity clique factors, its explicit all-on witnesses, and its growing comparison gap; the general rank method itself is not new. Ducey and Jalil (2013) analyzed modular Cartesian-clique Smith data in the regime where the characteristic does not divide the number of vertices, covering the all-odd case in characteristic two, which is excluded from this claim. Codsi, Cristancho, Divoux and Sivashankar (2026) study parity and extremality for Lights Out on arbitrary graphs; no explicit multi-factor nullity is taken from that source. The 2021 continuation by Munter and Peters treats solvability over other rings and other graph products, not this closed binary formula.

## Limitations
The theorem assumes at least one even coordinate size. It does not determine minimum-weight winning press patterns or the full Hamming-weight enumerator of null patterns. Its uniqueness classification includes a previously known two-factor even-clique case. Earlier general Sylvester formulas provide a non-closed-form computational route to every instance, so the contribution is an explicit evaluated family rather than a new universal rank theory. Relevant unindexed equivalent formulas remain a bibliographic risk; no independent audit has been performed.

## References
- A. Codsi, A. Cristancho, T. Divoux, and S. Sivashankar, *Extremal Graphs for the Lights Out Problem*, arXiv:2602.07241v1 (2026).
- T. Peters, J. Goldwasser, and M. Young, *Lights Out! on Cartesian Products*, Electronic Journal of Linear Algebra **32** (2017), 464–474, DOI: 10.13001/1081-3810.3483.
- B. Curtis, J. Earl, D. Livingston, and B. Shader, *Resolution of Conjectures Related to Lights Out! and Cartesian Products*, arXiv:1802.05359v1 (2018).
- J. E. Ducey and M. Jalil, *Integer Invariants of Abelian Cayley Graphs*, arXiv:1308.2335v2 (2013).
- R. Munter and T. Peters, *Lights Out! on Graph Products over the Ring of Integers Modulo k*, Electronic Journal of Linear Algebra **37** (2021), 416–424, DOI: 10.13001/ela.2021.5601.
