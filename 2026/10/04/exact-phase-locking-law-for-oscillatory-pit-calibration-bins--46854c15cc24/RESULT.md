# Exact phase-locking law for oscillatory PIT calibration bins
## Finding
Let \(q(v)=1+a\cos(2\pi k v)\) on \([0,1]\), where \(k\ge1\) is an integer and \(0<a<1\), and let \(\varepsilon_\infty=\int_0^1|q(v)-1|\,dv=2a/\pi\). For \(N\ge1\) and an origin offset \(\tau\in[0,1/N)\), partition the circle into \(N\) equal bins \(B_j(\tau)=[\tau+(j-1)/N,\tau+j/N)\) modulo one, and define the population binned discrepancy \(E_N(\tau)=\sum_{j=1}^N|\int_{B_j(\tau)}q(v)\,dv-1/N|\). Then exactly \[E_N(\tau)=\frac{a}{\pi k}\left|\sin\frac{\pi k}{N}\right|\sum_{j=1}^N\left|\cos\left(2\pi k\left(\tau+\frac{j-1/2}{N}\right)\right)\right|.\] Its uniformly randomized-origin mean is exactly \(N\int_0^{1/N}E_N(\tau)\,d\tau=\varepsilon_\infty|\operatorname{sinc}(k/N)|\), with \(\operatorname{sinc}(x)=\sin(\pi x)/(\pi x)\). For the standard aligned grid \(\tau=0\), put \(g=\gcd(k,N)\), \(m=N/g\), and \(r=k/g\). Then \[\frac{E_N(0)}{\varepsilon_\infty}=\frac{|\sin(\pi r/m)|}{2r}A_m,\] where \(A_m=\csc(\pi/(2m))\) for odd \(m\), \(A_m=2\csc(\pi/m)\) for \(m\equiv0\pmod4\), and \(A_m=2\cot(\pi/m)\) for \(m\equiv2\pmod4\). Consequently \(E_N(0)=0\) if and only if \(N\mid2k\). In particular, at the nominal critical resolution \(N=2k\), the standard aligned equal-width grid is exactly blind, while \(E_{2k}(\tau)=\varepsilon_\infty|\sin(2\pi k\tau)|\); a half-bin shift \(\tau=1/(4k)\) recovers the full continuous discrepancy, and the uniform-origin average is \(2\varepsilon_\infty/\pi\). Thus the approximately \(64\%\) sinc attenuation reported for this benchmark at \(N=2k\) is the exact randomized-origin mean, not the value of the standard aligned grid.

## Assumptions and scope
The object is the oscillatory probability-integral-transform density \(q(v)=1+a\cos(2\pi k v)\) on \([0,1]\), with integer frequency \(k\ge1\) and amplitude \(0<a<1\). The continuous population \(L^1\) calibration discrepancy is \(\varepsilon_\infty=2a/\pi\). Equal-width bins are taken on the unit circle so that an origin shift changes only phase and does not create endpoint artifacts; the standard histogram grid is the special case \(\tau=0\).

The result is a population identity. It does not claim a finite-sample testing law, a minimax sample-complexity theorem, or optimality of any data-dependent bin choice.

## Proof
For the \(j\)-th shifted bin, direct integration gives
\[
\int_{B_j(\tau)}q(v)\,dv-\frac1N
=\frac{a}{2\pi k}\left[\sin(2\pi k v)\right]_{\tau+(j-1)/N}^{\tau+j/N}.
\]
Using the sine-difference identity yields
\[
\int_{B_j(\tau)}q(v)\,dv-\frac1N
=\frac{a}{\pi k}\sin\left(\frac{\pi k}{N}\right)
\cos\left(2\pi k\left(\tau+\frac{j-1/2}{N}\right)\right).
\]
Taking absolute values and summing proves the first exact formula.

For the randomized-origin identity, average \(E_N(\tau)\) over one bin-width of offsets. The translated midpoint intervals tile one full period modulo one, so
\[
N\int_0^{1/N}\sum_{j=1}^N
\left|\cos\left(2\pi k\left(\tau+\frac{j-1/2}{N}\right)\right)\right|d\tau
=N\int_0^1|\cos(2\pi k x)|\,dx=\frac{2N}{\pi}.
\]
Multiplying by the prefactor gives
\[
N\int_0^{1/N}E_N(\tau)\,d\tau
=\frac{2a}{\pi}\frac{|\sin(\pi k/N)|}{\pi k/N}
=\varepsilon_\infty|\operatorname{sinc}(k/N)|.
\]

