# All-order Laguerre fold diagram for zeros of two-Hermite short-time Fourier transforms

## Finding

Let \(n\geq1\) be an integer and \(t>0\). For the normalized real Hermite functions \(h_n\), the signal \(f=h_n\), and the analysis window \(g_t=h_0+t h_n\), consider the short-time Fourier transform \(V_{g_t}f\). Put \(z=\sqrt\pi(q-i\omega)=re^{i\theta}\) and \(s=r^2\). Up to a nowhere-zero Gaussian and phase factor, the transform is
\[
P_{n,t}(z)=\frac{z^n}{\sqrt{n!}}+tL_n(|z|^2),\qquad L_n(s)=\sum_{j=0}^n\frac{(-1)^j}{j!}\binom nj s^j.
\]
Every zero is isolated and belongs to one of the \(2n\) rays \(\theta=k\pi/n\), where \(k=0,\ldots,2n-1\); there are no zeros at the origin.

Write the simple positive roots of \(L_n\) as \(0<\lambda_1<\cdots<\lambda_n\). For each \(j=1,\ldots,n-1\) there is a **unique** point \(\beta_j\in(\lambda_j,\lambda_{j+1})\) satisfying
\[
2\beta_j L_n'(\beta_j)-nL_n(\beta_j)=0,
\]
and the positive threshold is
\[
\tau_j=\frac{\beta_j^{n/2}}{\sqrt{n!}\,|L_n(\beta_j)|}.
\]
The number of distinct real time-frequency zeros, including every parameter at which thresholds coincide, is exactly
\[
\boxed{N_n(t)=2n+n\sum_{j=1}^{n-1}\Big(2\mathbf1_{\{t>\tau_j\}}+\mathbf1_{\{t=\tau_j\}}\Big).}
\]
Thus \(N_n(t)=2n\) at all sufficiently small positive amplitudes and \(N_n(t)=2n^2\) at all sufficiently large amplitudes. Every intermediate gap contributes either zero, \(n\), or \(2n\) nodes as its amplitude crosses its own threshold. If several thresholds coincide, their contributions add without intersections because they occupy disjoint radial intervals.

At noncritical amplitudes every zero is regular with local topological index \(+1\) or \(-1\), and exactly half the nodes have each index (in either consistent orientation). At each threshold \(\tau_j\), the \(n\) nodes on the corresponding gap are nondegenerate real-map folds: the real Jacobian has rank one, and their local index is zero. They split into two nondegenerate nodes of opposite index as \(t\) increases through the threshold. For \(n=2\) the unique threshold is exactly \((1+\sqrt2)/2\), giving counts \(4\), \(6\), and \(8\) below, at, and above it.

## Assumptions and scope

The Hermite normalization is \(h_0(x)=2^{1/4}e^{-\pi x^2}\) and \(h_n(x)=H_n(\sqrt{2\pi}x)h_0(x)/\sqrt{2^n n!}\), where \(H_n\) is the physicists' Hermite polynomial. The transform convention is
\[
V_gf(q,\omega)=\int_{\mathbb R}f(x)\overline{g(x-q)}e^{-2\pi i\omega x}\,dx.
\]
The amplitudes are strictly positive and real; arbitrary complex amplitudes, combinations of more than two Hermite windows, and noise-contaminated spectrograms are not classified. All counts are of distinct points in the full real \((q,\omega)\)-plane, not algebraic multiplicities. The thresholds need not be asserted pairwise distinct. Topological indices in the proof use the oriented complex \(z\)-plane; reversing the frequency axis reverses all index signs but not their equal populations.

## Proof

