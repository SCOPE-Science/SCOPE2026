# The full three-characteristic Gabor projector spectrum of prime-power cubic chirps

## Finding
Fix any prime \(p\), integer \(k\ge1\), and \(N=p^k\). Let \(\zeta=e^{2\pi i/N}\) and define the unit cubic chirp on the cyclic ring \(\mathbb Z/N\mathbb Z\) by \(g(t)=N^{-1/2}\zeta^{t^3}\). Use the unitary translations \((T_af)(t)=f(t-a)\) and modulations \((M_bf)(t)=\zeta^{bt}f(t)\). The complete \(N^2\)-element Gabor system consists of \(v_{a,b}=M_bT_ag\). Form its rank-one projectors \(P_{a,b}=v_{a,b}v_{a,b}^{*}\), and the unweighted projector Gram matrix
\[
K_{(a,b),(c,d)}=\operatorname{tr}(P_{a,b}P_{c,d})=|\langle v_{a,b},v_{c,d}\rangle|^2.
\]
**Complete spectrum** (every listed multiplicity is exact; other eigenvalues are zero):

- If \(p=2\): the eigenvalue \(N\) occurs twice, and \(N2^{1-r}\) occurs \(4^{r-1}\) times for each \(2\le r\le k\).
- If \(p=3\): the eigenvalue \(N\) occurs three times, and \(N3^{1-r}\) occurs \(2\cdot3^{2r-2}\) times for each \(2\le r\le k\).
- If \(p\ge5\): the eigenvalue \(N\) occurs once, and \(Np^{-r}\) occurs \((p-1)p^{2r-1}\) times for each \(1\le r\le k\).

A range with lower endpoint above its upper endpoint is empty. Thus at prime exponent \(k=1\), the exceptional primes \(2\) and \(3\) have just one positive spectral level, while for \(p\ge5\) there are two.

The exact ranks are
\[
\boxed{\operatorname{rank}K=\begin{cases}(N^2+2)/3,&p=2,\\(N^2+3)/4,&p=3,\\(pN^2+1)/(p+1),&p\ge5.\end{cases}}
\]
As \(k\to\infty\) with \(p\) fixed, the fraction of identifiable complex matrix directions tends respectively to \(1/3\), \(1/4\), or \(p/(p+1)\). In particular the characteristic-three defect is stronger than the characteristic-two defect, while all primes at least five have much higher limiting rank fractions.

Let \(\mathcal L(H)=(\operatorname{tr}(HP_{a,b}))_{a,b}\) denote the unweighted Hilbert--Schmidt projector-analysis map. Its squared nonzero singular values are the stated eigenvalues. The smallest positive eigenvalue and corresponding nonzero-subspace analysis condition number are
\[
\boxed{\begin{array}{c|c|c} \text{case}&\lambda_{\min}^{+}&\kappa(\mathcal L\vert_{(\ker\mathcal L)^\perp})\\ \hline p=2,\ k=1&2&1\\p=2,\ k\ge2&2&\sqrt{N/2}\\p=3,\ k=1&3&1\\p=3,\ k\ge2&3&\sqrt{N/3}\\p\ge5&1&\sqrt N\end{array}}
\]
These are quotient/injectively restricted condition numbers, not conditioning for globally invertible linear tomography, since the full lifting always has a kernel.

**Complete missing-coordinate classification.** The Weyl matrices \(W_{a,b}=M_bT_a\) with \(A_g(a,b)=\langle g,W_{a,b}g\rangle=0\) form a complex Hilbert--Schmidt basis of \(\ker\mathcal L\). For \(a=0\) only \(b=0\) survives. For \(a\ne0\), put \(s=v_p(a)\), \(r=k-s\), and \(B\equiv3a^2+b\pmod N\). The direction survives exactly under the following congruence, and then has the listed squared ambiguity modulus:
\[
\begin{array}{c|c|c} \text{case}&\text{survival congruence}&|A_g(a,b)|^2\\ \hline p=2,\ r=1&B\equiv2^s\pmod{2^{s+1}}&1\\p=2,\ r\ge2&B\equiv0\pmod{2^{s+1}}&2^{1-r}\\p=3,\ r=1&B\equiv0\pmod N&1\\p=3,\ r\ge2&B\equiv0\pmod{3^{s+1}}&3^{1-r}\\p\ge5&B\equiv0\pmod{p^s}&p^{-r}\end{array}
\]
At \((a,b)=(0,0)\) the squared ambiguity modulus is one. Every Weyl direction not covered by these congruences belongs to the lifting kernel.

