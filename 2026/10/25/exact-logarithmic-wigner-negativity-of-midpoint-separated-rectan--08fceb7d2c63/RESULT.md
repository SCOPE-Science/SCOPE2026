# Exact logarithmic Wigner negativity of midpoint-separated rectangular pulse trains

## Finding

The negative phase-space volume of a coherent train of nonoverlapping top-hat pulses grows logarithmically with the frequency cutoff. Under the **pair-midpoint separation** condition, its leading coefficient has the explicit, phase-independent and center-independent form

\[
\mathcal N_\psi(R)=\left(\frac{2}{\pi^2}+\frac{8}{\pi^3}\frac{\sum_{j<k}|a_ja_k|}{\sum_j|a_j|^2}\right)\log R+O_\psi(1).
\]

The interference contribution comes from every unordered pair of pulses. For \(N\) pulses of equal magnitude the coefficient is exactly \(2/\pi^2+4(N-1)/\pi^3\). In this family, the coefficient is maximized precisely by equal-magnitude amplitudes and can be made arbitrarily large by increasing the finite number of pulses.

## Assumptions and scope

Choose any pulse length \(\ell>0\), positive integer \(N\), pairwise distinct real centers \(c_1,\ldots,c_N\), and nonzero complex amplitudes \(a_1,\ldots,a_N\). For every unordered index pair \((j,k)\), \(1\le j\le k\le N\), define its midpoint \(m_{jk}=(c_j+c_k)/2\). Assume that

\[
|m_{jk}-m_{uv}|>\ell
\]

whenever \((j,k)\ne(u,v)\) are unordered pairs. In particular, the original pulse intervals are pairwise disjoint. This is a nonempty family for every finite \(N\); for example \(c_j=10^{j-1}\ell\), \(1\le j\le N\), works, because distinct unordered base-ten two-digit sums are separated by at least \(\ell\) and in this example strictly more.

Put \(S=\sum_j|a_j|^2\) and normalize the wavefunction by

\[
\psi(x)=\frac{1}{\sqrt{\ell S}}\sum_{j=1}^{N}a_j\mathbf1_{[c_j-\ell/2,c_j+\ell/2]}(x),\qquad \|\psi\|_2=1.
\]

Use the cycles-frequency Wigner convention

\[
W_\psi(x,\xi)=\int_{\mathbb R}\psi(x+t/2)\overline{\psi(x-t/2)}e^{-2\pi i\xi t}\,dt,
\]

and define the truncated *negative* volume, rather than its doubled version, by

\[
\mathcal N_\psi(R)=\int_{\mathbb R}\int_{-R}^{R}\max\{-W_\psi(x,\xi),0\}\,d\xi\,dx\quad(R>0).
\]

All integrals at finite \(R\) are finite. The remainder may depend on the fixed pulse geometry, amplitudes and length. No uniformity is asserted as centers coalesce or \(N\) grows.

## Proof

**1. Exact decomposition into disjoint midpoint channels.** For each unordered pair let

\[
r_{jk}(x)=\ell-2|x-m_{jk}|.
\]

The \((j,k)\) term of the Wigner integral is supported where \(|x-m_{jk}|<\ell/2\), with its integration variable \(t\) ranging over an interval centered at \(c_j-c_k\) and of half-length \(r_{jk}(x)\). Its Fourier integral is \(e^{-2\pi i(c_j-c_k)\xi}\sin(2\pi\xi r_{jk}(x))/(\pi\xi)\). The value at \(\xi=0\) is understood by continuity. Combining conjugate ordered pairs gives, on these disjoint spatial channels,

\[
W_\psi(x,\xi)=\frac{\sin(2\pi\xi r_{jj}(x))}{\pi\ell S\xi}|a_j|^2\quad\text{in channel }(j,j),
\]

\[
W_\psi(x,\xi)=\frac{2\sin(2\pi\xi r_{jk}(x))}{\pi\ell S\xi}\operatorname{Re}\!\left(a_j\overline{a_k}e^{-2\pi i(c_j-c_k)\xi}\right)\quad\text{in channel }(j,k),\ j<k,
\]

and it vanishes outside their union. The hypothesis that all channel centers differ by more than \(\ell\) is what lets us take an absolute value separately in each channel. Mere separation of the original pulses would not suffice for \(N\ge3\).

**2. Exact spatial absolute integral.** Let

\[
J_\ell(\xi)=\int_0^\ell|\sin(2\pi s\xi)|\,ds,
\qquad A=\sum_{j<k}|a_ja_k|.
\]

Since the substitution \(s=\ell-2|x-m_{jk}|\) has two branches, each with Jacobian \(1/2\), integrating an absolute sine over a channel yields exactly \(J_\ell(\xi)\). Writing \(\vartheta_{jk}=\arg(a_j\overline{a_k})\), for every \(\xi\ne0\) we obtain

\[
\int_{\mathbb R}|W_\psi(x,\xi)|\,dx
=\frac{J_\ell(\xi)}{\pi\ell S|\xi|}\left[S+2\sum_{j<k}|a_ja_k|\,|\cos(2\pi(c_j-c_k)\xi-\vartheta_{jk})|\right].
\]

This identity, not a heuristic frequency average, is the starting point for the asymptotic.