**1. Exact transform and angular restriction.** The standard Hermite cross-STFT identities, with \(z=\sqrt\pi(q-i\omega)\), read
\[
V_{h_0}h_n=e^{-\pi i q\omega}e^{-\pi(q^2+\omega^2)/2}\frac{z^n}{\sqrt{n!}},\qquad
V_{h_n}h_n=e^{-\pi i q\omega}e^{-\pi(q^2+\omega^2)/2}L_n(|z|^2).
\]
These follow, for example, by substituting the Hermite generating function into the Gaussian defining integral and equating coefficients; they also agree with the general complex-Hermite identities in the cited literature. Linearity for the real window \(g_t\) proves the stated \(P_{n,t}\). The Gaussian and phase prefactors never vanish. Since \(P_{n,t}(0)=t>0\), the origin is not a zero. For \(r>0\),
\[
\operatorname{Im}P_{n,t}(re^{i\theta})=\frac{r^n}{\sqrt{n!}}\sin(n\theta).
\]
Hence every zero lies on a ray \(\theta=k\pi/n\). On that ray write \(\sigma=(-1)^k\), so the radial equation is
\[
R_n(s)=-\frac{\sigma}{t\sqrt{n!}},\qquad R_n(s)=s^{-n/2}L_n(s),\quad s>0.
\]

**2. Exact number and nondegeneracy of radial extrema.** Classical positive-weight Laguerre orthogonality gives exactly \(n\) simple roots \(\lambda_1,\ldots,\lambda_n\) in \((0,\infty)\). Since \(R_n\) vanishes at every root, Rolle's theorem gives at least one critical point inside each of the \(n-1\) gaps. But
\[
R_n'(s)=\frac{H_n^*(s)}{2s^{n/2+1}},\qquad H_n^*(s)=2sL_n'(s)-nL_n(s).
\]
Here \(H_n^*\) is a degree-\(n\) polynomial, with \(H_n^*(0)=-n<0\) and leading coefficient \(n(-1)^n/n!\). Thus \(H_n^*(s)\to+\infty\) as \(s\to-\infty\), giving a negative real root by continuity. Together with the \(n-1\) distinct positive roots supplied by Rolle's theorem, these exhaust the degree and hence are all simple; in particular **there is exactly one positive critical point in each Laguerre gap and none elsewhere**. A direct additional identity, obtained from the Laguerre differential equation, is
\[
sR_n''+(n+1-s)R_n'+\left(\frac{n^2}{4s}+\frac n2\right)R_n=0.
\]
At each positive critical point, \(R_n\neq0\) and \(R_n''\neq0\); its sign is \(-\operatorname{sgn}R_n\). Thus the stationary value is a strict positive maximum or a strict negative minimum according to the alternating sign of \(L_n\) in that gap.

**3. Exhaustive root counts.** On \((0,\lambda_1)\), \(R_n\) decreases monotonically from \(+\infty\) to zero. On \((\lambda_n,\infty)\), it moves monotonically from zero toward infinity of sign \((-1)^n\). Each outer interval contributes one solution on exactly \(n\) of the \(2n\) rays: altogether \(2n\) simple zeros for every \(t>0\). In the inner gap \((\lambda_j,\lambda_{j+1})\), \(R_n\) has sign \((-1)^j\), vanishes at both endpoints, and has the unique nondegenerate extremum \(\beta_j\). Only those \(n\) rays with \(\sigma=(-1)^{j+1}\) can meet the radial equation. The target level has magnitude \(1/(t\sqrt{n!})\); comparing it to the absolute extremal height \(|R_n(\beta_j)|\) gives respectively zero, one tangent, or two solutions per matching ray when \(t<\tau_j\), \(t=\tau_j\), or \(t>\tau_j\). Distinct radial intervals preclude collisions between different gap contributions, including simultaneous thresholds. This proves the count formula, exhaustiveness, and finiteness.

