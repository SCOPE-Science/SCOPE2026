# A phase-independent singular-value Weyl law for Binet recurrence derivatives on Fock space

## Finding

Let \(U_n=\sum_{j=1}^m A_j\lambda_j^n\) be a nonzero complex Binet recurrence, with pairwise distinct nonzero roots \(\lambda_j\), nonzero coefficients \(A_j\), and the Ward normalization \(U_0=\sum_j A_j=0\). On the standard Gaussian Bargmann–Fock Hilbert space \(\mathcal F^2\), let \(D_U\) be the polynomial operator
\[
D_U f(z)=\frac{\sum_{j=1}^m A_j f(\lambda_j z)}{z},
\]
with its removable value at the origin. Write \(R=\max_j|\lambda_j|\). Then exactly the following alternatives hold:

1. If \(R>1\), no bounded operator on \(\mathcal F^2\) extends \(D_U\) on polynomials.
2. If \(R<1\), the extension is compact and belongs to every Schatten class \(\mathcal S_p\), for each \(p>0\).
3. If \(R=1\), the extension is compact, and writing \(c_U=\sum_{|\lambda_j|=1}|A_j|^2>0\), its singular values in nonincreasing order satisfy the exact Weyl law
\[
\lim_{k\to\infty} k\,s_k(D_U)^2=c_U,
\qquad
s_k(D_U)\sim\sqrt{\frac{c_U}{k}}.
\]
Consequently, in this critical case \(D_U\in\mathcal S_p\) precisely when \(p>2\); it belongs to weak Schatten \(\mathcal S_{2,\infty}\) but not \(\mathcal S_2\). Furthermore,
\[
\sum_{k=1}^N s_k(D_U)^2=c_U\log N+o(\log N),
\qquad
\sum_{n=1}^N\frac{|U_n|^2}{n}=c_U\log N+O(1).
\]
The coefficient is independent of all arguments of the characteristic roots, including rational relations, periodic zeros, or irrational rotations.

For the Jackson difference derivative \(D_q f(z)=[f(z)-f(qz)]/[(1-q)z]\), \(0<|q|\ne1\) or \(|q|=1\) with \(q\ne1\), the critical coefficient is
\[
\lim_{k\to\infty}k\,s_k(D_q)^2
=\begin{cases}|1-q|^{-2},&0<|q|<1,\\ 2|1-q|^{-2},&|q|=1,\ q\ne1,\end{cases}
\]
and \(|q|>1\) gives no bounded Fock-space extension. In particular, for every nontrivial point of the unit circle the coefficient jumps by a factor of two on passage from the open disk to the boundary.

## Assumptions and scope

The Hilbert space is normalized by
\[
\|f\|_{\mathcal F^2}^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)
=\sum_{n=0}^{\infty}n!|a_n|^2,
\qquad f(z)=\sum_{n\ge0}a_n z^n.
\]
All roots and coefficients are fixed finite Binet data, the roots are distinct and nonzero, and \(U_0=0\); the theorem does not assert such results for confluent roots, infinite Binet sums, or other Fock-space normalizations. The singular values are those of the compact extension in the two bounded regimes. The critical limit concerns rank \(k\to\infty\), not the monomial-index order, which need not converge because of cancellations.

## Proof

**1. Matrix reduction and boundedness.** The normalized monomials \(e_n=z^n/\sqrt{n!}\) form an orthonormal basis, and the Ward condition makes the quotient analytic at the origin. Direct substitution, first on polynomials, gives
\[
D_U e_0=0,\qquad D_U e_n=\frac{U_n}{\sqrt n}\,e_{n-1}\quad(n\ge1).
\]
Thus the operator is a unilateral weighted backward shift, and, when bounded, \(D_U^*D_U\) is diagonal with entries \(|U_n|^2/n\) for \(n\ge1\), in addition to the zero entry at \(n=0\). Its nonzero singular values are exactly the decreasing rearrangement of \(\{|U_n|/\sqrt n:n\ge1\}\).

If \(R<1\), \(|U_n|\le(\sum_j|A_j|)R^n\). All weighted-shift entries decay geometrically, proving compactness and \(\mathcal S_p\) membership for all \(p>0\). If \(R=1\), they are bounded by \((\sum_j|A_j|)/\sqrt n\); the operator is compact. In both regimes the extension agrees pointwise with the original entire-function quotient: polynomial truncations converge in \(\mathcal F^2\), and every point evaluation is continuous.

