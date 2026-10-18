# Arbitrarily many Fourier-ratio peaks under periodic heat flow

## Finding

Define the Fourier ratio of a nonzero trigonometric polynomial on the circle by
\[
\mathcal R(f)=\frac{\sum_{n\in\mathbb Z}|\widehat f(n)|}{\bigl(\sum_{n\in\mathbb Z}|\widehat f(n)|^2\bigr)^{1/2}},
\qquad \widehat f(n)=\frac1{2\pi}\int_0^{2\pi}f(x)e^{-inx}\,dx.
\]
The following two conclusions hold for the ordinary periodic heat semigroup \(H_t=e^{t\partial_x^2}\).

**Oscillatory complexity.** For every integer \(K\ge1\) and every \(T>0\), there is a real-valued, mean-zero trigonometric polynomial \(f\) such that \(t\mapsto\mathcal R(H_tf)\) has at least \(K\) distinct **strict local maxima** and at least \(K-1\) distinct strict local minima in \((0,T)\). There is an explicit \((K+1)\)-cosine construction with prescribed comparison times, at which the ratio is respectively greater than \(1.99\) and less than \(1.43\).

**Unbounded transient amplification.** For every \(B>1\) and every \(T>0\), there are a real-valued, mean-zero trigonometric polynomial \(g\) and a time \(0<t_*<T\) with
\[
\mathcal R(H_{t_*}g)>B\,\mathcal R(g).
\]
Thus even for real analytic initial data on the circle, Fourier-ratio complexity under heat evolution need not decrease, need not be unimodal, and admits no signal-independent transient amplification bound.

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), its Laplacian is \(\partial_x^2\), and the Fourier basis is \(e^{inx}\). All polynomials have finitely many nonzero Fourier coefficients. In particular, their Fourier ratios are well defined at every finite time, and the heat evolution is exact coefficientwise multiplication by \(e^{-n^2t}\).

For the oscillation assertion put \(m=K+1\) and choose any positive integer \(L\) for which
\[
\eta=\exp\bigl(-3L^2T/(2m)\bigr)\le \frac1{100m}.
\]
For \(2\le j\le m\), set
\[
\tau_j=\frac{m-j+1}{m}T,\quad \lambda_j=j^2L^2,
\quad a_1=1,\quad
 a_j=\exp\!\left(\sum_{h=2}^j(\lambda_h-\lambda_{h-1})\tau_h\right).
\]
An explicit admissible polynomial is
\[
f(x)=2\sum_{j=1}^{m}a_j\cos(jLx).
\]
No uniform coefficient-size, Sobolev-norm, or frequency-bandwidth constraint is imposed; any such constraint would require a separate theorem.

## Proof

**1. Exact Fourier-ratio reduction.** The only Fourier coefficients of \(f\) are \(\widehat f(\pm jL)=a_j\). If \(b_j(t)=a_je^{-\lambda_jt}>0\), then
\[
R(t):=\mathcal R(H_tf)=\sqrt2\frac{\sum_{j=1}^{m}b_j(t)}{\bigl(\sum_{j=1}^{m}b_j(t)^2\bigr)^{1/2}}.
\tag{1}
\]
The logarithmic amplitude differences satisfy
\[
\log\frac{b_j(t)}{b_{j-1}(t)}
=(\lambda_j-\lambda_{j-1})(\tau_j-t),\qquad 2\le j\le m.
\tag{2}
\]
All spectral gaps are at least \(3L^2\), and consecutive times \(\tau_j\) are spaced by \(T/m\).

**2. High comparison points.** At \(t=\tau_j\), identity (2) gives \(b_{j-1}=b_j=:B_j\). For \(i<j-1\), applying (2) along the intermediate indices gives \(b_i\le\eta^2 B_j\), because the intervening crossing times exceed \(\tau_j\) by at least \(T/m\). The same bound holds for \(i>j\), because their crossing times precede \(\tau_j\) by at least \(T/m\). Consequently (1) yields
\[
R(\tau_j)\ge\frac{2}{\sqrt{1+(m-2)\eta^4/2}}>1.99.
\tag{3}
\]
The strict numerical bound follows from \(\eta\le1/(100m)\), for all \(m\ge2\).

**3. Low comparison points.** Use the two endpoint times \(0\) and \(T\), and, for \(2\le j\le m-1\), the interior midpoint \(v_j=(\tau_j+\tau_{j+1})/2\). The increasing chronological order is \(0,\tau_m,v_{m-1},\tau_{m-1},\ldots,v_2,\tau_2,T\) when \(m\ge3\). At each interior \(v_j\), mode \(j\) dominates: by (2), all other amplitudes are at most \(\eta b_j(v_j)\). At time zero mode \(m\) dominates, and at time \(T\) mode \(1\) dominates, with the same bound. Therefore at every listed low comparison point \(v\),
\[
R(v)\le\sqrt2\,[1+(m-1)\eta]<1.43.
\tag{4}
\]
When \(m=2\), the only comparison times are \(0,\tau_2,T\).

