# Tangent-line criterion for ternary two-qubit local unambiguous discrimination
## Finding
For any linearly independent triple \(S=\{\lvert\psi_1\rangle,\lvert\psi_2\rangle,\lvert\psi_3\rangle\}\subset\mathbb C^2\otimes\mathbb C^2\), fix \(k\in\{1,2,3\}\). Identify a two-qubit vector \(\sum_{a,b=0}^1 x_{ab}\lvert ab\rangle\) with its coefficient matrix \(X=(x_{ab})\), so that the vector is a product state exactly when \(\det X=0\).

Let
\[
W_k=\operatorname{span}\{\psi_j:j\ne k\}^{\perp}.
\]
Because the triple is linearly independent, \(W_k\) is two-dimensional and \(W_k\cap\psi_k^{\perp}\) is one-dimensional. Choose a nonzero coefficient matrix \(C_k\) spanning that intersection, and choose any \(D_k\in W_k\setminus\mathbb C C_k\). Then \(\lvert\psi_k\rangle\) has no product detector for LOCC-unambiguous discrimination if and only if
\[
\det C_k=0,\qquad
\operatorname{tr}(\operatorname{adj}(C_k)D_k)=0,\qquad
\det D_k\ne0.
\]
Equivalently, the projective line \(\mathbb P(W_k)\) is tangent to the Segre quadric of product states at the unique point \(\mathbb P(W_k\cap\psi_k^{\perp})\). Therefore the complete triple is locally unambiguously discriminable exactly when this tangency obstruction is absent for each \(k=1,2,3\).

This turns the first exceptional case highlighted by Yang et al.—three states on two qubits—into three explicit quadratic tests rather than an existential search over product detectors.

## Assumptions and scope
The three states are pure and linearly independent and live on \(\mathbb C^2\otimes\mathbb C^2\). "Locally unambiguously discriminable" is used in the standard LOCC sense in which every state must have a product detecting vector orthogonal to all the other candidate states but not to that state. No claim is made about the optimum success probability, minimum-error discrimination, mixed-state ensembles, or larger local dimensions.

The matrix identification depends on local computational bases, but the criterion does not: local changes of basis act by invertible left/right matrix multiplication and preserve rank one, while replacing \(D_k\) by \(\alpha D_k+\beta C_k\) with \(\alpha\ne0\) preserves the three-way obstruction because, when the first two displayed quantities vanish, \(\det(\alpha D_k+\beta C_k)=\alpha^2\det D_k\).

## Proof
Fix \(k\). Chefles's product-detector criterion says that \(\lvert\psi_k\rangle\) is locally unambiguously identifiable from the triple exactly when there is a product vector \(\phi\in W_k\) with \(\langle\psi_k\mid\phi\rangle\ne0\).

Since the triple is linearly independent, the linear functional \(\phi\mapsto\langle\psi_k\mid\phi\rangle\) is nonzero on \(W_k\). Hence its kernel inside \(W_k\) is exactly the line spanned by \(C_k\). Every vector in \(W_k\) has the form
\[
X(s,t)=sC_k+tD_k.
\]
Moreover,
\[
\langle\psi_k\mid X(s,t)\rangle=t\langle\psi_k\mid D_k\rangle,
\]
so a product vector detects \(\psi_k\) exactly when \(\det X(s,t)=0\) for some projective point \([s:t]\) with \(t\ne0\).

For \(2\times2\) matrices, determinant polarization gives the homogeneous quadratic
\[
p_k(s,t)=\det(sC_k+tD_k)
=s^2\det C_k+st\operatorname{tr}(\operatorname{adj}(C_k)D_k)+t^2\det D_k.
\]
If \(p_k\equiv0\), then \(D_k\) itself is product and is a detector because \(D_k\notin\mathbb C C_k\). If \(p_k\not\equiv0\), the fundamental theorem of algebra gives two projective zeros counted with multiplicity. There is no zero with \(t\ne0\) precisely when the only zero is \([1:0]\) with multiplicity two, i.e. precisely when
\[
\det C_k=0,
\quad
\operatorname{tr}(\operatorname{adj}(C_k)D_k)=0,
\quad
\det D_k\ne0.
\]
This proves the algebraic criterion.

