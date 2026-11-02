# Exact universal-cycle enumeration for nonadjacent repeated letters

## Finding

Let \(q\ge3\) be an integer, and let \(\Sigma_q\) be a labeled alphabet of \(q\) symbols. Define the length-four language
\[
\mathcal N_q=\{abac,\ abca,\ abcb:\ a,b,c\in\Sigma_q\text{ are pairwise distinct}\}.
\]
Every member has precisely three different symbols, with its unique repeated symbol in nonconsecutive positions. An **oriented universal cycle** is a circular word with exactly one cyclic length-four occurrence of every member of \(\mathcal N_q\), and no other length-four factors. Identify cycles under rotations of the circular word only; do not identify reversal or alphabet relabeling.

Such cycles exist for every \(q\ge3\), have length \(3q(q-1)(q-2)\), and their exact count is \(U_3=12\). For every \(q\ge4\), their number is
\[
\boxed{U_q=\frac{2^{q-1}q^{q-2}(q-2)^{q-1}}{q-1}\;7^{q(q-2)(q-4)/3}\,[6(q-1)]^{q(q-3)/2}\,[2(4q-5)]^{(q-1)(q-2)/2}\,((q-3)!)^{q(q-1)}.}
\]
For example, \(U_4=1,177,583,616\) and \(U_5=4,143,132,985,665,169,391,616,000,000,000\). Here factorials and exponentiation have their usual integer meanings. The exponent of \(7\) is integral because the product \(q(q-2)(q-4)\) is divisible by \(3\).

## Assumptions and scope

Symbols are distinguishable; cyclic words are compared by rotation alone. A length-four factor wraps around the circular boundary. The alphabet is exactly \(\Sigma_q\), but each individual permitted factor uses three symbols. In the proof, \(d=q-2\), \(P=q(q-1)\), and \(T=q(q-1)(q-2)\). The directed overlap graph has \(T+P=q(q-1)^2\) vertices, and its \(3T\) edges are labeled by the distinct permitted words. There is one universal cycle for each Euler tour with one fixed, specified labeled edge as its first edge.

## Proof

**1. Graph, degrees, and connectivity.** Introduce vertices \(D(a,b,c)=abc\) with pairwise distinct letters, and \(P(a,b)=aba\) with \(a\ne b\). Overlap of three consecutive symbols yields exactly the following edges:
\[
D(a,b,c)\longrightarrow D(b,c,a),\qquad
D(a,b,c)\longrightarrow P(b,c),\qquad
P(a,b)\longrightarrow D(b,a,c)\quad(c\notin\{a,b\}).
\]
They correspond, respectively, to the four-letter factors \(abca\), \(abcb\), and \(abac\). A \(D\)-vertex has indegree and outdegree \(2\); a \(P\)-vertex has both degrees \(d\). The graph is strongly connected: the first edge rotates an injective triple, while the two-edge route \(D(a,b,c)\to P(b,c)\to D(c,b,a)\) interchanges its first and last letters. Rotations and that transposition generate all six orders of a fixed three-element set. In the second step, any new letter different from \(b,c\) can replace the former first letter, connecting all three-element supports via single-letter exchanges (for \(q=3\), there is only one support). Every \(P\)-vertex is reached from a suitable \(D\)-vertex and reaches one. Balanced strong connectivity gives Euler tours, hence universal cycles.

**2. A determinant for directed spanning trees.** Order vertices with all \(D\)'s first and all \(P\)'s second. Write \(R\) for the permutation \(D(a,b,c)\mapsto D(b,c,a)\), \(Q\) for the \(D\)-to-\(P\) adjacency, and \(S\) for the \(P\)-to-\(D\) adjacency. Then the directed outdegree Laplacian is
\[
L=\begin{pmatrix}2I-R&-Q\\-S&dI\end{pmatrix},\qquad R^3=I.
\]
On functions of the ordered pairs \((a,b)\), let \(Xf(a,b)=\sum_{c\notin\{a,b\}}f(a,c)\), \(Yf(a,b)=\sum_{c\notin\{a,b\}}f(c,b)\), and \(Jf(a,b)=f(b,a)\). Direct evaluation of the edge maps gives \(SQ=X\), \(SRQ=Y\), and \(SR^2Q=dJ\). Setting \(A=z+2\) and \(t=(z+d)(A^3-1)\), the Schur complement, initially over rational functions, proves the polynomial identity
\[
\det(zI+L)=(A^3-1)^{T/3-P}\det\bigl(tI_P-A^2X-AY-dJ\bigr).
\]
A negative intermediate exponent is permitted: the right-hand side is a rational expression identically equal to the left-hand polynomial. We evaluate it only at \(z=0\), where \(A^3-1=7\ne0\).

**3. Exact pair-space decomposition.** The \(P\)-dimensional real space of functions on ordered unequal pairs splits as the direct sum of:

* constants (dimension \(1\)), on which \(X,Y,J\) act by \(d,d,1\);
* two standard copies of the \((q-1)\)-dimensional zero-sum letter space, represented on \(f(a,b)=u\varphi(a)+v\varphi(b)\), with matrices
\[
X=\begin{pmatrix}d&-1\\0&-1\end{pmatrix},\quad
Y=\begin{pmatrix}-1&0\\-1&d\end{pmatrix},\quad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix};
\]
* symmetric pair-functions with all row sums zero, dimension \(m_+=q(q-3)/2\), on which \(X=Y=-I\) and \(J=I\);
* antisymmetric pair-functions with all row sums zero, dimension \(m_-=(q-1)(q-2)/2\), on which \(X=Y=-I\) and \(J=-I\).

