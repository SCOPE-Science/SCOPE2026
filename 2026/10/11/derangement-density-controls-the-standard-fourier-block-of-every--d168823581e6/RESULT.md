# Derangement density controls the standard Fourier block of every doubly transitive action
## Finding
Let a finite group \(G\) act doubly transitively on a set \(\Omega\) of size \(n\ge 2\). Let \(\rho\) be the permutation character, so
\[
\rho=1_G+\chi,
\]
where \(\chi\) is the irreducible standard constituent of degree \(d=n-1\). Write \(D\) for the number of derangements of the action, namely elements of \(G\) fixing no point. Define the central Fourier projection onto the \(\chi\)-isotypic block by
\[
(P_\chi f)(x)=\frac{d}{|G|}\sum_{g\in G}\chi(g^{-1})f(xg).
\]
Then its two endpoint norms are exactly
\[
\boxed{\|P_\chi\|_{\ell^1\to\ell^1}=\|P_\chi\|_{\ell^\infty\to\ell^\infty}=\frac{2dD}{|G|}.}
\]
The complementary projection has the equally explicit norm
\[
\boxed{\|I-P_\chi\|_{\ell^1\to\ell^1}=\|I-P_\chi\|_{\ell^\infty\to\ell^\infty}=1+\frac{2d(D-d)}{|G|}.}
\]
Consequently
\[
\|P_\chi\|\ge \frac{2(n-1)}{n},\qquad \|I-P_\chi\|\ge 1,
\]
and equality in either inequality holds exactly when the action is sharply doubly transitive. In that equality case \(G\) is a Frobenius group of order \(n(n-1)\), and \(I-P_\chi\) is precisely averaging over its Frobenius kernel.

For the natural action of \(S_n\), if \(D_n\) is the derangement number, this becomes
\[
\|P_\chi\|=\frac{2(n-1)D_n}{n!},\qquad
\|I-P_\chi\|=1+\frac{2(n-1)(D_n-(n-1))}{n!},
\]
and therefore \(\|P_\chi\|/(n-1)\to 2/e\).

## Assumptions and scope
The spaces \(\ell^p(G)\) use counting measure. Replacing counting measure by normalized counting measure leaves the displayed operator norms unchanged because both domain and codomain norms are scaled by the same constant. The action need not be faithful. Double transitivity is used to make the nontrivial constituent of the permutation representation irreducible and to make the permutation rank equal to two.

A derangement is an element \(g\in G\) with no fixed point on \(\Omega\). A sharply doubly transitive action is one for which there is exactly one group element carrying any ordered pair of distinct points to any other ordered pair of distinct points.

## Proof
Let \(F(g)\) denote the number of fixed points of \(g\). The permutation character is \(\rho(g)=F(g)\). Because the action is transitive, the trivial representation occurs in the permutation representation exactly once. Because the action has permutation rank two, the character inner product satisfies \(\langle\rho,\rho\rangle=2\). Hence \(\rho=1_G+\chi\) with \(\chi\) irreducible and \(\chi(1)=n-1=d\). Pointwise,
\[
\chi(g)=F(g)-1.
\]

Schur orthogonality gives the central primitive idempotent kernel
\[
k_\chi(g)=\frac{d}{|G|}\chi(g^{-1}),
\]
so convolution by \(k_\chi\) is exactly \(P_\chi\). For convolution on a finite group, both endpoint operator norms equal the \(\ell^1\)-mass of the convolution kernel: the upper bound is the triangle inequality; equality for \(\ell^1\) is attained on a point mass, and equality for \(\ell^\infty\) is attained by choosing phases that match one row of the convolution matrix. Thus
\[
\|P_\chi\|=\frac{d}{|G|}\sum_{g\in G}|\chi(g)|.
\]

Since \(\chi\) is nontrivial, \(\sum_g\chi(g)=0\). The integer \(\chi(g)=F(g)-1\) is negative exactly when \(F(g)=0\), and there it equals \(-1\). Therefore the total negative mass is exactly \(D\), the positive mass is also \(D\), and
\[
\sum_{g\in G}|\chi(g)|=2D.
\]
This proves the first boxed identity.

