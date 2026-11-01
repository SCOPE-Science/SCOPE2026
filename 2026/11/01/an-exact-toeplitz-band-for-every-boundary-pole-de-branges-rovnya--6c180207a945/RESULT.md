# An exact Toeplitz band for every boundary-pole de Branges–Rovnyak Gram matrix

## Finding

Let \(m\geq1\), let \(Q\) be a complex polynomial of degree exactly \(m\) with all zeros on the unit circle, and let \(P\) be any complex polynomial of degree at most \(m\). Put \(\phi=P/Q\). Form the de Branges–Rovnyak space \(\mathcal H(b)\) corresponding to the non-extreme Pythagorean pair \(\phi=b/a\). For a polynomial \(R\) of degree at most \(m\), write its degree-\(m\) reversal as
\[
R^{\#}(z)=z^m\overline{R(1/\overline z)}.
\]
There is a unique unimodular constant \(\kappa\) such that \(Q^{\#}=\kappa Q\). Define the explicit polynomial
\[
W(z)=Q(z)^2+\kappa^{-1}P(z)P^{\#}(z)
   =\sum_{r=0}^{2m}w_rz^r.
\]
For every integer \(N\geq2m\), let \(M_N=(\langle z^j,z^k\rangle_{\mathcal H(b)})_{0\leq j,k\leq N}\), with inner product linear in its first argument, and let \(B_N\) have ones immediately above its diagonal and zeros elsewhere. Then
\[
\bigl(Q(B_N)^2M_N\bigr)_{jk}=
\begin{cases}
w_{k-j},&0\leq j\leq N-2m,\quad 0\leq k-j\leq2m,\\
0,&0\leq j\leq N-2m,\quad\text{otherwise}.
\end{cases}
\]
Consequently the **entire** matrix \(Q(B_N)^2M_N\) equals the upper triangular Toeplitz band \(T_N(W)\), with \((T_N(W))_{jk}=w_{k-j}\) for \(0\leq k-j\leq2m\) and zero elsewhere, plus a matrix supported in the last \(2m\) rows and therefore of rank at most \(2m\). This holds for arbitrary repeated or distinct boundary poles and arbitrary complex coefficients; every interior band coefficient is constant, not merely polynomial in the row number.

## Assumptions and scope

The unit circle is \(\mathbb T=\{z:|z|=1\}\); the disk is \(\mathbb D=\{z:|z|<1\}\). Roots of \(Q\) lie on \(\mathbb T\), so \(Q\) has no zero in \(\mathbb D\), and the rational analytic function \(\phi=P/Q\) lies in the Smirnov class. A rational Smirnov function determines a unique non-extreme Pythagorean pair \((b,a)\), with \(b/a=\phi\), \(a\) outer and \(a(0)>0\); when \(P=0\), take \(b=0,a=1\). The inner product in \(\mathcal H(b)\) is normalized by the Hardy norm formula
\[
\langle f,g\rangle_{\mathcal H(b)}=\langle f,g\rangle_{H^2}
 +\langle T_{\overline\phi}f,T_{\overline\phi}g\rangle_{H^2}
\]
for polynomials, with \(\langle z^j,z^k\rangle_{H^2}=\delta_{jk}\). Here \(T_{\overline\phi}\) denotes the adjoint of the densely defined multiplication operator \(T_\phi\) on \(H^2\). No noncancellation or normalization condition on the coefficients of \(P\) or \(Q\) is imposed. Indices start at zero, and \(N\geq2m\) avoids a vacuous interior band.

## Proof

**Reversal.** Since all roots of \(Q\) lie on \(\mathbb T\), reversing and conjugating its coefficients preserves its multiset of zeros. Thus \(Q^{\#}=\kappa Q\) with \(|\kappa|=1\). On \(\mathbb T\), for \(R=P,Q\), the identity \(\overline{R(z)}=z^{-m}R^{\#}(z)\) holds. Therefore, away from the finitely many zeros of \(Q\),
\[
\overline{\phi(z)}\,Q(z)^2
 =\frac{P^{\#}(z)}{Q^{\#}(z)}Q(z)^2
 =\kappa^{-1}Q(z)P^{\#}(z).
\]
The right-hand side is a polynomial, so the identity extends in the boundary \(L^2\) sense without a singularity.

**Toeplitz cancellation.** Fix \(j\geq0\) and set \(F_j(z)=z^jQ(z)^2\) and \(U_j(z)=\kappa^{-1}z^jQ(z)P^{\#}(z)\). The preceding boundary identity shows that the polynomial \(F_j\) belongs to the domain of \(T_{\overline\phi}\) and that
\[
T_{\overline\phi}F_j=U_j.
\]
Moreover \(U_j\) belongs to the domain of multiplication by \(\phi\), because
\[
T_\phi U_j=\kappa^{-1}z^jP(z)P^{\#}(z)
\]
is a polynomial. Thus, for every integer \(k\geq0\), adjointness and the norm identity yield
\[
\begin{aligned}
\langle F_j,z^k\rangle_{\mathcal H(b)}
 &=\langle F_j,z^k\rangle_{H^2}
   +\langle U_j,T_{\overline\phi}z^k\rangle_{H^2}\\
 &=\langle z^jQ^2,z^k\rangle_{H^2}
   +\langle T_\phi U_j,z^k\rangle_{H^2}\\
 &=\langle z^jW,z^k\rangle_{H^2}
 =\begin{cases}w_{k-j},&0\leq k-j\leq2m,\\0,&\text{otherwise}.\end{cases}
\end{aligned}
\]
The last step uses the Hardy monomials as an orthonormal basis and the convention that the inner product is linear in its first argument.

**Finite Gram identity.** Write \(Q(z)^2=\sum_{r=0}^{2m}d_rz^r\). For \(0\leq j\leq N-2m\), no truncation occurs in row \(j\) when multiplying by \(Q(B_N)^2\), and hence
\[
\begin{aligned}
\bigl(Q(B_N)^2M_N\bigr)_{jk}
 &=\sum_{r=0}^{2m}d_r\langle z^{j+r},z^k\rangle_{\mathcal H(b)}\\
 &=\langle z^jQ^2,z^k\rangle_{\mathcal H(b)}
 =w_{k-j}
\end{aligned}
\]
when \(k-j\in\{0,\dots,2m\}\), and zero otherwise. This proves the stated band. Subtracting the full upper triangular Toeplitz matrix leaves a matrix whose first \(N-2m+1\) rows vanish, so the remaining \(2m\) rows give the asserted rank bound. All quantified statements follow directly from the polynomial cancellation, without a limiting or numerical argument.

## Verification

The accompanying standalone `CHECK.py` computes the Taylor coefficients of \(\phi\) by the exact recurrence \(Q\phi=P\), forms monomial Gram matrices from the exact coefficient identity, and compares every untruncated row of \(Q(B_N)^2M_N\) with the coefficients of \(W\). It tests six Gaussian-integer examples, including single poles, distinct poles, mixed multiplicities and nonreal polynomial coefficients. All generated values stay in the exactly represented Gaussian integers. These finite checks test algebra and indexing; the preceding proof establishes the identity for every admissible polynomial and every degree.

For an especially concrete two-pole example take \(Q(z)=1-z^2\), \(P(z)=2+z-z^2\), and \(m=2\). Then \(Q^{\#}=-Q\), \(\kappa=-1\) and \(W=Q^2-PP^{\#}\). The formula determines all five interior diagonals without computing any individual orthogonal polynomial.

## Relationship to prior work

Dellepiane and Seco [1], in Sections 4.2–4.3 of their March 2026 preprint, identify finite-band-plus-boundary-row structure for a second-order boundary pole and suggest an all-order version when \(\phi=P/(1-z)^m\). The result above proves an exact formula for every positive order and extends the denominator to **arbitrary finite multisets** of boundary poles. It yields constant Toeplitz diagonals with an explicit polynomial symbol and a \(2m\)-row residual; the source neither states nor proves this all-denominator formula.

Hartmann and Lamberti [2] describe the decomposition of rational non-extreme de Branges–Rovnyak spaces with several boundary zeros of the Pythagorean mate and establish interpolation theorems. Their decomposition does not give the exact original-norm Gram identity or the Toeplitz symbol derived here. Łanucha, Michalska, Nowak and Sołtysiak [3] investigate single-boundary-point higher-order local Dirichlet norms and shift-isometry characterizations, not the arbitrary-pole finite-Gram factorization. The starting adjoint-Toeplitz norm formula is classical; it is an ingredient rather than the new claim.

## Limitations

The theorem describes a transformed **finite Gram matrix**, not an explicit formula for every orthonormal polynomial and not a statement that the original Gram matrix itself is banded. The residual has at most \(2m\) nonzero rows, but no general formula for its rank or inverse is claimed. The assumptions require the denominator's zeros to lie on \(\mathbb T\); arbitrary rational Smirnov denominators with roots off \(\mathbb T\) are not covered by the same reversal identity. No numerical test is treated as a proof, and full uniqueness in unindexed literature is not asserted.

## References

[1] Eugenio Dellepiane and Daniel Seco, *Orthogonal polynomials in de Branges–Rovnyak spaces*, arXiv:2603.03093v1, publicly posted 2026-03-03. https://arxiv.org/html/2603.03093v1 (especially §§2, 4.2–4.3).

[2] Andreas Hartmann and Giuseppe Lamberti, *Interpolation and random interpolation in de Branges–Rovnyak spaces*, Journal of the London Mathematical Society 112 (2025), e70323, first published 2025-10-09. https://doi.org/10.1112/jlms.70323 (especially Theorem 1.1 and §2).

[3] Bartosz Łanucha, Małgorzata Michalska, Maria Nowak and Andrzej Sołtysiak, *De Branges–Rovnyak spaces and local Dirichlet spaces of higher order*, arXiv:2306.07146 (2023). https://arxiv.org/abs/2306.07146.
