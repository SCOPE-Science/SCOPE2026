# Sharp \(2n+1\) backward-shift defects from projection-perturbed truncated Toeplitz shifts

## Finding

For every integer \(n\geq1\), set \(r=2n+2\), let \(K=H^2(\mathbb D)\ominus z^{2r}H^2(\mathbb D)\), and let \(e_j(z)=z^j\), \(0\leq j<2r\), be its standard orthonormal basis. Let \(A\) be the truncated Toeplitz operator with analytic symbol \(z^r\), and let \(P\) be the orthogonal projection onto
\[
\operatorname{span}\{e_{r+2},e_{r+4},\ldots,e_{r+2n}\}.
\]
Thus \(P\) is positive, self-adjoint, and has rank exactly \(n\). Define \(M=\ker(A-P)\).

**Theorem.** Every element of \(M\) vanishes at zero, and the *minimal nearly backward-shift-invariant defect* of \(M\) equals
\[
\boxed{\operatorname{def}_{S^*}(M)=2n+1.}
\]
More explicitly, for any closed subspace \(N\subset H^2(\mathbb D)\) let
\[
\operatorname{def}_{S^*}(N)=\dim\left(\frac{N+S^*(N\cap zH^2)}{N}\right)
\]
when this dimension is finite. This dimension is also the smallest possible dimension of a space \(E\) such that \(S^*f\in N+E\) for every \(f\in N\) with \(f(0)=0\).

A general upper bound \(2n+1\) for arbitrary rank-at-most-\(n\) perturbations of scalar truncated Toeplitz operators appears in Chattopadhyay–Khan, Theorem 5.4. The new point here is **attainment for every rank**, even when the perturbation is an orthogonal projection and the unperturbed truncated Toeplitz symbol is a single monomial. Thus the existing universal bound cannot be lowered under either of those restrictions.

## Assumptions and scope

All Hilbert spaces and scalar products are complex. The Hardy space \(H^2(\mathbb D)\) has its usual monomial orthonormal basis. For an inner function \(\theta\), \(K_\theta=H^2\ominus\theta H^2\); the truncated Toeplitz operator with symbol \(a\in L^\infty(\mathbb T)\) is \(A_a^\theta f=P_{K_\theta}(af)\). The backward shift is \(S^*f(z)=(f(z)-f(0))/z\). For model spaces, \(S^*K_\theta\subseteq K_\theta\).

The new construction uses \(\theta=z^{4n+4}\) and \(a=z^{2n+2}\), so the model space is finite-dimensional and no domain or unbounded-symbol questions arise. The definition of defect permits the auxiliary defect space in the entire Hardy space, not just the finite model space; the computed quotient rank therefore proves minimality in either interpretation. No statement on the smallest model-space dimension for a given defect is made.

## Proof

**1. Coordinate description of the perturbed kernel.** Put \(r=2n+2\). Write any \(f\in K_{z^{2r}}\) uniquely as
\[
f=\sum_{i=0}^{r-1}x_i e_i+\sum_{i=0}^{r-1}y_i e_{r+i}.
\]
The analytic truncated Toeplitz operator acts by
\[
Af=\sum_{i=0}^{r-1}x_i e_{r+i},
\]
whereas the orthogonal projection acts by
\[
Pf=\sum_{j=1}^{n}y_{2j}e_{r+2j}.
\]
Consequently \(f\in M\) precisely when
\[
x_{2j}=y_{2j}\quad(1\leq j\leq n),\qquad
x_i=0\quad\bigl(i\notin\{2,4,\ldots,2n\}\bigr).
\]
In particular \(x_0=0\), so \(M\subset zH^2\). Its dimension is \(r\), since the \(r\) coordinates \(y_0,\ldots,y_{r-1}\) are free.

**2. An exact quotient-coordinate map.** Define the surjective linear map \(L:K\to\mathbb C^r\) by
\[
(Lh)_i=\begin{cases}
h_i-h_{r+i},&i\in\{2,4,\ldots,2n\},\\
h_i,&i\notin\{2,4,\ldots,2n\},
\end{cases}
\]
where \(h_i\) denotes the coefficient of \(e_i\). The coordinate description shows that \(\ker L=M\). Therefore
\[
\dim\bigl((S^*M+M)/M\bigr)=\operatorname{rank}(L S^*|_M).
\]
For \(f\in M\) parametrized by \(y=(y_0,\ldots,y_{r-1})\), use \(S^*e_i=e_{i-1}\) for \(i\geq1\) and \(S^*e_0=0\). A direct coefficient calculation yields **exactly**
\[
(LS^*f)_{2j-1}=y_{2j},\qquad
(LS^*f)_{2j}=-y_{2j+1}\quad(1\leq j\leq n),\qquad
(LS^*f)_{r-1}=y_0,
\]
and all other coordinates vanish. The input coordinates \(y_0,y_2,y_3,\ldots,y_{2n},y_{2n+1}\) are distinct and freely variable; the output coordinates \(1,2,\ldots,2n+1\) are distinct. Hence this linear map has rank exactly \(2n+1\), not merely at most that value. Since \(M\subset zH^2\), this proves the asserted minimal defect for every \(n\geq1\). In fact the only unused free kernel parameter is \(y_1\).