## Assumptions and scope
Indices are cyclic residues modulo \(N\); the norm of \(g\) is exactly one. All \(N^2\) projectors are included with no extra measurement weights. The matrix norm is Hilbert--Schmidt and the output norm is Euclidean. Results are for the unmodified phase \(t^3\) on prime-power **cyclic rings**; replacing the ring with a finite field of the same order is not a harmless equivalence. No composite-modulus Chinese remainder extension is asserted.

## Proof
**1. Cubic difference and Gauss-sum reduction.** Expand the self-ambiguity function:
\[
A_g(a,b)=\zeta^{-a^3}N^{-1}\sum_{t\bmod N}\zeta^{-3at^2+(3a^2+b)t}.
\]
For \(a=0\), ordinary character orthogonality gives \(A_g(0,b)=\mathbf1_{\{0\}}(b)\). For \(a\ne0\) let \(s=v_p(a)\), \(r=k-s\), and \(B=3a^2+b\). If \(c\) is the quadratic coefficient and \(d=\gcd(c,N)\), the sum \(\sum_{t\bmod N}\zeta^{ct^2+Bt}\) vanishes unless \(d\mid B\). If \(d\mid B\), dividing out the common factor gives \(d\) times a primitive quadratic Gauss sum modulo \(N/d\). In all cases when the reduced odd modulus has an invertible leading coefficient, a direct square expansion yields \( |G(u,v;p^j)|^2=p^j\), since \(2u\) is invertible: only the zero shift survives.

For dyadic reduced moduli, odd \(u\) and \(j\ge2\), the same expansion instead gives
\[
|G(u,v;2^j)|^2=2^j\sum_{h:\,2uh\equiv0\ (\mathrm{mod}\ 2^j)}\exp\left(\frac{2\pi i(uh^2+vh)}{2^j}\right)=2^j(1+(-1)^v).
\]
The only surviving shifts are \(h=0\) and \(h=2^{j-1}\); the latter has integral quadratic phase. When \(j=1\), \(G(u,v;2)=1+(-1)^{u+v}\), with squared modulus \(4\) exactly for odd \(v\). This treats the exceptional even-prime branch without any unproved Gaussian phase evaluation.

**2. Prime at least five.** Here \(3\) is invertible and the quadratic coefficient \(-3a\) has valuation exactly \(s\). The Gauss sum survives precisely if \(p^s\mid B\), then the reduced modulus is \(p^r\) and
\[
|A_g(a,b)|^2=p^{-r}.
\]
There are exactly \((p-1)p^{r-1}\) choices of \(a\) with valuation \(s=k-r\), and exactly \(p^r\) valid modulations \(b\) for each such translation. Thus the level \(p^{-r}\) has multiplicity \((p-1)p^{2r-1}\), with \(1\le r\le k\), in addition to the origin. The total number of nonzero labels is
\[
1+\sum_{r=1}^k(p-1)p^{2r-1}=\frac{pN^2+1}{p+1}.
\]

**3. Prime three.** Here the coefficient \(-3a\) has valuation \(s+1\), as long as \(s\le k-2\). In that case the Gauss sum survives precisely when \(3^{s+1}\mid B\); its reduced modulus is \(3^{r-1}\), so
\[
|A_g(a,b)|^2=3^{1-r},\qquad 2\le r\le k.
\]
Exactly \(2\cdot3^{r-1}\) translations and \(3^{r-1}\) modulations realize each such level, yielding multiplicity \(2\cdot3^{2r-2}\). If \(s=k-1\), the quadratic coefficient vanishes modulo \(N\) and the remaining linear coefficient is congruent to \(b\); precisely \(b=0\) survives, with squared modulus one. There are two such nonzero translations, plus the origin. Therefore
\[
3+\sum_{r=2}^{k}2\cdot3^{2r-2}=\frac{N^2+3}{4}.
\]

**4. Prime two.** Write \(r=k-s\). If \(r=1\), the reduced Gauss sum is modulo two, so precisely \(B\equiv2^s\pmod{2^{s+1}}\) survives with squared modulus one. If \(r\ge2\), precisely \(B\equiv0\pmod{2^{s+1}}\) survives, with squared modulus \(2^{1-r}\). Exactly \(2^{r-1}\) translations have this valuation; each admits exactly \(2^{r-1}\) valid modulations. Thus squared-ambiguity level \(2^{1-r}\) occurs \(4^{r-1}\) times for \(1\le r\le k\), plus the identity. For \(r=1\), the extra label and the identity give the two top occurrences. The total number of nonzero labels is
\[
1+\sum_{r=1}^{k}4^{r-1}=\frac{N^2+2}{3}.
\]

