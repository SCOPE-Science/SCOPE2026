# Composite cubic-chirp Gabor tomography: exact spectrum and stable flat-signal recovery

## Finding
For every integer \(N\ge5\) coprime to \(6\), the cubic-chirp Gabor intensity lifting has an **exact, completely factorized operator spectrum**, including all multiplicities and its entire Weyl-basis nullspace. The operator becomes increasingly rank-deficient along squarefree integers with many distinct prime factors, yet it remains injective (up to constant phase) on signals with no zero coordinates and satisfies a uniform quantitative stability inequality on normalized constant-modulus signals.

Set \(N=\prod_{p^r\parallel N}p^r\) and
\[
R_{p,r}=1+\frac{p(p^{2r}-1)}{p+1},\qquad
m_{p,r}(t)=\begin{cases}(p-1)p^{2(r-t)-1},&0\le t<r,\\1,&t=r.\end{cases}
\]
Then the nonzero eigenvalues of the Gram matrix of all \(N^2\) rank-one Gabor projectors, and equivalently of the intensity-lifting normal operator, are
\[
\lambda_{(t_p)}=\prod_{p^r\parallel N}p^{t_p},\qquad
\operatorname{mult}(\lambda_{(t_p)})=\prod_{p^r\parallel N}m_{p,r}(t_p),
\quad 0\le t_p\le r.
\]
The zero eigenvalue has multiplicity
\[
N^2-\prod_{p^r\parallel N}R_{p,r}.
\]
In particular, the operator rank equals \(\prod_{p^r\parallel N}R_{p,r}\), independently of the unit cubic coefficient.

For example, at \(N=25\) the eigenvalue–multiplicity pairs are \((25,1),(5,20),(1,500),(0,104)\); at \(N=35\) they are \((35,1),(7,20),(5,42),(1,840),(0,322)\). For prime \(N\) the kernel is the trace-zero diagonal space; composite \(N\) has additional off-diagonal missing Weyl modes.

Despite this linear failure, two nonvanishing signals with the same complete Gabor intensity measurements differ by a global phase. For normalized flat signals \(x,y\) (all coordinate magnitudes \(N^{-1/2}\)),
\[
\|\mathcal L(xx^*)-\mathcal L(yy^*)\|_2
\ge \frac{2\sin(\pi/N)}{\sqrt N}
\min_{|c|=1}\|x-cy\|_2.
\]
Moreover, for \(N\) a product of all primes from \(5\) through a growing bound, the rank fraction tends to zero:
\[
\frac{\operatorname{rank}\mathcal L}{N^2}
=\prod_{p\mid N}\left(1-\frac1p+\frac1{p^2}\right)\longrightarrow0.
\]

## Assumptions and scope
The modulus is an integer \(N\ge5\) with \(\gcd(N,6)=1\), and the cubic phase coefficient \(a\) satisfies \(\gcd(a,N)=1\). Denote the cyclic group by \(\mathbb Z_N=\mathbb Z/N\mathbb Z\), and use the standard Hermitian inner product on \(\mathbb C^N\). Put
\[
g_a(j)=N^{-1/2}e^{2\pi i a j^3/N},\quad
(T_u f)(j)=f(j+u),\quad
(M_v f)(j)=e^{-2\pi i vj/N}f(j).
\]
For each \((u,v)\in\mathbb Z_N^2\), define \(g_{u,v}=M_vT_ug_a\), \(P_{u,v}=g_{u,v}g_{u,v}^*\), and
\[
\mathcal L:\mathbb C^{N\times N}\to\mathbb C^{N^2},\qquad
\mathcal L(X)_{u,v}=\operatorname{tr}(P_{u,v}X).
\]
Both spaces have their Hilbert–Schmidt or Euclidean norms. The projectors are unscaled, rather than divided by \(N\), so the normal-operator eigenvalues have the normalization given above. We distinguish operator injectivity from nonlinear phase retrieval on rank-one matrices.

A Weyl operator is \(W_{u,v}=M_vT_u\). For a residue \(u\not\equiv0\pmod{p^r}\), write \(\nu_p(u)\in\{0,\ldots,r-1\}\) for its local valuation; the case \(u\equiv0\pmod{p^r}\) is treated separately. No assertion is made for moduli divisible by \(2\) or \(3\), or for nonunit cubic coefficients.

## Proof
**1. Local ambiguity and exact zeros.** First take \(N=p^r\), \(p\ge5\), and let \(u,v\in\mathbb Z_N\). The normalized ambiguity coefficient is
\[
A(u,v)=\langle g_a,M_vT_ug_a\rangle
=\frac{e^{2\pi i a u^3/N}}N
\sum_{j\bmod N}e^{2\pi i[3au j^2+(3au^2-v)j]/N}.
\]
If \(u=0\), character orthogonality gives \(A(0,v)=\mathbf1_{\{v=0\}}\). If \(u\ne0\) and \(t=\nu_p(u)<r\), the quadratic coefficient has exact valuation \(t\). Grouping the sum into residue classes modulo \(p^{r-t}\) proves that the sum vanishes if \(p^t\nmid(3au^2-v)\); since \(p^t\mid u\), this is exactly \(p^t\nmid v\). Otherwise the sum equals \(p^t\) times a quadratic Gauss sum over \(\mathbb Z/p^{r-t}\mathbb Z\) with a unit quadratic coefficient.

