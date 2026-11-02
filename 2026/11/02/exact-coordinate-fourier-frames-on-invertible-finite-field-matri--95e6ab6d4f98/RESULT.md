# Exact coordinate Fourier frames on invertible finite-field matrices

## Finding
For any finite field \(\mathbb F_q\) of prime-power order \(q\), every integer \(d\ge2\), and any nontrivial additive character \(\psi\), the constant and all \(d^2\) single-entry additive characters restricted to invertible \(d\)-by-\(d\) matrices form a Riesz family. Its *complete normalized Gram spectrum* is explicit. The mode producing the upper frame bound changes **exactly at dimension four**, independently of field size.

Put
\[
 a=-\frac1{q^d-1},\qquad b=\frac1{(q^d-1)(q^{d-1}-1)},
\]
and
\[
\begin{aligned}
\lambda_0&=1+2(d-1)a+(d-1)^2b,\\
\lambda_1&=1+(d-2)a-(d-1)b,\\
\lambda_2&=1-2a+b,\\
\mu_\pm&=\frac{1+\lambda_0\pm\sqrt{(1-\lambda_0)^2+4d^2a^2}}2.
\end{aligned}
\]
Then the Gram eigenvalues, with multiplicities, are
\[
\mu_-\ (1),\quad\mu_+\ (1),\quad
\lambda_1\ (2(d-1)),\quad\lambda_2\ ((d-1)^2).
\]
Moreover \(0<\mu_-<\lambda_1<\lambda_2\), and
\[
\lambda_2>\mu_+\ \text{if }d=2,3;\qquad
\mu_+>\lambda_2\ \text{if }d\ge4.
\]
Consequently the sharp *squared* spectral condition number is
\[
\kappa_2^2=\frac{\max\{\lambda_2,\mu_+\}}{\mu_-}.
\]
The frame becomes asymptotically tight for every fixed \(q\): \(\kappa_2=1+O_q(dq^{-d})\) as \(d\to\infty\).

## Assumptions and scope
Equip \(\operatorname{GL}_d(\mathbb F_q)\) with uniform probability measure. Let \(f_0(X)=1\) and \(f_{ij}(X)=\psi(X_{ij})\) for all \(1\le i,j\le d\). Define the Hermitian Gram matrix \(G_{\alpha\beta}=\mathbb E_{X\in\operatorname{GL}_d(\mathbb F_q)}\overline{f_\alpha(X)}f_\beta(X)\). The theorem concerns this specific full first-coordinate Fourier band, not higher-degree characters, singular matrices, or unequal sample weights. Here \(\kappa_2\) refers to the singular-value ratio of the synthesis/evaluation operator, so its square is the Gram-eigenvalue ratio.

## Proof
**1. Rank-one and rank-two character sums.** Write \(A=q^d-1\), \(B=q^{d-1}-1\). The first column of a uniform invertible matrix is uniform among the \(A\) nonzero vectors. The sum of a nontrivial coordinate character over all vectors is zero, giving \(\mathbb E\psi(X_{11})=-1/A=a\). To evaluate a rank-two character, use invariance under invertible row/column operations to reduce its coefficient matrix to the first two diagonal matrix units. An ordered independent column pair \((v,w)\) has \(A(q^d-q)\) choices. For fixed \(v\ne0\),
\[
\sum_{w\notin\operatorname{span}(v)}\psi(w_2)
=-\sum_{w\in\operatorname{span}(v)}\psi(w_2)
=\begin{cases}-q,&v_2=0,\\0,&v_2\ne0.\end{cases}
\]
Since \(\sum_{v\ne0,\,v_2=0}\psi(v_1)=-1\), averaging yields \(q/[A(q^d-q)]=1/(AB)=b\). The argument uses only nontrivial-character orthogonality and is valid in all characteristics and extension degrees.

**2. Rook decomposition.** Two coordinate functions have Gram entry \(1\) when identical, \(a\) when their indices differ in exactly one coordinate (same row or column), and \(b\) when both indices differ. This is because the corresponding difference of matrix units has rank one or two. The constant couples to each coordinate with entry \(a\). The coordinate block decomposes into the all-ones line, row-contrast and column-contrast spaces, and the row-and-column-zero subspace. Their respective eigenvalues are \(\lambda_0\), \(\lambda_1\), and \(\lambda_2\), with dimensions \(1\), \(2(d-1)\), and \((d-1)^2\). The constant couples only to the all-ones line: its resulting symmetric two-dimensional block is
\[
\begin{pmatrix}1&da\\da&\lambda_0\end{pmatrix},
\]
with eigenvalues \(\mu_-\) and \(\mu_+\).

