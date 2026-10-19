# First four exact rank-weighted Fourier uncertainty levels on prime dihedral groups

## Finding
Let \(p\ge5\) be an odd prime and let \(G=D_{2p}=\langle r,s:r^p=s^2=e,\ srs=r^{-1}\rangle\). For a complex function \(f:G\to\mathbb C\), set
\[
\sigma(f)=\sum_{\pi\in\widehat G}(\dim\pi)\,\operatorname{rank}\left(\sum_{g\in G}f(g)\pi(g)\right),\qquad
\Theta_G(k)=\min_{|\operatorname{supp}f|=k}\sigma(f).
\]
Then the first four **exact-support** levels are
\[
\boxed{(\Theta_G(1),\Theta_G(2),\Theta_G(3),\Theta_G(4))
=(2p,\ p,\ 2p-4,\ p-1).}
\]
In particular, increasing the allowed number of **nonzero** taps from two to three raises the minimum rank by \(p-4\), while a fourth tap lowers it by \(p-3\). The rank equals the dimension of the image of the corresponding left-convolution operator on \(\mathbb C[G]\).

## Assumptions and scope
All supports have **exactly** the prescribed cardinality; all coefficients on a support are arbitrary nonzero complex numbers. The convention for the noncommutative Fourier transform uses \(\pi(g)\) rather than \(\pi(g)^*\); taking adjoints and inversions of group arguments does not change the rank-weighted invariant or the minimum. No positivity, equal-weight, inversion symmetry, or reality assumption is imposed. The assertion covers every prime \(p\ge5\), not composite rotation orders or larger support sizes. The two one-dimensional irreducibles and the \((p-1)/2\) two-dimensional irreducibles are all counted with their dimensions.