These dimensions sum to \(P\). Orthogonality to constants and both standard copies forces zero row and column sums; symmetry or antisymmetry then gives the last two spaces. The dimension of the symmetric zero-row-sum space is \(\binom q2-q\), because the nonoriented-edge incidence rows of the complete graph have rank \(q\) for \(q\ge3\); the antisymmetric rank of the directed incidence map is \(q-1\), giving dimension \(\binom q2-q+1\). Thus the decomposition holds even at \(q=3\), where the symmetric space has dimension zero.

The constant eigenfactor simplifies exactly to
\[
t-d(A^2+A+1)=z(z+d+1)(A^2+A+1),
\]
whose derivative at zero is \(7(d+1)\). At \(z=0\), the standard block is
\[
\begin{pmatrix}3d+2&4-d\\2-d&5d+4\end{pmatrix}
\]
with determinant \(14d(d+2)=14dq\). The symmetric and antisymmetric scalar eigenfactors at zero are \(6(d+1)=6(q-1)\) and \(8d+6=2(4q-5)\), respectively. Consequently the coefficient of \(z\) in \(\det(zI+L)\) is
\[
7^{T/3-P}\,7(q-1)\,[14q(q-2)]^{q-1}\,[6(q-1)]^{m_+}\,[2(4q-5)]^{m_-}.
\]

**4. Directed matrix-tree and BEST normalization.** Since the graph is balanced and strongly connected, its \(T+P\) directed in-arborescence cofactors are equal. The directed matrix-tree theorem identifies their sum with the coefficient above. Hence every cofactor is exactly
\[
\tau_q=\frac{7^{\,1+q(q-1)(q-5)/3}}{q(q-1)}[14q(q-2)]^{q-1}[6(q-1)]^{m_+}[2(4q-5)]^{m_-}.
\]
The BEST theorem, with a particular four-letter edge fixed as the first edge, counts Euler tours as \(\tau_q\prod_v(\deg^+(v)-1)!\). There are \(T\) vertices of degree \(2\) and \(P\) vertices of degree \(q-2\), so this product is \(((q-3)!)^P\). Each oriented universal cycle has exactly one rotation beginning with the specified edge, because each permitted length-four word occurs once. This establishes \(U_q=\tau_q((q-3)!)^P\). Simplification of the powers of \(7,q,q-2\) gives the boxed formula for \(q\ge4\); direct substitution at \(q=3\) gives \(12\). This finishes the proof.

## Verification

Run the included standalone Python file with `python verify.py` (Python standard library only). It independently generates the permitted language, constructs the full overlap graph, evaluates exact Laplacian cofactors using fraction-free integer elimination for \(q=3,4,5\), and compares them with the all-alphabet formula. It also enumerates all 12 rooted tours at \(q=3\), constructs and checks one complete universal cycle at each \(q=3,4,5,6\), and checks every cyclic length-four window of those witnesses. The expected final line is `VERIFY_OK`.

These finite checks are diagnostics, not substitutes for the determinant and connectivity proofs for all \(q\). No independent formal or external verification is claimed.

## Relationship to prior work

Gardner and Godbole's *Universal Cycles of Restricted Words* (first publicly available 2017-11-19, arXiv:1711.07029v1) establishes existence for several much broader families, notably augmented onto words; those existence results do not enumerate oriented cycles of the specific nonadjacent-repeat language. The earlier Leitner–Godbole *Universal Cycles of Classes of Restricted Words* (arXiv:0808.1309) treats existence for onto and almost-onto collections and does not give the present exact count. Chen–Kitaev–Sun (arXiv:1908.01116v1) analyze probabilities for removing words from full de Bruijn languages and small binary cases; their reported probability bounds and cases do not imply this fixed structured all-alphabet count. Classical directed matrix-tree and BEST theorems provide counting tools, but the sparse adjacency and its four-isotypic-space determinant are specific here.

Other restricted four-letter universal-cycle families, including those with adjacent repeated positions or only two distinct symbols, have different edge sets. Their universal-cycle counts do not determine this one. Public literature and computational searches may miss an equivalent formulation; novelty is not independently certified.

## Limitations

The count identifies only rotations, not reversal or symbol relabeling. No asymptotic estimate, classification of cycles by symmetry, or counts for length-five patterns is claimed. The new part of the argument is the exact restricted overlap-graph spectrum; the directed matrix-tree and BEST theorems are standard. The proof is a same-manuscript mathematical derivation supported by executable checks and has not undergone independent audit or refereeing.

## References

1. K. B. Gardner and A. Godbole, *Universal Cycles of Restricted Words*, arXiv:1711.07029v1 (2017-11-19), https://arxiv.org/abs/1711.07029.
2. A. Leitner and A. Godbole, *Universal Cycles of Classes of Restricted Words*, arXiv:0808.1309 (2008), https://arxiv.org/abs/0808.1309.
3. H. Z. Q. Chen, S. Kitaev, and B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116v1 (2019-08-03), https://arxiv.org/abs/1908.01116.
4. The directed matrix-tree theorem and the de Bruijn–van Aardenne-Ehrenfest–Smith–Tutte (BEST) theorem (standard graph-enumeration identities).
