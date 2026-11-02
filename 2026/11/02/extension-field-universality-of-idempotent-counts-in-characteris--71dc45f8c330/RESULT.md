# Extension-field universality of idempotent counts in characteristic-two perfect evolution algebras

## Finding
For all integers \(n\ge1\) and \(m\ge1\), put \(q=2^m\) and select a uniformly random \(A\in\operatorname{GL}_n(\mathbb F_q)\). Consider the evolution algebra with natural basis \(e_1,\ldots,e_n\), mixed products \(e_i e_j=0\) for \(i\ne j\), and a structure matrix whose coordinate-square map is \(x\mapsto A x^{[2]}\), where \(x^{[2]}=(x_1^2,\ldots,x_n^2)^T\). This algebra is perfect because \(A\) is invertible.

Let \(D(A)=\dim_{\mathbb F_2}\{x\in\mathbb F_q^n:A x^{[2]}=x\}\). The fixed-point set is an \(\mathbb F_2\)-vector space and \(0\le D(A)\le n\). Its exact probability distribution equals the distribution of \(\dim_{\mathbb F_2}\ker(B-I)\) for a uniformly random \(B\in\operatorname{GL}_n(\mathbb F_2)\), **independently of** \(m\).

Writing \({u\brack v}_2\) for a Gaussian binomial coefficient and defining \(g_0=1\) and \(g_k=|\operatorname{GL}_k(\mathbb F_2)|=\prod_{i=0}^{k-1}(2^k-2^i)\), we have, for every \(0\le k\le n\),
\[
\mathbb E\!\left[{D(A)\brack k}_2\right]=\frac1{g_k}.
\]
In particular, for each \(0\le d\le n\),
\[
\boxed{\Pr(D(A)=d)=\sum_{k=d}^n\frac{(-1)^{k-d}\,2^{\binom{k-d}{2}}{k\brack d}_2}{g_k}.}
\]
Consequently, the number \(N(A)\) of **nonzero** idempotents is exactly \(2^{D(A)}-1\), and its entire probability law is independent of \(m\). For \(n=2\) the probabilities of \(N(A)=0,1,3\) are respectively \(1/3,1/2,1/6\). For \(n=3\) the probabilities of \(N(A)=0,1,3,7\) are respectively \(2/7,7/12,1/8,1/168\).

## Assumptions and scope
The sample space is the set of all **labeled, invertible** natural-basis structure matrices, with uniform counting measure. It is not a distribution on isomorphism classes, noninvertible matrices, or randomly chosen graph-supported sparse matrices. Coordinates follow the column convention \(x^2=A x^{[2]}\). The exponent \(2\) is the characteristic-two Frobenius, not an arbitrary power. The field extension degree \(m\), matrix size \(n\), and all ranks \(k,d\) are quantified above.

## Proof
**1. Additive fixed space.** Write \(\sigma(x)=x^{[2]}\) and \(F_A=A\circ\sigma\). Because \(\mathbb F_q\) has characteristic two, \(F_A\) is additive and \(\mathbb F_2\)-linear. Hence its fixed set \(V_A\) is an \(\mathbb F_2\)-vector space.

**2. Fixed vectors descend linearly.** Suppose \(x_1,\ldots,x_k\in V_A\) are linearly independent over \(\mathbb F_2\). They are also linearly independent over \(\mathbb F_q\). Indeed, otherwise choose a dependent subfamily of minimal size and a nontrivial relation \(\sum_i c_i x_i=0\), scaled so one coefficient is \(1\). This relation space on that minimal support is one-dimensional over \(\mathbb F_q\). Applying \(F_A\) yields \(\sum_i c_i^2 x_i=0\). Both normalized relations belong to the same one-dimensional space, so \(c_i^2=c_i\) for every coefficient. The only roots of \(z^2=z\) in \(\mathbb F_q\) are \(0,1\). Thus the supposed dependence would already be over \(\mathbb F_2\), a contradiction. Therefore \(\dim_{\mathbb F_2}V_A\le n\).