**5. Exact projector spectrum and kernel.** The normalized Weyl matrices \(N^{-1/2}W_{a,b}\) are an orthonormal Hilbert--Schmidt basis. Conjugation by a Weyl shift acts diagonally on each Weyl direction; discrete Fourier orthogonality implies
\[
\|\mathcal L(H)\|_2^2=N\sum_{a,b}|A_g(a,b)|^2|\widehat H(a,b)|^2,
\]
where \(\widehat H(a,b)\) are the coefficients of \(H\) in the normalized Weyl basis (up to harmless convention-dependent index permutation). Consequently the eigenvalues of the normal operator, equivalently those of the square projector Gram matrix, are precisely \(N|A_g(a,b)|^2\). Steps 2--4 provide all their multiplicities. A Weyl direction belongs to \(\ker\mathcal L\) exactly when its ambiguity coefficient vanishes. Passing to the real Hermitian subspace preserves the positive eigenvalue levels and total real dimensions because the normal operator preserves adjoints.

**6. Asymptotic and conditioning statements.** The ranks just proved divided by \(N^2\) give their stated limits. The top eigenvalue is \(N\) in each prime regime. The smallest positive eigenvalues follow by taking the largest available \(r\) in the lists, giving \(2\), \(3\), or \(1\) as stated, with the two small prime-power boundary cases handled explicitly. Ratios of square roots of the eigenvalues give the claimed restricted condition numbers.

## Verification
The standalone `check_primepower_cubic.py` computes the complete self-ambiguity array by FFT from the defining window in 21 independent prime-power cases (including exponents up to eight for prime two, five for prime three, and three for prime five). It compares all entries against the number-theoretic piecewise formula, checks exact rank/count and the Moyal sum, and for dimensions at most sixteen separately constructs and diagonalizes the full projector Gram matrix. The execution record `checker_output.txt` reports maximum observed entrywise discrepancy below \(7\times10^{-16}\) and complete Gram eigenvalue discrepancy below \(1.1\times10^{-14}\). These are corroborations; the infinite-parameter theorem is proved by exact Gauss-sum orthogonality, not inferred from finite data.

## Relationship to prior work
Bojarovska and Flinth, *Phase Retrieval from Gabor Measurements* (arXiv:1503.05800), already analyze cubic Alltop windows and prove qualitative failure of general signal phase retrieval. In prime dimension their framework includes the familiar nonzero ambiguity pattern. Alaifari and Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements* (arXiv:1901.05296), establish general ambiguity-based Fourier identities. Li, *Explicit Full-Spark Gabor Windows with Quantitative Phase Retrieval* (arXiv:2609.09614), gives the general projector Gram spectral diagonalization in Proposition 2.4, and constructs repaired Chu chirp windows; the latter paper's preprint versions also discuss zero ambiguity of unmodified cubic chirps for composite prime powers. Related published results compute the complete spectra of *impulse-perturbed* chirps and finite-field Alltop variants. These enabling formulas and earlier qualitative obstructions are acknowledged; the candidate contribution is the complete **unmodified cyclic prime-power** spectrum, including the extra loss of rank at prime three and all exact eigenvalue multiplicities across all exponents.

## Limitations
The theorem concerns all time-frequency shifts over a cyclic prime-power ring, with a precisely normalized unmodified cubic phase. It is not a generic statement about arbitrary cubic coefficients, finite fields, or composite moduli with several prime factors, and it does not provide stable global recovery since the lifting has a kernel. It does not claim to have discovered the known qualitative Alltop phase-retrieval obstruction. An equivalent full 2-adic/3-adic prime-power ambiguity census in older radar/polyphase sequence literature remains a realistic originality risk. Independent expert assessment has not been performed.

## References
- I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (2015), Section 2.4, Example 2.3.
- R. Alaifari and M. Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements*, arXiv:1901.05296 (first public version 2019-01-12), Section 2, Lemma 2.2.
- D. Li, *Explicit Full-Spark Gabor Windows with Quantitative Phase Retrieval*, arXiv:2609.09614 (2026 preprint), Proposition 2.4.
