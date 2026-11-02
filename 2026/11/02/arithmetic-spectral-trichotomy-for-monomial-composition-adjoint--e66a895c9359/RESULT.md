# Arithmetic spectral trichotomy for monomial composition–adjoint products

## Finding
On the complex Hardy space \(H^2(\mathbb D)\), let \(C_k f=f(z^k)\) for integers \(k\ge2\), and set \(T_{m,n}=C_m C_n^*\). Put \(d=\gcd(m,n)\), \(p=m/d\), \(q=n/d\). For \(m\ne n\) all these contractions have the same ordinary and Fredholm-essential spectrum, namely \(\overline{\mathbb D}\), and satisfy the exact completely isometric, essential-norm polynomial calculus
\[
\|F(T_{m,n})\|=\|F(T_{m,n})\|_{\mathrm{ess}}=\max_{|z|=1}\|F(z)\|,
\]
for every finite square matrix polynomial \(F(z)=\sum_{j=0}^s A_jz^j\) (operators on \(H^2\otimes\mathbb C^h\), with essential norm there). Their point spectra and power dynamics split sharply into three arithmetic cases:

(a) If \(q=1<p\) (\(n\mid m\)), the positive-degree restriction is an orthogonal sum of infinitely many forward unilateral shifts and, possibly, one-dimensional zeros. Its point spectrum is \(\{0,1\}\); its powers do not converge strongly to the constant projection.

(b) If \(p=1<q\) (\(m\mid n\)), the positive-degree restriction is an orthogonal sum of infinitely many backward unilateral shifts and, possibly, one-dimensional zeros. Its point spectrum is \(\mathbb D\cup\{1\}\); its powers converge strongly to the projection onto constants.

(c) If \(p,q>1\), the positive-degree restriction is an orthogonal sum of finite nilpotent Jordan chains; in particular every chain length occurs with infinite multiplicity. Its point spectrum is \(\{0,1\}\), yet its approximate-point spectrum is the entire closed disk, and its powers converge strongly to the constant projection.

Here the constant monomial always gives a one-dimensional reducing identity summand. In case (a), if \(n=1\) there are no zero summands; the stated theorem assumes \(n\ge2\), so zero summands are present. In case (b), \(m\ge2\), so zero summands are present. In the excluded diagonal case \(m=n\), \(T_{m,m}\) is instead the orthogonal projection onto the span of \(\{z^{mk}:k\ge0\}\), with spectrum \(\{0,1\}\).

## Assumptions and scope
All operators act on complex \(H^2(\mathbb D)\) with normalized orthonormal basis \(e_k(z)=z^k\), \(k\in\mathbb N_0\). "Fredholm-essential spectrum" means the set of scalars for which \(T-\lambda I\) is not Fredholm. \(S\) denotes the standard isometric unilateral forward shift, \(S^*\) its backward adjoint, and \(J_L\) the nilpotent forward shift of dimension \(L\). Matrix polynomials are evaluated by coefficientwise spatial amplification. No unbounded symbols or weighted Bergman spaces are included.

## Proof
1. **Exact basis action.** Since \(C_m e_k=e_{mk}\), each \(C_m\) is an isometry and
\[
T_{m,n}e_j=\begin{cases}e_{(m/n)j},&n\mid j,\\0,&n\nmid j.\end{cases}
\]
(The quotient index is an integer in the indicated case; the divisibility condition is essential even when the rational product happens to be integral elsewhere.) Consequently every positive index has at most one outgoing and one incoming arrow. The directed edges \(nk\to mk\), \(k\ge1\), form disjoint chains; \(e_0\) is fixed.

2. **Divisibility classification.** Write \(m=dp\), \(n=dq\), \(\gcd(p,q)=1\). If \(q=1<p\), then each chain containing a multiple of \(n\) proceeds forever in the forward direction, because multiplying by \(p\) preserves divisibility by \(n\). Its backward direction stops after finitely many steps, because a nonzero integer cannot be divisible by arbitrarily high powers of \(p\). The remaining indices \(j\) with \(n\nmid j\) are isolated zeros. There are infinitely many disjoint forward chains, obtained by starting from \(n r\) with \(p\nmid r\), and \(r\) ranging over infinitely many positive integers. If \(p=1<q\), reverse every arrow and exchange \(m,n\): this yields infinitely many backward-shift chains and isolated zeros.

If \(p,q>1\), every forward chain is finite: after \(s\) steps its index would be \(j p^s/q^s\), forcing \(q^s\mid j\), impossible for unbounded \(s\). The backward direction is finite by the analogous \(p\)-divisibility argument. For every \(N\ge0\) and every \(r\ge1\) coprime to \(pq\), the indices
\[
 d q^N r,\ d p q^{N-1}r,\dots,\ d p^N r
\]
form a maximal forward Jordan chain of length \(N+1\). Its first vertex is not divisible by \(m\), its last vertex not divisible by \(n\). Distinct \(r\) at fixed \(N\) give disjoint chains (unique coprime \(p,q\)-factor powers). Thus every Jordan length has infinite multiplicity. Together with the elementary in/out-degree condition, this proves each asserted orthogonal decomposition. When \(m=n\), the basis action becomes a coordinate projection.

