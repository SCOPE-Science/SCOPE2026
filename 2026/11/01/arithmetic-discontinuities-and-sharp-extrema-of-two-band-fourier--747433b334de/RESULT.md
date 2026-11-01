# Arithmetic discontinuities and sharp extrema of two-band Fourier Lebesgue constants

## Finding

For every real \(\alpha>1\) and positive integer \(N\), put \(m_N=\lfloor\alpha N\rfloor\) and
\[
P_{N,\alpha}(t)=\sum_{j=0}^{N-1}e^{ijt}+\sum_{j=0}^{N-1}e^{i(j+m_N)t},\qquad
\Lambda_N(\alpha)=\frac1{2\pi}\int_{-\pi}^{\pi}|P_{N,\alpha}(t)|\,dt.
\]
The normalized Lebesgue constants converge for **every** such \(\alpha\):
\[
C(\alpha)=\lim_{N\to\infty}\frac{\Lambda_N(\alpha)}{\log N}.
\]
If \(\alpha\) is irrational, \(C(\alpha)=16/\pi^3\). If \(\alpha=p/q\), where \(p>q\ge1\) are coprime integers, then
\[
C(p/q)=\frac{16}{\pi^3}\left(1+2\sum_{\ell=1}^{\infty}
\frac{(-1)^{q\ell}}{(4p^2\ell^2-1)(4q^2\ell^2-1)}\right).
\]
The series converges absolutely. Every rational slope with even reduced denominator has \(C(p/q)>16/\pi^3\); every rational slope with odd reduced denominator has \(C(p/q)<16/\pi^3\). Consequently \(C\) is continuous at every irrational slope and discontinuous at every rational slope in \((1,\infty)\).

Both global extrema over \(\alpha>1\) are attained uniquely:
\[
\boxed{\min_{\alpha>1}C(\alpha)=C(2)=\frac{8(2\sqrt2-1)}{3\pi^2}},
\qquad
\boxed{\max_{\alpha>1}C(\alpha)=C(3/2)=\frac{8(3\sqrt3-2)}{5\pi^2}}.
\]
Numerically, these are approximately \(0.494022401288\) and \(0.518140714512\), compared with the irrational value \(0.516024550931\).

## Assumptions and scope

The torus carries normalized measure \(dt/(2\pi)\). Both Fourier blocks have \(N\) consecutive positive-frequency coefficients equal to one. The starting-frequency offset of the second block is \(m_N\); \(\alpha>1\) is fixed while \(N\to\infty\). The blocks are disjoint for all sufficiently large \(N\). There are no hypotheses on Diophantine approximation of irrational \(\alpha\). Logarithms are natural. In the rational case the fraction is always reduced before applying the parity rule.

## Proof

**1. Reduction to an almost-periodic logarithmic mean.** By the geometric-series identity,
\[
P_{N,\alpha}(t)=\frac{(1-e^{iNt})(1+e^{im_Nt})}{1-e^{it}}.
\]
The absolute value is even. Since \(|1-e^{iNt}|\le Nt\) for \(0\le t\le1/N\), the contribution of this short interval to \(\Lambda_N\) is uniformly bounded. For \(0<t\le\pi\),
\[
\left|\frac1{2\sin(t/2)}-\frac1t\right|\le Kt
\]
with an absolute \(K\), while the numerator has modulus at most four. Therefore, putting
\(F_a(u)=|1-e^{iu}|\,|1+e^{iau}|=4|\sin(u/2)\cos(au/2)|\),
\[
\Lambda_N(\alpha)=\frac1\pi\int_1^{\pi N}\frac{F_{m_N/N}(u)}u\,du+O(1).
\]
For all \(u\ge0\), \(|F_a(u)-F_b(u)|\le2|a-b|u\). As \(|m_N/N-\alpha|<1/N\), integration yields
\[
\Lambda_N(\alpha)=\frac1\pi\int_1^{\pi N}\frac{F_\alpha(u)}u\,du+O(1).
\tag{1}
\]
Here the bounded error can be taken uniformly in \(N\) and \(\alpha>1\).

The function \(F_\alpha\) is bounded and uniformly almost periodic, being the pullback of a continuous function on a two-torus. Its Cesàro mean \(M_\alpha=\lim_{R\to\infty}R^{-1}\int_0^R F_\alpha(u)\,du\) exists. If \(G(R)=\int_0^R(F_\alpha-M_\alpha)\,du=o(R)\), integration by parts shows \(\int_1^R F_\alpha(u)du/u=M_\alpha\log R+o(\log R)\). Consequently (1) gives \(C(\alpha)=M_\alpha/\pi\) without a rate assumption.

**2. Irrational and rational means.** If \(\alpha\notin\mathbb Q\), continuous torus equidistribution makes the two phases independent. Since each of \(|\sin|\) and \(|\cos|\) has mean \(2/\pi\), it follows that \(M_\alpha=16/\pi^2\), hence \(C(\alpha)=16/\pi^3\).

