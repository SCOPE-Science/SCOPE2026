# A sharp spectral-collapse boundary for exponentially weighted half-plane translations

## Finding
For every real \(\alpha>-1\) and \(a,b\geq0\), consider the weighted composition operator
\[
(W_{a,b}f)(z)=e^{-bz}f(z+a)
\]
on the weighted Bergman space \(A^2_\alpha(\mathbb C_+)\), where \(\mathbb C_+=\{z:\operatorname{Re}z>0\}\). Put \(\eta=(\alpha+1)/2>0\). Its spectrum and Fredholm essential spectrum, in both cases, are exactly
\[
\begin{array}{c|c}
(a,b)&\sigma(W_{a,b})=\sigma_{\rm e}(W_{a,b})\\ \hline
(0,0)&\{1\}\\
a>0,\ b=0 &[0,1]\\
a=0,\ b>0 &\{\lambda:|\lambda|\le1\}\\
a>0,\ b>0 &\{0\}.
\end{array}
\]
For every integer \(n\ge1\), the exact operator norm is \(1\) if \(ab=0\). If \(ab>0\), define
\[
t_n=\frac{2\eta b/a}{\sqrt{n^2b^2+4\eta b/a}+nb}.
\]
Then
\[
\boxed{\|W_{a,b}^n\|=e^{-abn(n-1)/2-ant_n}\left(\frac{t_n}{t_n+nb}\right)^\eta.}
\]
For fixed \(a,b>0\), its sharp asymptotic is
\[
\boxed{\|W_{a,b}^n\|=\left(\frac{\eta}{eab}\right)^\eta n^{-2\eta}e^{-abn(n-1)/2}(1+O(n^{-2})).}
\]
For every \(a,b\ge0\), integer \(n\ge1\), and finite positive integer \(j\), the approximation number satisfies \(a_j(W_{a,b}^n)=\|W_{a,b}^n\|\). In particular every nonzero power is noncompact, even though \(W_{a,b}\) and its nonzero Calkin image are quasinilpotent when \(ab>0\). The spectral-radius transition across the coordinate axes occurs despite convergence of the operator norms to \(1\) on approach to either axis.

## Assumptions and scope
The Bergman norm is \(\|f\|^2=\pi^{-1}\int_0^\infty\int_{-\infty}^\infty x^\alpha |f(x+iy)|^2\,dy\,dx\). Everything is over complex Hilbert spaces. The spectrum is the usual bounded-operator spectrum; the essential spectrum is the spectrum in the Calkin algebra (failure of Fredholmness). Approximation numbers are \(a_j(T)=\inf\{\|T-F\|:\operatorname{rank}F<j\}\). No numerical approximation is needed to interpret the formulas.

## Proof
**1. Exact Laplace model.** The weighted Paley–Wiener theorem identifies \(A^2_\alpha(\mathbb C_+)\) isometrically with \(L^2((0,\infty),c_\alpha t^{-2\eta}dt)\), where \(c_\alpha=\Gamma(\alpha+1)/2^\alpha\), via \((\mathcal Lh)(z)=\int_0^\infty e^{-zt}h(t)dt\). Under this equivalence,
\[
(B_{a,b}h)(s)={\mathbf{1}}_{s>b}e^{-a(s-b)}h(s-b).
\]
Consequently, with \(t=s-nb\),
\[
(B_{a,b}^nh)(t+nb)=e^{-ant-abn(n-1)/2}h(t).
\]
The resulting exact input-to-output squared density ratio is \(e^{-2ant-abn(n-1)}(t/(t+nb))^{2\eta}\). Therefore
\[
\|B_{a,b}^n\|=\sup_{t>0}e^{-ant-abn(n-1)/2}(t/(t+nb))^\eta.
\]
If \(ab=0\) this supremum is \(1\), approached at \(t\downarrow0\) when \(b=0\), or \(t\uparrow\infty\) when \(a=0\). If \(ab>0\), the logarithmic derivative of the variable factor is
\[
-an+\frac{\eta nb}{t(t+nb)}.
\]
It decreases strictly from \(+\infty\) to \(-an\) and vanishes exactly at \(t(t+nb)=\eta b/a\), yielding the stated unique \(t_n\) and exact formula. Rationalizing the positive root gives \(t_n=\eta/(an)+O(n^{-3})\). Substitution proves the sharp asymptotic, including the \(O(n^{-2})\) relative remainder.

**2. Approximation numbers.** For each \(n\), the positive continuous input/output ratio approaches its supremum on some nonempty finite interval \(I\subset(0,\infty)\). Fix \(\varepsilon>0\) and take such an interval on which the ratio exceeds \(\|B_{a,b}^n\|-\varepsilon\). The weighted \(L^2(I)\) space has an infinite orthonormal sequence. Every finite-rank operator sends that weakly null sequence to a norm-null sequence, whereas \(B_{a,b}^n\) increases the norm of each vector by at least \(\|B_{a,b}^n\|-\varepsilon\). Thus \(\|B_{a,b}^n-F\|\ge\|B_{a,b}^n\|-\varepsilon\) for every finite-rank \(F\). Let \(\varepsilon\downarrow0\). This proves all approximation-number identities and noncompactness, without assuming the supremum is attained by an input function.