For an odd prime-power modulus \(Q\) and a unit \(\alpha\), the exact identity
\[
\left|\sum_{j\bmod Q}e^{2\pi i(\alpha j^2+\beta j)/Q}\right|^2=Q
\]
follows by replacing the pair of summation variables with their difference \(h\) and one original variable: the inner character sum in the original variable vanishes unless \(2\alpha h\equiv0\pmod Q\), hence only \(h=0\) survives. As \(2\alpha\) is a unit, this gives \(Q\). Therefore
\[
|A(u,v)|^2=
\begin{cases}
1,&u=v=0,\\
p^{t-r},&u\ne0,\ t=\nu_p(u),\ p^t\mid v,\\
0,&\text{otherwise}.
\end{cases}
\]
This proves both directions of the local zero criterion, not merely a sufficient vanishing condition.

**2. Spectrum and local multiplicities.** The normalized Weyl operators \(N^{-1/2}W_{u,v}\) form an orthonormal basis of the Hilbert–Schmidt matrix space. Conjugation by a Gabor shift acts on each Weyl operator by a scalar character. Summing these characters over the full Gabor group shows that the normal operator \(\mathcal L^*\mathcal L\) is diagonal in this basis and that its eigenvalue at \(W_{u,v}\) is precisely
\[
N|A(u,v)|^2.
\]
This standard Gabor spectral diagonalization is credited to the prior literature below; it is also obtained directly by expanding \(\sum_{s,t}|\operatorname{tr}(P_{s,t}W_{u,v}/\sqrt N)|^2=N|A(u,v)|^2\) and applying character orthogonality to remove off-diagonal entries.

For \(N=p^r\), the special pair \((u,v)=(0,0)\) gives eigenvalue \(p^r\) once. At every \(0\le t<r\), there are exactly \((p-1)p^{r-t-1}\) residues \(u\) of valuation \(t\), and exactly \(p^{r-t}\) residues \(v\) divisible by \(p^t\). Thus eigenvalue \(p^t\) has multiplicity
\[
(p-1)p^{2(r-t)-1}.
\]
Summing these multiplicities and adding the identity pair gives
\[
R_{p,r}=1+\sum_{t=0}^{r-1}(p-1)p^{2(r-t)-1}
=1+\frac{p(p^{2r}-1)}{p+1}.
\]
The remaining \(p^{2r}-R_{p,r}\) Weyl coefficients vanish.

**3. Composite modulus.** By the Chinese remainder theorem, \(\mathbb Z_N\cong\prod_{p^r\parallel N}\mathbb Z/p^r\mathbb Z\). Under the associated unitary identification of signal spaces, the cubic chirp is a tensor product of local normalized cubic chirps. Their phase coefficients are multiplied by units, which do not change the local classification. Time–frequency shifts correspond bijectively to products of local shifts, with local modulation indices permuted by units. Hence the family of rank-one projectors is a tensor product family up to reindexing, and the normal operator is unitarily equivalent to a tensor product of the local normal operators. Tensor-product eigenvalues and multiplicities yield the stated full multiset and product rank. Equivalently, \(W_{u,v}\) lies in the kernel precisely when one local factor violates the local nonvanishing criterion.

For prime \(N=p\), the only zero coefficients have \(u=0\) and \(v\ne0\); their Weyl operators span exactly the trace-zero diagonal matrices. For composite \(N\), choose a prime divisor \(p\) and \(u=p\not\equiv0\pmod N\), \(v=1\). Then \(p\mid u\), \(p\nmid v\), so the corresponding Weyl operator is a nonzero off-diagonal kernel mode. (For \(N=p^r\), \(r\ge2\), the same choice works.)

**4. Full-support uniqueness.** For every local prime divisor of \(N\), the delay \(u=1\) is a unit and its ambiguity coefficient is nonzero at every Doppler frequency. The eigenvalues on all Weyl operators \(W_{1,v}\) are therefore positive. If \(\mathcal L(xx^*)=\mathcal L(yy^*)\), the shift-one cyclic diagonals of the Hermitian matrix \(xx^*-yy^*\) must vanish. In particular,
\[
x_{j+1}\overline{x_j}=y_{j+1}\overline{y_j}\qquad(j\bmod N).
\]
For full-support vectors define \(r_j=y_j/x_j\ne0\). The preceding identities imply \(r_{j+1}\overline{r_j}=1\). Hence the ratios alternate between a value \(c\) and \(1/\overline c\). The cyclic length \(N\) is odd, so consistency forces \(c=1/\overline c\), equivalently \(|c|=1\), and every ratio equals \(c\). Thus \(y=cx\). Global phase is the only ambiguity on this class. In contrast, all coordinate basis vectors give identical intensity data because the cubic window is flat, so this is not unrestricted phase retrieval.

