# Laplacian spectrum and integral-spectrum boundary for line graphs of matching-deleted cliques

## Finding
For integers \(n\ge4\) and \(0\le t\le\lfloor n/2\rfloor\), let \(G_{n,t}\) be the complete graph on \(n\) labeled vertices with a matching of \(t\) edges deleted, and let \(H_{n,t}=L(G_{n,t})\) be its line graph. Write \(m=\binom n2-t\). The following formulas determine the complete Laplacian characteristic polynomial \(P_{n,t}(\lambda)=\det(L(H_{n,t})-\lambda I_m)\), and give the sharp integrality classification:

\[
\boxed{H_{n,t}\text{ is Laplacian integral}\quad\Longleftrightarrow\quad t=0\ \text{or}\ 2t=n\ \text{or}\ (n,t)=(4,1).}
\]

For \(t=0\) (the triangular graph),
\[
P_{n,0}(\lambda)=(-\lambda)(n-\lambda)^{n-1}(2n-2-\lambda)^{m-n}.
\]
For \(t\ge1\), put \(r=n-2t\) and abbreviate
\[
\begin{aligned}
x&=2n-4-\lambda,&y&=2n-3-\lambda,&z&=2n-2-\lambda,\\
U&=\lambda^2-(3n-5)\lambda+2n^2-6n-2t+6,\\
V&=\lambda^2-(3n-3)\lambda+2n^2-2n-2t,\\
W&=\lambda^2-(3n-3)\lambda+2n^2-3n-2t,\\
Q&=\lambda^2-(3n-3)\lambda+2n^2-2n-4t.
\end{aligned}
\]
If \(r=0\), then
\[
\boxed{P_{n,t}(\lambda)=(-\lambda)x^{2t(t-2)}(n-2-\lambda)^t(n-\lambda)^{t-1}.}
\]
If \(r\ge1\), then the following expression **after the displayed exact cancellations** is a polynomial:
\[
\boxed{P_{n,t}(\lambda)=(-\lambda)
 x^{2t(t-2)}y^{(2t-1)(r-1)}z^{r(r-3)/2}
 U^tV^{t-1}W^{r-1}Q.}
\]
The only potentially negative powers are resolved by these identities in the indicated boundary cases:
\[
\begin{array}{ll}
t=1:& U=x(n-1-\lambda),\quad Q=x(n+1-\lambda);\\
r=1:&Q=z(n-1-\lambda);\\
r=2:&W=z(n-1-\lambda).
\end{array}
\]
Here a negative exponent denotes a factor to cancel *before* polynomial evaluation; it is not a spectral pole. The formulas include all boundary cases. For example \(P_{4,1}(\lambda)=-\lambda(3-\lambda)^2(5-\lambda)^2\).

## Assumptions and scope
All graphs are finite, simple and undirected. A matching means pairwise vertex-disjoint edges; all choices of the removed matching yield isomorphic graphs. The Laplacian is degree matrix minus adjacency matrix, including the usual zero eigenvalue. A graph is Laplacian integral when **every** Laplacian eigenvalue is an integer. The entire theorem applies to every integer \(n\ge4\) and every integer \(t\) in the range above. No assertion is made about deletions that are not matchings or about adjacency spectra of the line graphs.

## Proof
**Incidence determinant.** Set \(a=2t\). Divide the vertices of the base graph into the \(a\) endpoints \(A\) of the deleted matching and the \(r=n-a\) remaining vertices \(B\). In \(G_{n,t}\), vertices in \(A\) have degree \(n-2\), and vertices in \(B\) have degree \(n-1\). The three edge classes \(AA,AB,BB\) have sizes \(a(a-2)/2,ar,r(r-1)/2\), respectively. For an edge \(e=uv\), put \(D_e=d(u)+d(v)\), equal to \(2n-4,2n-3,2n-2\) on these classes. Let \(B_G\) be the unsigned vertex-edge incidence matrix. Since \(B_G^{\mathsf T}B_G=2I+A(H_{n,t})\),
\[
L(H_{n,t})=\operatorname{diag}(D_e)-B_G^{\mathsf T}B_G.
\]
Consequently, over the rational function field in \(\lambda\), the matrix determinant lemma gives
\[
P_{n,t}(\lambda)=x^{a(a-2)/2}y^{ar}z^{r(r-1)/2}
\det\left(I_n-B_G\operatorname{diag}(D_e-\lambda)^{-1}B_G^{\mathsf T}\right).
\]
Omit absent edge classes when \(r=0\) or \(r=1\). The identity is rational but becomes a polynomial by the determinant on the left.

**Invariant subspaces.** Assume \(t\ge1\) and \(r\ge1\). In the symmetric \(n\)-by-\(n\) matrix inside the final determinant, the vector differences between the two vertices in each removed pair give a \(t\)-dimensional eigenspace with eigenvalue
\[
1-\frac{a-2}{x}-\frac r y=\frac U{xy}.
\]
The pair-constant vectors on \(A\) whose total over all pairs is zero give a \((t-1)\)-dimensional eigenspace with eigenvalue
\[
1-\frac{a-4}{x}-\frac r y=\frac V{xy}.
\]
Vectors supported on \(B\), of sum zero, give an \((r-1)\)-dimensional eigenspace with eigenvalue
\[
1-\frac{r-2}{z}-\frac a y=\frac W{yz}.
\]
The remaining two-dimensional space is spanned by the indicator vectors of \(A\) and \(B\). Its quotient matrix is
\[
\begin{pmatrix}
1-2(a-2)/x-r/y&-r/y\\
-a/y&1-2(r-1)/z-a/y
\end{pmatrix},
\]
whose determinant simplifies identically to \(-\lambda Q/(xyz)\). Multiplying the determinants of the four invariant blocks and the exterior edge-class factors gives the claimed polynomial expression for \(r\ge1\). In the special case \(r=0\), the pair-difference and pair-constant eigenspaces remain, but the all-ones vector on \(A\) has eigenvalue \(-\lambda/x\), yielding the displayed perfect-matching formula. If \(t=0\), the well-known line graph \(L(K_n)\) is \((2n-4)\)-regular, and its unsigned-incidence decomposition gives Laplacian eigenvalues \(0\) once, \(n\) with multiplicity \(n-1\), and \(2n-2\) with multiplicity \(m-n\).