**3. Positivity and spectral endpoints.** We have \(\lambda_2-\lambda_1=d(b-a)>0\) and \(\lambda_1-\lambda_0=-d(a+(d-1)b)\ge0\), because \(q^{d-1}-1\ge d-1\). The second inequality is strict except \((q,d)=(2,2)\). As \(\mu_-<\min(1,\lambda_0)\), the lower spectral endpoint is \(\mu_-\) once its positivity is checked. For \(d\ge3\), \(\lambda_0-d^2a^2\ge1-2(d-1)/A-d^2/A^2>0\): at \(d=3\), \(A\ge7\) suffices, and at \(d\ge4\), \(A\ge2^d-1\ge3d\) suffices. For \(d=2,q\ge3\), \(A\ge8\) similarly suffices; the remaining \((q,d)=(2,2)\) has \(\lambda_0-d^2a^2=2/9\). Thus \(\mu_->0\).

For the upper endpoint, set \(u=1/A\) and \(t=1/B\). Since \(\lambda_2>1\), comparison with the larger eigenvalue of the two-dimensional block reduces to the sign of
\[
\det\left(\lambda_2I-
\begin{pmatrix}1&da\\da&\lambda_0\end{pmatrix}\right)
=d u^2\left[(4-d)+(6-2d)t-(d-2)t^2\right].
\]
The bracket is positive for \(d=2\), equals \(1-t^2>0\) for \(d=3\), and is strictly negative for every \(d\ge4\). This proves the exact sharp dimension-four crossover and the condition-number formula.

**4. Asymptotic tightness.** For fixed field size, \(|a|=O(q^{-d})\), \(b=O(q^{-2d+1})\) and all four eigenvalue levels are \(1+O_q(dq^{-d})\) as \(d\to\infty\), yielding the stated condition-number limit.

## Verification
The accompanying `verify_invertible_coordinate_frame.py` enumerates invertible matrices directly over prime fields and forms the complex Gram matrix from actual character values, independently of the rank-one/rank-two formula. It verifies counts, every matrix entry, the full eigenvalue spectrum, and the upper-mode crossover for \((q,d)=(2,2),(3,2),(5,2),(2,3),(3,3),(2,4)\). Run `python verify_invertible_coordinate_frame.py` with Python 3 and NumPy; expected final line: `ALL_CHECKS_PASS`. Finite tests are checks only; the proof above establishes the theorem for every prime power and dimension.

## Relationship to prior work
Delsarte's rank-metric association scheme yields character values constant on matrix-rank classes and supplies the historical finite-field Fourier framework. In particular, its general rank-character formulas imply the rank-one and rank-two input values used here. They do not, in the inspected paper, form the simultaneous constant-plus-coordinate Gram matrix or identify its exact Riesz bounds and dimension-four endpoint switch. Results for determinant-one \(2\)-by-\(2\) matrices (which coincide with the present domain for \(q=2,d=2\)), rank-one matrices, and symplectic-matrix subsets concern different sampling sets; the isolated overlap with \(q=2,d=2\) is a previously covered special case and is not claimed to be novel. The new assertion is the all-prime-power, all-dimensional Gram spectral classification and sharp crossover for *invertible* square matrices.

## Limitations
No claim is made that the basic rank-character identities are new, or that this spectrum optimizes sample weights or covers higher Fourier bands. The derivation uses a nontrivial additive character fixed consistently across entries; an arbitrary mixing of unrelated characters is outside the scope. Older representation-theoretic treatments of matrix-group restriction could contain equivalent formulas and warrant independent literature review. Independent validation has not been performed.

## References
- P. Delsarte, “Bilinear Forms over a Finite Field, with Applications to Coding Theory,” *Journal of Combinatorial Theory, Series A* **25** (1978), 226–241, DOI: `10.1016/0097-3165(78)90015-8`. Full primary text: Section 3 and Appendix.
- K.-U. Schmidt, “Symmetric Bilinear Forms over Finite Fields with Applications to Coding Theory,” `arXiv:1410.7184` (first public posting 2014-10-27), related work for the distinct symmetric-form rank scheme.
