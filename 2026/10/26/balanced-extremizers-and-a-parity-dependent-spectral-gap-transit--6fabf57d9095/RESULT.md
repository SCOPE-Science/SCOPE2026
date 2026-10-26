# Balanced extremizers and a parity-dependent spectral-gap transition for holomorphic product caps

## Finding

Fix integers \(n\ge3\) and \(d\ge2\). On the complex unit sphere \(S^{2n-1}\subset\mathbb C^n\) with probability Haar surface measure \(\sigma\), let \(\mathcal H_d\) be the complex vector space of holomorphic homogeneous polynomials of degree exactly \(d\). For \(0<\tau<1/4\), define the product cap
\[
E_\tau=\{z\in S^{2n-1}:|z_1|^2|z_2|^2>\tau\}.
\]

**Theorem (sharp concentration, spectral gap, and critical edge).** The compression of multiplication by \(\mathbf1_{E_\tau}\) to \(\mathcal H_d\) is diagonal in the monomial basis, with the complete spectrum described below. Its largest eigenvalue \(\Lambda_{n,d}(\tau)\) is attained exactly on the *balanced* powers of the first two coordinates. If \(d=2r\), its one-dimensional top eigenspace is \(\operatorname{span}_{\mathbb C}\{z_1^rz_2^r\}\); if \(d=2r+1\), its two-dimensional top eigenspace is \(\operatorname{span}_{\mathbb C}\{z_1^rz_2^{r+1},z_1^{r+1}z_2^r\}\). No other nonzero polynomial attains the sharp concentration quotient.

Write \(\lambda_{a,b}=\lambda_{a,b}^{(n,d)}(\tau)\) for the explicitly defined eigenvalue below. Then
\[
\Lambda_{n,d}=\lambda_{\lfloor d/2\rfloor,\lceil d/2\rceil},\qquad
\Lambda_{n,d}^{(2)}=
\begin{cases}
\lambda_{r-1,r+1}, &d=2r,\\
\max\{\lambda_{r-1,r+2},\lambda_{r,r}\},&d=2r+1\ge3.
\end{cases}
\]
These are the largest and second-largest **distinct** eigenvalues and satisfy \(\Lambda_{n,d}>\Lambda_{n,d}^{(2)}>0\). The exact positive gap \(\Delta_{n,d}=\Lambda_{n,d}-\Lambda_{n,d}^{(2)}\) is optimal in the quantitative inequality
\[
\int_{E_\tau}|P|^2d\sigma\le\Lambda_{n,d}\|P\|_2^2-\Delta_{n,d}\|P-\Pi_{\rm top}P\|_2^2,
\qquad P\in\mathcal H_d,
\]
where \(\Pi_{\rm top}\) is the full-sphere orthogonal projection onto the stated top eigenspace. Equality holds precisely for sums of top-eigenspace and second-eigenspace components, including the zero polynomial.

For odd degrees, \(d=2r+1\ge3\), the identity of the second eigenspace genuinely changes as the threshold moves: \(\lambda_{r,r}>\lambda_{r-1,r+2}\) for all sufficiently small \(\tau>0\), whereas \(\lambda_{r-1,r+2}>\lambda_{r,r}\) for \(\tau\) sufficiently close to \(1/4\). Thus at least one intermediate threshold has a cross-branch equality. No uniqueness of this crossing is asserted. For even degrees, the second eigenspace always comes from the two unbalanced pure-two-coordinate monomials described above.

For every fixed \(n\ge3\) and \(c>0\), the sharp concentration has the universal edge limit
\[
\boxed{\lim_{d\to\infty}\Lambda_{n,d}(1/4-c/d)=\Pr\{\chi^2_{2n-3}<4c\}.}
\]
Here \(\chi^2_{2n-3}\) is chi-square with \(2n-3\) degrees of freedom; the threshold \(1/4-c/d\) is taken only for sufficiently large \(d\) so that it is positive.

## Assumptions and scope