If \(R>1\), write \(U_n=R^n(V_n+E_n)\), where
\[
V_n=\sum_{|\lambda_j|=R} A_j (\lambda_j/R)^n,
\qquad E_n\longrightarrow0.
\]
Distinct roots have distinct boundary phases, so the elementary geometric-sum identity gives
\[
\lim_{N\to\infty}\frac1N\sum_{n=1}^N|V_n|^2
=\sum_{|\lambda_j|=R}|A_j|^2>0.
\]
Because \(V_n\) is bounded, it follows that \(|V_n+E_n|\) stays bounded away from zero along infinitely many indices. Therefore \(|U_n|/\sqrt n\) is unbounded, excluding a bounded extension.

**2. Uniform distribution of the finite oscillatory symbol.** Now suppose \(R=1\). Separate unit roots from the strictly contracting roots:
\[
U_n=V_n+O(\rho^n),\qquad V_n=\sum_{j\in J}A_j\lambda_j^n,
\qquad J=\{j:|\lambda_j|=1\},
\]
where any \(0<\rho<1\) larger than all subunit moduli may be chosen (and the remainder is exactly zero if there are none). Let \(K\) be the compact subgroup of \(\mathbb T^{|J|}\) generated, in the closure sense, by \(g=(\lambda_j)_{j\in J}\). The powers \(g^n\) are equidistributed in Haar probability measure on \(K\): for every continuous character \(\chi\), its Cesàro average is \(1\) if \(\chi(g)=1\), otherwise a bounded geometric sum divided by \(N\) and hence tends to zero; characters are uniformly dense in the continuous functions on \(K\).

Consequently the bounded sequence \(b_n=|U_n|^2\) has a limiting empirical probability law \(\mu\), the distribution under Haar measure of \(|\sum_{j\in J}A_jz_j|^2\). Character orthogonality, or the same finite geometric-sum calculation, gives
\[
\int t\,d\mu(t)=\lim_{N\to\infty}\frac1N\sum_{n=1}^N b_n
=\sum_{j\in J}|A_j|^2=c_U.
\]
The remainder \(O(\rho^n)\) affects neither empirical convergence nor the mean.