**3. Why this matches the general bound (background, not asserted new).** For any nonconstant inner \(\theta\), let \(K=K_\theta\) and \(A=A_a^\theta\). The space
\[
E_\theta=\{h\in K:zh\in K\}=S^*(K\cap zH^2)
\]
has codimension at most one in \(K\): for \(h\in K\), the condition \(zh\perp\theta z^k\) is automatic for \(k\geq1\), leaving only the single condition \(\langle zh,\theta\rangle=0\). If \(f\in\ker A\cap zH^2\) and \(h=S^*f\), then for every \(e\in E_\theta\),
\[
\langle Ah,e\rangle=\langle aS^*f,e\rangle
=\langle af,ze\rangle=0.
\]
Thus the image of \(S^*(\ker A\cap zH^2)\) under \(A\) lies in the at-most-one-dimensional space \(E_\theta^\perp\). Choosing a preimage of a basis of that image shows \(\operatorname{def}_{S^*}(\ker A)\leq1\).

For any rank-at-most-\(n\) operator \(F\), put \(M_0=\ker A\), \(M=\ker(A-F)\), and \(Q=\ker A\cap\ker F\). Then \(Q\subset M_0\cap M\), and both \(\dim(M_0/Q)\) and \(\dim(M/Q)\) are at most \(n\), by applying \(F|_{M_0}\) and \(A|_M=F|_M\), respectively. For vectors in \(Q\cap zH^2\), the backward shift lies in \(M_0\) modulo at most one dimension, and then lies in \(M\) modulo at most \(n+1\) dimensions. Extending from \(Q\cap zH^2\) to \(M\cap zH^2\) contributes at most \(n\) further dimensions. Therefore
\[
\operatorname{def}_{S^*}(M)\leq2n+1.
\]
This short argument independently recovers the existing universal upper estimate; Part 2 supplies the missing extremal realization.

## Verification

The included standard-library script `checks/check_defect.py` builds the exact integer matrices of \(A\), \(P\), \(A-P\), \(S^*\), the kernel parametrization, and \(L\). It uses rational Gaussian elimination, checks that \(P^2=P=P^*\) has rank \(n\), verifies \(\ker(A-P)=\operatorname{ran}B\) for the displayed kernel parametrization, and checks that \(LS^*B\) is exactly the sparse matrix in Part 2. The script was run successfully for every integer \(1\leq n\leq10\), producing defect dimensions \(3,5,\ldots,21\). The parameter-uniform proof is algebraic and does not depend on those finite tests.

To reproduce, execute `python3 checks/check_defect.py` in a directory containing the extracted file. Python's standard library suffices. This computation does not test other inner functions, other perturbations, or any classification claim.

## Relationship to prior work

Khan, Lata, and Singh (arXiv:2507.05721, first submitted July 8, 2025) study finite-rank perturbations of Toeplitz operators on vector-valued Hardy spaces and finite-defect nearly invariant subspaces. Liang and Partington (arXiv:1911.10072) and Chattopadhyay, Das, and Pradhan (arXiv:2005.02255) give related representations for Toeplitz kernels on the full Hardy space. These do not explicitly compute the present compressed-monomial, positive-projection kernel defect.

Chattopadhyay and Khan (arXiv:2610.40295, submitted October 29, 2026), Theorem 5.4, prove the universal upper bound \(2n+1\) for scalar truncated Toeplitz perturbations. Their treatment provides upper estimates and illustrations for ranks one and two, but no explicit family exhibiting equality for every rank was found in the inspected material. We therefore **do not** claim the upper bound as new; the claim is its sharp attainment under particularly restrictive natural hypotheses. The different spaces and directions of the other cited works prevent their statements from implying this equality without an additional construction.

## Limitations

The example proves optimality of the universal *defect dimension*, not minimality of the polynomial degree or the finite model-space dimension. It does not classify all extremizers, show robustness under perturbations of the monomial symbol, determine multiband optimal defects, or extend the construction to all inner functions. Publication priority is assessed only against the sources inspected and searched; a previously overlooked monomial-model example may exist. No independent mathematical audit has been performed.

## References

1. A. Khan, S. Lata, D. Singh, *Perturbations of Toeplitz operators on vector-valued Hardy spaces*, arXiv:2507.05721 (first version July 8, 2025), https://arxiv.org/abs/2507.05721.
2. A. Chattopadhyay, A. Khan, *Perturbations of Truncated Toeplitz operators*, arXiv:2610.40295 (first version October 29, 2026), Theorem 5.4, https://arxiv.org/abs/2610.40295.
3. Y. Liang, J. R. Partington, *Representing kernels of perturbations of Toeplitz operators by backward shift-invariant subspaces*, arXiv:1911.10072, https://arxiv.org/abs/1911.10072.
4. A. Chattopadhyay, S. Das, C. Pradhan, *Kernels of Perturbed Toeplitz Operators in vector-valued Hardy spaces*, arXiv:2005.02255, https://arxiv.org/abs/2005.02255.
5. R. O'Loughlin, *Matrix-valued truncated Toeplitz operators: unbounded symbols, kernels and equivalence after extension*, arXiv:2012.00654, https://arxiv.org/abs/2012.00654.