**3. Two periodic averages with bounded errors.** Because the mean of \(|\sin u|\) over a period is \(2/\pi\), periodic integration with at most one incomplete period gives

\[
J_\ell(\xi)=\frac{2\ell}{\pi}+O(|\xi|^{-1}),\qquad |\xi|\ge1.
\]

Likewise, for each nonzero fixed \(d\) and real \(\vartheta\), \(|\cos(2\pi d\xi+\vartheta)|-2/\pi\) is periodic, has zero mean, and admits a bounded primitive. Integration by parts therefore yields, at either sign of frequency,

\[
\int_1^R\frac{|\cos(2\pi d\xi+\vartheta)|}{\xi}\,d\xi=\frac2\pi\log R+O_{d,\vartheta}(1).
\]

The \(O(|\xi|^{-1})\) error in the sine average contributes only \(O(1)\) to the frequency integral after multiplication by \(1/|\xi|\). Integrating the exact identity above over both positive and negative frequencies gives

\[
\int_{-R}^{R}\int_{\mathbb R}|W_\psi(x,\xi)|\,dx\,d\xi
=\left(\frac4{\pi^2}+\frac{16A}{\pi^3S}\right)\log R+O_\psi(1).
\]

The compact region \(|\xi|\le1\) contributes a finite constant, including at \(\xi=0\).

**4. Signed mass and negativity.** The Wigner marginal identity under the stated Fourier convention is

\[
\int_{\mathbb R}W_\psi(x,\xi)\,dx=|\widehat\psi(\xi)|^2.
\]

By Plancherel and \(\|\psi\|_2=1\), the integral of this signed marginal over \([-R,R]\) is between zero and one. Since \(\max\{-w,0\}=(|w|-w)/2\) for real \(w\), the negative volume is one half of the preceding absolute integral up to a uniformly bounded correction. This proves the stated coefficient and bounded remainder.

**5. Sharp amplitude bound.** The Cauchy–Schwarz inequality gives \((\sum_j|a_j|)^2\le NS\). As \(2A=(\sum_j|a_j|)^2-S\), one has \(A/S\le(N-1)/2\), with equality if and only if \(|a_1|=\cdots=|a_N|\). Substitution proves the sharp fixed-\(N\) upper bound. Taking \(N\) arbitrarily large in the displayed ten-power center construction proves unboundedness of the family of attainable leading coefficients.

## Verification

The companion `verify.py` independently evaluates the original Wigner integral by intersecting the two translated pulse intervals and compares it with the channel formula for finite examples. It also compares the exact spatial integral of the absolute Wigner function with numerical integration over each channel and reports the predicted logarithmic slopes for one, two, three, and seven pulses. `integral_check.py` separately computes the truncated negative volume by frequency quadrature and compares decade-difference slopes with the analytic coefficient for one, two and three pulses. Running `python verify.py` and `python integral_check.py` with NumPy version 2 or later reproduces `verify_output.txt` and `integral_output.txt`. These finite tests are not proofs of the unbounded-frequency asymptotic, whose proof appears above.

## Relationship to prior work

Kenfack and Życzkowski (2004) defined and studied integrated Wigner negativity for Fock and Gaussian-cat states. Keating, Steege and Pattanayak (2008) demonstrated that the unsmoothed negative volume of infinite-square-well eigenstates can diverge and studied Gaussian coarse graining; their Sec. “The Square Well” exhibits the divergent one-dimensional momentum tail. Neither source states the pair-separated rectangular train coefficient obtained here. Sala Mayato, Loughlin and Cohen (2018), Secs. 6–7, analyze Wigner cross terms and moment-indeterminacy for separated wavefunctions, including multiple components, but do not calculate negative-volume cutoff asymptotics. These results supply real ingredients, particularly the cross-Wigner decomposition, but no inspected source implies the new exact coefficient or the sharp equal-amplitude maximization without further analysis.

## Limitations

The theorem assumes a hard rectangular profile of common length and strictly separated *all unordered-pair midpoints*. When the midpoint channels overlap, absolute values cannot generally be separated; the stated coefficient need not hold. The asymptotic concerns a sharp symmetric cutoff in cycles-frequency, not spatial Gaussian smoothing. The result makes no claim that the negative volume itself is finite as the cutoff is removed; in fact, the strictly positive coefficient proves it is infinite. The cutoff remainder is only \(O_\psi(1)\), without a universal constant or convergence claim. Publication priority has not been independently certified; an equivalent result in older time-frequency literature may exist.

## References

1. A. Kenfack and K. Życzkowski, “Negativity of the Wigner function as an indicator of nonclassicality,” arXiv:quant-ph/0406015v1 (first public 2004-06-02), https://arxiv.org/abs/quant-ph/0406015.
2. T. E. Keating, A. T. C. Steege and A. K. Pattanayak, “Negativity of the Coarse Grained Wigner Function as a Measure of Quantal Behavior,” arXiv:0811.2924v1 (first public 2008-11-18), https://arxiv.org/abs/0811.2924.
3. R. Sala Mayato, P. Loughlin and L. Cohen, “M-indeterminate distributions in quantum mechanics and the non-overlapping wave function paradox,” arXiv:1807.11725v1 (first public 2018-07-31), https://arxiv.org/abs/1807.11725.