**3. Count fixed \(\mathbb F_2\)-subspaces.** Let \(k\le n\). There are \(Q_{n,k}(q)=\prod_{i=0}^{k-1}(q^n-q^i)\) ordered \(k\)-tuples of \(\mathbb F_q\)-linearly independent vectors. Each \(k\)-dimensional \(\mathbb F_2\)-subspace having such a basis is represented by exactly \(g_k\) ordered \(\mathbb F_2\)-bases. For an eligible ordered basis \((x_1,\ldots,x_k)\), its coordinatewise squared vectors are again \(\mathbb F_q\)-linearly independent: apply the inverse of field Frobenius to any putative dependence. Exactly \(|\operatorname{GL}_n(\mathbb F_q)|/Q_{n,k}(q)\) invertible matrices send this squared ordered frame to the original frame. Therefore a uniformly random \(A\) fixes every vector of the chosen subspace with probability \(Q_{n,k}(q)^{-1}\). Taking the expectation of the number of fixed \(k\)-subspaces yields
\[
\mathbb E\!\left[{D(A)\brack k}_2\right]
=\frac{Q_{n,k}(q)}{g_k}\cdot\frac1{Q_{n,k}(q)}=\frac1{g_k}.
\]
The \(k=0\) identity uses the empty product and the zero subspace.

**4. Identify and invert the distribution.** For \(q=2\) the map \(\sigma\) is the identity, so \(F_A=A\), and the same calculation gives precisely the Gaussian-binomial moments of the fixed-space dimension of uniform \(\operatorname{GL}_n(\mathbb F_2)\) matrices. The transform \(M_k=\sum_{d=k}^n\Pr(D=d){d\brack k}_2\) is upper triangular with diagonal entries \(1\), so the moments determine the entire distribution. Standard Gaussian-binomial inversion, equivalently \(\sum_{j=0}^r(-1)^j2^{\binom j2}{r\brack j}_2=0\) for every \(r>0\), yields exactly the displayed probability formula. Finally, an \(\mathbb F_2\)-space of dimension \(D\) has \(2^D\) elements including zero. These are precisely the idempotents, completing the proof. \(\square\)

## Verification
The standalone file `verify_binary_evolution_law.py` uses exact finite-field arithmetic to enumerate **every** invertible \(2\times2\) and \(3\times3\) matrix over \(\mathbb F_2\) and \(\mathbb F_4\). It constructs the binary matrix of \(A\sigma-I\), computes the kernel dimension, compares the full distributions with their \(\operatorname{GL}_n(\mathbb F_2)\) analogues, and verifies the expected nonzero-idempotent count. Its output ends `VERIFY_OK`. The exhaustive cases are \(n=2,q=2\) (6 matrices), \(n=2,q=4\) (180), \(n=3,q=2\) (168), and \(n=3,q=4\) (181440). No finite experiment is used to infer the general identity; the proof applies to every \(m,n\).

## Relationship to prior work
Kaygorodov, Martín González, and Viruel, *Evolution algebras: a survey of results and a list of open problems* (arXiv:2610.22248v1, first public 2026-10-15), Remark 23, establishes that the **mean** number of nonzero idempotents of a uniformly sampled invertible structure matrix is \(1\), over every finite field. Their Question 22 identifies random evolution algebras as a natural subject. The present result identifies the **entire** distribution in characteristic two, including all its Gaussian-binomial moments and its invariance under passage from \(\mathbb F_2\) to any finite binary extension. The mean alone does not specify those probabilities. The random fixed-space distribution of ordinary binary invertible matrices is a classical comparison object and is not claimed as a newly discovered distribution. Wei and Zou's work on isomorphism classes concerns orbit counts, which are different from the labeled uniform matrix measure used here.

## Limitations
No statement is made about odd characteristic, singular structure matrices, uniform sampling from isomorphism classes, or arbitrary nonlinear semilinear maps. A fully exhaustive examination of historical literature on random Frobenius-semilinear maps and linearized polynomials has not been completed; an equivalent classical statement could imply the distribution identity. Mathematical validity and priority are different questions. No independent mathematical audit is claimed.

## References
1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, 2026-10-15, especially Remark 23 and Question 22. https://arxiv.org/html/2610.22248v1
2. Y. Wei and Y. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, Linear Algebra Appl., 2023, DOI:10.1016/j.laa.2023.06.006; arXiv:2310.12368.
3. Standard Gaussian-binomial inversion over finite vector spaces (elementary identity reproduced in the proof).