The monomial \(z^\alpha=z_1^{\alpha_1}\cdots z_n^{\alpha_n}\) has degree \(|\alpha|=d\). If \(a=\alpha_1\), \(b=\alpha_2\), and \(s=a+b\), set \(\gamma=n+d-s-2\ge1\). The associated eigenvalue is the probability
\[
\lambda_{a,b}=\Pr\{XY>\tau\},\quad (X,Y,1-X-Y)\sim\operatorname{Dirichlet}(a+1,b+1,\gamma).
\]
Equivalently, with \(\mathrm B\) the beta function and \(I_x\) the regularized incomplete beta function, define
\[
q(v)=\frac{1-\sqrt{1-4\tau/v^2}}2,\qquad
\lambda_{a,b}=\frac1{\mathrm B(s+2,\gamma)}\int_{2\sqrt\tau}^{1}
 v^{s+1}(1-v)^{\gamma-1}
 \big[I_{1-q(v)}(a+1,b+1)-I_{q(v)}(a+1,b+1)\big]dv.
\]
The **entire** concentration spectrum is the multiset of these \(\lambda_{a,b}\) for \(a,b\ge0\), \(a+b\le d\), assigning each listed entry multiplicity \(\binom{d-a-b+n-3}{n-3}\). Coincident values from distinct pairs have combined multiplicity; this formula does not claim pairwise distinctness. In particular, the formula specifies all matrix eigenvalues and is numerically reproducible by one-dimensional beta integrals.

The region depends on the product of the two squared coordinate moduli, not on their union or intersection at a fixed individual-coordinate threshold. The assertion is for complex holomorphic homogeneous polynomials, not for arbitrary real or harmonic polynomials. All integrals over the sphere use probability surface measure, and all ratios are invariant under scaling of \(P\).

## Proof

**1. Spectrum and normalization.** The map \(z\mapsto(e^{i\theta_1}z_1,\ldots,e^{i\theta_n}z_n)\) preserves \(E_\tau\) and \(\sigma\). Independent phase integration makes distinct monomials orthogonal both on the full sphere and over \(E_\tau\). Under full-sphere measure, the squared coordinate moduli are \(\operatorname{Dirichlet}(1,\ldots,1)\), and weighting this law by \(|z^\alpha|^2\), then renormalizing by \(\|z^\alpha\|_2^2=\alpha!(n-1)!/(n+d-1)!\), gives \(\operatorname{Dirichlet}(\alpha_1+1,\ldots,\alpha_n+1)\). Aggregating the last \(n-2\) coordinates gives the three-shape law in the statement, and counting exponent allocations outside the first two coordinates gives the displayed multiplicity. If \(V=X+Y\), then \(V\sim\operatorname{Beta}(s+2,\gamma)\), while \(U=X/(X+Y)\sim\operatorname{Beta}(a+1,b+1)\) is independent of \(V\). The condition \(XY>\tau\) is \(V>2\sqrt\tau\) and \(q(V)<U<1-q(V)\), giving the integral.

**2. Strict improvement by transferring degree out of unused coordinates.** Suppose an exponent on a coordinate \(j\ge3\) is positive. Transfer one unit from that coordinate to coordinate 1, keeping the total degree fixed. In the corresponding Dirichlet laws, condition on the sum \(X_1+X_j\) and on every other coordinate. The conditional proportion assigned to coordinate 1 changes from \(\operatorname{Beta}(p,q)\) to \(\operatorname{Beta}(p+1,q-1)\), with \(p\ge1\) and \(q\ge2\). These beta densities have increasing likelihood ratio proportional to \(u/(1-u)\), so the latter variable strictly first-order stochastically dominates the former. Since the event \(X_1X_2>\tau\) increases in \(X_1\), its probability increases; strictness follows by restricting to a positive-measure set of conditional parameters where the event cuts through the interior of the admissible proportion interval (such a set exists for every \(0<\tau<1/4\)). The same argument works for transfer into coordinate 2. Iterating shows that maximal concentration requires that all \(d\) exponent units lie in the first two coordinates.

