# The clique-start obstruction to adjacency–Laplacian quantum-walk equivalence on complete split graphs

## Finding
For integers \(a,b\ge1\), form the graph \(G_{a,b}=K_a\vee\overline K_b\), with a clique \(C\) of size \(a\) joined to an independent set \(I\) of size \(b\). Starting at a single vertex \(v\), let \(p_A(w,t)=|\langle e_w,e^{itA}e_v\rangle|^2\) and \(p_L(w,t)=|\langle e_w,e^{itL}e_v\rangle|^2\), where \(L=A-D\). For **every clique start \(v\in C\)**, the return-probability difference is
\[
p_A(v,t)-p_L(v,t)=-\frac{b(b-1)(2a+b-3)}{12}t^4+O(t^6).
\]
In particular it is strictly negative for sufficiently small nonzero real \(t\) whenever \(b\ge2\). This uniform clique-start obstruction is the contribution of the result.

Combining it with the established independent-set-start criterion from *Exterior-state adjacency–Laplacian equivalence on weighted split joins* (reference 3, at unit weights) gives the complete classification:
\[
(\forall w\in V(G_{a,b}))(\forall t\in\mathbb R)\quad p_A(w,t)=p_L(w,t)
\]
holds if and only if **either** \(b=1\) (the graph is complete, with arbitrary initial vertex) **or** \(a\ge2\), \(b=2a-1\), and \(v\in I\).

For context, the exterior-start equality in the irregular family can be expressed in the signed amplitude form
\[
e^{itL}e_v=e^{-iat}S\,\overline{e^{itA}e_v},\qquad
S_{ww}=\begin{cases}+1,&w\in I,\\-1,&w\in C.\end{cases}
\]
The bar denotes entrywise complex conjugation in the vertex basis. This relation follows from the invariant blocks used in the established exterior-start criterion; it is included for a self-contained proof, not as a separate novelty claim. The classification is **within complete split graphs**, not among arbitrary graphs.

## Assumptions and scope
All graphs are finite, unweighted, undirected, loopless, and labeled; the join contains all edges between \(C\) and \(I\). The parameters \(a,b\) are arbitrary positive integers. Time is an arbitrary real number, and the same time and edge weight are used in both unitary evolutions. The initial state must be a localized vertex vector, not an arbitrary superposition. The negative-Laplacian convention \(L=A-D\) agrees with the primary quantum-walk reference. The result concerns all vertex-resolved **position probabilities**, not equality of amplitudes without complex conjugation, equality for arbitrary initial states, or mixing times.

## Proof
**1. Bright/dark decomposition and necessary frequency constraint.** Write the normalized uniform part vectors as
\[
|I\rangle=b^{-1/2}\sum_{w\in I}e_w,\qquad
|C\rangle=a^{-1/2}\sum_{w\in C}e_w,
\]
and set \(s=\sqrt{ab}\), \(\delta=a-1\). On their two-dimensional invariant span, in the ordered basis \((|I\rangle,|C\rangle)\), the adjacency and negative-Laplacian operators have the matrices
\[
A_B=\begin{pmatrix}0&s\\s&\delta\end{pmatrix},\qquad
L_B=\begin{pmatrix}-a&s\\s&-b\end{pmatrix}.
\]
The zero-sum independent-vertex vectors form a dark subspace with eigenvalues \(0\) under \(A\) and \(-a\) under \(L\); the zero-sum clique-vertex vectors form another dark subspace with eigenvalues \(-1\) and \(-(a+b)\), respectively. These decompositions exhaust the vertex space, with zero-dimensional components allowed at size one.

For a source \(v\) on either part and a receiving vertex \(w\) on the opposite part, the dark components cannot contribute. The standard two-by-two exponential formula gives, in both source orientations,
\[
p_A(w,t)=\frac{4}{\Omega_A^2}\sin^2\!\left(\frac{\Omega_A t}{2}\right),\qquad
p_L(w,t)=\frac{4}{\Omega_L^2}\sin^2\!\left(\frac{\Omega_L t}{2}\right),
\]
where
\[
\Omega_A^2=(a-1)^2+4ab,\qquad \Omega_L^2=(a-b)^2+4ab.
\]
The Taylor series of either expression is \(t^2-\Omega^2t^4/12+O(t^6)\). Equality for every time forces \((a-1)^2=(a-b)^2\); since \(b\ge1\), this means \(b=1\) or \(b=2a-1\). The only members with \(b=2a-1\) and \(a=1\) again have \(b=1\).

**2. Sufficiency.** If \(b=1\), the graph is \(K_{a+1}\), all degrees equal \(a\), and \(e^{itL}=e^{-iat}e^{itA}\) globally. If instead \(b=2a-1\) with \(a\ge2\), let \(R=\operatorname{diag}(1,-1)\) on the ordered bright basis. Direct comparison yields
\[
L_B+a\mathbf 1=-R A_B R.
\]
Consequently \(e^{itL_B}=e^{-iat}R e^{-itA_B}R=e^{-iat}R\overline{e^{itA_B}}R\), since \(A_B\) is real. Every independent-vertex source splits into an independent dark vector plus a real multiple of \(|I\rangle\), and has no clique-dark component. On that dark subspace the same conjugation identity holds because \(A=0\) and \(L=-a\). Combining both summands proves
\[
e^{itL}e_v=e^{-iat}S\overline{e^{itA}e_v}\quad(v\in I),
\]
with the stated diagonal \(S\). Its entries all have modulus one, so all vertex probabilities agree.