**5. Flat-signal stability.** Suppose \(|x_j|=|y_j|=N^{-1/2}\) for every \(j\), and put \(r_j=x_j/y_j\in\mathbb T\), \(m=N^{-1}\sum_jr_j\). The eigenspaces of the normal operator corresponding to both cyclic diagonals with displacements \(1\) and \(-1\) have eigenvalue exactly \(1\). They are orthogonal because \(N\ge5\). For \(H=xx^*-yy^*\), this yields
\[
\|\mathcal L(H)\|_2^2
\ge\frac2{N^2}\sum_j|r_{j+1}-r_j|^2.
\]
The cycle-graph Poincaré inequality, with sharp spectral gap \(4\sin^2(\pi/N)\), gives
\[
\sum_j|r_{j+1}-r_j|^2
\ge4\sin^2(\pi/N)N(1-|m|^2).
\]
Finally \(\min_{|c|=1}\|x-cy\|_2^2=2(1-|m|)\), and \(1-|m|^2\ge1-|m|\). Combining the three inequalities proves the displayed stability bound. The constant is certified as valid; optimality is not asserted.

**6. Arithmetic rank collapse.** If \(N\) is squarefree, the local rank fraction is \(R_{p,1}/p^2=1-p^{-1}+p^{-2}\). Along increasing products of all primes at least \(5\), the logarithm of the rank fraction is at most \(-\sum_{p\mid N}(p^{-1}-p^{-2})\), which tends to minus infinity by the classical divergence of the sum of reciprocal primes. Thus the identified operator fraction tends to zero, despite full-support phase uniqueness.

## Verification
Execute `python cubic_chirp_check.py` with Python 3 and NumPy. The checker constructs the normalized cubic chirp independently, evaluates every cyclic ambiguity coefficient using discrete FFTs for \(N=5,7,25,35,49,55,125\), and compares the predicted eigenvalue multiplicities to both the ambiguity magnitudes and an independent two-dimensional circulant-Gram diagonalization. It also evaluates direct nonlinear Gabor intensities for randomly selected normalized flat signals at \(N=5,25,35\) and verifies the proved stability bound numerically. It reports `CUBIC_CHIRP_GABOR_SPECTRUM_CHECK_OK` and `FLAT_SIGNAL_STABILITY_DIRECT_INTENSITY_OK`. These finite checks are supplemental; the proof applies to every modulus in the stated domain.

## Relationship to prior work
Alltop introduced cubic phase sequences for low periodic correlations. Malikiosis developed finite Gabor frame constructions; Bojarovska–Flinth proved Gabor phase-retrieval criteria and an all-nonzero signal theorem under a different, stronger ambiguity-axis assumption. Goldberger–Kang–Okoudjou supplied the general projector-Gram diagonalization and **already computed the prime-modulus Alltop projector rank**; that prime result is not claimed as new here. Li's 2026 Proposition 5.1 **already proves a sufficient prime-power ambiguity-vanishing congruence**; that obstruction is also not claimed as new. The contribution examined here is the converse and precise magnitude across every local valuation class, the exact multiplicity and nullspace product theorem for *every* odd modulus coprime to six, and the contrast between severe linear tomography rank collapse and quantitative recovery of flat signals. The general diagonalization and Gauss-sum method are credited rather than renamed as new discoveries.

## Limitations
The proof assumes \(\gcd(N,6)=1\) and a unit cubic coefficient. It does not cover moduli divisible by \(2\) or \(3\). The operator is generally not invertible, and unrestricted phase retrieval fails. Full-support uniqueness is qualitative; the explicit quantitative lower bound is proved only for normalized constant-modulus signals, and is not asserted to be sharp. The prime-modulus case and the one-sided prime-power zero obstruction are earlier results. The novelty comparison is bounded: a more specialized earlier exact cubic-ambiguity or Gabor-tomography computation might give equivalent conclusions. No independent mathematical audit has been performed.

## References
1. W. O. Alltop, “Complex sequences with low periodic correlations,” *IEEE Transactions on Information Theory* **26** (1980), 350–354. DOI: 10.1109/TIT.1980.1056185.
2. R.-D. Malikiosis, “A note on Gabor frames in finite dimensions,” arXiv:1304.7709 (first posted 2013-04-29).
3. I. Bojarovska and A. Flinth, “Phase Retrieval from Gabor Measurements,” arXiv:1503.05800 (first posted 2015-03-19), especially Sections 2.2–2.4.
4. A. Goldberger, S. Kang and K. A. Okoudjou, “Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\),” arXiv:2106.01509 (first posted 2021-06-02), especially Theorem 2 and Proposition 4.
5. D. Li, “Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations,” arXiv:2609.09614 (first posted 2026-09-09), especially Proposition 5.1.