3. **Spectra.** For \(m\ne n\), the operator is a direct sum of one identity and either infinitely many copies of \(S\), infinitely many copies of \(S^*\), or arbitrarily long finite \(J_L\) with infinite multiplicities. The resolvent exists for \(|\lambda|>1\) by the Neumann series. For \(|\lambda|\le1\), each shift model, or the long-Jordan-block model, has approximate eigenvectors for the asserted spectral set. For the Jordan case with \(|\lambda|<1\), take the length-\(L\) vector with coefficients proportional to \((\lambda^{L-1},\ldots,\lambda,1)\); its residual is of order \(|\lambda|^L\); on the unit circle use unit-modulus coefficients with residual of order \(L^{-1/2}\). Choosing disjoint chains yields weakly null approximate eigensequences, hence non-Fredholmness. In the \(S\) case, the open disk is residual spectrum with infinite-dimensional cokernel, while in the \(S^*\) case it is point spectrum with infinite-dimensional kernel; the unit circle is essential in either case. The finite-Jordan case has only zero eigenvalues off \(e_0\), and the forward case likewise; the backward case has every open-disk eigenvalue. These observations prove all spectral claims.

4. **Completely isometric polynomial and essential norms.** Every summand of \(T\) is a compression of the forward shift, its adjoint, or a scalar identity, so matrix-valued von Neumann's inequality gives \(\|F(T)\|\le\max_{\mathbb T}\|F(z)\|\). Conversely, the norm of \(F(S)\) (and also \(F(S^*)\)) equals that boundary supremum by the Hardy multiplication model. The compressions \(F(J_L)\) converge strongly to \(F(S)\) on finitely supported vectors as \(L\to\infty\), so their norms approach the boundary supremum. In each arithmetic case infinitely many copies of the appropriate model, or infinite copies of every \(J_L\), occur on mutually orthogonal subspaces. For each candidate norming vector, translations to distinct equal-model summands yield a weakly null sequence with unchanged image norm. Compact operators vanish along that sequence. Thus \(\|F(T)\|_{\mathrm{ess}}\ge\max_{\mathbb T}\|F(z)\|\), completing equality. In the backward case, \(F(S^*)\) has the same norm via adjointing coefficient matrices and conjugating the circle parameter.

5. **Power topology.** On every finite Jordan chain, powers eventually vanish. Likewise, powers of the backward unilateral shift converge strongly to zero, first on finitely supported vectors and then by uniform boundedness. The direct-sum dominated convergence argument gives \(T^k\to P_0\) strongly for cases (b) and (c), where \(P_0\) projects onto constants. Conversely, a forward-shift summand preserves the norm of each nonzero vector under all powers, excluding strong convergence to \(P_0\) in case (a). The diagonal case is an orthogonal projection and has different behavior.

## Verification
The entire argument is analytic and uses no extrapolation from truncations. The accompanying small deterministic checker compares the exact edge rule, finite chain endpoints, and finite-matrix polynomial lower-bound samples for several distinct \((m,n)\) pairs. Those checks are supplementary, not substitutes for the all-integer proof. The matrix-polynomial assertion is for fixed finite coefficient dimensions; no arbitrary operator-valued coefficient algebra is asserted.

## Relationship to prior work
Leng and Zhao (2026), Theorem 3.24, establish Schatten membership equivalence for \(C_\varphi C_\psi^*\) with inner \(\psi\); our monomial products fall outside every finite Schatten class, consistent with their theorem. Their Theorem 3.17 treats other product order in the Hilbert–Schmidt setting. The statements inspected do not identify the number-theoretic shift/Jordan decomposition, its point-spectrum trichotomy, strong-power boundary, or completely isometric essential polynomial calculus. These further conclusions derive from a direct exact arithmetic orbit decomposition plus standard shift theory. The classic infinite-multiplicity and shift-norm ingredients are not claimed separately as innovations.

## Limitations
This is a special-symbol theorem; it does not classify products for general finite Blaschke factors or arbitrary Hardy composition symbols. A different or earlier full spectral classification in the composition-operator literature remains possible despite the source and record searches. No independent expert or external mathematical validation has been performed. The polynomial functional calculus is proved for finite matrix-polynomial amplifications, not for all bounded Borel functions.

## References
- Q. Leng and X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1 (first public 2026-10-11), especially Theorems 3.17 and 3.24, https://arxiv.org/html/2610.15472v1 .
- L. He, Y. Yan, S. Zhang, and X. Zhao, *Some Properties of Products of Linear Fractional Composition Operators on Weighted Dirichlet Spaces*, arXiv:2609.29897 (2026-09-24), https://arxiv.org/abs/2609.29897 .
- Classical unilateral-shift multiplication model and matrix-valued von Neumann inequality (standard operator theory).