**3. Strict improvement by balancing the two distinguished exponents.** At fixed \(s=a+b\), the distribution of \(V\) is unchanged. For a given \(q\in(0,1/2)\), set \(H_a(q)=\Pr\{q<U<1-q\}\) for \(U\sim\operatorname{Beta}(a+1,s-a+1)\). Because the shapes are positive integers, with \(N=s+1\), the beta-binomial identity is
\[
H_a(q)=\Pr\{\operatorname{Bin}(N,1-q)\ge a+1\}-\Pr\{\operatorname{Bin}(N,q)\ge a+1\}.
\]
Consequently
\[
H_{a+1}(q)-H_a(q)=\binom N{a+1}
\big[q^{a+1}(1-q)^{N-a-1}-(1-q)^{a+1}q^{N-a-1}\big].
\]
The expression is positive, zero, or negative according as \(2(a+1)\) is less than, equal to, or greater than \(N\), because \(q/(1-q)<1\). After averaging with the positive beta density of \(V\), the same *strict* ordering holds for \(\lambda_{a,s-a}\). Thus the unique balancing point for even \(s\) and the two adjacent balancing points for odd \(s\) are precisely all maximizing pairs at that \(s\), while the next-best pairs at a fixed \(s\ge2\) are the immediately next most balanced. The strict transfer result of Step 2 then proves the top-eigenvalue and top-eigenspace classification.

**4. Second eigenvalue and sharp stability.** Let \(M_s\) be the largest eigenvalue among monomials whose first two exponents add to \(s\). For \(s<d\), transfer any available outside unit into the first two coordinates and then balance; by Steps 2–3, \(M_{s+1}>M_s\). Hence the largest eigenvalue with \(s<d\) occurs at \(s=d-1\), with balanced exponents. The best non-top eigenvalue with \(s=d\) occurs at the next most balanced pair. For \(d=2r\), transferring the single outside unit from \((a,b)=(r,r-1)\) into the first coordinate produces \((r+1,r-1)\), so this fixed-\(s=d\) runner-up strictly dominates \(M_{d-1}\). For \(d=2r+1\), the two remaining candidates are exactly \((r-1,r+2)\) with \(s=d\) and \((r,r)\) with \(s=d-1\); either can be larger. This proves the stated exact formula for \(\Lambda^{(2)}\). Diagonality gives the stability inequality coefficient by coefficient. A second-eigenvector attains equality at that coefficient, making the gap sharp, and spectral support characterizes all equality cases.

**5. The odd-degree second-eigenspace transition.** Fix \(d=2r+1\ge3\). For the \((r-1,r+2)\) candidate, the marginal squared modulus of its first (less highly weighted) coordinate has beta parameter \(r\), so \(\Pr\{XY\le\tau\}\ge\Pr\{X\le\tau\}=\Theta(\tau^r)\) as \(\tau\downarrow0\). For the competing \((r,r)\) candidate with one outside exponent, its joint Dirichlet density is bounded above by a constant times \(x^ry^r\) on the simplex (the residual shape is \(n-1\ge2\)). Splitting the integral at \(x=\tau\) and using \(y\le\tau/x\) gives \(\Pr\{XY\le\tau\}=O(\tau^{r+1}(1+|\log\tau|))\). Thus the balanced-with-one-outside branch is larger near zero.

For the opposite endpoint write \(\delta=1/4-\tau\downarrow0\). In \(V,U\) coordinates, the event \(V^2U(1-U)>1/4-\delta\) occupies \(1-V=O(\delta)\) and \(|U-1/2|=O(\sqrt\delta)\), and it contains a smaller product neighborhood of the same respective orders. The positive beta densities at \(U=1/2\) and \(V=1\) show that for a Dirichlet residual parameter \(\gamma\), the event probability is \(\Theta(\delta^{\gamma+1/2})\). The unbalanced fixed-\(s=d\) candidate has \(\gamma=n-2\), while the balanced-with-one-outside candidate has \(\gamma=n-1\). Therefore the former strictly dominates sufficiently close to \(1/4\). Continuity yields at least one interior crossing; no assertion about the number or uniqueness of crossings is needed or proved.