**4. Oscillation count.** There are \(m-1\) distinct crossing times \(\tau_m<\tau_{m-1}<\cdots<\tau_2\), each strictly between two consecutive low comparison points. By (3)--(4), the continuous function \(R\) attains an interior maximum in each corresponding closed interval. Formula (1) is positive and real analytic for real \(t\), and is not constant, so each maximum can be chosen strict. This gives at least \(m-1=K\) distinct strict local maxima in \((0,T)\). Between each two successive maxima, (4) forces an interior strict minimum, hence at least \(m-2=K-1\) distinct strict local minima. As \(L\to\infty\) with \(m,T\) fixed, the crossing values tend to \(2\) and all low comparison values tend to \(\sqrt2\).

**5. Arbitrary transient amplification.** Fix \(0<t_*<T\) and an integer \(q\ge2\). For an integer \(L>0\), take
\[
g_L(x)=2\sum_{j=1}^{q}e^{j^2L^2t_*}\cos(jLx).
\]
At \(t=t_*\), all \(q\) positive-frequency amplitudes (and their negative-frequency partners) are equal. Thus
\[
\mathcal R(H_{t_*}g_L)=\sqrt{2q}\quad\text{exactly}.
\]
At \(t=0\), the largest-frequency pair dominates as \(L\to\infty\), so \(\mathcal R(g_L)\to\sqrt2\). Hence the amplification tends to \(\sqrt q\). Choose \(q>B^2\) and then sufficiently large \(L\). This proves the remaining assertion.

## Verification

The accompanying independent coefficient-space/physical-grid checker uses exact rational crossing-time identities and discrete Fourier transforms of sampled, rescaled heat snapshots. It returned `VERIFY_OK: 197 checks`. It tests the strict high/low inequalities and the number of separated comparison intervals for \(2\le m\le8\), an unaliased Fourier grid, and several large-amplification constructions. These finite tests corroborate, but do not replace, the all-\(K\), all-\(T\) analytic proof above. To run it, execute `python checker.py` with NumPy installed.

For one transparent instance take \(K=3\), \(T=1\), \(L=12\). Then \(m=4\), the crossing times are \(1/4,1/2,3/4\), the corresponding logarithms of the initial positive-frequency coefficients are \(0,324,684,936\), and the ratio approaches \(2\) at crossings versus \(\sqrt2\) at the separating midpoints.

## Relationship to prior work

Iosevich, Iosevich, Palsson and Yavicoli (2026), *PDE propagation, sampling, and the Fourier ratio* (arXiv:2603.07851; first public March 8, 2026), obtain **a priori heat-snapshot Fourier-ratio bounds** used to control sufficient random-sampling budgets at fixed positive time. The present result concerns the actual ratio **along a single individual heat trajectory**: it proves that pointwise monotonicity or even unimodality cannot follow merely from heat-frequency damping. It does not contradict the cited paper's stated fixed-time upper-bound theorems, which depend on regularity and nondegeneracy parameters.

Iosevich, Palsson and Yavicoli (2026), *Discretization, sampling, and the Fourier ratio* (arXiv:2601.17493), develop the underlying smoothness-to-recovery mechanism without proving a temporal monotonicity theorem. Aldaleh and collaborators (2025), *The Fourier Ratio and complexity of signals* (arXiv:2511.19560), analyze approximation and complexity for Fourier-ratio classes, not this heat-flow trajectory. Iosevich, Hovhannisyan, Keyshams and Vagharshakyan (2026), *Metric entropy of Fourier ratio classes on \(\mathbb Z_N\)* (arXiv:2606.24229), treat stationary class-level entropy and sampling rather than repeated temporal extrema. These distinctions compare mathematical implications, not title similarity.

## Limitations

The examples use arbitrarily large Fourier bandwidth and highly unequal positive Fourier amplitudes. They establish the absence of universal trajectorywise monotonicity, unimodality, or signal-independent amplification bounds without extra constraints; they do **not** rule out controlled behavior for fixed spectral bandwidth, coefficient dynamic range, Sobolev norm ratio, or for fixed-time bounds that depend on such parameters. The construction says nothing about how many actual sensors a particular reconstruction algorithm will require. Unindexed equivalent examples in general spectral exponential families remain a historical-priority risk; independent mathematical review is not included.

## References

1. A. Iosevich, J. Iosevich, E. Palsson, A. Yavicoli, *PDE propagation, sampling, and the Fourier ratio*, arXiv:2603.07851 (first public March 8, 2026), https://arxiv.org/abs/2603.07851.
2. A. Iosevich, E. Palsson, A. Yavicoli, *Discretization, sampling, and the Fourier ratio*, arXiv:2601.17493 (first public January 24, 2026), https://arxiv.org/abs/2601.17493.
3. K. Aldaleh et al., *The Fourier Ratio and complexity of signals*, arXiv:2511.19560 (first public November 24, 2025), https://arxiv.org/abs/2511.19560.
4. A. Iosevich, V. Hovhannisyan, Z. Keyshams, A. Vagharshakyan, *Metric entropy of Fourier ratio classes on \(\mathbb Z_N\)*, arXiv:2606.24229 (first public June 23, 2026), https://arxiv.org/abs/2606.24229.