For reduced \(\alpha=p/q\), the period is \(2\pi q\). The absolutely and uniformly convergent cosine series are
\[
|\sin(u/2)|=\frac2\pi-\frac4\pi\sum_{n\ge1}\frac{\cos(nu)}{4n^2-1},
\qquad
|\cos(pu/(2q))|=\frac2\pi-\frac4\pi\sum_{m\ge1}\frac{(-1)^m\cos(mpu/q)}{4m^2-1}.
\]
The only nonconstant products with nonzero period mean satisfy \(nq=mp\). Coprimality forces \(n=p\ell\), \(m=q\ell\). Orthogonality, with the factor four in \(F\), now gives precisely the displayed rational series for \(C(p/q)\). For even \(q\), all summands are positive. For odd \(q\), they alternate in sign and strictly decrease in magnitude; the sum is strictly negative.

**3. Sharp global extrema.** For integers \(p>q\ge1\), let
\[
a_\ell(p,q)=\big[(4p^2\ell^2-1)(4q^2\ell^2-1)\big]^{-1}>0.
\]
In the even-\(q\) case, \(q\ge2\) and \(p\ge3\). Every term \(a_\ell(p,q)\) is at most \(a_\ell(3,2)\), and at least one inequality is strict unless \((p,q)=(3,2)\). Thus \(3/2\) uniquely maximizes the rational excess, and the irrational and odd-denominator values are smaller.

For odd \(q\), the deficit is \(D(p,q)=a_1-a_2+a_3-\cdots\), satisfying \(0<D(p,q)<a_1(p,q)\). Except at \((p,q)=(2,1)\), one has \(p\ge3\), so \(D(p,q)<a_1(p,q)\le1/105\). But
\[
D(2,1)>a_1(2,1)-a_2(2,1)=\frac1{45}-\frac1{945}=\frac{20}{945}>\frac1{105}.
\]
Thus \(2\) uniquely maximizes the odd-denominator deficit and is the unique global minimum.

To evaluate the two extremal constants in radicals, substitute \(u=2qv\) in the period mean:
\[
C(p/q)=\frac4{\pi^2}\int_0^\pi|\sin(qv)\cos(pv)|\,dv.
\]
Splitting the integral at the zeros of both trigonometric factors gives
\[
\int_0^\pi|\sin v\cos(2v)|\,dv=\frac{4\sqrt2-2}{3},
\quad
\int_0^\pi|\sin(2v)\cos(3v)|\,dv=\frac{6\sqrt3-4}{5},
\]
which yields the stated constants.

**4. Continuity classification.** At every reduced rational \(p/q\), the nonzero signed series correction differs from the irrational constant, and nearby irrational slopes exist; \(C\) is discontinuous there. Conversely, if \(\alpha_j\to\alpha\notin\mathbb Q\), any rational subsequence \(\alpha_j=p_j/q_j\) (in lowest terms) has \(q_j\to\infty\); otherwise a bounded-denominator subsequence near \(\alpha\) would be eventually constant, impossible. Since \(p_j>q_j\), the absolute series correction is bounded by \(O(q_j^{-4})\), which tends to zero. Irrational terms already equal the common value. Hence \(C\) is continuous at every irrational.

## Verification

Run \(\texttt{python check.py}\) with Python 3 and no external dependencies. The checker verifies the absolutely convergent rational series against direct period-midpoint integrals for eight coprime pairs, the parity and global bounds, the radical extrema, and finite-size numerical slopes for four sample parameters. It reports 30 successful checks. In particular, the finite-size slopes near \(\alpha=2\), \(3/2\), and \(\sqrt2\) agree with the respective coefficients. The analytic Cesàro-mean argument, resonance classification, and strict bounds constitute the proof; numerical tests are not an infinite certificate.

## Relationship to prior work

The classical one-block Dirichlet Lebesgue constant has coefficient \(4/\pi^2\), as recounted in Liflyand's 2006 survey. That survey also develops broader almost-periodic jump-mean methods for some multiplier kernels; those methods motivate but do not directly supply the explicit two-band rational resonance series, reduced-denominator sign law, and sharp global extremizers. Jaming, Kellay, Saba, and Wang (2024) study lower \(L^1\) estimates for spectra with gaps increasing to infinity; the present spectra instead have unit gaps inside both growing blocks and only one macroscopic gap. The result should not be read as claiming novelty for the general existence of an almost-periodic mean.

## Limitations

The result treats exactly two equal-length blocks with equal positive coefficients, fixed gap ratio \(\alpha>1\), and the ordinary continuous circle. It does not claim uniform convergence in \(\alpha\); indeed the limit function is discontinuous at rational slopes. Other block lengths, arbitrary coefficient phases, higher dimensions, and finite cyclic sampling are not covered. The originality comparison does not exclude indirect appearance of the same specific arithmetic evaluation in older or inaccessible treatments of general Fourier jump polynomials; independent historical and mathematical review remains to be performed.

## References

1. P. Jaming, K. Kellay, C. Saba, Y. Wang, *On L1-norms for non-harmonic trigonometric polynomials with sparse frequencies*, arXiv:2409.07093, first posted September 11, 2024. https://arxiv.org/abs/2409.07093
2. P. Jaming, K. Kellay, C. Saba, *The Littlewood problem and non-harmonic Fourier series*, arXiv:2303.10919, 2023. https://arxiv.org/abs/2303.10919
3. E. R. Liflyand, *Lebesgue constants of multiple Fourier series*, Online Journal of Analytic Combinatorics 1 (2006), article 5. https://combinatorialpress.com/article/ojac/vol1/liflyand_2006.pdf
