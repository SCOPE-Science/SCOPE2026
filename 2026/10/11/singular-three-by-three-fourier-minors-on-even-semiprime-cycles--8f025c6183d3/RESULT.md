# Singular three-by-three Fourier minors on even semiprime cycles

## Finding
For every odd prime \(p\), let \(G=\mathbb Z_2\times\mathbb Z_p\), let \(\zeta=e^{2\pi i/p}\), and let \(\mathcal F\) be the \(2p\)-by-\(2p\) character matrix
\[
\mathcal F_{(x,j),(\alpha,k)}=(-1)^{x\alpha}\zeta^{jk}
\qquad ((x,j),(\alpha,k)\in G).
\]
For a three-point set \(S\subseteq G\), call \(S\) **parity-pure** if the first coordinate is constant on \(S\), and **prime-colliding** if its three second coordinates are not all distinct.

**Classification.** For *all* three-point row and column sets \(I,J\subseteq G\), the matrix \(\mathcal F[I,J]\) is singular if and only if
\[
(I\text{ is parity-pure and }J\text{ is prime-colliding})
\quad\text{or}\quad
(J\text{ is parity-pure and }I\text{ is prime-colliding}).
\]
Every such singular minor has rank exactly two. The number of ordered pairs \((I,J)\) giving singular minors, with each three-point set unordered, is
\[
\boxed{8p(p-1)\binom p3
=\frac43p^2(p-1)^2(p-2).}
\]
There are \(\binom{2p}{3}^2\) pairs in total.

**Support consequences (of the same classification).** If a function on \(G\) has precisely three nonzero Fourier coefficients, then its number of zeros is in \(\{0,1,2,4\}\), and each count occurs for every odd prime \(p\). In particular, three zeros are impossible. Furthermore, writing
\[
\Theta^{\mathrm{ex}}_{2p}(k)
=\min\{|\operatorname{supp}\widehat f|:
|\operatorname{supp}f|=k\},
\]
for every prime \(p\ge5\) one has the sharp exact-support value
\[
\boxed{\Theta^{\mathrm{ex}}_{2p}(2p-3)=4.}
\]
The last statement concerns **exact** support; it is not the at-most-support uncertainty invariant.

## Assumptions and scope
All matrices, linear dependencies, coefficients, and ranks are over \(\mathbb C\). A nonzero Fourier coefficient means exactly nonzero, without equal-modulus or real-valued restrictions. The Fourier transform is the unnormalized character sum, and its sign convention does not affect support cardinalities. The group \(G\) is canonically isomorphic to \(\mathbb Z_{2p}\). The theorem includes \(p=3\) for the minor classification and zero-count spectrum, but the last exact-support formula is asserted only for \(p\ge5\).

## Proof
**1. Nonsingularity in the mixed/mixed case.** Maria Loukaki's Theorem A for order \(2p\) states that a square submatrix of its Fourier matrix is nonsingular whenever its row and column sets have identical counts in the two \(\mathbb Z_2\) fibers. Under the character indexing above this assertion applies unchanged, up to invertible index permutations and multiplying rows or columns by nonzero numbers. If three-point \(I\) and \(J\) both meet both parity fibers, each has a \((2,1)\) or \((1,2)\) fiber count. If their counts match, invoke Theorem A directly. Otherwise replace every \((\alpha,k)\in J\) by \((\alpha+1,k)\). This operation interchanges the counts; it also multiplies row \((x,j)\) by \((-1)^x\), so it preserves the singularity of the minor. Thus *every* mixed/mixed minor is nonsingular.

**2. Any pure row or column triple.** Suppose \(I\) is parity-pure: its elements have distinct prime coordinates \(j_1,j_2,j_3\). On these rows the entries are, for each column \((\alpha,k)\), a fixed nonzero sign times \(\zeta^{j_i k}\). If all three prime coordinates of \(J\) are distinct, this is a three-by-three minor of the prime-order Fourier matrix, multiplied by invertible diagonal signs. It is nonsingular by Chebotarev's theorem on prime Fourier minors. If two prime coordinates of \(J\) coincide, because the points of \(J\) are distinct, precisely two columns have the same \(k\) but opposite parity \(\alpha\). Their restrictions to \(I\) are proportional, so the determinant is zero. The remaining column has a different \(k\); the two-column submatrix formed by it and one colliding column has rank two, because any two distinct prime rows give a nonsingular prime-order two-by-two Fourier minor. Hence the entire three-by-three minor has rank exactly two. Transposing gives the same statement when \(J\) is parity-pure. A parity-pure triple cannot itself be prime-colliding, so the two singularity alternatives are disjoint. This proves the classification.

**3. Exact counting.** There are exactly \(A=2\binom p3\) parity-pure three-point sets. A prime-colliding three-point set must contain both \((0,k)\) and \((1,k)\) for one uniquely determined \(k\in\mathbb Z_p\), plus one point \((\alpha,\ell)\) with \(\ell\ne k\). There are \(B=2p(p-1)\) such sets. Because pure and colliding are disjoint, the number of singular ordered pairs is \(2AB=8p(p-1)\binom p3\). Each has nullity one by Step 2.

