# Odd-over-even squeezing resonances and exact distinct Gabor-zero densities for three Gaussian scales

## Finding

For any three **distinct** positive scales \(a_1>a_2>a_3>0\) and **strictly positive** real coefficients \(c_1,c_2,c_3\), define the normalized Gaussians \(h_a(t)=(2a)^{1/4}e^{-\pi a t^2}\), the signal \(f=\sum_{j=1}^3c_jh_{a_j}\), and its short-time Fourier transform with Gaussian window \(g=h_1\):
\[
V_gf(x,\nu)=\int_{\mathbb R}f(t)g(t-x)e^{-2\pi i\nu t}\,dt.
\]
Write
\[
\mu_j=\frac{\pi(1-a_j)}{2(1+a_j)},\quad d_j=\frac{(4a_j)^{1/4}}{\sqrt{1+a_j}},\quad
\alpha=\mu_2-\mu_1,\quad\beta=\mu_3-\mu_1,
\]
so \(0<\alpha<\beta\), and set \(A=c_1d_1>0\), \(B=c_2d_2>0\), \(C=c_3d_3>0\). All Gabor zeros are isolated and have multiplicity **at most two**. Multiple zeros occur **if and only if** both of the following hold:

\[
\boxed{\frac{\alpha}{\beta}=\frac pq\ \text{in lowest terms, with }p\text{ odd and }q\text{ even},}
\]
\[
\boxed{\frac1\alpha\log\frac{A\beta}{B(\beta-\alpha)}=\frac1\beta\log\frac{A\alpha}{C(\beta-\alpha)}.}
\]
At such a resonance, **infinitely many** Gabor zeros are double, their entire set is explicit, and all other zeros are simple. There are no triple or higher-order zeros.

For \(R>0\), let \(N_{\rm mult}(R)\) count zeros of \(V_gf\) inside \(x^2+\nu^2\le R^2\) with analytic multiplicity, and let \(N_{\rm distinct}(R)\) count their distinct locations. Then
\[
\boxed{N_{\rm mult}(R)=\frac{2\beta}{\pi}R^2+O_f(1),}
\]
whereas
\[
\boxed{N_{\rm distinct}(R)=\begin{cases}
\frac{2\beta}{\pi}\left(1-\frac1q\right)R^2+O_f(1),&\text{when both resonance tests hold},\\
\frac{2\beta}{\pi}R^2+O_f(1),&\text{otherwise}.
\end{cases}}
\]
In particular, on the resonance surface the *leading distinct-zero density* loses exactly the fraction \(1/q\); the usual multiplicity-weighted density never changes. The density is independent of the middle Gaussian width and the amplitudes, except for this explicit arithmetic multiplicity correction.

## Assumptions and scope

All widths are positive and ordered strictly, and all three signal coefficients are positive real numbers. The complex frequency variable in the Bargmann representation is \(z=x-i\nu\), so Euclidean radii in the Gabor plane equal \(|z|\). Zero multiplicity means the holomorphic zero order of the nonvanishing-factor-normalized Bargmann transform; it is well-defined for the Gaussian-window STFT. The constants implicit in \(O_f(1)\) depend on the fixed widths and amplitudes. The result does not assert uniformity as widths collide or a coefficient approaches zero.

## Proof

**1. Exact Gaussian transform and reduction.** With normalization
\[
\mathcal Bf(z)=2^{1/4}\int_{\mathbb R}f(t)e^{2\pi tz-\pi t^2-\pi z^2/2}\,dt,
\]
completion of the square gives
\[
\mathcal Bh_a(z)=\frac{(4a)^{1/4}}{\sqrt{1+a}}\exp\left(\frac{\pi(1-a)}{2(1+a)}z^2\right)=d_a e^{\mu(a)z^2}.
\]
The well-known nonvanishing STFT/Bargmann factor identifies its zeros with those of \(\mathcal Bf(x-i\nu)\), up to a reflection of the frequency coordinate. Hence
\[
\mathcal Bf(z)=e^{\mu_1 z^2}G(z^2),\qquad G(w)=A+Be^{\alpha w}+Ce^{\beta w}.
\]
Because \(G(0)=A+B+C>0\), no zero is at \(z=0\). The substitution \(w=z^2\) therefore takes each zero of \(G\) to exactly two nonzero Gabor zeros and preserves its order.

