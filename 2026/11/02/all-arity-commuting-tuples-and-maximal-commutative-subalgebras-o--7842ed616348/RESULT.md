# All-arity commuting tuples and maximal commutative subalgebras of two-step multiarrow path algebras

## Finding

Fix a finite field \(\mathbb F_q\), two integers \(r,s\ge1\), and the acyclic quiver with three vertices, \(r\) arrows from the first vertex to the second and \(s\) arrows from the second to the third. Let \(A_{r,s}=\mathbb F_qQ_{r,s}\) be its **unquotiented path algebra**, so its \(rs\) distinct length-two paths remain linearly independent. For each \(k\ge0\), let \(C_k(q;r,s)\) count ordered \(k\)-tuples of arbitrary elements of \(A_{r,s}\) that commute pairwise under associative multiplication. Empty tuples are counted once.

Set \(Q=q^k\) and \(L=(Q-1)/(q-1)\), and define
\[
B_{r,s}(Q,q)=Q^r+Q^s-1+L(q^r-1)(q^s-1).
\]
Then the complete **all-arity commuting-tuple count** is
\[
\boxed{C_k(q;r,s)=Q\Bigl[Q^{rs}B_{r,s}(Q,q)
+(Q-1)q^{rs}(Q^rq^s+Q^sq^r)
+(Q-1)q^{r+s}Q^{rs}
+(Q-1)(Q-2)q^{r+s+rs}\Bigr].}
\]
This is valid for every prime-power field order, including characteristic two, without a restriction on \(k\). In particular, \(C_0=1\) and \(C_1=q^{3+r+s+rs}\).

Write \(D=1+rs+\max(r,s)\). The maximum dimension of a unital commutative \(\mathbb F_q\)-subalgebra of \(A_{r,s}\) is exactly \(D\). If \(\max(r,s)\ge2\), **there are exactly one or two** subalgebras of this maximum dimension: one if \(r\ne s\), two if \(r=s\). They are the scalar identity together with the entire length-two-path space and either the first-arrow or second-arrow space, choosing the larger arrow space (both choices when equal). For the boundary \(r=s=1\), the maximum dimension remains \(3\), but the exact number attaining it is
\[
\boxed{q^3+3q^2+q+1.}
\]

## Assumptions and scope

Let the vertex idempotents be \(e_1,e_2,e_3\), with arrow bases \(\alpha_1,\ldots,\alpha_r\) and \(\beta_1,\ldots,\beta_s\). Their compositions \(\gamma_{ij}=\alpha_i\beta_j\) form an independent basis of the length-two-path space. Let \(U,V,W\) denote the spans of the \(\alpha_i\), \(\beta_j\), and \(\gamma_{ij}\), respectively. The algebra has dimension \(3+r+s+rs\), radical \(U\oplus V\oplus W\), and radical square \(W\ne0\). A commuting tuple is not required to consist of units, nilpotents, or idempotents. All statements concern the associative algebra itself, not its group of units or a quotient that identifies parallel paths.

## Proof

For \(k\) elements, assemble the coefficients of \(e_1,e_2,e_3\) into vectors \(a,b,c\in\mathbb F_q^k\); assemble the coefficients of each \(\alpha_i\), \(\beta_j\), and \(\gamma_{ij}\) into vectors \(x_i,y_j,z_{ij}\in\mathbb F_q^k\). Write \(u=a-b\), \(v=b-c\), \(w=a-c=u+v\). For vectors \(h,t\in\mathbb F_q^k\), let \(h\wedge t\) denote their usual exterior product; it vanishes precisely when they are linearly dependent. Direct multiplication in the path basis shows that pairwise commutativity is equivalent to
\[
u\wedge x_i=0,\qquad v\wedge y_j=0,\qquad
w\wedge z_{ij}=-x_i\wedge y_j
\quad(1\le i\le r,\ 1\le j\le s).
\]
The choice of \(b\) contributes a factor \(Q\); the differences \(u,v\) range independently over \(\mathbb F_q^k\). The following five disjoint cases count the remaining coefficients.

When \(u=v=0\), the equations say \(x_i\wedge y_j=0\) for all \(i,j\), and every \(z_{ij}\) is free. If all first-arrow vectors vanish, the second-arrow vectors have \(Q^s\) choices; if all second-arrow vectors vanish, the first-arrow vectors have \(Q^r\) choices, with the all-zero family counted twice. If both families are nonzero, all their vectors lie in the same one-dimensional subspace. There are \(L\) such lines, and a fixed line contributes \((q^r-1)(q^s-1)\). Consequently this case contributes \(Q^{rs}B_{r,s}(Q,q)\).

When \(u=0\) and \(v\ne0\), the \(x_i\) are arbitrary and the \(y_j\) are scalar multiples of \(v\), with \(Q^rq^s\) choices. For each pair, the equation involving \(z_{ij}\) is soluble with exactly \(q\) solutions: writing \(y_j=\lambda_jv\), one can choose \(z_{ij}=\lambda_jx_i\) plus an arbitrary vector in the line spanned by \(v\). This gives \((Q-1)Q^rq^{s+rs}\). Symmetrically, \(v=0\ne u\) contributes \((Q-1)Q^sq^{r+rs}\).