**6. Critical edge law.** For the balanced top monomial of degree \(d\), use independent unit-scale gamma variables \(G_1\sim\operatorname{Gamma}(a+1,1)\), \(G_2\sim\operatorname{Gamma}(b+1,1)\), \(G_3\sim\operatorname{Gamma}(n-2,1)\), with \(a=\lfloor d/2\rfloor\), \(b=\lceil d/2\rceil\). Setting \(T=G_1+G_2+G_3\), \(X=G_1/T\), \(Y=G_2/T\), \(V=X+Y\), the gamma central limit theorem and law of large numbers imply, jointly,
\[
d(1-V)\Rightarrow G_3,\qquad \sqrt d\,(X-Y)\Rightarrow Z,
\]
where \(Z\sim N(0,1)\) is independent of \(G_3\). Since \(XY=(V^2-(X-Y)^2)/4\), the continuous mapping theorem gives
\[
d(1/4-XY)\Rightarrow G_3/2+Z^2/4.
\]
The two independent terms are gamma variables with a common scale \(1/2\) and shapes \(n-2\) and \(1/2\); their sum is \(\chi^2_{2n-3}/4\). At any fixed positive \(c\), continuity of this law proves the claimed concentration limit.

## Verification

The standalone program `check.py` independently computes each tested eigenvalue by two different one-dimensional integrals: the conditional \((V,U)\) beta formula and a conditional \(Y\mid X\) beta formula. It checks the full finite-degree ordering, the even/odd runner-up formulas, both opposite small/large-threshold branches in odd degree, and convergence to the chi-square edge limit. It also checks the beta-binomial balancing step using exact rational arithmetic. Execute `python check.py` with Python 3, NumPy, and SciPy. The packaged `verification_output.txt` is the output of a run made from this source. The finite checks corroborate but do not replace Steps 1–6, which prove the stated all-integer and all-threshold theorem.

## Relationship to prior work

Bauer, Hagger, and Vasilevski (arXiv:1808.10372, first posted August 30, 2018) develop algebras of Toeplitz operators for product-type symbols on the complex ball, including monomial decompositions and symbol integral representations. Quiroga-Barranco (arXiv:2106.01980, first posted June 3, 2021) supplies broad invariant-symbol and monomial action formulas (Theorem 7.3 and Corollary 7.4). Such diagonalization and integral-formula principles are background here, not claimed as new. The claim is the strict degree-transfer and beta-binomial ordering on the **product-coordinate threshold set**, the exact second-eigenvalue parity dichotomy and branch switch, and the critical chi-square edge law. The two cited papers' inspected statements do not imply these order and edge assertions as stated; evaluating the generic integral formulas alone does not determine extremizers or spectral ordering.

## Limitations

This result concerns the boundary Hardy \(L^2\) norm of exact-degree holomorphic polynomials, not full weighted-Bergman-space Toeplitz norms or arbitrary finite-degree bands. It does not determine the **number or uniqueness** of odd-degree runner-up branch crossings; only their existence. The numerical checker tests finite examples and is not a formal infinite proof. Literature novelty is a best-knowledge assessment; older or unindexed results on Dirichlet product tails or Toeplitz-symbol orderings may be equivalent. No independent mathematical audit has been performed.

## References

1. W. Bauer, R. Hagger, N. Vasilevski, *Algebras of Toeplitz operators on the n-dimensional unit ball*, arXiv:1808.10372 (initial submission August 30, 2018), https://arxiv.org/abs/1808.10372.
2. R. Quiroga-Barranco, *Toeplitz operators, T-m-invariance and quasi-homogeneous symbols*, arXiv:2106.01980 (initial submission June 3, 2021), https://arxiv.org/abs/2106.01980.
3. Standard gamma–Dirichlet aggregation, beta-binomial identities, and the gamma central limit theorem are used as classical tools; no novel attribution is claimed for them.