**3. No clique start in an irregular member.** Let \(v\in C\), and for \(H\in\{A,L\}\) denote the diagonal return moments by \(m_j(H)=\langle e_v,H^je_v\rangle\). Since \(H\) is real symmetric, the \(t^4\) coefficient of the return probability \(|\langle e_v,e^{itH}e_v\rangle|^2\) is exactly
\[
\mathcal C_4(H)=\frac{m_4(H)}{12}-\frac{m_1(H)m_3(H)}3+\frac{m_2(H)^2}{4}.
\]
This follows by multiplying the fourth-order Taylor expansion of the amplitude and its conjugate. To evaluate these moments without omitted vertices, use the invariant three-cell coordinate system consisting of the chosen clique vertex, the other \(a-1\) clique vertices, and all \(b\) independent vertices; in this order the per-vertex-amplitude matrices are
\[
T_A=\begin{pmatrix}0&a-1&b\\1&a-2&b\\1&a-1&0\end{pmatrix},\qquad
T_L=T_A-\operatorname{diag}(a+b-1,a+b-1,a).
\]
Starting from the first coordinate vector, \(m_j(H)=(T_H^j)_{11}\). Direct multiplication and the displayed moment identity give
\[
\mathcal C_4(A)=\frac{a^3+3a^2b-a^2+ab^2+3b^2-3b}{12},\qquad
\mathcal C_4(L)=\frac{(a+b)^2(a+b-1)}{12}.
\]
Their difference simplifies exactly to
\[
p_A(v,t)-p_L(v,t)=-\frac{b(b-1)(2a+b-3)}{12}t^4+O(t^6).
\]
When \(a\ge1\) and \(b\ge2\), this coefficient is strictly negative. Therefore every irregular split graph fails the all-time equality test for a clique-localized source. With step 1 and step 2, both directions of the classification are proved. \(\square\)

## Verification
The standalone standard-library script `verify.py` constructs each full adjacency and negative-Laplacian matrix, independently of the bright decomposition. It checks exact rational fourth-order coefficients for each orientation of a cross-part transition and for every clique return, across all \(72\) pairs \(1\le a\le8\), \(1\le b\le9\). It independently checks the predicted yes/no classification by vertex-resolved matrix-exponential power series for all \(42\) pairs \(1\le a\le6\), \(1\le b\le7\), for both source types and three nonzero times. Run from this directory with `python3 verify.py`. The script uses no external packages. The infinite-parameter conclusions rest on the explicit algebraic proof, **not** on these finite computations or on a numerical tolerance.

## Relationship to prior work
Wong and Lockhart (2021) analytically establish two small examples and numerically report their eighth family: \(K_a\vee\overline K_{2a-1}\), with the walk localized in the independent part (Section IV). Reference 3 proves the independent-set-start criterion in greater generality: for clique size \(r\), exterior size \(s\), clique edge weight \(\alpha>0\), and join edge weight \(\eta>0\), equivalence from an exterior vertex holds exactly when \(\alpha(r-1)=\eta|r-s|\). This gives the criterion used here by taking unit weights. Changing the sign of a real symmetric Laplacian conjugates amplitudes and preserves transition probabilities. The weighted result does not classify clique starts; the distinct result here is the explicit clique return difference for every irregular unit-weight split graph, which completes the source classification. Kirkland, Monterde, and Plosker study transfer and periodicity of twin vertices, which are different observables from equality of all position probabilities across two Hamiltonians.

## Limitations
The clique-return result is for unweighted complete split graphs with localized starts; no obstruction for arbitrary weighted joins, irregular graphs, arbitrary source superpositions, or transfer/mixing-time behavior is asserted. The comparison with existing work is limited to the sources inspected. The numerical script tests finite sizes and times only; its results are consistency checks rather than an infinite proof.

## References
1. T. G. Wong and J. Lockhart, *Equivalent Laplacian and Adjacency Quantum Walks on Irregular Graphs*, arXiv:2107.05580 (first public 2021-07-12), https://arxiv.org/pdf/2107.05580 ; specifically Section IV and the concluding open questions.
2. S. Kirkland, H. Monterde and S. Plosker, *Quantum state transfer between twins in weighted graphs*, arXiv:2201.02720 (first public 2022-01-08), https://arxiv.org/pdf/2201.02720 ; in particular the distinctions among adjacency, Laplacian, periodicity and transfer.
3. *Exterior-state adjacency–Laplacian equivalence on weighted split joins*, Resultary record d7a52b140b8f, Finding and boundary/unit-weight cases, https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-exterior-state-adjacency-laplacian-equivalence-on-weighted-split--d7a52b140b8f/RESULT.md .
