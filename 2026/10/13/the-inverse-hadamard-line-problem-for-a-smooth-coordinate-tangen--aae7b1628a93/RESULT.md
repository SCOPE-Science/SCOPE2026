# The inverse Hadamard line problem for a smooth coordinate-tangent quadric has exactly two torus orbits

## Finding
Let \(W\subset\mathbf P^3_{\mathbf C}\) be any smooth quadric tangent to the four coordinate planes \(H_i=\{x_i=0\}\), for \(0\le i\le3\). For two projective lines, let \(L\star R\) denote the Zariski closure of their coordinatewise Hadamard products. Set
\[
\mathcal F(W)=\{(L,R)\in\operatorname{Gr}(1,3)\times\operatorname{Gr}(1,3):L\star R=W\}.
\]
The diagonal torus \(T=(\mathbf C^\times)^4/\mathbf C^\times\) acts by \(\delta\cdot(L,R)=(\delta L,\delta^{-1}R)\). For every such \(W\), there are lines \(L,R\) for which
\[
\mathcal F(W)=\bigl(T\cdot(L,R)\bigr)\;\sqcup\;\bigl(T\cdot(R,L)\bigr).
\]
These are **exactly two distinct free torus orbits** of ordered decompositions, each isomorphic to \((\mathbf C^\times)^3\). Switching the two factors interchanges the orbits; hence, modulo both coordinatewise reciprocal rescaling and factor interchange, the decomposition is unique. The statement is set-theoretic: no reducedness assertion is made about the scheme-theoretic fiber of a rational parameter map.

## Assumptions and scope
Work throughout over \(\mathbf C\). Coordinates \(x_0,\ldots,x_3\) on the target projective space are fixed, and no coordinate permutation is included in the equivalence relation. The quadric is smooth and all four fixed coordinate planes are tangent. A line is a reduced projective linear subspace of dimension one. The Hadamard product means the closure of coordinatewise products at pairs where at least one resulting coordinate is nonzero. The torus element \(\delta\) has four nonzero diagonal entries, modulo simultaneous scalar multiplication. No genericity assumption is imposed beyond these hypotheses.

## Proof
**1. Recover factors from the quadric.** Choose either ordering of the two rulings of the smooth quadric and a Segre isomorphism
\[
\psi:\mathbf P^1\times\mathbf P^1\longrightarrow W
\]
with \(\psi^*\mathcal O_W(1)=\mathcal O(1,1)\). A concrete choice is obtained by an invertible linear change of the defining quadratic form into the equation \(z_{00}z_{11}-z_{01}z_{10}=0\), followed by the standard Segre parametrization.

Write the pullback of coordinate \(x_i\) as a bilinear form \(s^\mathsf{T}C_i t\) with a \(2\times2\) matrix \(C_i\). Since \(H_i\) is tangent to \(W\), the divisor of this section on \(\mathbf P^1\times\mathbf P^1\) is the union of one line of each ruling. Thus \(C_i\) has rank one. The section is nonzero because a nondegenerate quadric is not contained in any hyperplane. Factor each section uniquely up to a nonzero scalar:
\[
\psi^*x_i=\ell_i(s)m_i(t),\qquad 0\le i\le3.
\]
The four sections \(\psi^*x_i\) form a basis of \(H^0(\mathbf P^1\times\mathbf P^1,\mathcal O(1,1))\): their target coordinates are linearly independent and both spaces of sections have dimension four. Consequently neither of the maps
\[
\lambda(s)=[\ell_0(s):\cdots:\ell_3(s)],\qquad
\mu(t)=[m_0(t):\cdots:m_3(t)]
\]
is constant. Each map is defined by four linear forms without a common zero and embeds \(\mathbf P^1\) as a projective line. Calling their images \(L\) and \(R\), we have the exact identity \(\psi(s,t)=\lambda(s)\star\mu(t)\). Thus \(L\star R=W\); in fact the Hadamard map is a morphism and an isomorphism for this pair.

**2. All decompositions have the displayed form.** Let any ordered pair \((L',R')\) satisfy \(L'\star R'=W\). Parameterize the lines by two copies of \(\mathbf P^1\), and pull back the four coordinate functions to products of linear forms. Since their image is not contained in a hyperplane, these four sections are linearly independent, and hence form the complete basis of \(H^0(\mathcal O(1,1))\). Therefore their map is basepoint-free and gives an isomorphism \(\mathbf P^1\times\mathbf P^1\to W\). The resulting isomorphism differs from \(\psi\) by an automorphism of the product. Every such automorphism either independently reparametrizes the two \(\mathbf P^1\) factors or first interchanges them. In the first case, uniqueness of each nonzero rank-one tensor factorization forces \(\ell'_i=a_i\ell_i\) and \(m'_i=a_i^{-1}m_i\), up to common projective scalars. Thus the pair lies in \(T\cdot(L,R)\). In the interchanging case it lies in \(T\cdot(R,L)\). Conversely every pair in either torus orbit has Hadamard product \(W\).