**Boundary cancellation.** Direct substitution into the four explicit quadratics gives the three identities printed under the formulas. If \(t=1\), the only negative power of \(x\) is \(x^{-2}\) and is canceled by \(UQ\); if \(r=1\), the negative power \(z^{-1}\) is canceled by \(Q\); if \(r=2\), it is canceled by \(W\). These are all cases with a negative exponent for \(n\ge4\). Thus no auxiliary genericity assumptions about \(t\) or \(r\) are needed.

**Integral-spectrum boundary.** The formulas for \(t=0\) and \(r=0\) display only integral roots. Likewise \(P_{4,1}(\lambda)=-\lambda(3-\lambda)^2(5-\lambda)^2\). Conversely, suppose \(r>0\). If \(t\ge2\), the quadratic \(U\) occurs as an uncanceled factor and has discriminant
\[
\Delta_U=(n-3)^2+8(t-1).
\]
Since \(2\le t\le(n-1)/2\), this lies strictly between \((n-3)^2\) and \((n-1)^2\). The only possible intervening perfect square is \((n-2)^2\); equality would require \(8(t-1)=2n-5\), impossible by parity. Hence \(U\) has irrational roots and the spectrum is not integral. Finally, if \(t=1\) and \(r>0\), then \(n\ge5\). The uncanceled factor \(W^{r-1}\) has discriminant \((n-3)^2+8\), which is not a square when \(n\ge5\): a hypothetical square \(s^2\) would satisfy \((s-(n-3))(s+(n-3))=8\); positive same-parity factors can only be \(2,4\), forcing \(n-3=1\), a contradiction. This completes the classification.

## Verification
The accompanying `verify.py` uses exact symbolic arithmetic (SymPy, version 1.12 or newer) to form each line graph explicitly from its edge set, construct its Laplacian, compute its full characteristic polynomial, and compare coefficientwise with the stated determinant formulas after cancellation. It also cross-checks the spanning-tree counts from the derivative at zero against the evaluated weighted-incidence tree formula; for smaller instances it independently computes a cofactor determinant. The full script was executed successfully for all \(n\in\{4,5,6,7,8,9\}\) and all permitted \(0\le t\le\lfloor n/2\rfloor\), totaling 24 graph parameters. The script checks finite examples only; the general theorem is supplied by the preceding incidence and invariant-subspace proof.

## Relationship to prior work
Cámara and Haemers proved that the **base graph** \(K_n\) with a matching deleted is determined by its adjacency spectrum (2012 preprint, Proposition 2.1). Their result does not state the Laplacian spectrum of its **line graph** or classify when that spectrum is integral. Classical work by Grone and Merris examines Laplacian integral graphs in general but does not, in the material accessible here, present this exact two-parameter line-graph classification. Dong (2019, Theorem 5.1 and its line-graph specialization) provides general spanning-tree formulas for line graphs; the tree counts in the auxiliary exact checker are corroboration, not claimed as a new general principle. These generic incidence tools also do not state the resulting matching-deletion integrality boundary. The result concerns the *line graph of a matching-deleted clique*; it is not a result about a matching-deleted complete bipartite graph or about the base graph's adjacency spectrum.

## Limitations
The result is an exact spectral and integrality theorem, not a claim of spectral determination up to isomorphism, and does not establish eigenvalue simplicity or new universal spectral inequalities. The proof is combinatorial linear algebra valid in characteristic zero. Exhaustive calculation for small orders cannot by itself establish the all-order result. An earlier equivalent formula under terminology such as line graphs of multicones or cocktail-party joins could have escaped the checked indexing; this remains an originality risk until further independent literature review. Independent audit is not performed.

## References
1. M. Cámara and W. H. Haemers, *Spectral characterizations of almost complete graphs*, arXiv:1211.4420, first posted 2012-11-19, especially Section 2, Proposition 2.1; https://arxiv.org/abs/1211.4420.
2. R. Grone and R. Merris, *The Laplacian Spectrum of a Graph II*, SIAM Journal on Discrete Mathematics 7 (1994), 221–229, https://doi.org/10.1137/S0895480191222653.
3. F. Dong, *Formulas counting spanning trees in line graphs and their extensions*, arXiv:1907.07376 (2019), especially Theorem 5.1, https://arxiv.org/abs/1907.07376.
4. C. Adiga, K. Das, and B. R. Rakshith, *Some graphs determined by their signless Laplacian (distance) spectra*, Electronic Journal of Linear Algebra 36 (2020), https://doi.org/10.13001/ela.2020.4951 (comparison to the base graph's matching-deletion join literature).
