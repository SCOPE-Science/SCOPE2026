# Exact Walsh-tail quotient norms for complete multipartite chaoses

## Finding

Fix an integer \(r\ge2\), nonempty pairwise disjoint coordinate blocks \(B_1,\ldots,B_r\) with sizes \(n_j\ge1\), and \(N=\sum_{j=1}^r n_j\). On the uniform real Boolean cube \(\{-1,1\}^N\), let
\[
S_j(x)=\sum_{i\in B_j}x_i,\qquad Q(x)=\prod_{j=1}^r S_j(x).
\]
Write \(\mathcal T_{>r}\) for the linear space of real functions whose Walsh coefficients vanish in every degree at most \(r\). Then the **exact quotient norm** of this complete \(r\)-partite homogeneous chaos is
\[
\boxed{\inf_{R\in\mathcal T_{>r}}\|Q+R\|_\infty
=\prod_{j=1}^r\frac{4^{m_j}}{\binom{2m_j}{m_j}},\qquad m_j=\lfloor n_j/2\rfloor.}
\]
An optimizer is \(F_*(x)=C\prod_j\operatorname{sgn}(S_j(x))\), with \(\operatorname{sgn}(0)=0\) and \(C\) the boxed product. If all block sizes are odd, this is the **unique** optimal representative in the affine coset \(Q+\mathcal T_{>r}\); in every case all minimizers agree with \(F_*\) wherever \(Q\ne0\).

There is a quantitative stability form. For any \(F\in Q+\mathcal T_{>r}\) such that \(\|F\|_\infty\le(1+\varepsilon)C\), with \(\varepsilon\ge0\),
\[
\mathbb E\big[|Q|\,|F-F_*|\big]\le 2\varepsilon C\,\mathbb E|Q|.
\]
For fixed \(r\) and \(\min_j n_j\to\infty\), the exact parity-sensitive asymptotic is
\[
C=\left(\frac\pi2\right)^{r/2}\prod_{j=1}^r\sqrt{n_j}
\left(1+\frac14\sum_{j=1}^r\frac{(-1)^{n_j}}{n_j}
+O_r\big((\min_j n_j)^{-2}\big)\right).
\]
In particular, when every \(n_j\sim N/r\), the quotient norm is asymptotic to \((\pi N/(2r))^{r/2}\), despite \(\|Q\|_\infty=\prod_j n_j\) growing at the higher degree \(r\).

## Assumptions and scope

All functions are real-valued; the cube carries uniform probability measure \(2^{-N}\), and all norms are uniform (supremum) norms. For \(T\subseteq\{1,\ldots,N\}\), \(\chi_T(x)=\prod_{i\in T}x_i\) and \(\widehat f(T)=\mathbb E[f\chi_T]\). The optimization is over **all** higher-degree Walsh functions, not merely symmetric corrections. Empty higher-degree tails, including the case \(N=r\), are permitted. The sizes \(n_j\) need not be equal. The assertion is not about arbitrary coefficients on a multipartite hypergraph or arbitrary hypergraph edge supports.

## Proof

**1. A one-block coefficient identity.** Let \(X_1,\dots,X_n\) be independent uniform signs, \(S=X_1+\cdots+X_n\), and \(m=\lfloor n/2\rfloor\). By permutation symmetry and \(\sum_i X_i=S\),
\[
\mathbb E[X_i\operatorname{sgn}S]=\frac{\mathbb E|S|}{n}=:\alpha_n.
\]
Conditioning on \(T=S-X_i\) gives \(\mathbb E_{X_i}[X_i\operatorname{sgn}(T+X_i)]=(\operatorname{sgn}(T+1)-\operatorname{sgn}(T-1))/2\). If \(n=2m+1\), this equals one precisely when \(T=0\); if \(n=2m\), it equals one half precisely when \(|T|=1\). The corresponding binomial probabilities imply, in both cases,
\[
\alpha_n=4^{-m}\binom{2m}{m}>0,\qquad \mathbb E|S|=n\alpha_n.
\]

**2. Sharp lower bound.** Orthogonality and the fact that \(Q\) is homogeneous of degree \(r\) give \(\mathbb E[QF]=\mathbb E[Q^2]=\prod_j n_j\) for every \(F=Q+R\) with \(R\in\mathcal T_{>r}\). Since the block sums are independent,
\[
\prod_j n_j=\mathbb E[QF]\le\|F\|_\infty\mathbb E|Q|
=\|F\|_\infty\prod_j(n_j\alpha_{n_j}).
\]
Thus \(\|F\|_\infty\ge C:=\prod_j\alpha_{n_j}^{-1}\).