**4. Charges and fold singularities.** On a zero in the ray \(k\), differentiate the real and imaginary parts in polar coordinates. The oriented real Jacobian in the \(z\)-plane is
\[
J(z)=\det D(\operatorname{Re}P_{n,t},\operatorname{Im}P_{n,t})
=\frac{2nt(-1)^k s^n}{\sqrt{n!}}R_n'(s).
\]
Thus all noncritical zeros are regular and have index \(\operatorname{sgn}J\). In the first outer interval the index is positive; in the last it is negative; there are \(n\) of each. In every inner gap with two radial solutions, \(R_n'\) changes sign once, so the corresponding two nodes on each ray have opposite indices. At its threshold \(R_n'=0\) but \(R_n''\neq0\); the angular derivative \(\partial_\theta\operatorname{Im}P=n(-1)^k s^{n/2}/\sqrt{n!}\) is nonzero, and the second radial derivative of the real part is \(4t s^{n/2+1}R_n''\neq0\). The implicit function theorem and one-variable Morse lemma give a nondegenerate fold with local degree zero, splitting into opposite-sign zeros on the two-root side. No other singular zero is possible.

**5. Exact two-mode illustration.** For \(n=2\), \(L_2(s)=1-2s+s^2/2\), and \(H_2^*(s)=s^2-2\). The unique positive critical point is \(\beta_1=\sqrt2\), so \(\tau_1=1/(2(\sqrt2-1))=(1+\sqrt2)/2\). The general count formula gives \(4\), \(6\), and \(8\), including exactly two fold nodes at equality.

## Verification

The standalone script `verify_all_orders.py` checks the differential identity symbolically for all integer degrees from one through twelve; uses exact polynomial real-root isolation to check the interlacing statement for those degrees; independently evaluates ten defining STFT integrals for five distinct Hermite orders; and checks the two-mode threshold and finite examples up to degree seven. The largest high-precision defining-integral discrepancy was less than \(10^{-45}\). Run `python verify_all_orders.py` with Python, SymPy, and mpmath. The script is an independent finite diagnostic; the proof above, not finite extrapolation, establishes the all-orders theorem. The output is recorded in `checker_output.txt`.

## Relationship to prior work

The Hermite cross-STFT/complex-Hermite polynomial formulas and the polyanalytic Bargmann framework are established in Abreu (2009), Gröchenig–Jaming–Malinnikova (2018/2019), and later sources including the 2026 Hermite-spectrogram treatment. The novelty claimed here is **not** the complex-Hermite formula or positivity of Laguerre roots, but the exact all-order amplitude-dependent \(2n\)-through-\(2n^2\) nodal count, all fold thresholds, and signed-index cancellation, obtained by studying \(L_n(s)/s^{n/2}\). Sète and Zur address generic polyanalytic-polynomial zeros rather than this constrained Hermite STFT family. None of the inspected statements gives the threshold formula or implies it without the radial interlacing argument. Related general polynomial-zero and Wigner-state results do not yield this cross-STFT classification.

## Limitations

No assertion is made that different radial-gap threshold values are distinct; coincidences are handled additively. The statement covers only the indicated positive real two-Hermite windows and prescribed Hermite input. It does not characterize the zero loci of arbitrary polyanalytic STFTs, imply a general upper bound for them, or establish publication priority against every historical special-function or time-frequency treatment. The original transformed polynomial formula is established literature; it is used as a premise, not presented as a new identity.

## References

- L. D. Abreu, *Sampling and interpolation in Bargmann-Fock spaces of polyanalytic functions*, arXiv:0901.4386, first posted 28 January 2009, especially §§2–3; https://arxiv.org/abs/0901.4386.
- K. Gröchenig, P. Jaming, E. Malinnikova, *Zeros of the Wigner distribution and the short-time Fourier transform*, arXiv:1811.03937, especially §6 and equation (26); https://arxiv.org/abs/1811.03937.
- O. Sète and R. Zur, *On the zeros of polyanalytic polynomials*, arXiv:2403.04591, especially the zero-count discussion; https://arxiv.org/abs/2403.04591.
- *Zeros of the Spectrogram of White Noise with Hermite Windows*, arXiv:2610.13531, especially Proposition 2.2 for the complex-Hermite STFT and the later random zero sections; https://arxiv.org/abs/2610.13531.
- NIST Digital Library of Mathematical Functions, §18.2(vi) and §18.16(iv), orthogonal-polynomial zero simplicity and Laguerre roots; https://dlmf.nist.gov/18.2.
