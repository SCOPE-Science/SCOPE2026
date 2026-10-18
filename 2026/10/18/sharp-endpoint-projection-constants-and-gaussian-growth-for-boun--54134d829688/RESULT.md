# Sharp endpoint projection constants and Gaussian growth for bounded-order interactions

## Finding
Let \(r\ge4\) and \(2\le d\le r-2\). For finite sets \(X_i\) of sizes \(m_i\ge2\), let \(U_{r,d}\) be the real subspace of functions on \(X=\prod_{i=1}^r X_i\) expressible as sums of functions depending on at most \(d\) coordinates. Denote the minimum norm of a real linear projection onto this subspace in \(\ell_p(X)\) by \(\lambda_p(U_{r,d})\).

Set \(E_i\) to be averaging in coordinate \(i\) and \(D_i=I-E_i\). For \(B\subseteq[r]\), set \(P_B=\prod_{i\in B}D_i\prod_{i\notin B}E_i\). Then the orthogonal-in-the-counting-inner-product interaction truncation
\[
Q_d=\sum_{|B|\le d}P_B
\]
is a minimum-operator-norm projection onto \(U_{r,d}\) for **every** \(1\le p\le\infty\), among **all** real linear projections, not just permutation-equivariant ones.

Define \(M=\prod_i m_i\). For \(A\subseteq[r]\), define \(z_i(A)=m_i-1\) if \(i\in A\), and \(z_i(A)=-1\) otherwise. Write \(e_j(z)\) for the degree-\(j\) elementary symmetric polynomial, with \(e_0=1\). The sharp endpoint norm is
\[
\boxed{\lambda_1(U_{r,d})=\lambda_\infty(U_{r,d})=
\frac1M\sum_{A\subseteq[r]}\Bigl(\prod_{i\notin A}(m_i-1)\Bigr)
\left|\sum_{j=0}^d e_j(z(A))\right|.}
\]
In the equicardinal case \(m_i=q\ge2\), equivalently
\[
\lambda_\infty(U_{r,d})=\frac1{q^r}\sum_{h=0}^r\binom rh(q-1)^{r-h}
\left|\sum_{j=0}^{d}[t^j](1+(q-1)t)^h(1-t)^{r-h}\right|.
\]
For each fixed \(q\ge2\) and fixed \(d\ge2\), as \(r\to\infty\) through integers satisfying \(r\ge d+2\),
\[
\boxed{\lim_{r\to\infty}r^{-d/2}\lambda_\infty(U_{r,d})
=\frac{(q-1)^{d/2}}{d!}\,\mathbb E|\operatorname{He}_d(Z)|,}
\]
where \(Z\) is standard normal and the probabilists' Hermite polynomials are specified by \(e^{tz-t^2/2}=\sum_{j\ge0}\operatorname{He}_j(z)t^j/j!\). For pairwise interactions this specializes to the explicit sharp linear-growth law
\[
\lim_{r\to\infty}\frac{\lambda_\infty(U_{r,2})}{r}
=(q-1)\sqrt{2/\pi}\,e^{-1/2}.
\]
For example \(\lambda_\infty(U_{4,2})=9/4\) for binary coordinates and \(91/27\) for ternary coordinates. Also \(\lambda_2(U_{r,d})=1\).

## Assumptions and scope
All scalars are real; \(\ell_p(X)\) is finite-dimensional and equipped with its usual counting-measure norm (uniform normalization, if used, has the same operator norms). The integer cutoff \(d\) is between two and \(r-2\) inclusive. There are no restrictions on the finite coordinate sizes except \(m_i\ge2\). Minimality holds at all Banach exponents; the **evaluated** constants here concern only \(p=1\) and \(p=\infty\), plus \(p=2\). The Gaussian limit is for fixed finite alphabet size and fixed interaction order, not a jointly growing order or alphabet.

## Proof
**Interaction decomposition.** On the finite-dimensional space of functions on \(X\), the commuting idempotents \(E_i\) and \(D_i\) give mutually annihilating projections \(P_B\) with \(\sum_B P_B=I\). A function independent of coordinates outside \(C\) is annihilated by every \(P_B\) with \(B\not\subseteq C\). Conversely, each \(P_B f\) depends only on coordinates in \(B\). It follows that \(\operatorname{ran}Q_d=U_{r,d}\), \(Q_d^2=Q_d\), and \(Q_d\) is symmetric for the counting inner product.

**Global least-norm property.** Let \(G=\prod_i\operatorname{Sym}(X_i)\) act by independent coordinate permutations. This action is isometric on every \(\ell_p(X)\), including the endpoints, and stabilizes \(U_{r,d}\). Average any projection \(R\) onto \(U_{r,d}\) over \(G\). The resulting projection \(\bar R\) has norm at most \(\|R\|\) and commutes with \(G\). To see that \(Q_d\) is the unique such projection, note that a matrix commuting with \(G\) has entries depending only on the equality pattern \(\{i:x_i=y_i\}\). Its space is therefore spanned by the \(2^r\) products of coordinate identities and coordinate-averaging matrices, equivalently by the \(P_B\). Thus \(\bar R=\sum_B c_BP_B\). Because it fixes the range \(U_{r,d}\), each coefficient for \(|B|\le d\) must be one; because its image lies in that range, the other coefficients are zero. Therefore \(\bar R=Q_d\). This proves \(\|Q_d\|\le\|R\|\) without assuming \(R\) equivariant.