**3. Spectral regions.** When \(a,b>0\), the sharp power formula implies \(\lim_{n\to\infty}\|B_{a,b}^n\|^{1/n}=0\). Since every spectrum is nonempty and compact, \(\sigma(B_{a,b})=\{0\}\). Its Calkin image is nonzero by Step 2 but has spectral radius zero, hence its spectrum is also \(\{0\}\). When \(b=0<a\), the model is multiplication by \(e^{-at}\), so both spectra equal its nonatomic essential range \([0,1]\). If \(a=b=0\), the operator is the identity.

For \(a=0<b\), decompose \(t=r+kb\), with \(0<r<b\) and \(k\in\mathbb N_0\). The weighted-space unitary normalization gives on each fiber a unilateral shift whose weights are \(q_k(r)=((r+kb)/(r+(k+1)b))^\eta\). These weights approach \(1\). The full operator has norm \(1\), so its spectrum is contained in the unit disk. For each \(|\lambda|<1\), an adjoint eigenvector on every fiber with \(b/2<r<b\) has coordinates
\[
v_k(r)=\lambda^k\left(\frac{r+kb}{r}\right)^\eta v_0(r).
\]
They are square summable, uniformly on that interval, for any nonzero square-integrable \(v_0\). The adjoint eigenspace is infinite-dimensional, so \(B_{0,b}-\overline\lambda I\) is not Fredholm. Closure includes the unit circle; both spectra therefore equal the closed unit disk.

**4. Sharp boundary discontinuity.** For fixed \(b>0\) as \(a\downarrow0\), or fixed \(a>0\) as \(b\downarrow0\), the exact supremum formula is bounded by \(1\) and exceeds the value at each fixed \(t>0\); a two-step limit shows the norm tends to \(1\). But the spectral radius is \(0\) in the open quadrant and \(1\) on either positive axis. This is the claimed spectral-collapse boundary.

## Verification
Run `python CHECK.py` with Python 3; the checker independently evaluates the critical equation and strict optimizer inequality across positive parameters, reconstructs approximate \(L^2\) norm ratios using interval-supported inputs, and tests the large-power asymptotics and boundary cases. All theorems above are proved analytically. These finite tests are consistency checks only; they neither enumerate all parameters nor certify the spectrum.

## Relationship to prior work
Elliott and Wynn, *Composition operators on weighted Bergman spaces of a half plane* (arXiv:0910.0408v1), prove the norm–spectral-radius–essential-norm equality for **unweighted** composition operators and give the weighted Laplace representation used here. The exponential prefactor in the present operator changes the operator class and breaks that equality. Čučković and Zhao, *Weighted Composition Operators on the Bergman Space* (2004), give broad criteria for weighted composition on the **disk**, not an exact two-parameter half-plane spectrum or power norms. Petkova, *Wiener-Hopf operators and spectral problems on weighted \(L^2\) spaces* (arXiv:1106.4769v3), gives disk-spectrum results for weighted translation semigroups under positive bounded-shift-ratio conditions; the super-Gaussian transformed weight that produces the interior-quadrant operator here fails those conditions. The 1975 work of Petersen concerns weighted irrational rotations, not this absorbing half-line translation. Chalendar–Partington (arXiv:1910.01475) treat general iterates predominantly on the disk, with only unweighted half-plane composition in their relevant section, rather than these explicit power norms. Matache (2019) studies weighted composition and spectral questions on half-plane **Hardy** space, a different Hilbert scale; the complete historical text was not available for a claim-by-claim comparison, and Hardy-side spectral statements may anticipate part of the present boundary classification. These distinctions do not rule out an unlocated equivalent historical formulation.

## Limitations
The proof concerns only the explicit exponential multiplier and real nonnegative translation parameters on the Hilbert Bergman scale; no classification of general analytic weights or inducing maps is claimed. The assertion of originality is limited to examined primary sources and database comparisons; two broadly relevant weighted-composition papers' complete texts were unavailable. A finite checker does not prove the infinite-dimensional assertions. Independent verification has not been carried out.

## References
1. S. J. Elliott and A. Wynn, *Composition operators on weighted Bergman spaces of a half plane*, arXiv:0910.0408v1 (first publicly available 2009-10-02), Theorems 3.4–3.6 and Lemma 3.3. https://arxiv.org/abs/0910.0408
2. Ž. Čučković and R. Zhao, *Weighted Composition Operators on the Bergman Space*, J. London Math. Soc. 70 (2004), 499–511. https://doi.org/10.1112/S0024610704005605
3. V. Petkova, *Wiener-Hopf operators and spectral problems on weighted \(L^2\) spaces*, arXiv:1106.4769v3 (2012), Theorem 3. https://arxiv.org/abs/1106.4769
4. K. Petersen, *The spectrum and commutant of a certain weighted translation operator*, Math. Scand. 37 (1975), 297–306. https://doi.org/10.7146/math.scand.a-11608
5. I. Chalendar and J. R. Partington, *Weighted composition operators: isometries and asymptotic behaviour*, arXiv:1910.01475 (2019), especially §§2 and 4.2. https://arxiv.org/abs/1910.01475
6. V. Matache, *Weighted composition operators on the Hilbert Hardy space of a half-plane*, Complex Variables and Elliptic Equations 65 (2020), 498–524 (first online 2019-05-23). https://doi.org/10.1080/17476933.2019.1594206
7. I. Chalendar and J. R. Partington, *Composition operators on function spaces on the halfplane: spectra and semigroups*, arXiv:2204.05894. https://arxiv.org/abs/2204.05894