**4. Exactly three Fourier coefficients.** Write the inverse Fourier synthesis as \(H(t)=\sum_{\chi\in J}c_\chi\chi(t)\), where \(|J|=3\) and each \(c_\chi\ne0\). If \(H\) vanished at three distinct points \(I\), then \(\mathcal F[I,J]\) would be singular with a kernel vector whose three coordinates are nonzero. When \(J\) is mixed, the classification forces \(I\) to be parity-pure and \(J\) to be prime-colliding; its one-dimensional right kernel is then supported on the *colliding pair*, contradicting the three nonzero coefficients. Therefore mixed-support \(J\) allows at most two zero points. When \(J\) is parity-pure, \(H\) differs only by a constant sign between the two parity fibers, and the corresponding three-term polynomial on \(p\)-th roots has at most two zeros by Chebotarev. Consequently its zero count is \(0\), \(2\), or \(4\). In particular, exactly three zeros never occur, although four zeros can occur and contain many three-point subsets.

All four stated zero counts are realized: generic nonzero coefficients have no zero; generic nonzero coefficients on one evaluation hyperplane have exactly one zero; for \(J=\{(0,0),(0,1),(1,2)\}\), imposing zeros at \((0,0)\) and \((0,1)\) produces a one-dimensional coefficient kernel with every coordinate nonzero (prime-order two-by-two minors), and no third zero is possible; finally \(J=\{(0,0),(0,1),(0,2)\}\) with coefficients of \((z-1)(z-\zeta)\) has two zeros in each parity fiber, giving four. For the generic arguments, the finitely many coordinate and evaluation hyperplanes are proper and cannot cover a complex affine hyperplane; the chosen three characters generate the dual group, so distinct evaluation rows do not define proportional linear functionals.

**5. The high-support uncertainty gap.** Suppose \(p\ge5\) and \(|\operatorname{supp}f|=2p-3\). Thus \(f\) has exactly three zeros. If \(\widehat f\) had one nonzero coordinate, \(f\) would have no zeros. With two Fourier coordinates, any nonempty zero set of \(f\) has cardinality \(\gcd(d,2p)\), where \(d\not\equiv0\pmod{2p}\) is the difference of their frequencies; this is one of \(1,2,p\), not three. With exactly three Fourier coordinates, Step 4 excludes three zeros. Therefore \(|\operatorname{supp}\widehat f|\ge4\). Conversely, take a primitive \(2p\)-th root \(\omega\) and the coefficient polynomial
\[
P(z)=(z-1)(z-\omega)(z-\omega^2).
\]
It has precisely three roots among the \(2p\)-th roots of unity and precisely four nonzero coefficients: both interior coefficients contain \(1+\omega+\omega^2\ne0\) because \(2p>3\). Consequently the cyclic function with those four Fourier coefficients has exactly \(2p-3\) nonzero values. This proves the sharp formula.

## Verification
The companion standard-library program `verify_minors.py` represents each minor determinant as an exact integer polynomial in a primitive \(p\)-th root, reduced modulo \(\Phi_p(X)=1+\cdots+X^{p-1}\). It enumerates every three-by-three minor and checks the classification and total counts for \(p=3,5,7\): respectively \(48\) out of \(400\), \(1600\) out of \(14400\), and \(11760\) out of \(132496\). These are exhaustive **finite** checks, not proofs for all primes. The universal conclusion follows from the two nonvanishing theorems and the case analysis above.

## Relationship to prior work
Loukaki's Theorem A gives a powerful *sufficient* fiber-matching criterion for nonsingularity of Fourier minors of order \(2p\), rather than an if-and-only-if classification of three-by-three defects. The present argument invokes that theorem and prime-order Chebotarev nonsingularity as named published inputs, then determines every exceptional rank-two configuration and its multiplicity. Bonami and Ghobber study equality in the conventional at-most-support uncertainty problem for products of primes; their invariant does not distinguish exact three-zero gaps. Krahmer, Pfander, and Rashkov include a finite order-six Fourier minor census (the \(p=3\) case), consistent with the formula; that special numerical case is not asserted to be new. Caragea and Lee study principal Fourier minors, all nonsingular for the square-free orders here, rather than the nonprincipal defects classified above.

## Limitations
The work makes no assertion for minors larger than three, for repeated prime factors, or for positive-characteristic Fourier matrices. The strongest nonvanishing inputs are previously published; the contribution is their exact three-by-three structural classification, count, and support-gap consequences. An older implicit equivalent calculation, particularly in coding-theory or sparse interpolation literature, remains possible; external independent verification of originality and proof has not been performed.

## References
1. M. Loukaki, *Chebotarev's theorem for cyclic groups of order pq and an uncertainty principle*, Bull. Lond. Math. Soc. (2025), DOI:10.1112/blms.70192; first posted arXiv:2412.08600v1, 2024-12-11.
2. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060.
3. F. Krahmer, G. E. Pfander and P. Rashkov, *Uncertainty in time-frequency representations on finite abelian groups and applications*, Appl. Comput. Harmon. Anal. 25 (2008), 209–225.
4. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793.
5. P. E. Frenkel, *Simple proof of Chebotarev's theorem on roots of unity*, arXiv:math/0312398.
