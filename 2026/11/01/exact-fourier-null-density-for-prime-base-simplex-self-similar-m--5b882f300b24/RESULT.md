# Exact Fourier-null density for prime-base simplex self-similar measures

## Finding
For any prime \(p\ge2\), put \(d=p-1\) and let \(\mu_p\) be the uniform affine self-similar probability measure defined below. The entire set of nonzero **integer** frequencies at which \(\widehat\mu_p\) vanishes is given by a single-permutation rule at the first nonzero \(p\)-adic digit layer: for \(m\in\mathbb Z^d\setminus\{0\}\),
\[
\widehat\mu_p(m)=0\quad\Longleftrightarrow\quad
\exists v\ge0:\ \{m_1/p^v\bmod p,\ldots,m_d/p^v\bmod p\}=\{1,\ldots,p-1\}.
\]
The displayed condition includes the requirement that every coordinate is divisible by \(p^v\), so each quotient is an integer. The exponent \(v\) is automatically unique.

For every integer \(L\ge1\), the exact number of residue classes modulo \(p^L\) whose first \(L\) Fourier-mask factors include a zero is
\[
N_{p,L}=(p-1)!\,\frac{p^{L(p-1)}-1}{p^{p-1}-1}.
\]
Consequently the complete integer-frequency zero set \(\mathcal Z_p\) has the natural box density
\[
\lim_{N\to\infty}\frac{\#(\mathcal Z_p\cap[-N,N]^d)}{(2N+1)^d}
=\frac{(p-1)!}{p^{p-1}-1}.
\]
For instance the density is \(1/4\) for \(p=3\), and \(1/26\) for \(p=5\). On \(L^2(\mathbb T^d)\), convolution by the torus pushforward of \(\mu_p\) has kernel exactly the closed span of the Fourier characters indexed by \(\mathcal Z_p\), so the formula measures the frequency density of its nullspace.

## Assumptions and scope
Use the standard coordinate vectors \(e_1,\ldots,e_d\in\mathbb R^d\). Independently choose \(U_j\) uniformly from \(\{0,e_1,\ldots,e_d\}\), and put \(\mu_p=\operatorname{Law}(\sum_{j\ge1}p^{-j}U_j)\). Normalize the Fourier transform by \(\widehat\mu_p(m)=\int e^{-2\pi i m\cdot x}\,d\mu_p(x)\). The prime \(p\) ranges over all rational primes including two; \(m\) ranges over integer lattice frequencies only; the counting statement concerns residue classes in \((\mathbb Z/p^L\mathbb Z)^d\); the density uses symmetric integer cubes. No assertion is made about nonintegral real frequencies.

## Proof
**Step 1: zero masks are necessary and sufficient.** Independence gives the absolutely convergent infinite product
\[
\widehat\mu_p(m)=\prod_{j=1}^{\infty}M_j(m),\qquad
M_j(m)=\frac{1+\sum_{i=1}^{d}\exp(-2\pi i m_i/p^j)}{p}.
\]
For fixed \(m\), \(\lvert1-M_j(m)\rvert\le(2\pi/p^j)\sum_i|m_i|/p\), so the series of departures from one converges. Thus, if none of its factors vanishes, the infinite product is nonzero. A Fourier zero therefore occurs at some finite level \(j\).

**Step 2: prime-power cyclotomic rigidity.** Put \(q=p^j\), \(s=p^{j-1}\), and let \(\zeta\) be a primitive \(q\)-th root of unity. The mask vanishes just when
\[
F(\zeta)=0,\qquad F(z)=1+\sum_{i=1}^{p-1}z^{m_i\bmod q}.
\]
Write the coefficient of \(z^a\) in \(F\), for \(0\le a<q\), as \(c_a\ge0\). Since the prime-power cyclotomic polynomial is \(\Phi_q(z)=1+z^s+\cdots+z^{(p-1)s}\), reduction modulo \(\Phi_q\) shows that \(F(\zeta)=0\) if and only if, for every \(0\le a<s\), the \(p\) coefficients
\(c_a,c_{a+s},\ldots,c_{a+(p-1)s}\) are equal. Indeed, the powers \(1,z,\ldots,z^{s-1}\) are a basis for the quotient of \(\mathbb Q[z]\) by \(\Phi_q\) over \(\mathbb Q(\zeta_p)\); equivalently, polynomial division by the monic \(\Phi_q\) yields this coefficient condition. As \(\sum_{a=0}^{q-1}c_a=p\), exactly one of these coefficient groups can be nonzero, and every coefficient in that group must equal one. Because \(F\) contains the constant term, the group must be \(a=0\). Therefore the nonconstant exponents modulo \(p^j\) are exactly \(s,2s,\ldots,(p-1)s\) in some order. This is equivalent to all coordinates being divisible by \(p^{j-1}\), with their quotients forming a permutation of \(1,\ldots,p-1\) modulo \(p\). The minimum coordinate valuation is exactly \(j-1\), so two different levels cannot vanish simultaneously. This proves the complete zero criterion.

**Step 3: finite-scale census.** Fix \(L\ge1\). For an allowed first nonzero digit layer at \(v\in\{0,\ldots,L-1\}\), there are precisely \((p-1)!\) assignments of the leading nonzero residues and \(p^{(L-v-1)d}\) arbitrary higher digits. The layers are pairwise disjoint. Hence
\[
N_{p,L}=(p-1)!\sum_{v=0}^{L-1}p^{(L-v-1)d}
=(p-1)!\frac{p^{Ld}-1}{p^d-1}.
\]

**Step 4: infinite density.** The periodic collection of classes counted in Step 3 has box density \(N_{p,L}/p^{Ld}\). Every additional zero at a later level has all coordinates divisible by \(p^L\), a set of box density \(p^{-Ld}\). Thus, writing \(\underline\delta\) and \(\overline\delta\) for lower and upper densities,
\[
\frac{N_{p,L}}{p^{Ld}}\le\underline\delta(\mathcal Z_p)
\le\overline\delta(\mathcal Z_p)\le\frac{N_{p,L}}{p^{Ld}}+p^{-Ld}.
\]
Letting \(L\to\infty\) proves the limit and its value. Finally, Fourier characters diagonalize torus convolution, with eigenvalues \(\widehat\mu_p(m)\); their zero eigenspace is the stated nullspace.

## Verification
The standalone standard-library checker `verify.py` tests prime-power cyclotomic divisibility using direct exact integer polynomial long division, independently of the digit-permutation predicate. It exhaustively checks all character residues for \((p,L)=(2,7),(3,4),(5,1)\) and the census at \((p,L)=(5,2)\), plus one thousand further deterministic prime-power cases. All checked instances agree with the exact counts and the theorem's criterion. The analytic proof, not these finite experiments, establishes the arbitrary-prime and infinite-scale assertions.

## Relationship to prior work
Lam and Leung (1995) establish foundational results on vanishing sums of roots of unity, including the prime-power cyclotomic structure used in Step 2. Dutkay and Jorgensen (2006a) give the general infinite Fourier-product formula and directly study these simplex digit systems; their Theorem 5.6 shows that the same prime-base example has a complete exponential spectrum generated by \((1,2,\ldots,d)\). Their 2006b paper develops related Fourier-spectral machinery. The present claim does **not** reassert spectrality or the existence of those orthogonal exponentials. Its object is the complete **integer-frequency Fourier-zero set**, the exact null-residue census at every scale, and the natural density of convolution-null modes. A preexisting exponential basis does not by itself determine the latter quantities. The classification and count are an explicit new combination of established mask and cyclotomic principles; no claim is made that those principles are new.

## Limitations
The statement concerns the canonical equal-weight simplex digits and the matching *prime* contraction base. It does not classify Fourier zeros at real nonintegral frequencies, composite bases, or arbitrary unequal digit weights. The frequency density is a natural density, not a claim about a unique sparsest complete orthogonal basis. The novelty assessment is bounded by the accessible primary literature and related searches; equivalently formulated density computations in historical literature remain possible. Independent audit has not been performed.

## References
- T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, first public preprint 1995-11-13, arXiv:math/9511209, https://arxiv.org/abs/math/9511209.
- D. E. Dutkay and P. E. T. Jorgensen, *Analysis of orthogonality and of orbits in affine iterated function systems*, first public preprint 2006-06-14, arXiv:math/0606349, especially equations (2.3)–(2.5), Section 5 and Theorem 5.6, https://arxiv.org/abs/math/0606349.
- D. E. Dutkay and P. E. T. Jorgensen, *Fourier frequencies in affine iterated function systems*, first public preprint 2006-04-25, arXiv:math/0604547, https://arxiv.org/abs/math/0604547.