For the complement, its convolution kernel is \(\delta_e-k_\chi\). Double transitivity implies \(|G|\ge n(n-1)=n d>d^2\), so its coefficient at the identity is positive. Since \(\chi(e)=d\),
\[
\begin{aligned}
\|I-P_\chi\|
&=1-\frac{d^2}{|G|}+\frac{d}{|G|}\sum_{g\ne e}|\chi(g)|\\
&=1-\frac{d^2}{|G|}+\frac{d}{|G|}(2D-d)\\
&=1+\frac{2d(D-d)}{|G|}.
\end{aligned}
\]

Cameron and Cohen proved that a transitive permutation group of degree \(n\) and permutation rank \(r\) has at least \((r-1)|G|/n\) derangements, with equality exactly in the corresponding Frobenius equality case. Here \(r=2\), hence \(D\ge |G|/n\). Together with \(|G|\ge n(n-1)\), this gives \(D\ge d\), the two lower bounds above, and the equality classification. If equality holds, then \(|G|=n(n-1)\), the action is Frobenius and doubly transitive, hence sharply doubly transitive. Its Frobenius kernel \(K\) has order \(n\); its nonidentity elements are exactly the derangements. In this case the kernel of \(I-P_\chi\) is \(1/n\) on \(K\) and zero off \(K\), so \(I-P_\chi\) is averaging over \(K\).

For \(S_n\), the standard character satisfies the same fixed-point formula and \(D=D_n\). The classical inclusion-exclusion identity
\[
\frac{D_n}{n!}=\sum_{j=0}^{n}\frac{(-1)^j}{j!}
\]
gives the displayed formulas and the limit \(2/e\).

## Verification
The proof is exact and does not depend on finite enumeration. The accompanying `verify.py` independently enumerates \(S_n\) for \(2\le n\le 8\), checks \(\sum_g|\chi(g)|=2D_n\), and verifies both endpoint formulas as exact rational identities. It also checks the sharply doubly transitive affine groups \(\operatorname{AGL}(1,p)\) for \(p\in\{3,5,7,11\}\), including the statement that the complementary kernel is uniform on the translation subgroup and zero elsewhere. Its terminal line is

`VERIFY_OK symmetric_n=2..8 affine_primes=3,5,7,11`

These finite checks are corroborative only; the universal statement is proved above.

## Relationship to prior work
Cameron and Cohen proved the sharp lower bound for the number of fixed-point-free elements in a transitive permutation group in terms of permutation rank, including the Frobenius equality case. Their argument is phrased in the fixed-point distribution and does not formulate endpoint norms of central Fourier projections.

Renteln's treatment of the derangement graph records, for \(S_n\), that the standard character is the number of fixed points minus one and uses its sum over the derangements to compute a Cayley-graph eigenvalue. That is a signed sum over one conjugacy-invariant subset, rather than the full absolute character mass that controls the endpoint Fourier projection norm here.

Alaghmandan and Spronk develop the central Fourier algebra of a compact group, including the character basis and Schur-orthogonality framework for central harmonic analysis. Their paper supplies the natural harmonic-analytic setting and lists primary MSC 43A30 and 43A77, but the result here concerns the endpoint norm of one central isotypic projection for a finite doubly transitive action and the exact contractivity boundary of its complement.

## Limitations
The theorem is restricted to the standard constituent coming from a doubly transitive finite permutation action. For higher-rank transitive actions the nontrivial permutation character need not be irreducible, so the same fixed-point identity does not isolate one Fourier block. No claim is made here about intermediate \(\ell^p\) norms, about arbitrary irreducible characters, or about infinite groups.

The originality comparison cannot exclude an equivalent formulation hidden in older compact-group Lebesgue-constant or finite-group idempotent literature under different terminology. The inspected close primary sources are listed below, and the exact formulas and the sharply doubly transitive contractivity characterization were not found there.

## References
1. P. J. Cameron and A. M. Cohen, *On the number of fixed point free elements in a permutation group*, Discrete Mathematics 106/107 (1992), 135--138, DOI:10.1016/0012-365X(92)90540-V.
2. P. Renteln, *On the Spectrum of the Derangement Graph*, Electronic Journal of Combinatorics 14 (2007), R82, DOI:10.37236/1000.
3. M. Alaghmandan and N. Spronk, *Amenability properties of the central Fourier algebra of a compact group*, arXiv:1407.6783.