When \(u\ne0\) and \(v=-u\), the vectors \(x_i,y_j\) are all multiples of the same vector, making every cross-wedge zero, while all \(z_{ij}\) are free. This contributes \((Q-1)q^{r+s}Q^{rs}\).

Finally, when \(u,v\ne0\) and \(w=u+v\ne0\), write \(x_i=\lambda_i u\) and \(y_j=\mu_jv\). Since \(w\wedge v=u\wedge v\), the choice \(z_{ij}=-\lambda_i\mu_jv\) solves the final equation, and its entire solution set is that vector plus the line \(\mathbb F_qw\). Thus there are \(q^{r+s+rs}\) solutions for each of the \((Q-1)(Q-2)\) choices of \((u,v)\). The five counts, multiplied by the factor \(Q\), prove the formula, including the case \(k=0\).

For fixed \(q,r,s\), regard the displayed formula as a polynomial in \(Q=q^k\). Its degree is \(D=1+rs+\max(r,s)\). If \(\max(r,s)\ge2\), its leading coefficient equals \(1\) for \(r\ne s\) and \(2\) for \(r=s\). If \(r=s=1\), the leading coefficient is \(q^3+3q^2+q+1\). To relate this to subalgebras, note that every pairwise-commuting tuple generates a unital commutative subalgebra. The finite algebra has finitely many subalgebras. A finite union of proper linear subspaces of a fixed \(d\)-dimensional subalgebra contributes only \(O(q^{k(d-1)})\) tuples as \(k\to\infty\); similarly, intersections of two distinct \(d\)-dimensional subalgebras are proper. Therefore, if \(d\) is the largest commutative-subalgebra dimension and \(M\) counts such subalgebras, then
\[
C_k(q;r,s)=M q^{kd}+O(q^{k(d-1)}).
\]
Comparing leading powers yields \(d=D\) and the claimed values of \(M\). The explicitly defined subalgebras \(\mathbb F_q1\oplus U\oplus W\) and \(\mathbb F_q1\oplus V\oplus W\) are commutative because every product of two elements in their respective radicals vanishes. Their dimensions are \(1+r+rs\) and \(1+s+rs\); the obtained count \(M\) shows these are the only maximum-dimensional cases when \(\max(r,s)\ge2\).

## Verification

The standalone file `verify.py` checks the algebra's native basis multiplication and commutator, independently of the five-case enumeration. Complete ordered-pair censuses over \(\mathbb F_2\) for \((r,s)=(1,1),(2,1),(1,2),(2,2)\) yield respectively \(928,6400,6400,139264\); the \(\mathbb F_3\) census at \((1,1)\) yields \(33777\). An exhaustive triple census at \((q,r,s)=(2,1,1)\) yields \(9472\). Four additional cross-wedge-family enumerations validate the zero-diagonal case. Binary row-reduced-subspace censuses independently find \(23\) three-dimensional commutative unital subalgebras for \(r=s=1\), and a unique maximum-dimensional one for each of \((r,s)=(2,1),(1,2)\). These finite tests are corroborative only; the preceding case analysis proves the general statement.

Run `python verify.py` with the Python standard library. The code is complete and uses no external dependencies.

## Relationship to prior work

Kaur, Sharma and Singh (2020, arXiv:2006.01493, Sections 1, 3, and 8) compute branching matrices and simultaneous-conjugacy counts for commuting tuples in **invertible** upper triangular and unitriangular **groups**, in odd characteristic. Their group result does not count unrestricted path-algebra elements with arbitrary parallel arrows or zero diagonal coefficients. Green and Schroll (2023, arXiv:2302.08169, Sections 2–7) study the differently defined *commuting algebra* obtained by imposing relations between parallel paths. In contrast, the present calculation retains all distinct parallel paths and counts commuting **elements**, not quotient algebra dimensions. Sharma (2016) studies simultaneous conjugacy of full-matrix tuples rather than the stated multiarrow-algebra tuple cardinality. Related published Kronecker-path-algebra counts treat one radical-square-zero arrow layer; the present algebra has composable layers and nonzero radical square. Nearby results on commuting pairs in four-vertex path radicals do not directly give these all-arity counts in the full three-vertex algebra.

## Limitations

The result treats two consecutive nonempty parallel-arrow bundles on three vertices, not arbitrary quivers or arbitrary algebra quotients. The field must be finite, but its characteristic is unrestricted. The maximal-subalgebra classification refers to subalgebras of **largest dimension**, not all subalgebras maximal under inclusion. A literature comparison cannot prove worldwide publication priority; an unlocated general enumeration theorem might imply this specialization. No independent mathematical validation has been performed.

## References

1. D. Kaur, U. B. Sharma, A. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493v1 (first posted 2020-06-02), especially Sections 1, 3, 8. https://arxiv.org/abs/2006.01493
2. E. L. Green, S. Schroll, *The Commuting Algebra*, arXiv:2302.08169v1 (first posted 2023-02-16), especially Sections 2–7. https://arxiv.org/abs/2302.08169
3. U. B. Sharma, *Simultaneous Similarity Classes of Commuting Matrices over a Finite Field*, Linear Algebra Appl. 501 (2016), 48–97. https://doi.org/10.1016/j.laa.2016.03.015