## Proof
**The representation blocks.** Write uniquely
\[
f=\sum_{a\in\mathbb Z_p}u_a\,\delta_{r^a}+
\sum_{a\in\mathbb Z_p}v_a\,\delta_{r^as},\quad
U(z)=\sum_a u_az^a,\quad V(z)=\sum_a v_az^a.
\]
Let \(\zeta=e^{2\pi i/p}\). The two linear characters yield \(U(1)+V(1)\) and \(U(1)-V(1)\). For \(1\le j\le(p-1)/2\), choose
\[
\pi_j(r)=\begin{pmatrix}\zeta^j&0\\0&\zeta^{-j}\end{pmatrix},\qquad
\pi_j(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The associated Fourier block is
\[
M_j=\begin{pmatrix}U(\zeta^j)&V(\zeta^j)\\ V(\zeta^{-j})&U(\zeta^{-j})\end{pmatrix},
\quad\det M_j=D(\zeta^j),\quad
D(z)=U(z)U(z^{-1})-V(z)V(z^{-1}).
\]
Thus \(D(z^{-1})=D(z)\), and each rank-one \(M_j\) reduces \(\sigma(f)\) by exactly \(2\) compared with the full value \(2p\). A vanishing linear block reduces it by \(1\). All calculations with \(D\) are in the cyclic group algebra \(\mathbb C[z,z^{-1}]/(z^p-1)\).

**A prime-order zero-count lemma.** Chebotarev's nonsingularity theorem for every square minor of the prime Fourier matrix, equivalently the sharp prime uncertainty principle, implies that a nonzero Laurent polynomial with at most \(t\) occupied exponents modulo \(p\) can vanish at at most \(t-1\) of the \(p\)-th roots of unity. This applies to arbitrary complex coefficients; it is not an argument from integrality of coefficients. In particular, a two-term polynomial cannot vanish at both \(\zeta^j\) and \(\zeta^{-j}\) for nonzero \(j\).

**One and two taps.** One group element produces invertible matrices in every Fourier block, so \(\Theta_G(1)=2p\). For two taps, translation reduces to \(f=a\delta_e+b\delta_h\), with \(h\ne e\) of order \(2\) or \(p\). In the left regular representation, the eigenvalues of left translation by \(h\) are the roots of unity of order \(\operatorname{ord}(h)\), each of multiplicity \(2p/\operatorname{ord}(h)\). Thus the nullity of \(aI+bL_h\) is either zero or exactly \(2p/\operatorname{ord}(h)\). The maximal nullity is \(p\), attained by \(\delta_e-\delta_s\), proving \(\Theta_G(2)=p\).

**Three taps.** When all three taps lie in one coset of \(\langle r\rangle\), left translation reduces to \(V=0\). The Fourier support is then two copies, including both linear characters, of the ordinary \(p\)-point Fourier support of \(U\). The prime uncertainty lemma gives \(\sigma(f)\ge2(p-2)=2p-4\).

For a mixed coset distribution \((2,1)\) or \((1,2)\), the polynomial \(D\) has at most three monomials, with exponents \(0,\pm d\), where \(d\ne0\). The coefficient at \(\pm d\) is the product of the two nonzero coefficients in the two-tap coset; hence \(D\) is not the zero function on \(\mathbb Z_p\). The prime lemma gives at most two roots among the \(p\)-th roots of unity. The singleton coset ensures each \(M_j\ne0\), so its nullity is at most one. By \(D(\zeta^j)=D(\zeta^{-j})\), the nontrivial roots occur in pairs and contribute at most \(2\) to total regular nullity. If either linear character vanishes, then \(D(1)=0\), so a nontrivial root pair is impossible; the singleton also prevents both linear characters from vanishing. In all cases mixed support has \(\sigma(f)\ge2p-2\). Finally, the polynomial
\[
U(z)=(z-\zeta)(z-\zeta^2),\qquad V=0
\]
has three nonzero coefficients (since \(p\) is odd) and exactly the two distinct Fourier zeros \(\zeta,\zeta^2\), proving \(\Theta_G(3)=2p-4\).

**Four taps: one coset.** For distribution \((4,0)\) or \((0,4)\), the prime lemma yields \(\sigma(f)\ge2(p-3)=2p-6\ge p-1\).

**Four taps: three and one.** Suppose the coset distribution is \((3,1)\) or \((1,3)\). Now \(D\) has at most seven nonzero coefficients, at the zero difference and the six oriented differences of the three-point coset. It is **not identically zero**: a three-element set in \(\mathbb Z_p\) has at least five distinct differences by Cauchy–Davenport; hence at least four of the six ordered nonzero differences are distinct, and some nonzero difference occurs exactly once. The coefficient of that difference in \(U(z)U(z^{-1})\) (or \(V(z)V(z^{-1})\)) is a product of two nonzero taps and cannot be canceled by the singleton coset. The prime lemma gives at most six Fourier roots of \(D\). No \(M_j\) is zero because the singleton polynomial never vanishes. Without a vanishing linear character, total nullity is at most six. If one linear character vanishes, \(D(1)=0\); the remaining nontrivial roots come in pairs, so at most four can occur, and total nullity is at most five. Both linear characters cannot vanish because the singleton coset sum is nonzero. Therefore \(\sigma(f)\ge2p-6\ge p-1\).

**Four taps: two and two.** Here \(D\) has at most five terms, at \(0,\pm d,\pm e\). If \(D\) is not identically zero, at most four Fourier roots occur. If no linear character vanishes, all the nullity comes from at most four nontrivial roots; if a linear character vanishes, then \(D(1)=0\), leaving at most two nontrivial roots (the number must be even), and at most two missing linear characters. Thus total nullity is at most four and \(\sigma(f)\ge2p-4\ge p-1\). If \(D\) vanishes identically, each \(M_j\) has rank exactly one: its determinant is zero, but it cannot be the zero matrix because the two-term \(U\) cannot vanish at both \(\zeta^j\) and \(\zeta^{-j}\). The two-dimensional irreducibles alone then contribute \(p-1\) to \(\sigma(f)\). Hence again \(\sigma(f)\ge p-1\).

The four-tap signal
\[
f=(\delta_e-\delta_r)*(\delta_e-\delta_s)
=\delta_e-\delta_r-\delta_s+\delta_{rs}
\]
attains the bound. Both linear blocks vanish, and each two-dimensional Fourier block has rank one because \(U(z)=1-z\) and \(V(z)=-(1-z)\) are nonzero at every nontrivial \(p\)-th root. Thus \(\sigma(f)=2\cdot(p-1)/2=p-1\). This completes every exact-support case.

## Verification
The standalone file `check_profile.py` builds the left regular convolution matrix directly, computes exact modular ranks at five primes \(p\in\{5,7,11,13,17\}\) with suitable auxiliary residue characteristics, and separately verifies by exact cyclotomic coefficient arithmetic that the displayed three-tap polynomial has precisely two vanishing prime-frequency evaluations. Its output is `CHECK_OK`. These calculations verify examples only: the uniform theorem rests on the Fourier-block analysis and the cited prime-order zero-count theorem.

## Relationship to prior work
The foundational noncommutative rank-support uncertainty measure and its global product bound are known from Meshulam and from Alagic–Russell. Tao's prime-cyclic Fourier theorem supplies the full-minor lemma; using it alone on the rotation subgroup proves the single-coset bounds but does not control **mixed** dihedral supports. The published two-spike rank law on arbitrary finite groups already implies the second entry; that entry is included to make the exact four-level profile coherent, not offered as an isolated new result. A published three-tap dihedral census treats **unit coefficients**, for which all such convolutions are invertible when \(p\ne3\); it does not bound ranks over arbitrary complex coefficients. The known exact-support profile on cyclic groups of order \(2p\) has the same first four numerical entries, but applies to an abelian character table and cannot imply the mixed two-dimensional dihedral block analysis above. General characteristic-polynomial decompositions for Cayley digraphs supply the representation method, not these support-constrained minima. The contribution is the sharp **nonabelian** first-four profile, including a growing three-versus-two support reversal and the equality construction for four taps.

## Limitations
The result makes no claim for five or more taps, for composite odd rotation order, for fields other than \(\mathbb C\), or for a classification of every extremizer. It uses Chebotarev's established prime Fourier-minor theorem as a mathematical premise. Exact residue-field rank checks are not certificates for all primes or arbitrary complex coefficients. A still-unidentified general theorem on low-support convolution rank could potentially subsume part or all of the result; the cited comparisons do not establish absolute bibliographic uniqueness. No independent audit is asserted.

## References
1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286v1, first public 2003-08-29; *Math. Res. Lett.* 12 (2005), 121–127. https://arxiv.org/abs/math/0308286 .
2. R. Meshulam, *An uncertainty inequality for groups of order pq*, *European J. Combin.* 13 (1992), 401–407. https://meshulam.net.technion.ac.il/files/2021/05/uncer_pq.pdf .
3. G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702v1, first public 2006-08-28. https://arxiv.org/abs/math/0608702 .
4. M. Arezoomand and B. Taeri, *On the characteristic polynomial of n-Cayley digraphs*, *Electron. J. Combin.* 20 (2013), P57. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p57/pdf/ .
5. X. Huang, Q. Huang, and L. Lu, *Enumeration of cubic Cayley graphs on dihedral groups*, arXiv:1609.05419v1, first public 2016-09-18. https://arxiv.org/abs/1609.05419 .
