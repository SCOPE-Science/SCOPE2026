# Sharp two-mask phase retrieval trichotomy on prime-cyclic Sidon supports

## Finding
Fix an odd prime \(p\), put \(\omega=\exp(2\pi i/p)\), and choose distinct \(r_0,r_1\in\mathbb F_p\). For an array \(x=(x_n)_{n\in\mathbb F_p}\), measure all \(p\) intensities in each of the two quadratic masks:
\[
I_r(k)=\left|\sum_{n\in\mathbb F_p}x_n\omega^{rn^2-kn}\right|^2,
\quad k\in\mathbb F_p,\quad r\in\{r_0,r_1\}.
\]
A nonempty support \(S\subset\mathbb F_p\) is a *directed Sidon support* if its map \((a,b)\mapsto a-b\) is injective on ordered pairs of distinct elements. (This is equivalent to the usual difference-Sidon condition.) The nonzero entries may be arbitrary complex numbers.

**Theorem.** Within the class of all nonzero arrays with directed Sidon support, the two-mask intensity fiber of an array with \(s\) nonzero entries contains exactly the following numbers of classes modulo common unit-modulus scalar:

* \(s=1\): precisely \(p\) classes, one at each location;
* \(s=2\): precisely two classes when the two nonzero moduli differ, and one class when they agree;
* \(s\ge3\): precisely one class.

Both the support and every pair product are recovered explicitly for \(s\ge2\). The two-mask count in the last case is optimal: **no single phase-only Fourier mask** is injective on the directed-Sidon class of cardinality at least three. Moreover, the two-class ambiguity at cardinality two, and the location ambiguity at cardinality one, persist for **every collection, even an arbitrarily large collection, of phase-only diagonal Fourier masks**.

For \(s=2\), with support \(\{a,b\}\) and coefficients \(A=x_a\), \(B=x_b\), the only possible nontrivial partner (besides global phase) is
\[
y_a=\frac{|B|}{|A|}A,\qquad
 y_b=\frac{|A|}{|B|}B,
\]
with every other coordinate zero. It coincides with the original phase class exactly when \(|A|=|B|\).

## Assumptions and scope
Indices, differences, squaring, and inverses are in the prime field \(\mathbb F_p\). The mask entries have modulus one. Distinct mask exponents are necessary; their values are otherwise arbitrary. The intensity Fourier transform is the *full unnormalized* \(p\)-point transform; intensities are squared moduli. The fiber classification is explicitly **relative to the union of Sidon-support signal classes**; an unrestricted competitor is not assumed to have Sidon support, and no claim of unrestricted injectivity is made. No noise robustness is asserted.

Every directed Sidon support with \(s\ge3\) is proper in \(\mathbb F_p\), and such supports occur only when \(s(s-1)\le p-1\), for example \(\{0,1,3\}\subset\mathbb F_7\).

## Proof
**1. Exact recovery of cyclic correlations.** Put \(z_r(n)=x_n\omega^{rn^2}\). Define
\[
C_r(d)=\frac1p\sum_{k\in\mathbb F_p}I_r(k)\omega^{kd}.
\]
Expanding the square and using \(p^{-1}\sum_k\omega^{k(d-n+m)}=\mathbf1_{d=n-m}\) gives the exact identity
\[
C_r(d)=\sum_{n\in\mathbb F_p}x_n\overline{x_{n-d}}\omega^{r(n^2-(n-d)^2)}.
\tag{1}
\]
In particular \(C_r(0)=\sum_n|x_n|^2\). For a directed Sidon support and \(d\ne0\), either \(C_r(d)=0\), or there is a unique ordered pair \((a,b)\in S^2\), \(a\ne b\), \(a-b=d\), and
\[
C_r(d)=x_a\overline{x_b}\omega^{rd(a+b)}\ne0.
\tag{2}
\]
Thus \(D=\{d\ne0:C_{r_0}(d)\ne0\}\) is exactly the directed difference set and \(|D|=s(s-1)\), which determines \(s\ge1\).

**2. Absolute support and off-diagonal product recovery.** For each \(d\in D\), divide the two nonzero correlations:
\[
\frac{C_{r_1}(d)}{C_{r_0}(d)}
=\omega^{(r_1-r_0)d(a+b)}.
\tag{3}
\]
Its exponent \(e_d\in\mathbb F_p\) is uniquely identified, because \(\omega\) has exact order \(p\). All factors \(2\), \(r_1-r_0\), and \(d\) are invertible. Set
\[
s_d=\frac{e_d}{(r_1-r_0)d},\qquad
a_d=\frac{s_d+d}{2},\qquad b_d=\frac{s_d-d}{2}.
\tag{4}
\]
The ordered pair at difference \(d\) is exactly \((a_d,b_d)\). Hence \(S=\bigcup_{d\in D}\{a_d,b_d\}\) for \(s\ge2\). Equation (2) then supplies every nonzero off-diagonal product, without an unknown phase factor:
\[
P_{ab}=x_a\overline{x_b}=C_{r_0}(a-b)\omega^{-r_0(a^2-b^2)}.
\tag{5}
\]
If another Sidon-supported array has the same measurements, it has the same \(D\), pairs, support, and products.