**3. Exact attainment.** Put \(G(x)=\prod_j\operatorname{sgn}(S_j(x))\). Each one-block sign function is odd under simultaneous reversal of that block, so its Walsh expansion contains only characters of **odd cardinality** from that block. Consequently the expansion of \(G\) has no term of degree less than \(r\). Every degree-\(r\) term selects exactly one coordinate from each block and has coefficient \(\prod_j\alpha_{n_j}=C^{-1}\); all other degree-\(r\) coefficients vanish. The degree-\(r\) Fourier polynomial of \(CG\) is therefore exactly \(Q\), hence \(F_*:=CG\in Q+\mathcal T_{>r}\). Since \(|G|\le1\) and equals one at the all-positive input, \(\|F_*\|_\infty=C\). This attains the lower bound.

**4. Equality and stability.** For any admissible \(F\) define a probability measure \(d\nu=|Q|\,d\mathbb P/\mathbb E|Q|\) and, on its support, \(h=\operatorname{sgn}(Q)F/C\). The fixed Fourier data imply \(\mathbb E_\nu h=1\). If \(\|F\|_\infty\le(1+\varepsilon)C\), then \(h\le1+\varepsilon\); writing \(h-1=(h-1)_+-(1-h)_+\) and using its zero mean gives \(\mathbb E_\nu|h-1|=2\mathbb E_\nu(h-1)_+\le2\varepsilon\). On \(Q\ne0\), \(F_*=C\operatorname{sgn}(Q)\); multiplication by \(C\mathbb E|Q|\) gives the stated stability inequality. Equality at \(\varepsilon=0\) forces \(F=F_*\) on \(Q\ne0\). If every \(n_j\) is odd, no block sum can vanish, proving uniqueness on the entire cube.

**5. Asymptotics.** The standard central-binomial Stirling expansion is
\[
4^{-m}\binom{2m}{m}=(\pi m)^{-1/2}\left(1-\frac1{8m}+O(m^{-2})\right).
\]
Replace \(m\) by \(n/2\) for even \(n\), and by \((n-1)/2\) for odd \(n\). This yields \(\alpha_n^{-1}=\sqrt{\pi n/2}(1+(-1)^n/(4n)+O(n^{-2}))\). Multiply the \(r\) expansions, with fixed \(r\), to obtain the displayed parity-sensitive formula.

## Verification

The standalone standard-library program `checks/verify.py` exhaustively verifies the integer Walsh–Hadamard coefficients of the constructed optimizers and their sharp dual pairings for 269 block-size tuples with two to four blocks and total dimension at most eleven. It also tests the weighted stability inequality under a high-degree parity perturbation. All 269 cases passed. These finite tests check normalization and boundary cases; the preceding proof establishes the result for all block sizes and all \(r\ge2\).

## Relationship to prior work

Defant, Galicer, Mansilla, Mastyło and Muro (arXiv:2302.00233, first posted February 1, 2023), Theorem 3.1, determine the **projection constant** of a Walsh spectral subspace as the mean absolute value of its character sum. Applied to the complete multipartite degree-\(r\) support, this gives \(\mathbb E|Q|\), a related but different invariant. Their result does not state the uniform norm of the particular coset \(Q+\mathcal T_{>r}\), its rigidity, or its stability. Our lower bound is naturally dual to that projection formula; the additional special Fourier-spectrum property of a product of sign-of-sum functions supplies equality. One should not infer this equality for general hypergraphs: for the triangle's quadratic edge polynomial, the same lower bound is strict.

Eskenazis and Zhang (arXiv:2311.09021, November 15, 2023) study approximation by Walsh tails, including \(L_1\) bounds for symmetric polynomials and comparison inequalities. Their full preprint does not furnish this exact real \(L_\infty\) multipartite formula or its stability. Oleszkiewicz's 2017 Rademacher-sum estimates, as discussed there, concern one-block linear sums and do not state this multi-block chaos result. The factorization makes the present extremal family unusually tractable; elementary tensor-product reformulations remain a residual novelty risk.

## Limitations

The result is a sharp calculation for one natural family of uniformly weighted, multipartite homogeneous polynomials. It does not give a general exact quotient norm for arbitrary Walsh polynomials, weighted parts, or general hypergraphs; for even block sizes uniqueness is asserted only off the zero set of \(Q\). The asymptotic error applies to fixed \(r\), not to \(r\) growing with dimension. The computational checks are finite and do not substitute for the proof. Independent mathematical validation has not been performed.

## References

- A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233 (first version February 1, 2023), especially Theorem 3.1. https://arxiv.org/abs/2302.00233
- A. Eskenazis and H. Zhang, *Approximation of polynomials from Walsh tail spaces*, arXiv:2311.09021 (first version November 15, 2023), especially Proposition 1 and Theorems 2–4. https://arxiv.org/abs/2311.09021