Now take the standard aligned grid. Write \(g=\gcd(k,N)\), \(m=N/g\), and \(r=k/g\). The absolute-cosine sum consists of \(g\) copies of a reduced \(m\)-point sum. If \(m\) is odd, multiplication by the coprime residue \(r\) permutes all residue classes modulo \(m\), and the elementary symmetric cosine sum is
\[
\sum_{s=0}^{m-1}|\cos(\pi s/m)|=\csc\left(\frac{\pi}{2m}\right).
\]
If \(m\) is even, then \(r\) is odd and the odd residue classes modulo \(2m\) are permuted; pairing symmetric terms and summing the resulting finite geometric progression gives
\[
\sum_{\substack{1\le s<2m\\ s\text{ odd}}}|\cos(\pi s/m)|
=\begin{cases}
2\csc(\pi/m),&m\equiv0\pmod4,\\
2\cot(\pi/m),&m\equiv2\pmod4.
\end{cases}
\]
Substitution into the first formula proves the stated \(A_m\) law.

For \(m\ge3\), the reduced coprimality condition implies \(|\sin(\pi r/m)|>0\), and every listed \(A_m\) is positive. The only zero cases are therefore \(m=1\) or \(m=2\), equivalently \(N/g\mid2\), which is exactly \(N\mid2k\). At \(N=2k\), the midpoint phases are all congruent modulo sign, and the general shifted formula reduces to
\[
E_{2k}(\tau)=\varepsilon_\infty|\sin(2\pi k\tau)|.
\]
Hence \(\tau=0\) gives zero, while \(\tau=1/(4k)\) gives \(\varepsilon_\infty\). Averaging the last identity over one bin-width gives \(2\varepsilon_\infty/\pi\).

## Verification
The proof is symbolic and finite. As a supplementary stress check, the exact bin-integral expression was compared against the closed arithmetic formula for integer frequencies through multiple small \(k\) and \(N\) values, including all blindness cases in the tested range, and the phase-average identity was numerically integrated for several coprime and non-coprime pairs. These checks agreed with the analytic formulas; they are not used as proof.

Critical boundary cases are explicit: \(N=1\) is blind for every integer frequency because the sole bin is the whole interval; \(N=2\) is blind for every integer \(k\); and the restriction \(0<a<1\) makes \(q\) a strictly positive density.

## Relationship to prior work
Kipnis's recent calibration-testing note studies this same oscillatory PIT benchmark and reports the approximation \(\mathrm{ECE}_1^{(N)}\approx\varepsilon_\infty|\operatorname{sinc}(k/N)|\), including roughly \(64\%\) retention at \(N=2k\). The associated full workshop paper uses the same benchmark and interpretation. The identity above shows that the sinc expression is exactly the average over a uniformly randomized bin origin, whereas the standard aligned grid has an arithmetic phase law and is exactly blind at \(N=2k\).

General calibration-binning literature studies binning bias, consistency, and smooth alternatives, but the checked sources did not state this exact finite-frequency origin-phase law, the divisibility criterion \(N\mid2k\), or the interpretation of the sinc curve as the randomized-origin mean.

## Limitations
The theorem concerns a single-frequency cosine perturbation and equal-width circular bins. It does not classify multi-frequency mixtures, adaptive bins, or finite-sample empirical ECE. The originality comparison cannot exclude an equivalent elementary aliasing identity in older signal-processing or quadrature terminology; that remains the main residual literature risk.

## References
1. A. Kipnis, *Why Constants Matter in Distribution Testing: From Uniformity to Calibration*, arXiv:2607.08378v1, first public 2026-07-09.
2. A. Kipnis, *Calibrating the Calibration Tester: Optimal Binning and Minimax Calibration Testing for Continuous Predictive Models*, 2026 workshop manuscript, OpenReview identifier dy7XNC3W0g.
3. F. Futami and M. Fujisawa, *Information-theoretic Generalization Analysis for Expected Calibration Error*, arXiv:2405.15709, 2024.