**3. Counting-to-Weyl lemma.** Let a bounded sequence \(0\le b_n\le B\) have empirical distribution \(\mu\) as above. Put \(M(\varepsilon)=\#\{n\ge1:b_n/n>\varepsilon\}\). Then
\[
\lim_{\varepsilon\downarrow0}\varepsilon M(\varepsilon)
=\int_0^B\mu((t,\infty))\,dt=\int t\,d\mu(t).
\]
Here is a proof without any unproved distributional regularity. Fix a partition \(0=t_0<t_1<\cdots<t_h=B\), choosing all interior cut points outside the countable set of atoms of \(\mu\). The interval of indices satisfying \(t_{i-1}/\varepsilon<n\le t_i/\varepsilon\) contains approximately \((t_i-t_{i-1})/\varepsilon\) terms. Empirical convergence on prefixes implies that the scaled count on such a block with \(b_n>t_i\), respectively \(b_n\ge t_{i-1}\), tends to \((t_i-t_{i-1})\mu((t_i,\infty))\), respectively \((t_i-t_{i-1})\mu([t_{i-1},\infty))\), whenever the cut point is not an atom. These counts bound the desired block count from below and above; endpoint atoms at \(0,B\) affect only the two boundary blocks, whose total error is at most twice the partition mesh. The resulting upper and lower sums converge, as the mesh tends to zero, to the layer-cake integral shown above. Indices beyond \(B/\varepsilon\) never contribute.

Apply the lemma to \(b_n=|U_n|^2\). By the matrix reduction, \(M(\varepsilon)=\#\{k:s_k(D_U)^2>\varepsilon\}\). Since \(\varepsilon M(\varepsilon)\to c_U>0\), elementary inversion of these monotone counting functions yields \(k\,s_k(D_U)^2\to c_U\), establishing the pointwise sharp singular-value asymptotic without any irrationality or nonvanishing assumption on the individual \(U_n\).

**4. Schatten and logarithmic consequences.** As \(s_k(D_U)^2\sim c_U/k\), the Schatten sum \(\sum_k s_k(D_U)^p\) converges precisely when \(p>2\), while \(\sup_k\sqrt k\,s_k(D_U)<\infty\). Summing the rearranged squares gives \(\sum_{k\le N}s_k(D_U)^2=c_U\log N+o(\log N)\).

For the stronger monomial-index sum, expand \(|U_n|^2\) into pairs of Binet modes. The diagonal pairs from distinct unit roots yield \(c_U/n\). All other pairs with modulus below one have absolutely summable contributions. Every cross pair of distinct unit roots has multiplier \(\lambda_j\overline{\lambda_\ell}\ne1\), and its harmonic sum \(\sum_{n\le N}(\lambda_j\overline{\lambda_\ell})^n/n\) is bounded uniformly in \(N\) by summation by parts. This proves the \(O(1)\) remainder.

**5. Jackson boundary transition.** In the Jackson quotient take \((A_1,A_2)=((1-q)^{-1},-(1-q)^{-1})\) with \((\lambda_1,\lambda_2)=(1,q)\). If \(0<|q|<1\), only the first root is on the unit circle, giving \(c_U=|1-q|^{-2}\). If \(|q|=1\) and \(q\ne1\), both roots contribute, giving \(c_U=2|1-q|^{-2}\). If \(|q|>1\), the first case of the trichotomy applies. This proves the stated exact jump.

## Verification

A standalone finite checker accompanies the result. It verifies the exact monomial coefficient identity, the Ward normalization, and finite sorted-singular-value samples for a periodic cancellation example and an irrational rotation example. It additionally checks the Jackson coefficients. These computations test implementation and normalization only; the all-index asymptotic and counting lemma are proved above. To reproduce, run `python3 checker.py` using a Python standard-library interpreter. The actual analytic normalization is \(\|z^n\|^2=n!\), so any alternative Gaussian scale changes all displayed singular values.

## Relationship to prior work

Orozco López, *The U-Derivative Associated with Linear Recurrence Sequences*, arXiv:2610.20593v1 (first posted 2026-10-14), provides the Binet quotient and monomial identity and classifies algebraic properties of recurrence calculi. The sections inspected do not supply its boundedness classification on the classical Gaussian Fock Hilbert space or the sharp rank-ordered singular-value limit. Alpay, Cerejeiras, and Kähler, arXiv:2112.07883, construct Fock-type Hilbert spaces adapted to more general Gelfond–Leontiev derivatives and study sampling; this does not entail a spectral Weyl formula on the fixed classical Gaussian Fock space. Hekkelman and McDonald, SIGMA 20 (2024), article 007, give an abstract density-of-states/Dixmier-trace framework, which may be applicable to some diagonal weighted operators but does not itself identify the pointwise rank-ordered coefficient for these recurrence derivatives. This result uses an explicit, independently proved finite-frequency counting principle for that coefficient.

## Limitations

The theorem requires finitely many pairwise distinct nonzero Binet roots, finite nonzero amplitudes, and the Ward normalization. The singular-value statement at the critical radius is an asymptotic, not an exact finite-index singular-value formula or a second-order remainder. The phase-independent constant does not assert monomial-index pointwise convergence, which can fail even for roots of unity. A broader published abstract rearrangement theorem could encompass the counting lemma after reduction; historical priority of such a formulation has not been exhaustively excluded. All scientific assessment here is limited to self-review; no independent audit or validation has been performed.

## References

1. R. Orozco López, *The U-Derivative Associated with Linear Recurrence Sequences*, arXiv:2610.20593v1, posted 2026-10-14. https://arxiv.org/html/2610.20593v1
2. N. Alpay, P. Cerejeiras, and U. Kähler, *Generalized Fock-space and fractional derivatives: Uniqueness of Sampling and Interpolation Sets*, arXiv:2112.07883. https://arxiv.org/html/2112.07883v4
3. E. Hekkelman and E. McDonald, *A General Dixmier Trace Formula for the Density of States on Open Manifolds*, SIGMA 20 (2024), 007. https://sigma-journal.com/2024/007/