**2. Exhaustive multiplicity test.** At a multiple zero \(w\), both \(G(w)=0\) and \(G'(w)=0\). Solving the two equations linearly for the exponentials yields the *necessary and sufficient* identities
\[
Be^{\alpha w}=-\frac{A\beta}{\beta-\alpha},\qquad
Ce^{\beta w}=\frac{A\alpha}{\beta-\alpha}.
\]
Their moduli have a common real solution \(\operatorname{Re}w=x_*\) precisely when
\[
x_*:=\frac1\alpha\log\frac{A\beta}{B(\beta-\alpha)}
=\frac1\beta\log\frac{A\alpha}{C(\beta-\alpha)}.
\]
Their phases require \(\alpha\operatorname{Im}w\in\pi(2\mathbb Z+1)\) and \(\beta\operatorname{Im}w\in2\pi\mathbb Z\). This simultaneous congruence is soluble exactly when \(\alpha/\beta=p/q\) is reduced with odd numerator \(p\) and even denominator \(q\). In that case every multiple zero is
\[
\boxed{w_j=x_*+\frac{\pi i q}{\beta}(2j+1),\quad j\in\mathbb Z,}
\]
with corresponding Bargmann/Gabor zeros \(z=\pm\sqrt{w_j}\) (convert back to \((x,\nu)\) by \(z=x-i\nu\)). At each such \(w_j\),
\[
G''(w_j)=B\alpha^2e^{\alpha w_j}+C\beta^2e^{\beta w_j}=A\alpha\beta\ne0.
\]
Thus each has order exactly two. Outside this set, every zero has order one; higher multiplicities cannot occur.

**3. All-zero counting with a bounded error.** This argument is included to avoid relying on an unquoted zero-distribution theorem. Choose \(M\) large enough that \(A\) dominates the other terms on \(\operatorname{Re}w=-M\), and \(Ce^{\beta w}\) dominates on \(\operatorname{Re}w=M\), each by a strict factor exceeding two. All zeros lie within the vertical strip \(|\operatorname{Re}w|<M\). Apply the argument principle to the rectangle bounded by these two vertical lines and \(\operatorname{Im}w=\pm T\), initially choosing heights that avoid zeros. The change of argument on the left vertical side is \(O(1)\), while the change on the right vertical side is \(2\beta T+O(1)\).

On each horizontal side, the imaginary part of an arbitrary fixed rotation of \(G(x+iT)\) is a real linear combination of \(1,e^{\alpha x},e^{\beta x}\). This three-dimensional extended Chebyshev system has at most two real zeros unless that imaginary part is identically zero. Therefore a continuous argument of the nonvanishing horizontal boundary has net argument change bounded by a constant independent of \(T\); in the identically zero case its argument is constant. The argument principle gives
\[
\#\{G(w)=0:|\operatorname{Im}w|\le T\}=\frac{\beta}{\pi}T+O(1)
\]
with multiplicity. The strip bound and the same uniform strip count imply that replacing \(|\operatorname{Im}w|\le T\) by \(|w|\le T\) changes this by \(O(1)\): for \(T>2M\), the two regions differ only in horizontal slabs of thickness at most \(M^2/T\), whose zero counts are uniformly bounded by applying the rectangle estimate at nearby heights. Thus \(\#\{G(w)=0:|w|\le T\}=\beta T/\pi+O(1)\). The map \(w=z^2\) gives the stated full multiplicity count with \(T=R^2\).

**4. The distinct-zero correction.** On a resonance, \(w_j\) is a vertical arithmetic progression of step \(2\pi q/\beta\). It contributes \(\beta T/(\pi q)+O(1)\) double zeros to \(|w|\le T\). Each lifted nonzero zero contributes two distinct positions in the \(z\)-plane, and each double position contributes one to the difference between multiplicity-weighted and distinct counting. Therefore
\[
N_{\rm mult}(R)-N_{\rm distinct}(R)=\frac{2\beta}{\pi q}R^2+O(1).
\]
Without a resonance there are no multiple zeros and the two counting functions coincide. This proves the theorem.

## Verification

The accompanying `check.py` performs independent high-precision Gaussian integral comparisons, exact symbolic greatest-common-divisor tests for the resonant exponent ratios \(1/2\) and \(1/4\) and the nonresonant ratio \(1/3\), and checks seven explicit double zeros including \(G''(w_j)=A\alpha\beta\). It also uses the exact rational-polynomial reduction in three commensurate examples to compare weighted and distinct counts at three cutoffs. The saved output is in `checker_output.txt`. These finite checks supplement but cannot certify the infinite counting law.

## Relationship to prior work

Zhang (2006), arXiv:quant-ph/0604128v1, constructs and studies coherent superpositions of squeezed vacua, including their photon-number parity. It motivates the positive three-scale Gaussian family but does not give a Gabor-zero multiplicity/density classification. Cappiello, Rodino and Toft (2014), arXiv:1403.4474v1, characterize quadratic-composition Bargmann transforms under radial symmetry; the present analysis uses explicit Gaussian images and makes a quantitative zero-census assertion not supplied by that characterization. Heittokangas and Wen (2019), arXiv:1908.09491v1, discuss the classical Langer bounded-error zero-counting law for exponential sums. **That multiplicity-weighted leading law is prior work**, not claimed as an independent discovery. The contribution here is the exact odd-over-even and coefficient-balance test for *all* multiple Gabor zeros, their explicit locations, and the rational-denominator loss in the **distinct** planar-zero density. Gröchenig, Jaming and Malinnikova (2018), arXiv:1811.03937v1, establish qualitative zero-free criteria, not the present singular density stratification.

## Limitations

The classification applies only to sums of three centered real Gaussians with distinct widths, positive coefficients, and the Gaussian analysis window. It does not include translated/chirped pulses, signed or complex coefficients, more scales, or a parameter-uniform error. The universal total counting law is a consequence of established exponential-sum theory and is proved here only to support the new distinct-zero statement. The proposed novelty is qualified: an equivalent arithmetic multiple-zero calculation could exist in incompletely indexed literature, and no independent audit has yet been performed.

## References

1. Z.-M. Zhang, *Generating superposition and entanglement of squeezed vacuum states*, arXiv:quant-ph/0604128v1 (18 April 2006), https://arxiv.org/pdf/quant-ph/0604128.
2. M. Cappiello, L. Rodino and J. Toft, *Radial symmetric elements and the Bargmann transform*, arXiv:1403.4474v1 (18 March 2014), https://arxiv.org/pdf/1403.4474.
3. J. Heittokangas and Z.-T. Wen, *The asymptotic number of zeros of exponential sums in critical strips*, arXiv:1908.09491v1 (26 August 2019), https://arxiv.org/pdf/1908.09491. The paper reports R. E. Langer's 1931 bounded-error theorem.
4. K. Gröchenig, P. Jaming and E. Malinnikova, *Zeros of the Wigner Distribution and the Short-Time Fourier Transform*, arXiv:1811.03937v1 (9 November 2018), https://arxiv.org/pdf/1811.03937.