**Exact endpoint norm.** An individual kernel entry of \(E_i\) equals \(1/m_i\), while that of \(D_i\) equals \((m_i-1)/m_i\) on a matching coordinate and \(-1/m_i\) on a mismatch. Consequently the \((x,y)\) entry of \(Q_d\) is \(M^{-1}\sum_{j=0}^d e_j(z(A))\), where \(A=\{i:x_i=y_i\}\). For fixed \(x\) and \(A\), there are exactly \(\prod_{i\notin A}(m_i-1)\) choices of \(y\) with that equality set. Every row has the same absolute sum, giving the displayed \(\ell_\infty\) norm. Since the matrix is symmetric, its maximum absolute column sum is equal, giving the \(\ell_1\) norm. Grouping equal-sized-coordinate terms by \(h=|A|\) yields the binomial formula. The \(p=2\) assertion follows from orthogonality.

**Sharp Gaussian growth.** Let \(Y_1,\dots,Y_r\) be independent with \(\mathbb P(Y_i=q-1)=1/q\) and \(\mathbb P(Y_i=-1)=(q-1)/q\). Then each has mean zero and variance \(q-1\). Write \(V_{r,j}=\sum_{|B|=j}\prod_{i\in B}Y_i\). The endpoint norm is \(\mathbb E|\sum_{j=0}^d V_{r,j}|\). The generating function
\[
\prod_{i=1}^r\left(1+\frac{tY_i}{\sqrt{r(q-1)}}\right)
=\sum_{j=0}^r\frac{t^jV_{r,j}}{[r(q-1)]^{j/2}}
\]
converges coefficientwise in distribution through every fixed degree to \(\exp(tZ-t^2/2)\). Indeed its logarithm is \(t\sum_iY_i/\sqrt{r(q-1)}-t^2\sum_iY_i^2/[2r(q-1)]+o_{\mathbb P}(1)\), with the first term tending to \(tZ\) by the central limit theorem and the second to \(-t^2/2\) by the law of large numbers; the remainder and its derivatives of each fixed order vanish uniformly on compact sets in probability. Hence
\[
r^{-d/2}\sum_{j=0}^d V_{r,j}\ \Longrightarrow\ \frac{(q-1)^{d/2}}{d!}\operatorname{He}_d(Z).
\]
Moreover, centered independence gives \(\mathbb E(V_{r,j}V_{r,k})=0\) for distinct degrees and \(\mathbb E V_{r,j}^2=\binom rj(q-1)^j\), so these normalized random variables are uniformly bounded in \(L^2\). Their absolute values are uniformly integrable and their expectations converge. Finally \(\operatorname{He}_2(Z)=Z^2-1\) and \(\mathbb E|Z^2-1|=4e^{-1/2}/\sqrt{2\pi}\), which gives the explicit pairwise constant.

## Verification
The standalone script `verify.py` uses only Python's standard library. Run it with `python verify.py` in the directory containing that file. It constructs the exact integer-scaled kernel matrix for eight mixed and equal-size examples, verifies symmetry, full idempotence, rank via the diagonal trace, and equality of the row-sum norm with the combinatorial formula. It also evaluates \(9/4\) and \(91/27\) exactly, compares the two equivalent finite formulas for many small parameter choices, and checks finite-dimensional numerical convergence consistent with the proved Gaussian scaling. The latter is a sanity check, not a proof of the limit.

## Relationship to prior work
Kozdęba's 2018 minimal-projection formula concerns the three-variable subspace of functions missing one coordinate; his 2020 paper concerns one-coordinate additive summands. Kozdęba and Kozdęba (2025), Theorem 16, determine minimal projections for the \(r-1\)-coordinate subspace, and their concluding section specifically identifies intermediate coordinate orders as further work. The present domain \(2\le d\le r-2\) does not occur in those evaluated statements. Rudin's averaging theorem and finite permutation symmetry are established techniques and are **not** proposed as novel. Similarly, the classical Krawtchouk-to-Hermite limit, including Minabutdinov's 2015 strengthening, is an ingredient, **not** a new polynomial asymptotic. The quantified statement here is the sharp operator minimum, its explicit endpoint value for every finite alphabet product, and the induced Gaussian limiting minimum in the previously unevaluated interaction range. The generic averaging principle alone does not specify these numerical minima.

## Limitations
No formula is asserted for the optimal \(\ell_p\) norm when \(1<p<\infty\) and \(p\ne2\). The Gaussian growth conclusion fixes \(d\) and \(q\). The proof does not assert uniqueness among *all* norm-minimizing projections, only uniqueness among permutation-equivariant projections. Different terminology in the Fourier, Krawtchouk or approximation-theory literature could conceal prior equivalence; originality is not independently audited.

## References
- M. Kozdęba, "Minimal projection onto certain subspace of \(L_p(X\times Y\times Z)\)," *Numerical Functional Analysis and Optimization* 39 (2018), 1407–1422. DOI: 10.1080/01630563.2018.1479716. First online 2018-09-10.
- M. Kozdęba, "Uniqueness of minimal projections in smooth expanded matrix spaces," *Monatshefte für Mathematik* 194 (2021), 275–289; first online 2020-10-18. DOI: 10.1007/s00605-020-01471-y.
- A. Kozdęba and M. Kozdęba, "On the Minimality of Projections in Expanded Matrix Spaces," *Symmetry* 17 (2025), 1835. DOI: 10.3390/sym17111835. In particular Theorem 16 and Section 5.
- A. Minabutdinov, "The higher order asymptotic expansion of the Krawtchouk polynomials," arXiv:1508.07421 (2015), Sections 1–2.