The product states in \(\mathbb P(\mathbb C^2\otimes\mathbb C^2)\cong\mathbb P^3\) form the Segre quadric \(Q=\{\det X=0\}\). The restriction of its defining quadratic to \(\mathbb P(W_k)\) is exactly \(p_k\). A single double intersection at \([C_k]\) is therefore exactly tangency of \(\mathbb P(W_k)\) to \(Q\) at \([C_k]\), proving the geometric formulation. Applying the product-detector criterion for all three indices gives the final equivalence for the entire triple.

As a boundary example, for
\[
\lvert\psi_1\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2,\quad
\lvert\psi_2\rangle=(\lvert00\rangle-\lvert11\rangle)/\sqrt2,\quad
\lvert\psi_3\rangle=\lvert10\rangle,
\]
the source's two-qubit obstruction is recovered: the tangent criterion holds for \(k=1,2\), while for \(k=3\) the relevant line meets the product quadric in two distinct points, so only \(\psi_3\) has a product detector.

## Verification
The proof is exact finite-dimensional algebra. The bundled `verify.py` independently constructs \(W_k\), the adapted pair \((C_k,D_k)\), and the quadratic coefficients. It checks the displayed Bell-pair obstruction and then compares the algebraic criterion with direct roots of the restricted determinant polynomial on one thousand random linearly independent complex triples. Its packaged execution returned `VERIFY_OK random_triples=1000 known_obstruction=passed`.

The random test is only a regression check; it is not evidence for the universal quantifier. The universal statement is established by the quadratic-factor proof above.

## Relationship to prior work
Chefles gives the general necessary-and-sufficient LOCC criterion in terms of the existence of a product detecting state. Yang et al. restate that criterion and identify multiqubit systems, including \(2\otimes2\), as the exceptional setting where arbitrary three-state sets need not all be locally unambiguously discriminable; their explicit two-qubit witness is the Bell-pair-plus-product triple used above. Their inspected text does not classify which ternary two-qubit triples fail or give an algebraic test for failure.

Niu and Griffiths prove that every two-dimensional subspace of \(\mathbb C^2\otimes\mathbb C^2\) contains a product vector and note that generically there are two; their proof is the same underlying quadratic intersection with the product-state surface. They do not connect the double-root/tangent case to product detecting vectors for a ternary LOCC discrimination problem.

The contribution here is the exact synthesis: for the smallest exceptional discrimination problem, failure is not merely "lack of a suitable product state" but precisely tangency of one explicitly determined projective line to the Segre quadric at the state-orthogonal point, equivalently the three scalar matrix conditions above.

## Limitations
The criterion is specialized to three linearly independent pure states on two qubits. The determinant is quadratic only because both local dimensions equal two; higher local dimensions lead to different determinantal geometry. The result does not optimize inconclusive probability or claim a protocol achieving a globally optimal unambiguous measurement probability.

The algebra is short once Chefles's detector condition and the two-qubit product quadric are placed together, so there is residual literature risk that an equivalent tangency criterion appears under algebraic-geometric or matrix-pencil terminology in an unindexed source. Targeted searches did not locate such a statement.

## References
1. Y.-H. Yang, F. Gao, G.-J. Tian, T.-Q. Cao, H.-J. Zuo, and Q.-Y. Wen, “Bound on local unambiguous discrimination between multipartite quantum states,” Quantum Information Processing 14, 731–737 (2015), DOI 10.1007/s11128-014-0870-3; published online 2014-11-12.
2. A. Chefles, “Condition for unambiguous state discrimination using local operations and classical communication,” Physical Review A 69, 050307(R) (2004), DOI 10.1103/PhysRevA.69.050307.
3. C.-S. Niu and R. B. Griffiths, “Two qubit copying machine for economical quantum eavesdropping,” arXiv:quant-ph/9810008; Physical Review A 60, 2764–2776 (1999), DOI 10.1103/PhysRevA.60.2764.