**3. The two orbits do not meet.** If \((R,L)=\delta\cdot(L,R)\), then \(R=\delta L\). This would imply \(W=L\star R=\delta(L\star L)\). But when a projective line is parametrized by \(s_0,s_1\), the four coordinates of \(L\star L\) are quadratic binary forms, all belonging to the three-dimensional vector space \(\operatorname{Sym}^2\mathbf C^2\); the resulting variety lies in a projective plane. This contradicts the fact that a smooth quadric spans \(\mathbf P^3\). Hence the two orbits are disjoint.

**4. Both torus actions are free.** Suppose \(\delta L=L\) and \(\delta^{-1}R=R\). The induced automorphisms of the two source lines give the same coordinatewise product as the identity pair. Since \(L\times R\to W\) is an isomorphism, both induced automorphisms must be the identity. Because \(L\) is not contained in a coordinate hyperplane, a point of \(L\) has all four coordinates nonzero. A diagonal projective transformation fixing this point is scalar and hence the identity in \(T\). Thus each stabilizer is trivial. This also establishes the isomorphism of each orbit with the three-dimensional algebraic torus.

## Verification
The proof is universal and uses no finite enumeration. For an independent exact sample, choose
\[
L=[s_0:s_1:s_0+s_1:s_0+2s_1],\quad
R=[t_0:t_1:t_0+3t_1:t_0+5t_1].
\]
With Segre monomials ordered \((s_0t_0,s_0t_1,s_1t_0,s_1t_1)\), the coordinate-change matrix is
\[
M=\begin{pmatrix}1&0&0&0\\0&0&0&1\\1&3&1&3\\1&5&2&10\end{pmatrix},\qquad\det M=1.
\]
Thus this product parametrizes a smooth quadric. In target coordinates its equation is
\[
x_0x_1-(-x_0+4x_1+2x_2-x_3)(2x_0-15x_1-5x_2+3x_3)=0.
\]
The inverse symmetric matrix of this equation has zero diagonal, proving tangency to the four coordinate planes. The included standard-library-only `verify.py` checks the exact invertible matrix, four rank-one coordinate tensors, four tangencies, and the defining polynomial identity. Its output is in `verification_output.txt`; these finite checks corroborate this example, not the universal theorem.

## Relationship to prior work
Antolini, Ballico and Oneto, *Algebraic surfaces as Hadamard products of curves*, arXiv:2502.18813 (initially public 2025-02-26), prove that products of two lines producing quadrics are smooth and tangent to all four coordinate planes (Lemma 3.2), characterize their five-dimensional family (Theorem 1.1), and reconstruct the **quadric from its singular coordinate locus** (Theorem 3.9). They explicitly ask how to reconstruct the two lines from the quadric in Question 3.12; reciprocal diagonal nonuniqueness is already in their Remark 2.4. Their dimension-three parameter-fiber calculation does not classify its two ordered scaling orbits. The finding here answers that inverse problem, both constructively and for every smooth member, and identifies the precise ambiguity.

Bocci, Carlini and Kileel, *Hadamard products of linear spaces* (2016), analyze Hadamard products, ruling geometry and identifiability for points of fixed linear spaces; the relevant Corollary 6.5 does not reconstruct unknown lines from a supplied quadric. Ballico, *Real Ghosts of Complex Hadamard Products* (2024), treats cancellation, symmetries and real ghosts, but the examined statements do not classify this inverse-fiber problem.

## Limitations
The classification concerns complex smooth quadrics tangent to all four fixed coordinate planes, ordered pairs of projective **lines**, and equivalence under reciprocal diagonal rescaling; it excludes singular quadrics, higher-degree factors and descent over non-algebraically-closed fields. The two-orbit assertion is set-theoretic: possible nonreduced scheme structures of parameter fibers are not determined. The exact sample cannot replace the general proof. An older equivalent statement indexed through projective Segre geometry rather than Hadamard products remains a residual literature risk.

## References
1. D. Antolini, E. Ballico and A. Oneto, *Algebraic surfaces as Hadamard products of curves*, arXiv:2502.18813v1 (2025); revised v2 (2026), Sections 2–3, especially Lemma 3.2, Theorem 1.1 and Question 3.12. https://arxiv.org/html/2502.18813v2
2. C. Bocci, E. Carlini and J. Kileel, *Hadamard products of linear spaces*, Journal of Algebra 448 (2016), 595–617, Section 6 and Corollary 6.5. https://web.math.princeton.edu/~jkileel/HadamardPublished.pdf
3. E. Ballico, *Real Ghosts of Complex Hadamard Products*, Symmetry 16 (2024), article 1300, Sections 2–4. https://doi.org/10.3390/sym16101300
4. C. Bocci and E. Carlini, *Hadamard Products of Projective Varieties*, Birkhäuser (2024), especially the chapter *Grids and Rulings*. https://doi.org/10.1007/978-3-031-54263-3
