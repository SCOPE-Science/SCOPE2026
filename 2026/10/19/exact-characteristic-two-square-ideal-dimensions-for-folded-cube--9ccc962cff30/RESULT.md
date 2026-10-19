# Exact characteristic-two square-ideal dimensions for folded-cube evolution algebras

## Finding
For a field \(K\) of characteristic \(2\) and integer \(d\ge2\), take the vector group \(G=(\mathbb F_2)^d\). Write \(\epsilon_i\) for its coordinate vectors and \(\mathbf1=\sum_i\epsilon_i\). The Cayley evolution algebra \(E_d\) has natural basis \(\{e_x:x\in G\}\) with \(e_xe_y=0\) when \(x\ne y\) and
\[
e_x^2=\sum_{i=1}^d e_{x+\epsilon_i}+e_{x+\mathbf1}.
\]
For every \(d\ge2\), the graph is the simple connected folded hypercube. Its structural adjacency operator \(A_d\) satisfies
\[
\dim_K(E_d^2)=\operatorname{rank}_K(A_d)=
\begin{cases}
2^d,&d\text{ even},\\
2^{d-1}-2^{(d-1)/2},&d\text{ odd}.
\end{cases}
\]
For odd \(d\), \(A_d^2=0\), and its homology has dimension
\[
\dim_K(\ker A_d/\operatorname{im} A_d)=2^{(d+1)/2}.
\]
This exact rank, not merely the square-zero dichotomy, is the assertion.

## Assumptions and scope
The field has characteristic two, with no finiteness or algebraic-closure requirement. The integer \(d\) is at least two, ensuring that the \(d+1\) prescribed generators are pairwise distinct. The algebra is nonassociative; \(E_d^2\) denotes the span of all products in the algebra. The operator \(A_d\) is ordinary linear adjacency, not the nonlinear squaring map.

## Proof
Identify \(K[G]\) with the commutative square-zero algebra \(R_d=K[t_1,\ldots,t_d]/(t_1^2,\ldots,t_d^2)\) through \(g_i=1+t_i\). Translation by \(g_i\) is multiplication by \(g_i\). Therefore \(A_d\) is multiplication by
\[
a_d=\sum_{i=1}^d (1+t_i)+\prod_{i=1}^d(1+t_i).
\]
Set \(f_d=1+\sum_{i=1}^d t_i+\prod_{i=1}^d(1+t_i)\). In characteristic two, \(a_d=f_d\) for odd \(d\), while \(a_d=1+f_d\) for even \(d\). Every element of the augmentation ideal of \(R_d\) squares to zero: a monomial of positive degree squares to zero, and Frobenius is additive. Hence \(f_d^2=0\). For even \(d\), multiplication by \(1+f_d\) is invertible (its square is one), proving the first case.

For odd \(d\), we prove a stronger all-\(d\) normal form: an algebra automorphism of \(R_d\) carries \(f_d\) to a sum of \(\lfloor d/2\rfloor\) products of disjoint pairs of square-zero variables, with one unused variable when \(d\) is odd. The base cases are \(f_0=f_1=0\). For \(d\ge2\), let \(P=\prod_{i=1}^{d-2}(1+t_i)\), \(u=P+1\), \(a=t_{d-1}\), \(b=t_d\). Then \(P^2=1\), \(u^2=0\), and direct expansion gives
\[
f_d=f_{d-2}+(P+1)(a+b)+Pab=f_{d-2}+P(a+u)(b+u).
\]
Introduce \(a'=P(a+u)\) and \(b'=b+u\). Their squares are zero; together with the unchanged first \(d-2\) coordinates they give an invertible triangular coordinate change (both recover \(a,b\) using \(P^{-1}=P\)). Consequently \(f_d=f_{d-2}+a'b'\) in the new coordinates. Iteration establishes the claimed normal form, without division by two or extension of \(K\).

Let \(d=2k+1\). Multiplication by \(f_d\), after conjugation by this coordinate change, is the differential \(D\) on the tensor product of \(k\) four-dimensional factors \(K[U,V]/(U^2,V^2)\) and one two-dimensional factor \(K[W]/(W^2)\), where \(D\) multiplies by \(\sum_{j=1}^k U_jV_j\). In each four-dimensional factor, multiplication by \(UV\) is the direct sum of the contractible two-term complex \(K\cdot1\to K\cdot UV\) and two zero differentials on \(K\cdot U\), \(K\cdot V\). Expanding the tensor product, every summand containing at least one contractible factor is contractible; the residual homology has dimension \(2^k\) from selecting one of \(U_j,V_j\) in each pair, times \(2\) from the untouched \(W\), yielding \(2^{k+1}\). In characteristic two the signs in the tensor differential are immaterial, and \(D^2=0\).

For any square-zero linear map on an \(N\)-dimensional space, the homology dimension is \(N-2\operatorname{rank}D\). Thus
\[
\operatorname{rank}(A_d)=\frac{2^d-2^{k+1}}2=2^{d-1}-2^k.
\]
Finally, the span of the defining basis squares of an evolution algebra equals \(E_d^2\); hence its dimension equals the structural-matrix rank. This proves every asserted statement.

## Verification
`verify.py` constructs the exact binary adjacency matrices using XOR bitsets and performs Gaussian elimination over \(\mathbb F_2\) for every \(2\le d\le10\). The observed ranks are \(4,2,16,12,64,56,256,240,1024\) in increasing \(d\). All nine equal the proved formula. These finite checks are supplementary and do not prove the general statement.

## Relationship to prior work
Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v1 (12 May 2026), defines the Cayley evolution algebra in Definition 9.1 and addresses expansion, structural and spectral questions. It does not provide the folded-cube characteristic-two rank formula or the square-zero homology calculation. Established spectral formulas for folded cubes generally concern characteristic-zero eigenvalues and do not imply modular rank. A previously identified parity statement for cubelike evolution algebras establishes that an even-sized connection set makes the double squaring operator zero, but does not determine the intermediate dimension of the square ideal. The new assertion concerns that exact dimension for a canonical family.

## Limitations
Only the specified folded-cube connection sets and characteristic two are covered. No uniform expansion lower bound is claimed for the family. The homology refers to the linear adjacency operator, not to homological invariants of the graph's topological complexes. Literature searches cannot exclude unindexed binary-adjacency-rank results under coding-theory terminology; independent review remains outstanding.

## References
- P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v1, submitted 12 May 2026, especially Sections 2.3, 5 and 9.1, https://arxiv.org/html/2605.12672v1.
- *Folded Cube Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/FoldedCubeGraph.html (standard identification and graph family).
- *Automorphism Groups of Cayley Evolution Algebras*, arXiv:2301.08480 (related general Cayley-evolution algebra background; no modular folded-cube rank claim relied upon).