**3. Rank-one completion for three or more atoms.** Take distinct \(i,j,k\in S\). From the complete off-diagonal products,
\[
|x_i|^2=\frac{P_{ji}P_{ik}}{P_{jk}}>0.
\tag{6}
\]
The same formula recovers all diagonal products, since \(s\ge3\). All entries of the rank-one Hermitian matrix \((x_a\overline{x_b})_{a,b\in S}\) are therefore known. A nonzero rank-one Hermitian matrix determines its generating vector up to a single unimodular multiplier: fix any index with positive diagonal and use its row. This proves the singleton fiber for \(s\ge3\).

**4. The two smaller supports.** For \(s=2\), equation (5) determines \(P=A\overline B\) and (1) at zero determines \(E=|A|^2+|B|^2\). The two positive squared moduli are the roots of
\[
q^2-Eq+|P|^2=0.
\tag{7}
\]
If distinct, their two assignments to the recovered locations produce precisely two phase classes; the displayed partner interchanges their magnitudes without changing \(P\) or \(E\). When equal, the assignments coincide. For \(s=1\), every nonzero-shift correlation is zero and the zero-shift correlation is the squared modulus; every one of the \(p\) possible positions yields these same intensities.

**5. Optimality and intrinsic obstructions.** Consider one arbitrary phase-only diagonal mask \(m_n\), \(|m_n|=1\). Set \(z_n=m_nx_n\). For any nonzero cyclic shift \(t\), define \(y_n=\overline{m_n}z_{n-t}\). Then \(|\widehat{my}|=|\widehat{mx}|\) because its masked signal is a translate of \(z\). The support of \(y\) is \(S+t\), still Sidon. For \(s\ge3\), \(S\) is nonempty and proper in the prime cyclic group, so \(S+t\ne S\). Consequently no single phase-only mask is injective on this class.

For arbitrary phase-only masks \(m^{(\lambda)}\), every circular autocorrelation of a two-site masked signal depends only on \(E\) and \(P\), multiplied in the two nonzero shifts by the known mask cross-phase. The partner from step 4 shares \(E\) and \(P\), hence matches the intensities of *every* such mask. A single-site signal always produces constant intensity \(|A|^2\) under any phase-only mask, independent of its location. These are absolute information-theoretic obstructions and complete the proof.

## Verification
`CHECK.py` is a standalone Python 3 standard-library supplementary verifier. It enumerates every directed Sidon support of size two through five that exists in the prime orders \(3,5,7,11,13,17,19\), assigns nonzero Gaussian-integer coefficients, builds the cyclic correlations in an exact formal-root basis, reconstructs all ordered endpoints from the exponent differences, and tests the rank-one triple identity and the two-site magnitude swap. It also tests alternative distinct chirp-exponent pairs for the smaller orders. The script completed with `CHECK_OK configurations=4983` and support counts per prime \(3,10,35,165,338,1224,2109\), respectively. No floating-point phase comparisons are involved. This finite check does not establish the infinite-prime theorem independently; equations (1)–(7) provide the complete proof.

## Relationship to prior work
Novikov and Xu (2026) produce strong nonuniqueness examples for conventional continuous/discrete Fourier phase retrieval, including Pauli partners and background-assisted settings. Their investigated results do not use the two deterministic quadratic masks or give this Sidon-support trichotomy. Jaganathan, Oymak and Hassibi (2013/2017) establish generic sparse Fourier recovery modulo translation/reflection under different zero-padded measurements, not uniform absolute-location recovery for all Sidon supports. Jaganathan, Eldar and Hassibi (2015) use nonunimodular masks with zeros and zero-padding, rather than two phase-only quadratic masks. Relevant finite cyclic Gabor tomography and sparse STFT support results use different measurement families and do not imply the rank-one completion or two-mask minimality here. The contribution is the exact universal Sidon-class two-pattern fiber theorem and its sharp one-/two-atom obstructions, not the standard Fourier/autocorrelation identity by itself.

## Limitations
The Sidon assumption is substantive: if nonzero differences repeat, a correlation is a sum of several products and the single-root decoding in (3) fails. The theorem only classifies competitors **within** the Sidon class. It gives no stability bound under measurement noise or uniqueness for arbitrary three-sparse supports. The spectral masks use prime-cyclic arithmetic; composite cyclic orders may have noninvertible differences. Earlier unindexed equivalent results in coded-diffraction literature remain a possible priority risk.

## References
1. R. Novikov and T. Xu, *On phase retrieval for continuous and discrete Fourier transforms*, arXiv:2604.25662, first submitted 2026-04-28. https://arxiv.org/abs/2604.25662
2. K. Jaganathan, S. Oymak and B. Hassibi, *Sparse Phase Retrieval: Uniqueness Guarantees and Recovery Algorithms*, arXiv:1311.2745 (2013); IEEE Trans. Signal Process. 65 (2017). https://arxiv.org/abs/1311.2745
3. K. Jaganathan, Y. C. Eldar and B. Hassibi, *Phase Retrieval with Masks using Convex Optimization*, ISIT 2015. https://webee.technion.ac.il/Sites/People/YoninaEldar/conferences/243_Phase%20Retrieval%20with%20Masks%20using%20Convex%20Optimization.pdf
4. M. A. Iwen, A. Viswanathan and Y. Wang, *Fast Phase Retrieval from Local Correlation Measurements*, SIAM J. Imaging Sci. 9 (2016). https://doi.org/10.1137/15M1053761
